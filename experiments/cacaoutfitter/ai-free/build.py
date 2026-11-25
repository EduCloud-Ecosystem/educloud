"""Build the AI-free Waypoint course image from exact source revisions (Python 3.12+)."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile

WAYPOINT = "af44909f8a0757b1f15c35d74414a7d47f559a39"
IDE = "b95a3d65bb01c996c126d70dc5042008d112d274"
PACK = "course-workspace/classroom/info511-nhanes-v1/learner"


def export(repo, revision, paths, destination):
    archive = destination / "source.tar"
    subprocess.run(["git", "-C", repo, "archive", "--output", archive, revision, *paths], check=True)
    with tarfile.open(archive) as tree:
        tree.extractall(destination, filter="data")
    archive.unlink()


def build(args, root):
    context = root / "course-image"
    context.mkdir()
    export(args.waypoint, WAYPOINT, ["course-workspace/course", PACK], root)
    export(args.ide, IDE, ["integrations/math-inspector", "integrations/notebook-labs/marimo", "LICENSE"], root)
    bundled = root / "package"
    subprocess.run([sys.executable, root / "integrations/math-inspector/build.py", bundled], check=True,
                   env={**os.environ, "SOURCE_DATE_EPOCH": "1795478400"})
    wheel, = bundled.glob("*.whl")
    shutil.copy2(wheel, context)
    shutil.copy2(Path(__file__).with_name("Dockerfile"), context)
    shutil.copytree(root / PACK, context / "learner")
    path = context / "learner/nhanes-wrangling.ipynb"
    notebook = json.loads(path.read_text())
    instructions, = [c for c in notebook["cells"] if c["id"] == "task-instructions"]
    lead, tutoring, _ = "".join(instructions["source"]).partition("For an optional hint,")
    if not tutoring:
        raise ValueError("Expected pinned starter instructions")
    instructions["source"] = (lead + "The Math inspector offers instructor-written concept notes. Select a join or reshape in your code, or a prediction cell. You can edit, run, save and submit with the panel closed.\n").splitlines(True)
    path.write_text(json.dumps(notebook, indent=1) + "\n")
    readme = context / "learner/README.md"
    guide = readme.read_text()
    start = guide.index("Predict the input/joined/output schemas")
    end = guide.index("## Task", start)
    readme.write_text(guide[:start] + "Predict the columns and observational units in the labeled cells. "
                      "The Math inspector offers course-authored conceptual questions. This edition "
                      "runs without generative AI. Use the assignment disclosure field to describe "
                      "how you worked.\n\n" + guide[end:])
    base = "educloud-waypoint-course:" + WAYPOINT[:12]
    subprocess.run(["docker", "build", "-t", base, root / "course-workspace/course"], check=True)
    subprocess.run(["docker", "build", "--network=none", "--build-arg", "WAYPOINT_BASE=" + base,
                    "-t", args.tag, context], check=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--waypoint", type=Path, required=True)
    ap.add_argument("--ide", type=Path, required=True)
    ap.add_argument("--tag", default="educloud-info511:ai-free")
    args = ap.parse_args()
    with tempfile.TemporaryDirectory() as scratch:
        build(args, Path(scratch))
