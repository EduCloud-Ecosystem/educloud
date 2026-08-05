# EduCloud — Platform Status & Pilot Priorities

*Assessed 2026-07-21 against git history, roadmaps, changelogs, and validation
records in each module repo. Companion to `EDUCLOUD-INVENTORY.md` (the July 21
orientation pass). Names used are the current scheme — Cairn, Belay, Waypoint,
Portage, Outfitter — with prior on-disk names noted.*

> Note (July 22): this is the July 21 snapshot. For sequencing, the plan of
> record is `LINE-E-ROADMAP.md` (E0–E4) with `claude-lanes/LINE-P-ROADMAP.md`
> for the personal line; SYSTEM.md §7 carries the consolidation.

## 0. Executive summary

The platform's forcing function is external and immovable: **GitHub Classroom
shuts down August 28, 2026, with final data deletion September 4** (Cairn
ROADMAP). Fall courses start the same week. Everything else — both NSF
proposals, adopter letters, the flagship story — feeds on a Fall 2026 pilot
actually running.

The uncomfortable finding: **the module with the hardest deadline is the one
currently idle.** Cairn's last commit is June 14 (five weeks ago); the recent
energy went to Portage (July 20–21). Cairn is also the *closest to done* — its
Phase 1 MVP is complete and the host-agnostic adapters have landed — so the
remaining pilot gap is small and concrete. The single most important resource
decision right now is to point the build effort back at Cairn until a pilot
deployment exists.

Second finding: the five modules are architecturally coherent but **the
platform-level glue is entirely undocumented on disk**. No system-definition
doc exists; the five-name scheme appears nowhere except this week's reports;
the umbrella folder isn't under version control; Portage still has no pushed
remote. The glue items are cheap (days) and high-leverage — they're what makes
five repos read as one platform to a reviewer, a collaborator, or a Dean.

## 1. Module-by-module

### Cairn — classroom layer (`~/dev/quad`, remote: EduCloud-Ecosystem/cairn)

**Status: strongest module; MVP complete; idle since June 14.**

Evidence: ROADMAP Phase 1 fully checked — GitHub App auth, classrooms,
assignments from templates, student self-claim join, idempotent provisioning
queue, deadline auto-lock, **sandboxed container grading** (network/memory/
cpu/pids limits, dropped caps, read-only rootfs), CSV score export, instructor
dashboard (React/Vite), Postgres store behind a build tag, operator auth.
Commits past the roadmap file: webhook receiver with secret threading, student
sessions + scoped API + student page, **Forgejo adapter** (README: working
end-to-end), **GitLab adapter + OAuth resolver**. 17 Go test files. Deploy is
a single docker-compose.

**Remaining for a Fall pilot (the 1.0-beta gap):**
- **GHC import** — the migration path for instructors leaving Classroom. The
  single highest-value missing feature; it's the difference between "an
  alternative" and "the replacement." Not started (no commit evidence).
- `doctor` self-diagnostics + one-command deploy hardening (compose exists;
  needs the paved path an instructor can follow alone).
- Student-facing views completion (instructor console done; student page
  landed but marked follow-up).
- Instructor onboarding docs (setup guides exist per host; no end-to-end
  "migrate your course in an afternoon" doc).
- A real deployment running a real course section — pilot infrastructure
  (see Waypoint P1).
- Doc drift: ROADMAP.md Phase 2 checkboxes are stale (Forgejo/GitLab shipped
  per commits/README but unchecked) — update before anyone external reads it.

**Explicitly deferrable past the pilot:** LMS roster agent (Phase 3 — CSV
import suffices), LTI integration (Phase 4), multi-tenant hosted offering.

**Modularity/holism:** the host-adapter seam is the platform's reference
pattern (Outfitter's provider adapters copy it). Needs: adopt the shared
attribution vocabulary ({course, assignment, student} opaque labels) in its
data model exports; an OIDC seam so Waypoint/Keycloak can front identity later
(own OAuth now is fine); DCO file missing (Belay has one; Cairn doesn't).

### Belay — peer AI tutor (`~/dev/peer-tutor-framework`, remote: Gchism94)

**Status: deepest engineering rigor of the five; feature-complete core; parked
since June 18.**

Evidence: evaluation-first loop with the deterministic leak/Governance gate;
338-test baseline (Slice O floor per VALIDATION); license-gated, pack-scoped
knowledge/corpus pipeline with BM25 indexing just landed (Slice O); DS pack as
reference, `_skeleton` pack seam for new domains; full governance set (DCO,
LICENSING, PRIVACY, CoC); 79 KB VALIDATION.md as the build record.

**Remaining (from its own ROADMAP, all cited to in-tree sources):**
- Reasoner-prompt de-quantum (eval-gated — still carries quantum-era worked-
  example guidance from the extraction origin) + the DS claim-check it bundles.
- Real corpus ingestion (operator step — pipeline built, only seed corpus
  ships), live strong-judge benchmark (pending a local endpoint — **a Portage
  integration point**), measure-key cleanup.
- **Instructor mode is net-new** (no auth on the API today) — required before
  any real course pilot with students; this is the biggest gap between "framework"
  and "product."
- Containerized runner (the recorded convergence point with Cairn's grading
  containment), facilitator benchmark family, more DomainPacks, naming/publish
  (repo name is a placeholder, final name pending an atomic commit — it's Belay).

**Modularity/holism:** already the governance model for the others. Needs:
move to EduCloud-Ecosystem org; the strong-judge endpoint and all student-lane
inference should declare Portage policy modes (student lanes = `sovereign`);
its `cohort` field aligns with the shared attribution vocabulary — codify it.

### Waypoint — publishing/federation (`~/dev/HOST`, remote: EduCloud-Ecosystem/HOST)

**Status: local pre-build proven; blocked on a server; the Registry proper not
started.**

Evidence: Phase 0 done (requirements, tenant intake, onboarding contract,
templates); Phase 1.5 done (local Coolify stack, Keycloak realm export, full
visitor-auth round trip proven locally, five demo apps with instantiated
Dockerfiles); Phase 1 (provision) pending budget — provider decision moved
Hetzner → DigitalOcean. Phases 2–9 (install/secure Coolify, Keycloak on
server, tenant onboarding, auth matrix, backups, launch) await the server.
CHANGELOG is a disciplined doc-history; STATUS_DECK.html exists.

**Remaining:**
- **Provision the server** (the only blocker for Phases 2–9; a budget
  decision, not an engineering one).
- Phases 2–9 per PLAN.1.md — largely configuration by design.
- **The Registry itself** — catalog, search, register CLI, federation
  metadata standard — exists only as the June proposal doc
  (`educloud/architecture/EduCloud-registry-federation-proposal.md`). PLAN.1
  deliberately only "prepares its seam" (a scoped Coolify API token). This is
  Ben Markwart's funded workstream; it needs to exist in credible draft form
  by grant-writing season (~Dec), not by pilot.
- Repo hygiene: no top-level README, no LICENSE, no governance files — the
  only module a stranger can't orient in. Rename HOST → waypoint when
  convenient.

**Modularity/holism:** Waypoint is the *deployment substrate* for everything —
Coolify hosts Cairn, Belay, Portage's LiteLLM proxy, demo tenants; Keycloak is
the ecosystem identity provider every module's OIDC seam eventually points at.
The onboarding contract ("a Coolify application IS the contract") is the right
shape; make each sibling module ship a conforming template.

### Portage — model routing (`~/dev/claude-lanes`, remote: EduCloud-Ecosystem/portage — **unpushed**)

**Status: most active; Phases 0–1 built and verified; Scale-1 transition fully
specified this week; Phase 6a ready for its build session.**

Evidence: LiteLLM spine smoke-tested; Claude Code → LiteLLM direct connection
verified and documented (phase-1-findings); ruff/pytest green; versions
pinned. This week: specs/10–11 (open-weight-only end state; hybrid PAYG
transition), REVISION-PLAN.md, and the full doc pass (unified T0–T7 ladder,
`proprietary_displacement` flip metric, escalation boundary, per-lane policy
modes). KICKOFF-PROMPT now scopes the Phase 6a session.

**Remaining:**
- Phase 6a build (OpenRouter allowlist + Together + PAYG ceiling as LiteLLM
  config; `unavailable`/`model_failed` split in failup.py; displacement +
  rescue reports in measure.py; bench baseline before subscription
  cancellation). Personal pilot = Greg's working version.
- Phases 2–5 hardening items not yet done (stub-runner test suite for the
  guard/decomposer, herdr plugin verification, maintenance rails).
- Later: sovereign tier wiring (Jetstream2), Parity Bench, learning loop.
- **Push the repo.** Still local-only. One `git push -u origin main` ends the
  single-disk risk that has now persisted through two status reports.

**Modularity/holism:** defines the policy-mode vocabulary (`sovereign` /
`open_weight_only` / `hybrid`) the whole platform uses for data-sensitivity
posture; its spend logs share the attribution vocabulary; Belay is its first
in-platform consumer (strong-judge endpoint, student-lane inference).

### Outfitter — compute brokering (`~/dev/outfitter`, remote: EduCloud-Ecosystem/outfitter — unpushed)

**Status: M0 spec-first scaffold only (July 21); no code.**

Evidence: DESIGN (broker/adapter control plane in Go, mirroring Cairn's
pattern), specs 00–05 (adapter interface, cost model, budget guards, Cairn
integration, MVP scope), governance, Claude Code kickoff — all committed
(`d42bd0a`).

**Remaining:** everything past specs — M1 skeleton (adapter interface +
docker reference adapter + conformance harness), M2 codespaces + guards, M3
Cairn integration, M4 research providers. Plus one **admin item that
shouldn't wait for code: file the ACCESS Discover allocation** (~2-week
turnaround; removes compute from both grant budgets per START-HERE; also
unblocks future Jetstream2 work for Portage's sovereign tier).

**Modularity/holism:** by design already — it copies Cairn's adapter seam,
shares the attribution vocabulary with Portage's ledger, and its budget-safe
invariant (no provisioning without ceiling + lifetime + teardown) is the
platform's verifier philosophy applied to money.

### The umbrella (`~/dev/educloud` + org level)

**Status: rich June corpus, now visibly stale; not under version control.**

Remaining: the system-definition document (the white paper now covers the
outward-facing half; a short SYSTEM.md should cover the internal contracts);
name propagation (Quad/Sol/Registry/Commons → current names across ~15 docs);
the PESOSE date correction (Sept 1, 2026 → **NSF 26-506 Track 1, March 2,
2027**) in seven documents; `git init` the umbrella (grants/strategy work has
no history or backup); brand doc (`educloud-brand.md` — only a PNG exists);
org consolidation (Belay still on the personal account; HOST rename); the two
xlsx models kept current.

## 2. The holistic layer — what makes five modules one platform

These are the shared contracts. None is expensive; together they're the
difference between a suite and a platform.

1. **The verifier invariant (the signature).** No module trusts a model's — or
   a provider's — self-report: Cairn's sandboxed autograder, Belay's leak gate,
   Portage's fail-up guard, Outfitter's conformance tests and budget guards.
   State it once in SYSTEM.md and in the white paper; it is the platform's
   thesis and its differentiator in every grant narrative.
2. **Attribution vocabulary.** Opaque `{course, assignment, student}` labels
   flow through Cairn rosters, Outfitter's cost ledger, Portage's spend logs,
   Belay's cohort measures. Already consistent by design — codify it so it
   stays that way.
3. **Policy modes.** `sovereign` / `open_weight_only` / `hybrid` (defined in
   Portage) are the platform's data-sensitivity posture. Student-facing lanes
   default `sovereign`; enforced by config absence, never runtime checks.
4. **Identity.** Keycloak (Waypoint) is the ecosystem OIDC provider; every
   module keeps a bring-your-own-OIDC seam now and points it at Waypoint when
   the server exists.
5. **Deployment contract.** Every module ships a Coolify-conforming container
   ("the application is the contract"); Waypoint's templates directory is the
   registry of record.
6. **Governance floor.** Apache-2.0 + DCO + CoC + CONTRIBUTING in every repo
   (Belay is the model; Cairn lacks DCO; Waypoint lacks everything), and one
   ecosystem-level GOVERNANCE doc under the org.
7. **One org.** EduCloud-Ecosystem for all five repos, pushed. Today: cairn ✓
   (remote set), portage ✓ (remote set, **unpushed**), outfitter ✓ (unpushed),
   HOST ✓ (pushed, needs rename), Belay ✗ (personal account).
8. **One definition.** SYSTEM.md + the white paper carry the five-name scheme;
   everything else links to them instead of restating.

## 3. Priority stack for piloting

| P | What | Why now | Effort shape |
|---|---|---|---|
| **P0** | **Cairn → pilot-ready**: GHC import, doctor + one-command deploy, student views, instructor migration doc, roadmap-file refresh | Aug 28 shutdown; ~5 weeks; it's closest to done and highest external stakes; every grant artifact downstream depends on a running pilot | The build focus until it ships |
| **P1** | **Provision the Waypoint server** and run Phases 2–3 (Coolify + Keycloak), then deploy Cairn on it | The pilot needs a host; local pre-build already proved the stack; this is a budget decision blocking config work | Hours of work once the droplet exists |
| **P2** | **Umbrella coherence**: SYSTEM.md, name propagation, PESOSE date fixes, `git init` educloud/, push Portage/Outfitter, move Belay to the org | Days of work; converts five repos into one reviewable platform; ends the unpushed-work risk | A focused day or two |
| **P3** | **File the ACCESS Discover allocation** | 2-week turnaround, pure admin, unblocks grant budgets + the future sovereign tier | An afternoon |
| **P4** | **Portage Phase 6a** (the scoped Claude Code session) | Personal pilot momentum + publication window; fully specified; runs in parallel without eating Cairn's clock | Parallel track, session-sized |
| **P5** | **Belay: instructor mode design + prompt de-quantum**, aiming at a single-course pilot late fall | Not needed for the GHC replacement; is the grant differentiator; instructor mode is the product gap | After P0 ships, or as background design |
| **P6** | **Outfitter M1** (docker adapter + conformance) | Cairn's container runner covers pilot grading; broker earns its build after the pilot | Post-pilot |
| — | **Waypoint Registry draft (Ben)** | Grant-season deadline (~Dec), not pilot; needs a credible draft + the Coolify seam | Parallel, Ben's track |

**The sequencing in one line:** Cairn until it runs a real course, Waypoint
just enough to host it, glue-week for the umbrella, Portage and Belay on
parallel tracks that never block the classroom.

## 4. Risks

- **Calendar risk (highest):** five weeks to shutdown; GHC import doesn't
  exist yet; instructors migrate in August or not at all this year.
- **Single-disk risk:** Portage and Outfitter are unpushed; the umbrella has
  no VCS at all. One disk failure erases the most active work.
- **Doc-drift risk:** roadmap checkboxes lag commits (Cairn), names lag the
  scheme (everywhere), a stale deadline sits in seven grant docs. Reviewers
  and collaborators read the docs, not the commits.
- **Bus-factor:** every module is effectively one person right now; the
  Registry is the only externally-owned workstream and it hasn't started.
- **Integration debt:** the holistic layer (§2) is all convention, no
  enforcement, until SYSTEM.md + org consolidation land.

## 5. Licence-gated items

- `EduCloud-Ecosystem/verifier-contract` (CC-P1 v2, 2026-08-05): created
  private, `LICENSING.md` states the intended Apache-2.0 grant. Goes public
  and Apache-2.0 when the University of Arizona IP release clears — same
  condition as `portage/LICENSING.md` and `belay/LICENSING.md`.
