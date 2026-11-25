"""Run the AI-free course image through a real notebook, local Cairn and local Git host."""
import argparse
import base64
from contextlib import ExitStack
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

from playwright.sync_api import expect, sync_playwright

from build import IDE, WAYPOINT, export

CAIRN = "a3b624b8e0b81efce0fbe2e4e54a48df2ea96569"
WORKSPACE = "/home/learner/work"


def create_assignment(course, browser, profile, url):
    from info511_demo import req

    revision = course.start()
    teacher, _ = course.login(browser, "teacher", "/auth/login")
    cid = req(course, teacher, "POST", "/classrooms", {
        "name": "Disposable AI-free INFO 511 test", "host": "forgejo",
        "host_namespace": "course-test", "join_policy": "roster"
    }, 201)["id"]
    req(course, teacher, "POST", f"/classrooms/{cid}/roster", {"username": "alice"}, 201)
    aid = req(course, teacher, "POST", f"/classrooms/{cid}/assignments", {
        "title": profile.title, "slug": profile.task, "type": "individual",
        "grading_spec": "grading.json", "template": {"namespace": "course-test", "name": "template", "ref": revision}
    }, 201)["id"]
    req(course, teacher, "PATCH", f"/assignments/{aid}/grading-policy", {
        "template_commit": revision, "grading_spec": "grading.json"
    })
    teacher.close()
    course.env.update(CAIRN_SUBMISSIONS="true", CAIRN_SUBMISSION_CLASSROOMS=cid,
                      CAIRN_WORKSPACE_URLS=json.dumps({cid: url}))
    course.restart()
    return aid


def complete_notebook(page, fixture, names):
    """Use synthetic predictions and learner code only after checking the packaged starter."""
    notebook, _, explanation, assistance = names
    reference = json.loads((fixture / notebook).read_bytes())
    edits = {c["id"]: "".join(c["source"]) for c in reference["cells"]
             if c["id"] in ("schema-prediction", "unit-prediction", "learner-work")}
    page.wait_for_function("""() => window.jupyterapp?.shell.currentWidget?.content?.widgets
        ?.some(w => w.model.id === 'learner-work')""", timeout=90000)
    page.evaluate("""async edits => {
        const app = window.jupyterapp, panel = app.shell.currentWidget;
        const cells = Object.fromEntries(panel.content.widgets.map(w => [w.model.id, w.model.sharedModel]));
        if (!cells['task-instructions'].getSource().includes('Math inspector')
            || !cells['unit-prediction'].getSource().includes('REPLACE_ME')
            || !cells['schema-prediction'].getSource().includes('REPLACE_ME')
            || !cells['learner-work'].getSource().startsWith('# Write your')) {
            throw Error('Expected an uncompleted AI-free starter');
        }
        for (const [id, source] of Object.entries(edits)) cells[id].setSource(source);
        await panel.sessionContext.ready;
        await app.commands.execute('notebook:run-all-cells');
    }""", edits)
    page.wait_for_function("""() => {
        const cells = window.jupyterapp.shell.currentWidget.content.widgets.filter(w => w.model.type === 'code');
        return cells.length === 2 && cells.every(w => Number.isInteger(w.model.executionCount));
    }""", timeout=90000)
    page.evaluate("""async files => {
        const app = window.jupyterapp;
        await app.commands.execute('docmanager:save');
        for (const [name, content] of Object.entries(files)) {
            await app.serviceManager.contents.save(name, {type:'file', format:'text', content});
        }
    }""", {n: (fixture / n).read_text() for n in (explanation, assistance)})
    return edits


def submit(page, context, course, item, files):
    from info511_demo import req

    with page.expect_popup() as tab:
        page.get_by_role("link", name="Submit saved files to Cairn", exact=True).click()
    picker = tab.value
    for name in files:
        picker.get_by_role("checkbox", name=name, exact=False).check()
    picker.get_by_role("button", name="Prepare saved files", exact=True).click()
    with context.expect_page() as tab:
        picker.get_by_role("button", name="Continue in Cairn", exact=True).click()
    receiver = tab.value
    sid = item["submission_id"]
    receiver.get_by_label("Assignment", exact=True).select_option(sid)
    receiver.get_by_role("button", name="Receive saved files from Waypoint", exact=True).click()
    expect(receiver.locator("#bridge-status")).to_contain_text("Nothing has been submitted yet.")
    endpoint = f"/me/work/{sid}/submission-receipts"
    assert req(course, context, "GET", endpoint)["receipts"] == []
    with receiver.expect_response(lambda r: r.url.endswith("/submission-previews") and r.request.method == "POST") as res:
        receiver.get_by_role("button", name="Review saved files", exact=True).click()
    assert res.value.status == 201
    preview = res.value.json()
    expected = [{"path": name, "action": "create", "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
                for name, raw in sorted(files.items())]
    assert preview["status"] == "preview" and preview["changes"] == expected
    assert all(row["status"] != "committed" for row in req(course, context, "GET", endpoint)["receipts"])
    receiver.get_by_role("button", name="Confirm submission", exact=True).click()
    expect(receiver.get_by_text("Submission received", exact=True)).to_be_visible(timeout=90000)
    receipt = req(course, context, "GET", endpoint + "/" + preview["id"])
    assert receipt["status"] == "committed" and receipt["changes"] == expected
    return {"id": preview["id"], "commit": receipt["commit_revision"], "changes": expected, "checks": []}


def rehearse(args, root):
    sources = root / "sources"
    sources.mkdir()
    export(args.waypoint, WAYPOINT, ["course-workspace"], sources)
    export(args.ide, IDE, ["integrations/waypoint"], sources)
    cairn_source = sources / "cairn"
    cairn_source.mkdir()
    export(args.cairn, CAIRN, [], cairn_source)
    workspace = sources / "course-workspace"
    sys.path[:0] = [str(workspace / p) for p in ("classroom", "course", "rehearsal")]
    sys.path.insert(0, str(sources / "integrations/waypoint"))
    from assignment_profiles import NHANES
    from cairn_journey import Course, FORGEJO_IMAGE, port, wait_http
    from image_smoke import RELAY, docker
    from info511_demo import active_work, await_grade
    from info511_policy import template_files
    from submission_handoff import verify_receipt_after_restart

    image = docker("image", "inspect", "-f", "{{.Id}}", args.image)
    checkout = docker("image", "inspect", "-f", "{{.Id}}", args.checkout_image)
    forge = docker("image", "inspect", "-f", "{{.Id}}", FORGEJO_IMAGE)
    policy = template_files(args.checker_source, image, profile=NHANES)
    binary = root / "cairn"
    subprocess.run(["go", "build", "-o", binary, "./cmd/cairn"], cwd=cairn_source, check=True)
    origin = "http://127.0.0.1:" + str(port())
    name = "journey-" + secrets.token_hex(6)
    token = secrets.token_urlsafe(32)
    with ExitStack() as clean:
        network = docker("network", "create", "--internal", name)
        clean.callback(docker, "network", "rm", network)
        editor = docker("run", "-d", "--pull=never", "--network", network, "--name", name,
                        "-e", "JUPYTER_TOKEN=" + token, "-e", "WORKSPACE_CAIRN_ORIGIN=" + origin,
                        "-e", "WORKSPACE_CAIRN_LOCAL_TEST=1", image, "jupyter", "lab", "--no-browser",
                        "--ip=0.0.0.0", "--port=8888",
                        "--LabApp.expose_app_in_browser=True")
        clean.callback(docker, "rm", "-fv", editor)
        relay = docker("run", "-d", "--pull=never", "-p", "127.0.0.1::8888", image, "python", "-c", RELAY, name)
        clean.callback(docker, "rm", "-fv", relay)
        docker("network", "connect", network, relay)
        url = "http://" + docker("port", relay, "8888/tcp")
        wait_http(url + "/api/status?token=" + token)
        course_dir = root / "course"
        course_dir.mkdir()
        course = Course(course_dir, binary, url, image, cairn_source, cairn_origin=origin,
                        template_files=policy, checkout_image=checkout, distinct_learner_passwords=True)
        clean.callback(course.close)
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            aid = create_assignment(course, browser, NHANES, url)
            learner, _ = course.login(browser, "alice", f"/assignments/{aid}/accept")
            item = active_work(course, learner, profile=NHANES)
            origins = {urlsplit(base).netloc for base in (url, course.url, course.forge)}
            learner.route("**/*", lambda route: route.continue_() if urlsplit(route.request.url).netloc in origins else route.abort())
            page = learner.new_page()
            page.goto(url + "/lab/tree/" + NHANES.files[0] + "?token=" + token)
            edits = complete_notebook(page, NHANES.package / "operator/attempts/alice", NHANES.files)
            files = {}
            for name in NHANES.files:
                docker("cp", f"{editor}:{WORKSPACE}/{name}", str(root / name))
                files[name] = (root / name).read_bytes()
            saved = json.loads(files[NHANES.files[0]])
            cells = {cell["id"]: cell for cell in saved["cells"]}
            assert all("".join(cells[key]["source"]) == source for key, source in edits.items())
            assert all(isinstance(c["execution_count"], int) and not any(o["output_type"] == "error" for o in c["outputs"])
                       for c in cells.values() if c["cell_type"] == "code")
            records = list(csv.DictReader(io.StringIO(files[NHANES.files[1]].decode())))
            assert len(records) == 192 and tuple(records[0]) == NHANES.csv_header
            receipt = submit(page, learner, course, item, files)
            grade = await_grade(course, learner, item["submission_id"], receipt["commit"], profile=NHANES)
            repository = item["repo_web_url"].removeprefix(course.forge + "/")
            for name, raw in files.items():
                data = course.api("GET", f"/repos/{repository}/contents/{name}?ref=" + receipt["commit"], user="alice")
                assert base64.b64decode(data["content"]) == raw
            course.restart()
            fresh, _ = course.login(browser, "alice", "/student/login?host=forgejo")
            verify_receipt_after_restart(course, fresh, item["submission_id"], receipt)
            browser.close()
    return {
        "scope": "Disposable synthetic learner on local Docker, Cairn and Forgejo",
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "waypoint": WAYPOINT, "ide": IDE, "cairn": CAIRN, "course_and_grader_image": image,
        "checkout_image": checkout, "forgejo_image": forge, "assignment": NHANES.task,
        "jupyter_root": WORKSPACE, "starter_predictions_and_code_saved": True, "kernel": "Python", "executed_code_cells": 2,
        "generated_csv_rows": len(records), "explicit_preview_and_confirmation": True,
        "files_read_back_byte_exactly": sorted(files), "receipt_survived_cairn_restart": True,
        "csv_correctness_points": [grade["grade"]["score"], grade["grade"]["max_score"]],
        "owned_services_cleaned_up": True
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("waypoint", "ide", "cairn", "checker-source"):
        parser.add_argument("--" + name, required=True, type=lambda s: Path(s).resolve())
    parser.add_argument("--image", default="educloud-info511:ai-free")
    parser.add_argument("--checkout-image", required=True)
    parser.add_argument("--output", type=Path, help="Write the sanitized result after successful cleanup.")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="educloud-journey-") as tmp:
        result = rehearse(args, Path(tmp))
    summary = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(summary)
    print(summary, end="")
