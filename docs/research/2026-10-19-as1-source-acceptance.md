# Connected temporary assessment — source acceptance

October 19, 2026. Merged [Waypoint #53](https://github.com/EduCloud-Ecosystem/waypoint/pull/53)
connects the disabled AS1 HTTP/current-authorization/Store path to Outfitter's
reviewed data-only test peer. This is partial A1 source acceptance. Production
uploads remain unconditionally disabled; no operational upload, actual benchmark,
trusted cleanup or participant-pilot gate closes.

Reviewed head `1386bcd3779715e467c19c0ab6c4e3eaf44f38ca` merged as
`8e6f5bf6dc7a024ebee32a9261280a59c262c910`; both trees equal
`4e816aaeddade88955c317f0310eb8692bed90ff`. The final eight-file delta
contains documentation/evidence only. Runtime, tests, recipes, fixtures and
workflow bytes match tested `a5dd74b4a5a68d2aabbecf5ee32e8e1d3892e591`.
The [evidence index](evidence/2026-10-19-as1-source/acceptance.json) binds the
component's public records and protected coordinator artifacts. Hashes of a
private archive do not imply public availability or compiler attestation.

## Delivered boundary

AS1 reuses Waypoint's real scoped Store, Owner, Guard, current session/project
authorization and publication fences. Its fresh test-only schema and separate
typed policy allow sixteen lifetime rows, four per subject including tombstones,
128 ordinary intents plus the existing essential slot, bounded JSON/query
projections and finite denial reserves. Short transactions complete and release
under the same guard with `keep=False` before IPC, body transfer or waiting.
There is no study-token reuse, outstanding ordinary publication debt, raw SQLite
fallback, new allowance ledger or fake compute reservation for upload-only data.

Current authorization is checked at launch, bounded transfer and final response
publication. Revocation, logout, membership change and project closure latch
absorbing local denial; lifelines close before remote denial IPC. A response
already authorized at the final bounded copy cannot be retracted by a later
revocation. Network waits occur outside the authorization/guard locks.
HTTP rejects duplicate/conflicting Content-Length and Transfer-Encoding, checks
an absolute transfer deadline and closes broker stdin after the exact body,
rather than waiting for network connection EOF. Buffered read-ahead, would-block,
quiet polling and cancellation are exercised. Replies use the exact closed Go
codec, authority/epoch/scope bindings and observation implications.

Constructor, main/deferred descriptor-close and metadata-abort uncertainty stay
sticky and prevent another launch. Neither a free lease, PID nor stale ACK
proves writer drain. Synthetic `observed_absent` requires denied admission,
observed drain and revocation, but remains untrusted `cleanup_unresolved`.
Temporary bytes never enter the retained study Worker, snapshots, diagnostics or
exports. Public construction and production routes refuse before reading content;
only tests construct the positive fresh boundary. No flag, configuration,
environment, header or imported receipt can enable production uploads.

Unsupported AS1 recovery, checkpoint, restore, activation, raw backup and study
export refuse before effects. Rejection uses config markers and a stable,
no-follow, at-most-100-byte SQLite header read, never a live SQLite opener.
Absent future destinations or unrecognized headers provide no AS1 signal and
no positive authority; existing conservative inventory/recovery validation still
runs before classification or effects. Earlier profiles and digests are unchanged.

## Verification and limits

| Evidence | Result and exact scope |
| --- | --- |
| Independent final review | **CLEAR:** coordinator Store/Owner/Guard and narrow compatibility deltas; independent peer/HTTP/identity and final evidence/artifact review. Final 1,053-file inventory verified; all 880 earlier component evidence files unchanged. |
| Frozen local full suite | **PASS with two explicit skips:** 605 methods, 603 PASS, zero FAIL/ERROR, two SKIP at runtime `a5dd74b4`; all 59 AS1 methods ran. All 1,046 scoped files match immutable Git and identical before/after inventories. |
| Separate pure-validator invocation | **PASS:** the exact two skipped methods passed separately at the same runtime using retained Outfitter `9cf556b`. Full-suite skips remain SKIP; counts overlap and are not added. |
| Exact final hosted controls | **PASS:** [run 39366502109](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39366502109), 605 methods, 603 PASS / two SKIP / zero FAIL/ERROR; all 59 AS1 passed. Artifact output matches the timestamp-stripped job log. Both ZIP archive digests match GitHub. |
| Hosted PDF regression | **PASS:** eleven methods without skips and pinned font checksum, from the job log. No new PDF artifact was independently viewed; earlier accepted visual evidence remains separate. |
| Ordinary hosted Docker | **PASS:** existing broker `54464389`, 41 HTTP, 25 recovery and 12 guard checks; two selected legacy replays and 60 conservative CPU-seconds charged. Five evidence ZIP member sets/sizes/hashes and report/source bindings verified. The original failed replay stays unselected/NOT RUN. This does not execute the new assessment workload. |
| Optional clean source builds | **SKIPPED:** existing gate unchanged. |
| Operational assessment and umbrella runtime | **NOT RUN / OPEN:** docs-only canonical integration has no configured umbrella CI. Actual host, storage, measurements, independent cleanup and participant exercises remain unqualified. |

Local connected helpers remain the archived Darwin `4de6a090` builds, with exact
binary/source bindings. Hosted controls instead built new Linux helpers from
accepted Outfitter `8584ca8`; all 84 source hashes matched, with Go 1.24.13 and
binary hashes recorded. Those binaries were not uploaded. The separate pure
validator is the retained `9cf556b` build; none of these origins are relabeled.
Explicit environment overrides, argv, exits, timings, interpreter binary/platform
and full-run source inventories are retained. Other environment remains inherited;
no compiler attestation or independent operational qualification is claimed.
DCO sign-off trailers are not cryptographic commit signatures.

## Retained failures and next components

The first frozen full run at `4682a815` remains **FAIL**: 603 methods comprising
599 PASS, two affected methods with three ERROR records and two SKIP. Its live
SQLite rejection probe bypassed conservative inventory handling. A focused
21-method correction passed on pre-commit bytes matching later `e8a0c00c`; it was
not a clean-commit rerun. The full `e8a0c00c` run remains **FAIL**: 605 methods,
600 PASS, three affected methods with five ERROR records and two SKIP, caused by
an absent future recovery destination. The final rejection-only header check
fixes both, with the full-run inventories and original logs preserved.

Earlier dirty-snapshot failures, fixes and checker corrections remain in the
[component verification](https://github.com/EduCloud-Ecosystem/waypoint/blob/1386bcd3779715e467c19c0ab6c4e3eaf44f38ca/research-workspace/evidence/2026-10-19/as1-completion/final-verification.json).
The original 99-method run had 98 other passing methods and one method with
nine failed action subtests at the overflow-refusal precondition, not nine
executed safety-action bypasses. Constructor/close uncertainty, quiet-poll,
logout and observation controls retain their actual red evidence. Slow-client
connection reset was corrected as a transport-refusal expectation, not a JSON
success. Their partial dirty-source bindings do not become the final full-run
inventory. The artificial sixteen-by-64-KiB row probe is a storage fixture,
not sixteen validated manifests or upload-capacity qualification.

Exactly five original trailing-space lines in three raw failure logs remain
byte-identical. Source/docs whitespace checks exclude those exact artifacts;
there is no unqualified whole-patch whitespace PASS. Failed controls and
unsupported/null measurements remain visible.

Next, connect the separately versioned larger CPU profile through the existing
Outfitter execution authority, permanent per-slot reservations and independently
checked counters. Finish bounded streaming Python/R recipes and independent
scientific checks, real aggregate writer/storage enforcement and separately
reviewed Waypoint execution/provenance integration. Reuse A4/A5; no new portal,
ledger or scheduler is needed. Synthetic receipts cannot supply actual fitting
measurements, and a 10 GB tmpfs under 1 GiB task memory is insufficient.

The [researcher/instructor milestone](../strategy/researcher-instructor-pilot.md)
and [planning budget](../strategy/researcher-instructor-pilot-budget.md) still need
selected allocation, hosts, operators, window and finite native-unit allowance.
Encryption/key custody, spool/swap/crash/backup exclusions, independent expiry,
termination, revocation and deletion under faults, second-machine/operator and
whole-service privacy/accessibility acceptance remain open. Historical quota
NO-GO, fifth-headroom FAIL, exhausted v4 allowance and disabled source candidates
remain unchanged. No purchase, live provider use, private/student data or
production deployment is authorized by this delivery. Docker/Compose on OrbStack
is baseline; Kubernetes/PAIR remain optional gated evaluations.
