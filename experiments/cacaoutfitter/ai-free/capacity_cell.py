"""Executed inside a real Python kernel by capacity.py."""
import json
import time
from pathlib import Path

work = Path("/home/learner/work")
assert (work / "nhanes-wrangling.ipynb").is_file()
(work / "capacity-ready.txt").write_text("ready")
release = work / "capacity-start.txt"
deadline = time.monotonic() + 25
while time.monotonic() < deadline:
    try:
        target = float(release.read_text())
        break
    except (FileNotFoundError, ValueError):
        # Jupyter's contents writer may already have opened the new file.
        time.sleep(.05)
else:
    raise TimeoutError("Cohort did not reach the starting point")
time.sleep(max(0, target - time.time()))
started = time.time()
# Repeat ordinary small-table work long enough to measure overlap across kernels.
for _ in range(30):
    rehearse_fixture()  # Supplied from the pinned operator notebook.
ended = time.time()
rows = len(pd.read_csv(work / "tidy-nhanes.csv"))  # pandas imported by the fixture
assert rows == 192
(work / "capacity-result.json").write_text(json.dumps(dict(
    seat=seat, started=started, ended=ended, rows=rows)))  # seat supplied by capacity.py
print("CONTINUITY_OK")
