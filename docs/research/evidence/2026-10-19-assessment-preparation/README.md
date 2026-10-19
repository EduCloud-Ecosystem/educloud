# Pure assessment integration evidence

`assessment-integration.json` records 37 passing coordinator checks at the
reviewed component heads. `verification.json` records merged revisions, exact
CI outcomes, local-log hashes and open gates. Counts of subtests and top-level
tests overlap where stated; they are not additional workloads.

The executable was built by the coordinator from Outfitter's reviewed production
files with `GOMAXPROCS=2 go build -p 1`. Its hash is in the integration result;
selected source bindings are in the index. The checker accepts a trusted local
executable and does not attest its build or sandbox arbitrary executable code.

To reproduce, use clean checkouts at the recorded heads and build that Outfitter
command. Then provide absolute checkout, executable and evidence paths:

```sh
python3 check_integration.py \
  --waypoint /absolute/waypoint-checkout \
  --outfitter /absolute/outfitter-checkout \
  --executable /absolute/reviewed-outfitter \
  --evidence-dir /absolute/new-evidence-directory
```

The evidence directory must have no existing `assessment-integration.json`.
Existing results are refused before checks; final output is created exclusively.
A failed check exits nonzero without producing a success record. Retain terminal
errors separately; do not substitute a result from another directory/run. The
checker verifies clean pinned heads and executable identity before/after, runs
the two real CLIs in an isolated temporary home/work directory, and observes
that no additional files appeared there. It neither starts a workload nor tests
whole-machine filesystem/network enforcement, encrypted scratch or cleanup.

`outfitter-before-validation-fixes.txt` preserves five failing subcases from
independent review. `coordinator-harness-corrections.json` records two mistaken
coordinator assertions. `negative-probe-isolation-correction.json` records the
later review of masked rejection probes and stale-result behavior. These are
preserved corrections, not claims that original controls passed. Large raw
local test logs remain in the operator's protected evidence archive with hashes
in the index; hosted run links retain the remote checks separately.

The synthetic shared fixture expires October 20, 2026. It remains an immutable
digest vector after expiry: preview does not revive its proposal or grant any
execution authority. No uploaded source data or source-data hash is retained by
this assessment record.
