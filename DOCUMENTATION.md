# EduCloud — Documentation Index

*Annotated map of the documentation that matters, by purpose. Paths are
relative to `~/dev/`. Updated 2026-10-07. Names: Cairn (was Quad), Belay (was
Sol), Waypoint (was "HOST"/Registry), Portage (was Commons/claude-lanes),
Outfitter (new).*

## Platform definition (read first)

| Doc | What it is |
|---|---|
| `educloud/SYSTEM.md` | **The canonical internal definition**: names, module boundaries, the platform invariant, shared contracts (including contract 9, bounded AI management), the scale table, and the two-line resource allocation. Where an older document conflicts, SYSTEM.md wins. |
| `educloud/EduCloud-White-Paper.docx` + `educloud/WHITEPAPER.md` (markdown master, v0.9.3, CC BY 4.0, destined for the EduCloud-Ecosystem org repo, Zenodo DOI at v1.0) | **The platform definition** — vision, five modules under current names, architecture principles, status, governance, funding, roadmap. First on-disk document carrying the full naming scheme. |
| `educloud/EDUCLOUD-STATUS.md` | Current October 6–7 component assessment, merged releases, synthetic acceptance evidence and remaining production gates. Original July snapshot is retained under `docs/research/`. |
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
and remaining course-evaluation/retention gates).

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

Current assessment: `EDUCLOUD-STATUS.md` (updated October 7, 2026). The computing priority
is browser Python/R coursework with durable files and tested recovery. The
classroom foundation is Cairn; Waypoint adopts JupyterHub for the workspace.

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
  evaluation, course destination approval, draft/ledger retention, quota-enforced
  capture workers, production queuing, pagination and an explicit reviewed/test-score
  combination policy remain gates. Existing production pilot stays on PR #2.
- Belay PR #12's identity work is unmerged; Portage's existing PR stack still
  needs profile repair. Neither is a prerequisite for the computing pilot.
- Outfitter remains specification-only; defer brokering until there is a real
  second provider and a first consumer to validate its lifecycle against.
- Preserve existing local strategy changes and unpublished module commits when
  reconciling branches. Public documentation is not the whole local state.

New records: `docs/decisions/2026-10-06-computing-continuity.md`; archived July
status at `docs/research/2026-07-21-platform-status.md`. Older branding, policy and
naming cleanup remains secondary to this deliverable. No grant or allocation
application is represented as submitted by this assessment.
