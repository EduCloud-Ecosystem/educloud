# EduCloud — Documentation Index

*Annotated map of the documentation that matters, by purpose. Paths are
relative to `~/dev/`. Research-pilot entries updated 2026-10-18; other entries
retain their earlier review dates. Names: Cairn (was Quad), Belay (was
Sol), Waypoint (was "HOST"/Registry), Portage (was Commons/claude-lanes),
Outfitter (new).*

## Platform definition (read first)

| Doc | What it is |
|---|---|
| `educloud/SYSTEM.md` | **The canonical internal definition**: names, module boundaries, the platform invariant, shared contracts (including contract 9, bounded AI management), the scale table, and the two-line resource allocation. Where an older document conflicts, SYSTEM.md wins. |
| `educloud/EduCloud-White-Paper.docx` + `educloud/WHITEPAPER.md` (markdown master, v0.9.3, CC BY 4.0, destined for the EduCloud-Ecosystem org repo, Zenodo DOI at v1.0) | **The platform definition** — vision, five modules under current names, architecture principles, status, governance, funding, roadmap. First on-disk document carrying the full naming scheme. |
| `educloud/EDUCLOUD-STATUS.md` | October 17 accepted local research baseline and P1 implementation, followed by preserved October 6–7 classroom/AI assessment and evidence. Unrechecked component status remains historical. |
| `educloud/LINE-E-ROADMAP.md` | EduCloud execution roadmap E0–E4 (MVP → pilot → institutional → federated), the dependency spine, and the expansion contract. |
| `educloud/EDUCLOUD-INVENTORY.md` | The July 21 orientation pass: directory map, document inventory, duplicates, staleness flags. |
| `educloud/START-HERE.md` | June umbrella index + next-step gates. **Stale** (old names, superseded PESOSE date) — retained until SYSTEM.md/name propagation lands. |

## Module documentation

**Cairn** (`cairn/`): `KICKOFF-PROMPT.md` (the pilot-sprint session brief),
`README.md` (what/why, status), `DESIGN.md` (the architecture spec),
`ROADMAP.md` (phases, refreshed July 21 with the pilot-sprint block),
`docs/github-setup.md` / `forgejo-setup.md` / `gitlab-setup.md` /
`migrating-github-to-forgejo.md` (per-host operator guides),
`docs/grading-policy.md` (pinned deterministic grading and automatic pushes),
`docs/llm-assessment.md` (opt-in source capture, bounded OpenAI/imported feedback
and proposed scores, durable usage/pause controls, instructor review/publication
and remaining course-evaluation/retention gates),
`docs/assessment-evaluation.md` (offline/live synthetic evaluation CLI, frozen
baseline, corpus-bound evidence validation, separate policy/score review and
resumable offline review packet).

**Belay** (`belay/`): `INSTRUCTOR_MODE.md` (instructor-mode
design spec, July 2026 — session-ready), `README.md`, `ARCHITECTURE.md`,
`VALIDATION.md` (the 79 KB build/verification record — the ground truth),
`GROUND_TRUTH.md` (read-only audit), `ROADMAP.md` (every item cited to
in-tree sources), `PRIVACY.md` (distress safety + grades firewall),
`process_measures.md`, `STATE_AUDIT_DOMAIN.md`.

**Waypoint** (`waypoint/`): `PLAN.1.md` (the phased build plan on Coolify),
`INTEGRATION.md` (how hosting relates to EduCloud/Cairn and MESA),
`CHANGELOG.md` (document history), `HOST_SESSION_BUILD.md` +
`CLAUDE_CODE_INSTRUCTIONS.md` (build-session operating instructions),
`docs/ONBOARDING.md` (tenant contract), `docs/REQUIREMENTS.md`,
`docs/TENANTS.md`, `docs/STATUS_DECK.html` (visual status).
The separate research service lives in `research-workspace/`: `CONTRACT.md`,
`README.md`, `VERIFICATION.md`, `SOURCE-BUILDS.md`, immutable image references
and selected public evidence. Source-build evidence and its later cleanup
observation live in `evidence/2026-10-17/source-builds/` and
`evidence/2026-10-17/replay-cleanup-reconciliation/`. Portable environment/replay
and coordinated recovery acceptance is
tracked in the October 17 umbrella record below.

**Portage** (`portage/`): `LINE-P-ROADMAP.md` (personal-stack staging
S0–S5 — the plan of record), `PLATFORM.md` (capstone architecture),
`REVISION-PLAN.md` (the Scale-1 transition work order), `HANDOFF.md` (build
phases + buy-over-build), `PROJECT.md` (novelty claim), `KICKOFF-PROMPT.md`
(next session = Phase 6a), `EDUCLOUD-BRIEF.md` (decentralized-AI positioning),
`specs/00–09` (reasoning record), `specs/10`–`11` (normative Scale-1
architectures: open-weight-only end state; hybrid PAYG transition), `specs/12`
(model-market surveillance), `specs/13` (routing paradigm — why
verify-then-escalate rather than classification-first, and the three
corrections the 2026-08-08 landscape scan produced),
`config/profiles/scale2.educloud.*` + `scale2.educloud.md` (**the Scale-2
EduCloud profile, built and tested** — LINE-E-ROADMAP E0's config diff),
`docs/phase-1-findings.md` (verified: Claude Code → LiteLLM direct),
`docs/prompts/CC-P7`–`CC-P14`, `KNOWN_GOOD_VERSIONS.md`.

**Outfitter** (`outfitter/`): `README.md`, `DESIGN.md` (broker/adapter model,
Go stack rationale, allocation intelligence in §9), `ROADMAP.md` (M0–M5, plus
M1.5 and the 2026-08-08 build-vs-integrate triage and ACCESS path),
`specs/00–06` (adapter interface, cost model, budget guards, Cairn
integration, MVP scope, and the allocation planner), `specs/08` (isolation
tiers for untrusted student code — **platform-level, consumed by Cairn and
Belay**), `docs/prompts/CC-O1`, `KICKOFF-PROMPT.md` + `HANDOFF.md`
(build-session brief).
The executable local broker is specified in `specs/09`, the read-only Jetstream2
preflight/gated API in `specs/10`, and local held recovery/fencing in `specs/11`.
Operator guides: `docs/LOCAL-RESEARCH-BROKER.md`, `docs/JETSTREAM2-PREFLIGHT.md`,
`docs/LOCAL-RECOVERY.md` (accepted local P1 release; remote/hosted gates remain).

> `specs/07` is **reserved** for the endpoint manifest (SYSTEM.md contract 9),
> to be authored when sovereign wiring approaches post-Aug-28. Isolation tiers
> took `08` for that reason.

**Prompt-number namespace (recorded 2026-08-08 after a collision).** Claude Code
prompts are named `CC-<series><n>` and the series is shared across repos, so a
number means one thing platform-wide: `CC-P*` Portage engine + personal pilot
(P0–P15 used), `CC-C*` the completed cross-cutting cleanup series (C1–C5),
`CC-HB*` Herdr build, `CC-CA*` Cairn (CA1–CA17 used), `CC-B*` Belay (B1–B4
used), `CC-O*` Outfitter (O1 used), `CC-W*` Waypoint (W1 used). Prompts live
in each repo's `docs/prompts/`.

## Strategy & funding (`educloud/`)

| Doc | What it is |
|---|---|
| `strategy/EduCloud-business-plan.md` | Master business & operating plan. |
| `strategy/EduCloud-funding-strategy.md` | Diversified funding portfolio, ranked; §2 is the master funding calendar (all dates, updated July 2026). |
| `strategy/EduCloud-team-funding-roadmap.md` | Two-anchor grant teams + integrated timeline. |
| `strategy/EduCloud-financial-model.xlsx` | Parameterized financial model. |
| `strategy/willamette-pitch.md` | Willamette positioning. |
| `grants/PESOSE-Track1/` | Project description draft + budget. **Correct deadline: NSF 26-506 Track 1, March 2, 2027** (drafts still cite Sept 1, 2026 — fix pending). |
| `grants/IUSE-ESL-Level1/` | Draft + budget, target ~Jan 20, 2027. |
| `grants/foundations/` | Eight non-NSF drafts (Sloan ×2, Hewlett, ECMC, Ascendium, NLnet, Spencer) + send-order README. |
| `grants/EduCloud-adopter-LOC-recruitment-kit.md` | Adopter/letter recruitment templates. |

## Architecture memos (`educloud/architecture/`)

`EduCloud-registry-federation-proposal.md` (the Registry/Waypoint federation
layer — Ben Markwart's workstream) · `EduCloud-hosting-reconciliation.md`
(the decision that made Coolify the hosting engine).

## Cross-module decisions and research (`educloud/docs/`)

The [research workspace pilot](docs/specs/research-workspace-pilot.md) defines
the October 17 implementation contract for Waypoint project/run/evidence
workflows and Outfitter's bounded local execution. It preserves separate
institutional, scientific and cloud-provider acceptance gates.
The [October 17 acceptance record](docs/research/2026-10-17-research-pilot-acceptance.md)
freezes the merged P0/P1 revisions and subsequent source-build, native-accounting
and optional inference increments, preserving each evidence boundary.
The [build backlog](docs/strategy/research-pilot-build-backlog.md) sequences
remaining portability/recovery, optional Kubernetes evaluation, bounded
Jetstream2, direct Portage qualification and shared pilot controls. The
[capacity decision record](docs/decisions/2026-10-17-research-pilot-capacity.md)
requires a concrete reviewed cost packet before any new charge; no new service
subscription is assumed necessary for the present local phase.

The [local Kubernetes foundation](docs/specs/local-kubernetes-evaluation.md) and
[offline tool](tools/local-kubernetes/README.md) prepare two zero-workload
namespaces for the host owner's OrbStack evaluation. They preserve Outfitter
admission/accounting, add no shared database or workload launcher, and leave
network enforcement and workload acceptance unqualified. A separate
[operator observation](docs/research/evidence/2026-10-18-local-kubernetes/infrastructure/README.md)
records two namespaces/eight policy objects and targeted admission/RBAC checks,
retaining the original timeouts and invalid negative probes.

The umbrella is where a decision spanning more than one module lives, so no
single module's repo becomes the de-facto owner of a platform-wide rule.

`docs/policy/data-destinations.md` (+ `check_destinations.py`, which enforces
it against the document's own register) — SYSTEM.md contract 11 ·
`docs/decisions/` (CW02, 2026-07-28, and the 2026-08-08 landscape-scan record) ·
`docs/strategy/` (two-solution-lines, portage-scale-mapping,
verifier-first-recommendation) · `docs/research/` (edge inference, routing-stack
reference, self-hosted search, XDA change assessment) · `docs/specs/`
(portage-scale-2-3, 05-federated-sovereign).

Module-scoped decisions stay in the module: Waypoint's
`docs/decisions/2026-08-08-analogue-scan.md` (hosting/identity/LTI) and
Portage's `docs/specs/13-routing-paradigm.md` are correctly placed there
because each governs one module's design. Outfitter's `specs/08` is the
exception that proves the rule — it lives in Outfitter because Outfitter
provisions the compute, but it is normative for Cairn and Belay too, and is
flagged as platform-level here so it is not mistaken for a broker-only concern.

## Governance

`educloud/project-docs/GOVERNANCE.md` + `CONTRIBUTING.md` (umbrella, old
naming) · Belay's full set (`DCO`, `LICENSING.md`, `CODE_OF_CONDUCT.md`,
`CONTRIBUTING.md`) — the per-repo model · Cairn's `LICENSE` + `CONTRIBUTING.md`
+ `CODE_OF_CONDUCT.md` · Outfitter's full set (mirrors Belay).

## People briefs (`educloud/onboarding/`, `educloud/collaborators/`)

| Doc | Audience |
|---|---|
| `onboarding/EduCloud-Brief-for-Ben-Markwart-rev2.docx` | Ben Markwart (CALES) — **canonical July version**; June copies exist in two places. |
| `collaborators/John Chen/00-START-…-orientation` (+ `onboarding/John-Chen-orientation.md`) | John Chen read-in. |
| `onboarding/EduCloud-Brief-for-Barney-Maccabe.docx` | Barney Maccabe, InfoSci Dean of Research (July 21). |
| `mesa/educloud-mesa-integration.html` + `educloud-mesa-pitch.pdf` | MESA/Tyson — interactive integration page + one-pager. |

## Known gaps (tracked in EDUCLOUD-STATUS.md)

Current research assessment: `EDUCLOUD-STATUS.md` and the October 17 acceptance
record. The local Waypoint/Outfitter Python/R research baseline is merged; P1
portability and coordinated recovery are merged with pinned local evidence and
passing CI. Source construction/qualification on ARM64 and AMD64 is accepted
through Waypoint #31; #32 records later cleanup and a conservative charge while
preserving the original failed replay. Local synthetic identity/access merged
in #33: 158 offline controls, 74 local browser/service checks and a separate
seven-check provider-logout supplement; final ordinary CI passed and source
builds were skipped. Failed attempts and conservative charges remain retained.
Read-only storage inventory/retention reporting merged in #34 (176 total
workspace tests), and incremental broker output limits merged in #35 (184 total
workspace tests). Final ordinary CI passed for both; source builds were skipped.
The first storage-admission draft reproduced five failure-boundary defects.
PR #36 preserves an inert rejected patch and offline
witnesses, not quota implementation; accepted application files are unchanged.
Neither reporting nor per-process output bounds enforce a total storage quota
or authorize deletion. PR #37 adds an opt-in fresh-store operation guard and
guard-aware recovery: 235 offline controls, nine local browser checks with a
simulated provider, twelve actual local Docker/provider checks and final ordinary
CI passed. New regressions address the first four witnesses; the consumed-headroom
witness, whole-store quotas and accepted-store migration remain open. The two
incomplete browser attempts and 127 prior evidence files are retained.
An independent post-merge audit then reproduced a final-launch race: cancellation,
user revocation or project closure committed before launch still reached the
intercepted broker spawn. PR #38 corrects the final fence and superseding-settlement
and post-launch observer failures: 295 offline controls, including sixty dispatch
tests, and final CI passed; a separate 26-control independent recheck passed.
Original failures remain unchanged. PR #39 qualifies seventeen source-pinned writer
categories with eight production-connected Python controls, seven simulated
broker controls and final ordinary CI. Review corrected a self-comparing append
fixture; its earlier evidence is retained. All 168 prior evidence files match.
PR #40 implements finite row/session/encoded-field limits on a fresh local-key
profile, with existing authority binding and safety actions preserved at limits.
All 317 local tests passed, including 21 finite controls; exact-head and post-merge
CI passed existing controls/Docker checks, with source builds skipped. Two review
defects were reproduced and corrected; original failed evidence and all 182 prior
evidence files remain unchanged. Finite-profile OIDC and restore explicitly
refuse; new finite-profile provider/browser/human acceptance remains NOT RUN.
PR #41 qualifies SQLite/guard write paths with nine disposable controls and 318
local tests, plus passing exact-head/post-merge CI; source builds skipped.
Its retained failed restart assumption is a fixture failure, not a production
defect. All 199 prior evidence files and production source remain unchanged.
Whole-store capacity remains UNKNOWN and quota_enforced:false. Waypoint #42 adds
a fresh opt-in export path that releases its reader before artifact I/O and
rechecks current authority plus exact captured metadata before returning bytes.
Its 334 local tests, independent review and exact-head/post-merge CI passed;
source builds skipped and all 209 prior evidence files remain unchanged.
Waypoint #43 implements the fresh opt-in guard publication profile after two
independent-review corrections: 368 local controls and exact-head CI passed.
Fixed ordinary/safety scratch slots retain failed publications and uncertainty;
the conditional 12 MiB named-payload bound is not whole-store capacity.
Cached durability never skips fresh residue/hold checks. Outfitter #15 qualifies
twenty connected broker writer observations, 32 model cases and two optimized
oracle probes after review corrections and passing exact-head/post-merge CI. Earlier false
acceptances remain preserved; runtime source and the active broker pin are
unchanged by that qualification. Outfitter #16 implements serialization before
spill: 18 focused and 754 full race test/subtest passes, independent review and
exact-head/post-merge CI passed. Waypoint #44 accepts the separate old/new-binary qualification:
45 controls and seven original local Docker attempts with 210 CPU-seconds charged.
Review corrected an accounting false pass; 384 combined tests, 16 optimized
controls and exact-head CI passed. Retrospective receipt validation is separate
from the original workload. Waypoint #45 adopts that broker in standard Docker
CI after 41 HTTP, 25 recovery, 12 guard checks, two successful replays and five
verified bundles; optional source-build qualification keeps its original broker.
Waypoint #46 implements scoped SQLite ownership for a fresh opt-in v4 profile:
433 local tests, 49 included ownership controls and 29 detected deliberate
regressions pass after fifteen review findings were corrected. Independent
source/evidence review and final-head CI passed. Uncertain ownership holds
readers and writers, including safety actions, for the same root in that process.
Waypoint [#47](https://github.com/EduCloud-Ecosystem/waypoint/pull/47) merged the fixed v4 local Docker qualification: four Python/R
attempts across two synthetic projects, 18 controls, correct independent results,
verified cleanup and 120 conservative CPU-seconds charged. Final acceptance and
merge evidence are recorded in the research acceptance record; current CI Docker
checks still exercise older profiles. Independent person/machine and selected
shared-pilot operations are the next gates.
No checkpoint, journal, quota or migration changes are accepted.
All four source candidates remain
disabled. Independent human reproduction (#28), promotion/distribution, hosted
identity, retention/deletion and store-wide limits (#29) remain open. Kubernetes is an optional post-P1 evaluation;
Docker remains the default. No live cloud/provider acceptance is claimed.

The following classroom/AI assessment retains its October 7 review boundary
except for the explicit Outfitter update below. Cairn and the JupyterHub-based
course workspace remain a separate path from the new research service.

- Waypoint now includes encrypted preserved-image recovery, separate-runner
  restoration, hard XFS byte/inode quotas, health timers and nginx/Keycloak
  configuration. Synthetic quota exhaustion/recovery and nginx tests pass.
  The authenticated course rehearsal connects real synthetic Keycloak/Hub and
  Forgejo/Cairn flows, with explicit file transfer, real Git-push webhooks,
  pinned pass/fail grading and bounded notebook traffic;
  see Waypoint `course-workspace/rehearsal/README.md` and the status evidence.
  Live institutional OIDC/revocation, real DNS/certificates, selected-host capacity,
  the actual backup account and institution-wide recovery still need acceptance.
  Institutional workspace recovery is implemented with a current operator roster
  and credential, retained homes and fresh Hub sessions; its external identity
  service and proxy/TLS are separate recovery dependencies.
- Cairn's instructor-owned grading manifest and per-step operator ceilings were
  fixed, merged and verified on the pilot host. Aggregate execution/output,
  shared-kernel assessment review, HTTPS and retention remain separate gates.
  PR #3 also preserves valid student sessions after denied operator requests; it
  is merged and tested but was not deployed to the production pilot in this pass.
  PR #4 pins automatic grades to each pushed submission commit and makes
  configured webhook setup failures visible/retryable. PR #5 adds opt-in bounded
  source capture, imported feedback/proposed rubric scores, instructor review and
  atomic publication, verified locally in browser and across SQLite/PostgreSQL.
  PR #6 adds a separately enabled OpenAI adapter, durable daily usage reservations,
  a pause control and private pending proposals; four live synthetic calls and
  the instructor-approval/student-feedback browser flow passed. Instructor-scored
  evaluation is still pending: PR #7 adds a repeatable synthetic suite and
  offline human-review packet, with 17/18 valid proposals and two unstable case
  pairs in its first baseline. PR #8 adds safe validation failure categories,
  corpus-bound report checks and a separate missing-work policy decision record.
  The user selected unassessable-until-review for readable work with no relevant
  answer. V2 calibration rubrics implement that choice; the 18-call development
  recheck yielded 18 valid proposals and 36/36 provisional matches. Instructor
  ratings and a held-out benchmark remain pending. No stored course rubric is
  changed by the worksheet. Course destination approval, draft/ledger
  retention, quota-enforced capture workers, production queuing, pagination and
  an explicit reviewed/test-score
  combination policy remain gates. Existing production pilot stays on PR #2.
- Belay's historical PR #12 assessment and Portage's older PR stack remain
  outside this update. The new finite Portage gateway/qualification path merged
  through #10/#11 after review fixes and passing final CI; 95 synthetic controls
  pass, while all 12 actual-engine gates remain NOT RUN. The offline review packet
  merged in #12 with 61 focused controls; it exposes missing capacity evidence
  without authorizing execution or spending. PR #13 fixes confirmed approval
  expiry races after metadata checks and before admission/dispatch: 17 separate
  synthetic controls and final CI pass; admitted unknown reservations stay held.
  All 12 actual-engine gates remain NOT RUN. A separate Jetstream2 hosted-API
  fixture contract merged in #14 with 147 new controls, 450 total passing tests
  and six existing skips; final CI passed. It has no transport, credentials,
  ledger mutation or live eligibility. Provider usage is not independently
  measured consumption. A separate offline restart witness reproduced 32
  inference/102 metadata calls under one 16-inference-call approval, plus three
  metadata calls before repeat unknown-work refusal. Durable approval/attempt
  authority merged in #15 using an existing operator-owned store, permanent
  lifetime slots and explicit offline migration. After a clock correction and
  deterministic concurrency-test repair, 63 guard controls, 175 runner controls,
  513 full-suite tests/six skips and final CI passed. Completed/unknown repeats
  make zero further fixture contacts. Original failures and all twelve runtime
  NOT RUN gates remain; a host recommendation is not live-use approval.
  No default route changed.
  Neither component is a prerequisite for the Python/R computing pilot.
- Outfitter now has the merged bounded Docker broker consumed by the research
  workspace. Native-SU journal and simulated independent cleanup implementation
  merged in #8 after two independent-review fixes and passing final CI. Live
  Jetstream2, independent-host supervision and provider settlement remain open
  in Ben's unchanged issues #1–#5. PR #10 records the reviewed blocked operator
  packet and rescue design; its 1 SU proposal is not a guaranteed charge cap.
  The separate simulated rescue implementation merged in #11 after four review
  corrections and final CI (376 tests/subtests plus Docker/recovery/consumer
  checks). Its 40 process-crash cases do not qualify independent hosts; unknown
  late effects, 64-sweep storage limit and unsettled charges remain visible.
  PR #12 adds pure metadata compatibility after five review fixes: final CI
  passed 607 tests/subtests and the existing Docker/recovery/consumer checks.
  It has no live transport or creator/ledger integration, and matching supplied
  metadata does not qualify boot, host suitability or effective network policy.
  PR #13 binds one experiment attempt and its compatibility evidence to native
  admission and both simulated create effects. A serialization defect was fixed;
  final CI passed 736 tests/subtests plus Docker/recovery/consumer checks. Restart
  and settlement do not renew the attempt; guest execution and live access remain
  unqualified, and unknown liabilities stay held.
  PR #14 records a reviewed supplemental operational packet. Restricted private
  SSH is the engineering recommendation; allocation/hosts/access remain
  unselected, and the 64 total sweeps are shared across phases for one reservation.
  No additional subscription is demonstrated necessary. Engineering, operational
  and live-approval gates remain; architecture re-approval is not required for
  ordinary authorized design work.
  Local recovery/fencing P1 is merged;
  it does not establish remote source-loss recovery or provider settlement.
  The local synthetic consumer bridge merged in #9 with 19 consumer checks;
  Cairn's disposable adapter merged in #32 with 19 local Docker controls and
  passing final CI. It proposes results without grade publication or production
  wiring; the broader live handoff and second-human gates remain separate.
- Preserve existing local strategy changes and unpublished module commits when
  reconciling branches. Public documentation is not the whole local state.

New records: `docs/decisions/2026-10-06-computing-continuity.md`; archived July
status at `docs/research/2026-07-21-platform-status.md`. Older branding, policy and
naming cleanup remains secondary to this deliverable. No grant or allocation
application is represented as submitted by this assessment.
