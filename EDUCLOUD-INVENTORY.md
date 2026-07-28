# EduCloud — Repository & Document Inventory

*Read-only orientation pass · generated 2026-07-21 · no files edited, renamed, moved, or resolved*

## 0. Scope and headline findings

Root scanned: `~/dev` (`/Users/gregchism/dev`). This root holds ~29 top-level
projects; only a subset are EduCloud. EduCloud is **not** one repo — it is an
umbrella folder (`educloud/`) plus five module repos scattered as siblings.

Three findings dominate everything below:

1. **The current five-name scheme is not saved anywhere on disk.** The task's
   current names are Cairn / Belay / Waypoint / Portage / Outfitter. A full
   content search of the EduCloud folders finds **only "Cairn"** (2 mentions,
   always as an *alternative* to "Quad"). **Belay, Waypoint, Portage, and
   Outfitter appear in zero files.** Every saved document still uses the prior
   names: Quad, Sol, Registry / HOST, Commons / claude-lanes, "compute
   brokering." The rename has not propagated.

2. **There is no system-definition / source-of-truth document.** No `SYSTEM.md`,
   no `DESIGN.md` at the umbrella level, no top-level file in the dev root
   (`~/dev` has no tracked `.md` files at all). The closest thing is
   `educloud/START-HERE.md`, but it is a June index that predates the rename and
   is itself internally stale (see §5). **System definition: not yet saved.**

3. **Outfitter (compute provisioning) has no repository.** It exists only as
   narrative inside the grant and strategy docs. The one adjacent artifact is
   `InfoSciCourses/compute-cost-simulator/` — an older (April 2026) teaching
   cost simulator, not a provisioning/brokering control plane.

---

## 1. Directory map

Pruned dirs (noted, not descended): `.git`, `node_modules`, `.venv`, `.venv`/
`venv`, `__pycache__`, `.pytest_cache`, `.ruff_cache`, `dist`, `_site`,
`.Rproj.user`, `*.egg-info`, `.claude`.

### EduCloud umbrella + modules

```
~/dev/
├── educloud/                         UMBRELLA (plain folder, NOT a git repo)
│   ├── START-HERE.md                 index / closest thing to a definition (June, stale)
│   ├── educloud-avatar-light-1024.png  brand avatar (only brand asset found)
│   ├── strategy/                     business plan, funding strategy, team+funding roadmap,
│   │                                 financial model (.xlsx), willamette pitch
│   ├── grants/                       PESOSE-Track1/, IUSE-ESL-Level1/, foundations/ (8 LOIs),
│   │                                 adopter-LOC recruitment kit
│   ├── architecture/                 registry-federation-proposal, hosting-reconciliation
│   ├── onboarding/                   John Chen orientation, Ben Markwart brief (+rev2, +pdf)
│   ├── collaborators/                Ben Markwart/ (brief docx+pdf), John Chen/ (orientation)
│   ├── mesa/                         MESA integration (interactive .html), pitch (.pdf)
│   └── project-docs/                 README/GOVERNANCE/CONTRIBUTING (titled "Quad") + diagrams/ (2 svg)
│
├── quad/          → CAIRN     Go control plane + React (web/). GitHub: Gchism94/quad
│   ├── DESIGN.md  README.md  ROADMAP.md  CODE_OF_CONDUCT.md  CONTRIBUTING.md  LICENSE  go.mod
│   ├── cmd/ internal/ pkg/ web/ deploy/ docs/ (forgejo/github/gitlab-setup, contributor-tracker.xlsx)
│
├── HOST/          → WAYPOINT  Registry / federation / hosting on Coolify. GitHub: EduCloud-Ecosystem/HOST
│   ├── CHANGELOG.md  PLAN.1.md  INTEGRATION.md  HOST_SESSION_BUILD.md  CLAUDE_CODE_INSTRUCTIONS.md
│   ├── docs/ (ONBOARDING, REQUIREMENTS, TENANTS, STATUS_DECK.html)
│   ├── server/ apps/ templates/ keycloak/ traefik/ dev/     (no top-level README.md)
│
├── claude-lanes/  → PORTAGE   Model routing / inference ("Commons"). LOCAL ONLY (no git remote)
│   ├── PLATFORM.md  PROJECT.md  HANDOFF.md  EDUCLOUD-BRIEF.md  KICKOFF-PROMPT.md
│   ├── KNOWN_GOOD_VERSIONS.md  README.md  CLAUDE.md  pyproject.toml
│   ├── specs/ (00–09)  herdr/  herdr-meters/  tests/  docs/  scripts/
│
├── peer-tutor-framework/  → BELAY   Peer AI tutor ("Sol"). GitHub: Gchism94/peer-tutor-framework
│   ├── ARCHITECTURE.md  GROUND_TRUTH.md  README.md  ROADMAP.md  VALIDATION.md
│   ├── STATE_AUDIT_DOMAIN.md  process_measures.md  PRIVACY.md
│   ├── LICENSING.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md  DCO
│   ├── backend/  frontend/ (widget.html)
│
└── InfoSciCourses/compute-cost-simulator/   OUTFITTER-ADJACENT (April 2026 teaching cost sim; not a module repo)
```

### Non-EduCloud siblings in `~/dev` (exist; not part of this inventory, not descended)

`GameTree/`, `gametree-matching-poc/`, `InfoSciCourses/` (course repos: INFO511/521/523/526/557,
Capstone, CoursesArchive, github-classroom-reinvite-app), `PHQ-MH-CP/`, `State-Data/`,
`book-corpus/`, `dataviz-lecs/`, `gym-of-tucson-website/`, `js2-AI-Healthcare/`,
`meadows-1972-bibliometrics/` (+ `-public-export/`), `personal-website/`, `qmd-grading/`,
`quantum-inventioneers/` (the quantum tutor Belay's core was extracted from — lineage, not a module),
`redmond-compass/`, `reverie/`, `slp-platform/`, `srvpkg/`, `steppe/`, `steppe-private/`,
`taskcapture/`, `three-canyon-consult/`.

---

## 2. Module table

| Module (current) | Path | Prior names on disk | Apparent state | Evidence |
|---|---|---|---|---|
| **Cairn** | `~/dev/quad/` | "Quad" (README: "Working name — placeholder") | **Alpha, active.** Core provisioning, self-enroll, grading, Forgejo + GitHub + GitLab adapters working; instructor dashboard in progress. Last commit 2026-06-14. | `go.mod`, `DESIGN.md`, `README.md`, `ROADMAP.md`, `.git` → `github.com/Gchism94/quad`, `web/` (React), `cmd/`+`internal/`+`pkg/` (Go) |
| **Belay** | `~/dev/peer-tutor-framework/` | "Sol"; repo name "peer-tutor-framework" (placeholder) | **Framework, evaluation-first.** Deterministic Governance/leak gate, "Robin" DomainPack, validation harness. Last commit 2026-06-18. | `.git` → `github.com/Gchism94/peer-tutor-framework`, `ARCHITECTURE.md`, `backend/` (Python), `frontend/widget.html`, `DCO`, `LICENSING.md`, `PRIVACY.md` |
| **Waypoint** | `~/dev/HOST/` | "HOST", "EduCloud Registry" | **Build in progress on Coolify.** Catalog/federation + Keycloak identity + Traefik. Last commit 2026-06-16 (file mtimes show 2026-07-21 = checkout/mount artifact, not edits). | `.git` → `github.com/EduCloud-Ecosystem/HOST`, `PLAN.1.md`, `INTEGRATION.md`, `keycloak/`, `traefik/`, `templates/`, `apps/`, `docs/` (no top-level README) |
| **Portage** | `~/dev/claude-lanes/` | "Commons", "claude-lanes", "inference plane" | **Active build, most recently touched.** LiteLLM tier ladder, deterministic verifier, Parity Bench. Last commit 2026-07-20/21. **No git remote — local only.** | `pyproject.toml`, `PLATFORM.md`, `HANDOFF.md`, `PROJECT.md`, `specs/00–09`, `herdr/`, `herdr-meters/` |
| **Outfitter** | *(none)* | "compute brokering layer" | **No repository.** Described only in grant/strategy narrative (Codespaces, HPC, Jetstream2, Pegasus, ACCESS Discover, cost reporting). Adjacent: `InfoSciCourses/compute-cost-simulator/` (April 2026 teaching tool). | Narrative in `educloud/grants/*`, `educloud/strategy/*`; `compute-cost-simulator/` has `pyproject.toml`, `ccs/`, `dashboard/` |

---

## 3. Document inventory (planning / design / grant / governance / brand)

Dates are last-modified (YYYY-MM-DD). "Match" = which §4 target-checklist item the file satisfies.

### Umbrella — strategy / grants / architecture / onboarding

| Path | Date | ~Size | One-line | Match |
|---|---|---|---|---|
| `educloud/START-HERE.md` | 2026-06-13 | 7 KB | Index + next steps for the whole EduCloud folder ("working name; alternatives Quad/Cairn"). | START-HERE / index |
| `educloud/strategy/EduCloud-business-plan.md` | 2026-06-12 | 30 KB | "EduCloud — Business & Operating Plan." | Business plan |
| `educloud/strategy/EduCloud-funding-strategy.md` | 2026-06-12 | 14 KB | "Diversified Funding Strategy" — portfolio ranked by viability. | Funding specification |
| `educloud/strategy/EduCloud-team-funding-roadmap.md` | 2026-06-12 | 13 KB | "Team, Funding & Integrated Roadmap" — two-anchor grant teams + timeline. | Team funding roadmap |
| `educloud/strategy/EduCloud-financial-model.xlsx` | 2026-06-11 | 15 KB | Parameterized financial model (xlsx; outside md/docx/html/txt scope, noted). | (supports funding) |
| `educloud/strategy/willamette-pitch.md` | 2026-06-11 | 5 KB | Willamette positioning / tenure-track proposal template. | — |
| `educloud/architecture/EduCloud-registry-federation-proposal.md` | 2026-06-11 | 8 KB | "EduCloud Registry & Federation Layer" — Markwart's contribution. | Registry/Waypoint federation proposal |
| `educloud/architecture/EduCloud-hosting-reconciliation.md` | 2026-06-11 | 9 KB | "Reconciling the Hosting Platform with EduCloud" → Coolify. | Hosting reconciliation memo (Coolify) |
| `educloud/grants/PESOSE-Track1/EduCloud-PESOSE-Track1-draft.md` | 2026-06-12 | 21 KB | PESOSE Track 1 Project Description (working draft). | Funding specification |
| `educloud/grants/PESOSE-Track1/EduCloud-PESOSE-Track1-budget.md` | 2026-06-13 | 6 KB | PESOSE Track 1 budget & justification. | Funding specification |
| `educloud/grants/PESOSE-Track1/SEPTEMBER-sprint-plan.md` | 2026-06-12 | 7 KB | Week-by-week sprint to a Sept 1, 2026 PESOSE submission. | — |
| `educloud/grants/PESOSE-Track1/letters-of-collaboration-asks.md` | 2026-06-12 | 8 KB | LOC templates + recipients for the September PESOSE. | — |
| `educloud/grants/IUSE-ESL-Level1/EduCloud-IUSE-ESL-Level1-draft.md` | 2026-06-11 | 20 KB | IUSE EDU ESL Level 1 Project Description (working draft). | Funding specification |
| `educloud/grants/IUSE-ESL-Level1/EduCloud-IUSE-ESL-Level1-budget.md` | 2026-06-11 | 5 KB | IUSE ESL Level 1 budget & justification. | Funding specification |
| `educloud/grants/EduCloud-adopter-LOC-recruitment-kit.md` | 2026-06-11 | 9 KB | Adopter / letter-of-collaboration recruitment kit + templates. | — |
| `educloud/grants/foundations/README.md` | 2026-06-11 | 2 KB | Send-order map for the 7 non-NSF foundation drafts. | — |
| `educloud/grants/foundations/Sloan-OpenSource-in-Science-LOI.md` | 2026-06-11 | 5 KB | Sloan "Open Source in Science" 2-page flagship LOI. | — |
| `educloud/grants/foundations/Sloan-OSPO-Willamette-LOI.md` | 2026-06-11 | 4 KB | Sloan University-OSPO LOI (conditional on Willamette move). | — |
| `educloud/grants/foundations/Hewlett-OER-LOI.md` | 2026-06-11 | 4 KB | Hewlett Open Education LOI ("Sol/OER framing"). | — |
| `educloud/grants/foundations/ECMC-concept-paper.md` | 2026-06-11 | 4 KB | ECMC Foundation concept paper. | — |
| `educloud/grants/foundations/Ascendium-concept-paper.md` | 2026-06-11 | 4 KB | Ascendium Education Philanthropy concept paper. | — |
| `educloud/grants/foundations/NLnet-NGI-application.md` | 2026-06-11 | 4 KB | NLnet NGI/Commons Fund application (Registry standard). | — |
| `educloud/grants/foundations/Spencer-small-research-grant.md` | 2026-06-11 | 4 KB | Spencer small research grant hedge if IUSE misses. | — |
| `educloud/onboarding/John-Chen-orientation.md` | 2026-06-12 | 10 KB | Read-in for John Chen; PESOSE-September question teed up. | — |
| `educloud/mesa/educloud-mesa-integration.html` | 2026-06-11 | 22 KB | Interactive MESA integration page (incl. Registry). | **Architecture diagram (HTML)** |
| `educloud/project-docs/README.md` | 2026-06-11 | 6 KB | Repo README titled "Quad" (umbrella snapshot). | — |
| `educloud/project-docs/GOVERNANCE.md` | 2026-06-11 | 6 KB | "Quad Governance" — founding stewards. | Governance |
| `educloud/project-docs/CONTRIBUTING.md` | 2026-06-11 | 4 KB | "Contributing to Quad" — DCO, license split. | Governance |
| `educloud/project-docs/diagrams/quad-roadmap.svg` | 2026-06-11 | 10 KB | Funding/launch roadmap diagram (SVG). | (diagram, not HTML) |
| `educloud/project-docs/diagrams/quad-mesa-integration.svg` | 2026-06-11 | 12 KB | EduCloud × MESA architecture diagram (SVG). | (diagram, not HTML) |

### The Ben Markwart brief (four files, two versions)

| Path | Date | One-line | Match |
|---|---|---|---|
| `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart-rev2.docx` | **2026-07-08** | **July refresh — NEWEST version.** | **Ben brief (July)** |
| `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart.docx` | 2026-06-13 | June brief (byte-identical to the collaborators copy). | Ben brief (June) |
| `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart.pdf` | 2026-06-13 | June brief, PDF render. | Ben brief (June) |
| `educloud/collaborators/Ben Markwart/EduCloud-Brief-for-Ben-Markwart.docx` | 2026-06-13 | June brief (identical md5 to onboarding copy). | Ben brief (June) |
| `educloud/collaborators/Ben Markwart/EduCloud-Brief-for-Ben-Markwart.pdf` | 2026-06-13 | June brief PDF (identical md5 to onboarding copy). | Ben brief (June) |
| `educloud/collaborators/John Chen/00-START-EduCloud-Orientation-for-John-Chen.docx` / `.pdf` | 2026-06-12 | John Chen orientation (docx + pdf). | — |

### Module specs & governance

| Path | Date | One-line | Match |
|---|---|---|---|
| `quad/DESIGN.md` | 2026-06-11 | "Design Doc — Open-Source Classroom Platform." | **DESIGN.md / architecture spec** |
| `quad/README.md` | 2026-06-16 | "Quad" — host-agnostic auto-grading platform; status alpha. | — |
| `quad/ROADMAP.md` | 2026-06-04 | Quad roadmap. | — |
| `quad/CONTRIBUTING.md` / `CODE_OF_CONDUCT.md` / `LICENSE` | 2026-06-03 | Quad governance set (differs from the project-docs copies). | Governance |
| `quad/docs/github-setup.md` | 2026-06-14 | GitHub adapter setup ("already implemented — configuration only"). | — |
| `quad/docs/forgejo-setup.md` / `gitlab-setup.md` / `migrating-github-to-forgejo.md` | 2026-06-13/16 | Per-host setup guides. | — |
| `peer-tutor-framework/ARCHITECTURE.md` | 2026-06-18 | Belay architecture — evaluation-first tutor loop + Governance gate. | Architecture spec (module) |
| `peer-tutor-framework/GROUND_TRUTH.md` | 2026-06-18 | Read-only audit of the framework. | — |
| `peer-tutor-framework/VALIDATION.md` | 2026-06-18 | 79 KB validation record. | — |
| `peer-tutor-framework/LICENSING.md` / `CONTRIBUTING.md` / `CODE_OF_CONDUCT.md` / `DCO` / `PRIVACY.md` | 2026-06-17/18 | Full governance + privacy set. | **Governance (LICENSING, DCO, CoC, CONTRIBUTING)** |
| `HOST/PLAN.1.md` | (commit 2026-06-16) | "Build the EduCloud Hosting Layer on Coolify." | — |
| `HOST/INTEGRATION.md` | (commit 2026-06-16) | How the hosting layer relates to EduCloud/Quad and MESA. | — |
| `HOST/CHANGELOG.md` | (commit 2026-06-16) | Document history for the hosting layer repo. | — |
| `HOST/CLAUDE_CODE_INSTRUCTIONS.md` | (commit 2026-06-16) | Complete operating instructions for Claude Code build. | **Claude Code prompt/build file** |
| `HOST/HOST_SESSION_BUILD.md` | (commit 2026-06-16) | Project memory for the hosting build session. | Claude Code build file |
| `HOST/docs/ONBOARDING.md` / `REQUIREMENTS.md` / `TENANTS.md` | (commit 2026-06-16) | Publish/requirements/tenancy guides. | — |
| `HOST/docs/STATUS_DECK.html` | (commit 2026-06-16) | Hosting-layer status deck (HTML). | (2nd HTML deck) |
| `claude-lanes/PLATFORM.md` | 2026-07-21 | "final definition (working name: Commons)" — architecture capstone. | Architecture spec (module) |
| `claude-lanes/PROJECT.md` | 2026-07-20 | "quota- and sovereignty-aware routing for coding agents." | **PROJECT.md / ledger** |
| `claude-lanes/HANDOFF.md` | 2026-07-21 | Build instructions, phases 0–10, acceptance criteria. | Claude Code build file |
| `claude-lanes/KICKOFF-PROMPT.md` | 2026-07-20 | "Kickoff prompt for Claude Code," session 1. | **Claude Code prompt file** |
| `claude-lanes/EDUCLOUD-BRIEF.md` | 2026-07-20 | Positioning brief: decentralized AI as public infrastructure. | — |
| `claude-lanes/CLAUDE.md` | 2026-07-16 | Repo operating instructions for Claude Code. | Claude Code prompt file |
| `claude-lanes/KNOWN_GOOD_VERSIONS.md` | 2026-07-21 | Pinned known-good dependency versions. | — |

Brand assets: `educloud/educloud-avatar-light-1024.png` is the only brand file found. **No `educloud-brand.md` exists** (see §6).

---

## 4. Match list — target checklist

| Target | Result |
|---|---|
| Ben Markwart brief — June | `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart.docx` (+ identical copy in `collaborators/Ben Markwart/`), 2026-06-13. Matched on title + June content. |
| Ben Markwart brief — July refresh | `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart-rev2.docx`, **2026-07-08 — the NEWER of the two.** Matched on `-rev2` + latest mtime. |
| DESIGN.md / architecture spec | `quad/DESIGN.md` ("Design Doc — Open-Source Classroom Platform"). Module-level specs also exist: `peer-tutor-framework/ARCHITECTURE.md`, `claude-lanes/PLATFORM.md`, `HOST/PLAN.1.md`. |
| Architecture diagram as HTML | `educloud/mesa/educloud-mesa-integration.html` (interactive, incl. Registry). Also `HOST/docs/STATUS_DECK.html`. (SVG diagrams in `project-docs/diagrams/`.) |
| Funding specification | `educloud/strategy/EduCloud-funding-strategy.md` (primary), plus the PESOSE/IUSE grant drafts + budgets. |
| Business plan | `educloud/strategy/EduCloud-business-plan.md`. |
| Team funding roadmap | `educloud/strategy/EduCloud-team-funding-roadmap.md`. |
| PROJECT.md / project ledger | `claude-lanes/PROJECT.md` (Portage only). No umbrella-level PROJECT ledger. |
| START-HERE / index | `educloud/START-HERE.md`. |
| Brand document (`educloud-brand.md`) | **MISSING.** Only a PNG avatar exists. |
| Registry / Waypoint federation proposal | `educloud/architecture/EduCloud-registry-federation-proposal.md`. |
| Hosting reconciliation memo (Coolify) | `educloud/architecture/EduCloud-hosting-reconciliation.md`. |
| `docs/policy/` directory | **MISSING.** No `policy/` dir in any EduCloud folder (only false hits inside `.venv`). |
| Watch-items file | **MISSING.** No watch-items file anywhere in the EduCloud folders. |
| Governance: LICENSING.md | `peer-tutor-framework/LICENSING.md`. (No umbrella-level LICENSING.md.) |
| Governance: CONTRIBUTING.md | `educloud/project-docs/CONTRIBUTING.md`, `quad/CONTRIBUTING.md`, `peer-tutor-framework/CONTRIBUTING.md`. |
| Governance: DCO | `peer-tutor-framework/DCO`. (Referenced but no DCO file in quad or HOST.) |
| Governance: CODE_OF_CONDUCT.md | `quad/CODE_OF_CONDUCT.md`, `peer-tutor-framework/CODE_OF_CONDUCT.md`. |
| Governance: GOVERNANCE.md | `educloud/project-docs/GOVERNANCE.md`. |
| Claude Code prompt / build files | `HOST/CLAUDE_CODE_INSTRUCTIONS.md`, `HOST/HOST_SESSION_BUILD.md`, `claude-lanes/KICKOFF-PROMPT.md`, `claude-lanes/HANDOFF.md`, `claude-lanes/CLAUDE.md`. |
| System definition / source of truth | **MISSING / not yet saved** (see §0, §5). |

**Missing targets:** system-definition doc · brand document (`educloud-brand.md`) · `docs/policy/` directory · watch-items file · umbrella-level PROJECT ledger.

---

## 5. Stale documents (quoted claims)

The whole corpus predates the rename, so *every* doc that names a module is
technically stale against the new scheme. The concrete, checkable instances:

**(a) Prior module names used as current components** — Sol, Registry, Quad, Commons:

- **Quad** — `educloud/project-docs/README.md`: `# Quad`; `educloud/project-docs/GOVERNANCE.md`: `# Quad Governance`; `quad/README.md`: "Quad" as the platform name. (Should be Cairn.)
- **Registry** — `educloud/architecture/EduCloud-registry-federation-proposal.md`: `# EduCloud Registry & Federation Layer`; `START-HERE.md`: "…and the EduCloud Registry on top." (Should be Waypoint.)
- **Sol** — `educloud/strategy/EduCloud-team-funding-roadmap.md`: "his Pedalogical guardrailed-AI-tutor work maps directly onto **Sol**"; "learning tech / the **Sol** dimension"; "**Sol**/AI GA." (Should be Belay.)
- **Commons** — `claude-lanes/PLATFORM.md`: "final definition (working name: **Commons**)"; `claude-lanes/README.md`: `# Commons`. (Should be Portage.)

**(b) Superseded PESOSE deadline** — September 1, 2026 (superseded by NSF 26-506, Track 1, **March 2, 2027**):

- `educloud/grants/PESOSE-Track1/SEPTEMBER-sprint-plan.md`: "We are preparing PESOSE Track 1 for the **September 1, 2026** deadline … rather than March 2027."
- `educloud/grants/PESOSE-Track1/EduCloud-PESOSE-Track1-draft.md`: "**Target deadline:** September 1, 2026 … accelerated from March 2027."
- Also names Sept 1, 2026 as current: `START-HERE.md`, `onboarding/John-Chen-orientation.md`, `strategy/EduCloud-business-plan.md`, `strategy/EduCloud-funding-strategy.md`, `strategy/EduCloud-team-funding-roadmap.md`. (`START-HERE.md` and the two strategy roadmap docs are internally inconsistent — they cite both Sept 1 2026 and Mar 2 2027.)
- The whole `grants/PESOSE-Track1/letters-of-collaboration-asks.md` is framed "Ready to Send (September PESOSE)."

**(c) GitHub host adapter described as complete** (it is in progress):

- `quad/docs/github-setup.md:9`: "The GitHub adapter is already implemented — this is configuration only, no code."
- `educloud/project-docs/README.md:25`: "**Done — Control plane + GitHub adapter.**"
- `educloud/onboarding/John-Chen-orientation.md:27`: "The GitHub and Forgejo adapters are complete and live-validated."

---

## 6. Duplicates & near-duplicates (recommendation only — nothing resolved)

1. **Ben brief, June — exact duplicate.** `educloud/onboarding/EduCloud-Brief-for-Ben-Markwart.docx` and `educloud/collaborators/Ben Markwart/EduCloud-Brief-for-Ben-Markwart.docx` are **byte-identical** (same md5); same for the two `.pdf` copies. The **July `-rev2.docx` (2026-07-08)** supersedes both. *Suggested canonical: `-rev2.docx`; the June docx/pdf pairs are outdated copies kept in two places.*

2. **"Quad" governance docs — near-duplicate, materially different.** `educloud/project-docs/{README,CONTRIBUTING}.md` vs `quad/{README,CONTRIBUTING}.md` have **different md5s** — they are separate, diverged copies. The `project-docs/` set is the umbrella "curated" snapshot (adds the Registry layer); the `quad/` set is the versioned repo copy. *Suggested canonical: the `quad/` repo copies for the live project; treat `project-docs/` as an umbrella snapshot that has drifted and needs a re-sync.*

3. **EduCloud brief, two homes.** A stakeholder-positioning "EduCloud brief" exists both as `claude-lanes/EDUCLOUD-BRIEF.md` (Portage-authored) and conceptually overlaps the Ben brief — different documents, not copies, but worth noting they compete as "the EduCloud brief."

4. **Two status HTMLs.** `educloud/mesa/educloud-mesa-integration.html` and `HOST/docs/STATUS_DECK.html` are different artifacts; neither is a dup, but there is no single canonical architecture diagram.

---

## 7. Things the descriptions did not account for (where it looks like real work)

- **`claude-lanes/` (Portage) is the most active repo and has no git remote** — local-only, last touched 2026-07-20/21, with a full `specs/00–09` reasoning record, `herdr/` + `herdr-meters/` implementation, and pinned `KNOWN_GOOD_VERSIONS.md`. This is substantial unpushed work; a laptop loss would lose it.
- **`HOST/` file mtimes all read 2026-07-21 16:35** (the moment folder access was granted) while its last real commit is 2026-06-16 — the recent timestamps are a checkout/mount artifact, not edits. Judge HOST activity by commit date, not mtime.
- **`peer-tutor-framework/` (Belay) is the most governance-complete module** — it alone carries `DCO`, `LICENSING.md`, `PRIVACY.md`, `CODE_OF_CONDUCT.md`, plus a 79 KB `VALIDATION.md` and a `STATE_AUDIT_DOMAIN.md`. The governance maturity lives here, not in the umbrella.
- **`quantum-inventioneers/`** is the quantum tutor that Belay's domain-agnostic core was extracted from (per `peer-tutor-framework/README.md`) — lineage worth tracking, though it is a separate app, not a module.
- **`InfoSciCourses/compute-cost-simulator/`** (April 2026, Python, has a `dashboard/`, `curriculum/`, `teaching/`) is the closest thing to Outfitter's "cost reporting" — a possible precursor/asset to fold in.
- **Two GitHub orgs in play:** `github.com/Gchism94/` (quad, peer-tutor-framework — personal) vs `github.com/EduCloud-Ecosystem/` (HOST — org). Portage isn't on GitHub at all. Naming/ownership of the module repos is not yet consolidated under one org.
- **The umbrella `educloud/` is a plain folder, not a repo** — none of the strategy/grant/architecture planning corpus is under version control.
- **`educloud/strategy/EduCloud-financial-model.xlsx` and `quad/docs/quad-contributor-tracker.xlsx`** are live spreadsheets (outside the md/docx/html/txt inventory scope) that carry real planning data.

---

*End of inventory. No files were edited, renamed, moved, or resolved. Every decision surfaced here is left to Greg.*
