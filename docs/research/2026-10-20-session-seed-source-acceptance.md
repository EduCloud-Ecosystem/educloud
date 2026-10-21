# Session seed and retained helper source acceptance

October 20, 2026 delivery (merged October 21 at 01:14:04 UTC).
**J1 is tested, independently reviewed and merged.** A private external Linux
test can now create a fresh, fixed two-slot synthetic session and retain the
exact helper binary exercised by CI. This closes the first gate of the
[full-journey integration plan](../strategy/research-assessment-integration-plan.md).
Connected Waypoint execution remains the next source gate; scientific execution
and actual-host qualification remain open.

## Immutable delivery

[Outfitter #23](https://github.com/EduCloud-Ecosystem/outfitter/pull/23) was
reviewed at `3f81553774b7237fc8acbffd7db12fe92936628e` and merged as
`6a974671f008640ddccd32547131ca6e696fefa4`. The reviewed head, actual CI testmerge
`164511c5b23ccce6279aa2e224d0eff62ac31ad2` and merged commit share tree
`8c3ea960c2aac6545aa0fffa2f71bb5c13be5287`. Merge parents are accepted
`8afcb56b11bf9342449330177a1ceaa20499f9ba` and the reviewed head.
The [machine-readable acceptance](evidence/2026-10-20-session-seed-source/acceptance.json)
binds source, exercised bytes, complete evidence and review digests. Protected
raw logs and archives remain retained separately; hosted artifacts may expire.

The fixed TEST-only seed selector creates assets exclusively relative to checked
descriptors. It preserves the original parent deadline and ownership, refuses
existing or partial state, and never resets or adopts a session. Non-Linux
external setup refuses. Ordinary dispatch, production commands, public wire
contracts, existing profiles and accounting authority are unchanged.

CI now retains the actual R1 race binary through a fixed output path. Its verifier
requires hash and size agreement with the sole executable witness from the
positive lifecycle, all six complete original-process results, unchanged source
metadata and ten pinned assets. It publishes the association only after bounded
reads and checked copies. This replaces a separate rebuild that could differ
from the exercised executable. The association records a combined compile-and-test
result; it is not compiler attestation or permission to execute the artifact.

## Performed verification

The accepted [configured Linux PR run](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39523851991)
completed both jobs successfully. Root and independent review checked the actual
testmerge, all 323 source inventory entries, ten assets, complete joblogs, both
ZIP digests and all 45 archive members.

| Evidence | Result and scope |
| --- | --- |
| Six serial metadata/race groups | All exited zero with original Wait, both stream EOFs and process-group absence recorded. All 7,461 Go JSON events match archived captures and raw joblog: 110 listing events and 7,351 runtime events. |
| Race runtime | 1,622 PASS / zero FAIL / two SKIP including overlapping parents and subtests; 299 top-level PASS / two SKIP. All 107 Broker parents occur in the unchanged 58/49 partition; eleven unique packages. |
| New helper controls | All ten seed boundary leaves PASS. Actual external seed and two-slot owner lifecycle PASS in 25.93 seconds. |
| Retained executable | Linux amd64 race ELF, 11,662,125 bytes, SHA256 `e9c1a4923c2d855da64b5173d799a838b9b391fdc2ca0ec65adfbd161013f9ca`, identical to the exercised executable witness. No local execution of this ELF. |
| Downstream | Static checks, build, dedicated actual Docker lifecycle and all 83 report checks PASS: 26 Docker, 38 recovery and 19 synthetic consumer. The deliberately wrong-answer control remains; successful compute does not publish a grade. |
| Separate skips | Race-suite Docker lifecycle SKIP remains distinct from the later actual Docker step, which passed in 0.41 seconds. Provider self-expiry remains unsupported/SKIP. |
| Local verifier controls | Final changed-source fixture passed all 44 pure mocked/filesystem unit methods within the reserved 30-second window and 10-second child cap; original process reaped and no group residue observed. CI also reports 44 PASS. |
| Whole job | 895 seconds against the unchanged 900-second cap: only five seconds nominal headroom, with whole-second API precision. Robust timing fit and capacity are not established. |

The accepted run used Go 1.26.9, Linux amd64 and CGO1 with empty GOFLAGS/GOWORK.
The same two jobs, six serial commands, default race settings, 600-second Go
alarms and 15-minute main-job limit remain. No timeout increase or unchanged
retry produced this acceptance. Earlier Linux cross-compilation, Darwin refusal
and Go/Python literal checks remain separate evidence; native Python/helper
interoperability is a J2 gate.

## Retained failures and limits

[Run 39517478678](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39517478678)
failed the new expiry control. Its compound assertion did not identify the failed
branch. The corrected fixture preserves clock history and separately checks the
exact refusal, write-hook count and partial target. A later pass does not identify
the historical failed branch.

[Run 39520327366](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39520327366)
passed the six groups but failed helper input qualification after a separate
compiler exited zero; downstream steps were skipped. The failed predicate and
rebuilt bytes were not retained, so its precise historical cause remains UNKNOWN.
Retaining the exercised binary removes the rebuild assumption without assigning
that historical cause. The first local retention-unit run also remains 43 PASS /
one FAIL: a new assertion compared macOS `/var` and `/private/var` spellings. The
one-line fixture correction resolves the temporary root; assertions below the
original failed line were not credited to that run.

The storage job continues to reproduce historical `5827c84` counterexamples.
Quota, runtime and all-writer enforcement remain absent, whole-root capacity
remains UNKNOWN and the fifth headroom control remains FAIL. Its successful job
does not qualify current v7 storage. Earlier cleanup acceptance and failed
controls remain unchanged. The verifier's closed v2 failure codes do not imply
all inherited CI stderr is sanitized, and the after-snapshot prelaunch refusal
has no separate targeted test.

## Remaining integration gates

J2 may now implement the separately typed private Waypoint EX2 state, then its
native peer and connected service with current authorization and irreversible
dispatch. Its 96 ordinary operations are metadata transaction capacity, not 96
execution attempts; the positive helper capability remains two synthetic slots.
Existing AS1, v1/v2 and default meanings remain unchanged. J2 has not passed its
source or runtime acceptance merely because J1 is complete.

Installed scientific execution, faithful actual counters, aggregate storage
enforcement, versioned actual estimates/exports and complete researcher/instructor
journeys remain J3–J5 work. Host selection, encryption/key custody, independent
cleanup/deletion, second operator/machine and manual accessibility remain J6
gates. No provisioning, spending, credentials, private/student data or production
activation is authorized. The [planning budget](../strategy/researcher-instructor-pilot-budget.md)
is unchanged.
