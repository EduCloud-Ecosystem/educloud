# Standard Docker CI broker adoption evidence

This is a byte-preserved copy of public synthetic CI evidence and its local
read-only audit for Waypoint head `e16bcd3ad7d28cf6a56845621e65ca38ac526923`,
[run 39114639604](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39114639604).
It prevents the workflow's fourteen-day artifact retention from becoming the
only copy. It is not a new test, an operator rollout or a replacement for the
original two-binary qualification in Waypoint #44.

`artifacts/` contains all nine public files downloaded from artifact
`12131747065`: four reports and five export bundles. `artifact-audit.json` records
their SHA-256 values, source counts, broker identity, cleanup/replay observations
and bounded PASS/NOT RUN conclusions. Its SHA-256 is
`7a609daf40a8f536f2fcf81efe0838c07a4d50d9dab1f4e494512d5d01b7a35a`.
`ci-run.json`, `ci-artifacts.json` and `ci.log` are the original captured public
metadata and job log. The reported GitHub artifact archive digest is distinct
from the independently recorded hashes of its extracted members.

`verify_artifacts.py` is the exact original audit source, including its original
local checkout path. It inspects files and invokes read-only Git; it runs no
broker or Docker workload. It writes the audit report, so do not execute it
inside this frozen evidence directory. Reproduction needs a disposable copy,
the exact Waypoint checkout and an explicitly recorded path adaptation. This
archive does not claim that the historical script is a portable operator tool.

The head CI passed 384 controls, 41 HTTP checks, 25 recovery checks, 12 guard
checks, two successful historical replays and five bundle verifications. Counts
overlap. The original failed historical run remains NOT RUN; the two successful
replays retain 60 conservative CPU-seconds. Optional source builds were skipped.
No new finite-v3 provider, browser, independent-human, physical-capacity, native
or cloud acceptance is established. Source candidates remain disabled.
