# Portage — Scale 1 to EduCloud: the mapping, improvements, simplifications

> **Placement note (2026-07-28, CW02-decisions.md).** §4.1 (defer Together) and
> §4.2 (collapse local_burst) conflicted with the pilot-reconciled ladder; the
> conflict is resolved by the dormant-slot synthesis in CW02 §3 — both
> simplifications are adopted, realized as *dormant tier slots* (T5 Together
> disabled with a re-enable trigger; T2 freed for local_large) rather than
> deletions, so the T0–T7 numbering and the Groq-at-T3 decision both hold.

*July 2026. Verifies that the personal pilot expands to EduCloud by
configuration rather than rebuild, and records the changes that make that true.*

---

## 1. The test

At each scale step, everything should change by config and nothing by code.
Anywhere that fails is a defect in the pilot now, while it is cheap to fix.

| Scale | Deployment | Identity | Default mode | Ladder change |
|---|---|---|---|---|
| 1, personal | iMac + MacBook | none | hybrid | as piloted |
| 2, course | Waypoint host, Fall 2026 | Cairn sessions, OIDC seam | sovereign for student lanes | insert institutional_sovereign |
| 3, institutional | Coolify multi-tenant | Keycloak via Waypoint | sovereign default | same ladder, more deployments |
| 4, federation | cross-institution | CILogon federation | per-site policy | per-site provider registries |

What must survive every step unchanged: the Herdr and LiteLLM separation, the
five-class failure taxonomy, the verifier contract, the metric names, and the
policy-mode vocabulary. Those are the platform contracts. The pilot is their
first running instance.

---

## 2. What already maps cleanly

- **Separation of responsibilities.** Herdr owns policy, LiteLLM owns
  transport, verifiers own truth, measure.py owns cost. Scales without change.
- **The failure taxonomy.** `unavailable`, `not_good_enough`, `policy_blocked`,
  `invalid_task`, `ceiling_stall` serve Cairn grading and Belay tutoring as
  well as they serve routing. Adopt platform-wide.
- **Budget envelopes.** The no-provisioning-without-ceiling rule is Outfitter's
  invariant applied to tokens. Same philosophy, same schema.
- **The two regimes.** Interactive against routed generalizes directly: at
  course scale, instructors choose their interactive tools, and every
  student-facing lane is routed regime under sovereign mode.
- **The stall artifact.** A ceiling stall that surfaces evidence instead of
  fabricating an answer is exactly the behavior a graded setting requires.

---

## 3. Improvements

**3.1 failup.py consumes verifiers through the CC-P1 contract.**
The report gives failup.py its own pass or fail interface. Left alone, that
respecifies the mechanism the verifier contract unified. Change the boundary:
failup.py invokes verifier executables per the wire format, reads verdict
documents, and branches on reason codes. The pilot then becomes the contract's
second consumer and proves portability before Cairn's Go implementation. That
is running evidence for the PESOSE standard claim, produced as a side effect of
the pilot.
*Cost: one boundary change in Phase 1. Gate: the conformance runner passes
against the pilot's verifiers.*

**3.2 Align the policy-mode vocabulary.**
The report coins `hybrid_open_first`. The platform vocabulary is `sovereign`,
`open_weight_only`, `hybrid`, and open-first ordering is already encoded in
`routing_order`, so the fourth name adds nothing and forks the spec. Rename to
`hybrid`. The pilot's sensitive configuration is `sovereign` at personal scale,
enforced by absence, same as a student lane.
*Cost: a rename in one file.*

**3.3 Tiers are pure config.**
The personal ladder correctly lacks an institutional tier under the JS2
work-only rule. The EduCloud profile must be the same engine with
`institutional_sovereign` inserted between local and remote-open by editing
`routing_order` and the provider registry. Verify nothing in Herdr hardcodes
tier semantics beyond the ordered list.
*Cost: a Phase 1 assertion, not a feature.*

**3.4 The task record carries the attribution vocabulary.**
Add optional opaque `{course, assignment, student}` label fields to the task
record now, empty at Scale 1. Classroom telemetry then aggregates with zero
schema migration, and cost, usage, and outcomes read the same way across
Cairn rosters, Outfitter's ledger, and Portage's spend logs.
*Cost: three nullable fields.*

**3.5 Split sensitive into personal_sensitive and regulated.**
OpenRouter ZDR is acceptable for personal-sensitive work. It is not FERPA
compliance. `regulated` means local or sovereign only, by absence, matching the
data-destinations policy. The `data_classification` field carries the platform
enum so the pilot and the policy share one vocabulary.
*Cost: an enum change now. Retrofitting it after student data exists is a
compliance incident waiting to be written up.*

**3.6 Ship the deployment contract.**
Containerize Herdr plus LiteLLM as one Coolify-conforming compose, even while
the pilot runs bare on the iMac. The application is the contract, and the
compose is the migration path to the Waypoint host. Add the bring-your-own-OIDC
seam as a config stub pointing nowhere, so Keycloak lands later as a config
edit.
*Cost: a compose file and an empty config block.*

---

## 4. Simplifications

**4.1 Defer Together, T5.**
Three hosted-open providers is redundancy a single user never exercises, and
OpenRouter already routes to Together endpoints. Cut to Groq plus OpenRouter
for calibration. Re-add Together only if telemetry shows OpenRouter
unavailability. One fewer key, budget line, and benchmark surface.

**4.2 Collapse local_burst as a tier.**
Both Macs are 16GB running the same models, so the MacBook is a second
health-checked deployment of `local_fast`, load-balanced by LiteLLM. Tiers are
capability rungs, machines are deployments. The taxonomy still logs a sleeping
laptop as `unavailable`. The ladder loses a rung and nothing else changes.

**4.3 Seven aliases, not twelve.**
Calibrate with `classifier`, `code_small`, `code_large`, `research_synthesis`,
`embedding`, `proprietary_code`, `proprietary_research`. Every alias is a
benchmark cell, and `code_medium`, `vision`, and `reranker` earn their cells
when telemetry shows a routing decision that needs them.

**4.4 One source of truth for configuration.**
The report implies four hand-maintained files: policy, model registry, provider
registry, LiteLLM config. Generate the LiteLLM config from the registry. Herdr
reads policy plus registry, and nothing else is edited by hand. This is the
two-manifest rule applied to the router itself.

**4.5 One Perplexity surface.**
Education Pro interactive during calibration. The API stays disabled and the
science-profile routing lands with the science lane, never before it. Three
Perplexity surfaces collapse to one with a sunset date.

---

## 5. What this buys the grants

- The pilot's calibration window overlaps the Fall 2026 pilot start, so its
  dashboards, displacement metric, and stall artifacts are working evidence for
  both NSF narratives, produced before a single course deployment exists.
- The verifier contract gains a second consumer in a second language context,
  which is the portability claim demonstrated rather than asserted.
- The two 16GB Macs are the under-resourced arm of the Parity Bench equity
  factor. Scale 1 telemetry seeds that measurement at no additional cost, and
  the equity finding is the one IUSE needs.
- The regulated split plus enforcement by absence is the security and privacy
  plan's architectural core, stated once and demonstrated in the pilot.

---

## 6. Actions

1. Fold 3.1 through 3.6 into the Phase 1 Claude Code prompt as gates, not
   suggestions.
2. Apply 4.1 through 4.5 to the pilot config before Phase 2 opens.
3. Record the scale table in SYSTEM.md as the expansion contract.
4. At calibration exit, cut the Scale 2 profile as a config diff against
   Scale 1 and review that diff. If it contains code, the mapping failed and
   the defect gets fixed before the Fall deployment.
