# Line E roadmap — EduCloud, MVP to full build

> October 6, 2026 priority update: the current sequence is in
> `EDUCLOUD-STATUS.md` and `docs/decisions/2026-10-06-computing-continuity.md`.
> The stages below preserve the original plan; elapsed dates are not evidence
> that their exit criteria were achieved. Python/R computing continuity comes
> before requiring all five modules in a pilot.

*Original plan: July 2026. Scales the platform from the pre-shutdown MVP to the federated
full build. Timeline anchors are external and immovable: GitHub Classroom
retires August 28, 2026, IUSE closes about January 20, 2027, PESOSE Track 1
closes March 2, 2027, Track 2 and the MESA IDSS positioning sit in 2028.*

---

## What EduCloud is at each scale

| Scale | Deployment | Identity | Inference posture |
|---|---|---|---|
| MVP | one Waypoint host | Cairn sessions, OIDC seam stubbed | sovereign default, JS2 tier inserted |
| Pilot | one host, real course | same | same, measured |
| Institutional | Coolify multi-tenant | Keycloak | sovereign default, hybrid by instructor policy |
| Federated | cross-institution | CILogon | per-site provider registries |

The expansion contract favors portable interfaces and configuration, with explicit
code changes and data migrations where required. Each transition needs its own
authentication, isolation, operations and recovery acceptance evidence.

---

## E0 — MVP. Now to August 28, 2026.

The forcing function is the shutdown. Everything else yields to it.

- **Cairn pilot-ready:** GHC import, one-command deploy with doctor
  self-diagnostics, student views completed, the migrate-in-an-afternoon doc,
  roadmap files refreshed.
- **Waypoint host provisioned:** Coolify and Keycloak live per the proven
  local build. Cairn deployed on it.
- **Portage EduCloud profile:** the Scale 2 config diff cut against Line P's
  Scale 1. Inserts `institutional_sovereign` (JS2 vLLM) into `routing_order`,
  sets student lanes `sovereign` by absence, carries the attribution labels
  and the `regulated` classification. Reviewed as a diff.
- **First builds of all five modules** land by end of August, including the
  Outfitter broker skeleton and Belay's instructor-mode alpha.
- **Admin in parallel:** ACCESS Discover allocation filed, Sloan LOI sent,
  umbrella repo under version control, org consolidation done.

**Exit:** the project lead's own course is migrated before the shutdown and
the platform survives a stranger reading the repos.

## E1 — Pilot semester. Fall 2026.

- The pilot section runs the full semester from the first assignment.
- **Test gates execute:** component suites plus live course use for every
  module; grading-at-scale, Belay strong-judge, and Portage sovereign-tier
  full-implementation tests on Jetstream2 under the ACCESS allocation.
- **Belay single-course tutoring pilot** later in the term, instructor mode
  live, leak gate through the shared verifier contract.
- **The Registry draft** (Ben's workstream) reaches credible form by December.
- **Evidence harvest:** adopter letters collected as courses actually use
  Cairn, since PESOSE letters require current users. The Parity Bench
  twelve-task pilot cut runs, with the resource-tier factor seeded by Line P's
  two-Mac under-resourced arm. The evaluator is confirmed.

**Exit:** a semester of verified pilot data, letters in hand, both NSF
packages complete for Sponsored Projects by December.

## E2 — Grant season. Winter 2026 to spring 2027.

- IUSE ESL Level 1 submitted about January 20, 2027.
- PESOSE Track 1 (NSF 26-506) submitted March 2, 2027, carrying the verifier
  contract as the portable standard with two consumers in two languages, the
  maintenance-rails artifact, and the governance plan the planning grant is
  scoped to fund.
- Foundation LOIs (Hewlett, ECMC, Ascendium, Spencer, NLnet) go out with pilot
  data in the send-order sequence.
- Preregistered full Parity Bench run after the pilot closes; the equity
  finding lands either way and both outcomes publish.

**Exit:** both federal packages submitted, the foundation sequence moving,
the bench preregistration locked.

## E3 — Institutional scale. 2027.

- **Multi-course rollout** across INFO sections, then flagship adoption per
  the CALES and college briefs, grading-at-scale verified before each
  expansion.
- **Keycloak becomes the ecosystem identity provider:** every module's OIDC
  seam points at Waypoint. Multi-tenant Coolify onboarding per the tenant
  contract.
- **Cairn 1.0:** LMS roster sync, LTI grade passback, multi-tenant hosted
  option alongside self-hosting, so the zero-IT path exists and the Matthew
  filter stays open.
- **Outfitter research adapters:** HPC and Pegasus, conformance-tested against
  the live allocation, Cairn integration complete.
- **Belay additional DomainPacks** and the containerized runner converged with
  Cairn's grading containment.
- **Federation pilots** begin with two or three external adopters from the
  existing network, Registry live between them.

**Exit:** 1.0 releases across the modules, at least two external institutional
deployments, the managing-organization decision funded by Track 1 underway.

## E4 — Full build. 2027 to 2028.

- **PESOSE Track 2** submission in the 2028 cycle, funding the managing
  organization the governance charter describes, on demonstrated adoption.
- **Federation at scale:** the Registry as the cross-institution metadata
  standard, per-site provider registries, per-site data-use agreements
  following the federated model already designed for the HPC research.
- **The nonprofit stewardship transfer** executes per the IP structure held
  open since the waiver: Apache and AGPL split preserved, DCO preserved,
  foundation as long-term steward.
- **MESA IDSS positioning:** EduCloud as the education and broader-impacts
  infrastructure for the 2028 Category I submission.
- Full Parity Bench as a standing instrument, equity measured per deployment
  tier, results feeding the IUSE follow-on levels.

**Exit, the definition of done for Line E:** an independently governed,
federated, self-hostable platform where any source remains pluggable, student
lanes are sovereign by construction, every module passes deterministic gates,
equity is a measured number, and no part of it depends on one person or one
vendor.

---

## The dependency spine, one line per link

Cairn pilot gates the letters. Letters gate PESOSE. The pilot semester gates
the bench. The bench gates the equity claim IUSE needs. Track 1 gates the
managing organization. Adoption gates Track 2. Track 2 and adoption gate the
full build. Nothing downstream moves if the August deadline slips, which is
why E0 owns the build effort now.

## Standing rules

- The inclusion test admits every component: stable, auditable, reproducible,
  equitable, compliant by construction, cost-predictable.
- Portage on Line E serves four consumers: instructor-facing AI, Belay's
  tutoring lane, the AI sandboxes, and Outfitter's allocation planner (an
  operations lane; system telemetry only, never student content). Anything
  else must pass the inclusion test (stable, auditable, reproducible, equitable, compliant by construction,
  cost-predictable) and crosses as config against the shared engine, never
  code.
- Line P feeds Line E evidence and config, never code paths outside the shared
  engine. The two lines keep separate judgment by design.
- Every scale step ships as a reviewed config diff. SYSTEM.md carries the
  scale table as the expansion contract.
