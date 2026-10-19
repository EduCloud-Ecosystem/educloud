# Initial synthetic estimator acceptance

`a4-integration.json` records 32 coordinator checks across eleven actual CLI
scenarios at Waypoint's reviewed head. The counters are invented arithmetic
fixtures, not measured performance. `verification.json` binds merged revisions,
CI, source review, owner results and these artifacts. Focused and new test counts
are subsets of the 512 owner tests, not additional workloads.

The owner validator build/source archive was separately checked against merged
Outfitter `de65bdab`; its sanitized build record is included. The coordinator
used its own previously reviewed production-equivalent binary. Different binary
hashes do not imply different source revisions. Neither checker attests a
binary's build: the operator selects trusted local code.

To reproduce, use a clean Waypoint checkout at the pinned tested head
`053bb1ef5ff5e7a359e9f1e2a0cfbdd8d2a4f6ad` and a trusted Outfitter build from the
recorded revision. Use absolute paths and a fresh result destination:

```sh
python3 check_integration.py \
  --waypoint /absolute/pinned-waypoint \
  --executable /absolute/trusted-pure-outfitter \
  --evidence-dir /absolute/new-results
```

An existing result is refused before the test calls. The final record is created
exclusively; failures cannot replace a prior PASS. Retain terminal failures
separately. The checker observes no new files in its isolated temporary home/work
directory; it does not audit whole-machine effects or sandbox an arbitrary
executable. It calls no resource workload or provider.

`checker-corrections.json` preserves an actual isolated pre-fix failure-control
witness under optimized Python: assertions could disappear. Final operational
checks use explicit exceptions and counts derived from outcomes. The 32-check
run also passed with `PYTHONOPTIMIZE=1`. Duplicate-attempt and duplicate-cleanup
probes now preserve the other identity and rebind cleanup hashes, so one guard
cannot mask the other. Earlier 31-check records remain in the private archive;
their normal PASS results are not rewritten. The owner snapshot's coordinator
annotation refers to that earlier run, while this index binds the final 32.

Owner logs remain in the protected local archive with their hashes recorded.
Absolute private paths are omitted from the published owner/build snapshots.
Original preparation failures remain linked through the earlier acceptance
record; this estimator does not clear cleanup liabilities, renew allowances,
promote source candidates or admit private/student data.
