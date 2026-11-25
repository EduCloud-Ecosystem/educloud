# Rehearse the saved NHANES assignment

Run this from the AI-free image directory on a machine with Docker, Go, and a Python 3.12+ environment containing Playwright, Chromium and Requests. Build the course image using [the course image instructions](README.md). The runner exports pinned revisions from local checkouts of Waypoint, the IDE and Cairn. Waypoint supplies the instructor's synthetic attempt and grading policy. The separate checker source checkout supplies one deterministic Python file verified against the course's SHA-256 binding. Learners only need their course workspace.

| Source | Tested revision |
| --- | --- |
| Waypoint | `af44909f8a0757b1f15c35d74414a7d47f559a39` |
| EduCloud IDE | `b95a3d65bb01c996c126d70dc5042008d112d274` |
| Cairn | `a3b624b8e0b81efce0fbe2e4e54a48df2ea96569` |
| Belay Classroom (staff-side checker source) | `c5a27073e74b9eeb7ab697190915378b50132883` |

On a cold operator machine, prepare the local Git host and Cairn checkout helper first. The helper image is built from the pinned Cairn checkout. Its resulting ID may vary across platforms and builds. The test records the actual image IDs used.

```sh
docker pull codeberg.org/forgejo/forgejo:16.0.5@sha256:cf5f5ae6acf2ababca0ee3d255705b83a47f35b25e07fc931d694d60664053fe
git -C "$CAIRN_SOURCE" show a3b624b8e0b81efce0fbe2e4e54a48df2ea96569:Dockerfile.checkout |
  docker build -t cairn-checkout:journey -
```

Run with the paths to the local source trees and the checkout helper image tag or ID. To reproduce the recorded machine's image selection, use the image IDs in [the receipt](journey-result.json) as the values for `--image` and `--checkout-image`.

```sh
python journey.py --waypoint "$WAYPOINT_SOURCE" --ide "$IDE_SOURCE" \
  --cairn "$CAIRN_SOURCE" --checker-source "$BELAY_CLASSROOM_SOURCE" \
  --checkout-image cairn-checkout:journey --output journey-result.json
```

The browser opens the blank packaged starter, fills the prediction and code cells using the synthetic fixture, runs both code cells in the course Python kernel and saves the explanation and disclosure. The runner inspects the saved bytes and the CSV's 192 rows. The learner selects four files in Waypoint, reviews Cairn's preview, and confirms submission. The test compares each committed file against the bytes in the workspace, waits for Cairn's four-point CSV correctness check, then restarts Cairn and signs in again to verify the persisted receipt.

The dedicated course image places the NHANES starter directly in its normal workspace root. The rehearsal starts Jupyter with its default root and checks the same four assignment-relative filenames Cairn grades. The test runs one synthetic learner. The operator's locally available Git host provides disposable OAuth and repositories. GitHub integration, teaching judgment, the explanatory rubric, hosted JupyterHub, and cohort capacity require their own acceptance checks.

Only aggregate results, filenames and software identities go in the output. The private temporary directory, browser session, editor, grading resources and disposable Git service are removed when the runner exits normally or unwinds a test failure.
