# Edge inference and small models — what they mean for EduCloud

*Research synthesis, 2026-08-04. Two deep literature and vendor-documentation
passes, ~220 tool calls, citations throughout. The conclusion is not the
obvious one: for EduCloud, edge AI is not a cost optimisation. It is a privacy
mechanism and an equity instrument, and the equity finding cuts against the
approach most people would reach for first.*

---

## 1. Four findings that change decisions

**1. On-device inference is the only architecture where student data never
moves at all.** `data-destinations.md` §4.3 records that the `regulated` class
has no deployment at any scale — identifiable student content has nowhere to
go, deliberately. Inference that runs in the student's own browser is not a
better tier in that table; it is *outside* it. No destination, no processor, no
authorization question. That is a stronger privacy property than D1
institutional hosting, and it is available today.

**2. Chrome's built-in Prompt API — the obvious "free on-device AI" answer —
is an anti-equity play.** It requires **22 GB free disk**, and either **>4 GB
VRAM or 16 GB RAM with 4 cores**, and on ChromeOS runs **only on Chromebook
Plus**. Not available on Chrome for Android or iOS at all. It excludes the
exact population EduCloud exists to serve. It can be an opportunistic fast
path; it can never be a dependency.

**3. Apple's Foundation Models framework is contractually unavailable to us.**
Its acceptable-use requirements explicitly prohibit uses that generate
*"scholarly and academic research products, journals, textbooks, trade books,
or **courseware**."* Read literally, that names our product. It is also
Swift-only with no web path. **Rule it out and stop considering it.**

**4. Constrained decoding produces well-formed wrong answers, and the effect is
large.** *The Constraint Tax* (arXiv:2605.26128, May 2026) measured 15,000
generations across Qwen2.5-0.5B/1.5B/3B and SmolLM2-1.7B: hard schema
constraints moved validity 61.5% → **100%** while accuracy *fell* 19.7% →
**11.0%**, and "wrong-but-schema-valid" outputs rose to **88.9%**. On a
calendar tool-call task both modes were 100% valid, but executable accuracy was
91.5% prompt-only versus **48.0%** schema-constrained. Corroborated by *Let Me
Speak Freely?* (EMNLP 2024): GSM8K 76.6 → 49.3 under JSON mode, with the
mechanism identified as schema field ordering destroying chain-of-thought.

That fourth finding is the one that matters most to us, and §5 explains why.

---

## 2. What is actually true about small models

**The tiny-model thesis is real, but conditional.** It reduces to: *a small
model plus your labelled data beats a large model plus your prompt, on a task
with a closed output space and bounded state.* It says nothing favourable about
zero-shot small models, multi-step agents, or long context.

Where it holds, measured:

- Fine-tuned Qwen2.5-0.5B reaches **0.828 F1 on relation classification** vs
  GPT-5.4 at 0.69 (arXiv:2606.22606). The authors concede the comparison
  favours the tuned model and make no out-of-domain claim.
- distil labs fine-tuned **LFM2.5-350M** on bounded tool tasks: shell
  61.4→**98.0%**, smart home 63.2→**96.7%**, banking voice routing
  34.5→**95.9%** — matching GPT-oss-120B, a model **343× larger**, from ~5,000
  synthetic examples after one epoch.

Where it collapses:

- **Off the shelf, sub-1B is not close.** Qwen3.5-0.8B scores **9** on the
  Artificial Analysis Intelligence Index while six labs field models above 50.
- **Agentic multi-turn fails.** LFM2.5-350M scores **18.86 on τ²-Bench
  Telecom**. Its own BFCL v3 44.11 → BFCL v4 21.86 shows the cliff arrives the
  moment tool calling becomes agentic rather than single-shot.
- **Factual recall is absent.** 80–82% hallucination rates on AA-Omniscience
  across the Qwen3.5 sub-10B family. Small models must be paired with
  retrieval; they cannot be the knowledge store.
- **Long context is nominal.** Qwen3.5-0.8B advertises 262K. No study validates
  effective context at this scale; the nearest evidence has Qwen2.5-**7B** F1
  falling 45.5% past ~43% of stated maximum. Assume worse below 1B.

**Two traps worth naming, because both touch our registry today.**

*Quantization below 2B is not free.* Qwen3-0.6B loses **~10% MMLU at 4-bit**
against ~1% for Qwen3-14B; at 3-bit small models fall to MMLU ~25–28, which is
chance. Worse, degradation scales with **training tokens per parameter** (ACL
2025) — so the well-trained tiny models worth running are precisely the ones
least tolerant of aggressive quantization. The "Q4 is basically free" heuristic
comes from 7B–70B and does not transfer.

*Gemma's "E" sizes are not what they appear.* Gemma 4 **E2B** is 2.3B
*effective* but **5.1B with embeddings**, and its Q4_K_S GGUF is **3.04 GB** —
Per-Layer Embeddings cost RAM even when they don't cost FLOPs. Our registry
pins `gemma4:e4b` on the MacBook; the same arithmetic applies and the real
footprint is larger than the name implies. **Worth measuring during HB-0's
native gates rather than discovering under load.**

**BitNet: real kernels, empty roster.** bitnet.cpp shows genuine 2.4–6.2×
speedups and BitNet b1.58 2B4T is a credible MIT-licensed model at 0.4 GB. But
**no natively-trained 1.58-bit model was released by any lab in 2026**, the
context ceiling is 4K, and all benefit requires bitnet.cpp rather than
transformers. Do not bet an architecture on ternary weights. The pragmatic
frontier is Q4 on a well-trained 0.35–1B model.

---

## 3. The equity finding, which is the important one

Line E's Parity Bench carries a **resource-tier factor**, currently seeded by
"Line P's two-Mac under-resourced arm." Two 16 GB Macs are not an
under-resourced arm. They are a developer's spare hardware. The genuine
equity question is what a student on a school-issued Chromebook can run — and
the edge research answers it with numbers.

**Exclusion by architecture:**

| Architecture | Devices excluded |
|---|---|
| WASM/CPU floor (wllama, ~250 MB model) | **<5%** |
| WebGPU required (WebLLM, Transformers.js) | ~15–20% globally, **concentrated catastrophically in ChromeOS** |
| WebGPU + ≥1 GB VRAM | ~30–40% |
| Chrome Prompt API | **the large majority of an undergrad population** |

The ChromeOS concentration is the crux: **WebGPU on ChromeOS requires Vulkan**,
and Chrome's own Intent-to-Ship states ChromeOS has *"low Vulkan
penetration."* WebGPU Compatibility Mode, which would rescue these devices via
OpenGL ES 3.1, shipped for **Android first** in Chrome 146 and had not reached
ChromeOS through Chrome 150. Chrome also reports **31% of Windows Chrome users
lack Direct3D FL 11.1+**.

So the device tiers, concretely:

- **School Chromebook (4–8 GB, $200–400):** WebGPU probably unavailable, Prompt
  API excluded, 32/64 GB eMMC cannot meet the 22 GB requirement. What works is
  **wllama on WASM with a ~250 MB GGUF** at low-single-digit to ~10 tok/s — a
  150-token answer in 15–40 seconds. Viable for bounded classification and hint
  generation. **Not viable for chat.**
- **Five-year-old Windows laptop (Iris Xe, 8 GB):** WebGPU likely yes, Prompt
  API excluded. Qwen2.5-0.5B at 291 MB works. **This is the median device and
  it is fine.**
- **Base iPad (A16, 6 GB):** WebGPU yes, Apple Intelligence **no** — the
  cheapest iPad a student buys is excluded from Apple's on-device model. Hard
  **~500 MB Safari tab memory ceiling** means 270M–500M class only.
- **Modern MacBook (M1–M4):** 30–100+ tok/s, no problems. This cohort is not
  the equity question.

**The implication for the bench.** A preregistered instrument that measures
verified task success across *these* tiers — WASM floor, WebGPU mid, native
high — measures something an IUSE reviewer actually cares about: whether the
platform's benefit is available to students who did not buy a $2,000 laptop.
That is a materially stronger equity finding than a two-Mac arm, and the
tiering above is defensible and citable.

**Recommended cheap action: ship a capability probe.** One page of JavaScript
reading `navigator.gpu`, adapter limits, `shader-f16`,
`navigator.storage.estimate()`, `deviceMemory` and `hardwareConcurrency`,
served to existing course web traffic. It costs an afternoon, requires no
model, collects no personal data, and converts the resource-tier factor from an
assumption into measured data before the pilot. **This is the single
highest-leverage thing in this document.**

---

## 4. Where this fits each module

**Belay — the strongest fit, and the one that resolves a standing problem.**
Student-facing tutoring is `sovereign` by default and is exactly the workload
whose data should never move. A tutoring turn is bounded, retrieval-grounded,
and does not need frontier reasoning. On-device Belay means the student's
question never reaches any server — stronger than the sovereign tier, and it
makes the marginal cost of an additional student **zero**, which is the
Matthew-filter argument made concrete. Constraint: 5–15 tok/s on the floor
tier, so the interaction must be designed around short, bounded exchanges
rather than open chat.

**Cairn — helps at the edges, does not solve the storage question.** Cairn is
the system of record; rosters and grades are server-side by necessity, and
on-device inference changes nothing about that. Where it does help: a
grading-feedback drafter or a rubric-check hint could run client-side, keeping
submission content off the server for that step. Do not overclaim this — it
does not move Cairn's R2 classification and it does not change the D1/D2
deployment decision that blocks the pilot.

**Portage — the routing question, and a real conflict.** A tiny local model as
the `classifier` alias is well-matched: classification is precisely where the
thesis holds. But note the honest finding from *Evaluating SLMs for Front-Door
Routing* (arXiv:2604.02367): Qwen2.5-3B reached 0.783 accuracy at 988 ms and
zero marginal cost — Pareto-dominant — but **no model met the study's viability
bar of ≥0.85 accuracy**. A 6–8 point gap remains. Our `classifier` alias
already has a local deployment; the question is whether it could be *much*
smaller, and the answer is "only after fine-tuning."

**Waypoint — one architectural conflict to decide early.** wllama's
multithreaded WASM requires **COOP/COEP cross-origin isolation headers**, and
those headers break iframe embedding. If Cairn is to launch as an **LTI tool
from Canvas or D2L**, that conflicts directly with multithreaded in-browser
inference on the same origin. Decide whether the edge component is a separate
origin, or accept single-threaded WASM. **This is a design decision, not a
detail, and it is cheap now and expensive later.**

---

## 5. Why this makes the verifier contract *more* important, not less

The Constraint Tax result deserves restating in platform terms.

Grammar-constrained decoding guarantees a small model emits schema-valid
output. It does not make the content correct — measured accuracy went *down*,
and **88.9% of outputs became wrong-but-valid**. A schema-valid wrong answer
passes every check a system normally applies: it parses, it validates, it has
the right fields, it looks exactly like a correct answer.

That is the precise failure mode this platform was built to catch. SYSTEM.md
§3's invariant — *no module trusts a model's self-report* — is not
philosophical hygiene here; it is the only thing standing between a 350M model
and silently wrong grading feedback. The CC-P1 verifier contract is what makes
small models *safe to deploy at all*, because it is an independent
deterministic check on content rather than on form.

Two consequences:

1. **CC-P1 becomes a prerequisite for any edge work**, not a parallel track.
   Deploying a tiny model without a verifier is deploying the exact failure the
   research documents.
2. **The practical recipe the evidence supports** — fine-tune rather than
   prompt; keep schemas flat; put reasoning fields before answer fields, or
   leave reasoning unconstrained and *"constrain late"* (which recovered
   accuracy 26.8% → 40.7% at equal validity); and **validate every output
   independently of the decoder**, because XGrammar has 38 documented
   under-constrained failures where it reports success while violating the
   declared schema.

---

## 6. distill.py was already pointed here

The most actionable finding is that this is not new capability. `distill.py`
exists in the engine repo today, parked until HB-4, and its header states its
purpose: *"turn the platform's own verifier logs into training data."*

The research says fine-tuning is the single largest lever — larger than model
choice or decoding strategy — and that **~5,000 examples over one epoch** took
a 350M model from 34.5% to 95.9% on bounded tool routing. EduCloud generates
exactly that data as a byproduct of running: Cairn's grading runs, Belay's
leak-gate verdicts, and every fail-up escalation are labelled examples whose
labels came from a deterministic verifier rather than from a model.

That is an unusually good position. Most people fine-tuning small models must
manufacture synthetic labels of unknown quality. The verifier contract makes
ours trustworthy by construction — which is the same property that makes the
Parity Bench credible.

So the tiny-model path is: **CC-P1 (trustworthy labels) → operate (accumulate
them) → distill.py (train the small model) → the bench (verify it holds).**
Each step already exists in the roadmap. Nothing new needs inventing.

---

## 7. What to do, and when

**Now, costs an afternoon:** ship the capability probe (§3). It is the only
item here that should touch August, and it does not compete with Cairn.

**HB-0 native gates, already scheduled:** measure `gemma4:e4b`'s real memory
footprint against its name (§2), since the E-series arithmetic is misleading.

**Before any edge commitment — verify, do not assume:** whether WebGPU actually
works on the Chromebook models your students carry. ChromeOS Vulkan penetration
is documented only qualitatively. This single measurement determines whether
the mid tier exists for your population.

**E1 pilot:** nothing. Do not build edge inference during the pilot semester.

**HB-4 / S4:** `distill.py` gains a small-model target and the collapse guards
it is already specified to need.

**E3 / 2027:** Belay on-device as the student sovereign lane, gated on CC-P1
being settled in practice.

**Do not build:** anything depending on Chrome's Prompt API; anything on
Apple's Foundation Models framework; anything on MediaPipe LLM Inference for
Web, which is **maintenance-only** with Google directing developers to
LiteRT-LM, itself an early preview supporting two models.

**One licensing item to resolve.** The Gemma Terms of Use are not open source
and state that *"Google reserves the right to restrict (remotely or otherwise)
usage."* For a platform whose thesis is that no vendor is a hard dependency,
and which is heading to PESOSE on that claim, a remotely-restrictable model in
the live registry is a positioning problem as much as a legal one. Gemma 4's
model card reportedly says Apache-2.0, which would be a significant departure
— **verify against the actual LICENSE file.** If it does not hold, prefer Qwen
(Apache-2.0), SmolLM2 (Apache-2.0), Granite (Apache-2.0) or LFM2.

---

## 8. Operational gotchas worth knowing before designing anything

- **Safari evicts your model.** WebKit deletes script-created storage for
  origins with no user interaction in **7 days of browser use**. A student
  using the tool weekly re-downloads it weekly. `navigator.storage.persist()`
  is mandatory — and Chrome/Safari decide silently from engagement heuristics,
  so persistence cannot be guaranteed.
- **Eviction is all-or-nothing** — IndexedDB, Cache API and OPFS go together.
  There is no partial model loss, only total re-download.
- **Thermal throttling is severe:** iPhone 16 Pro loses **41.5%** throughput
  over 20 consecutive inferences (40.5 → 23.7 tok/s). Design the UX around the
  throttled number, not the first-query number.
- **Metered connections:** Chrome and Edge refuse to download *their* models on
  metered networks. Your download has no such protection and will happily pull
  700 MB over a student's hotspot. Gate it explicitly behind
  `navigator.connection.saveData`, show the MB figure, require consent. Data
  caps are a real equity harm and an easy one to inflict by accident.
- **Accessibility:** token-by-token streaming into an `aria-live` region floods
  screen readers — buffer to sentence boundaries. And equity-of-latency is
  itself an accessibility concern: if the tool is graded coursework, a student
  at 5 tok/s has a materially worse instrument than one at 100 tok/s. That is a
  defensible-practice problem, not only a UX one.

---

*Primary sources include: The Constraint Tax (arXiv:2605.26128); Let Me Speak
Freely? (EMNLP 2024 Industry); JSONSchemaBench (arXiv:2501.10868); Llamas on
the Web (arXiv:2605.20706, UCSC/Microsoft Research); LLM Inference at the Edge
(arXiv:2603.23640); An Empirical Study of Qwen3 Quantization
(arXiv:2505.02214); Low-Bit Quantization Favors Undertrained LLMs (ACL 2025);
Evaluating SLMs for Front-Door Routing (arXiv:2604.02367); Chrome Prompt API
and built-in AI documentation; Apple Foundation Models acceptable-use
requirements; WebKit storage policy and standards-positions #495; gpuweb
implementation status; Gemma Terms of Use; Liquid AI, IBM Granite, Qwen and
NVIDIA model cards; distil labs fine-tuning reports. Retrieved 2026-08-04. Full
citation list in the research transcript; vendor-published figures are marked
as such and several load-bearing items are flagged unverified in §7.*
