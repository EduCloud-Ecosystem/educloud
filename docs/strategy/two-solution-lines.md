# Two solution lines — Personal and EduCloud

*July 2026. The personal line is a preference-driven, fully open deployment.
The EduCloud line is what an education infrastructure should ship. They share
one engine and one verifier contract. They share nothing else by default.*

---

# Line P — Personal, fully open

**Policy mode: `open_weight_only`.** All subscriptions cancelled. Proprietary
adapters remain installed, disabled, with a $0 soft cap. One flag to set:
either pure open (rescue off, ceiling stalls surface evidence) or a $10
hard-capped PAYG rescue line for the rare frontier save. Zero subscriptions
either way.

## Interfaces

| Replaces | Tool | Notes |
|---|---|---|
| Claude Code | Aider | terminal, git-native auto-commit, prompt caching |
| Claude Cowork | OpenHands | Docker workspace, Lane B automation on the iMac |
| Claude chat + Perplexity | Open WebUI | chat, RAG, web search via SearXNG toggle |

OpenCode stays optional as a second terminal harness. All three point at
LiteLLM behind Herdr, so the ladder is invisible to every surface.

## The ladder, corrected

Local first. The pasted plan routed everything to OpenRouter, which abandons
the free tier and the routing brain. Restored here.

| Rung | Model | Where | Cost | Role |
|---|---|---|---|---|
| Steward | Qwen3-Coder 7B Q4, warm | iMac + MacBook | $0 | triage, routing, routine work, ~45% of tasks |
| Bulk | DeepSeek V4 Flash | OpenRouter | $0.14 / $0.28 | everyday overflow, summaries, standard coding |
| Cached edits | Kimi K2.7 Code | OpenRouter | ~$0.95 in, ~$0.19 cached, ~$4 out | rapid high-frequency terminal loops |
| Workhorse | GLM-5.2 | OpenRouter | ~$0.45 / $3.31 | hard agentic coding, architecture, the ceiling |
| Rescue, optional | Anthropic or OpenAI PAYG | disabled by default | $10 hard cap | only on verified open failure, logged |

Corrections against the pasted plan: DeepSeek-R1 is the January 2025 model,
superseded by the V4 line and slow for agent loops; V4 Flash is newer and four
times cheaper. Llama 3.3 is December 2024 and loses to the free local steward
for its whole role. GLM-5.2 was missing and is the strongest open agentic
coder. Kimi K3 weights land July 27; re-check the cached-edits pin that week.

## Spend

$20 to $45 a month, matching prior modeling, bounded by usage with no caps.
Down from $140. Provider hard limits stay in herdr-meters: OpenRouter $35,
Groq $20, rescue $10 or $0.

## The trade, stated

No frontier rescue in pure mode. The hardest tier fails to a ceiling stall
with attempted tiers and verifier evidence, and you decide by hand. That is
the cost of full openness, and the stall artifact makes it a visible cost
rather than a silent one.

---

# Line E — EduCloud, education infrastructure

**Principle: ship plug points, never vendor picks.** The platform carries
adapters and policy. Each institution plugs its own sources: local nodes,
campus HPC, Jetstream2 and ACCESS, hosted open providers, or a commercial
contract where procurement allows one. Any source remains pluggable. The
platform never requires a consumer account from a student.

## The inclusion test

A component belongs in EduCloud only if it is:

1. **Stable.** Pinned versions, tested rollback, survives upstream drift.
2. **Auditable.** The institution can inspect where inference ran and why.
3. **Reproducible.** Version-pinned open weights, so a 2026 study re-runs in
   2029 and means something.
4. **Equitable.** Works at community-college resourcing, measured by the
   Parity Bench resource-tier factor, never assumed.
5. **Compliant by construction.** Student lanes run sovereign, enforced by
   absence. ZDR is a personal-grade control and never the FERPA answer.
6. **Cost-predictable.** Allocated or flat compute over metered spend, with
   budget ceilings on everything that meters.

## Defaults the platform ships

- Policy modes `sovereign`, `open_weight_only`, `hybrid`, with student-facing
  lanes defaulting sovereign.
- The verifier contract and conformance suite.
- A vetted starter registry: pinned open-weight models with license and
  provenance recorded, a warm small model meeting the tutoring latency floor,
  and an institutional-inference workhorse class.
- Provider adapters as the plug points: Ollama-class local, vLLM on campus
  HPC, Jetstream2 inference, hosted open APIs, commercial APIs behind policy.
- The data-destinations policy with the `regulated` classification and the
  sensitive-config CI check.
- Budget envelopes and the stall artifact, since a graded setting must never
  receive a fabricated success.

## Excluded from EduCloud, by design

These live in Line P and stay there:

- Consumer subscription quota arbitrage and consumer quota meters.
- Price-chasing across hosted providers week to week.
- Unpinned bleeding-edge model adoption.
- Personal ZDR routing as a sensitivity answer.
- Any component whose maintenance story is one person's attention.

## Why the lines stay separate

Line P optimizes for cost and autonomy under one user's judgment, and it can
absorb risk by hand at a ceiling stall. Line E optimizes for durability,
audit, and equity across institutions, and nobody is standing by to absorb
risk by hand in a graded course at scale. The engine is shared. The judgment
is not, and keeping the lines distinct is what lets each be good at its job.

---

## Actions

1. Flip Line P to `open_weight_only`, set the rescue flag, cancel the
   remaining subscriptions, and update the pins per the corrected ladder.
2. Encode Line P in the Phase 1 Claude Code prompt as the pilot
   configuration.
3. Record the inclusion test in SYSTEM.md as the EduCloud admission rule for
   models and providers.
4. Keep the Scale 2 config-diff test from the mapping doc. Line E is that
   diff, and it must stay code-free.
