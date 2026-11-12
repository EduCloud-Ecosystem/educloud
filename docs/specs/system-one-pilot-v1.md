# System One classroom pilot coordination

2026-11-12. User direction: System One maps input plus questions directly to
typed decisions, rather than being a fast text generator. First bounded outcome:
**shadow decision integration through actual Belay-classroom and Portage**.

## Ownership and isolation

Worktrees are under `/Users/gregchism/dev/.educloud-worktrees/`. Engineering is
owned by this coordination workstream; Greg retains instructional and pilot
acceptance. No other chat, background agent or research agent was dispatched.

| Repository | Worktree / branch | Base | Scope |
| --- | --- | --- | --- |
| Portage | `portage-system-one-shadow-pilot-v1` / `codex/system-one-shadow-pilot-v1` | `79742746b10ace18e498111dd5a8f3227edd995c` | Typed score contract, rules baseline, synthetic gateway hook, existing ledger, tests/demo |
| Belay-classroom | `belay-classroom-system-one-consumer-v1` / `codex/system-one-classroom-consumer-v1` | `656d6ec1e4be5f9ef7267f5a2bb5145a90238dfe` | Dependency pins, actual-SDK tests/workflows, handoff; no tutor source |
| EduCloud | `educloud-system-one-pilot-coordination-v1` / `codex/system-one-pilot-coordination-v1` | `9897c92371400fcb991619c4a46d438a960ef404` | Coordination and reviewed evidence |

Remote Portage main was checked at `7974274`, the compatible classroom base.
Primary `portage` is divergent `codex/ai-pilot` at `9e2a877`, lacking qualification
controls in selected main. Its untracked guidance, all existing worktrees and
the dirty EduCloud main remain untouched. Original Belay `79589b3` is untouched.
Read-only dependencies: Cairn exporter `0cf3158fdf5bbbecc52d3cc9cd88ef33bdfb63fc`
and existing Waypoint presenter `3ec286f5d41e857622d9b24f23b3c31e6f248605`.

## Decision and responsibility boundary

Reuse existing authenticated admission, membership, reservations, usage ledger
and Belay task aliases. No new service, browser flow or reservation authority.
`PILOT_DECISIONS=rules-shadow-v1` enables the ordinary rules baseline only on a
synthetic gateway; default is off. Hosted/qualification modes reject the hook.

At most 4096 UTF-8 bytes from the latest user message plus fixed questions
(`task_class`, `recommended_tier`, `needs_retrieval`) enter one backend call.
Invalid/non-finite/ambiguous scores abstain. Scores are uncalibrated, never
probabilities. Content-free metadata retains backend/source identity, elapsed
time and call counts against the original admitted request. No input, generated
text or exception message is logged. Real-data retention policy remains open.

Advice cannot change the actual route, permissions, grades or charges. Membership
and deadline are rechecked after shadow work. Unknown usage keeps its original
hold. Each explicit JSON repair remains a separately counted transport/decision.
The backend interface is trusted bounded local code, not an arbitrary plugin
sandbox. A real model must qualify its artifact, execution bounds and data use.

The working pilot uses **ordinary rules**, and a synthetic score fixture checks
the single-forward-call contract. Neither is a trained System One model or
evidence of accuracy, calibration, scientific validity or savings.

## Concrete work queue

1. **Engineering, this slice:** source controls, actual SDK and native Cairn
   enrollment compatibility, standalone reproduction and retained failures.
2. **Engineering, next endpoint gate:** bind one approved generative service to
   `code_small`/`code_large`; verify exact model/version/precision, API behavior,
   concurrency, accounting, outages and budget bounds. Keep System One advisory
   so training a classifier does not block the first useful classroom pilot.
3. **Decision-model qualification:** choose a pinned local artifact; freeze
   non-sensitive cases/labels; compare rules, typed model and current LLM route
   on coverage/error/abstention, downstream quality, latency and total cost.
   Calibrate before exposing probabilities. Rozhin is a prospective engineering
   reviewer; no external assignment or commitment is inferred. Do not train on
   learner records by default.
4. **Classroom delivery:** reuse Waypoint/Cairn notebook → optional help/no-AI →
   save → explicit submission → receipt/reopen. Prior browser evidence is
   separate from this SDK slice. Institutional login, supported host/images,
   approved model service and human walkthrough remain gates. A pre-provisioned
   host may precede automated Outfitter placement; expiry/cleanup stays open.

Keep colony/NAIRR experiments separate. Later comparisons retain five matched
arms, common model/data/resource access, and retries, failed work, preparation,
coordination and reviewer costs. No scientific advantage is claimed here.

## Reproduction and evidence

In the pinned Portage checkout, Python 3.11+ and stdlib suffice:

```sh
python3 integrations/ai_pilot/decision_demo.py
```

Four finite loopback requests, seven controls, owned-server/state cleanup,
typed advice, three actual synthetic inference transports, zero external model
calls. No credentials or model downloads. Full tests use existing `uv.lock`.

Final source pins, environment locks, passed/failed/skipped checks and artifact
hashes live in `system-one-pilot-v1-validation.json`. Historical evidence stays
unchanged. No production deployment, merge, paid inference or learner data.
Portage draft PR is deferred because its existing PR workflow invokes a paid
model reviewer. Local delivery and ordinary human review are ready separately.

## Verified delivery

- Portage `709f5aba85dd2e56f87e9f5c32a2ac7438268ee5`, pushed: 539 passes,
  six unavailable sibling-contract checks skipped; 175 existing synthetic
  admission/qualification controls pass. All three profile-render checks pass.
- Belay-classroom `c5a27073e74b9eeb7ab697190915378b50132883`, pushed:
  1,138 broad-suite passes with 22 explicit environment-dependent skips;
  22/22 freshly exported native enrollment checks and 28/28 actual SDK/shadow
  checks pass separately. Lint, formatting and mypy pass.
- Standalone decision demo: seven controls pass, three loopback inference
  transports, zero external model calls. All owned demo services/state cleaned.
- Broad-suite skips cover unavailable local PostgreSQL, PowerShell, sibling
  verifier contracts, real LLM evaluation, and the two separately tested native
  enrollment cases. These are recorded, not reclassified as passes.
- Initial score-overflow, refusal-accounting, qualification-handler and lint
  failures are fixed and retained. One broad run reused expiring 120-second
  native snapshots and produced two refusals. Verification now uses the existing
  separate broad and fresh-native gates; no deadline or product rule was weakened.

Software is ready for a **synthetic shadow walkthrough**, not a trained-model
trial or live classroom deployment. Hosted CI and local checks remain separate
in the JSON; no component is merged or deployed by this delivery.
