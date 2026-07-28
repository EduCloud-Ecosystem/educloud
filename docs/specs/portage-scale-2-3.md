# Portage — Scale 2 and Scale 3

> *Placed here at CC-P0 v2 (2026-07-28), extracted from `~/dev/portage/docs/specs/08-scale-tiers.md`'s Scale-2/3 sections per that file's own banner and CW02-decisions.md §4. Scale 1 remains in the engine repo (`docs/specs/08-scale-tiers.md`); the scale-invariance rule (same custom core at every scale) holds across all three and is stated there.*

## Scale 2 — + HPC (Jetstream2)

Everything in Scale 1, plus the **sovereign tier** made real. It already occupies
its slot between free-local and hosted-open (`institutional_sovereign`,
inserted between T2 and T3 in the EduCloud profile — CW02-decisions §3); at
Scale 1 it is simply empty. `local → sovereign HPC (free, no quota draw) →
hosted open → proprietary PAYG`.

- **Custom Jetstream2 adapter** (the report confirms nothing turnkey exists:
  STREAM is a June-2026 paper without a confirmed public repo; FIRST is real
  and production — ~35 models behind an OpenAI-compliant gateway at ALCF — but
  gated to DOE accounts, not NSF ACCESS). Borrow both designs: Globus
  Auth/Compute for control plane, OpenAI-compatible exposure, and STREAM's
  dual-channel firewall traversal pattern if off-instance access is needed. In
  EduCloud, **Outfitter owns provisioning/reaping of these nodes**; Portage
  consumes the endpoints Outfitter reports healthy.
- **Deployment mode first, adapter second:** Jetstream2's inference API is
  network-gated, so the zero-adapter path is running Lane B *on* a JS2 VM
  where the endpoint is native — a LiteLLM deployment entry and nothing else.
  Build the external adapter only when off-instance access is confirmed live.
- **Data pin unchanged and non-negotiable:** JS2 is sovereign, *not private*
  (shared infra, admin-visible, research-use-only). Sensitive lanes keep
  `policy_mode: sovereign` (local-only); the sovereign HPC tier is absent by
  construction there.
- Watch item (from the report): Globus-based DOE↔NSF federation could make
  FIRST-style service reachable to ACCESS users "without warning" — recheck
  quarterly; it would replace most of the custom adapter.

## Scale 3 — Full EduCloud (federated, multi-user, published)

Everything in Scale 2, with the pool widened and the heavy backends now earning
their weight:

- **Federation = LiteLLM deployments**, nothing more: multiple sovereign
  endpoints (JS2 + campus HPC + any ACCESS resource) as same-`model_name`
  deployments with `order` = free-before-allocation and native cooldowns.
  The deleted custom broker stays deleted. Per-course virtual keys are the
  course-level meter; Keycloak (Waypoint) fronts authn.
- **Adopt vLLM Semantic Router as the classification backend** (Apache-2.0,
  4.3k stars, weekly releases; ModernBERT intent classification, session-aware
  routing, PII detection that *complements* — never replaces — the
  deterministic sensitive pin). The custom wrapper survives on top: the report
  is explicit that clarify-before-dispatch and pre-model override hooks are
  not in its feature set.
- **Adopt Langfuse as the trace/score store**; the stall-gated efficiency
  metric and `proprietary_displacement` remain custom scores/aggregations on
  its exported traces (~50–100 lines instead of a bespoke logging backend).
  Mind unit-based pricing at institutional volume.
- **Adopt OpenSpec's `changes/` + GIVEN/WHEN/THEN schema** for plans (required
  here for community compatibility); keep the custom runnable-check executor
  and human gate — the report found no SDD tool that makes runnable
  per-subtask acceptance commands a first-class object.
- **Publish:** herdr-meters to the plugin marketplace (confirmed gap), and the
  guard + measurement method + meter-sovereign fusion as the release/paper.
  Novelty verified current: neither 9Router nor OmniRoute (v3.0.0, 67+
  providers) has an institutional tier — both remain commercial-subscription
  arbitrage. The per-lane `proprietary_displacement` measured during pilot terms
  is the evidence base for the "public infrastructure, no proprietary
  dependency" claim in PESOSE/IUSE materials.
