# EduCloud — System Definition

*The canonical internal definition: module names and boundaries, shared
contracts, and the platform invariant. The white paper
(`EduCloud-White-Paper.docx` / `WHITEPAPER.md`) is the outward-facing
companion; `DOCUMENTATION.md` indexes everything; `EDUCLOUD-STATUS.md` carries
current status and priorities. Where an older document conflicts with this
one, this one wins.*

*v1.1 · July 2026 — §7 added: the two lines, the scale table (expansion
contract), and resource allocation, consolidating `LINE-P-ROADMAP.md`
(claude-lanes) and `LINE-E-ROADMAP.md` (this folder).*

## Current classroom implementation (November 2026)

The first INFO 511 classroom profile uses the notebook, authored Math Inspector and Cairn without generative AI. The optional pilot tutor is **belay-classroom**, a separate repository from original Belay.
Waypoint's classroom line includes the notebook, admission and saved-file handoff;
Cairn owns submission and grading. See [the current integration guide](docs/pilot/INTEGRATION.md)
and [central status](README.md#pilot-status). Older host/product examples below are
architecture history, not evidence of a current deployment. The [pilot protocol](docs/development/PILOT_PROTOCOL_V1.md)
is the shared development minimum. Each repository's actual LICENSE/LICENSING and
path-specific SPDX declarations govern; no blanket Apache license applies to all
components. Current public repositories and readiness are recorded in `pilot/`.

## 1. Names

Names are settled as of July 2026. Prior working names appear throughout the
June corpus and in repo paths; they map as follows.

| Current | Prior names | Repo (local) | Remote |
|---|---|---|---|
| **Cairn** | Quad | `~/dev/cairn` | `EduCloud-Ecosystem/cairn` |
| **Belay** | Sol; repo placeholder "peer-tutor-framework" | `~/dev/belay` (renamed 2026-07-28) | `EduCloud-Ecosystem/belay` |
| **Waypoint** | "HOST"; the EduCloud Registry | `~/dev/waypoint` (renamed 2026-07-28) | `EduCloud-Ecosystem/waypoint` |
| **Portage** | Commons; claude-lanes; "inference plane" | `~/dev/portage` | `EduCloud-Ecosystem/portage` |
| **Outfitter** | "compute brokering layer" | `~/dev/outfitter` | `EduCloud-Ecosystem/outfitter` |

Repo directory renames are deliberate, separate decisions; the remote names
are canonical. New documents use current names; old documents get a mapping
banner when touched, not a rewrite.

## 2. Module boundaries

Each module owns a specific problem and explicitly does not own its
neighbors'. The modules compose by deployment, not by dependency: Cairn runs
alone; everything else is additive.

- **Cairn — the classroom layer.** Owns assignments, rosters, per-student
  repositories, collection, sandboxed grading, and the instructor/student
  surfaces. Does not own where compute comes from (Outfitter), who the user is
  (Waypoint), or how AI calls are routed (Portage). The Git host is a plugin
  behind one adapter interface: GitHub, Forgejo, GitLab.
- **Belay — the peer tutor.** Owns the tutoring loop, the deterministic leak
  gate (every draft passes through the active domain's grader), the wellbeing
  floor, DomainPacks, and its license-gated knowledge corpus. Does not mint
  identity, choose models (it declares task classes; Portage routes), or see
  grades (the grades firewall is Belay policy).
- **Waypoint — publishing and federation.** Owns hosting (Coolify), identity
  (Keycloak), the tenant onboarding contract, and the registry: catalog,
  register CLI, and the federation metadata standard. Does not own course
  logic or model routing.
- **Portage — model routing.** Owns the inference ladder (local → sovereign →
  hosted open-weight → PAYG frontier), the deterministic fail-up guard, policy
  modes, budgets/meters, and the measurement harness (Parity Bench,
  displacement). Does not provision machines (Outfitter) and never stores
  student records.
- **Outfitter — compute brokering.** Owns placement of workloads onto compute
  providers (Docker, Codespaces, campus HPC, Jetstream2, Pegasus) under budget
  ceilings, with lifecycle (provision → status → teardown → reap) and
  normalized cost attribution, and staged allocation intelligence (the
  planner: provider choice, automatic swaps, pre-provisioning from system
  telemetry and the course calendar). Does not schedule inside a cluster,
  route model calls, or own identity.

## 3. The platform invariant

**No component trusts a model's — or a provider's — self-report. A
deterministic check decides success.** Cairn's sandboxed autograder, Belay's
leak gate, Portage's fail-up guard, and Outfitter's conformance tests and
budget guards are the same rule applied to grading, tutoring, routing, and
spending. Any proposed feature that asks the platform to take a model's word
for an outcome is out of contract.

## 4. Shared contracts

1. **Attribution vocabulary.** Opaque `{course, assignment, student}` labels,
   assigned by Cairn, flow unchanged through Outfitter's cost ledger,
   Portage's spend logs, and Belay's cohort measures. No module re-keys them;
   no module resolves them to identities it doesn't need.
2. **Policy modes** (defined in Portage, honored platform-wide):
   `sovereign` (local + institutional infrastructure only; no remote of any
   kind), `open_weight_only` (hosted open-weight allowed; no proprietary), and
   `hybrid` (proprietary reachable only behind the escalation boundary:
   verified open failure, documented specialist need, or explicit override).
   Student-facing lanes default to `sovereign`. Sensitivity is enforced by
   config absence — the restricted configuration contains no other providers —
   never by a runtime check and never by a provider's retention promise.
3. **Identity.** Keycloak (Waypoint) is the ecosystem OIDC provider. Every
   module keeps a bring-your-own-OIDC seam and points it at Waypoint when
   deployed together; module-local auth is a standalone-mode fallback, not the
   platform path.
4. **Deployment contract.** Every module ships a container deployable through
   Coolify; Waypoint's onboarding contract ("the application is the
   contract") and its `templates/` directory are the registry of record.
5. **Adapter discipline.** External systems sit behind per-module adapter
   interfaces (Git hosts in Cairn, compute providers in Outfitter, models
   behind capability aliases in Portage, domains as packs in Belay), each
   with a conformance test. Provider quirks live inside that provider's
   adapter only.
6. **Governance floor.** Respect each repository's actual LICENSE/LICENSING and
   path-specific exceptions, DCO sign-off, contribution guidance and the shared
   pilot implementation protocol. The current adoption inventory lives in
   `pilot/components.json`; old July file-gap lists are not current evidence.

7. **One org.** All five repos live under `EduCloud-Ecosystem`. Pending as of
   July 2026: push Portage and Outfitter (remotes set, unpushed); transfer
   Belay from the personal account; rename HOST → waypoint.
8. **Measurement discipline.** No efficiency or quality claim without a
   preregistered gate; availability failures (`unavailable`) are never scored
   as quality failures.
9. **The endpoint manifest (stub, CW02 §5).** The Portage↔Outfitter seam:
   Outfitter emits a manifest of provisioned inference capacity (endpoint id,
   OpenAI-compatible base_url, pinned model IDs, health, allocation remaining
   against a ceiling, lifetime with guaranteed teardown, policy tags);
   Portage's registry render consumes it. Normative spec:
   `outfitter/specs/07-endpoint-manifest.md` (producer owns; to be authored
   when sovereign wiring approaches, post-Aug-28). Invariants: no endpoint
   without ceiling/lifetime/teardown; the manifest never overrides a
   workspace's sensitivity pin — config absence still wins.
10. **Bounded AI management.** Models with system-level knowledge manage the
   platform's resources: Portage's steward and learning loop decide model
   routing, and Outfitter's allocation planner (its `specs/06`) decides
   compute placement, swaps, and pre-provisioning. They act only inside
   deterministic envelopes they cannot alter (budget ceilings, policy modes,
   lifetimes, append-only decision logs, confirm thresholds), and a learned
   manager is promoted or demoted by shadow scoring under the non-inferiority
   gate. Models decide allocations; deterministic systems define the limits
   and verify the outcomes.

11. **Data destinations (Axis B).** Contract 2 above governs where inference
   *payloads* may go. This one governs where *records* may live, and the two
   are deliberately not the same question: opaque attribution labels
   de-identify a payload because a model never needs a name, and do nothing
   for a store an instructor uses to grade named humans. Destination tiers,
   strongest first for education records: D1 institutional, D2
   self-stewarded, D3 shared sovereign (Jetstream2), D4 commercial cloud.
   Education records (R2) live on D1 or D2 only, absent a recorded
   authorization from the responsible administrator. Home:
   `docs/policy/data-destinations.md`; enforced by
   `docs/policy/check_destinations.py` against that document's own register.
   Module pointers: `cairn/PRIVACY.md`, `belay/PRIVACY.md`.

Resource-constrained service development follows the
[resource-efficiency record](docs/specs/resource-efficiency-v1.md): preserve a
complete AI-off task and human-help path, use reviewed materials and ordinary
deterministic tools before adding inference, and compare full task effort and
usefulness rather than token counts alone. Browser notebooks may replace hosted
work only after the exact task, packages, device, persistence, export, network
boundary and accessible hosted fallback have been accepted. Portage remains the
sole inference admission/accounting authority; any eventual retry or escalation
is a distinct bounded attempt. An approved institutional endpoint is the service
target, with external public/synthetic research routes separately qualified.
No campus API, GPU inventory, pooled personal credits or allocation is assumed.
Independent batch jobs precede fleet/model sharding; experimental distributed
inference or autonomous managers do not become a classroom dependency merely
because an offline fixture passes. The first tools prepare evidence only and
do not establish a deployed service or measured savings.

The [research workspace contract](docs/specs/research-workspace-pilot.md) applies
these boundaries to reviewed Python/R evidence and coordinated local recovery:
Waypoint owns access/artifacts, Outfitter owns finite admission and one-way
authority cutover, and Portage retains inference policy. Its
[acceptance record](docs/research/2026-10-17-research-pilot-acceptance.md) separates
the merged local baseline and P1 from untested hosted/provider gates.

The [temporary research-assessment contract](docs/specs/research-assessment.md)
extends these same authorities with upload expiry, allowlisted measurement and
cleanup receipts, deterministic resource estimates and allocation-preparation
exports. It does not reuse retained-source study bundles. Measured consumption,
reservations and provider charges are distinct; missing measurements remain
unknown. Tool adapters cannot bypass Outfitter admission or Portage policy.
Whole-service data-destination and FERPA acceptance remain required.

## 5. Dates that govern planning

- **August 28, 2026** — GitHub Classroom shutdown (final data deletion
  September 4). The pilot forcing function.
- **~January 20, 2027** — NSF IUSE: EDU, ESL Level 1 (NSF 23-510 January
  window; verify exact date). UA OSP internal ~3–5 business days prior.
- **March 2, 2027** — NSF PESOSE Track 1 (NSF 26-506). The September 1, 2026
  acceleration was abandoned; any document citing it is superseded.
- The full funding calendar lives in
  `strategy/EduCloud-funding-strategy.md` §2.

## 6. Document authority

For any question, read in this order: `SYSTEM.md` (this file — names,
boundaries, contracts) → `EDUCLOUD-STATUS.md` (current state and priorities)
→ the line roadmaps (`LINE-E-ROADMAP.md` here for the platform;
`claude-lanes/LINE-P-ROADMAP.md` for the personal stack)
→ `DOCUMENTATION.md` (index of everything) → the module's own repo docs
(authoritative for that module's internals) → the June planning corpus
(historical unless banner-corrected). The white paper is the outward-facing
statement of §§1–4 and follows this file when they diverge.

## 7. The two lines and the expansion contract

Development runs on two lines with one shared engine and deliberately
separate judgment. The plan of record is: personal MVP first, then the
EduCloud MVP, then dual full implementation as the evidence warrants.

- **Line P — personal** (`claude-lanes/LINE-P-ROADMAP.md`, stages S0–S5).
  The maintainer's full working stack on the iMac and MacBook. Line P is
  deliberately inclusive: every lane (code, science, design, cowork), the
  research stack, shared memory, the learning loop, and the 60–90 day
  calibration program. It is the proving ground, and it may run anything.
- **Line E — EduCloud** (`LINE-E-ROADMAP.md`, stages E0–E4). The platform
  deployment. Line E is deliberately narrow about AI: Portage serves four
  consumers — **instructor-facing AI**, **Belay's tutoring lane**, **the AI
  sandboxes** (grading and Outfitter-provisioned compute), and **Outfitter's
  allocation planner** (an operations lane: system telemetry only, never
  student content). Anything beyond those four stays on Line P until it earns
  admission.
- **The inclusion test** (admission to Line E): stable, auditable,
  reproducible, equitable, compliant by construction, cost-predictable.
- **The transfer rule:** Line P feeds Line E *evidence and config*, never
  code paths outside the shared engine. A component crosses as configuration
  against the shared engine or it does not cross.
- **The expansion contract:** each Line E scale is a config diff against the
  previous scale. A diff that contains code is a defect and is fixed before
  the step ships.

The scale table (carried here per Line E's standing rules):

| Scale | Deployment | Identity | Inference posture |
|---|---|---|---|
| MVP (E0) | one Waypoint host | Cairn sessions; OIDC seam stubbed | sovereign default; JS2 tier inserted |
| Pilot (E1) | one host, real course | same | same, measured |
| Institutional (E3) | Coolify multi-tenant | Keycloak | sovereign default; hybrid by instructor policy |
| Federated (E4) | cross-institution | CILogon | per-site provider registries |

Resource allocation across the lines:

| Resource | Line P | Line E |
|---|---|---|
| Effort | Personal time: 10% baseline, ~20% surge through August; S3 calibration runs on daily use, not extra hours | E0 owns the build surge now (the dependency spine starts at the August deadline); grant-funded effort after IUSE / Track 1 |
| Compute | iMac + MacBook; hosted-open steady state $20–45/mo; proprietary rescue capped at $10/30 days, confirm-gated | Waypoint host (DigitalOcean); Jetstream2 under the ACCESS Discover allocation; course compute brokered by Outfitter under budget ceilings |
| Hardware trigger | 128 GB-class node only if the dashboard's hardware case fires: Strix Halo class, personal money | DGX Spark class, grant money, on the same evidence rule — the dashboard decides, not appetite |
| Subscriptions | None fixed after S4; during S3 calibration only, Pro-tier comparison arms (Claude Pro, Perplexity Education Pro) inside a $60–80 envelope, $100 ceiling | None; sovereign-first by construction; hybrid exists only as instructor policy at institutional scale |
| Model spend | Personal envelope, three-price accounting | Per-course budgets through the attribution labels; student lanes carry no proprietary path at all |

Cross-line commitments already scheduled: the Portage **EduCloud profile is
an E0 deliverable** — a reviewed config diff against Line P's Scale 1 that
inserts `institutional_sovereign` (Jetstream2 vLLM) into the routing order,
sets student lanes sovereign by absence, and carries the attribution labels
and the `regulated` classification. The Parity Bench's **resource-tier
factor** is seeded by Line P's two-Mac under-resourced arm, which is what
turns the equity claim in the IUSE narrative into a measured number. The
**CC-P1 verifier contract** is the portable standard PESOSE carries, with
consumers in two languages (Portage's guard in Python; the grading gate in
Go). The HB-0…HB-4 build prompts and the CC-P1 contract text are authored
but **not yet in-repo** — landing them in `claude-lanes/` is an S0
prerequisite.
