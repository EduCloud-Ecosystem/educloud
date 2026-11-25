"""Prove that expiring a scarce CPU job leaves two local Waypoint notebooks usable."""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import sys
import tempfile
import time

import requests


def run(*args):
    return subprocess.check_output(args, text=True, timeout=90).strip()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def owned(kind, instance):
    listing = {"container": ["ps", "-aq"], "network": ["network", "ls", "-q"],
               "volume": ["volume", "ls", "-q"]}[kind]
    return run("docker", *listing, "--filter", f"label=educloud.workspace.instance={instance}").split()


def cleanup(instance):
    for kind in ("container", "network", "volume"):
        for item in owned(kind, instance):
            args = ["docker", kind, "rm"]
            if kind == "container":
                args.append("-f")
            run(*args, item)
    require(all(not owned(k, instance) for k in ("container", "network", "volume")),
            "Disposable classroom still has owned resources")


def wait_hub(base):
    for _ in range(90):
        try:
            if requests.get(base + "/hub/health", timeout=2).status_code == 200:
                return
        except requests.ConnectionError:
            pass
        time.sleep(1)
    raise RuntimeError("Local Hub did not become healthy")


def check_files(sessions, smoke, base, phase):
    for user, session in sessions.items():
        url = f"{base}/user/{user}/api/contents/course-result.txt"
        text = f"{user}-{phase}"
        smoke.change(session, "PUT", url, json={"type": "file", "format": "text", "content": text}).raise_for_status()
        response = session.get(url, timeout=10)
        response.raise_for_status()
        require(response.json()["content"] == text, "Saved learner work differs")


def check_after_restart(sessions, base):
    for user, session in sessions.items():
        url = f"{base}/user/{user}/api/contents/course-result.txt"
        response = session.get(url, timeout=10)
        response.raise_for_status()
        require(response.json()["content"] == f"{user}-after-expiry", "Retained home differs")


def expire_job(args, root, during_job):
    cli = [str(args.outfitter.resolve()), "--state-dir", str(root / "state")]
    project, request = "synthetic-course", "scarce-cpu"
    run(*cli, "project-init", "--project-id", project, "--budget-cpu-seconds", "60")
    for directory in ("input", "recipe"):
        (root / directory).mkdir()
    spec = dict(schema_version=1, request_id=request, project_id=project,
                image=args.job_image, command=["python", "-c", "import time; time.sleep(60)"],
                input_dir=str(root / "input"), recipe_dir=str(root / "recipe"), cpus=1,
                memory_mb=96, pids_limit=32, timeout_seconds=20, max_output_bytes=1024,
                isolation="reviewed-local", allow_supervised_reaper=True)
    path = root / "job.json"
    path.write_text(json.dumps(spec))
    with subprocess.Popen([*cli, "run", "--request", str(path)], stdout=subprocess.DEVNULL) as proc:
        try:
            for _ in range(80):
                if proc.poll() is not None:
                    raise RuntimeError("CPU job finished before the classroom probe")
                status = subprocess.run([*cli, "status", "--request-id", request], capture_output=True,
                                        text=True, timeout=5)
                if status.returncode == 0:
                    row = json.loads(status.stdout)
                    if row["status"] == "running" and row["execution_started"]:
                        break
                time.sleep(.2)
            else:
                raise RuntimeError("CPU job never entered running state")
            deadline = row["deadline"]
            during_job()
            row = json.loads(run(*cli, "status", "--request-id", request))
            require(row["status"] == "running", "Job closed during the active-window control")
            proc.wait(timeout=50)
        finally:
            if proc.poll() is None:
                run(*cli, "cancel", "--request-id", request)
    row = json.loads(run(*cli, "status", "--request-id", request))
    # The CLI and the independent watchdog race to observe the same deadline.
    # Both terminal paths verify release. An ambiguous or early end fails.
    deadline_status = row["status"] in {"failed", "cancelled"} and row["error"] in {
        "execution deadline or cancellation reached", "watchdog deadline, cancellation or broker loss"}
    finished = datetime.fromisoformat(row["finished_at"].replace("Z", "+00:00"))
    require(deadline_status and row["deadline"] == deadline
            and finished >= datetime.fromisoformat(deadline.replace("Z", "+00:00"))
            and row["cleanup_verified"] and not row["unresolved_liability"],
            f"Unexpected terminal CPU receipt: {row['status']} {row['error']}")
    return {key: row[key] for key in ("status", "deadline", "finished_at", "error", "cleanup_verified",
                                      "unresolved_liability", "compute")}


def exercise(args, root, instance):
    sys.path.insert(0, str(args.waypoint.resolve() / "course-workspace"))
    import smoke  # Waypoint's ordinary sign-in, contents and kernel probes.

    password = secrets.token_hex(24)
    volume_label = "educloud.workspace.instance=" + instance
    run("docker", "volume", "create", "--label", volume_label, instance + "-hub-data")
    # Hub and learners must resolve each other on the Hub-created per-user networks.
    # Binding port zero keeps each parallel rehearsal on its own loopback port.
    edge = instance + "-edge"
    run("docker", "network", "create", "--label", volume_label, edge)
    name = instance + "-hub"
    envfile = root / "hub.env"
    with envfile.open("x") as f:
        f.write(f"WORKSPACE_TEST_PASSWORD={password}\n")
    run("docker", "run", "--detach", "--pull=never", "--name", name, "--network", edge, "--label", volume_label,
        "--publish", "127.0.0.1::8000", "--env-file", str(envfile),
        "-e", "WORKSPACE_INSTANCE=" + instance, "-e", "WORKSPACE_AUTH_MODE=local-test",
        "-e", "WORKSPACE_PUBLIC_URL=http://127.0.0.1", "-e", "WORKSPACE_IMAGE=" + args.course_image,
        "-e", "WORKSPACE_ACTIVE_LIMIT=2", "-e", "WORKSPACE_MEMORY_MB=768", "-e", "WORKSPACE_CPU_LIMIT=1",
        "-v", "/var/run/docker.sock:/var/run/docker.sock", "-v", instance + "-hub-data:/data",
        "--memory=1g", "--cpus=1", args.hub_image)
    def connect():
        address = run("docker", "port", name, "8000/tcp")
        require(re.fullmatch(r"127\.0\.0\.1:[0-9]+", address), "Hub requires loopback")
        base = "http://" + address
        wait_hub(base)
        return base

    base = connect()
    users = ("alice", "bob")

    def sign_in():
        return {u: smoke.login(base, u, password) for u in users}

    sessions = sign_in()
    check_files(sessions, smoke, base, "initial")
    observed = json.loads(run("docker", "inspect", *owned("container", instance)))
    learners = [c for c in observed if c["Config"]["Labels"].get("educloud.workspace.kind") == "learner"]
    require(len(learners) == 2, "Expected two learner containers")
    homes = set()
    networks = set()
    for c in learners:
        limits = c["HostConfig"]
        require(limits["CpuPeriod"] > 0 and limits["CpuQuota"] == limits["CpuPeriod"]
                and limits["Memory"] == 768 * 1024**2, "Learner CPU or RAM limit differs")
        mounts = [m["Name"] for m in c["Mounts"] if m["Destination"] == "/home/learner"]
        require(len(mounts) == 1, "Expected an individual home")
        homes.update(mounts)
        links = c["NetworkSettings"]["Networks"]
        require(len(links) == 1, "Expected one learner network")
        networks.update(links)
    require(len(homes) == len(networks) == 2, "Learners must have distinct homes and networks")
    receipt = expire_job(args, root, lambda: check_files(sessions, smoke, base, "during"))
    check_files(sessions, smoke, base, "after-expiry")
    for user, session in sessions.items():
        smoke.kernel(session, base, user, "python3", "assert sum([2, 3]) == 5; print('CONTINUITY_OK')")
    for user, session in sessions.items():
        smoke.change(session, "DELETE", f"{base}/hub/api/users/{user}/server").raise_for_status()
        session.close()
    for _ in range(60):
        if len(owned("container", instance)) == 1:
            break
        time.sleep(1)
    require(len(owned("container", instance)) == 1, "Learner servers did not stop")
    run("docker", "restart", name)
    base = connect()
    sessions = sign_in()
    check_after_restart(sessions, base)
    for session in sessions.values():
        session.close()
    return {"synthetic_learners": len(users), "cpu_limit_each": 1, "memory_mib_each": 768, "distinct_home_volumes": len(homes),
            "distinct_learner_networks": len(networks), "both_saved_during_lease": True,
            "both_executed_after_expiry": True, "both_recovered_after_hub_restart": True,
            "outfitter_job": receipt}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--waypoint", type=Path, required=True)
    parser.add_argument("--outfitter", type=Path, required=True)
    for flag in ("hub-image", "course-image", "job-image"):
        parser.add_argument("--" + flag, required=True)
    args = parser.parse_args()
    endpoint = os.environ.get("DOCKER_HOST") or run("docker", "context", "inspect", "--format", "{{.Endpoints.docker.Host}}")
    require(endpoint.startswith("unix://"), "Use a local Docker engine")
    for image in (args.hub_image, args.course_image, args.job_image):
        require(re.fullmatch(r"sha256:[0-9a-f]{64}", image) and
                run("docker", "image", "inspect", "--format", "{{.Id}}", image) == image,
                "Every rehearsal image must be preloaded and immutable")
    # Use a private temporary root for the test password and ephemeral broker state.
    instance = "cacao-" + secrets.token_hex(6)
    with tempfile.TemporaryDirectory(prefix="cacaoutfitter-") as directory:
        try:
            result = exercise(args, Path(directory), instance)
        finally:
            cleanup(instance)
    result.update(cleanup_verified=True, hub_image=args.hub_image, course_image=args.course_image,
                  job_image=args.job_image, broker_sha256=hashlib.sha256(args.outfitter.read_bytes()).hexdigest())
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
