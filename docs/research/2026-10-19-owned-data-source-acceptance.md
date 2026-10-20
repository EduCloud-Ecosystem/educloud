# Disabled owned-data broker source acceptance

October 19, 2026. Merged
[Outfitter #19](https://github.com/EduCloud-Ecosystem/outfitter/pull/19) delivers
the disabled broker source/test slice of the
[temporary-data contract](../specs/assessment-owned-data.md). It does not complete
A1 or authorize production uploads, execution, trusted cleanup or a selected host.
The [earlier checkpoint](2026-10-19-owned-data-review.md) remains historical
failed evidence, with its original counts and coverage limits.

Reviewed head `4ca7e74e5c8a8541d08e409ed6c46a53414fbea2` merged as
`8584ca8db9a7e5eaf8d29d9670349b57f3939ab6`; both trees equal
`5c8a7b3dde8b95a947f9d3fc80a9f02ee34abd29`. The coordinator and author
independently verified the PR/main/tree state. The
[acceptance index](evidence/2026-10-19-owned-data-source/acceptance.json) records
exact source, artifact and audit hashes.

## Delivered boundary

The existing journal, locks, Watch and Reap own a fresh test-only data scope.
No additional ledger, queue, scheduler, compute grant, attempt or reservation is
created for the upload session. Production prepare, ingest and seal refuse from
fixed command arguments before stdin/state access. Ordinary compute/native and
unsupported recovery/export operations refuse assessment-only state before
effects. Positive storage/clock construction and fixture seeding exist only in
test code. Existing charged and unresolved accounting remains intact.

One irreversible writer has exact body/EOF framing, immutable expiry and bound
owner/watcher lifelines. Positive kernel checks distinguish anonymous pipes
from named, renamed and unlinked FIFOs on the observed Darwin/Linux platforms;
access direction, descriptor identity and pairing checks remain required.
Private close confirmation follows actual successful Close; sticky uncertainty
overrides it. Nil-content crash windows, failed publication, unknown ownership
and active writers retain holds. Lease freedom and PID/ACK observations cannot
establish writer drain or deletion.

Safe synthetic removal can occur after confirmed close even when all eight
immutable observation slots are occupied. Earlier unknown observations remain
unchanged; no ninth record or trusted closure is invented. Stable lease
tombstones survive. Status stays `cleanup_unresolved` and all upload, execution,
actual-resource and cleanup-trust flags remain false. Temporary input does not
enter the retained study Worker, snapshots, diagnostics or exports.

## Verification and its limits

| Evidence | Result |
| --- | --- |
| Immutable source review | **CLEAR.** Platform/stream/journal/CLI review plus the final test-only correction; 221 source bindings matched. Production, helper entrypoint and eleven canonical fixture vectors are unchanged between `4de6a090` and final `4ca7e74`. |
| Final local targeted controls | **PASS:** four test events with default race runtime and the same four in the separate exit-sleep-zero race run. Vet, formatting and whitespace passed. This is not a final full local suite. |
| Prior production-equivalent local source | At `4de6a090`, **144 affected** and **28 focused default-runtime** passing events overlap. The coordinator's **97 actual helper/CLI checks** are also bound to `4de6a090`; their binaries were not rebuilt or relabeled as `4ca7e74`. |
| Exact final hosted suite | **PASS:** [run 39357243561](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39357243561), both required jobs successful. Full race log: **1,047 PASS / 0 FAIL / 2 SKIP**, all ten packages passed. The 150 owned-data, 85 separate-process and 13 pipe events are overlapping subsets. All 4,970 JSONL events match the retained job log. |
| Actual Linux witnesses | **PASS:** eight descriptor observations distinguish anonymous pipefs/link count one from named/renamed/unlinked filesystem FIFOs. Positive lifecycle, fresh-generation writer refusal and saturated blocked-writer cleanup controls ran. This does not qualify an actual selected host or independent failure domain. |
| Existing Docker/recovery/consumer regression | **PASS:** later actual Docker lifecycle and 26 Docker, 38 recovery and 19 synthetic-consumer report checks. These exercise existing adapters/contracts, not temporary assessment execution or measured CPU/provider consumption. Provider self-expiry after host/watchdog/daemon loss remains unsupported. |
| Historical storage-writer job | **PASS within its separate counterexample scope:** 22 test events, 32 model cases and two optimized probes at its historical `5827c84e` source pin. It grants no current lifecycle, quota or available-capacity credit. |
| Operational assessment | **NOT RUN / OPEN:** real uploads, benchmark dispatch/measurements, host/encryption/spool policy, independent cleanup and second-operator/whole-service acceptance. |

The final local command records preserve arguments, explicit environment
overrides, start/end times, exit codes and log hashes; other environment remains
inherited. Older inline refusal checks lacked raw per-call outputs and a full
environment/compiler snapshot. Their later transcript supplement and source
archive remain explicitly retrospective, not a new execution or attestation.
The root finite-body fresh-generation probe does not itself prove before-body
refusal; the separate author control keeps stdin open and verifies that gate.

## Failed evidence retained

The `79cf73f` full local run remains **FAIL: 1,020 PASS / 2 FAIL / 2 SKIP**.
The `7972ce8` hosted run remains **FAIL: 952 PASS / 74 FAIL / 2 SKIP**, and its
Darwin unlinked-FIFO negative retains two failed leaves plus two failed parents.
The corrected positive kernel boundary is distinct from those failures.

The `4de6a090` hosted run remains **FAIL: 1,046 PASS / 1 FAIL / 2 SKIP**. A
separate default-race reproduction with unchanged production code showed that
the writer held its file while blocked, then closed and physically removed the
scope while the same eight unknown observations survived. The old test demanded
an additional absence record that the bounded log could not append. The final
control establishes saturation using at most eight acknowledged reconciliation
calls after the initial cancellation; it asserts no early removal, exact denial,
confirmed close, physical absence, unchanged observations, stable tombstones and
false trust flags. No application deadline, observation limit or production
behavior was relaxed.

An intermediate `a39cf04` optimized run still failed its three-second watcher
progress expectation; its separate diagnostic pass remains separate. No stable
kernel/filesystem cause is inferred. The final acknowledged setup removes that
scheduling assumption. Earlier header, maximum-form, sentinel, commit-time,
close-uncertainty, direct-provider, lease and legacy-migration failures remain
retained. The old 82-check stale-generation limitation and the coordinator's
later Go-output-chunk parser correction remain explicit checker limitations,
not newly invented product failures.

## Next delivery and decisions

The existing Waypoint owner continues the real AS1 HTTP/Store/current-auth and
peer journey. Separately reviewed larger-workload profile and measurement
integration source/test work is authorized, preserving imported v1 schemas and
digests and reusing the merged A4/A5 estimator/export paths. Neither the current
small profile nor a new parser alone completes the
[researcher/instructor milestone](../strategy/researcher-instructor-pilot.md).

The [approved provisional budget](../strategy/researcher-instructor-pilot-budget.md)
is planning only. Exact allocation, host, operator, allowance and attended live
window remain unselected. Present one concrete decision packet when engineering
gates are ready; identify any exact target choice needed earlier while continuing
independent work. Live Jetstream2 still requires Greg's separate approval.
No resource, purchase, subscription, model download, private/student-data use,
production deployment or default-routing change occurred through this source
acceptance. Docker/Compose on OrbStack remains the baseline.
