# CW-02 — Decision session record

*2026-07-28. Run at high effort against the CW-01 orientation report
(`portage-handoff/reports/CW01-orientation.md`). Four items were genuinely
contested and were decided interactively; everything else resolves from
documents already authored, with the trace recorded here. The edit pass
(CW-03) is authored against this memo.*

---

## 1. Amended authority order

CW-01 finding 9 showed the old authority order was self-contradicting: it named
specs 10/11 canonical for tier numbering while the current decisions
contradicted their content. Amended order, effective now:

1. **This memo**, then `lineP-roadmap.md` rev 2, then the CW-01 drift
   register's "current decision" column — which is recognized as a decision
   record, not merely a search list.
2. `portage-scale1-pilot-reconciled.md`, **except** its §2 ladder (superseded
   by §3 below) and its §5 subscription wording (clarified in §5.11 below).
3. Specs 10 and 11 — canonical again **only after** the CW-03 edit pass
   rewrites their ladder and alias sections to match §3.
4. Everything else in the repo, suspect until confirmed.

---

## 2. The four session decisions

### 2.1 The ladder: dormant-slot synthesis (resolves B2, B3, B4)

The register fixes three constraints — Groq at T3, `local_burst` collapses,
Together deferred — and exactly one shape satisfies all three at once: keep the
T0–T7 numbering, make the freed slots dormant rather than deleted. Dormant
slots are already specs/11's config idiom (`local_large: enabled: auto`).
Full table in §3.

Consequences: `local_burst` disappears as a tier; the MacBook becomes a second
health-checked deployment of `local_fast` (a sleeping laptop is a deployment
property — `unavailable` — not a tier event). Together's slot survives as
schema with `enabled: false` and a written re-enable trigger. The freed T2
takes `local_large`, pre-reserving the 128GB-node slot the hardware docs and
lineP S5 both anticipate.

### 2.2 `commons_tier` → `portage_tier`: rename now, gated (B1)

One isolated commit in the CW-03 naming series (with A7's prose rename), 14
config sites + 1 test. Gate: `tests/test_litellm_readiness.py` green **plus one
live proxy boot** asserting non-empty `/model/info` with 12 deployments — the
exact healthy-but-empty signature KNOWN_GOOD_VERSIONS documents from the last
time this key was wrong. Rationale: the engine is public under the Portage
name; this is the cheapest moment the rename will ever be.

### 2.3 Verifier contract: standalone Apache repo `EduCloud-Ecosystem/verifier-contract`

SPEC.md, both JSON schemas, the reason-code registry, and the conformance suite
— Apache-2.0 throughout, boring name on purpose. Both consumers (Portage
`failup.py`, Python; Cairn grader, Go) depend on it as an external, which
structurally forces the wire-format discipline and is the strongest form of the
PESOSE "portable standard, two consumers, two languages" claim.

CC-P1 is re-pathed accordingly (CC-P1 v2, to be authored): Step 1 targets the
new repo; Step 2's LeakOracle port runs in `~/dev/belay` against a sibling
checkout; consumers vendor the conformance runner. The "EduCloud repository
root" it assumed does not exist and is no longer needed.

### 2.4 Retirements: delete code, banner specs (B8, B12)

Delete in CW-03: `scripts/scheduler.py`, `herdr/lanes.sh`,
`.claude/tiers.claude.json`. Git history is the archive, per MANIFEST's own
norm. `specs/04` gets a HISTORICAL banner like specs/03 — its reset mechanics
still feed the Parity Bench subscription-baseline cost accounting.
`scripts/distill.py` is **not** deleted: it stays as parked HB-4 code with a
header note (the build plan believed it unwritten; it exists and needs the
collapse guards added).

---

## 3. The canonical Scale-1 ladder

```
T0  deterministic       rules, sensitivity pins, triage, acceptance discovery
T1  local_fast          ONE capability rung, TWO deployments:
                        iMac (warm steward) + MacBook (dynamic; absence logs
                        `unavailable`, never `not_good_enough`)
T2  local_large         DORMANT — future 128GB node (Strix Halo personal /
                        DGX Spark grant), enabled: auto on the hardware-case
                        dashboard trigger
T3  remote_open_fast    Groq — pinned model IDs, per-model compatibility record
T4  remote_open_broad   OpenRouter — open-weight allowlist + ZDR, no auto-router
T5  remote_open_direct  DORMANT — Together; defined, disabled; re-enable
                        trigger: OpenRouter unavailability in telemetry
T6  proprietary         rescue only — verified open failure + budget envelope
                        + logged reason + confirm gate ($10/30d, no fallbacks)
T7  ceiling_stall       terminal state, not a routable rung; produces the
                        stall artifact (attempted tiers + verifier evidence)
```

- **T-numbers are labels, not code.** `routing_order` is an ordered list
  (scale-mapping §3.3 assertion lands in Phase 1); the EduCloud profile
  inserts `institutional_sovereign` between T2 and T3 as a config entry with
  no renumbering. The personal ladder carries no sovereign rung (JS2
  work-only rule).
- **Failure taxonomy unchanged:** five classes per pilot-reconciled §4,
  implemented at S1/HB-2.
- **Provider caps** (pilot-reconciled §5) unchanged, with the Together line
  dormant alongside its tier.

**The seven capability aliases** (register #7, scale-mapping §4.3) and their
default tier mapping — every alias is a benchmark cell:

| Alias | Default tier |
|---|---|
| `classifier` | T1 |
| `code_small` | T1 |
| `code_large` | T3/T4, bench-assigned |
| `research_synthesis` | T4 |
| `embedding` | T1 |
| `proprietary_code` | T6 |
| `proprietary_research` | T6 |

The `local/*` alias namespace (specs/10:169–175, specs/11:151–156) and the
nine/twelve lists are retired by the CW-03 rewrite. `code_medium`, `vision`,
`reranker` earn cells when telemetry shows a routing decision that needs them —
Gemma 4 E4B's native vision is registry metadata until then.

---

## 4. Resolved by existing record (no new judgment required)

| Item | Decision | Trace |
|---|---|---|
| B5 aliases | Seven, as above | register #7; scale-mapping §4.3 |
| B6 tiers files | Deployment config. Leave as-is (marked deprecated-pending) until HB-0 regenerates them from the registry; they move to `portage-local` at CC-P0 v2, sanitized examples stay in the engine | MANIFEST destinations; build-plan standing rule "config is rendered, never hand-edited" |
| B7 roster pins | Documentation says the standing three (Qwen3-Coder 7B, Gemma 4 E4B, embedder) now, via the lineP rev 2 swap. **Runtime pins change only when HB-0 pulls the models and passes the per-model tool-call smoke test.** Pinning uninstalled models is what produced the current KGV state; not repeating that | KGV's own verification discipline; build-plan pitfall #1 gate |
| B9 plan.py + specs/01 | Engine code, stays; added to the CC-P0 v2 destination list (its omission was an oversight — it is a core contribution per PROJECT.md and the landscape survey). HB-2 authoring notes that failup and plan both consume the verifier contract | boundary test in lineP rev 2 |
| B10 umbrella moves | EDUCLOUD-BRIEF.md, specs/05, specs/08 Scale-2/3 move to `~/dev/educloud` **at CC-P0 v2**, not piecemeal now; CW-03 adds "moves at CC-P0" banners. The umbrella is now under git, so the destination exists | MANIFEST; reconciliation log 2026-07-28 |
| B11 phase numbering | **S0–S5 is canonical.** REVISION-PLAN's own header names LINE-P the plan of record. CW-03 adds one mapping table (S0 ⊃ CC-P0 v2 + HB-0 + HB-1; S1 ⊃ HB-2 + contract consumption; S2 ⊃ HB-3; S3 = calibration; S4 ⊃ HB-4; PLATFORM Phases 7–10 → post-S5 / Line E) and retires KICKOFF-PROMPT with a banner | REVISION-PLAN:3–5 |
| D2 Herdr naming | "Herdr" names the policy brain (classify, adapt, budget, capability selection, verification state); `herdr-meters` is its seed implementation; the multiplexer is a surface. CW-03 adds this definition where PLATFORM introduces the stack | pilot-reconciled §1 |
| D4, D14–D17 | Five-class taxonomy, contract consumption, `personal_sensitive`/`regulated` enum, task-record labels, two-retry cap — all S1/HB-2 implementation, none touched in CW-03 | lineP rev 2 S1 |
| D12 runtime policy | `OLLAMA_MAX_LOADED_MODELS=1` both machines, keep-alive pinned iMac only, `launchctl setenv`. Lands in docs via the lineP swap; `local-serve.sh` rewritten to single-model in CW-03; final pins at HB-0 | lineP rev 2 |
| Subscriptions | **No real conflict.** Max: cancelled, done (all three documents agree once read closely). Pro-tier arms (Claude Pro, Perplexity Education Pro, ChatGPT Plus) ride through the S3 staged cutover — each cancellation dated, evidence attached, reversible one cycle. CW-03 reconciles pilot-reconciled §5's wording; `tiers.claude.json` deletion covered by §2.4 | lineP rev 2 S3; REVISION-PLAN:8–10 |
| Kimi K3 re-check | Overdue since July 27. Becomes a dated KGV watch item in CW-03 and a registry step in the HB-0 prompt | build plan; lineP rev 2 |
| CC-P2 re-path | Its `modules/` premise is moot and its repo-wide scope now spans five repos + umbrella. CC-P2 v2 is authored after CC-P0 v2, per-repo, with the root manifest convention replaced by per-repo manifests + an umbrella index | CW-01 §7.5 |

## Deliberately still open

- **Placement of `portage-scale-mapping.md` in `educloud/docs/strategy/`** —
  now unblocked by §2.1; CW-03 places it with a one-line banner noting §4.1/§4.2
  are realized as dormant slots.
- **The 429/budget enforcement gap** (no budget blocks in any LiteLLM config) —
  HB-2 work, flagged so it is not mistaken for done.
- **Belay org transfer, waypoint GitHub rename, educloud repo creation, pushes**
  — user actions from the reconciliation log, still pending.

---

## 5. The Portage↔Outfitter seam

**Decision: producer owns the schema.** The endpoint manifest — what Outfitter
emits about provisioned inference capacity, what Portage's registry render
consumes — is authored as `outfitter/specs/07-endpoint-manifest.md` (normative),
with pointer rows in `educloud/SYSTEM.md` §4 (Shared contracts) and in
Portage's registry spec when HB-0 creates it. Authored when sovereign wiring
approaches (post-August-28); nothing in S0–S1 blocks on it. The manual
`SOVEREIGN_TOKEN` deployments remain the acceptable stand-in.

Shape sketch (to be refined in the spec):

```yaml
endpoints:
  - id: js2-vllm-1
    base_url: ...            # OpenAI-compatible
    api: openai-chat
    models: [gpt-oss-120b]   # pinned IDs
    health: healthy|degraded|unavailable
    allocation: {unit: SU, remaining: 1240, ceiling: 2000}
    lifetime: {expires: <ts>, teardown: guaranteed}
    policy_tags: [sovereign, research-only]
```

Invariants carried over: no endpoint without a ceiling, a lifetime, and a
teardown path (Outfitter specs/03); sensitivity remains enforced by config
absence on Portage's side — the manifest never overrides a workspace pin.

---

## 6. CW-03 edit-pass work list (authored against this memo)

Ordered; each numbered group is one commit series in `~/dev/portage` unless
noted.

1. **Naming.** A7 prose (`PLATFORM.md:1,130`, `README.md:1`,
   `pyproject.toml:2` → `portage-control-plane`) + §2.2 `commons_tier` →
   `portage_tier` (14 sites + test), gated by readiness test + live proxy boot.
2. **CCR past-tense.** `specs/00:18`, `CLAUDE.md:21–22`,
   `docs/setup-two-lane.md:17,32` (A8).
3. **LINE-P-ROADMAP → rev 2** from the project (A9); resolves D11 docs, D12
   policy, D13, D17 statement.
4. **Ladder rewrite** to §3: `PLATFORM.md` §2–3, `REVISION-PLAN.md` §3,
   `specs/02` ladder, `specs/08` Scale-1 table, `specs/10`/`11` tier and alias
   sections (seven aliases; Groq section added; Together and local_burst
   sections rewritten as dormant-slot / deployment notes).
5. **Retirements** per §2.4 + `distill.py` parked header.
6. **Banners.** specs/05, specs/08 Scale-2/3, EDUCLOUD-BRIEF ("moves at
   CC-P0"); Herdr definition paragraph (D2); phase-numbering mapping table +
   KICKOFF-PROMPT retirement banner (B11).
7. **Mechanical fixes.** CI workflow rename (A10); Kimi K3 watch item (A11);
   `ollama/` → `ollama_chat/` six lines + readiness test rerun (A12);
   `local-serve.sh` single-model runtime policy.
8. **educloud:** place `portage-scale-mapping.md` in `docs/strategy/` with the
   dormant-slot banner; add the SYSTEM.md §4 pointer row for the endpoint
   manifest (stub).

Then, in order: **CC-P0 v2** (the split, with plan.py added to destinations and
the `verifier-contract` repo in the org plan) → **HB-0** (gateway, registry,
real model pulls, pins verified) → **CC-P1 v2** (re-pathed per §2.3) → HB-1,
HB-2 (S1), CC-P2 v2.

Execution guidance: CW-03 groups 1–8 are Sonnet-at-medium work with one
exception — group 4 (the ladder rewrite) should be reviewed at the gate by the
top model, since it is the substrate every later prompt reads.
