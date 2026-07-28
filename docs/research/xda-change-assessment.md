# Change-Assessment Report: XDA Local-LLM Articles vs. the Herdr Routing Stack

> Saved from chat per MANIFEST.md; canonical staging name `xda-change-assessment.md`.
> Source of the Gemma 4 E4B roster decision, the two-retry cap, and the Ollama
> runtime policy carried into Line P rev 2.

## TL;DR
- **Adopt two things, trial three, reject one.** The articles validate your core architecture (few models, deterministic routing, local-first with cloud rescue) rather than overturning it. The clearest wins are (a) adding **Gemma 4 E4B** as the MacBook offline generalist/vision model and (b) borrowing the first article's **per-specialist tool-scoping + two-retry cap** discipline into Herdr/OpenHands — both are process/config changes, not a model zoo.
- **Do NOT convert your one-warm-steward design into a multi-warm specialist swarm on 16GB.** On a 16GB unified-memory Mac, keeping one 7B warm (~5.5GB resident) is comfortable; keeping a 7B + 4B both resident (~9–10GB) is tight and risks macOS swap/jetsam kills. Each model swap costs a ~3–8s cold start. Your standing rule holds.
- **A small local thinking model (DeepSeek-R1-Distill or Gemma 4 thinking mode) is worth a TRIAL as a distinct planner/decomposer capability — but gated, not always-on.** Thinking tokens are expensive on Apple Silicon (reasoning traces balloon — DeepSeek's own R1 update grew average chains from 12,000 to 23,000 tokens), so use it only for the fail-up guard's harder local retries and Herdr's decomposition stage, with a thinking-token budget cap.

## Key Findings
- **Article 1 (tiny specialists)** describes a deterministic n8n + Ollama pipeline with a five-role division of labor: a 2B-class router (Qwen 3.5 2B, ~2.7GB, temp 0, JSON-only), a coder (Qwen 2.5 Coder 7B Q4, 4.7GB), three prompt-differentiated Qwen 3.5 9B workers (research/data/automation, ~6.6GB), and a Qwen 3.5 4B verifier — with tool-scoping per role and a two-retry cap. This is architecturally almost identical to your Herdr design, just executed with more models on presumably larger hardware.
- **Article 2 (thinking model)** recommends **DeepSeek R1 Distill Llama 8B** as an *additive* specialist for reasoning-heavy work (heuristic evaluation, root-cause analysis), explicitly NOT replacing Qwen/Gemma. Tooling is LM Studio; the value proposition is the visible chain-of-thought, not raw capability.
- **Article 3 (Gemma 4)** makes the case for **Gemma 4 E4B** on a 16GB laptop: 8B total / 4.5B active via Per-Layer Embeddings, ~5GB at Q4, 128K context, native vision, native function calling, configurable thinking. It's positioned as a $0 offline generalist + vision/OCR + "second brain" over Obsidian via Ollama.
- **Corroborating XDA pieces** ("stopped obsessing over parameter count," "2B handles 90%," "one pulled ahead") converge on: pick by tool-calling (BFCLv3) and instruction-following (IFEval), not parameter count; Gemma 4 E4B wins vision/tone, Qwen wins reasoning/coding/function-calling; route with something tiny, execute with something purpose-built, escalate to a generalist only when reasoning is truly needed.
- **Hardware reality (subagent-confirmed):** Per the Ollama FAQ/API docs (v0.1.23 release notes), "If not set, the model will stay loaded for 5 minutes by default… If set to a negative duration (e.g. -1), the model will stay loaded indefinitely… If set to 0, the model will be unloaded immediately once finished." Cold-start for a ~4.7GB Q4 model on a 16GB M-series is ~3–8s (best hands-on datapoint: 3–5s for an 8B on an M2/16GB). A 16GB Mac comfortably fits ~one 7B warm; two small models resident is possible but near the memory-pressure edge.

## Details

### Article 1 — "I replaced Claude Code with a team of tiny specialists" (Anurag Singh, Jul 24 2026)
**Models & quant (verbatim from article):**
- Router: **Qwen 3.5 2B**, ~2.7GB, large context, temperature 0, forced JSON output (task type, inputs, tools, specialist, success criteria). Does not solve tasks.
- Coder: **Qwen 2.5 Coder 7B Q4**, 4.7GB, larger context, temp 0.1, scoped to project dir + file-edit tools + sandboxed terminal only.
- Workers: three **Qwen 3.5 9B** instances (~6.6GB, same weights, different prompts/tools), temp 0.2 — research (search/fetch), data (Python/SQL executed by n8n), automation (approved n8n nodes only).
- Verifier: **Qwen 3.5 4B** — checks output against success criteria (tests pass, sources present, calculations match).

**Tooling:** n8n (workflow/orchestration, visible execution log) + Ollama (local API). Deliberately "boring"/observable rather than an opaque agent framework.

**Workflow structure:** deterministic route → execute → verify → on failure return structured error JSON to only the relevant specialist, **capped at two retries**. Key insight: failures are *contained* to one workflow stage, so a broken coder change re-runs only the coder, not the whole plan.

**Claimed benefits:** near-zero cost, no token guzzling, full observability, contained failures. **Pitfalls the author reports:** each model individually is worse than Claude; Claude is still better for open-ended "plan the whole project" requests. No hardware spec or latency numbers are given (a top comment on the article explicitly asks "What is your PC setup?").

**Assessment vs. your stack:** This is *your architecture already* — Herdr's deterministic tier ladder, the fail-up guard, the five-class failure taxonomy, and per-tier logging are a more rigorous version of the same idea. The novel, adoptable pieces are (1) **per-specialist tool-scoping as a hard constraint** (research worker can't touch files; automation worker can't invent shell commands) and (2) the **two-retry hard cap** to prevent expensive loops. Both map onto OpenHands tool permissions and Herdr retry policy.

### Article 2 — "I stopped using Qwen and Gemma after finding a local LLM that thinks" (Nolen Jonker, Jul 24 2026)
**Model:** **DeepSeek R1 Distill Llama 8B** (chosen over the Qwen-based distill because Llama 8B has the edge on code-heavy benchmarks; Qwen 7B distill leads on math/general reasoning). Runs in **LM Studio** with GPU offload. Per the official DeepSeek-R1 model card/GitHub repo, "we fine-tuned several dense models… We open-source distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series," with the Qwen distills "finetuned with 800k samples curated with DeepSeek-R1" (Qwen2.5 base for the 1.5/7/14/32B variants; Llama-3.1-8B-Base and Llama3.3-70B-Instruct for the 8B and 70B).
**Workflow:** additive specialist — "not getting uninstalled," Qwen and Gemma still do daily work; the distill handles reasoning-heavy tasks where "watching the reasoning matters as much as the answer" (Nielsen heuristic UX evaluation, finding one root cause across three complaints).
**Benefits:** trustworthy visible reasoning; rules out weaker answers first. **Pitfalls:** the author notes the thinking block "ran long… though I'm still not sure if that's thorough or just excessive for such a simple riddle" — i.e., **overthinking**. Independent sources confirm R1-style models overthink trivial tasks (a 2+3 problem can consume ~900 tokens) and can bleed thinking into structured output (disable thinking for JSON extraction); the DeepSeek R1 0528 update itself documented average reasoning-chain length growing from 12,000 to 23,000 tokens on the full model, illustrating how quickly reasoning traces expand.
**Apple Silicon latency:** an R1-Distill-7B on an M2/16GB delivers ~25–40 tok/s; reasoning models are throughput-sensitive because they emit many more tokens — keep the largest distill only if it stays above ~10 tok/s.

### Article 3 — "Gemma 4 is lightweight, runs on my 16GB laptop, costs $0" (Abhinav Raj, Jul 24 2026)
**Model:** **Gemma 4 E4B** — "E" = effective; 8B total parameters, ~4.5B active via Per-Layer Embeddings (each decoder layer gets a small per-token embedding table, cheap at inference). Runs with the footprint/speed of a 4B (~5GB at Q4) but draws on ~2× the stored knowledge. 128K context, native vision, native function calling, configurable thinking.
**Tooling:** Ollama runtime; Obsidian + community plugins (AI Providers / Local GPT) for a private offline "second brain" over your vault; native function calling ("search the vault," "read this file").
**Use cases:** handwriting/label/document OCR and transcription into a knowledge base; drafting/iteration; vision for notes. **Benefits:** truly offline, $0, no metering — the author iterates 10× instead of twice because each prompt only costs seconds.
**Pitfalls (from comments + related pieces):** multiple readers report it runs **slow on 16GB** (one on M4 base MBP: "bit faster but still slow"); Gemma 4 E4B's thinking mode runs longer than Qwen3.5:4b, and full-vs-short thinking is roughly a 73s-vs-25s difference on a coding task. Thinking can bleed into structured output.

### Corroborating techniques from related XDA 2026 articles
- **"Stopped obsessing over parameter count":** pick models by **BFCLv3 tool-calling** and **IFEval instruction-following**, not size. Per IBM's published Granite 4.0 Nano benchmarks (reported by VentureBeat, Oct 2026), "On BFCLv3 (function/tool calling), Granite-4.0-1B led with a score of 54.8, the highest in its size class," versus Gemma 3 1B's 16.3; and "On IFEval (instruction following), Granite-4.0-H-1B scored 78.5, outperforming Qwen3-1.7B (73.1)." Explicit specialist-stable recommendation: "Route with something tiny (LFM2.5-230M), execute with something purpose-built (Qwen/Granite function-calling), hand off to the generalist only when reasoning is genuinely needed." **This is your steward+ladder design, endorsed.**
- **"Local LLM can call Claude when it's stuck":** Ollama + LiteLLM + OpenRouter, deterministic Python orchestrator (a top comment nails it: "Try local, try local, try Claude. Purely deterministic, just a Python function"). Escalate with *only* the needed context (task, errors, snippets, summary), not the whole conversation. Matches your Herdr rescue tier.
- **"Gave my local agent a real memory":** local Qdrant + MCP for persistent semantic memory; key lesson — "a local model will recite your rules back to you and then completely ignore them," so memory use must be scaffolded/triggered deterministically, not left to the model's discretion. Relevant to your shared Qdrant/MCP memory.
- **Ollama multi-model mechanics:** `OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_NUM_PARALLEL`, `OLLAMA_KEEP_ALIVE`; raising NUM_PARALLEL multiplies KV-cache memory; LRU eviction when memory is full. On macOS you must set env vars via `launchctl setenv` (not `.zshrc`) and restart the Ollama menubar app.

### Candidate changes mapped to stack components

| # | Candidate change (source) | Stack component | Verdict | Reasoning |
|---|---|---|---|---|
| 1 | Add **Gemma 4 E4B** as MacBook offline generalist + vision/OCR (Art. 3) | MacBook 4B-class slot; optional vision model | **Adopt** | Replaces two planned slots (4B generalist + small vision) with one multimodal model; native function calling + 128K ctx; ~5GB fits 16GB. Best-in-class vision/tone at this size per XDA head-to-heads. |
| 2 | **Per-specialist hard tool-scoping + two-retry cap** (Art. 1) | OpenHands tool perms; Herdr retry policy | **Adopt** | Pure process/config; contains failures, prevents loops; complements your fail-up guard and five-class taxonomy. No new models. |
| 3 | **Small local thinking model** (DeepSeek-R1-Distill-Llama-8B or Gemma 4 thinking mode) as gated planner/decomposer + hard-retry tier (Art. 2) | Herdr planner stage; fail-up guard local retry | **Trial** | Can improve decomposition and hard local retries, but thinking tokens are much longer and overthink trivial tasks. Only worth it gated with a token budget, measured against measure.py priors. |
| 4 | **Choose steward/specialist by BFCLv3 + IFEval, not size** (parameter-count article) | Model registry selection criteria | **Adopt** | Cheap discipline; directly informs which 1–4B model (Granite 4.0 H, LFM2, Qwen) to pick for tool-calling-heavy steward subtasks. |
| 5 | **Convert warm steward → multi-warm specialist swarm** (Art. 1 spirit) | iMac steward | **Reject** | 16GB fits ~one warm 7B; 7B+4B resident is tight and risks swap/jetsam. Swaps cost 3–8s cold start. Violates your standing rule without payoff on this hardware. |
| 6 | **Sub-1B router model** (LFM2.5-230M / Qwen 2.5 2B) as a distinct warm model (Art. 1, param article) | Herdr triage/classification | **Trial** | A 230M router is nearly free to keep warm and could offload triage/classification from the 7B steward — but your steward already does this and Herdr routing is deterministic Python. Only adopt if measurement shows steward triage latency is a bottleneck. |
| 7 | **Gemma 4 E4B for steward non-coding duties** (summaries/drafting/classification) vs Qwen3-Coder 7B (Art. 3 + head-to-heads) | iMac steward subtasks | **Trial** | Gemma 4 E4B is stronger on tone/summarization/vision; Qwen3-Coder 7B is stronger on code/function-calling. Consider Gemma as a second warm model *only* if memory allows, else route non-coding steward subtasks to the MacBook's Gemma. |
| 8 | **Obsidian/MCP second-brain pattern** (Art. 3) + scaffolded memory triggers (memory article) | Open WebUI + Qdrant/MCP | **Adopt (process)** | Deterministic, triggered memory writes/reads rather than model-discretion; aligns with your Qdrant-via-MCP design. |
| 9 | **"Boring/observable" pipeline principle** (Art. 1) | Whole stack ethos | **Adopt (already aligned)** | Your deterministic verification + per-tier logging already embodies this; formalize an execution-log view like n8n's. |

### Implementation guidance (for every Adopt/Trial)

**#1 Gemma 4 E4B on MacBook (Adopt).**
- Registry: `gemma4:e4b` via Ollama (`OLLAMA_MODELS=/Volumes/AI/`). ~5GB Q4.
- Ollama env (macOS): `launchctl setenv OLLAMA_KEEP_ALIVE -1` for the MacBook's single warm model; restart menubar app.
- Disable thinking for structured/JSON steward calls (omit `<|think|>`); enable only for planning. Use "LOW thinking" system-prompt trick ("Think briefly… key steps only") to cap latency.
- HB build phase: **Phase 1 (local model provisioning)** — it becomes the offline worker + vision/OCR, retiring the separate small vision model.

**#2 Tool-scoping + retry cap (Adopt).**
- OpenHands: per-agent tool allowlists (research agent: fetch/search only; edit agent: fs + terminal in workspace; no cross-folder). Herdr: hard `max_retries=2` per task-class before tier escalation; on failure emit structured `{failed_test, file, reason}` to only the failing specialist.
- HB phase: **Phase 2 (routing/guard hardening).**

**#3 Thinking model (Trial).**
- Registry: `deepseek-r1-distill-llama:8b` (Q4, ~4.9GB) OR reuse Gemma 4 thinking mode to avoid a new model. On Apple Silicon prefer an MLX build for ~10–20% speedup.
- Herdr: add a **planner/decomposer capability tier** invoked only when (a) task-class prior from measure.py shows low local pass-rate, or (b) the fail-up guard's first local retry fails. Cap thinking tokens (`num_predict`/max_tokens) and strip `<think>` before passing to executor.
- Gate: keep it **cold/on-demand** (accept the 3–8s load) rather than warm — it's not a per-request model. Verify it stays >10 tok/s.
- HB phase: **Phase 3 (capability-tier expansion), behind a measure.py A/B.**

**#4 BFCLv3/IFEval selection (Adopt).** Add both scores as registry metadata columns; when choosing any sub-4B steward helper, require BFCLv3 ≥ ~50 for anything doing tool/function calls. Candidates: Granite 4.0 H (tool-calling), Qwen (function-calling/coding). HB phase: **Phase 0 (registry schema).**

**#6 Sub-1B router (Trial).** Only if measurement shows steward triage adds latency: add `lfm2` / small Qwen as an always-warm (<1GB) classifier feeding Herdr; keep Herdr's decision deterministic. HB phase: **Phase 3, measurement-gated.**

**#7 Gemma-for-steward-subtasks (Trial).** Route non-coding steward subtasks (summaries, drafting, classification) to Gemma 4 E4B (on MacBook if iMac memory is tight); keep Qwen3-Coder 7B warm on iMac for code/triage. Measure per-subtask pass-rate + latency before making Gemma a second warm iMac model. HB phase: **Phase 3.**

**#8 Memory scaffolding (Adopt-process).** Make Qdrant/MCP writes/reads deterministic (explicit store/recall triggers in the harness), not model-discretion. HB phase: **Phase 2.**

### Worth-it analysis (measurable improvement vs. added complexity)

- **#1 Gemma 4 E4B (Adopt):** *High value, low complexity.* Consolidates 2 planned models into 1, adds offline vision/OCR you didn't have, and keeps you at one warm model per machine. Expected: +offline capability, +vision, no memory-budget regression. Complexity: one registry entry + thinking-mode config. **Clearly worth it.**
- **#2 Tool-scoping + retry cap (Adopt):** *High value, near-zero complexity.* Reduces wasted retries and blast radius of a bad edit; directly lowers cost by preventing loop escalation to paid tiers. **Worth it.**
- **#3 Thinking model (Trial):** *Medium value, medium complexity.* Upside: better decomposition and harder local retries → fewer escalations to GroqCloud/OpenRouter/Opus, i.e., cost savings on genuinely hard tasks. Downside: much longer token latency, overthinking on easy tasks, thinking-bleed into JSON. Net positive *only if gated*; otherwise it slows the common case. **Trial behind measure.py; adopt only if it lifts a task-class's local pass-rate ≥0.9 without blowing latency budget.**
- **#4 BFCLv3/IFEval (Adopt):** *Medium value, trivial complexity.* Prevents picking a pretty-but-useless small model for tool calls. **Worth it.**
- **#5 Multi-warm swarm (Reject):** *Negative on 16GB.* Two warm models → memory pressure, swap to 2–5 tok/s, possible jetsam kill; swap-on-demand costs 3–8s per switch. No quality gain that a single warm 7B + deterministic routing doesn't already capture. **Not worth it until 24–32GB hardware.**
- **#6 Sub-1B router / #7 Gemma-subtasks (Trial):** *Low-to-medium value, measurement-gated.* Only pursue if logs show the steward is a latency/quality bottleneck on triage or non-coding subtasks. Honor the "few models" rule: don't add unless data says so.

## Recommendations
1. **Now (Phase 0–1):** Add Gemma 4 E4B to the MacBook as the offline generalist+vision model (#1); add BFCLv3/IFEval columns to the registry (#4). Pin one warm model per machine with `OLLAMA_KEEP_ALIVE=-1` set via `launchctl`. Keep `OLLAMA_MAX_LOADED_MODELS=1` on both 16GB machines.
2. **Next (Phase 2):** Implement per-specialist tool-scoping + two-retry cap in OpenHands/Herdr (#2); make Qdrant/MCP memory deterministic/triggered (#8).
3. **Then, measurement-gated (Phase 3):** Trial a gated thinking model as planner/hard-retry tier (#3); trial sub-1B router (#6) and Gemma-for-steward-subtasks (#7) *only if* measure.py logs show steward triage or non-coding subtasks are a bottleneck.
4. **Reject** converting the warm steward into a multi-warm specialist swarm on 16GB (#5). Revisit only if you move to ≥24GB unified memory.

**Thresholds that change these calls:**
- If you upgrade either machine to **≥24GB**, re-open #5/#7 (two warm models becomes comfortable; `OLLAMA_MAX_LOADED_MODELS=2`).
- If measure.py shows a task-class local pass-rate <0.9 that a thinking model lifts ≥0.9 **without** exceeding your latency budget, promote #3 from trial to adopt.
- If steward triage latency exceeds your interactive threshold, promote #6 (sub-1B router) to adopt.
- If the thinking model's median throughput drops below ~10 tok/s on your hardware, drop it.

## Caveats
- **The three primary articles are hands-on/anecdotal, not benchmarked.** Article 1 gives no hardware spec or latency/cost numbers (a commenter explicitly asks for the PC setup); Articles 2–3 rely on single-author impressions and reader comments (several report Gemma 4 "slow on 16GB"). Treat their claims as directional.
- **Model names reflect a mid-2026 landscape** (Qwen 3.5/3.6, Gemma 4, DeepSeek R1 distills, DeepSeek V4). Your registry names (Qwen3-Coder 7B, DeepSeek V4 Flash, Kimi K2.7, GLM-5.2, Opus 4.8) should be reconciled against current Ollama/OpenRouter tags at build time.
- **Cold-start and residency numbers are best-effort:** the 3–5s M2/16GB load figure is a single hands-on blog datapoint; no source offered a rigorously reproducible Apple-Silicon `load_duration` benchmark. Measure your own machine via Ollama's `load_duration` API field before finalizing keep_alive policy.
- **The BFCLv3/IFEval figures come from IBM's own Granite 4.0 benchmarking** (via VentureBeat); the located data benchmarks Granite-4.0-H-1B's 78.5 IFEval against Qwen3-1.7B (73.1), not against a 32B-class model — verify any larger-model comparison before relying on it.
- **Security note:** one XDA commenter and general reporting flag past LiteLLM supply-chain concerns; pin versions and monitor advisories for your gateway.
- **Per-Layer Embeddings "2× knowledge" framing** is the article's/Google's description; independent head-to-heads still show Qwen ahead on reasoning/coding, so don't treat Gemma 4 E4B as a coding-steward replacement.
