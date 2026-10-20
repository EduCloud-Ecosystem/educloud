# Assessment preparation, estimates, allocation drafts and queued grading — October 19, 2026

The component changes below are accepted and merged within their recorded
source, regression and integration scopes. The implemented assessment slice prepares closed benchmark manifests and previews
unverified receipts through the operator CLI. It accepts no temporary upload,
executes no benchmark and creates no workspace or broker ledger. This is partial
A1/A2 of the [assessment backlog](../strategy/research-pilot-build-backlog.md).
The later A4 calculation slice below is also merged with explicitly synthetic
inputs. Neither increment accepts the complete upload-to-allocation workflow.
The later initial A5 export increment below adds usable local draft packages;
it does not establish current application or resource readiness.

## Revisions and ownership

| Component | PR | Independently reviewed head | Merge revision |
| --- | --- | --- | --- |
| EduCloud canonical contract | [#37](https://github.com/EduCloud-Ecosystem/educloud/pull/37) | `1184ab2c2a0c82aa437b2d146f22dbae2b98efa7` | `bf9bc615fbfef5055f231f473e784b1183c73dad` |
| Outfitter pure receipt command | [#18](https://github.com/EduCloud-Ecosystem/outfitter/pull/18) | `2369ffb223a8615321a819c08e87b6f19d650745` | `de65bdab9303395226ebfb35e0e0740ab19b4d8e` |
| Waypoint preparation and preview | [#49](https://github.com/EduCloud-Ecosystem/waypoint/pull/49) | `c47351f46186d7fa055a7f486516f4dac0aeb274` | `d70aaccc454332cb5bacf31e93c99e2ce0b420cd` |
| Waypoint initial synthetic estimates | [#50](https://github.com/EduCloud-Ecosystem/waypoint/pull/50) | `053bb1ef5ff5e7a359e9f1e2a0cfbdd8d2a4f6ad` | `db7ad40e05baadba7b5063ed5003c9cdffe1eda8` |
| Waypoint initial allocation drafts | [#51](https://github.com/EduCloud-Ecosystem/waypoint/pull/51) | `a4bdc289c9fef7ddbdc03f1707db69e2e6fbf709` | `2d94f87a73fd3f606bf6a246aabb0a1ee2bb9465` |
| Waypoint Explore/Accelerate drafts | [#52](https://github.com/EduCloud-Ecosystem/waypoint/pull/52) | `9b782a17cc797d46d664b27e967b90611f6faf60` | `45ecd81cb5970d86a30a1f70e61e8e101fc7972a` |
| Cairn pinned grading context | [#33](https://github.com/EduCloud-Ecosystem/cairn/pull/33) | `70b984083fa711b12ae30bc22732d831a0b1ba1e` | `ab339c44248eca2f6c03c22ef951215e8969472a` |
| Cairn optional durable grading dispatch | [#34](https://github.com/EduCloud-Ecosystem/cairn/pull/34) | `2be331d245a989490ca815a3c71b12c0d2ff0ed0` | `536da6a58b8178c9da15157e385c5a67f5782ef1` |
| Cairn authenticated grading inspection | [#35](https://github.com/EduCloud-Ecosystem/cairn/pull/35) | `3b0adc4a8faab0aa1aee491b2d0b60e984c64219` | `912b9e1d035a83fa801096748627ad006dbba1d4` |

Each component has one authoring owner and a separate reviewer. The coordinator
owns integration acceptance and merging. The canonical-document owner is
frozen; Portage needs no new code for this Python/R preparation slice. Belay,
`portage-local`, Ben's Outfitter #1–#5 assignments and dirty primary checkouts
remain outside this increment. A separate reporting chat consolidates deliveries;
the existing coordinator follow-up tracks owners without competing edits.

## Implemented boundary

Waypoint adds `assessment-prepare`, `assessment-validate` and
`assessment-preview`. These return before Store/Broker initialization. Closed
ASCII/integer-only JSON, bounded regular-file reads, reviewed recipe identities,
absolute expiry and per-attempt reservation declarations define preparation.
The shared fixture declares one of twelve planned attempts: partial coverage
remains unverified and grants no admission, allowance or execution authority.

Preview calls the explicitly selected local `outfitter assessment-receipts`
executable with bounded transport and a deadline. That pure command validates or
projects one receipt pair before opening a ledger or constructing a provider.
Both sides check exact canonical digests and manifest/project/attempt/stage/
sample/reservation/environment/hardware bindings. They expose closed typed
metadata rather than raw output, filenames or arbitrary diagnostics. The legacy
study-bundle exporter remains separate and is not an assessment export route.

Reservation ceilings, conservative accounting, measured consumption and provider
charges remain distinct. Unsupported measurements and unknown reuse remain null.
Cleanup observations are untrusted claims: external termination, credential
revocation and temporary/recovery-copy deletion cannot be inferred from a
provider's execution-resource deletion assertion. Imported verified outcomes and
all-resolved untrusted cleanup are rejected; uncertainty retains quarantine,
reuse denial and liabilities. No report retention is finalized here.

Cairn separately captures stable queue job identity, immutable submission and
instructor policy before enqueue, then carries them through Worker and Service.
Ambiguous or legacy targets are refused before checkout; operators review and
manually re-enqueue old work. Deadline-locked submissions remain eligible for
manual grading, while webhooks remain active-only. Ordinary runner configuration
is unchanged. Those #33 results did not establish durable dispatch or atomic
grade/run publication. The later #34 increment below adds a bounded optional
protocol; neither change installs the Outfitter adapter into production.

## Evidence and retained failures

The [machine-readable integration result](evidence/2026-10-19-assessment-preparation/assessment-integration.json)
pins both component heads, the executable hash, canonical manifest/receipt
digests and each of 37 passing checks. The
[portable checker](evidence/2026-10-19-assessment-preparation/check_integration.py)
runs the actual Go command and Python CLI with public fixtures, including legacy
projection and marker exclusion. Seven attack classes are refused by both:
verified cleanup, all-resolved untrusted cleanup, contradictory active execution,
wrong attempt binding, populated unknown metrics, free-content fields and
conservative charges substituted for measured CPU. No new files were observed
in the isolated work directory/home. This observation and source review do not
constitute a whole-machine filesystem or network audit.

| Evidence | Result and scope |
| --- | --- |
| Cross-language operator integration | **PASS** — 37 checks; actual pure Go/Python programs, no workload/provider dispatch. |
| Waypoint local suite | **PASS** — 489 tests, including the 32 focused assessment tests as a subset. Independent reviewer matched the log hash, exact head and result. Warning-as-error invocation is owner-reported because the log does not contain its command line. |
| Waypoint hosted regression | **PASS** — [run 39337782583](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39337782583), `controls` and `actual-docker`; optional `clean-source-builds` **SKIPPED**. The Docker job covers the existing workflow, not assessment execution or new source-image promotion. |
| Outfitter local suite | **PASS** — final constrained uncached race run: all nine packages, 897 passing test/subtest events, zero failures and two expected skips. The first run remains **FAIL**: 890 passing events, four failing leaf controls plus two failed parent groups, and two skips. All six attachment cases and the retention case also pass unchanged in the targeted recheck: nine events including parents. |
| Outfitter hosted regression | **PASS** — both `go-and-docker` and `storage-writer-qualification` in [run 39338282015](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39338282015). The race/static, existing Docker lifecycle, recovery and consumer steps passed. |
| Cairn local race suite | **PASS** — 1,004 passing test/subtest events, 482 top-level tests included in that total, 15 gated skips. Focused 51 events/eight top-level tests overlap the full suite. |
| Cairn hosted regression | **PASS** — all eight checks at the reviewed head: [CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39337372434), [recovery](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39337372456), [synthetic consumer](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39337372428). |
| EduCloud contract/review | **PASS** within source/document scope; no configured hosted checks were reported, so remote CI is **NOT RUN**, not passed. |

Original failed evidence remains retained. Outfitter's independent review
reproduced five failing subcases before fixing untrusted verified cleanup and
active/terminal contradictions. Cairn's initial suite missed locked-submission
eligibility; the coordinator reproduced two failing subcases, then accepted the
shared active/locked eligibility fix after fresh tests and review. Two coordinator
harness assumptions also failed: the frozen fixture explicitly records
`reused: false`, and the Go executable reports rejection as fixed JSON on stdout
with a nonzero exit. Correcting these checks required no product change; a
separate null-reuse case verifies the genuinely unknown value. Independent review
also found that two negative probes could pass for unrelated legacy restrictions;
the final checker uses matching synthetic observation types and a positive
baseline to isolate the intended guards. It refuses an existing result file and
writes exclusively so a failed rerun cannot masquerade behind stale PASS evidence.
The [evidence index](evidence/2026-10-19-assessment-preparation/verification.json)
records original hashes and final checks without rewriting those failures as
passes. Full raw local logs remain in the operator's protected evidence archive.

## Initial A4 synthetic estimation

Merged Waypoint #50 adds the actual `assessment-estimate` operator command for
one or two synthetic series. Each retained receipt is validated through the
merged Outfitter pure command. Exact rational affine models fit per-size repeat
means for process CPU and whole-attempt execution duration in the analysis
stage. Held-out observations only evaluate the fixed model; they never change
its coefficients. Units, rounding, receipt digests, repeat variability, held-out
errors, exclusions, unknown dimensions, OOM and extrapolation limits remain
visible. Additional overhead must be explicitly outside modeled execution and
declared once or per attempt. Capacity and instructional concurrency/storage
assumptions remain separate from total consumption.

Every result is provisional, with readiness, execution, upload, actual-resource
acceptance, cleanup trust and retention finalization false. The example's
13,600 CPU nanoseconds are invented arithmetic inputs, not a Python/R performance
or capacity observation. No confidence interval, provider-unit/credit/dollar
conversion, resource recommendation or program submission is produced.

Independent exact-head review is **CLEAR**. The owner suite has **512 passing
tests**, including the **55 assessment tests** (32 inherited plus 23 new) as a
subset. The reviewer matched the log and checked all 175 archived Outfitter
source files against merge `de65bdab`. The
[exact-head CI](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39340371209)
passed `controls` and `actual-docker`; optional `clean-source-builds` was
**SKIPPED**. The Docker check remains legacy regression evidence, not execution
of an assessment workload. Reviewed and merged trees match
`73efa2e735c24c9b22644f8164d05886d19f1f85`.

The coordinator separately ran **32 passing checks across eleven actual CLI
scenarios** using its reviewed pure validator binary: exact coefficients,
dimensional totals/hours, two-series comparison, canonical ordering, held-out
perturbation, missing CPU, unknown overhead, OOM, charge-only legacy data and
duplicate/free-content refusal. Authority flags and remaining cleanup liabilities
survive. This is additional integration evidence, not 32 additional workloads.
The [integration record](evidence/2026-10-19-assessment-estimation/a4-integration.json),
[portable checker](evidence/2026-10-19-assessment-estimation/check_integration.py)
and [evidence index](evidence/2026-10-19-assessment-estimation/verification.json)
retain the source pins and hashes. The checker requires a fresh result path and
a trusted operator-selected binary; it does not attest the binary's build.

Review of the reusable checker found optimized Python could remove assertions,
and one duplicate-attempt probe also repeated its cleanup ID. An isolated
pre-fix optimized failure-control witness is retained. The final checker uses
explicit operational exceptions, derived outcome counts and separately isolated
attempt/cleanup identity probes; its final 32-check run passed under
`PYTHONOPTIMIZE=1`. Earlier normal 31-check PASS records remain historical evidence
with their coverage limits, not rewritten results.

## Initial A5 draft allocation exports

Merged Waypoint #51 adds actual `assessment-export-preview` and
`assessment-export` commands before Store/Broker initialization. Closed retained
estimates and bound manifests, explicit operator narrative, a selected profile
and a digest-bound operator-supplied font produce a reconstructable preview.
Export requires its exact approved digest; changed input or font invalidates
approval. This is local export consent, not authenticated scientific,
institutional or application approval.

ACCESS Discover, NAIRR research draft and NAIRR Classroom draft have distinct
layouts and fields. Other ACCESS tiers are explicitly refused at this revision.
NAIRR sources remain blocked/unverified; no access restriction was bypassed.
ACCESS's fixed public source can be explicitly fetched before preview, but a
successful unreviewed fetch never promotes current requirements. Export performs
no hidden refresh. Resource selection, external documents, scientific review,
eligibility and form correspondence remain outstanding.

Each fresh local package contains editable narrative/source, PDF, matching
JSON/CSV worksheet, retained preview, requirements/missing-document record and a
hash inventory. CSV cells are guarded as literal text. Narrative is explicit
plain text; paths, upload hashes, raw logs and unknown metadata cannot enter
through the closed estimate/manifest schemas. Unknown measurements, untrusted
cleanup and liabilities survive. The old source-containing study exporter is
not used. This does not authenticate manually supplied science or detect private
information deliberately typed into an approved narrative.

Publication uses a fresh descriptor-relative directory, restrictive permissions
and exclusive file creation. `package.json` is a **PREPARED_DRAFT** inventory,
never standalone proof of acknowledged completion. Success returns a separate
**COMPLETE_DRAFT** CLI receipt binding that inventory and the approved digest.
On failure there is no receipt; `INCOMPLETE` is preserved/recreated best-effort
with explicit uncertainty if recreation fails. Marker absence alone proves
nothing. Completed file/directory syncs are not crash-tested durability.

Independent exact-head source and evidence reviews are **CLEAR**, including all
18 final source bindings. The owner standard-library suite passes **536 tests**
without skips on system Python 3.14.5 using the real pure Outfitter validator;
the **24 export-boundary controls** overlap that suite. The optional bundled
Python 3.12.14 PDF suite separately passes **10 tests** without skips. Final
renderer anchor corrections occurred during the standard-library run: final
renderer coverage is the later PDF suite and final CLI artifacts, not a claim
that one immutable full suite tested the final renderer.

The coordinator separately passes **22 checks across eleven actual CLI preview
and refusal scenarios**: all three profiles, canonical approval digests, changed
narrative/old approval, wrong digests, raw-upload metadata, unsupported tier and
wrong-pathway refusals. It performed no PDF creation, refresh or workload.
Independent inspection of the owner's three successful real-CLI exports checks
24 payload hashes/sizes, receipt/package/canonical-preview binding, JSON/CSV and
PDF visible-field parity. All three single-page PDFs were independently rendered
and viewed. Every character is at least 11 points and lies within the one-inch
boundary at the declared 0.001-point numeric tolerance; measured horizontal
range is 72–540.0000443 points and vertical range 74.8847658–716.2666017 points.
This is fixture layout evidence, not manual accessibility or arbitrary-narrative
acceptance. The [coordinator evidence](evidence/2026-10-19-allocation-drafts/acceptance.json)
records source, log, artifact and checker hashes without private host paths.

Retained failures stay separate: the original final-fsync refusal left an
apparently complete directory; the corrected inventory/receipt protocol and
late-fsync/marker-recreation controls pass. The first three PDF glyph boxes
exceeded the margins, then corrected anchors passed every-character checks. An
initial bundled-Python full-suite run failed the unchanged SQLite extension
provenance witness because built-in `_sqlite3` has no `__file__`; the baseline
system-Python rerun passes without weakening or skipping it. A pypdf multiline
visitor-coordinate test also failed; final checks use direct anchors and
independent pdfplumber character geometry. Two root harness assumptions failed:
the owner's ACCESS observation was refreshed/unreviewed while root deliberately
used an unrefreshed snapshot, and the narrative key is `title`, not
`project_title`. The first comparison has a retained private JSON record; the
fixture-key traceback is recorded in the coordinator tool transcript, without a
separate bound local traceback file. Corrected isolated checks pass with no
product change.

The [exact-head hosted run](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39344177506)
passes `controls` (including 536 standard-library and ten optional PDF tests)
and existing `actual-docker`; optional `clean-source-builds` is **SKIPPED**.
Actual Docker remains legacy regression evidence, not temporary assessment
execution or source-image promotion. Reviewed and merged trees match
`f3ddf5c263569a7db5ea6546ab7ba023ad9a9fe3`. Every packet and all readiness,
actual-resource, upload, execution, cleanup-trust and retention-finalization
gates remain DRAFT/false. No application was submitted or resource deployed.

## Explore and Accelerate draft profiles

Merged Waypoint #52 extends the same approved-preview/export path with distinct
Explore and Accelerate profiles. Explore defaults to worksheet/Markdown/JSON
without a font, optional dependencies or PDF module import. The preview can
explicitly include an internal planning PDF with an internal two-page cap;
neither that PDF nor its cap is presented as a program requirement. Accelerate
has its own closed fields, checklist and three-page description cap. Maximize
remains explicitly unsupported. There is no generic tier fallback.

Explore's mode and null-or-digest-bound font are part of the approved record;
export cannot add a font or change mode. The three exact accepted #51 preview
records, source/font bindings and canonical digests remain valid and unchanged.
The existing publication protocol, literal narrative, CSV guards, PDF renderer,
manifest/receipt interfaces and runtime defaults remain unchanged. Requirements
fetch stays explicit and content-free before preview; export never refreshes.
All packets remain DRAFT and all authority/readiness gates stay false.

Independent exact-head source and evidence reviews are **CLEAR**, including all
11 source inventory bindings. The full system-Python 3.14.5 suite passes
**546 tests** without skips using the real pure Outfitter validator. The **ten
new profile controls** and **24 inherited boundary controls** are overlapping
subsets. The sequential optional bundled-Python 3.12.14 PDF suite passes
**11 tests** without skips, including all five supported PDF profiles and
overflow refusals. Actual isolated `-I -S` Explore testing proves optional
dependencies unavailable, no font access and no PDF module loading.

The coordinator separately passes **20 checks across seven actual isolated CLI
scenarios**, including successful font-free worksheet preview/export, canonical
binding, existing-directory refusal without changes, wrong approval, attempted
font/mode switching and unsupported Maximize refusal. No PDF, refresh, engine or
workload was created by those scenarios. Application arguments, exit codes and
outputs remain in the private archive; the isolated interpreter/bootstrap and
scenario harness source are recorded in the coordinator tool transcript, not a
separate bound portable checker file. Independent owner-artifact review
checks three modes, 23 payload hashes/sizes, three receipt/record/inventory
bindings, worksheet/CSV and visible PDF parity. Both existing one-page PDFs were
independently rendered and viewed. That report remains a pre-freeze record;
later evidence matches its exact PDF hashes to the frozen head rather than
rewriting its original pending source pin.

The first literal glyph-height check observed `10.999999999999972`; it remains
recorded. Raw PDF font operators are at least 11 points. Final checks declare
1e-6-point derived-height and 0.001-point coordinate tolerances, with no product
or layout change for this numerical observation. Both pages are readable and
within the declared margins. Four earlier #51 failure files remain byte-identical.
The [coordinator record](evidence/2026-10-19-access-profiles/acceptance.json)
and [isolated CLI checks](evidence/2026-10-19-access-profiles/root-cli-checks.json)
preserve exact pins, hashes, counts and these evidence boundaries.

The [exact-head CI](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39346092790)
passes `controls` (546 standard-library and 11 PDF tests) and existing
`actual-docker`; optional `clean-source-builds` is **SKIPPED**. Docker regression
does not execute a temporary assessment or promote source candidates. Reviewed
and merged trees match `db075b04a62966183b544b28c571c61ca06634b7`.
No application, host allocation, temporary upload, benchmark or deployment was
authorized by this increment.

## Optional durable queued grading

Merged Cairn #34 establishes a non-expiring queue-owned dispatch claim before
checkout for the optional `JobPolicyRunner` path. Only an acknowledged new claim
may execute. Run, grade, terminal tombstone and queue success publish in one
transaction; ambiguous responses are reread without redispatch. Minimal IDs,
digests and state survive grade/run retention and roster deletion. Published
duplicates cannot recreate purged result bodies. Ordinary runner behavior and
defaults remain unchanged.

The supported initiating caller is the real Worker. Direct `Service.GradeJob`
with a job-aware runner is inspect-only. If a failed claim write left no record,
the Worker holds its already-claimed queue row `in_progress`; an unsuccessful
write does not invent a permanent tombstone. Persisted claims never expire or
reopen automatically. Direct internal managed calls outside this protocol,
manual queue resets, old binaries, out-of-band writes and backup rollback or a
second restored admitting database are unsupported recovery/authority routes.
There is no external status recovery, compute allowance or refund authority.

Independent exact-head review is **CLEAR**, including all 25 source bindings
and five local log hashes. The full local serial race suite records **1,037
passing events / 493 overlapping top-level tests**, zero failures and **16
skips**. The focused **87 events / 22 top-level tests** are a subset; its one
skipped subprocess helper is exercised by three crash tests. Vet passed.
The actual pre-fix mutex-cancellation witness retains two failing subcases plus
their parent. The corrected post-lock checks pass. PostgreSQL's stale cross-row
snapshot concern was source-inferred before correction, not a reproduced
pre-fix runtime failure; queue updates now lock the job row then read the
barrier in a fresh statement.

All eight final CI checks pass: [main CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39341346384),
[recovery](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39341346372)
and [synthetic consumer](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39341346394).
The main job's configured PostgreSQL-tagged package passed in 3.191 seconds,
including the new real lock-wait control. This hosted runtime evidence is
separate from local PostgreSQL **NOT RUN** (compile/gated skips only).
Reviewed and merged trees match `b9a3ff2267a1ff3ebb1e7bc194a6b8cb9cf94722`.
The [component evidence](https://github.com/EduCloud-Ecosystem/cairn/blob/2be331d245a989490ca815a3c71b12c0d2ff0ed0/docs/evidence/2026-10-19-durable-grading/validation.json)
and [coordinator record](evidence/2026-10-19-assessment-estimation/cairn34-acceptance.json)
preserve these boundaries. The adapter remains uninstalled; no production
database, runner selection, deployment or private/student data changed.

## Operator inspection of queued grading

Merged Cairn #35 adds `GET /operator/grading-jobs` on the existing server/store.
It requires enabled authentication and a current allowlisted operator session;
anonymous, student, expired, revoked and synthetic development sessions are
refused before inspection-store reads. Exact job lookup or bounded binary
keyset pages expose closed IDs, enums, digests and independent run/grade presence
observations. Each response is one metadata snapshot; pages are not a frozen
whole-history inventory. SQL reads one joined statement; memory holds one read
lock. No new database opener, migration, table or provider call is added.

Target/source paths, runner free text, grade scores/bodies, run results, queue
diagnostics and raw database errors are excluded. Malformed metadata stays
invalid or unknown. Stored digests are observations, not fresh educational-body
verification. Record absence does not prove a retention purge; claimed worker
liveness and external effects remain unknown. An in-progress queue row without
a dispatch cannot establish runner mode or safe retry. Every response denies
replay authority. Default runner selection, deployment, external status recovery
and restored-store authority remain unchanged and unqualified.

Independent exact-head review is **CLEAR**. The full serial local race suite
records **1,084 passing events / 502 overlapping top-level tests**, zero failures
and **16 skips**. The corrected focused **51 events / 11 top-level tests** are a
subset. Vet passed. The owner-recorded commands/exit codes and independent
source/log hash/count checks are in the
[coordinator record](evidence/2026-10-19-assessment-estimation/cairn35-acceptance.json)
and the [component evidence](https://github.com/EduCloud-Ecosystem/cairn/blob/3b0adc4a8faab0aa1aee491b2d0b60e984c64219/docs/evidence/2026-10-19-grading-inspection/validation.json).
All 15 source bindings and five logs match; the five earlier component evidence
files remain byte-identical.

The actual pre-fix SQLite reader control retains **two failing subcases plus
their parent**: text substring selection hid embedded NUL suffixes in corrupt
target/status metadata, falsely projecting consistent publication. The corrected
SQLite reader slices bounded BLOB bytes before text conversion, preserving
malformed suffixes for validation. Both controls pass in focused and full runs.
This was a new inspection-reader defect, not an accepted dispatch-writer failure.

All eight exact-head CI checks pass: [main CI](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39343643827),
[recovery](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39343643837)
and [synthetic consumer](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39343643737).
The configured hosted PostgreSQL-tagged package passed in **2.880 seconds**,
including shared inspection conformance and a server-enforced read-only
connection control. Local PostgreSQL remains **NOT RUN**: its parent PASS with
three database-dependent skips is compile/gating evidence only. Reviewed and
merged trees match `a22af8e8cd8deb6583984b261a8b188f6238ebd3`.

## Next scope and open gates

The approved [product milestone](../strategy/researcher-instructor-pilot.md)
requires independent researcher and instructor completion of the actual-resource
Python/R journey through validated estimates, editable packets and verified
cleanup. Current source and synthetic evidence do not complete that milestone.
Optional tools must show a workflow, capability gap, measured benefit and
maintenance owner; resource and privacy decisions remain explicit.

The [disabled broker source acceptance](2026-10-19-owned-data-source-acceptance.md)
records merged Outfitter #19, final review/CI and its bounded source-only scope.
The [connected AS1 acceptance](2026-10-19-as1-source-acceptance.md) records merged
Waypoint #53, real HTTP/Store/current-auth/test-peer checks and preserved failures.
Production content remains disabled; this does not qualify operational uploads.
The separately versioned [larger CPU metadata acceptance](2026-10-19-large-cpu-source-acceptance.md)
records merged Outfitter #20, final CI and 47 independent pure-CLI checks. It
does not enable larger-input execution, measurements or cleanup trust; v1 and
all earlier evidence remain unchanged. The
[earlier checkpoint](2026-10-19-owned-data-review.md) remains historical failed
evidence; no operational upload or cleanup gate is closed. The
[provisional budget](../strategy/researcher-instructor-pilot-budget.md) approves
staged planning ceilings only, with exact live choices and approvals still open.

The [streaming scientific acceptance](2026-10-19-streaming-summary-source-acceptance.md) records Waypoint #54,
independent Python/R/checker source and exact local/hosted evidence with original
failures. It accepts a narrower scientific candidate only. Actual execution,
resource counters, aggregate storage and cleanup remain separately unqualified.

The initial A4 calculation is accepted for synthetic metadata only. Actual
target observations, additional stages/hardware, prediction uncertainty and
verified resource-specific conversions remain open. Conservative allowance
charges cannot supply fitting measurements. Initial A5 draft exports are now
accepted within the narrow scope above, with Explore and Accelerate added by
the subsequent increment. Maximize remains refused until a separate
multi-document profile exists. A1's connected temporary session, bounded intake,
current authorization and cleanup-or-quarantine source are now accepted within
the disabled test-only scope above. Next connect larger-profile execution,
measurement and independent scientific checks through existing authorities.
Retained study data paths must not receive assessment input. Selected hosts,
encryption, independent cleanup, operators and fresh native-unit allowances
remain unresolved before operational qualification. Refreshed/reviewed requirements and actual performance remain
open. Researchers review science, resources and form correspondence and submit
their own applications.

Temporary uploads, encrypted scratch, independent expiry/termination/revocation/
deletion under faults, actual CPU/GPU measurement and accounting, second operator
on a second machine, researcher/instructor exercises, manual accessibility,
hosted identity, capacity/off-host recovery and whole-service privacy acceptance
remain **NOT RUN / OPEN**. Historical quota NO-GO, fifth-headroom FAIL, exhausted
v4 allowance and disabled source candidates remain unchanged. Docker/Compose on
OrbStack stays the baseline; Kubernetes and PAIR are optional gated evaluations.

No purchase, subscription, cloud provisioning, production deployment, model
acquisition, inference run or default-routing change occurred. Coding this slice
requires no new cost decision. Before actual-resource work, the coordinator must
present selected capacity, hosts/model where relevant, operator, time window,
finite native-unit allowance, independent cleanup and recovery responsibilities.
These selections are not implied by passing local or hosted regression tests.
