# EduCloud status and computing-continuity priority

Research-pilot update: October 19, 2026. The classroom/AI assessment below retains
its October 6–7 review boundary unless explicitly updated. Its historical vendor
prices and component heads are not current quotes or new deployment decisions.
The original July snapshot is preserved in `docs/research/2026-07-21-platform-status.md`.

## October 19 research assessment implementation

The [research sandbox and allocation-readiness contract](docs/specs/research-assessment.md)
is approved for implementation. It adds a separate temporary-upload mode,
versioned measurement/cleanup receipts, actual-resource benchmarks, deterministic
estimation and ACCESS/NAIRR preparation. The [tool decision](docs/decisions/2026-10-19-research-assessment-tools.md)
and [A0–A6 backlog](docs/strategy/research-pilot-build-backlog.md#october-19-assessment-implementation-sequence)
record the implementation sequence. Development resumed in the existing
implementation chat on October 19; this contract update is not a completed
component deployment. The first component slice covers strict manifests,
content-free retention preview, an assessment export guard and validated
measurement/cleanup receipts. Upload and dispatch remain disabled pending actual
temporary-storage and independent-cleanup qualification.

The [first preparation slice is now accepted](docs/research/2026-10-19-assessment-preparation-acceptance.md)
at merged Waypoint #49 (`d70aaccc`) and Outfitter #18 (`de65bdab`): strict
manifests, pure receipt conversion/validation and a closed retention preview.
Independent reviews, 37 actual Go/Python integration checks and required hosted
regressions pass; original failures and optional skips remain recorded. The
broader A1/A2 packages remain incomplete. A4's first synthetic estimate command
is now merged in Waypoint [#50](https://github.com/EduCloud-Ecosystem/waypoint/pull/50),
merge `db7ad40e`: exact stage fitting, held-out errors, repeat variability and
visible unknown/OOM/extrapolation limits. Independent review, 512 local tests,
32 separate real-CLI checks and required CI pass. This accepts synthetic
calculation behavior only. Waypoint [#51](https://github.com/EduCloud-Ecosystem/waypoint/pull/51),
merge `2d94f87a`, adds initial A5 exports: ACCESS Discover and distinct NAIRR
research/Classroom drafts, editable source, PDF and matching JSON/CSV worksheet.
Independent source/evidence reviews, 536 standard-library tests, 10 optional PDF
tests, 22 separate real-CLI checks and required hosted CI pass. Final renderer
coverage is the later PDF suite and artifact inspection, rather than one
immutable full-suite renderer run. Root checked all three rendered pages,
24 package payloads, exact digest/receipt binding and visible-field parity.
Original publication, geometry, environment and checker failures remain visible.
All packets stay DRAFT. Subsequent Waypoint
[#52](https://github.com/EduCloud-Ecosystem/waypoint/pull/52), merge `45ecd81c`,
adds Explore worksheets without font/PDF dependencies, optional digest-bound
internal planning PDFs and a distinct Accelerate description draft. Independent
reviews, 546 standard-library/11 PDF tests, 20 separate isolated CLI checks and
required CI pass. The three exact earlier previews and their digests remain
unchanged. Root verified 23 payloads and both rendered pages; the initial
floating-point geometry observation remains recorded with explicit tolerances.
Maximize remains refused pending its own multi-document profile. Actual
measurements and program/application readiness stay open. The next core
dependency is A1's dedicated temporary session/data lifecycle, separate from the
retained study workflow.

The first connected A1 slice is now assigned under the
[owned-data implementation contract](docs/specs/assessment-owned-data.md).
Outfitter's existing owner implements data-only scope ownership, writer/watch
lifetime and cleanup-or-quarantine in the existing journal; Waypoint's existing
owner prepares its auth/Store/schema handoff before integration. No component
increment is accepted yet. Production upload/ingest/seal remain unconditionally
disabled, and no synthetic cleanup observation can establish trusted closure.
The declared upload cap is separate from unchanged manifest v1; selected expiry
is immutable and cannot exceed manifest/project/authorization/policy limits.
No new purchase, operational resource or qualification allowance is selected.

The accepted study-bundle exporter retains source bytes and cannot serve the
new temporary mode. Isolated encrypted scratch, exhaustive cleanup, allowlisted
retention and report preview need their own implementation and fault evidence.
Existing conservative CPU allowance charges remain separate from measured usage
and provider charges. Public/synthetic fixtures remain the admission boundary.
Live CPU/GPU qualification still needs selected allocation/hosts/model/operator,
window and finite allowance; second-operator reproduction, researcher/instructor
exercises and whole-service FERPA acceptance remain open. Ben's Docker/Jetstream2
assignment, the Zensical pilot and separate synthetic Modal comparison are
preserved. Historical evidence below does not close these new gates.

## October 17–18 research pilot

The local public/synthetic Python/R workflow is accepted and merged: Waypoint
[#26](https://github.com/EduCloud-Ecosystem/waypoint/pull/26), merge `8506baef`;
Outfitter [#6](https://github.com/EduCloud-Ecosystem/outfitter/pull/6), merge
`4275d1a`; and EduCloud [#13](https://github.com/EduCloud-Ecosystem/educloud/pull/13),
merge `cd6d80c`. The [baseline acceptance record](docs/research/2026-10-17-research-pilot-acceptance.md)
pins complete tested heads, images and evidence. Waypoint's final CI at `da4c655`
passed; local evidence includes 57 unit controls, 41 HTTP/Docker checks and an
earlier 23-check browser exercise. Outfitter records 27 real Docker checks.

P1 environment/replay and coordinated recovery are also merged: Outfitter
[#7](https://github.com/EduCloud-Ecosystem/outfitter/pull/7), merge `abfcfa28`,
and Waypoint [#30](https://github.com/EduCloud-Ecosystem/waypoint/pull/30), merge
`8a3e87c3`. Final tested heads are Outfitter `5827c84` and Waypoint `d09cb2f`
(implementation `bf275dd`); both CI runs and scoped independent reviews passed.
The acceptance packet records 119 unit controls, 41 final HTTP/Docker checks
(all recorded runs cleaned up), 25 workspace recovery checks and 17 catalog
browser checks (two simulated, no compute dispatched). Two automated historical
Python/R reproductions passed while the original failed R attempt remained
NOT RUN for replay. The broker's separate local recovery exercise passed 38 checks.

The final workspace restore step took 0.773 seconds in a 14.193-second exercise,
with no completed records or immutable artifacts lost at the frozen point;
pending work was cancelled without replay. These measurements are not hosted
recovery objectives or independent human reproduction. The special-file blocking
finding in broker recovery was fixed at `5827c84` and independently verified as
refused. Independent human reproduction and hosted/source-loss recovery
acceptance remain NOT RUN.

Source-runtime builds are now accepted through Waypoint
[#31](https://github.com/EduCloud-Ecosystem/waypoint/pull/31), merge `adc44643`,
reviewed head `5f98c068`. Native ARM64 and AMD64 construction/qualification
records are retained, with 49 checks per platform; 136 controls and ordinary
post-merge CI passed. The original probe and builder failures remain visible.
All four new source environments stay disabled, and durable image distribution,
promotion and independent human reproduction remain separate gates. The original
Documents-directory replay remains failed; a later read-only observation found
its container absent and its ledger conservatively charged 30 CPU-seconds.
Merged [#32](https://github.com/EduCloud-Ecosystem/waypoint/pull/32), merge
`bc5d2fa1`, records that supplemental reconciliation without rewriting the failed
receipt/report or refunding the charge. The matching ledger now records verified
cleanup with no unresolved liability; the workload remains failed.

Remaining work is sequenced in the [research build backlog](docs/strategy/research-pilot-build-backlog.md).
Waypoint [#27](https://github.com/EduCloud-Ecosystem/waypoint/issues/27) is closed
for source-image builds; [#28](https://github.com/EduCloud-Ecosystem/waypoint/issues/28) covers
independent second-operator/machine acceptance, and
[#29](https://github.com/EduCloud-Ecosystem/waypoint/issues/29) shared identity,
retention/storage, capacity and accessible operations. Open issues #28/#29 remain
unassigned. The local synthetic identity/access slice merged in
[#33](https://github.com/EduCloud-Ecosystem/waypoint/pull/33), merge `8bb8e415`,
reviewed head `264f8591`. Its evidence separates 158 offline controls, 74 real
local browser/service checks at application revision `b818d02`, and seven later
provider-logout checks. Final ordinary CI passed; source builds were skipped.
Failed attempts remain retained. All four owned stacks were removed; conservative
charges remain 210 CPU-seconds for the final pilot and 120 for earlier attempts.
Hosted identity, manual accessibility and independent human acceptance remain
open. Waypoint's read-only storage inventory/retention report merged in
[#34](https://github.com/EduCloud-Ecosystem/waypoint/pull/34), merge `a769dd86`,
with 176 total workspace tests and final ordinary CI passing. A stopped synthetic
store observation counted 163,779 logical bytes and 82 entries, all protected;
captured content/identity metadata matched before and after reading.
[#35](https://github.com/EduCloud-Ecosystem/waypoint/pull/35), merge `2a7d6cd0`,
bounds broker stdout/stderr incrementally while retaining identity/cancellation
checks and unknown liabilities. Its 184 total workspace tests and final ordinary CI
passed. Both source-build jobs were skipped. Whole-store admission is blocked:
the next draft reproduced five failures in dispatch holds, rollback uncertainty,
result publication, overlapping project initialization and consumed headroom.
[#36](https://github.com/EduCloud-Ecosystem/waypoint/pull/36), merge `640fa2d8`,
retains the rejected draft and reproducible witnesses as documentation/evidence
only; its accepted application source is unchanged. The narrower operation guard
merged in [#37](https://github.com/EduCloud-Ecosystem/waypoint/pull/37), merge
`a58001b2`, reviewed head `68fe5496`. Its opt-in fresh-store profile records durable
intents, pauses uncertain work and preserves guard state through held recovery.
The local record passed 235 offline controls, nine browser/HTTP checks with a
simulated provider and twelve actual local Docker/provider checks. Final ordinary
CI passed; source builds were skipped. New regressions cover the first four
witnesses; the fifth consumed-headroom case and whole-store admission remain
blocked. Two incomplete browser attempts, 127 prior evidence files and the dirty
rejected draft remain intact. No accepted store is migrated and no quota or
deletion is enabled. A subsequent independent audit reproduced three failed
controls: cancellation, local user revocation and project closure committed after
the early check but before launch still reached intercepted broker spawn. No
actual process was launched. The correction merged in
[#38](https://github.com/EduCloud-Ecosystem/waypoint/pull/38), merge `7d5cf925`,
reviewed head `ae00a41a`: final authority recheck, preservation of superseding
accounting and owned observer cleanup after a post-launch fence error. All 295
offline controls, including sixty dispatch tests, and final ordinary CI passed;
source builds were skipped. A separate independent recheck passed 26 targeted
tests and prevented all six original witness launches against corrected source.
The original failure remains reproducible against its frozen source. All 137
prior evidence files and the rejected draft remain unchanged. The capacity
contract merged in [#39](https://github.com/EduCloud-Ecosystem/waypoint/pull/39),
merge `599ee0ce`, reviewed head `e543ca4e`. Seventeen writer categories,
eight production-connected Python controls and seven pinned simulated broker
controls preserve UNKNOWN bounds; final ordinary CI passed, source builds skipped.
Review replaced a self-comparing append fixture with pre-submit expectations and
negative controls, retaining the earlier evidence. All 168 prior evidence files
are unchanged. Finite logical row/session/encoded limits merged in
[#40](https://github.com/EduCloud-Ecosystem/waypoint/pull/40), merge `e79a50c6`,
reviewed head `f7d0cd44`. The fresh local-key profile binds existing authority and
preserves safety actions at limits. All 317 local tests passed, including 21
finite controls; independent review and exact-head/post-merge CI passed, with
source builds skipped. Two reproduced binding/recovery-entry defects were fixed;
their original red source/log and all 182 prior evidence files remain unchanged.
Finite OIDC and restore explicitly refuse. Existing Docker CI is compatibility
coverage, not finite-profile provider acceptance; its provider/browser/human
gates remain NOT RUN. Whole-store quotas remain NO-GO, capacity UNKNOWN and the
fifth headroom failure FAIL. SQLite/guard qualification merged in
[#41](https://github.com/EduCloud-Ecosystem/waypoint/pull/41), merge `1e4b04c2`,
reviewed head `b8845f57`: nine disposable controls, 318 local suite tests and
exact-head/post-merge CI passed; source builds skipped. Production source and all
199 prior evidence files remain unchanged. The witnesses expose recurring WAL
and failed temporary-file growth; their passing results are not storage bounds.
The earlier failed restart assumption remains a fixture failure. Waypoint
[#42](https://github.com/EduCloud-Ecosystem/waypoint/pull/42) merged as `66a48dfe`
from reviewed head `b4ccf05e`: a fresh opt-in export profile closes its SQLite
transaction before artifact I/O, verifies copied evidence and rechecks current
authority plus exact private metadata before publication. The 334 local tests
include 16 new export tests; independent review and exact-head/post-merge CI
passed, source builds skipped. All 209 prior evidence files remain unchanged;
the initial descriptor-cleanup defect and fixture failures are preserved.
The fixed ordinary/safety guard-scratch contract received implementation GO
after exhaustion, takeover and compatibility review; corrected implementation
is accepted in #43 below. Every mutation rechecks residue/holds even with cached
durability proof. Failed safety publication reports failure and retains debt,
which can leave revocation unapplied in the new opt-in profile.
Outfitter's Docker writer qualification is accepted below. No quota admission,
accepted-store migration or default change.
Ben's existing Outfitter issues
#1–#5 remain assigned and unchanged.
Outfitter [#8](https://github.com/EduCloud-Ecosystem/outfitter/pull/8), merge
`534dcf18`, adds durable native-SU accounting and independent cleanup. Two
independent-review findings were fixed; final CI passed 115 tests/subtests,
26 Docker checks and 38 recovery checks. Provider failure controls use a local
simulator. Live Jetstream2, independent-host supervisor operation and provider
settlement remain NOT RUN. The durable synthetic consumer-job bridge is now
merged in [#9](https://github.com/EduCloud-Ecosystem/outfitter/pull/9), merge
`273bb014`, after one independent-review fix. Final CI passed 156 tests/subtests,
26 Docker, 38 recovery and 19 consumer checks. It uses actual local Docker
fixtures and does not publish grades. Cairn's opt-in disposable adapter is now
merged in [#32](https://github.com/EduCloud-Ecosystem/cairn/pull/32), merge
`bb41bdaf`: independent review fixes, 19/19 local Docker controls and all eight
final CI checks passed. Its separate command proposes results without storing
grades; production configuration remains unchanged. Cairn's subsequent
[#33](https://github.com/EduCloud-Ecosystem/cairn/pull/33), merge `ab339c44`, pins
job identity, immutable submission and instructor policy across queue retries.
Independent review and all eight CI checks passed after the deadline-locked
grading regression was reproduced and fixed. Subsequent
[#34](https://github.com/EduCloud-Ecosystem/cairn/pull/34), merge `536da6a5`, adds a
pre-checkout queue-owned claim and atomic run/grade/queue publication for the
optional job-aware path. Independent review, 1,037 local passing events (493
overlapping top-level tests, 16 skips), vet and all eight CI checks pass,
including hosted PostgreSQL. Mutex-cancellation failures are preserved; unknown
or unrecorded claims remain held. Restored-store authority and external status
recovery stay unqualified; this does not install the production Outfitter
adapter. Merged [#35](https://github.com/EduCloud-Ecosystem/cairn/pull/35),
merge `912b9e1d`, adds real authenticated operator inspection of bounded queue and
dispatch metadata on the already-open store. Independent review, 1,084 local
passing events (502 overlapping top-level tests, 16 skips), vet and all eight CI
checks pass. Hosted PostgreSQL runs the inspection and read-only-connection
controls; local PostgreSQL remains NOT RUN. A reproduced SQLite NUL-suffix
reader defect and its correction remain visible. Missing-record causes,
worker liveness and external effects remain unknown; inspection cannot grant
replay, reset, recovery or compute authority. No default runner or deployment
changed. The Jetstream2
operator/cleanup decision packet merged in
[#10](https://github.com/EduCloud-Ecosystem/outfitter/pull/10), merge `afc4fe82`,
after independent design review and final CI. It remains explicitly blocked:
its proposed 1 SU allowance is not a provider-enforced charge cap, operational
fields are unselected and independent-host cleanup is unqualified. The separate
offline rescue prototype merged in
[#11](https://github.com/EduCloud-Ecosystem/outfitter/pull/11), merge `e34604ce`,
reviewed head `73ae1ab4`, after three durability/clock fixes and an exact-status
parser correction. Final CI passed 376 tests/subtests, 26 Docker checks, 38
recovery checks and 19 consumer checks. Forty simulated crash boundaries use
separate processes on one machine, not actual independent hosts. Unknown late
effects and charges remain held; the 64-sweep observation limit and live gates
remain explicit. The pure metadata-compatibility evaluator merged in
[#12](https://github.com/EduCloud-Ecosystem/outfitter/pull/12), merge `5700ff52`,
reviewed head `eec00a96`. Five independently reproduced findings were corrected;
final CI passed 607 tests/subtests (including 231 compatibility and 220 rescue
controls), plus 26 Docker, 38 recovery and 19 consumer checks. Matching supplied
metadata does not prove boot, host suitability or effective network isolation;
the evaluator has no collection transport or creation/ledger integration.
The enforcement increment merged in
[#13](https://github.com/EduCloud-Ecosystem/outfitter/pull/13), merge `2ce00f49`,
reviewed head `e10972e7`. It binds one experiment to native admission, consumes its
sole attempt with the reservation and rechecks compatibility/expiry before both
simulated creates after rescue acknowledgement. Independent review fixed an
envelope-serialization defect; final CI passed 736 tests/subtests, plus 26 Docker,
38 recovery and 19 consumer checks. Fifteen creator-process crash boundaries are
local simulation. Restart, changed requests and settlement do not replenish the
attempt. Guest execution and live access remain NOT RUN; unknown late effects,
independent-host operation and terminal settlement remain unresolved.
The supplemental operational packet merged in
[#14](https://github.com/EduCloud-Ecosystem/outfitter/pull/14), merge `e9c18f97`,
reviewed head `2f5f4c63`, after review corrections and passing final CI. It recommends
restricted private SSH from existing approved capacity and an independent cleanup
host, without selecting resources or granting access. Its 64 total observer sweeps
are shared across both phases and restarts for one reservation. Fourteen historical
files are unchanged. No new subscription is demonstrated necessary; incremental
host/network/operator costs and residual exposure remain unknown. Live execution
still requires engineering, operational and approval gates, not approval alone.

Docker storage-writer qualification merged in
[#15](https://github.com/EduCloud-Ecosystem/outfitter/pull/15), merge `e5599066`,
reviewed head `0d94e3c8`. Exact-head/post-merge CI passed the new offline qualification and
existing broker/Docker checks. Twenty instrumented observations run against the
unchanged active broker pin, with 22 Go test/subtest passes, 32 separate model
cases and two optimized-process oracle probes. Review corrected false Boolean
proof flags and assertion-disabled oracle gates; the prior passing report,
initial root clearance and failed controls remain preserved. A cutover witness
also shows that a post-publication error can leave the destination active.
All ten existing evidence files and runtime source remain unchanged. Whole-root
capacity is UNKNOWN and the model remains unenforced.

Waypoint [#43](https://github.com/EduCloud-Ecosystem/waypoint/pull/43), merge
`5f2b21f1`, reviewed head `b063dc99`, adds fresh opt-in fixed ordinary/safety
guard publication slots. It qualifies takeover before business effects and
rechecks holds even when current bytes are unchanged. Independent review fixed
premature token release during cancellation and refused request preparation
after another process published. All 368 local controls and exact-head CI passed;
all 248 earlier evidence files and both original failures are retained.
The conditional 12 MiB sum covers only the three named guard payloads. Exhaustion
can block revocation or settlement, retaining active access or debt respectively.
No whole-store quota, accepted-store migration, OIDC/restore or default change.

The separate serialization-before-spill implementation merged in
[#16](https://github.com/EduCloud-Ecosystem/outfitter/pull/16), merge `54464389`,
reviewed head `28d34437`. It validates diagnostic success/failure variants and
the maximum mixed ledger before sidecar effects while preserving conservative
accounting. Eighteen focused and 754 full race test/subtest passes, independent
review and exact-head/post-merge CI passed. Two original orphan
failures and all 28 prior evidence files remain intact. Later I/O orphans and
background writers remain open. Separate two-binary qualification merged in Waypoint
[#44](https://github.com/EduCloud-Ecosystem/waypoint/pull/44), merge `2317eac6`,
reviewed head `968d0f1c`: the original synthetic run recorded 45 controls and
seven cleaned-up Docker attempts, each conservatively charged 30 CPU-seconds.
Review reproduced a false PASS that could erase those charges in the checker;
the corrected checker passes 16 focused controls normally and under optimized
Python, 384 combined tests and exact-head CI. Retrospective verification of the
seven original receipts retains all 210 charged CPU-seconds; it is not another
candidate workload. Original failures, source attribution and uncertain fixtures
remain. Standard Docker CI adoption merged separately in Waypoint
[#45](https://github.com/EduCloud-Ecosystem/waypoint/pull/45), merge `d8431162`,
reviewed head `e16bcd3a`. Its 384 controls and Docker CI passed; artifact review
verified 41 HTTP, 25 recovery and 12 guard checks, two successful replays and five
bundles. This changes only the CI checkout, not an operator's broker or state.
Optional source builds and historical pins stay frozen. Scoped SQLite ownership
merged in Waypoint [#46](https://github.com/EduCloud-Ecosystem/waypoint/pull/46),
merge `0efc6fd734e7f812cabc3822d2ea93b8c1063752`, reviewed head `40fe12e6`, runtime `43890cbf`.
Its fresh opt-in v4 profile passes 433 local tests, including 49 ownership
controls, and detects 29 deliberately broken variants. Fifteen reproduced review
findings are corrected and preserved. Independent source/evidence reviews, a
separate root 49-control recheck and final-head CI pass; counts overlap.
Uncertain ownership holds readers/writers and safety operations for the same root
in that process; clean full-cap safety paths pass. No checkpoint, journal, quota
or migration changes. All 343 historical evidence files remain exact. Current
cleanup wording distinguishes the original failed receipt from PR32's later
verified cleanup and retained charge.

The follow-up v4 qualification merged in Waypoint [#47](https://github.com/EduCloud-Ecosystem/waypoint/pull/47),
merge `d738e7da881fff95427e98292ae202f05d9a9f28`, reviewed head `5053358121f8a3d6a971c64cd70db7ddc32efea8`.
Its one fixed local exercise completed four
Python/R attempts, two synthetic projects, 18 controls and two bounded exports.
All four results match independent fixture answers; each run records verified
cleanup and a full 30-CPU-second charge, 120 total. Queued cancellation and
current-access removal dispatched no compute. Candidate03 source is `fe4788c4`,
using accepted Outfitter `54464389`; five checker findings plus the initial
boolean-control failure were fixed before execution, with original evidence
retained. Final independent reviews and exact-head CI passed; the merged tree
matches the reviewed head. The linked research record retains the evidence. Browser and late-revocation-race qualification remain NOT RUN/NOT
QUALIFIED; finite OIDC/restore refuse, source candidates stay disabled, whole-store
capacity remains UNKNOWN, quota NO-GO and fifth headroom FAIL. The local exercise
creates no new allowance. Next inputs are an independent operator/machine and a
selected shared-pilot host, cohort, storage, retention/recovery expectations and
support owner; no further generic profile or quota machinery is scheduled.

Portage [#10](https://github.com/EduCloud-Ecosystem/portage/pull/10) and
[#11](https://github.com/EduCloud-Ecosystem/portage/pull/11) merged as `cf41dde`
and `a3a4a6e`. Review fixed false-positive readiness, skipped-control and memory
evidence paths, and made paid CI review explicitly opt-in. Final checks passed;
the local suite recorded 225 passing tests with six existing integration skips.
The qualification record has 95 synthetic passing controls and all 12 actual
engine gates NOT RUN. The offline qualification/capacity review packet is now
merged in [#12](https://github.com/EduCloud-Ecosystem/portage/pull/12), merge
`577fdb9a`: 61 focused tests and 286 total tests passed, with six existing skips;
independent review and final CI passed. The example identifies 32 missing
capacity/cost fields and grants no authorization. The concrete operator packet
is prepared; no approved installed model was identified in the inspected local
inventory. Live use stays deferred while host/model/operator/window choices are
pending. The confirmed metadata/dispatch expiry gap was fixed in
[#13](https://github.com/EduCloud-Ecosystem/portage/pull/13), merge `11438ede`,
reviewed head `bf4c51c1`. Seventeen separate synthetic expiry controls pass;
the full suite passed 303 tests with six existing skips, and final CI passed
(paid review skipped). Expiry after admission retains uncertain reservations.
The original 95-control record and all 12 NOT RUN runtime gates are unchanged.
No engine was started, model acquired or default route changed. Jetstream2 hosted
inference remains an unselected recommendation. The pure fixture contract merged
in [#14](https://github.com/EduCloud-Ecosystem/portage/pull/14), merge `b2ba332f`,
reviewed head `2499c9d2`: 147 new controls and 450 total tests passed with six
existing skips; final CI passed and paid review was skipped. The classifier has
no transport, credential lookup, ledger mutation or live eligibility. Reported
usage stays provider-reported; uncertain outcomes retain unknown liability.
The original 95/17 evidence records and 12 runtime NOT RUN gates are unchanged.
The separate restart investigation confirmed an approval-lifetime limit gap:
two fresh processes under one fictional approval dispatched 32 simulated
inference calls and 102 metadata calls. Unknown reservations survived restart,
but three metadata calls preceded the repeat's unknown-work refusal. These are
offline failure witnesses, not engine qualification. The correction merged in
[#15](https://github.com/EduCloud-Ecosystem/portage/pull/15), merge `79742746`,
reviewed head `f22ff34c`: one protected local authority, existing-only startup,
permanent budget-bound slots, a runner lease and explicit offline migration.
It passed 63 guard controls, 175 runner controls, 513 full-suite tests/six skips
and both final CI gates; paid review was skipped. Completed and unknown-work
repeats make zero further fixture inference, metadata or authority contacts.
A clock-watermark defect and two CI failures remain recorded alongside their
corrections. All twelve runtime gates remain NOT RUN; no hosted lane, model or
execution window is approved.

Docker stays the baseline. Optional Kubernetes evaluation follows P1 before
custom multi-host expansion; existing institutional-capacity discovery may begin
independently. Native-SU Jetstream2 accounting/cleanup and optional direct Portage
qualification retain their own gates. No new subscription is assumed necessary
locally; the [capacity decision](docs/decisions/2026-10-17-research-pilot-capacity.md)
requires the exact dependency and finite exposure prepared before any cost.
No cloud purchase, live allocation test, production deployment or private-data
admission occurred in this update. Belay and `portage-local` remain unchanged.

The separately authorized local OrbStack migration remains host-owner work. The
[Kubernetes foundation package](tools/local-kubernetes/README.md) prepares and
checks namespace/quota/service-account/restricted-pod designs offline, with zero
workload allowance and no cluster calls. It neither performs the migration nor
enables a Kubernetes execution backend. The separate
[host-owner observation](docs/research/evidence/2026-10-18-local-kubernetes/infrastructure/README.md)
records two namespaces/eight policy objects, quota/Pod Security server dry-run
refusals, targeted worker RBAC denials and zero observed workloads. Two initial
discovery timeouts and two schema-invalid negative probes remain visible. The
request timeout is now 30 seconds, preserving endpoint/context pins and validation.
Workload execution is NOT RUN, NetworkPolicy enforcement is UNKNOWN and the full
live Outfitter Kubernetes adapter is not implemented. The prior four-attempt Waypoint
qualification allowance remains exhausted.

Outfitter [#17](https://github.com/EduCloud-Ecosystem/outfitter/pull/17) merged
at `b7eb50c6321a1cb39ee0642564547a652c713a02`, reviewed head `91f261af`.
Its disabled offline prototype binds one attempt to an exact cluster and namespace,
reserves before dispatch, and retains ambiguous cleanup liability. Independent
review found and verified the fix for mixed-ledger reaping that could skip owned
Docker cleanup. The [acceptance record](docs/research/2026-10-17-research-pilot-acceptance.md)
preserves that failed control. Exact-head CI passed 816 test/subtest events,
including 62 Kubernetes events, plus 26 Docker, 38 recovery and 19 consumer checks.
There is no live Kubernetes client, credential reader, CLI backend selector or
new workload allowance. Live termination, isolation and resource-cap enforcement
remain NOT RUN; historical storage-writer checks are not Kubernetes qualification.

The [local macOS runtime decision](docs/decisions/2026-10-18-local-macos-runtime.md)
selects OrbStack for this operator's Docker-compatible engine; Compose stays the
baseline and Linux/cloud Docker portability is unchanged. The subsequent
[backup and Desktop retirement record](docs/decisions/2026-10-18-orbstack-retirement.md)
records 45 cold volume restores, seven physical database clones, two current and
four historical SQL restores, and a verified native image archive/import. These
are bounded local recovery checks, not off-device or pristine-engine recovery.
All nine user-owned Desktop app/data/settings roots and eight administrator-owned
helper/link remnants are removed after a fresh authenticated cleanup. Both helper
services are stopped. The earlier official uninstall timeout and scoped permission
failures remain recorded alongside the independently reviewed completion.
Post-removal checks pass for 51 accepted container configurations (17 running,
34 historical stopped), 13 healthy checks, 57 volumes, 75 original image IDs and
147 references. Twenty-one app/service probes pass with six NOT RUN categories;
the shared engine guard passes. The uninstaller's removed Compose/Buildx links
were restored; the failed first probe and passing correction are both retained.
Eight earlier GC-lost images remain exactly recovered, with the original GC FAIL
preserved. Removed roots accounted for 38.28 GiB allocated, but immediate free
space rose only 0.99 GiB to 15.45 GiB; a later completion sample measured 13.07 GiB.
Nine purgeable snapshots were observed and left untouched; neither the initial
difference nor the intervening space change is fully attributed. Low capacity, full authentication,
reboot/startup behavior and Kubernetes workload qualification remain unresolved.
A Pro trial was observed; no license purchase was made.

## October 6–7 classroom decision (preserved)

The first user-facing computing replacement is **browser Python/R coursework
with saved files and recoverability across hosts**. Finish the usable classroom
path around Cairn, the most complete EduCloud component, and adopt JupyterHub for
interactive computing. Do not require Belay, Portage or a new Outfitter broker
before learners can run notebooks.

Reliability means an accountable operator, funded baseline capacity, a portable
course image, durable homes, bounded resource use, and independently recoverable
backups. A second temporary credit offer is useful overflow, not continuity.

## October 6–7 component assessment (historical)

| Component | Verified main | Assessment and next completion gate |
|---|---|---|
| Cairn | 7b2ab1d8efb4 | PRs #1–#9 merged. Opt-in source capture and instructor-reviewed assessment proposals pass local/browser/SQLite/PostgreSQL checks. The bounded OpenAI adapter passed four synthetic live calls, including browser approval and student feedback; PR #7 adds repeatable evaluation and offline human review; its larger baseline found one rejected proposal and score/assessability instability. PR #8 adds precise failure categories and stronger calibration records/report integrity. PR #9 applies the user-selected unassessable policy to calibration V2; 18/18 valid proposals and 36/36 provisional criterion matches passed its development recheck. Course quality/destination/retention acceptance remains. Automatic push grades now use immutable submission commits, expose revision history, and fail/retry configured webhook setup. PR #3 preserves student login after denied operator requests; verified locally and in CI. The existing pilot still runs PR #2 (`ceaee433f3a3`); no production upgrade was made in this local-first pass. Workspace navigation, pinned instructor grading policy, read-only test files, provenance and operator per-step ceilings are implemented. Live host acceptance passed. HTTPS, retention and broader assessment/operational gates remain. |
| Waypoint | 2afd881e6c54 | PRs #1–#9 merged. Real Git-push grading and bounded notebook traffic passed, including overflow rejection and freed-slot reuse. Python/R workspaces, encrypted trial and institutional recovery, dedicated-worker configuration, hard XFS quotas and nginx/Keycloak preparation are implemented. Synthetic identity/course/revocation, institutional restoration, independent-worker trial recovery and quota/HTTPS checks passed. Real institutional identity, selected-host capacity and the actual backup account remain acceptance gates. |
| Outfitter | b2cbdcad5b05 | Specifications only. Defer generalized brokering; later adopt the running workspace lifecycle as the first consumer and add a second host only after recovery is proven. |
| Belay | 89f25971749f | Working tutoring core. New PR #12 proposes authenticated institution/class isolation; it is unmerged and its current check rollup is empty. PR #11 has changed since September's audit. Neither was accepted by this pass. Not required for the computing MVP. |
| Portage | 2ec86ad0447d | Working routing components, eight open PRs with unchanged heads. September's staff-profile renderer finding still applies to those exact heads. Not required for Python/R compute. |
| verifier-contract | 9a0a84f76b08 | Existing contract/conformance foundation. Keep the required consumer-matrix work on the release backlog; not a dependency of notebook availability. |
| educloud | d002ab8817b3 | Prior computing, recovery and assessment review records merged; this follow-up records the repeatable assessment evaluation and its measured gaps. Original local strategy edits and unpublished commits are preserved. |

The October 6 baseline matched the September audit default heads. Cairn,
Waypoint and this umbrella have since advanced through the authorized merges.
Belay/Portage proposals remain separate from this release.

## GitHub Education: what changed and what remains

- GitHub Classroom retired August 28, 2026. The classroom-level Codespaces
  allowance for 50 students ended with it. Repositories and accounts remain.
- GitHub staff explicitly retained verified students' and educators' individual
  benefit: 180 core-hours and 20 GB of monthly storage allowance. Current student
  documentation still lists the personal benefit. At two cores, 180 core-hours
  is 90 running hours, not 180 hours on a two-core machine.
- Current billing documentation lists personal Free at 120 core-hours/15 GB-month
  and Pro at 180/20. Ordinary organization plans include no free Codespaces quota.
  Storage consumes allowance while a codespace exists; exhausted allowances can
  block use when no payment method is available.
- Copilot moved verified students to the distinct Copilot Student plan in March
  2026, with a changed model lineup. AI entitlements are separate from computing.
- Some Classroom integration documentation still describes the retired allowance
  beneath a retirement warning. That text does not supersede the explicit staff
  retirement notice. No official reinstatement was found in this review.

These are program-policy findings, not a check of Greg's or any student's actual
account status, billing settings, verification expiry or remaining allowance.

Sources checked October 6:
[Classroom retirement](https://github.blog/changelog/2026-08-27-github-classroom-deprecated/),
[GitHub staff benefit clarification](https://github.com/orgs/community/discussions/196615),
[individual student benefits](https://docs.github.com/en/education/about-github-education/github-education-for-students/about-github-education-for-students),
[current Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces),
[Copilot Student change](https://github.blog/changelog/2026-03-13-updates-to-github-copilot-for-students/).
The staff clarification is the May 28 comment in the linked discussion.

## Build sequence

1. Deliver the portable, one-course Python/R workspace and Cairn navigation.
2. Rehearse both kernels, own-file access, restart persistence and offline
   restore into a fresh namespace. Keep synthetic evidence separate from live
   institutional OIDC/TLS and actual second-host recovery.
3. Select the actual institution-controlled host, operator, capacity and backup
   destination. Enforce filesystem quotas, institutional roster/revocation and
   wildcard HTTPS before a real learner pilot. Separate this worker host from
   identity databases and other sensitive services.
4. Adopt Cairn's pinned instructor policy for each course, review its test harness
   and enforce aggregate execution, disk/output and isolation controls before
   relying on assessment results. The specific learner-manifest and per-step
   resource-ceiling findings are addressed by Cairn PR #2.
5. Run one real class and record availability, support effort, recovery time,
   concurrency and actual operating cost. Add Outfitter placement only when
   multiple provisioned backends create a demonstrated need.

The deployment and recovery implementation is in Waypoint `course-workspace/`;
Cairn's integration contract is `docs/course-workspaces.md`. Detailed rationale:
`docs/decisions/2026-10-06-computing-continuity.md`.

## Merged implementation and observed deployment

- [Cairn #1](https://github.com/EduCloud-Ecosystem/cairn/pull/1): workspace navigation.
- [Cairn #2](https://github.com/EduCloud-Ecosystem/cairn/pull/2): instructor grading authority and ceilings.
- [Waypoint #1](https://github.com/EduCloud-Ecosystem/waypoint/pull/1): notebook runtime/recovery.
- [Waypoint #2](https://github.com/EduCloud-Ecosystem/waypoint/pull/2): Linux archive permissions.
- [Waypoint #3](https://github.com/EduCloud-Ecosystem/waypoint/pull/3): minimal trial, bounded admission and resumable offline checkpoints.
- [Waypoint #4](https://github.com/EduCloud-Ecosystem/waypoint/pull/4): encrypted preserved-image recovery and dedicated-worker configuration.
- [Waypoint #5](https://github.com/EduCloud-Ecosystem/waypoint/pull/5): hard home quotas, quota-backed recovery and HTTPS/identity configuration.
- [EduCloud #1](https://github.com/EduCloud-Ecosystem/educloud/pull/1): priority/reassessment.

Cairn release `ceaee433f3a3ad12487824b132059fca10b7bc32` was built and
activated on the existing pilot host. The image's revision label and the running
container matched. HTTP health returned 200; anonymous classroom and grading-policy
requests returned 401. The served dashboard contains the new grading controls.
Application/database configuration was preserved, with a rollback image and
restricted on-host database/configuration snapshots retained before activation.
These snapshots are rollback preparation, not an off-host continuity solution.

The Go race suite, dashboard checks and real local browser policy-selection test
passed. The forged-score/read-only-policy Docker regression also passed **inside
the deployed Cairn container on the target Linux host**, using synthetic in-memory
records, without adding classroom data. Target data counts were unchanged.

Waypoint's [fresh linux/amd64 build/recovery run](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37586482789)
passed at PR #2's exact head. It executed both kernels, learner/network isolation,
workspace recreation, private offline archives, restore into fresh volumes and
overwrite refusal. The earlier run exposed Linux's chmod-after-chown restriction;
the fix sets archive permissions before transferring ownership without adding
capabilities. This complements the local arm64 rehearsal; it is not a cross-host
archive transfer or a live institution-authenticated notebook deployment.

## Deployment facts still requiring completion

The existing Cairn machine has 4 GB RAM and also hosts its database. It is not the
separate notebook worker. No remote notebook host/account/budget is recorded;
that connection/selection is pending from the operator. A local synthetic trial
is now available without buying infrastructure. No cloud purchase was made.

Cairn doctor reports no failures, with outstanding warnings for plain-HTTP
webhook configuration and unset grade retention. Existing operator authentication
remains enabled. The service still uses shared-kernel grading containers. Do not
read health/CI success as approval for real learner data without HTTPS, retention,
institutional policy and the relevant isolation/assessment review.

The notebook deployment still needs its dedicated worker, live Keycloak roster
and revocation tests, actual wildcard DNS/certificates, target-host quota/mount
and capacity acceptance, and an approved SFTP/S3 backup account. Synthetic quota,
HTTPS proxy and independent-runner recovery checks now pass, as recorded below. Existing Belay/Portage findings
remain outside this release.

## Minimal testing version and next completed build step

The operator trial is reduced to **one active synthetic learner**, one CPU and
1 GiB learner RAM, plus the separately capped 1 GiB Hub. It runs locally at no
additional hosting cost. The optional remote target is a separate 4 GiB / two
shared-vCPU / 80 GiB Ubuntu worker, using an SSH tunnel to the loopback-only
notebook port. DigitalOcean's Basic Regular bundled plan is $24/month before
taxes/backups as checked October 7 against its
[published pricing](https://www.digitalocean.com/pricing/droplets). The proposed
Droplet sizing has not been accepted on an actual 4 GiB worker.

Waypoint's `course-workspace/pilot.py` initializes private stable credentials,
starts/stops the trial without deleting files, and reports its status. The
[operator guide](https://github.com/EduCloud-Ecosystem/waypoint/blob/main/course-workspace/MINIMAL-PILOT.md)
contains local and SSH-tunnel setup. Test users alice/bob share a generated
password, with one active server at a time. This is not public student login.

The next continuity build step, `pilot.py checkpoint`, is implemented too: stop
the Hub and learner, archive the quiesced volumes with checksums and runtime image
metadata, then resume the previously running Hub. Failed backup attempts also
attempt to resume it. A previously stopped Hub remains stopped. Commands share
an operation lock, and existing archive paths and unrelated Hub containers are
refused. Direct Docker operations still require operator coordination.

Local arm64 acceptance passed at runtime commit `0da7491`: Python/R over notebook
WebSockets, inspected 1 GiB/one-CPU limits, blocked Internet access, a refused
second learner, file persistence through restart/checkpoint, and restored files
and kernels in fresh volumes. Thirteen unit tests passed, including failure
recovery and operation locking. The [fresh Linux amd64 run](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37668279326)
passed both the original two-user rehearsal and the new minimal-trial recovery
at that exact runtime commit. A real browser opened the Python/R launcher,
executed the Welcome notebook and saved its output; the CLI checkpoint then
resumed that Hub successfully. Checkpoint archives are private but remain local and unencrypted;
same-host restoration is not a second-host or off-host recovery claim.

## Encrypted recovery and hosted preparation (October 7)

The user selected **build and test locally first**. No Droplet, backup account,
public endpoint or institutional client was provisioned by this release.

Waypoint PR #4 packages quiesced files, private configuration, deployment scripts
and immutable Docker images into an encrypted Restic repository. Wrong keys,
ambiguous snapshot IDs, incompatible architectures and occupied restore targets
are refused. Backup status records failures and stale success; scoped retention
is previewed unless explicitly applied. Generated worker configuration and
systemd timers remain disabled until operator setup. Recovery currently supports
synthetic local-test deployments only; institutional migration is a further gate.

The [independent-worker rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37673554357)
passed at head `65d6188c2448a10ad06cac24e1161c3c9d5dd11f`; PR #4 merged as
`f99e7cebcb8d5e6db8083dfea92ba67be3ca343d`. Source and replacement jobs used
separate fresh Linux runners, transferring only the encrypted synthetic package
and metadata. The replacement rejected cached source images, restored saved files
and ran Python/R. This proves portable packaged recovery on that architecture;
it does not validate the future institution's backup account or service uptime.

Waypoint PR #5 merged as `0e92189689d0ad4af40131140d49651437f9491d` and
provisions hard byte/inode quotas on an administrator-prepared,
dedicated XFS mount. It never formats a physical device. Missing or stale health
status blocks new learner starts; actual limits remain enforced by the filesystem.
The synthetic Linux test exhausts a home, checks another learner can still write,
restores an encrypted quota-backed package and detects altered enforcement.
Ordinary backups from PR #4 remain supported.

The release also renders private nginx/Keycloak configuration. The client secret
is deliberately empty until installed by the operator. Actual nginx tests check
root/user TLS routes, redirect behavior, forwarded-header replacement, WebSocket
upgrades and unknown-host rejection. These are proxy tests, not an institutional
login or browser acceptance claim. Validation at runtime head `7649109` passed:
[quota-backed recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205120),
[nginx and unit checks](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205127),
and [independent-worker recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205180).
The final documentation head `26128636b1151ed049c220cd1135c8504c391f37` was also
checked before merge: [quota](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747268),
[policy/proxy](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747049),
[recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747267).

The synthetic identity/course rehearsal is implemented (evidence below).
Institutional/OIDC encrypted recovery is now implemented with current-roster
configuration and fresh Hub sessions (evidence below). Hosted acceptance needs
the selected worker and backup account: real institution login/revocation,
wildcard certificates, reboot/mount behavior, load, recovery objectives and the
Cairn assignment/submission/grading path. Host disk/log monitoring, paging,
retention/departure procedures and institution-wide recovery acceptance remain work.
No Outfitter broker is needed to finish this first course.

## Authenticated course rehearsal (October 7)

The disposable harness uses real Keycloak, JupyterHub, Forgejo OAuth/repositories
and a pinned Cairn build. Cairn's Git-host login and the Hub's Keycloak login stay
separate. The browser follows Cairn's actual workspace link; notebook saving and
repository submission remain explicit separate actions.

The Forgejo/Cairn phase passed locally on macOS with a synthetic source-file
fixture: operator login, roster-only assignment acceptance, private repository
provisioning, student/operator and own-grade boundaries, and 10/10 versus 0/10
against the instructor's pinned tests. A learner's forged 999-point rubric had
no effect. The browser rehearsal exposed and verified the Cairn session fix in
[PR #3](https://github.com/EduCloud-Ecosystem/cairn/pull/3), merged as
`260984572cd2946ce8685c4d4b74d117c32fffea`. Its production pilot was not upgraded.

[Waypoint PR #6](https://github.com/EduCloud-Ecosystem/waypoint/pull/6) merged as
`8b0de72104940b8bdebac10010b00c1d085c4b91`. The final reviewed head
`91c4804d81bc57046839b4a434b6a0316073c404` passed the
[full Linux course rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782788),
[quota/recovery regression](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782945)
and [policy/HTTPS checks](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782865).
All 31 local unit tests passed. The accepted report records Cairn `260984572cd29`
and the actual GitHub PR merge checkout `60420007732a0e175589a797ce7a1f6826585573`.

Full acceptance verified Keycloak PKCE authentication, per-user HTTPS, real
Python/R kernel execution over WSS, explicit saved-file transfer, and correct
and incorrect pinned grading. Inspected screenshots show the saved `solution.py`
open in JupyterLab and the learner-visible instructor test with both grading
attempts. Authenticated peer file access, unrostered login, previous-session
access and respawn after roster removal were denied; no learner server remained
active, and the saved file survived revocation.
The notebook roster guard now returns an explicit 403 with an instructor-contact
message instead of converting an access denial into a generic server error.

The full harness creates its own disposable XFS image with hard quotas and a
short-lived fixture CA. Python/WSS clients and the Hub trust that CA explicitly;
the browser uses a fixture certificate exception. No certificate or hosts entry
is installed on the user's computer. The workflow publishes only bounded
synthetic evidence and screenshots after success, not fixture keys/databases.

This is not acceptance of an institutional realm, funded host, public DNS/TLS,
real backup account or class-size capacity. It requests grading explicitly;
automatic Forgejo push-webhook delivery, institutional identity-service recovery,
roster synchronization and automatic notebook submission remain separate work.

## Institutional workspace recovery (October 7)

[Waypoint PR #7](https://github.com/EduCloud-Ecosystem/waypoint/pull/7), merged as
`0be6bfb5973aff5764ec82d7f15d91b58bdad1b3`, extends encrypted Restic packages to OIDC courses. Recovery
requires a current operator-supplied roster and client credential while binding
the original issuer, client ID, public origin and home limits. All archived
homes survive, including retained work from removed learners. The replacement
starts with a new Hub database/cookie secret, so obsolete Hub sessions/tokens
are not recovered. No service starts automatically.

Final head `003e673c82343598b9a87462c22faad9c4465905` passed all 34 local unit tests
and these workflows:

- [Institutional recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362234):
  encrypted backup, destruction of source Hub/volumes/filesystem, current-roster
  restore on a fresh XFS filesystem, wrong-key/missing-current-config refusal,
  fresh Hub sessions, removed/unrostered and peer denial, saved files, Python/R,
  hard quota verification and active revocation with retained work after recovery.
  The successful report and browser screenshot of reopened coursework were inspected.
- [Independent-worker trial recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362307):
  source backup and restoration on a separate clean runner passed.
- [Hard quotas](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362235),
  [complete course rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362251),
  and [policy/HTTPS](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362248): passed.

The institutional report records GitHub's tested PR merge checkout
`1201fe3efbdeca4b5bd2cb3362461b83c20f3bd3`; its saved image IDs are Hub
`sha256:e85c04026cfe2fe20ce09ddf5164ce646d4735a881fff64c30ac4259abae4df5`
and course `sha256:0e6ea23721d343dbed266e99884baf2c99e9d2033996abae1bb640cd726c22dd`.
See Waypoint `course-workspace/RECOVERY.md` for current-config requirements,
cutover, quota timers and backup/health service path updates.

The operator must supply genuinely current configuration; the tool cannot verify
its freshness. The IdP database/realm, DNS/TLS, CA trust and custom proxy/Compose
configuration remain separate dependencies. Institutional acceptance used an
independent surviving synthetic Keycloak instance on the same runner; it does
not establish institution-wide disaster recovery or acceptance of a real
SFTP/S3 account. No funded worker, public endpoint or production Cairn service
was changed.

Automatic Forgejo push grading and bounded notebook traffic are now covered
by the follow-up below. Real-host acceptance still needs selected
worker/backup capacity, institutional identities, TLS, operational monitoring
and recovery objectives before admitting learners.

## Automatic push grading, bounded traffic and LLM assessment (October 7)

[Cairn PR #4](https://github.com/EduCloud-Ecosystem/cairn/pull/4) merged as
`55940c218554f97fe1349c22415061b54000ad5f`. Signed default-branch pushes now
queue the exact submission commit; later repository changes cannot alter the
job's input. Each result records the submission commit and pinned instructor
policy, and student history shows the evaluated commit. Configured webhook
setup errors retry visibly rather than silently activating an incomplete repo.
Forgejo hook reconciliation restores active push events and the current secret.

The full local Go race suite and [Cairn CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37693621216)
passed. Real local Forgejo acceptance produced six commit-specific grades from
six rapid Git pushes, with correct/incorrect results despite a forged learner
rubric. Thirteen replayed deliveries, including after restart, added no grades;
bad signatures were denied and a draft-branch push was ignored. The inspected
student screenshot shows all six evaluated commits.

[Waypoint PR #8](https://github.com/EduCloud-Ecosystem/waypoint/pull/8) merged as
`2afd881e6c54dfe1cb56ebe67e5a1e8089aef6ef`, after all required checks passed on
head `11e95eb5078e9452abf6d2993b5b4cb361921a6b`. The
[full Linux course rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37693819845)
used real notebook work, Keycloak/Hub, Forgejo and Cairn merge `55940c218554`.
Its downloaded PASS report and notebook/student-grade screenshots were inspected.
Six pushes produced the expected commit-specific grades in 21.872 seconds;
13 replays produced no extra grades. The report records GitHub's synthetic PR
merge checkout `7a55d86403b46704bb6007c3406edddf533ed304`, distinct from the
reviewed head and final squash merge.

With two active learner notebooks, 24 authenticated file requests at six-way
concurrency and simultaneous Python/R execution passed. A third authorized
learner received HTTP 429; after one learner stopped, the freed slot could be
reused without changing another learner's saved file. Observed file-request
p50/p95 were 0.0345/0.0494 seconds. These are synthetic observations, not
production capacity estimates. The same run verified peer-file isolation,
roster denial, active revocation, old-session denial and retained saved files.

The [institutional recovery regression](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37693819583)
and [policy/HTTPS checks](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37693819303)
also passed, alongside 34 local unit tests. Acceptance used disposable synthetic
identities, repositories, containers and fixture-only webhook forwarding.

These tests do not establish production class-size capacity, an exactly-once
guarantee across worker crashes, other Git hosts' live delivery, or real-host
identity/TLS/backup acceptance. Cairn's production pilot remains on PR #2; no
production service or paid infrastructure was changed.

Greg's selected next assessment direction is **LLM-assisted feedback plus
proposed scores**, with flexible deliverables. Cairn `docs/llm-assessment.md`
records the pipeline: instructor-owned rubric, immutable submission and artifact
provenance, bounded format extraction, evidence citations, approved model data
destinations and budgets, deterministic schema/score/citation checks, then
instructor review/edit/approval before publication. Structural checks do not
prove that a model's judgment is correct. The earlier push-grading release did
not implement this pipeline; the review foundation is now covered below.

## Local assessment review foundation (October 7)

[Cairn PR #5](https://github.com/EduCloud-Ecosystem/cairn/pull/5) implements the
local artifact/proposal/review workflow, disabled by default and enabled with
`CAIRN_ASSESSMENT_REVIEW=1`. Merged as
`8c12a681bbfdb4baa201b77ccd48b33ac19b5535` after
[CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37701984975) passed on
head `82b20fa4760b2204575fcda7af37971b5388e3bb`. The new PostgreSQL CI job also
exposed an old nanosecond-precision test expectation, corrected to microseconds.

Instructors save a hashed assessment rubric and capture exact repository paths
at the recorded submission commit. Bounded extraction supports text, Markdown,
Python, R and notebook source. Missing, unsupported, unsafe or oversized files
block assessment. Source bytes, digests, locations and extraction version are
preserved privately. Notebook outputs/attachments are excluded from extracted
source; direct uploads, optional paths and PDF/Office/images remain future work.

Fixture or instructor-imported proposals contain per-criterion feedback,
uncertainty, scores and validated citations. The dashboard lets instructors
inspect evidence, edit or reject proposals, and explicitly publish. Publication
atomically checks rubric/commit/activity/roster freshness and writes the grade
with the review. Original proposals remain distinct from edits; concurrent or
replayed approvals cannot duplicate a grade. Students see only published
feedback. Deterministic and reviewed grades are separate history entries, not
an automatically combined course score.

The full local Go race suite and vet, 25 dashboard tests/build, and disposable
PostgreSQL conformance passed. PostgreSQL publication checks are now in CI.
Browser acceptance on the final build imported a synthetic proposal, changed
6/10 to 8/10, edited feedback, published, refreshed the instructor score and
verified the student's approved feedback/citations; screenshots were inspected.
This fixture uses synthetic checkout content, not a new real-Git or model test.
Tests also cover forged scores/citations, private drafts, stale activity,
unassessable criteria, rollback, concurrent approval, SQLite reopen, roster
erasure and exported-grade retention. Approved evidence/review records are
purged with their exported grade; other captures remain until roster erasure.

PR #5 did not connect a model provider; the following release adds the bounded
OpenAI adapter. No real student data was sent externally and no production
deployment occurred. Production gates include quota-enforced capture workers
(Git download size is not bounded by extraction limits), pagination, draft
retention, webhook completeness/out-of-order
acceptance and an explicit policy for combining reviewed/test results.

The next build after that foundation was the bounded provider adapter below.
Instructor-scored evaluation, destination approval and measured feedback/score
quality remain prerequisites for real student content.


## Bounded OpenAI assessment pilot (October 7)

[Cairn PR #6](https://github.com/EduCloud-Ecosystem/cairn/pull/6) adds the actual
provider path, merged as `58b0264ed3bdf0d51a680d4000108fed836a072d` after
[CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37710801209) passed
on head `b42ffa08fe4447c0c5737a8c8c8508b8a042dac7`. It is separately opt-in
behind operator authentication, review mode and an explicit classroom allowlist. The configured private key was read from an
owner-only file outside Git. No production secrets, deployment or real student
content were changed or transmitted.

The Responses API adapter uses pinned `gpt-5.4-mini-2026-03-17`, strict structured
output, a fixed destination, `store:false`, no tools or automatic retry, and
16,000-byte extracted input / 4,096-token output / 60-second request limits.
It sends rubric criteria and aliased source segments; roster metadata, filenames,
repository URLs and notebook outputs are omitted. Identifiers inside source or
rubric text are **not automatically redacted**, and `store:false` is not a
zero-provider-retention guarantee. See Cairn's `docs/llm-assessment.md` for the
verified API contract, exact controls and provider data-policy references.

A transactional ledger reserves usage before transmission: 20 requests per UTC
day per shared store, 3 per learner enrollment and 200,000 reservation units.
Units are request bytes plus the output allowance, not exact tokens or a dollar
cap. Known provider-reported tokens are recorded separately. Failed/uncertain
requests keep reservations, and deleting evidence cannot refund them. The ledger
retains minimal pseudonymous attempt/usage metadata without prompts or grades;
automatic ledger expiry remains unimplemented. One active request is allowed per
process; the durable pause control stops new requests and survives restart.
Generation checks freshness before and after the call, saves only a pending
proposal and cannot publish a grade. Instructor import cannot spoof provider
attestation.

Local verification passed Go race/vet/build, 25 frontend tests/typecheck/build,
and PostgreSQL 17 conformance. Tests cover preflight gates, errors, invalid model
output, no retries, state changes during a call, concurrent admission, restart
budgets/pause, and erasure without refunds. Four live calls used only hand-authored
synthetic examples: correct 10/10, incorrect 0/10, injection-only with both
criteria unassessable, plus browser generation followed by explicit approval and
student feedback/citation display. The first three remained unpublished proposals.
Reported input/output tokens were 431/259, 410/346, 414/335 and 380/140. Browser
pause persisted after refresh. Screenshot inspection confirmed the approved
student view.

These results establish the connection and workflow, not broad grading quality.
An incorrect-answer uncertainty statement was poorly calibrated. Next: a
permissioned instructor-scored benchmark, including partial/ambiguous work,
format diversity, prompt injection, score agreement, evidence accuracy and useful
feedback. Retention, course destination approval, billing-aware controls and
production capture/queue capacity remain course-readiness gates. The existing
production pilot remains on Cairn PR #2 (`ceaee433f3a3`).


## Repeatable assessment evaluation (October 7)

[Cairn PR #7](https://github.com/EduCloud-Ecosystem/cairn/pull/7), merged as
`3275ce7d155eb36f2438438b169e5e7c45fa38f5`, adds `assessment-eval run`,
`packet` and `review`. [CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37713835038)
passed on head `d78dab3e9bd8c7b94a536b55df512fce188cc442`. The bundled 12-case corpus covers
correct/incorrect/partial/terse text, Python, R, notebook source versus output,
prompt injection, missing files, unsupported formats and malformed notebooks.
References are agent-authored and provisional, not instructor-scored labels.
Offline extraction is the default; an explicit live run is limited to 9 or 18
sequential provider attempts in a dedicated private SQLite store. Every trial
saves a report; failed writes stop further calls. No grades are created.

The offline HTML packet lets an instructor read evidence before revealing model
feedback, enter independent scores and evidence/feedback/uncertainty ratings,
and export/import a partial worksheet. Review validation binds the worksheet to
the exact report, rejects stale/duplicate/out-of-range judgments and keeps blank
ratings incomplete. Reviewer identity is locally asserted, not authenticated.
Completion does not enable a course or publish grades.

The baseline made 18 live synthetic calls across two trials per case: **17 valid
pending proposals**, one rejected `invalid_proposal` on Python source, and six
expected extraction blocks. Accepted proposals matched **31/34 provisional
criterion references**. Numeric mean absolute error was 0.067 points across 30
numeric pairs; two additional criteria disagreed on zero versus unassessable.
Only **6/8 completed case pairs** had stable scores/assessability. Reported usage
was 8,224 input and 5,575 output tokens, including the rejected attempt. Database
inspection confirmed 18 reservations and zero grades. The live command exited
nonzero for the recorded failure; it was not retried or hidden.

One mixed-injection trial withheld credit for a correctly stated mean because it
wanted work the rubric did not require. Injection-only content alternated between
zero and null, exposing both model variability and a missing-evidence policy
ambiguity that needs instructor resolution. Some uncertainty wording was poorly
calibrated. Valid citation locations are structural checks, not proof of semantic
support. No actual human ratings have been supplied: the review packet has 34
pending judgments. Browser QA ratings were explicitly synthetic and excluded.

Go race/vet/build and CLI/packet tests passed; Playwright verified export/import,
preservation of a negative quality rating, partial-review status and rendering.
Cairn `docs/assessment-evaluation.md` and its frozen baseline JSON contain the
reproduction procedure, digests, counters and limits. Next: instructor review of
missing-evidence/partial-credit policy, then a held-out permissioned benchmark
with agreed quality thresholds. Do not tune to this smoke corpus and claim
independent validation. Production remains unchanged on Cairn PR #2.


## Calibration controls and failure diagnostics (October 7)

[Cairn PR #8](https://github.com/EduCloud-Ecosystem/cairn/pull/8) merged as
`fddf61f60cc3801f642f474a143cd7e1e4a96ab8` after
[CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37717638686) passed
on head `0b5766246b8bb9542c2dd1461f8832c636b53323`. It records bounded
validation categories for invalid points, missing/invalid/excessive citations,
criterion coverage/identity, evidence integrity and feedback limits. Provider
errors remain free of rejected response bodies, source, filenames and credentials.
Usage reservations and no-auto-retry behavior are preserved. The existing
baseline's generic `invalid_proposal` cannot be diagnosed retrospectively.

The offline review packet now displays recorded failure codes and separately
records a proposed missing-work policy (`zero` or `unassessable`) with reviewer,
time and rationale. Policy review cannot complete human criterion scoring and
does not rewrite the provider prompt, frozen baseline, course rubric or grades.
Legacy worksheets remain readable with policy status pending. A real instructor
policy decision and all 34 human judgments are still pending; browser QA uses
explicitly synthetic entries and is excluded from calibration evidence.

Saved reports are checked against re-extracted bundled source, original bytes,
segments, revision, rubric and input/proposal digests. Substituted evidence,
contradictory extraction states and missing outcomes in a completed live run are
rejected. This establishes corpus consistency, not cryptographic attestation of
provider execution or authenticated reviewer identity.

The full Go race suite, vet/build, diagnostic/no-retry and report-substitution
regressions passed locally. Browser QA verified policy export/import and showed
policy completion with zero completed score judgments. The saved baseline was
re-rendered without new provider requests; no additional API spend, real learner
content, production deployment or published grades were involved. Next remains
instructor calibration and deliberate policy implementation before a held-out
permissioned benchmark and course acceptance.


## Selected unassessable policy and V2 recheck (October 7)

The user selected **“Mark it unassessable until instructor review”** for readable
submissions containing no relevant substantive answer, including prompt-injection-
only content. [Cairn PR #9](https://github.com/EduCloud-Ecosystem/cairn/pull/9),
merged as `7b2ab1d8efb43b48453f0b7e24a003bc40daafa0` after
[CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/37723869637) passed
on head `efd1af31195e3c5fa684de062a507f7841bf3539`, implements this in `synthetic-eval-v2`'s captured instructor rubric: all criterion
points are null in that situation. Genuine partial/incorrect attempts still
follow rubric point rules; unreadable/missing/unsupported artifacts block
extraction. No production course rubric, global provider prompt or published
grade was changed. The user decision is recorded separately from human ratings.

V1 remains frozen and its reports/worksheets are readable. V2 keeps the same
source cases and provisional score references, while clarifying no-work handling
and the existing rule against demanding calculations not required by the rubric.
This is a development recheck of a known corpus, not an independent benchmark.

The two-trial live recheck produced **18/18 valid pending proposals**, **36/36
provisional criterion matches**, **9/9 stable score/assessability pairs**, and six
expected extraction blocks. Both injection-only trials returned null for both
criteria; mixed injection-with-answer and partial work retained 2/4 and 2/6.
Reported usage was 12,148 input and 5,307 output tokens. Database inspection
confirmed 18 reservations and zero grades. The full Go race suite, vet/build and
version-integrity tests passed; the old V1 packet rebuilt successfully. Frozen
results are in Cairn `docs/evaluations/2026-10-07-unassessable-v2.json`.

Policy selection is now resolved for this calibration. All 36 V2 human criterion
ratings remain pending, as do feedback usefulness, semantic citation review,
a held-out permissioned benchmark, destination/retention acceptance and production
readiness. The earlier V1 failure and disagreements remain in the evidence record.
