# EduCloud — Documentation Index

*Annotated map of the documentation that matters, by purpose. Paths are
relative to `~/dev/`. Updated 2026-07-21. Names: Cairn (was Quad), Belay (was
Sol), Waypoint (was "HOST"/Registry), Portage (was Commons/claude-lanes),
Outfitter (new).*

## Platform definition (read first)

| Doc | What it is |
|---|---|
| `educloud/SYSTEM.md` | **The canonical internal definition**: names, module boundaries, the platform invariant, shared contracts (including contract 9, bounded AI management), the scale table, and the two-line resource allocation. Where an older document conflicts, SYSTEM.md wins. |
| `educloud/EduCloud-White-Paper.docx` + `educloud/WHITEPAPER.md` (markdown master, v0.9.3, CC BY 4.0, destined for the EduCloud-Ecosystem org repo, Zenodo DOI at v1.0) | **The platform definition** — vision, five modules under current names, architecture principles, status, governance, funding, roadmap. First on-disk document carrying the full naming scheme. |
| `educloud/EDUCLOUD-STATUS.md` | July 21 status snapshot. For sequencing, `LINE-E-ROADMAP.md` is now the plan of record. |
| `educloud/LINE-E-ROADMAP.md` | EduCloud execution roadmap E0–E4 (MVP → pilot → institutional → federated), the dependency spine, and the expansion contract. |
| `educloud/EDUCLOUD-INVENTORY.md` | The July 21 orientation pass: directory map, document inventory, duplicates, staleness flags. |
| `educloud/START-HERE.md` | June umbrella index + next-step gates. **Stale** (old names, superseded PESOSE date) — retained until SYSTEM.md/name propagation lands. |

## Module documentation

**Cairn** (`quad/`): `KICKOFF-PROMPT.md` (the pilot-sprint session brief),
`README.md` (what/why, status), `DESIGN.md` (the architecture spec),
`ROADMAP.md` (phases, refreshed July 21 with the pilot-sprint block),
`docs/github-setup.md` / `forgejo-setup.md` / `gitlab-setup.md` /
`migrating-github-to-forgejo.md` (per-host operator guides).

**Belay** (`peer-tutor-framework/`): `INSTRUCTOR_MODE.md` (instructor-mode
design spec, July 2026 — session-ready), `README.md`, `ARCHITECTURE.md`,
`VALIDATION.md` (the 79 KB build/verification record — the ground truth),
`GROUND_TRUTH.md` (read-only audit), `ROADMAP.md` (every item cited to
in-tree sources), `PRIVACY.md` (distress safety + grades firewall),
`process_measures.md`, `STATE_AUDIT_DOMAIN.md`.

**Waypoint** (`HOST/`): `PLAN.1.md` (the phased build plan on Coolify),
`INTEGRATION.md` (how hosting relates to EduCloud/Cairn and MESA),
`CHANGELOG.md` (document history), `HOST_SESSION_BUILD.md` +
`CLAUDE_CODE_INSTRUCTIONS.md` (build-session operating instructions),
`docs/ONBOARDING.md` (tenant contract), `docs/REQUIREMENTS.md`,
`docs/TENANTS.md`, `docs/STATUS_DECK.html` (visual status).

**Portage** (`claude-lanes/`): `LINE-P-ROADMAP.md` (personal-stack staging
S0–S5 — the plan of record), `PLATFORM.md` (capstone architecture),
`REVISION-PLAN.md` (the Scale-1 transition work order), `HANDOFF.md` (build
phases + buy-over-build), `PROJECT.md` (novelty claim), `KICKOFF-PROMPT.md`
(next session = Phase 6a), `EDUCLOUD-BRIEF.md` (decentralized-AI positioning),
`specs/00–09` (reasoning record), `specs/10`–`11` (normative Scale-1
architectures: open-weight-only end state; hybrid PAYG transition),
`docs/phase-1-findings.md` (verified: Claude Code → LiteLLM direct),
`KNOWN_GOOD_VERSIONS.md`.

**Outfitter** (`outfitter/`): `README.md`, `DESIGN.md` (broker/adapter model,
Go stack rationale, allocation intelligence in §9), `ROADMAP.md` (M0–M5),
`specs/00–06` (adapter interface, cost model, budget guards, Cairn
integration, MVP scope, and the allocation planner), `KICKOFF-PROMPT.md`
+ `HANDOFF.md` (build-session brief).

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

Brand doc (`educloud-brand.md`) · full prose name propagation (July banners
cover the stale docs; rewrites deferred) · umbrella not under git · Portage
and Outfitter unpushed; Belay on the personal account; HOST rename pending.
