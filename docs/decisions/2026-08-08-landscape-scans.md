# Landscape scans, 2026-08-08 — the platform-level outcomes

*Five research passes run across one day: LLM routing/gateway/brokering; Morph's
full product line plus Perplexity, coding agents, observability and guardrail
providers, and AI-EdTech competitors; then hosting/identity analogues, compute-
brokering analogues, and code-execution isolation. The module-scoped conclusions
went into the modules. **This record holds only what crosses module boundaries**,
because those are the things that will otherwise end up owned by whichever repo
happened to notice them first.*

**Status:** decision record. Amends no contract in `SYSTEM.md`, but §4 names one
contract question that is now overdue an explicit answer.

---

## 1. The platform invariant survived contact with the field, and is uncontested

`SYSTEM.md` §3 says no component trusts a model's or provider's self-report; a
deterministic check decides. The scans looked for prior art against that and
found the opposite — corroboration, plus published backing that did not exist
when the invariant was written:

- **Routing.** The open-source field is saturated with classification-first
  routers (vLLM Semantic Router, LLMRouter, RouteLLM, Arch-Router, Morph's
  Router) and has **no maintained verify-then-escalate system**. The nearest
  research artifacts (FrugalGPT, eth-sri/cascade-routing) gate on *learned
  confidence*, not deterministic verification. eth-sri/cascade-routing (ICML
  2025, arXiv 2410.10347) proves cascade routing dominates pure routing — cite
  it rather than asserting the design.
- **Coding agents.** Surveyed Cursor, Copilot agent mode, Replit Agent, Devin,
  Windsurf, Amazon Q, Aider, OpenHands, SWE-agent: **none publishes a
  deterministic, non-LLM verification gate as its default trust mechanism.**
  Most "SWE-bench verified" numbers come from vendor harnesses using LLM-as-judge
  rather than an actual test run.
- **Tutoring.** Harvard's CS50 Duck published the failure mode directly:
  prompt-only leak prevention degrades measurably at scale — **22% of responses
  still contained full code** despite explicit anti-leak instructions, once the
  system prompt passed ~1,000 tokens (ACM, `dl.acm.org/doi/10.1145/3641554.3701945`).
  Two 2026 papers land close to Belay's actual architecture: an ACL 2026
  adversarial-student-agent benchmark for answer leakage (arXiv 2604.18660) and
  "Auditable Release Control for Pedagogical Leakage in LLM Tutors"
  (arXiv 2608.00515), which describes a deterministic release gate with a
  graduated disclosure contract.
- **Compute.** Nobody blocks provisioning on a predicted monetary ceiling across
  heterogeneous providers with per-student attribution. (Narrowed from the
  earlier absolute claim: GCP Spend Caps and AWS Budgets Actions now hard-block
  within a single provider. See `outfitter/specs/03` §7.)

**Consequence for the grant narratives:** the invariant is not just a design
preference to defend, it is an unclaimed position with published theoretical
backing in three of the four domains. That is a stronger sentence than the
proposals currently make.

## 2. Isolation is a platform concern, and it now has one owner

Three modules run untrusted code or provision the machines that do — Cairn's
autograder, Belay's runner, Outfitter's adapters — and until now each held its
own boundary independently. They had drifted badly: Cairn's container runner is
well-hardened (caps dropped, no-new-privileges, read-only rootfs, pids/memory/cpu
limits, fail-safe `--network none`), while Belay's runner is a child process with
`setrlimit` and socket monkeypatching that any of `ctypes`, `subprocess`, or a
raw `socket()` bypasses in one line, and which shares a process with the grading
harness so the reference solution is reachable.

**`outfitter/specs/08-isolation-tiers.md` is now the single normative spec**, and
lives in Outfitter because Outfitter provisions the compute — but it is
platform-level and Cairn and Belay are consumers, not independent implementers.
The design property that makes this work: **the isolation tier is a
per-assignment policy field, not a build-time decision**, because gVisor and Kata
are both RuntimeClass-selectable. That keeps tier changes a config diff, matching
the expansion contract (`SYSTEM.md` §7).

Also settled there, so it is not re-litigated per module: a plain OCI container
is not a security boundary (2024–2025 produced working `runc` escapes); GPU
coursework routes to batch/HPC rather than being isolated harder, because
gVisor's `nvproxy` is a large weakly-validated attack surface; and the harness
must run outside the sandbox, since if student code and test code share a process
the student wins.

## 3. LTI 1.3 is an adoption gate, and it was in nobody's must-have list

**A classroom tool that cannot LTI-launch from Canvas, Moodle, or Blackboard is
dead on arrival at most universities.** It sat at Cairn Phase 4 ("stretch") as
NRPS roster sync; the scan concluded the underlying capability is an identity
concern before it is a roster one, so it belongs to Waypoint, at must-have.
Recorded in `waypoint/docs/decisions/2026-08-08-analogue-scan.md` §2.

Two knock-on effects that make this a platform item rather than a Waypoint one:

- **NRPS replaces GitHub Classroom's roster import outright.** Cairn's migration
  story currently depends on `cairn import ghc` snapshotting before the
  September 4 deletion. LTI gives every *future* course a roster path with no
  GitHub dependency at all — which is the more durable version of the same
  promise.
- It interacts with `SYSTEM.md` contract 3 (Keycloak is the ecosystem OIDC
  provider). An LTI launch must not become a second, parallel identity system;
  the Waypoint record flags "mint a session directly vs. broker into Keycloak"
  as a decision to make explicitly rather than by whichever library quickstart
  gets copied.

## 4. One contract question is now overdue

`portage/docs/specs/13-routing-paradigm.md` §3 raised it and it has gone
unanswered since: **does contract 2's "no proprietary models" extend to
proprietary routing and classification infrastructure?**

It was raised about Morph's Router (hosted-only, undisclosed classifier, on the
critical path for every request), but the follow-up scans made it broader and
more urgent, because the same shape keeps appearing:

- Morph's **Reflexes** (hosted turn classifiers) would need to see raw student
  conversational content to work.
- Perplexity's **Internal Knowledge Search** and **Sonar** would send documents
  and queries to a third party.
- **Lakera Guard** and **Azure AI Content Safety**, the obvious guardrail
  vendors, are hosted-only with no open weights.

In every case the answer this platform reached independently was "no, build the
local equivalent" — and in every case a genuinely self-hostable open-weight
option existed (Meta's Prompt Guard 86M and IBM's Granite Guardian for
classification; a local retrieve-then-cite layer over Belay's existing BM25
index; Portage's own ladder in place of a hosted router). So the *practice* is
settled and consistent. **The rule is just not written down**, which means it is
being re-derived case by case, and the next case may be decided differently by
whoever hits it.

A hosted classifier on the critical path is arguably a larger sovereignty problem
than a proprietary model in a disabled rescue tier, because the rescue tier is
opt-in and audited while the classifier would touch every request. That asymmetry
is the substance of the question, and it belongs in `SYSTEM.md` contract 2, not
in a Portage spec.

## 5. What each module took away

Recorded here only as an index; the detail is in each repo.

| Module | Landed | Queued as prompts |
|---|---|---|
| **Portage** | `specs/13` (routing paradigm, three corrections) | `CC-P11` residency-survives-failover · `CC-P12` escalation cost · `CC-P13` classification-informed entry rung · `CC-P14` self-hosted Langfuse |
| **Belay** | ARCHITECTURE/VALIDATION citations; ROADMAP gaps recorded | `CC-B1` local guardrail model · `CC-B2` adversarial leak benchmark · `CC-B3` citation-grounded retrieval · `CC-B4` sandbox replacement |
| **Outfitter** | `specs/01` rewritten (4 corrections), `specs/08` new, `specs/02`+`03` revised, ROADMAP triage + ACCESS path | `CC-O1` M1 against the corrected interface |
| **Waypoint** | `docs/decisions/2026-08-08-analogue-scan.md`, CHANGELOG r8 | `CC-W1` LTI 1.3 |
| **Cairn** | — (its runner was already sound) | `CC-CA1` gVisor isolation tier |

## 6. Build-vs-adopt calls worth knowing platform-wide

Each is recorded in its own module, collected here so the umbrella has one view
of what the platform decided *not* to build:

- **ColdFront** (AGPLv3) for allocation request/approval/expiry, **Open XDMoD**
  (LGPL-3) for the usage warehouse — both ACCESS-native, both already read by
  campus RCS staff. Outfitter builds the monetary ceiling, not the portal.
- **PyLTI1p3** (MIT) for LTI, rather than hand-rolling OIDC launch validation.
- **Piston** (MIT) as a possible sandbox component; **nbgrader**'s format but
  never its execution model.
- **Langfuse** (MIT, self-hosted) for observability, instrumented via
  vendor-neutral OpenLLMetry so the sink stays swappable.
- **SkyPilot**: neither fork nor depend — port three ideas (capability flags,
  cluster-side hard TTL, one server-side pre-provision gate).
- **Skip on licence grounds:** Dokploy (relicensed Jan 2026), Portainer and
  Nomad (the needed features are the paid tier), Daytona (went closed-source
  June 2026 — a direct cautionary case for the no-proprietary-default rule).
