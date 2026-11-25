"""Exercise AI-free classroom notebooks on a disposable, local-engine JupyterHub."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import sys
import tempfile
from textwrap import indent
import time

import requests

from build import WAYPOINT, export

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from rehearse import cleanup, owned, require, run, wait_hub


def memory_available(image):
    info = run("docker", "run", "--rm", "--pull=never", "--network=none", "--memory=32m",
               "--entrypoint", "cat", image, "/proc/meminfo")
    return int(re.search(r"^MemAvailable:\s+(\d+) kB$", info, re.M)[1]) // 1024


def parallel(function, items, workers):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(function, items))


def temporary_roster(config, users):
    # The pinned local-test Hub checks its two sample accounts at login and spawn.
    lines = config.splitlines(keepends=True)
    sample = "{'alice', 'bob'}"
    for prefix in ("    c.DummyAuthenticator.allowed_users = ",
                   "    allowed = s['subjects'] if s['mode'] == 'oidc' else "):
        old = prefix + sample + "\n"
        require(lines.count(old) == 1, "Pinned synthetic roster definition changed")
        lines[lines.index(old)] = prefix + "{" + ", ".join(map(repr, users)) + "}" + "\n"
    return "".join(lines)


def benchmark(args, root, instance, hub, course):
    fixture = "course-workspace/classroom/info511-nhanes-v1/operator/attempts/alice/nhanes-wrangling.ipynb"
    export(args.waypoint, WAYPOINT, ["course-workspace/smoke.py", "course-workspace/hub/jupyterhub_config.py", fixture], root)
    workspace = root / "course-workspace"
    sys.path.insert(0, str(workspace))
    import smoke
    users = ["instructor"] + [f"learner{i:02}" for i in range(1, args.seats)]
    waiting_user = "nextlearner"
    original = workspace / "hub/jupyterhub_config.py"
    path = "/srv/jupyterhub/jupyterhub_config.py"
    digest = run("docker", "run", "--rm", "--pull=never", "--network=none", "--memory=32m",
                 "--entrypoint", "sha256sum", hub, path).split()[0]
    require(hashlib.sha256(original.read_bytes()).hexdigest() == digest, "Hub config differs from pinned Waypoint source")
    synthetic = root / "capacity_config.py"
    synthetic.write_text(temporary_roster(original.read_text(), [*users, waiting_user]))
    label = "educloud.workspace.instance=" + instance
    name = instance + "-hub"
    password = secrets.token_hex(24)
    env = root / "private.env"
    env.write_text(f"WORKSPACE_TEST_PASSWORD={password}\n")
    edge, data = instance + "-edge", instance + "-hub-data"
    run("docker", "network", "create", "--label", label, edge)
    run("docker", "volume", "create", "--label", label, data)
    run("docker", "run", "-d", "--pull=never", "--name", name, "--network", edge, "--label", label,
        "-p", "127.0.0.1::8000", "--env-file", str(env), "-e", "WORKSPACE_INSTANCE=" + instance,
        "-e", "WORKSPACE_AUTH_MODE=local-test", "-e", "WORKSPACE_PUBLIC_URL=http://127.0.0.1",
        "-e", "WORKSPACE_IMAGE=" + course, "-e", f"WORKSPACE_ACTIVE_LIMIT={len(users)}",
        "-e", f"WORKSPACE_MEMORY_MB={args.memory_mib}", "-e", "WORKSPACE_CPU_LIMIT=1",
        "-v", "/var/run/docker.sock:/var/run/docker.sock", "-v", data + ":/data",
        "-v", f"{synthetic}:/srv/jupyterhub/capacity_config.py:ro", "--memory=512m", "--cpus=1",
        hub, "jupyterhub", "-f", "/srv/jupyterhub/capacity_config.py")
    address = run("docker", "port", name, "8000/tcp")
    require(re.fullmatch(r"127\.0\.0\.1:\d+", address), "Expected loopback-only rehearsal")
    base = "http://" + address
    wait_hub(base)

    def sign_in(user):
        return user, smoke.login(base, user, password)

    def file_url(user, filename):
        return f"{base}/user/{user}/api/contents/{filename}"

    def read(user, filename):
        response = sessions[user].get(file_url(user, filename), timeout=10)
        response.raise_for_status()
        return response.json()["content"]

    started = time.monotonic()
    sessions = dict(parallel(sign_in, users, 2))
    ready_seconds = round(time.monotonic() - started, 2)
    cells = {c["id"]: "".join(c["source"]) for c in json.loads((root / fixture).read_text())["cells"]
             if c["cell_type"] == "code"}
    cell = (cells["load-input"] + "\n\ndef rehearse_fixture():\n" + indent(cells["learner-work"], "    ")
            + "\n" + (HERE / "capacity_cell.py").read_text())

    def execute(user):
        # Keep kernel and coordinator HTTP cookies independent across threads.
        with requests.Session() as session:
            session.cookies.update(sessions[user].cookies)
            smoke.kernel(session, base, user, "python3", f"seat = {user!r}\n" + cell)

    def release(user):
        smoke.change(sessions[user], "PUT", file_url(user, "capacity-start.txt"),
                     json={"type": "file", "format": "text", "content": str(target)}).raise_for_status()

    with ThreadPoolExecutor(max_workers=len(users)) as pool:
        futures = [pool.submit(execute, u) for u in users]
        remaining = set(users)
        deadline = time.monotonic() + 30
        while remaining:
            for f in futures:
                if f.done():
                    f.result()
            for user in remaining.copy():
                response = sessions[user].get(file_url(user, "capacity-ready.txt"), timeout=3)
                if response.status_code == 200 and response.json()["content"] == "ready":
                    remaining.remove(user)
                elif response.status_code != 404:
                    response.raise_for_status()
            require(time.monotonic() < deadline, "Kernels did not become ready together")
            if remaining:
                time.sleep(.1)
        target = time.time() + 2
        parallel(release, users, len(users))
        for f in futures:
            f.result()

    def files(user):
        result = json.loads(read(user, "capacity-result.json"))
        require(result["seat"] == user and result["rows"] == 192, "Unexpected seat output")
        csv = read(user, "tidy-nhanes.csv")
        require(len(csv.splitlines()) == 193, "Unexpected tidy CSV rows")
        return result, hashlib.sha256(csv.encode()).hexdigest()

    before = {u: files(u) for u in users}
    durations = [row["ended"] - row["started"] for row, _ in before.values()]
    overlap = min(row["ended"] for row, _ in before.values()) - max(row["started"] for row, _ in before.values())
    require(overlap > 0, "No common interval of measured notebook work")
    seats = run("docker", "ps", "-q", "--filter", "label=" + label, "--filter", "label=educloud.workspace.kind=learner").split()
    require(len(seats) == len(users), "Unexpected number of live notebook servers")
    homes, networks, peak = set(), set(), []
    for cid in seats:
        c = json.loads(run("docker", "inspect", cid))[0]
        limits = c["HostConfig"]
        require(limits["Memory"] == limits["MemorySwap"] == args.memory_mib * 1024**2 and
                limits["CpuPeriod"] == limits["CpuQuota"] > 0, "Notebook limits differ")
        network, = c["NetworkSettings"]["Networks"]
        networks.add(network)
        home, = [m["Name"] for m in c["Mounts"] if m["Destination"] == "/home/learner"]
        homes.add(home)
        memory = run("docker", "exec", cid, "cat", "/sys/fs/cgroup/memory.peak", "/sys/fs/cgroup/memory.events").splitlines()
        require("oom_kill 0" in memory, "A notebook hit the OOM killer")
        peak.append(int(memory[0]) / 1024**2)
    require(len(homes) == len(networks) == len(users), "Expected an individual home and network for every seat")
    # Ask for another active seat's real, already-verified result via its normal Contents route.
    cross_read = sessions[users[-1]].get(file_url(users[0], "capacity-result.json"), timeout=10)
    require(cross_read.status_code in (403, 404), "A peer's saved result must be private")

    def active_containers():
        return set(owned("container", instance))

    def stop(user, session):
        smoke.change(session, "DELETE", f"{base}/hub/api/users/{user}/server").raise_for_status()
        session.close()

    def wait_count(count):
        for _ in range(60):
            if len(active_containers()) == count + 1:  # Include the Hub.
                return
            time.sleep(1)
        raise RuntimeError("Notebook server count did not settle")

    # Authenticate the next rostered learner without following a sign-in redirect
    # that may itself start a server. Both admissions use this same Hub session.
    initial = active_containers()
    with requests.Session() as waiting:
        login_url = base + "/hub/login"
        waiting.get(login_url, timeout=10).raise_for_status()
        response = waiting.post(login_url, data={"username": waiting_user, "password": password,
                                "_xsrf": smoke.xsrf(waiting, login_url)}, allow_redirects=False, timeout=10)
        require(response.is_redirect, "Expected successful Hub sign-in")
        identity = waiting.get(base + "/hub/api/user", timeout=10)
        identity.raise_for_status()
        require(identity.json()["name"] == waiting_user, "Extra learner was not authenticated")
        spawn_url = f"{base}/hub/api/users/{waiting_user}/server"
        full = smoke.change(waiting, "POST", spawn_url)
        require(full.status_code == 429 and "active user limit exceeded" in full.text.lower(),
                "Expected active-seat limit response")
        require(active_containers() == initial, "A blocked arrival changed the active servers")

        stop(users[-1], sessions[users[-1]])
        wait_count(len(users) - 1)
        remaining_containers = active_containers()
        admitted = smoke.change(waiting, "POST", spawn_url)
        require(admitted.status_code in (201, 202), "Released seat did not admit the waiting learner")
        for _ in range(60):
            waiting.get(f"{base}/user/{waiting_user}/lab", timeout=10)
            ready = waiting.get(file_url(waiting_user, "nhanes-wrangling.ipynb"), timeout=10)
            if ready.status_code == 200 and "application/json" in ready.headers.get("Content-Type", ""):
                require(ready.json()["type"] == "notebook", "Waiting learner did not reach the assignment")
                break
            time.sleep(1)
        else:
            raise RuntimeError("Newly admitted learner did not reach the assignment")
        current = active_containers()
        require(remaining_containers < current and len(current) == len(initial),
                "Seat handoff replaced an unrelated notebook or exceeded capacity")
        for u in users[:-1]:
            require(files(u) == before[u], "Seat handoff interrupted another learner's saved work")
        stop(waiting_user, waiting)
    for u in users[:-1]:
        stop(u, sessions[u])
    wait_count(0)
    sessions = dict(parallel(sign_in, users, 2))
    for u in users:
        require(files(u) == before[u], "Saved outputs differ after server replacement")
        sessions[u].close()
    return dict(seats=len(users), instructor_notebooks=1, learner_notebooks=len(users)-1,
                distinct_homes=len(homes), distinct_networks=len(networks), saved_outputs_restored=len(users),
                cross_seat_read_http=cross_read.status_code, full_classroom_spawn_http=full.status_code,
                waiting_learner_admitted_after_release=True, continuing_seats_verified=len(users)-1,
                cpu_per_seat=1, memory_limit_mib_per_seat=args.memory_mib, all_servers_ready_seconds=ready_seconds,
                joins_and_reshapes_per_seat=30, output_rows_per_seat=192,
                workload_seconds_range=[round(min(durations), 3), round(max(durations), 3)],
                all_seat_workload_overlap_seconds=round(overlap, 3),
                cgroup_peak_mib_per_seat_range=[round(min(peak), 1), round(max(peak), 1)], notebook_oom_kills=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--waypoint", type=Path, required=True)
    parser.add_argument("--hub-image", required=True)
    parser.add_argument("--course-image", default="educloud-info511:ai-free")
    parser.add_argument("--seats", type=int, choices=range(2, 15), default=3)
    parser.add_argument("--memory-mib", type=int, choices=(512, 768, 1024, 2048), default=768)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    endpoint = os.environ.get("DOCKER_HOST") or run("docker", "context", "inspect", "--format", "{{.Endpoints.docker.Host}}")
    require(endpoint.startswith("unix://"), "Run on the intended machine with a local Docker socket")
    hub, course = [run("docker", "image", "inspect", "--format", "{{.Id}}", i)
                   for i in (args.hub_image, args.course_image)]
    available = memory_available(course)
    minimum = args.seats * args.memory_mib + 512 + 1024
    require(available >= minimum, f"Need {minimum} MiB available to Docker before launch; measured {available} MiB")
    instance = "capacity-" + secrets.token_hex(6)
    with tempfile.TemporaryDirectory(prefix="educloud-capacity-") as root:
        try:
            result = benchmark(args, Path(root), instance, hub, course)
        finally:
            cleanup(instance)
    result.update(observed_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
                  docker_os=run("docker", "info", "--format", "{{.OperatingSystem}}"),
                  docker_cpus=int(run("docker", "info", "--format", "{{.NCPU}}")),
                  docker_available_mib_at_start=available, course_image=course, hub_image=hub,
                  waypoint=WAYPOINT, scope="disposable loopback Hub, local-test accounts", cleanup_verified=True)
    encoded = json.dumps(result, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
