# EduCloud — An Open Platform for Teaching with Code

*White paper · v0.9.3 public draft · July 2026 · CC BY 4.0 · module
names are provisional*

## 1. Executive summary

EduCloud is an open-source, self-hostable platform for teaching with
code. It distributes assignments to per-student Git repositories,
collects and grades submissions in sandboxed containers, provides an AI
peer tutor that is prevented by construction from revealing solutions,
publishes and federates course artifacts across institutions, routes AI
model calls so that student data stays on infrastructure the institution
controls, and provisions compute under explicit budgets. The platform
consists of five modules. They share one design rule: **success is
decided by deterministic checks (test suites, linters, resolvable
citations, budget guards), never by a model’s own report of success.**

**The core problem is ownership.** The infrastructure that teaching with
code depends on (assignment workflows, grading, and now the AI that
students and instructors use) is rented from vendors on their terms.
Student data leaves the institution, AI behavior is governed by prompt
instructions rather than enforcement, and tools disappear when a
vendor’s priorities change. **GitHub’s retirement of GitHub Classroom on
August 28, 2026** (final data deletion September 4) shows the problem in
practice: thousands of courses lose their workflow on a vendor’s
schedule. EduCloud exists so that institutions own this infrastructure
instead. It is community-owned, self-hostable, and vendor-neutral.
Cairn, its classroom layer, is the direct analogue of GitHub Classroom,
so the shutdown is the adoption moment; the platform’s purpose is larger
than the replacement. Long-term stewardship is designed around an
independent nonprofit foundation; code is licensed Apache-2.0 under a
Developer Certificate of Origin; and sustainability rests on a
diversified grant portfolio anchored by NSF PESOSE Track 1 (March 2,
2027) and NSF IUSE (January 2027).

## 2. The problem

- **Rented infrastructure.** The tools computing courses depend on are
  vendor-owned. Student data sits on commercial terms, roadmaps follow
  the vendor’s market, and a product retirement can end a course
  workflow, as the Classroom shutdown shows. Its successors repeat the
  pattern (thin GitHub-only clones or closed hosted products), so
  educators who need host choice, student privacy, or institutional
  hosting still have no durable option.

- **Ungoverned AI in coursework.** AI tutors are entering CS and
  data-science courses without an enforcement layer. Tutors reveal
  solutions, student prompts flow to third-party APIs under commercial
  terms, and spending has no ceiling. Prompt instructions alone do not
  constitute governance.

- **Short-lived infrastructure.** Teaching tools are often grant-funded,
  built, and then abandoned. Durability requires community ownership,
  open licensing, federation across institutions, and funding designed
  around that structure from the beginning.

## 3. The platform: five modules, one umbrella

| **Module**                                | **What it does**                                                                                                                                                                                                                                                                             | **Stack**          | **Status (July 2026)**                                                                                          |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------|
| Cairn (was Quad)                          | Classroom layer, the GitHub Classroom analogue: assignments to per-student Git repos, collection, sandboxed container autograding, instructor dashboard. Host adapters: GitHub, Forgejo, GitLab.                                                                                             | Go + React         | MVP complete; all three host adapters landed; remaining pilot work is migration tooling and the deployment path |
| Belay (was Sol)                           | Peer AI tutor: evaluation-first loop; a deterministic gate runs every draft through the domain grader and strips solutions; wellbeing safeguards; pluggable DomainPacks; license-gated knowledge corpus.                                                                                     | Python             | Framework complete (338-test baseline); instructor mode is the remaining product gap                            |
| Waypoint (was “HOST” / EduCloud Registry) | Publishing and federation: Coolify hosting engine, Keycloak identity, tenant onboarding contract; catalog, register CLI, and metadata standard for cross-institution discovery.                                                                                                              | Coolify + Keycloak | Local stack and auth round-trip proven; awaiting server provisioning; registry in proposal stage                |
| Portage (was Commons / claude-lanes)      | Model routing: open-weight-first tier ladder, deterministic fail-up verification, policy modes (sovereign / open-weight-only / hybrid), cost measurement.                                                                                                                                    | Python + LiteLLM   | Routing spine built and verified; open-first transition specified; personal pilot in progress                   |
| Outfitter (new)                           | Compute brokering: one API to place course workloads on Codespaces, campus HPC, Jetstream2, Pegasus, or Docker, always under a budget ceiling with cost attribution. A staged allocation planner (rules first, then an LLM) chooses and swaps providers automatically within those ceilings. | Go                 | Specification complete, including the planner; implementation not started                                       |

**The modules are designed to work independently.** An instructor can
run Cairn alone as a Classroom replacement. An institution can then add
Waypoint for hosting and identity, Belay for tutoring, Portage for
sovereign AI routing, and Outfitter for compute brokering. Each addition
is a deployment step; none requires migrating what already runs.

## 4. Design principles

- **Deterministic verification.** Cairn’s autograder, Belay’s leak gate,
  Portage’s fail-up guard, and Outfitter’s conformance and budget guards
  all apply the same rule: a deterministic runner decides whether an
  attempt succeeded. A model’s claim of success is never sufficient.

- **Pluggable boundaries.** The Git host is a plugin (Cairn), the
  compute provider is a plugin (Outfitter), the model behind each
  routing alias is configuration (Portage), and the tutoring domain is a
  pack (Belay). No single vendor is a hard dependency.

- **Sovereignty by configuration.** Three policy modes (sovereign,
  open-weight-only, hybrid) govern where inference may run.
  Student-facing lanes default to sovereign: the sensitive configuration
  contains no external providers at all, so a misroute cannot occur.

- **Minimal data.** The platform stores Git usernames and assignment
  state, never student records. Belay additionally keeps grades
  inaccessible to the tutor and includes distress-safety behavior;
  Outfitter and Portage log usage and cost against opaque identifiers.

- **Shared attribution.** Opaque {course, assignment, student} labels
  are used consistently across Cairn rosters, Outfitter’s cost ledger,
  Portage’s spend logs, and Belay’s cohort measures, so cost, usage, and
  outcomes aggregate the same way everywhere.

- **AI inside the envelope.** Models with system-level knowledge manage
  the platform’s resources: routing in Portage, and compute allocation
  in Outfitter, where a planner chooses providers, swaps workloads, and
  pre-provisions ahead of course deadlines from live telemetry and the
  course calendar. These managers act only through budget ceilings,
  policy modes, and audited decision logs they cannot alter, and a
  learned manager replaces a simpler one only after beating it in shadow
  on measured cost and reliability.

- **Reuse of existing tools.** Coolify, Keycloak, LiteLLM, and provider
  APIs are configured rather than reimplemented. Custom code is limited
  to the components that are genuinely new: the verifiers, the gates,
  and the measurement.

- **Scaling is configuration.** The platform expands MVP → pilot →
  institutional → federated, and each scale is a configuration diff
  against the previous one; a diff that contains code is treated as a
  defect. Identity follows the same path (course sessions →
  institutional Keycloak → CILogon federation), and at federation each
  site keeps its own provider registry.

- **Measured claims.** Efficiency and quality claims must pass a
  preregistered quality gate. Portage’s Parity Bench compares the open
  platform against the commercial products it replaces, and its
  displacement metric provides an empirical criterion for when
  proprietary AI can be retired.

## 5. Status and roadmap

**August 28 is the schedule driver.** The near-term plan concentrates on
Cairn (migration tooling, one-command deployment, instructor onboarding
documentation) and on standing up one Waypoint host, with a course
section taught by the project lead integrated for the full semester as
the first pilot. First builds of all five modules are targeted for the
end of August. Each module then passes two test gates during the fall:
component tests (deterministic suites and live course use) and, where
shared compute is involved, full-implementation tests on NSF ACCESS /
Jetstream2. Belay pilots in a single course later in the fall; Portage
continues as the maintainer’s working deployment; Outfitter’s broker
skeleton lands with the first builds and integrates after the classroom
pilot is stable. The fall pilots produce the adopter letters and
evidence both NSF proposals require.

Development runs on two lines. A personal line serves as the proving
ground, where components are exercised inclusively on the maintainer’s
own stack. The EduCloud line admits a component only when it is stable,
auditable, reproducible, equitable, compliant by construction, and
cost-predictable, and it crosses as configuration against the shared
engine, never as code. Within EduCloud, AI serves four consumers:
instructor-facing tools, the peer tutor, the grading sandboxes, and the
allocation planner that manages compute (an operations role: system
telemetry only, never student content).

| **Horizon**                   | **Milestones**                                                                                                                                                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Now → late Aug 2026 (MVP)     | Cairn pilot-ready before the shutdown (Classroom import, deploy path, docs); Waypoint server provisioned, Coolify + Keycloak live; first builds of all five modules; first pilot section migrated                 |
| Fall 2026 (pilot semester)    | Pilot section runs the full semester; component and full-implementation test gates on Jetstream2 / ACCESS; Belay single-course tutoring pilot; registry draft (Waypoint); adopter letters collected               |
| Winter 2026–27 (grant season) | NSF IUSE ESL Level 1 submission (~Jan 20, 2027); NSF PESOSE Track 1 submission (March 2, 2027); foundation LOIs in sequence; preregistered benchmark run after the pilot closes                                   |
| 2027 (institutional)          | Multi-course rollout; Keycloak as the ecosystem identity provider; Cairn 1.0 (LMS roster sync, LTI, hosted option); Outfitter research-compute adapters; federation pilots with two or three external adopters    |
| 2027–28 (full build)          | PESOSE Track 2 funding the managing organization; federation at scale (CILogon, per-site provider registries); nonprofit stewardship transfer per the IP structure held open; equity measured per deployment tier |

## 6. Governance and sustainability

Long-term stewardship is designed around an independent nonprofit
foundation; governance drafts, founding stewards, and a fiscal-sponsor
assessment already exist in the planning documents. In the near term,
intellectual property can rest with a founding university under
open-source terms, and the PESOSE Track 1 planning grant is scoped to
fund the formal stewardship decision. Code is Apache-2.0; documentation
is CC BY; every contribution carries a Developer Certificate of Origin
sign-off. Institutions self-host, there are no per-seat fees, and any
future hosted offering would be one deployment option alongside
self-hosting.

## 7. Funding strategy

| **Program**                                                      | **Deadline**                  | **Ask**         | **Status**                                                                                    |
|------------------------------------------------------------------|-------------------------------|-----------------|-----------------------------------------------------------------------------------------------|
| NSF PESOSE Track 1 (NSF 26-506) — open-source ecosystem planning | March 2, 2027                 | ≤\$300K / 1 yr  | Full draft and budget written; reframing to the confirmed deadline                            |
| NSF IUSE: EDU — ESL Level 1                                      | ~Jan 20, 2027                 | ≤\$400K / 3 yr  | Full draft and budget written; anchor institution being finalized                             |
| Sloan — Open Source in Science LOI                               | Rolling — send now            | 2-page LOI      | Drafted, ready to send                                                                        |
| Foundations: Hewlett OER, ECMC, Ascendium, NLnet, Spencer        | Spring 2027 (with pilot data) | Varies          | Concept papers drafted; sequenced in a send-order plan                                        |
| NSF ACCESS Discover allocation                                   | ~2-week turnaround            | Compute credits | To file now; removes compute costs from both NSF budgets and provides the fall test substrate |

The portfolio is deliberately diversified: NSF provides the anchor
grants, foundations complement them, and institutional adoption supplies
the recurring in-kind base. Results from the Fall 2026 pilots strengthen
every application in the table.

## 8. Getting involved

- Instructors: pilot Cairn as your classroom layer this fall. Migration
  from GitHub Classroom is designed to take an afternoon.

- Institutions: flagship deployments, federation pilots, and letters of
  collaboration for the NSF proposals.

- Contributors: five Apache-2.0 repositories under a DCO. The plugin
  boundaries (Git hosts, compute providers, tutoring domains) are
  intended entry points.

## 9. Availability and citation

This white paper is maintained as a Markdown document in the EduCloud
organization on GitHub (github.com/EduCloud-Ecosystem), where it
versions alongside the code it describes. Tagged releases are archived
on Zenodo under a DOI so the document can be cited in grant materials
and publications; the DOI is added at the v1.0 tag. The text is licensed
CC BY 4.0.

**Suggested citation:** Chism, G. (2026). EduCloud: An Open Platform for
Teaching with Code (white paper, v0.9.3). EduCloud Ecosystem. Zenodo DOI
pending.

**Contact: Greg Chism · gchism94@gmail.com ·
github.com/EduCloud-Ecosystem**

*Prior working names appear in older documents: Quad (Cairn), Sol
(Belay), the EduCloud Registry / “HOST” (Waypoint), Commons /
claude-lanes (Portage).*
