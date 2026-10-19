# Assessment preparation and queued grading — October 19, 2026

The component changes below are accepted and merged within their recorded
source, regression and integration scopes. The implemented assessment slice prepares closed benchmark manifests and previews
unverified receipts through the operator CLI. It accepts no temporary upload,
executes no benchmark and creates no workspace or broker ledger. This is partial
A1/A2 of the [assessment backlog](../strategy/research-pilot-build-backlog.md),
not acceptance of the complete upload-to-allocation workflow.

## Revisions and ownership

| Component | PR | Independently reviewed head | Merge revision |
| --- | --- | --- | --- |
| EduCloud canonical contract | [#37](https://github.com/EduCloud-Ecosystem/educloud/pull/37) | `1184ab2c2a0c82aa437b2d146f22dbae2b98efa7` | `bf9bc615fbfef5055f231f473e784b1183c73dad` |
| Outfitter pure receipt command | [#18](https://github.com/EduCloud-Ecosystem/outfitter/pull/18) | `2369ffb223a8615321a819c08e87b6f19d650745` | `de65bdab9303395226ebfb35e0e0740ab19b4d8e` |
| Waypoint preparation and preview | [#49](https://github.com/EduCloud-Ecosystem/waypoint/pull/49) | `c47351f46186d7fa055a7f486516f4dac0aeb274` | `d70aaccc454332cb5bacf31e93c99e2ce0b420cd` |
| Cairn pinned grading context | [#33](https://github.com/EduCloud-Ecosystem/cairn/pull/33) | `70b984083fa711b12ae30bc22732d831a0b1ba1e` | `ab339c44248eca2f6c03c22ef951215e8969472a` |

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
is unchanged. Durable dispatch/no-replay claims, crashed-job recovery and atomic
grade/run publication are still separate gaps; the Outfitter adapter is not
installed into production by this change.

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
| Outfitter local suite | PENDING final constrained run. The first run has **FAIL**: 890 passing events, four failing leaf controls plus two failed parent groups, and two skips. All six attachment cases and the retention case subsequently pass unchanged with constrained concurrency: nine passing events including parents. |
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

## Next scope and open gates

A4's deterministic stage estimates can proceed with clearly synthetic
observations, repeat variability, held-out error, unit-preserving arithmetic and
explicit provisional results. Conservative allowance charges cannot supply
fitting measurements. Program exports and refreshed requirements follow that
usable estimation slice.

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
