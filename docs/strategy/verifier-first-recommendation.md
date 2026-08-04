# The strongest recommendation

*2026-08-04. Written after HB-0, the Scale-2 profile, the data-destinations
policy, spec 12 on market surveillance, and the edge-inference research. Those
five pieces were commissioned separately and converge on one thing, which is
what this memo is about.*

---

## 1. The recommendation

**Move CC-P1 — the verifier contract — ahead of HB-1, and treat it as the
flagship publishable artifact rather than internal plumbing.**

It is currently scheduled fourth, its prompt is stale, and its position in the
run order is ambiguous between two documents. It should be the next
substantive thing built after Cairn ships, and it should be resourced as the
thing the grants are actually about.

## 2. Why — the convergence

Each of the last five workstreams hit a wall, and it was the same wall.

| Workstream | What it ran into | What resolves it |
|---|---|---|
| Spec 12 — market surveillance | Public benchmarks inflate 6–40%; SWE-bench Pro showed GPT-5 at 41.8% public → **15.7% held-out**. Rankings are unreliable, not just scores | Your own held-out eval — the **Parity Bench** |
| Edge research — small models | Constrained decoding: validity 61.5%→100% while accuracy **fell** 19.7%→11.0%, **88.9% wrong-but-schema-valid** | Independent deterministic content check — the **verifier contract** |
| Edge research — distillation | Fine-tuning is the largest lever, but needs trustworthy labels | Verifier verdicts as labels — `distill.py`, gated on **CC-P1** |
| Scale-2 profile | "Sovereign by absence" had to be *proved*, not asserted | A machine check — shipped, and it's the same pattern |
| data-destinations | A policy nothing enforces is the failure mode this platform exists to avoid | A machine check — shipped |

**Nothing gates CC-P1.** It is hermetic, offline, needs no live gateway, and
its hardest input — Belay's LeakOracle — already exists and is the strongest
predicate in the codebase.

**CC-P1 gates nearly everything else.** HB-2's `failup.py` is specified as
running *on* the contract. `distill.py` needs its verdicts as labels. The
Parity Bench needs its profiles to score anything without an LLM judge. Belay's
leak gate is Step 2's port. And the PESOSE portability claim — *two consumers
in two languages* — **is** the conformance suite. That is one artifact carrying
both federal packages.

By contrast, HB-1 wires Aider, Open WebUI and OpenHands. Real quality-of-life,
genuinely useful to you daily, and it unlocks nothing downstream.

## 3. The strategic version of the same point

Everything researched this session says the same thing about the market: **in
2026, self-reported AI capability stopped being trustworthy, publicly and at
scale.**

- OpenAI abandoned its own headline benchmark, finding 59.4% of audited
  failures had broken tests and every frontier model could reproduce the answer
  key.
- A NeurIPS paper documented a lab testing 27 private variants and publishing
  only the best, worth up to 112% relative gain.
- A 55-study review found no contamination-detection method is consistently
  reliable, with inflation varying per model by training hygiene nobody can
  observe.
- Grammar constraints, the standard fix for structured output, were measured
  producing *more* wrong answers wearing valid schemas.
- Google reserves the right to remotely restrict Gemma usage. Apple's
  acceptable-use terms prohibit courseware outright.

EduCloud was architected around not trusting any of that — before it was
obviously necessary. SYSTEM.md §3's invariant, *no module trusts a model's or a
provider's self-report*, is now the scarce property rather than the fastidious
one.

**That reframes what EduCloud is.** It is not primarily an open-source
GitHub Classroom replacement — those exist, and Cairn's real job is to be the
demonstration surface that makes a pilot possible. What is genuinely scarce is
a platform where every claim is checked by a deterministic instrument outside
the model, and where the instrument is portable, published, and adoptable by
people who will never run your software.

Cairn, Belay, Portage and Outfitter are how you prove it works. The verifier
contract and the Parity Bench are what you are actually contributing.

## 4. What changes

**Immediately, at no cost to Cairn's clock:**

1. **Resolve the run-order ambiguity in writing.** `MANIFEST.md` says HB-1 then
   CC-P1; `CW02-decisions.md` §6 says CC-P1 then HB-1; CW02's own stage mapping
   agrees with MANIFEST. The only binding dependency is HB-2 consuming the
   contract. Settle it as: **Cairn → CC-P1 v2 → HB-1 → HB-2.**
2. **I author CC-P1 v2 next** — re-pathed to its own repo, Sol → Belay,
   reconciled against HB-0's registry. This is the item still outstanding from
   my original three and it is now the highest-value one.

**In the pilot window:**

3. **Re-scope the Parity Bench's resource-tier factor** from "two 16 GB Macs"
   to the measured device tiers in the edge research — WASM floor (<5%
   excluded), WebGPU mid (15–20%, concentrated in ChromeOS), native high. That
   converts the equity claim from a proxy into something an IUSE reviewer
   recognises as the actual question.
4. **Ship the capability probe.** An afternoon, no model, no personal data, and
   it turns the tier factor into measured data before the pilot rather than
   after.
5. **Score the bench with verifier profiles, not an LLM judge.** Using a model
   to grade the instrument that proves models need grading would be
   self-refuting, and a reviewer would be right to say so.

**In the grant narrative:**

6. **Lead with verification, not with the classroom tool.** The 2026 evidence
   base above is the strongest argument either package has, and it is external,
   citable, and was not available a year ago.
7. **Resolve the Gemma licence question.** A remotely-restrictable model in the
   live registry undercuts the vendor-independence claim both packages rest on.

## 5. What this costs, honestly

Reordering is not free. HB-1 is what makes your own daily stack pleasant to
use, and deferring it means Aider, Open WebUI and OpenHands stay unwired
through September. That is a real cost paid in your own friction, every day,
for a benefit that is mostly institutional.

Two things make it tolerable. HB-0 already delivered the gateway, so the
aliases work — HB-1 is convenience on top of a working proxy, not the proxy
itself. And CC-P1 is hermetic, so it can proceed without competing for the
hardware attention that HB-0's remaining gates and Cairn's deployment both need.

**What would falsify this recommendation:** if CC-P1 turns out to need
substantially more than a session or two, it stops being cheap and starts
competing with the pilot directly. The mitigation is Step 2's design — port
Belay's LeakOracle *first*, against the existing test fixtures, and let that
port tell you whether the contract shape is right before writing three more
profiles. If the port is ugly, stop and reconsider rather than pushing through.

---

## 6. Stretch goals

Four, ordered by ratio of claim strengthened to effort spent.

### 6.1 Make "no vendor is a hard dependency" a test, not a claim

Both grant narratives assert vendor independence. Right now it is a design
property nobody can check. **A CI job that boots the whole platform against a
fully open-weight configuration and runs the conformance suite green would
prove it** — and the Scale-2 student registry is already exactly that
configuration, so most of the work is done.

Cheap, and it is the kind of thing a reviewer remembers. It also converts a
claim that currently depends on trusting your architecture diagram into one
that depends on reading a build badge.

### 6.2 Get a third-party implementation of the verifier contract

PESOSE Track 1 wants the contract carried as a portable standard with two
consumers in two languages. Two consumers *you wrote* demonstrates portability
in principle. **An implementation by someone outside the project demonstrates
it in fact**, and that is a categorically stronger claim.

The conformance suite is what makes this askable: anyone can claim conformance
by passing a runner. A short workshop paper plus a public call for
implementations, timed after CC-P1 lands, could plausibly produce one before
Track 1 closes in March. Even one external implementation changes the sentence
from "we built it twice" to "someone else built it from the spec."

### 6.3 Turn the Parity Bench into a standing public instrument

The contamination crisis created a gap the field currently cannot fill: there
is **no held-out, education-specific, resource-tiered benchmark with a real
preregistration**. Every public option is contaminated, gamed, or measures
preference rather than task success.

Running the bench continuously across device tiers, publishing either outcome,
and releasing the harness would make it infrastructure rather than a study.
That is a Track 2 argument — it is exactly the kind of durable community asset
a managing organisation exists to steward, and it is defensible precisely
*because* the equity finding might come out unfavourable.

### 6.4 Release verifier-labelled training data

`distill.py`'s inputs are unusual: labels produced by deterministic verifiers
rather than by model judgments or crowdworkers. Almost everyone fine-tuning
small models manufactures synthetic labels of unknown quality.

The attribution vocabulary already makes the de-identification tractable, and
the data-destinations policy already governs what may be released. A public
dataset of verifier-labelled coding and tutoring outcomes would be a real
contribution, would directly support the small-model thesis the edge research
validates, and costs little beyond the release process — because the data is
generated as a byproduct of the platform simply running.

---

## 7. The one-line version

The five workstreams this session all failed at the same wall — you cannot
trust what a model or a vendor says about itself — and EduCloud already owns
the answer. **Build the answer next, and lead with it.**
