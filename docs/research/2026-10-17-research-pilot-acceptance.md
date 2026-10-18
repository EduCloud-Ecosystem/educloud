# Research pilot acceptance — 17 October 2026

**P0 local baseline, P1 portability/recovery, and source-runtime builds: accepted
and merged within their recorded scopes.** Independent human reproduction and
source-environment promotion remain **NOT RUN**. This record freezes the research-workspace release separately
from earlier course-workspace and AI pilot evidence. Public/synthetic data only;
no cloud provisioning, new subscription, production deployment or private-data
approval is established by these results.

## Accepted revisions

Merge status and the final Waypoint CI run were rechecked through GitHub on
October 17. A merge revision identifies the accepted main history; the tested
head identifies the implementation that produced the linked evidence.

| Component | Accepted PR | Tested head | Merge revision |
| --- | --- | --- | --- |
| Outfitter | [#6](https://github.com/EduCloud-Ecosystem/outfitter/pull/6) | `8542f092f9f4058c38c7b77ca019cd47803e0627` | `4275d1a07737baa612a0ebb39e7bdcf2a6ef42a0` |
| Waypoint | [#26](https://github.com/EduCloud-Ecosystem/waypoint/pull/26) | `da4c65530b4ec34676823a466cdce475612fd0fe` | `8506baefb530a81d2d41d2e508a3f346c9afa953` |
| EduCloud | [#13](https://github.com/EduCloud-Ecosystem/educloud/pull/13) | `7910be8fe8caf7e0ddc6a8db34490e124b3328ff` | `cd6d80c73f4a8d99e1fbaae7176fb03a0632f25c` |

Waypoint's final [CI run 39072775659](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39072775659)
passed both `controls` and `actual-docker` at the tested head above. The controls
log records 57 tests. Its workflow pins Outfitter `8542f09` and the runtime
references below. Outfitter's [Go/Docker CI](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39071072229)
also passed. EduCloud #13 supplies the component contract; it is not runtime
acceptance evidence.

## Runtime identity and workload

| Runtime | Immutable reference | Platform evidence |
| --- | --- | --- |
| Python | `python@sha256:229a2c5bfa27522db7815ea81f9bed70af17ccb9de9fc7ad142b1877b5830d36` | Local image inspected as `linux/arm64` on October 17. |
| R | `r-base@sha256:fa1972f31def171b83e0911e947ab8b57db143f0fc8a67af4c0d5ac329041646` | Local image inspected as `linux/arm64` on October 17. |

These are existing immutable images, not clean builds from captured source.
Other architectures require their own identity/execution evidence. The baseline
uses reviewed descriptive group summaries with baseline and trimmed conditions:
1 CPU, 256 MiB, 64 PIDs, 30 seconds, 65,536 output bytes, no workload network,
non-root execution and read-only inputs/recipe. Means use relative tolerance
`1e-12` and absolute tolerance `1e-9`; group names, counts and conditions match
exactly. These checks establish recipe behavior, not scientific validity.

## P0 acceptance matrix

| Criterion | Result | Evidence and limit |
| --- | --- | --- |
| Two projects and reviewed Python/R results | **PASS** | [Final HTTP/Docker report](https://github.com/EduCloud-Ecosystem/waypoint/blob/da4c65530b4ec34676823a466cdce475612fd0fe/research-workspace/evidence/2026-10-17/http-docker-verification.json): 41 checks; fixture results independently recomputed. |
| Access, duplicates, finite budget, cancellation and interruption | **PASS** | [57 local/unit controls and verification boundaries](https://github.com/EduCloud-Ecosystem/waypoint/blob/da4c65530b4ec34676823a466cdce475612fd0fe/research-workspace/VERIFICATION.md), plus actual HTTP controls. Tests do not substitute for hosted identity acceptance. |
| Owned Docker cleanup, broker loss and concurrent reservations | **PASS** | [27 actual Docker checks](https://github.com/EduCloud-Ecosystem/outfitter/blob/8542f092f9f4058c38c7b77ca019cd47803e0627/docs/DOCKER-ACCEPTANCE-2026-10-17.json). Simulated provider controls separately cover ambiguous creation and cleanup failure. |
| Unknown accounting stays reserved | **PASS** | Outfitter regression tests reject partial charges and reattribution; ambiguous late creation retains a liability. No uncertain refund or automatic replay. Full ceiling charges are conservative estimates, not measured CPU or provider settlement. |
| Browser and downloaded bundle | **PASS** within observed scope | [23 browser checks](https://github.com/EduCloud-Ecosystem/waypoint/blob/da4c65530b4ec34676823a466cdce475612fd0fe/research-workspace/evidence/2026-10-17/browser-verification.json). Browser evidence preceded later receipt/R parsing fixes; final automated checks cover those backend changes. |
| Failed control remains inspectable | **PASS** | [Initial R failure](https://github.com/EduCloud-Ecosystem/waypoint/blob/da4c65530b4ec34676823a466cdce475612fd0fe/research-workspace/evidence/2026-10-17/initial-r-failure.json) retained after the bounded file-descriptor limit changed from 128 to 1,024. It remains failed and charged. |
| General accepted CSV spelling in both runtimes | **PASS** | Merge review fixed R group coercion (`001`, `NA`, `NULL`) and a shared decimal grammar. Actual corrected Python/R checks are in the final HTTP report. |
| Independent second operator on a second machine | **NOT RUN** | [Waypoint #28](https://github.com/EduCloud-Ecosystem/waypoint/issues/28). Local agent/CI evidence is not independent human reproduction. |
| Live Jetstream2 execution/provider acceptance | **NOT RUN** | Read-only preflight and mocked worker controls are separate; no live worker, settled native-SU ledger or independent cloud cleanup acceptance. |

The Docker watchdog survives submitting-process loss. Loss of the host,
watchdog or daemon is not provider self-expiry. The explicit supervised-reaper
exception remains visible in every admitted request and receipt.

## P1 accepted implementation and bounded evidence

Both P1 PRs merged after scoped independent review and passing final CI. This
accepts the portable/recovery implementation within its local contract; it does
not close the clean-build, independent-human, hosted or live-provider gates.

| Component | Accepted PR | Tested head | Merge revision |
| --- | --- | --- | --- |
| Outfitter | [#7](https://github.com/EduCloud-Ecosystem/outfitter/pull/7) | `5827c84e9952cc67b85e91ceff4282e0ead6923b` | `abfcfa280a0982e03b80a50e0349a5ef99a13a41` |
| Waypoint | [#30](https://github.com/EduCloud-Ecosystem/waypoint/pull/30) | `d09cb2fa6824a1baeb4ed9104dd055d6b1d0480e` | `8a3e87c3cc37389de9f8e682810f3fde8966b754` |

Waypoint's implementation commit is
`bf275dd25e9c586c0b8d838b15687000c161e86f`; the tested head above adds the
[acceptance packet](https://github.com/EduCloud-Ecosystem/waypoint/blob/d09cb2fa6824a1baeb4ed9104dd055d6b1d0480e/research-workspace/evidence/2026-10-17/p1/acceptance.json).
[Waypoint CI 39074042397](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39074042397)
passed controls and actual HTTP/reproduction/recovery at that head.
[Outfitter CI 39073655503](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39073655503)
passed at `5827c84`. These are accepted revisions and evidence, not an assertion
that every service acceptance criterion has passed.

| Work | Result and evidence | Boundary |
| --- | --- | --- |
| Broker checkpoint/held restore/fenced activation | **PASS**: `3e5de0b` recorded 38/38 local CLI/Docker checks in 16.942 seconds, zero observed accounting loss. [Sanitized report](https://github.com/EduCloud-Ecosystem/outfitter/blob/5827c84e9952cc67b85e91ceff4282e0ead6923b/docs/evidence/2026-10-17-local-recovery.json); full Go race suite/vet passed. Final `5827c84` CI also passed. | Same-host source-fenced cutover; source loss remains unsupported for activation. The original local report keeps its tested revision. |
| Recovery special-file correction | **PASS**: `5827c84` rejects FIFO/device inputs before blocking; targeted recovery race controls/vet passed. Independent exact CLI reproduction exits 2 with no destination. | Correction covers the later input-handling change; the prior Docker report is not relabelled as a new local run. |
| Reviewed environment catalog and service controls | **PASS**: 119 unit controls at final Waypoint code; source hashes match the retained reports. Environment catalog pins dependencies, runtime/platform, recipe hashes, limits and explicit missing build provenance. | Existing-image execution is not a source build. |
| Actual research HTTP workflow | **PASS**: [41 final HTTP/Docker checks](https://github.com/EduCloud-Ecosystem/waypoint/blob/d09cb2fa6824a1baeb4ed9104dd055d6b1d0480e/research-workspace/evidence/2026-10-17/p1/http-docker-verification.json), all recorded runs cleaned up. | Public/synthetic local workflow using final broker `5827c84`. |
| Selected historical bundle replay | **PASS**: [two real local Docker reproductions](https://github.com/EduCloud-Ecosystem/waypoint/blob/d09cb2fa6824a1baeb4ed9104dd055d6b1d0480e/research-workspace/evidence/2026-10-17/reproduction/report.json); original failed R run was not selected and remains **NOT RUN** for replay. The two new runs cleaned up and charged their combined 60 CPU-second allowance. | Automated repeatability in the same operator environment. Historical recipe bytes retained; no independent human or source-image rebuild claim. Adjacent verification records binary/source/catalog hashes. |
| Coordinated workspace recovery | **PASS**: [25 final local checks](https://github.com/EduCloud-Ecosystem/waypoint/blob/d09cb2fa6824a1baeb4ed9104dd055d6b1d0480e/research-workspace/evidence/2026-10-17/p1/recovery-verification.json), restore step **0.773 seconds**, total exercise **14.193 seconds**. Zero completed records or immutable artifacts lost at the frozen point; pending work cancelled without replay. | Includes an explicitly injected interruption after source access was sealed. Both applications refused service until same-pair retry. No approved hosted recovery target or source-loss/remote recovery claim. |
| Catalog browser flow | **PASS** within observed scope: 17 checks, including two explicitly simulated cases; no compute was dispatched during that browser pass. | Distinct from the actual HTTP/Docker execution and earlier 23-check browser baseline. Manual screen-reader and second-user acceptance remain open. |
| Clean Python/R builds from pinned source | **PASS**, subsequently accepted in #31 | See the source-build addendum below. Four candidates remain disabled; this does not change the historical P1 evidence above. |
| Independent second operator/machine | **NOT RUN** | [Waypoint #28](https://github.com/EduCloud-Ecosystem/waypoint/issues/28). CI and same-operator replay do not replace this exercise. |
| Hosted identity, retention/deletion, total storage limits and capacity | **NOT RUN** for the research workspace | [Waypoint #29](https://github.com/EduCloud-Ecosystem/waypoint/issues/29). Course-workspace controls do not automatically qualify this separate service. |

Earlier working-tree observations (111 controls and a 0.257-second restore step)
were provisional. The final pinned acceptance figures above supersede them for
this release; they are not added together or presented as separate coverage.

Unknown/running jobs are retained in held restores. Source reconciliation and a
fresh matching checkpoint with no active/unresolved liabilities are required
before broker activation. The source becomes permanently non-admitting before
the replacement admits jobs. Without the current source, recovery stays held.
Waypoint additionally owns current membership/configuration/artifact checks,
source service retirement, invalidating restored sessions and fresh credentials.

## Source-build acceptance addendum

Waypoint [#31](https://github.com/EduCloud-Ecosystem/waypoint/pull/31) merged as
`adc44643c4e055046beb6db73d5a95ee07956f55`, from reviewed head
`5f98c068c2ec0b372fc098c8cc15063d75e1b38f`. The merged tree matches that reviewed
head. All 136 controls passed in the review; the final-head
[CI run 39077046829](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39077046829)
and [post-merge CI 39090945694](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39090945694)
passed the ordinary controls and actual Docker workflow. Source construction
was not rerun by those ordinary CI jobs; its separate evidence is below.

| Criterion | Result and bounded evidence |
| --- | --- |
| Pinned runtime source construction | **PASS**: Python 3.12.15 and R 4.6.1 built from captured source on native ARM64 and AMD64. Debian/compiler binaries were inherited, not rebuilt. [Source-build acceptance packet](https://github.com/EduCloud-Ecosystem/waypoint/blob/5f98c068c2ec0b372fc098c8cc15063d75e1b38f/research-workspace/evidence/2026-10-17/source-builds/acceptance.json) pins source/base/package/platform identities and artifact hashes. |
| ARM64 construction and probes | **PASS with retained failed controls**: one construction of each runtime; the original R probe failed, and a separate probe recheck verified those same images. The recheck is not a second build. A later builder-start deadline failure remains recorded. |
| AMD64 construction | **PASS**: a fresh build/qualification after the initial R probe failure, at `7a84e1a0cb22f5074618e267c023f5cd7562b032` in [CI 39075522315](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39075522315). The earlier failed attempt remains recorded. |
| Two projects, runtimes and conditions | **PASS**: 49 qualification checks per platform; eight successful matrix runs per platform. Three supplemental successful runs and one expected refusal remain separately identifiable. Counts/groups/conditions match exactly; mean tolerance remains relative `1e-12`, absolute `1e-9`. |
| Lineage and historical evidence | **PASS**: input, recipe, parameter and environment changes are separately traceable; two selected historical rows replayed successfully. Original failed runs and the rejected initial lineage comparison remain inspectable. |
| Distribution and exact future replay | **NOT RUN** as a durable distribution service: CI images are ephemeral; manifests/logs/digests are retained. Exact replay requires retaining/importing the exact image or a separately reviewed distribution path. Rebuilds may produce new identities. |
| Human reproduction and promotion | **NOT RUN**: automated second-machine evidence does not replace an independent human. All four source environments remain disabled for normal admission, dispatch and replay. |
| Documents-directory replay | **FAIL**, preserved: the original run stalled and its saved receipt reported unknown cleanup. The supplemental observation in merged [#32](https://github.com/EduCloud-Ecosystem/waypoint/pull/32) finds the exact container ID/name absent and the matching ledger cancelled, cleanup verified, unresolved liability false, and 30 CPU-seconds conservatively charged. The original failed execution and saved receipt are unchanged. No refund or shared Docker restart occurred. |

The [retained evidence guide](https://github.com/EduCloud-Ecosystem/waypoint/blob/5f98c068c2ec0b372fc098c8cc15063d75e1b38f/research-workspace/evidence/2026-10-17/source-builds/README.md)
explains each failure and image-identity limitation. Issue #27 is closed for its
source-build scope; #28 and #29 remain separate human/operations gates. Native
architecture timings come from different hosts and are not a performance comparison.

The [supplemental reconciliation](https://github.com/EduCloud-Ecosystem/waypoint/blob/2d7ee8529668e523fb12d1f6c1e8a739e36455a2/research-workspace/evidence/2026-10-17/replay-cleanup-reconciliation/README.md)
was reviewed at `2d7ee8529668e523fb12d1f6c1e8a739e36455a2` and merged as
`bc5d2fa147dd0ce2dd43a3a10d691aa028e8a5dd`; its
[CI 39091299294](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39091299294)
passed. It binds the later observation to the original request/run/image and
artifact hashes. The ledger timestamp is not an independently observed cleanup
time, and the inspecting process does not claim to have performed the cleanup.

## Native accounting and cleanup implementation acceptance

Outfitter [#8](https://github.com/EduCloud-Ecosystem/outfitter/pull/8) merged as
`534dcf187158a28008fa07d3bb05c00f27b88165` from final reviewed head
`07e8e5001b3db5569678b3c552d624d7348ff3d6`. Its
[final CI 39091365693](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39091365693)
passed 115 tests/subtests, 26 Docker checks and 38 recovery checks. These are
final CI results; the earlier retained local report remains tied to its own
implementation revision and records 27 Docker checks, not a new final-head run.

The [independent-review record](https://github.com/EduCloud-Ecosystem/outfitter/blob/07e8e5001b3db5569678b3c552d624d7348ff3d6/docs/evidence/2026-10-17-pr8-independent-review.json)
retains both original findings and their regression controls. A deadline after
recording a known port no longer permanently misclassifies that known effect as
an unknown creation. Cleanup now requires explicit non-null empty attachment
inventory during discovery and the fresh check before deletion. Missing storage
evidence refuses deletion and retains liability. Independent re-review passed.

The native journal and supervisor use the existing durable authority/ledger,
preserve request/attempt ownership, and keep native SUs separate from local
CPU-seconds. [Fault-injection evidence](https://github.com/EduCloud-Ecosystem/outfitter/blob/07e8e5001b3db5569678b3c552d624d7348ff3d6/docs/evidence/2026-10-17-native-su-cleanup.json)
covers lost creation responses, separate-process cleanup after creator loss,
late effects, API loss, foreign resources, incomplete inventory and held recovery.
These provider controls use a local HTTPS OpenStack simulator. Real Docker and
local recovery evidence are separate. Deletion, cancellation and observations
do not by themselves settle or refund native reservations.

Live allocation/capacity/image/network preflight, independent-host supervisor
acceptance, provider creation/workload/teardown and provider settlement all remain
**NOT RUN**. The [proposed live manifest](https://github.com/EduCloud-Ecosystem/outfitter/blob/07e8e5001b3db5569678b3c552d624d7348ff3d6/docs/manifests/jetstream2-live-test.proposed.json)
is an incomplete decision input, not permission to provision. No hard provider SU
cap or guaranteed expiry during API/host/supervisor outage is established. Ben's
existing assignments and broader live acceptance criteria remain unchanged.

## Optional inference implementation acceptance

Portage [#10](https://github.com/EduCloud-Ecosystem/portage/pull/10) and
[#11](https://github.com/EduCloud-Ecosystem/portage/pull/11) were reviewed, corrected
and merged in dependency order. The foundation brings the existing finite pilot
gateway into main; the qualification increment preserves the public API and
requires explicit selection of one local path. No default route changed.

| PR | Final tested head | Merge revision | Final-head checks |
| --- | --- | --- | --- |
| #10 | `c080530ce507611ea7d0cee1ed88143a798410ce` | `cf41ddedc7b9c5710a707365ccf7c5a8a9b5b7ad` | [CI 39091086027](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39091086027), gate passed; paid review skipped. |
| #11, retargeted to accepted main | `5aa8cf5d80b9b037f57768cdbd27aeb958299017` | `a3a4a6e5801a74fed45ae1bfab341c5db4ab45e2` | [Full-suite CI 39091314955](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39091314955) and [qualification CI 39091314970](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39091314970) passed; paid review skipped. |

Review corrected three false-positive evidence paths: incomplete readiness text
such as `NOT RUN`, skipped selected controls, and missing/invalid resident-memory
measurements cannot satisfy their corresponding gates. Paid model-based CI
review now requires an explicit opt-in. The final local suite passed 225 tests
with six existing integration skips. Those skips do not establish runtime or
integration acceptance.

The [retained qualification record](https://github.com/EduCloud-Ecosystem/portage/blob/5aa8cf5d80b9b037f57768cdbd27aeb958299017/docs/qualifications/2026-10-17-direct-local-review-controls.json)
contains **95 passing synthetic controls** and **12 runtime gates NOT RUN**.
It retains the source revision/hashes at collection; it is not rewritten to claim
collection at the later merge. All six retained source-file hashes were checked
against the final head and match. These controls use deterministic loopback servers,
not an actual model. They cover current attribution/membership, destination/model
refusal, finite allowances and concurrency, streaming/non-streaming failure,
cancellation and retained liabilities. Unknown work retains both its reserved
tokens and concurrency slot until evidence-backed reconciliation.

The [capacity protocol](https://github.com/EduCloud-Ecosystem/portage/blob/5aa8cf5d80b9b037f57768cdbd27aeb958299017/docs/specs/direct-inference-qualification.md)
prepares a maximum 16-attempt synthetic workload. An approved existing host,
permitted installed model/template, operator, resource limits and finite window
are still required. No engine was started, model acquired, live inference run,
production deployment performed or default route changed. An offline review
packet is the next increment; it cannot itself authorize execution or spending.

## Synthetic consumer bridge and offline decision packet

Two further implementation increments merged after independent review and final
CI. They close local engineering gaps, not live-provider or real-course gates.

| Component | Final reviewed head | Merge revision | Final-head evidence |
| --- | --- | --- | --- |
| Outfitter [#9](https://github.com/EduCloud-Ecosystem/outfitter/pull/9) | `2438cd1e93c06d4f09e549f2e750769c51df2373` | `273bb0148fead33c91fcb92e0cc9e0bacdb929c2` | [CI 39092556586](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39092556586): 156 tests/subtests, 26 Docker, 38 recovery and 19 consumer checks passed. |
| Portage [#12](https://github.com/EduCloud-Ecosystem/portage/pull/12) | `d3d117930285d8f7cd002d16e9b9f12e6067e90a` | `577fdb9a40239b98ba63dcd4676cb8e5213b23f4` | [Full-suite CI 39092275619](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39092275619) and [qualification CI 39092275617](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39092275617) passed. Local validation: 61 focused packet tests and 286 total tests passed, with six existing integration skips. Paid review skipped. |

Outfitter's [consumer contract](https://github.com/EduCloud-Ecosystem/outfitter/blob/2438cd1e93c06d4f09e549f2e750769c51df2373/specs/13-synthetic-consumer-handoff.md)
binds one synthetic consumer/project/job to immutable submission, policy, content,
image and limit identities in the existing ledger. Duplicate delivery returns
the same receipt; changed bindings conflict; unknown work cannot redispatch.
Read-only status remains available after client loss and in held/fenced states.
The actual Docker fixture checks deterministic correct/incorrect outcomes but
does not publish grades or integrate the production Cairn Runner. Independent
review found a bare parent-path validation gap that consumed an attempt before
refusal; [the fix and regressions](https://github.com/EduCloud-Ecosystem/outfitter/blob/2438cd1e93c06d4f09e549f2e750769c51df2373/docs/evidence/2026-10-17-consumer-review.json)
now refuse it before reservation. The original failed control is retained.

Portage's [offline packet](https://github.com/EduCloud-Ecosystem/portage/blob/d3d117930285d8f7cd002d16e9b9f12e6067e90a/docs/specs/direct-inference-qualification.md#offline-capacity-review-packet)
verifies one externally hash-pinned public record and explicit bounded artifact
references. It preserves the original 95 synthetic controls, all 12 runtime gates
NOT RUN, tested source/model identities, failures/skips and unknown liabilities.
The example exposes 32 missing capacity/cost fields. Field completeness never
grants execution, promotion, spending or hosted readiness. No engine, qualifier,
gateway or ledger is opened by packet generation; no network or subprocess runs.
Actual host/model/operator evidence is still required for a live decision.

The subsequent Cairn adapter and inference operator packet are recorded below.
Waypoint's subsequent local synthetic identity acceptance is recorded below.
Production Cairn wiring, live Jetstream2/inference, source-image promotion,
private-data admission and purchases remain outside this acceptance.

## Disposable Cairn consumer acceptance

Cairn [#32](https://github.com/EduCloud-Ecosystem/cairn/pull/32) merged as
`bb41bdaffe7a9ec9feb1b8fdcdcbbdda527b20f8` from reviewed final head
`2aa674ec42478ce6f0ca622e3267c65475d96784`; the merge tree matches that head.
All eight final checks passed across [main CI 39094293017](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39094293017),
[recovery CI 39094293038](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39094293038)
and [synthetic consumer CI 39094293023](https://github.com/EduCloud-Ecosystem/cairn/actions/runs/39094293023).

The separate opt-in command implements Cairn's Runner/PolicyRunner interfaces
against pinned Outfitter `273bb0148fead33c91fcb92e0cc9e0bacdb929c2`. Durable intent
precedes the single dispatch; repeated calls use status only. Cairn proposes a
result only from a complete matching receipt with verified cleanup/accounting.
Unknown execution or missing diagnostics return no result, not a zero grade.
It never stores a Grade or changes the running service, retry defaults, schema
or production configuration. The [integration contract](https://github.com/EduCloud-Ecosystem/cairn/blob/2aa674ec42478ce6f0ca622e3267c65475d96784/docs/synthetic-outfitter.md)
explicitly prohibits installing this adapter into the current production retry
path, which lacks the required stable job context.

The [local evidence](https://github.com/EduCloud-Ecosystem/cairn/blob/2aa674ec42478ce6f0ca622e3267c65475d96784/docs/evidence/2026-10-17-synthetic-outfitter.json)
retains 19/19 passing Docker controls at implementation `48476e6`, five sequential
workloads under a 150 CPU-second ceiling and a separate budget refusal. The
wrong-answer control remains wrong despite successful execution. The
[independent review](https://github.com/EduCloud-Ecosystem/cairn/blob/2aa674ec42478ce6f0ca622e3267c65475d96784/docs/evidence/2026-10-17-synthetic-outfitter-review.json)
retains three reproduced and fixed findings: blocking special-file reads in the
runner and CLI, and cancellation discarding an unresolved cleanup receipt.
Rechecks passed; per-job cleanup failures and liabilities remain visible.
Final-head CI is separate from the earlier pinned local report. Production
service wiring is not implemented. Live provider, real course data and a second
human operator remain NOT RUN.

## Inference operator decision prepared

The accepted offline packet was used to prepare a concrete operator brief from
eight pinned local input files. The read-only inventory at 20:18 Pacific on
October 17 found an Ollama executable, no default-port listener and no models in
the default or explicitly configured inventory inspected. It did not survey
other hosts, unrelated engines or unconfigured locations. Hardware inventory is
not evidence of approved available capacity or model fit.

The brief retains 95 synthetic passes, all 12 runtime gates NOT RUN and 32 missing
capacity/cost fields. The proposed workload remains at most 16 attempts within a
separately chosen window of at most 30 minutes. The needed choices are an existing
approved host and permitted installed model, its accountable operator and limits,
and a later bounded execution window. Deferral is the no-spend option. The
subsequently confirmed metadata/dispatch expiry gap is fixed in PR #13, recorded
below; the existing packet remains a historical snapshot. No engine start, acquisition,
model request or spending occurred in preparing the brief.

The local operator packet is retained separately from this public repository.
The reviewed brief SHA-256 is
`fed24abae27d2536231e0c8dc4300fcad4ce08c994126842052d8636204ec90d`;
the machine packet containing all eight input hashes has SHA-256
`3637cf01a9b08ac64cb0112e0eb31cbc7e3b692373d8d7337c84d6a1cb6fec9a`.
These identify the bounded inventory snapshot, not current capacity or approval.

## Local synthetic identity acceptance

Waypoint [#33](https://github.com/EduCloud-Ecosystem/waypoint/pull/33) merged as
`8bb8e41575aee399a62989be561e4252482a2435` from final reviewed head
`264f8591baef6c71bf4f3a76d8a4e9b748448834`.
[Ordinary CI 39095546967](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39095546967)
passed controls and actual Docker checks; the clean-source-build job was
**SKIPPED**, not rerun or promoted by this change.

The separate synthetic OIDC mode uses current issuer/subject membership checks
at request, dispatch, execution and publication. Key-mode fallback and forged
identity headers are refused. Revocation, provider outage, logout and local
replacement preserve denial, actual receipts and conservative charges.
The [retained evidence](https://github.com/EduCloud-Ecosystem/waypoint/blob/264f8591baef6c71bf4f3a76d8a4e9b748448834/research-workspace/evidence/2026-10-17/oidc-pilot/README.md)
distinguishes these observations:

| Evidence | Result and boundary |
| --- | --- |
| Full local browser/service run | **PASS**, 74 checks at `b818d02`; all 18 application/static/recipe files match the final candidate. Four identities, two projects, actual Python/R, active revocation, outage, replacement and bounded keyboard journeys. |
| Later observer-cleanup correction | **PASS**, two regression tests within 158 offline controls. The harness now prevents late pause and attempts exact-owned unpause even when teardown raises. This patch was not part of the earlier full browser run. |
| Provider logout supplement | **PASS**, seven separate checks after the exact confirmation route was added. The original 403 failure remains visible; it is not counted in the earlier 74-check run. |
| Visual/export review | Desktop/mobile screenshots inspected, no mobile horizontal overflow, and downloaded synthetic export validates with cancelled/missing-result gaps. Automated keyboard activation is not full manual accessibility acceptance. |
| Owned cleanup/accounting | Four exact stacks/networks/volumes and owned workloads absent. Final pilot retains 210 CPU-seconds, earlier attempts 120; copied replacement rows are not double-counted. Private state/images remain retained. |
| Failed attempts and prior evidence | Initial realm/harness, token-lifetime, provider-readiness and logout-route failures remain retained. All 79 frozen source-build evidence files and the original failed replay record remain unchanged. |
| Broader acceptance | Hosted identity, real/private data, manual screen-reader/focus-order acceptance, independent human reproduction, whole-store limits, retention/deletion and off-host recovery remain **NOT RUN**. Source candidates remain disabled; issue #29 stays open. |

## Approval expiry correction

Portage [#13](https://github.com/EduCloud-Ecosystem/portage/pull/13) merged as
`11438edec07ee7699a0c96e88a8fb5af60ec7348` from reviewed final head
`bf4c51c112de5f45600ad76d4796016b0abeea88`.
[Qualification CI 39095235012](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39095235012)
and [full-suite CI 39095235011](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39095235011)
passed; paid automated review was **SKIPPED**.

Deterministic delayed-metadata controls first reproduced dispatch after expiry
and insufficient remaining request headroom. The correction rechecks after
metadata, inside the reservation transaction after lock waits, and after connect
immediately before engine dispatch. A monotonic deadline prevents wall-clock
rollback from extending approval; transport timeouts respect remaining time.
Expiry after admission preserves the full unknown reservation and concurrency
slot. Interrupting a socket does not prove remote work stopped.

The [separate expiry evidence](https://github.com/EduCloud-Ecosystem/portage/blob/bf4c51c112de5f45600ad76d4796016b0abeea88/docs/qualifications/2026-10-17-expiry-controls.json)
records **17 passing synthetic controls** and the two original reproduced
failures at implementation `2343c654` under Python 3.12.13; all five recorded
source hashes match the final head. The full suite passed **303 tests**, with
six existing sibling-contract integration skips. The original **95 synthetic
controls and all 12 actual-engine gates NOT RUN** are unchanged. No real model
request, engine start, download, spending or default routing change occurred.

## Storage inventory and bounded broker output

The two foundation PRs below are accepted separately from whole-store admission.
Their merge trees match the reviewed heads. Neither installs a quota policy,
migrates an accepted store or authorizes deletion; issue #29 remains open.

| PR | Reviewed head | Merge revision | Final-head CI |
| --- | --- | --- | --- |
| Waypoint [#34](https://github.com/EduCloud-Ecosystem/waypoint/pull/34) | `efeb53ac5eb10c878c286d521ccd1498908d0950` | `a769dd86594a8791e4ec6777b38a92940a31fc18` | [39096829512](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39096829512): 176 total offline tests, 41 HTTP/Docker checks and historical replay/recovery passed. Source-build job **SKIPPED**. |
| Waypoint [#35](https://github.com/EduCloud-Ecosystem/waypoint/pull/35) | `714178b050e4f3e684101953b0fb7e7c988f2283` | `2a7d6cd08ce7881a5ea36d761e53fc0c6f0e4b71` | [39097535850](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39097535850): 184 total offline tests, 41 HTTP/Docker checks and historical replay/recovery passed. Source-build job **SKIPPED**. |

PR #34 adds 18 inventory tests within its full-suite total. The read-only
`storage-status` and `retention-plan` commands inventory SQLite/WAL/SHM, broker
authority/output, directories, temporary and unknown files without opening the
original database. Ambiguous-schema and incomplete-receipt findings were fixed
before acceptance. Successful settled artifacts from closed projects can only
be human review candidates. Uncertain authority and failed/unresolved work stay
protected; no deletion command or scheduler exists.

The [stopped synthetic-store observation](https://github.com/EduCloud-Ecosystem/waypoint/blob/efeb53ac5eb10c878c286d521ccd1498908d0950/research-workspace/evidence/2026-10-17/storage-inventory/README.md)
recorded **163,779 logical bytes and 82 filesystem entries**, all protected, with
zero review candidates. Source hashes match the reviewed implementation; both
reports agree on inventory hashes. Content and captured device/inode/mode/link
count/size/mtime/ctime matched before and after. Reads may update access times.
This is not a capacity measurement or a guarantee against subsequent changes;
`quota_enforced` and `deletion_authorized` remain false.

PR #35 adds eight real subprocess tests for exact output caps, endless
stdout/stderr with bounded traced memory, quiet/closed-pipe processes, callback
failure and deadline checks. An independent review found a late-callback
acceptance gap; it was corrected before merge. The process helper drains both
pipes incrementally and continues identity/cancellation checks. Deadline bounds
acceptance; caller return can include the bounded callback plus up to five
seconds of observer teardown. Stopping the observer does not prove provider
cleanup and cannot refund unknown execution.

These CI runs did not repeat the full OIDC browser exercise. Prior source-build,
replay reconciliation and OIDC evidence plus the catalog are
byte-unchanged. The four source candidates remain disabled. Whole-store durable
reservations, authority/settlement headroom, all-writer admission and recovery
destination capacity remain unfinished. Hosted/private-data, human accessibility,
independent operator and institutional retention gates remain **NOT RUN**.

## Blocked cloud operator packet

Outfitter [#10](https://github.com/EduCloud-Ecosystem/outfitter/pull/10) merged as
`afc4fe82ee368261d7662b380bf9f611b31aa182` from reviewed head
`3085e8f33350b6ce558a254cfdb7bc3de7f4c1b6` after independent design review and
passing [CI 39096489315](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39096489315).
The [operator packet](https://github.com/EduCloud-Ecosystem/outfitter/blob/3085e8f33350b6ce558a254cfdb7bc3de7f4c1b6/docs/JETSTREAM2-OPERATOR-DECISION.md)
and rescue candidate are accepted as documentation only. JSON invariants,
28 local links and whitespace checks passed; the older proposed live manifest
is unchanged. Live preflight was **NOT RUN**.

The packet retains unselected allocation, resource pins, operator and cleanup
host. Its proposed one-worker 1 SU allowance is a local reservation, **not** a
provider-enforced maximum charge. Independent-host cleanup, terminal late-effect
evidence and settlement remain unresolved engineering/operational gates.
The subsequent offline rescue implementation is accepted below; no live provider
effects or independent-host acceptance are implied. Ben's assignments stay
unchanged and Docker remains the baseline.

## Simulated independent cleanup handoff

Outfitter [#11](https://github.com/EduCloud-Ecosystem/outfitter/pull/11) merged as
`e34604ce2e4ab25c23366a8bea49683899425553` from reviewed final head
`73ae1ab4aae941cf87de03f745820166e44e7784`.
[Final CI 39098498344](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39098498344)
passed **376 tests/subtests, 26 Docker checks, 38 recovery checks and 19 consumer
checks**. The final local race-suite record belongs to implementation
`2658042f51d9148bd1c89ca59d8f1340c2347d80`; it includes 220 offline rescue
tests/subtests within the 376 total. The final head adds evidence/documentation.

The [implementation record](https://github.com/EduCloud-Ecosystem/outfitter/blob/73ae1ab4aae941cf87de03f745820166e44e7784/docs/JETSTREAM2-OFFLINE-RESCUE.md)
and [structured evidence](https://github.com/EduCloud-Ecosystem/outfitter/blob/73ae1ab4aae941cf87de03f745820166e44e7784/docs/evidence/2026-10-17-offline-rescue.json)
preserve the review and test stages. Forty SIGKILL boundaries exercise separate
source and cleanup processes with private directories on one machine. The
harness makes source state unavailable to fresh cleanup processes. This is
**same-machine process evidence**, not independent-host or physical power-loss
qualification.

Port and server creation each require a signed, durable cleanup acknowledgement
inside the creator. The server phase additionally binds the known port and
parent scope. Immutable executor selection stops the original host from
competing with its designated cleanup observer. Fresh ownership/configuration,
explicit attachment and empty-volume checks precede deletion. The observer has
no budget/admission/settlement authority and no receipt-ingestion path.

Independent review fixed three durability/clock findings: returning a receipt
despite persistence failure, clock rollback during acknowledgement persistence,
and missing parent-directory synchronization. Secondary review found substring
matching accepted signed concatenated outcomes; exact enum matching and signed
invalid-status regressions correct it. Original failing witnesses, harness
mistakes and the intermediate unused-import build failure remain recorded;
earlier passing CI at `6a984fe` is not relabelled as final-head evidence.

Only explicitly injected loopback HTTPS fixture transport is supported. No CLI,
credential discovery, live transport, production wiring or deployment is added.
Observed absence never proves a terminal provider outcome; late effects and
unknown charges remain unresolved. At most 64 retained sweeps are supported;
exhaustion refuses further cleanup while preserving scope. Actual independent
hosts, provider IAM, copied-host takeover, physical power-loss durability, clock
assumptions, live resource access and terminal late-effect handling remain
**NOT RUN or unqualified**. There is no provider-enforced spending cap.

## Hosted inference fixture contract

Portage [#14](https://github.com/EduCloud-Ecosystem/portage/pull/14) merged as
`b2ba332ff5f81ff15c7ada67d5fc2a79b65cde94` from reviewed final head
`2499c9d26f42f322bbfb73a5d49396e607915477`.
[Qualification CI 39098952693](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39098952693)
and [full-suite CI 39098952289](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39098952289)
passed; paid automated review was **SKIPPED**. Local evidence at implementation
`9cf520d4d5383857b4f2214b8a9a2f6ff068289b` under Python 3.12.13 records
**147 new fixture controls and 450 total passing tests**, with six existing
missing-sibling integration skips.

The [pure contract](https://github.com/EduCloud-Ecosystem/portage/blob/2499c9d26f42f322bbfb73a5d49396e607915477/docs/specs/jetstream2-hosted-contract.md)
validates fictional profiles, plans fixed requests, classifies fabricated
responses and emits sanitized evidence. It has no network client, credential
reader, ledger mutation, clock enforcement or live entry point. Even complete
fictional approval fields cannot enable execution. Unsupported response shapes,
duplicate keys, inconsistent/nonfinite usage, model drift, errors and incomplete
responses are refused. Supported above-reservation usage is retained in full
with a stop/bound-failure recommendation; unsupported/uncertain outcomes stay
unknown. Provider-reported usage is not an independent consumption measurement,
and a response hash cannot establish termination or reconciliation.

The [separate evidence](https://github.com/EduCloud-Ecosystem/portage/blob/2499c9d26f42f322bbfb73a5d49396e607915477/docs/qualifications/2026-10-17-hosted-contract-controls.json)
distinguishes pure classification from explicit temporary-ledger regression
harnesses. Gateway, qualifier, ledger, entry points, registry/default routes and
the original 95-control/17-expiry records remain unchanged. All 12 actual local
runtime gates remain **NOT RUN**. Real TLS/DNS, persistent attempt/catalog
ceilings, provider termination, entitlement, model compatibility and resource
bounds remain **NOT RUN or UNVERIFIED**. No hosted selection, credentials,
provider calls, spending or route promotion is authorized.

## Rejected whole-store admission draft

Waypoint [#36](https://github.com/EduCloud-Ecosystem/waypoint/pull/36) merged as
`640fa2d89d9e98be0d0ff8f0fbaae32e83fa74ec` from reviewed head
`9b06e9125dfe59d4c13f9f10191374c2d57ee26a`.
[Final CI 39098780066](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39098780066)
passed accepted controls and actual Docker/replay/recovery checks;
source reconstruction was **SKIPPED**. This accepts documentation and inert
failure evidence only. Application source remains identical to PR #35;
**whole-store quota enforcement is blocked and not implemented**.

The [blocked design and correction sequence](https://github.com/EduCloud-Ecosystem/waypoint/blob/9b06e9125dfe59d4c13f9f10191374c2d57ee26a/research-workspace/STORAGE-ADMISSION-BLOCKED.md)
and [five reproducible witnesses](https://github.com/EduCloud-Ecosystem/waypoint/blob/9b06e9125dfe59d4c13f9f10191374c2d57ee26a/research-workspace/evidence/2026-10-17/storage-admission-blocked/README.md)
retain the rejected three-file draft as a hash-bound inert patch. The draft can
launch after a hold, lose rollback uncertainty, clear an intent after a result
file effect, misclassify active project initialization as stale, and refuse
essential writes after reserved growth becomes observed storage.

Each defect has a comparison control. Exit zero from the offline reproducer
means **the defects reproduced**, not product acceptance. Rollback persistence
uses an in-memory model; the result case injects an oversized internal record;
headroom uses inventory arithmetic with mocked physical free space. Other cases
use disposable SQLite/files with intercepted provider launches. These do not
claim real disk-full/power-loss tests, ordinary-recipe reachability of the
oversized record, or that the quota contract is impossible.

The three dirty implementation files and recovery snapshot remain preserved.
All 121 prior evidence files are unchanged, source candidates remain disabled,
and liabilities/failed controls remain visible. Scoped design review cleared a
narrower durable operation/failure-state implementation in a fresh isolated
worktree while preserving the rejected draft. This is implementation scope,
not acceptance of new code; total writer bounds,
settlement headroom, recovery capacity, migration and quota enforcement are not
accepted by this checkpoint. No user capacity purchase can substitute for those
engineering corrections.

## Offline metadata compatibility

Outfitter [#12](https://github.com/EduCloud-Ecosystem/outfitter/pull/12) merged as
`5700ff52b1182d63f51723dbadb700c488cfc6ac` from reviewed final head
`eec00a969deafe7690c99506871bc6fb42b43974`.
[Final CI 39101128804](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39101128804)
passed **607 tests/subtests**, including 231 compatibility and 220 rescue
controls, plus 26 Docker, 38 recovery and 19 consumer checks. The local uncached
race-suite result belongs to implementation
`eea4fa3302b6d09f5022f32db8ff5d43098d06fc`; later commits clarify documentation
and record evidence. Final-head CI is separate from that local result.

The [contract](https://github.com/EduCloud-Ecosystem/outfitter/blob/eec00a969deafe7690c99506871bc6fb42b43974/specs/15-offline-metadata-compatibility.md)
and [evidence](https://github.com/EduCloud-Ecosystem/outfitter/blob/eec00a969deafe7690c99506871bc6fb42b43974/docs/evidence/2026-10-17-offline-compatibility.json)
bind configuration, native policy, profile and bounded synthetic snapshot with
versioned digests. The evaluator compares exact flavor dimensions, declared
image metadata/minimum resources, and complete normalized security-rule sets.
Missing observations stay distinct from explicit null/zero/empty evidence;
malformed input is rejected. Reports always retain `synthetic_offline`,
`provisioning_enabled: false`, `live_readiness: BLOCKED` and unverified boot.

Five independently reproduced findings were corrected: protocol zero falsely
matching unrestricted traffic, null rule objects becoming empty objects, UTC
year bounds checked before normalization, incomplete-rule alias normalization,
and invalid-text canonicalization. The record retains all five failing review
controls plus the intermediate unused-import build failure. Earlier passing
results are not final acceptance. The documented upstream API prose/source
disagreement does not establish Jetstream2's deployed behavior.

There is no client, environment/filesystem access, clock read, CLI, creator or
ledger integration. Supplied timestamps/completeness are fixture assertions;
metadata matching proves neither boot/host suitability nor effective filtering,
private reachability, capacity or entitlement. Native/rescue behavior, its
64-sweep limit, unknown liabilities and the proposed live manifest are unchanged.
Live engineering, operational and approval gates remain open.

The subsequent scoped implementation was authorized to bind a separate immutable experiment envelope
to authority/account, configuration, native policy and compatibility digests,
request identity, start/expiry, lifetime and native reservation. One total attempt
must be consumed atomically with reservation; settlement, restart and changed
request IDs must not replenish it. Repeated requests remain status-only. Bound
compatibility and expiry must be rechecked before each simulated port/server
create, including after delayed rescue acknowledgement. That authorization did
not establish accepted enforcement; the later #13 acceptance is recorded below.
Native record bounds and both rescue acknowledgements
remain required. No live entry point, credential lookup or guest execution is
included; private guest bootstrap, access and result transfer remain open.

## Fresh operation guard, held recovery and a remaining dispatch failure

Waypoint [#37](https://github.com/EduCloud-Ecosystem/waypoint/pull/37) merged as
`a58001b2731fa0dc9a1150b65c8940bf656625ec` from reviewed head
`68fe54960d9d3e56b39bd6aa51f21728f532b4c9`.
[Final-head CI 39102679294](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39102679294)
passed 235 offline controls, 41 existing HTTP/Docker checks, historical
replay/recovery and twelve new guard-provider checks; source builds were SKIPPED.
The [local evidence](https://github.com/EduCloud-Ecosystem/waypoint/blob/68fe54960d9d3e56b39bd6aa51f21728f532b4c9/research-workspace/evidence/2026-10-17/operation-guard/README.md)
records **235 offline controls**, **nine real local browser/HTTP checks with a
simulated provider**, and **twelve actual local Docker/provider checks**. The
latter use reviewed legacy Python/R runtimes and Outfitter
`5827c84e9952cc67b85e91ceff4282e0ead6923b`; newer Jetstream2 code is not implied.
Source hashes bind the application and harnesses to the local observations.

These passing records are bounded evidence; the subsequent final-authority
failure below prevents a complete dispatch-fencing acceptance claim.

This explicitly enabled fresh-store profile writes durable operation intents
before business effects and requires exact database completion receipts. Claims
and broker launch share a hold fence; provider waits release database/guard
locks. Uncertain outcomes preserve drafts, requests, files and liabilities,
including when rollback, close or failure-note writes fail. Normal concurrent
initialization defers without being treated as abandoned. Cancellation, logout,
revocation and settlement remain callable; failed writes cannot report success.

Guard-aware v2 checkpoint, held restore and cutover preserve authority,
revocations, charges and unfinished work without automatic replay. Missing or
mismatched bindings cannot fall back to legacy operation. Rolling the database
and sidecar back together is outside the local detection guarantee. The 4,096
ordinary-intent limit and one essential slot bound metadata counts; they are not
a storage quota or a physical-capacity guarantee.

New regression controls address the first four frozen draft witnesses. The fifth
consumed-headroom witness remains **BLOCKED**. The original dirty three-file draft,
its frozen patch and all **127** evidence files present at the accepted base are
unchanged. Two incomplete browser attempts remain visible: a collapsed panel
prevented the first harness action; UI polling raced another injected hold. They
are not counted as passing product checks. The final browser attempt passed all
nine controls, and the separate provider attempt passed all twelve.

Accepted stores were not migrated. Whole-store writer bounds, essential growth,
recovery capacity, retention/deletion and quotas remain unfinished. All four
source candidates stay disabled. Manual accessibility, independent human,
hosted and real-data acceptance remain **NOT RUN**; the earlier failed replay
and cleanup gate are preserved alongside the separate later observation.

The independent post-merge audit reproduced an additional **FAIL** at the final
spawn boundary. On the exact reviewed source, each of cancellation, local user
revocation and project closure committed after the early `should_cancel` check
but before `token.launch`. Each case still reached one intercepted broker spawn;
no real process was started. The final guard fence checked guard state and OIDC
publication without re-reading these local controls. Earlier pre-launch tests
cancelled before execution began and did not cover this boundary.

The source-pinned witness retains three earlier-denial **PASS** controls and
three late-denial **FAIL** controls. Its sanitized observation SHA-256 is
`880dc49971e429d320c3c52292c725a85d8f9d2491617ed65cfd35a1fa374b8d`;
the harness SHA-256 is
`41190959adc368c9dfc154833303df75dc51d559bfde537f3e54b622e8646040`.
Exit zero means the known failures were reproduced, not product acceptance.
The private audit bundle retains 22 immutable source files and their hash index;
these local hashes identify retained evidence, not a published correction.

The owner was tasked with correcting the final serialized local-authority check and adding
boundary controls for cancellation, membership/revocation, closure and expiry.
Pre-dispatch refusal must not be confused with a possibly launched outcome, and
no provider wait or remote identity request may move under database/guard locks.
That task did not establish acceptance; the subsequently reviewed #38 correction
is recorded below. The three failing witnesses and all previous passing/failed
records remain separate evidence.

## Final dispatch and settlement correction

Waypoint [#38](https://github.com/EduCloud-Ecosystem/waypoint/pull/38) merged as
`7d5cf925ffacd16129c6851f1b3d4f8bc4c1a8a0` from reviewed head
`ae00a41a2343858f74de9df9878923cdb197eb3b`.
[Final-head CI 39104328055](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39104328055)
passed controls and actual-Docker/recovery checks; source builds were SKIPPED.
The [local record](https://github.com/EduCloud-Ecosystem/waypoint/blob/ae00a41a2343858f74de9df9878923cdb197eb3b/research-workspace/evidence/2026-10-17/final-dispatch/local-verification.json)
records **295 offline controls**, including **sixty final-dispatch tests**.
The separate root recheck passed **26 targeted tests**, with zero real provider
processes; these are not extra full-suite counts or new browser acceptance.

The final spawn boundary now rechecks current local cancellation, user and
membership state, project closure/expiry and session authority in both guarded
and legacy modes, under the same writer ordering as those controls. Denial before
launch refuses; denial after possible launch retains conservative accounting and
suppresses publication. Review also reproduced and corrected two related defects:
worker refusal settlement could overwrite a superseding recovery/unknown record
with zero accounting, and a fence error after process creation could lose the
owned broker handle. Conditional worker settlement now preserves newer records,
and a launched handle remains available for bounded observer cleanup. Observer
termination still does not prove remote workload termination or settle liability.

The original [red witness](https://github.com/EduCloud-Ecosystem/waypoint/blob/ae00a41a2343858f74de9df9878923cdb197eb3b/research-workspace/evidence/2026-10-17/final-dispatch/pr37-red/observation.json)
and its 22 immutable source files are preserved byte for byte. It still reproduces
three late-denial failures and three early-denial passes on its original source.
Running its unchanged observation logic against an immutable corrected snapshot
prevents all six launches. The independent corrected-observation SHA-256 is
`b27fc831cc0a4b61df190ff8b75bfd2e0041b4b1accd0cca6957d236dea2f7f6`;
the review record SHA-256 is
`a06c8bb942a920ab9b3a1fc26a3bcf53393fda736d5e3531312fa2b98b164f9c`.
All four declared correction-source hashes, 28 frozen witness payload hashes
and 137 prior evidence files matched. The catalog and rejected dirty draft remain
unchanged. The frozen source's original end-of-file whitespace is retained with
its original hash rather than normalized.

The next authorized slice is a source-pinned writer/capacity contract with
disposable production-connected fixtures and a finite-authority growth proposal.
New sessions through an essential slot, SQLite journals/readers, recurring guard
replacement scratch, broker/watchdog writers and restore destination peaks do
not yet have a complete coordinated bound. Unknown files discharge no other
writer's allowance; observed consumption must not be subtracted indiscriminately.
The fifth consumed-headroom witness remains BLOCKED. Quotas, accepted-store
migration, retention deletion and hosted readiness remain unqualified; this
correction does not promote source images or authorize new capacity.

## One finite offline experiment

Outfitter [#13](https://github.com/EduCloud-Ecosystem/outfitter/pull/13) merged as
`2ce00f4950122890a6bcb792ee29e51127ad76c2` from reviewed head
`e10972e7650ff88b0fdfdb86833e592f66aa400b`.
[Final-head CI 39102893358](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39102893358)
passed **736 tests/subtests** across seven packages, including 129 experiment,
231 compatibility and 220 rescue controls, plus 26 Docker, 38 recovery and 19
consumer checks. The corrected local uncached race suite belongs to source
`0172b14ef213ba98f0f39be328c93dd57784bcfb`; final-head CI is separate evidence.

The [contract](https://github.com/EduCloud-Ecosystem/outfitter/blob/e10972e7650ff88b0fdfdb86833e592f66aa400b/specs/16-offline-experiment-enforcement.md)
binds one immutable experiment to source authority/account, configuration/native
policy, compatibility evidence, request/reservation, start/expiry, lifetime and
native amount. Consumption and reservation occur in one serialized ledger
update. Restart, changed requests and settlement do not grant a second attempt;
duplicates retrieve stored status without resuming creation. Matching bound
compatibility and expiry are rechecked before both simulated resource POSTs,
after the phase's durable rescue acknowledgement and final pre-POST boundary.

The separate envelope avoids circular policy/profile hashes. It permits 8 KiB
total, a 2 KiB profile and 4 KiB snapshot, at most eight rules each; existing
16 KiB native-policy/state limits remain. Independent review reproduced a defect
where outer JSON serialization changed opaque envelope bytes after hashing.
The correction rejects unstable bytes before persistence. The
[evidence record](https://github.com/EduCloud-Ecosystem/outfitter/blob/e10972e7650ff88b0fdfdb86833e592f66aa400b/docs/evidence/2026-10-17-offline-experiment.json)
preserves four failing negative cases, two positive controls, the earlier
723-test result and a separate test-fixture initialization failure. Passing later
results do not rewrite these failures.

Fifteen creator-process SIGKILL boundaries and competing creators exercise local
reservation, intent, acknowledgement, POST and saved-response transitions.
These are same-host simulations using injected loopback HTTPS endpoints. Both
rescue acknowledgements and the sole cleanup executor remain required. Lost/late
effects, the 64-sweep limit and unresolved native liabilities remain visible;
observational absence does not settle or refund them. Prior rescue/compatibility
evidence and the original proposed live manifest are unchanged.

**Guest execution remains NOT RUN and live readiness BLOCKED.** There is no live
constructor, creation CLI, credential discovery, deployment switch, SSH/cloud-init
or guest transport. Supplied metadata remains synthetic; boot, private access,
effective network isolation, independent-host cleanup and terminal settlement
are not established. Approval alone cannot close these engineering and
operational gates, and no provider call, allocation use or spending occurred.

## Confirmed approval-lifetime attempt gap

A separate offline investigation at Portage
`b2ba332ff5f81ff15c7ada67d5fc2a79b65cde94` found that the advertised 16 inference
attempts are enforced per runner invocation, not across an approval's lifetime.
The source-pinned fixture uses the actual qualifier loop, metadata validation,
gateway handler and temporary SQLite admission/settlement, substituting clocks,
server lifecycle, engine replies and transport. The parent deliberately starts
fresh Python workers; real sockets/DNS/HTTP and nested worker process launches
are blocked. No model, provider or real credential is used.

| Invariant | Offline observation |
| --- | --- |
| At most 16 inference attempts under one approval | **FAIL**: identical manifest/reference and temporary ledger in two fresh processes dispatch 16 + 16 simulated requests. Both invocation reports say attempt accounting PASS; those synthetic values do not qualify a runtime gate. |
| Lifetime metadata accounting | **FAIL against proposed new invariant**: 51 + 51 metadata operations, without a durable counter. The proposed 51-call ceiling is derived from the current protocol, not a previously implemented global guarantee. |
| No metadata after prior unknown work | **FAIL**: three metadata calls precede the repeat invocation's unknown-work refusal. |
| Unknown reservation/concurrency survives restart | **PASS**: one unknown request retains its 176-unit reservation and active slot; the repeat dispatches no inference. |

The complete scenario settles 384 synthetic provider-reported tokens across
32 calls within its 32,768-token allowance. Low usage therefore does not enforce
the separate attempt promise. Each successful invocation makes 13 calls each to
version/tags/show and 12 residency reads. The fixture fixes a fictional clock;
it does not test elapsed-time correctness, real cancellation, concurrent runners,
copied databases or alternate ledger paths. Those last risks remain source-backed
design concerns, not reproduced outcomes.

The private local failure record SHA-256 is
`0b8eef8c471dbfa0ccd5ec397d219b981c72d8184d4e5ac011a6e64b8a5c482e`;
the reproducer SHA-256 is
`d4f6d7072487db6467f12c7f91fa35df4b33ef18490ab5694e6a49cc0e360b41`.
These identify the retained local witness; no implementation fix is accepted
here. Independent review verified the packet/source/frozen-evidence hashes and
source consistency without rerunning the reproduction. It cleared the following
scope for corrective implementation:

- One protected operator registry and existing authoritative ledger on one host.
  Resolve and validate authority before opening the store; startup may not create
  a database, register a grant, reactivate membership or issue credentials.
- One canonical approval per capacity-budget identity, with permanent fixed
  inference/metadata slots and separately bounded authority checks. Admission
  inserts the attempt and reservation atomically. A runner lease permits the
  existing within-run concurrency while a second runner refuses. Unknown work
  blocks even the first metadata call; lost dispatch acknowledgement stays held.
- Limits apply per operation kind: inference 16 must still permit its last
  predefined residency sample, while inference 17 and metadata 52 refuse.
  Settlement, reconciliation and changed labels/credentials never renew slots.
- Explicit offline migration preserves historical rows, usage and unknown
  holds. Legacy or unbound work does not receive guessed ownership or fresh
  allowance. Reboot, missing clock continuity, restore and authority mismatch
  remain held; no automatic renewal or restore activation. General gateway
  defaults stay unchanged, and qualification mode must require its guard.

This is a local operator trust model. It cannot guarantee detection of privileged
in-place rollback or a registry/database copied together onto another host.
Replacement-grant lineage, cross-host authority, automated restore activation and
hosted transport are deferred. This proposal did not establish corrective
acceptance; the separately reviewed #15 result is recorded below.

The original 95/17/147 evidence records and all 12 runtime NOT RUN fields are
unchanged. Correcting this engineering gap precedes any live qualification;
it does not authorize a host/model, provider access, new allowance or deployment.

## Durable qualification approval correction

Portage [#15](https://github.com/EduCloud-Ecosystem/portage/pull/15) merged as
`79742746b10ace18e498111dd5a8f3227edd995c` from reviewed head
`f22ff34cf232490426149fb3bcc452de9652fe92`. Final-head
[qualification CI 39104327567](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39104327567)
and [full CI 39104327559](https://github.com/EduCloud-Ecosystem/portage/actions/runs/39104327559)
passed; paid review was SKIPPED. The
[evidence](https://github.com/EduCloud-Ecosystem/portage/blob/f22ff34cf232490426149fb3bcc452de9652fe92/docs/qualifications/2026-10-17-durable-approval-controls.json)
pins corrected source `7a2167ce4f4e75835898b1be1de6f02749da380d` and records
**63 guard controls**, **175 runner-preflight controls** and **513 full-suite
passes with six existing skips**. These overlapping suites are not additive.
Independent review verified all ten source/test hashes, the three frozen
95/17/147 records and historical design-packet/bundle hashes without broad reruns.

Qualification now resolves a protected operator registry before opening an
existing authoritative store. It cannot provision a store/grant, reactivate
membership or issue a credential at startup. One canonical approval per budget
owns permanent named inference, metadata and authority slots; attempt/reservation
admission is atomic. A cross-process runner lease permits the protocol's two
within-run calls while a competing runner refuses. Final dispatch claims fence
local authority and deadlines; claim commitment is the local revocation cutoff,
not a claim of remote cancellation.

| Corrected fixture | Observed bounded outcome |
| --- | --- |
| Complete first invocation | 16 inference, 51 metadata and 83 authority contacts; 192 provider-reported tokens. The final residency sample remains permitted after inference 16. |
| Completed fresh-process repeat | Zero inference, metadata or authority contacts. |
| Unknown-usage first invocation | One inference, six metadata and eight authority contacts; 176-unit reservation and one concurrency slot retained. |
| Unknown-work fresh-process repeat | Zero contacts; the original reservation remains held. |
| Abandoned attempt or dispatch claim | Fresh process refuses without replay; uncertainty remains held. |
| Competing process at the final slots | Competing runner refuses busy without contact; the owner completes the predefined plan. |

Review fixed a clock-watermark defect: a second unchecked clock read could
overwrite the already validated value. The failing regression is retained;
the correction persists the validated pair in its transaction. CI also retained
two distinct failures: run `39103722745` had two passes and sixty setup errors
because a test-output parent was missing; run `39103902273` had 61 passes and one
assertion failure because a contact-count trigger could miss both concurrent
final calls. The fixture now synchronizes the persisted final-slot identities;
it no longer relies on that timing. Runtime, fixture and final-evidence revisions
are separately pinned, and the failures were not removed by rerunning to green.

Settlement and reconciliation never refund attempt slots or revive a held
approval. Explicit offline migration preserves historical rows and liabilities;
unbound old work does not receive inferred ownership or fresh allowance. Reboot,
missing clock continuity and authority mismatch refuse; automatic restore
activation is not added. The local trust model cannot guarantee detection of
privileged in-place rollback or a copied registry/database on another host.
Generic gateway defaults and hosted runtime are unchanged. **All twelve actual
engine gates remain NOT RUN**; no model, provider, live inference, spending or
default-route change is authorized by this fixture acceptance.

## Supplemental worker operational packet

Outfitter [#14](https://github.com/EduCloud-Ecosystem/outfitter/pull/14) merged as
`e9c18f970bae38aef7254b90f1465dadd64673d5` from reviewed head
`2f5f4c63efc229d1c6fe9370e0ec40277cef9b3b`.
[Final CI 39104169911](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39104169911)
passed. This is documentation-only acceptance; no runtime or guest feature was
added. The [packet](https://github.com/EduCloud-Ecosystem/outfitter/blob/2f5f4c63efc229d1c6fe9370e0ec40277cef9b3b/docs/JETSTREAM2-OPERATIONAL-DECISIONS.md)
recommends restricted private SSH from existing approved capacity, an independent
cleanup host and one finite synthetic CPU-worker attempt. Allocation, host,
operator, private access and credential custody remain unselected; no live action
or resource authorization follows from the recommendation.

Independent review corrected guest-key/provider-credential wording, removed an
unnecessary architecture re-approval gate and clarified that the **64 total
persisted sweeps per reservation/observer store are shared across both resource
phases and restarts**. All fourteen protected historical files, including the
original proposed manifest, match the accepted base. Public primary sources
support the dated candidate facts; selected-provider behavior remains unknown.
The reviewed document SHA-256 is
`af5e6006a6eb462b877be1d2721dbb97b4fedd7cd11123c9418424d16fe3f034`;
the structured supplement SHA-256 is
`5f618ec1013677898b15baf92e2344ba468000d21737b96a6a695664f2b13507`.

No additional subscription is demonstrated necessary. Existing host/network
capacity and operating costs are unverified; any new infrastructure needs a
priced decision. The proposed 1 SU reservation remains a local accounting bound,
not a provider-enforced cap or verified maximum exposure. Late effects and
uncertain liabilities persist. Guest bootstrap/transport, production evidence
collection, independent-host recovery and terminal cleanup remain engineering
and operational gates before live approval can be executable. Ordinary scoped
design work continues under the existing build authorization.

## Storage writer contract qualification

Waypoint [#39](https://github.com/EduCloud-Ecosystem/waypoint/pull/39) merged as
`599ee0ce23942bbfc578124af12285484c357157` from reviewed head
`e543ca4e8a388bb71fe96e11e12b6765829e4a29`.
[Final CI 39105674607](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39105674607)
passed controls and actual-Docker/recovery checks; clean source builds were
SKIPPED. Production application source is unchanged. This accepts the
[contract and disposable qualification](https://github.com/EduCloud-Ecosystem/waypoint/blob/e543ca4e8a388bb71fe96e11e12b6765829e4a29/research-workspace/STORAGE-CAPACITY-CONTRACT.md),
not quota enforcement or a finite whole-store capacity claim.

The contract identifies seventeen writer categories against Waypoint
`7d5cf925ffacd16129c6851f1b3d4f8bc4c1a8a0` and Outfitter
`5827c84e9952cc67b85e91ceff4282e0ead6923b`. Local evidence records 296 suite
passes, including an entry point for eight new Python controls; seven selected
Go controls use a disposable export and simulated provider. The corrected eight
controls and three additional fault injections passed independent review. These
counts overlap and are not additive; no new browser/human acceptance is claimed.
Root independently verified eighteen manifest hashes, 23 Waypoint and eleven
Outfitter source hashes, all 168 historical evidence files and five byte-identical
pre-review artifacts, without repeating workloads.

| Control or gap | Recorded result and boundary |
| --- | --- |
| Append consumption and exact fit | **PASS, offline model** connected to actual submit writers. Expected paths, lengths and hashes derive before submission from trusted fixture inputs. One byte/entry short, wrong incarnation, missing proof, same-length corruption and unexpected files receive no credit. No admission hook uses this arithmetic. |
| Initial append ownership fixture | **FAIL in review methodology**, preserved: initial head `5168434554d0aa1c8276acc63adaefeffd1aa95f` compared an observed map with itself. Its passing test result and initial overly broad review remain historical, not independent ownership proof. The corrected witness and negative controls supersede that claim. |
| Guard replacement and partial writes | **PASS for bounded observation**, with retained failure paths: old/new generations coexist; file-sync and post-rename directory-sync failures retain temporary files or uncertainty. Completed replacement does not pay for the next scratch file. |
| Sign-in and held reader | **FAIL for a finite storage bound**: 24 sign-ins add session rows and grow WAL while reusing one essential slot. Existing ordinary-intent limits do not bound that growth. |
| Final metadata slot | **PASS**: two actual Store transitions compete and exactly one commits under a narrowed fixture limit. This is metadata-slot enforcement, not byte/entry quota enforcement. |
| Restore destination | **NOT RUN for enforced capacity refusal**: intercepted production restore creates a destination and held config before its copy call. The harness stops before copy, leaves the source unsealed and refuses UNKNOWN only in its offline model. |
| Whole-store quotas and fifth headroom witness | **NOT RUN / NO-GO** for quota enforcement; the fifth historical consumed-headroom failure remains **FAIL** and byte-identical. Physical disk exhaustion, power loss, portable SQLite/VFS peaks and real detached-watchdog storage peaks remain NOT RUN. |

The broker audit identifies recurring writes behind legacy opens and duplicate
commands, pre-watchdog snapshot copies without a copy deadline, background
cleanup writes outside the execution lease, protected temporary/orphan files and
unbounded repeated external checkpoint destinations. A stopped parent, settled
compute receipt or matching inventory scans do not prove all writers finished
or that bytes are reclaimable. All writer rows keep whole-root bounds UNKNOWN;
`quota_enforced:false` and available-capacity UNKNOWN remain explicit.

Root's final decision is **GO for a separate fresh opt-in finite logical-authority
slice**, with the [reviewed limits and safety matrix](../decisions/2026-10-17-research-pilot-capacity.md#finite-authority-engineering-decision).
It must preserve total history, existing authority/profile bindings, safe
refusals and restore preservation. **NO-GO for quota wiring** remains in force.
No accepted-store migration, deletion, journal/default change, source promotion,
live provider/model work or purchase occurred. Ben's assignments and the Docker
baseline are unchanged.

## Finite logical authority

Waypoint [#40](https://github.com/EduCloud-Ecosystem/waypoint/pull/40) merged as
`e79a50c6074e3ecf579a5bc5b0732c473d62502d` from reviewed head
`f7d0cd44fac9e594775302b512c04c75c252798e`. Its merge tree
`012a93d8ff3098c6c4393d0f78d3749430023fd0` matches the reviewed head.
[Exact-head CI 39107672215](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39107672215)
and [post-merge CI 39107809444](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39107809444)
passed controls and existing actual-Docker/replay/recovery checks; clean source
builds were SKIPPED. Docker results are compatibility evidence for existing
profiles, not finite-profile provider qualification.

The [profile contract](https://github.com/EduCloud-Ecosystem/waypoint/blob/f7d0cd44fac9e594775302b512c04c75c252798e/research-workspace/FINITE-AUTHORITY.md)
implements the reviewed engineering limits on fresh local-key stores: 128 total
users, 20 total projects, 1024 memberships, 1000 historical runs and 256 live
sessions/eight per subject. Revoked/closed/failed history still counts. Existing
tighter per-project, queue, expiry and compute limits remain. Versioned
config/database/guard binding, bounded canonical JSON and signed-counter overflow
checks fail closed. New rows/sign-ins use ordinary admission; existing sessions,
logout, revoke/rotate, membership demotion/removal, cancellation and conservative
accounting retain their safety behavior. Project initialization reserves its
owner membership against competing admissions.

Checkpoints preserve the finite profile and database marker. Finite-profile OIDC
and all four common/direct restore/cutover entry points explicitly refuse before
provider, destination or source-lock/sealing effects. These are safe refusals,
not accepted finite-profile identity-provider or recovery implementations.

| Control or gap | Recorded result and boundary |
| --- | --- |
| Local suite and finite controls | **PASS**: 317 tests include 21 finite controls and one bridge running eight frozen v1 controls. Counts overlap. Boundary history is seeded synthetic data, not 1000 provider runs. Final transitions exercise production methods; provider behavior is simulated. |
| Independent review | **PASS**: owner review reran the 21 controls and v1 bridge; supplemental disposable checks covered nine safety actions each starting independently at all five row caps, cross-process final-user-slot contention and OIDC refusal. The committed combined safety test is sequential and frees some capacity before later actions; it alone is not the independent full-cap matrix. |
| Database authority corruption | **FAIL originally, corrected**: deleting, retargeting or duplicating authority rows while retaining other markers allowed reopening and some safety writes. Exactly one matching identity and bounded sequence are now required before access or safety bypass. Fresh regression fixtures check unchanged database/config/guard after refusal. |
| Direct recovery entry points | **FAIL originally, corrected**: an internally consistent trusted fixture with a finite SQLite marker and stripped config markers reached direct destination creation or source locking. All four entry points now perform config/database preflight before these effects. |
| Encoded receipt overflow | **PASS, fault injection**: the mock injects roughly 720 KiB past the real collector's 262144-byte cap. Production would reject it earlier. This qualifies serializer refusal/retained uncertainty, not a reachable accepted receipt overflow. |
| New finite-profile browser, real provider and human acceptance | **NOT RUN**. Ordinary Docker CI does not close these gates. |
| Whole-store quotas and physical capacity | **NO-GO / UNKNOWN**: logical ceilings do not bound SQLite pages/WAL, repeated scratch, detached broker writers or restore destinations. `quota_enforced:false`; fifth consumed-headroom failure remains **FAIL**. No physical disk-full/power-loss or selected-host fit acceptance. |

The [acceptance record](https://github.com/EduCloud-Ecosystem/waypoint/blob/f7d0cd44fac9e594775302b512c04c75c252798e/research-workspace/evidence/2026-10-18/finite-authority/README.md)
preserves original red source/log: two tests, fifteen failed subtests and three
AccessError sequencing errors after shared-fixture revocation. Those three errors
are not independently demonstrated cancellation bypasses. Exploratory failures
and the first incomplete frozen archive remain recorded; intermediate source
trees were not frozen, so those logs make no exact-replay claim.

Root independently rechecked both fixes and verified all 25 source and 16
evidence hashes without rerunning workloads. Acceptance JSON SHA-256 is
`d78864f12b557e8ad96a5164911fcbe8ed1cdc8a5fc813f5f10d41aa07690015`;
manifest SHA-256 is
`b8897e209874aa6c760afcaf8ddd7faaecc32dd29914fb1571bbb0c6739a01fe`.
Owner's final independent review report SHA-256 is
`6a1ade34af7cf90619cf3b09f4fd4ac96ad4acd71e03b4669d7a3f0b944aec55`;
its exact-head targeted log SHA-256 is
`68fc942be4a01cd711ab2325080d3318c44afb8f25990f21281ea58922d29885`.

Root's immutable-blob audit confirmed all 182 prior October 17 evidence files
remain byte-identical. The existing v1 capacity contract/harness retain their
source meaning; the current test bridge verifies and runs a 43-file frozen
export of base `599ee0ce23942bbfc578124af12285484c357157`, archive SHA-256
`4da52b3c1889968d15ac12670a9bc9fe89379f15c9188ee7ef6d43ceed6f6333`.
Each archived file matches its original Git blob. These eight historical
controls are not relabeled as modified-runtime coverage. No accepted-store
migration, alternate ledger, history deletion, journal/default change, source
promotion or liability release is accepted. All four source candidates remain
disabled and earlier failed replay/cleanup evidence remains.

The next scoped offline work is Waypoint SQLite/guard write-peak qualification
and Outfitter Docker broker writer ownership qualification, with separate owners,
source pins, disposable witnesses and independent review. A reviewed concrete
protocol precedes broader implementation; quota admission remains NO-GO.

## SQLite and guard write qualification

Waypoint [#41](https://github.com/EduCloud-Ecosystem/waypoint/pull/41) merged as
`1e4b04c2d07dd4730d904fe93acb1795ad1a4d1c` from reviewed head
`b8845f571cf0c5c7907033054dd70f6fa083c975`.
[Exact-head CI 39108789105](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39108789105)
and [post-merge CI 39108929454](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39108929454)
passed existing controls/Docker compatibility; clean source builds were SKIPPED.
Application source, active broker pin and SQLite settings remain unchanged.

The [source-pinned protocol](https://github.com/EduCloud-Ecosystem/waypoint/blob/b8845f571cf0c5c7907033054dd70f6fa083c975/research-workspace/SQLITE-GUARD-PROTOCOL.md)
and [evidence record](https://github.com/EduCloud-Ecosystem/waypoint/blob/b8845f571cf0c5c7907033054dd70f6fa083c975/research-workspace/evidence/2026-10-18/sqlite-guard/README.md)
qualify nine disposable witnesses. The 318-test suite includes their bridge and
the existing bridge to eight frozen capacity controls; counts overlap. Owner
independent review reran the nine controls and bridge, added four effect-negative
controls and independently derived the maximum canonical guard-map size. Root
review did not repeat workloads; it verified 22 source pins, nine manifest hashes,
exact harness/contract/report bindings and all 199 prior evidence files against
base `e79a50c6074e3ecf579a5bc5b0732c473d62502d`.

| Control or gap | Recorded result and boundary |
| --- | --- |
| Held reader with 160 key rotations | **PASS witness; finite WAL bound unproved**. WAL reached 4614432 bytes; PASSIVE observed 1120 frames, zero checkpointed. Explicit TRUNCATE completed only after releasing the disposable reader. No production checkpoint setting changed. |
| Startup and borrowed safety writes | **PASS witnesses**: six opens grew WAL; eight borrowed essential rotations changed WAL without changing guard bytes. Intent/counter counts do not bound this history. |
| Full guard map | **PASS per-save logical bound**: seeded 4096 ordinary plus one essential item produced 2327358-byte current and candidate files. Enforced candidate ceiling is 4 MiB; current plus one candidate at most 8 MiB excludes prior scratch, other saves in the action and SQL/engine writers. |
| Failed temporary writes and commit acknowledgment | **PASS fault witnesses**: three file-sync failures retained three distinct temps; pre-commit revoke rolled back, post-commit revoke persisted, and both retained uncertainty. A post-rename sync error left a visible uncertain generation. These are injected application acknowledgment faults, not physical disk/VFS/power-loss qualification. |
| Safety actions under a reader | **PASS**: nine independent fixtures verify authentication, logout, membership demotion/removal, revoke/rotate, cancel, settlement and project close. Row caps were not filled; #40's full-cap checks remain separate evidence. No physical write-availability guarantee. |
| Restart recovery | **PASS corrected fixture**: a fresh process recovered 20 near-ceiling synthetic records as 19 cancelled and one interrupted/unknown, retaining a paused state. The 5228312-byte WAL observation is not a transient engine maximum. No provider ran. |
| Original restart assumption | **FAIL, retained fixture assumption**: the earlier same-process recovery expected a paused restart despite its live run lease. Original nine-control harness/report/log remain unchanged; this does not establish a production defect. The first seven-control exploratory log lacks a frozen exact harness and makes no replay claim. |
| Whole-store finite protocol | **NOT IMPLEMENTED / NO-GO**: reader coordination, retry-slot preservation/exhaustion and qualified engine ceilings remain proposals. Capacity UNKNOWN, `quota_enforced:false`, fifth consumed-headroom failure **FAIL**. Physical exhaustion, power loss, concurrent engine checkpoint races and complete writer ownership remain unqualified. |

The accepted qualification report SHA-256 is
`17527bfb90d7ffb955bbd5b4434486f363dd0715d53b7805c458181a6d624026`;
evidence manifest SHA-256 is
`ebb52fd3091f90933a8a3e23c1c42436d14838e1798c4bdca6c0b91b7f205d6b`.
The machine contract SHA-256 is
`6b0d81d3d75f4997d35fd605571d0ad35ac662afe145f4845fa018a51975bab5`;
qualification harness SHA-256 is
`e987ea7c68e3e6761c73af864cd3f623793d595ffd41d49010264a18303db332`.
These hashes identify evidence integrity, not independent authenticity or runtime
capacity. No accepted-store migration, restore enablement, deletion, source
promotion or liability release occurred.

Next is a narrowly scoped export-reader lifetime design: materialize bounded
metadata, release the SQLite read transaction before artifact I/O, verify exact
evidence, construct the bundle, and recheck current authority and unchanged
metadata before returning bytes. A concurrent revocation or metadata change
refuses export without retry or accounting mutation. The explicit opt-in
version/binding contract subsequently received independent design review and
narrow implementation GO under the [capacity decision](../decisions/2026-10-17-research-pilot-capacity.md#finite-authority-engineering-decision).
The reviewed original proposal SHA-256 is
`eabfa3fd139c98785d168415ba3aaf7ba6be0beb35c7fde815806ad0de4f23d9`;
the corrected pre-implementation contract SHA-256 is
`8fa312c32da9e96a8067b0e8ddb964d4eb81d5ac94efda72caff681141a4d6c2`.
The corrections distinguish current-state equality from transient change-and-
revert, and pre/during-read file mutation from later changes to already copied
bytes. The subsequent implementation is accepted below; whole-store admission
and guard scratch policies remain separate.

## Fresh opt-in bounded export

Waypoint [#42](https://github.com/EduCloud-Ecosystem/waypoint/pull/42) merged as
`66a48dfe29d61d3f6f48f016f2c474e1ac6af4f6` from reviewed head
`b4ccf05ecf9e7d796ba2b35a9a05d803fd973819`.
[Exact-head CI 39110032142](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39110032142)
and [post-merge CI 39110144665](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39110144665)
passed controls and existing actual-Docker compatibility checks; clean source
builds were **SKIPPED**. Head and merge share tree
`15cef753c0e3999245c72c008899309470ad769f`.
The [implemented contract](https://github.com/EduCloud-Ecosystem/waypoint/blob/b4ccf05ecf9e7d796ba2b35a9a05d803fd973819/research-workspace/BOUNDED-EXPORT.md)
and [evidence chronology](https://github.com/EduCloud-Ecosystem/waypoint/blob/b4ccf05ecf9e7d796ba2b35a9a05d803fd973819/research-workspace/evidence/2026-10-18/bounded-export/README.md)
bind the fresh `init --bounded-export` profile and preserve its failed controls.

The exact v2 mode/policy/export-protocol, guard v3 and database marker tuple is
required throughout; mixed/stripped bindings refuse. Existing v1/default paths
remain separate; finite OIDC, restore and cutover still refuse. The new helper
requires a local session token. It captures bounded project/run/private authority
metadata under the guard and a query-only SQLite transaction, then closes both
before descriptor-based bounded artifact reads and ZIP construction. Captured
hashes/results and public bundle structure are verified. Final authorization
reacquires the guard through a fresh exact capture/comparison and expiry check,
including private cancellation, session, membership and active-user state.
No export reader or guard lock spans HTTP streaming. Changes refuse without
automatic retry, output files, intents or accounting mutation.

| Control or boundary | Recorded result |
| --- | --- |
| Local suite and independent review | **PASS**: 334 full-suite tests include 16 export tests and both frozen bridges. Independent review reran the 16 export tests, 21 finite-v1 tests and both bridges, plus 13 supplementary controls. These counts overlap and are not additive. |
| Concurrent authority changes | **PASS** disposable production Store/HTTP controls: revoke/rotate/cancel/settle complete while artifact/ZIP work is blocked, and changed final authority/private metadata refuses publication. Revocation after final authorization permits already-authorized bytes to finish streaming. |
| Negative and supplemental controls | **PASS** control sensitivity: injected reader leak, missing final authorization and missing private cancellation comparison are detected. Fresh CLI/reopen/sign-in, required-runtime refusal and mutation during descriptor reading pass. Supplemental commands were inline; no standalone exact-harness replay claim. |
| Historical preservation | **PASS** root audit: all 209 prior evidence files, catalogs and image pins unchanged; 39 frozen #41 files equal base Git bytes. Current manifest binds 22 source and 38 evidence hashes; independent review binds 21 sources. Root independently audited code and bindings but did not rerun runtime/provider workloads. |
| Remaining acceptance | **NOT RUN** for new-profile live-provider, real/private-data, accepted-store and physical-capacity acceptance. New controls use simulated project allocation, no broker or Docker; existing Docker CI is a separate compatibility gate. Whole-store capacity **UNKNOWN**, quota admission **NO-GO**, `quota_enforced:false`, fifth headroom failure **FAIL**. |

The initial descriptor-close acknowledgement failure left four other descriptors
open; the correction attempts every close once, retains the first error and
refuses publication without retrying an ambiguously closed descriptor. Original
source, hashes and witness remain preserved. Incorrect verifier-field assertions,
duplicated finite-test discovery, a misplaced revocation assertion and a wrong-
directory import failure remain labeled fixture/invocation failures. The first
frozen archive omitted a transitive `test_recovery.py` fixture; its incomplete
archive/bridge/failure remain, and the accepted archive adds only that unchanged
base file. Expected injected negative failures are not candidate failures.

Current equality cannot detect transient change-and-revert. Later artifact
changes cannot modify previously verified copied bytes. Conservative charges
and UNKNOWN liabilities remain. This does not establish WAL, memory or time
maxima, engine ceilings, checkpoints, scratch reuse, migration or storage quotas.
The subsequent guard publication design received narrow implementation GO after
independent exhaustion/takeover/compatibility review and the required cache
clarification in the capacity decision. Its corrected implementation is accepted
in #43 below; this earlier design record alone did not establish runtime acceptance.

Manifest SHA-256:
`a7fce6b1312594855dca20af7dadc9f9ba829c6a3f456f76a28465836eea0db9`.
Frozen #41 archive SHA-256:
`6bf625ca8c826e85d2cb80893e1e61fd673e52fff6b33a9bf1439c8e7977efdf`.
Independent review SHA-256:
`49ab8c7fbce96357ccfdc2dd82fde7b02c754cc2e35855ea249118bfee3a44ac`.

## Docker broker storage-writer qualification

Outfitter [#15](https://github.com/EduCloud-Ecosystem/outfitter/pull/15) merged as
`e5599066970750ff3aa8f539bf0391f9c7e32346` from reviewed head
`0d94e3c830e97f236bd745d27942e06d24a03ba4`.
[Corrected-head CI 39109599802](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39109599802)
and [post-merge CI 39109844174](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39109844174)
passed the new offline qualification and existing broker/Docker checks. The
reviewed head and merge share tree `0e88fc7b17a90e75ac275a9a3652d88d8d3a32d0`.
The [protocol](https://github.com/EduCloud-Ecosystem/outfitter/blob/0d94e3c830e97f236bd745d27942e06d24a03ba4/specs/17-storage-writer-qualification.md)
and [witness interpretation](https://github.com/EduCloud-Ecosystem/outfitter/blob/0d94e3c830e97f236bd745d27942e06d24a03ba4/qualification/storage_writers/README.md)
extend the five broker rows of Waypoint #39. Runtime source and Waypoint's active
broker pin `5827c84e9952cc67b85e91ceff4282e0ead6923b` remain unchanged.

The runner verifies eleven source hashes, exports that exact pinned revision and
records declared test instrumentation before exercising production functions.
The corrected local record has **22 Go test/subtest passes**, **20 connected
observations**, **32 separate model cases** and **two optimized-process oracle
fault probes**. These are different evidence units, not an additive test count.
The connected tests use disposable files/processes and fake provider operations.
Main baseline `e9c18f970bae38aef7254b90f1465dadd64673d5` is compared separately;
this neither qualifies its runtime nor promotes it to the active consumer pin.

| Control or gap | Recorded result and boundary |
| --- | --- |
| Spill and publication ordering | **PASS counterexample witnesses**: three distinct output sidecars survive injected ledger-sync failures while prior authority and 30 unknown CPU-seconds remain. Output encoding/replacement and six publication fault points distinguish old authority from visible but unproved new generations. Later I/O orphans remain possible. |
| Lowered compact-record limit | **PASS ordering witness only**: injected limit is one byte; production limit is 98304 bytes. A normal CLI request reaching that production cap is **NOT DEMONSTRATED**. |
| Snapshot growth and cancellation | **PASS counterexample witnesses**: the walk/refusal leaves 1026 entries including two parents; growth after stat retains 16 MiB plus one byte. Copy may continue after cancellation while checkpoint completes with unknown work. Exact expected bytes/hashes are derived before copying. |
| Background Watch ownership | **PASS instrumented process witnesses**: stale/shared readiness, blocked ledger update, requester exit, continued generations and post-cutover readiness writes do not establish all writers stopped. Helpers are independently supervised real processes using actual Watch code, not the CLI launcher's parent/child handoff. That launcher remains **NOT RUN**. |
| Checkpoint/cutover | **PASS counterexample witnesses**: only referenced diagnostics are copied; unknown source files remain protected. An injected post-rename directory-sync failure returns activation error while source is fenced and destination visibly active. Before-publication failure is a distinct case. An error alone cannot certify both non-admitting or release either root. |
| Finite ownership model | **PASS corrected model controls; NOT ENFORCED**. Exact Boolean proofs, integer/nonnegative terms and explicit oracle failures reject reviewed invalid inputs. The model consumes declared fixture inputs, not a production ownership census or quota admission path. |
| Physical/provider/whole-store acceptance | **NOT RUN** for physical exhaustion, failed temporary removal, host/power loss, actual CLI watchdog handoff, complete writer discovery, enforced destination refusal and production quotas. Qualification invokes no Docker/cloud provider. Existing Docker CI is a separate compatibility gate. Whole-root capacity remains **UNKNOWN**, `quota_enforced:false`, fifth headroom failure **FAIL**. |

The [evidence chronology](https://github.com/EduCloud-Ecosystem/outfitter/blob/0d94e3c830e97f236bd745d27942e06d24a03ba4/docs/evidence/2026-10-18-storage-writers/README.md)
retains the initial missed snapshot hook: **19 passes/one failure**, with one fake
provider create because the intended refusal boundary was not reached. Canonical
path matching and explicit hook/content assertions correct that fixture. No real
provider was called. The later `qualified-v1` passing report and initial root
clearance at `e0eff0bc74b2ed35420a98d43cab7edb13258e56` are **superseded for model
validation**: second independent review reproduced eight false acceptances of
UNKNOWN/non-Boolean flags and thirteen incorrectly accepted negative controls
under Python optimization with a deliberately always-accepting model. The exact
old model, red records, old passing report and successful old-head CI remain
preserved. The correction requires literal Boolean proofs and explicit failures;
both always-accept and always-reject oracle faults must fail with assertions off.

Root's corrected-head audit verified the source, instrumentation and artifact
hashes, all ten prior evidence files and unchanged upstream contract/fifth-failure
copies. Focused model probes and both optimized oracle probes passed; root did
not rerun the connected Go workload or any provider. Corrected report SHA-256:
`fb960be0672f99cec5e14185191a6ce99eb20d1f5a56107ce7e171e014d2bf92`.
Model SHA-256:
`13bf957f19dd33c996a90a82bbb34fbaee575557f7974f20ce791bf9202a4dda`.
Runner SHA-256:
`123f52d7317f9269ef6ef8d74e19a87821957b62b9aeeab31dabc78324ff35b2`.

Independent design review gives narrow implementation GO for pre-serializing
ledger/output plans inside the existing transaction, validating both diagnostic
outcomes and the maximum mixed ledger before file effects while preserving
native/consumer fields and conservative accounting. Keep one encoded output
buffer at a time. The separate implementation is accepted in #16 below.
It does not repair later I/O orphans, repeated scratch, background ownership,
snapshot/cutover gaps or whole-store quotas, and does not change the active pin.
Ben's assignments, live operational choices and all unresolved liabilities remain.

## Ledger serialization before diagnostic effects

Outfitter [#16](https://github.com/EduCloud-Ecosystem/outfitter/pull/16) merged as
`5446438985e31cb739f2048a2aa2176918831a7e` from independently reviewed head
`28d34437e61a7bfe50fbfafcabc656a7f09fceec`. The head and merge share tree
`b65c2c381a282f221e0cb8acfa2a47bf8b3fca4e`.
[Exact-head CI 39110530266](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39110530266)
passed both broker/Docker and pinned writer-qualification jobs.
[Post-merge CI 39110992276](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39110992276)
also passed both jobs at the merge revision.
The [specification](https://github.com/EduCloud-Ecosystem/outfitter/blob/28d34437e61a7bfe50fbfafcabc656a7f09fceec/specs/18-ledger-serialization-preflight.md)
precedes implementation, and the
[implementation report](https://github.com/EduCloud-Ecosystem/outfitter/blob/28d34437e61a7bfe50fbfafcabc656a7f09fceec/docs/evidence/2026-10-18-ledger-preflight/implementation.json)
binds the source and retained failures.

Within the existing transaction, preparation computes actual encoded output
digests/lengths, validates both diagnostic outcomes and each compact record, then
serializes the largest mixed-outcome ledger with all native/consumer metadata.
Sidecar persistence starts only after that succeeds. Publication reencodes one
output at a time, verifies its plan and selects the validated outcome matching
actual persistence. Diagnostic failure still permits conservative accounting.
Plans retain source strings and small metadata, not an array of encoded outputs;
the extra encoding work is not a physical-memory or elapsed-time bound.

| Control or gap | Result and limit |
| --- | --- |
| Original serializer/capacity failures | **FAIL preserved** against the prior runtime: a logically valid but unencodable timestamp and a valid aggregate ledger exceeding 64 MiB each left an orphan diagnostic. Old ledger and unknown-file bytes remained. Runnable fixture source and raw failures are retained. These constructed `Store.Update` cases do not claim ordinary CLI reachability. |
| Focused candidate controls | **PASS**: 18 race test/subtest events across five top-level tests. Includes refusal before filesystem effects, all eight outcomes for three diagnostics, largest mixed-form selection, private lowered boundaries, plan mismatch, native/consumer preservation and immutable experiment checks. Production limits are unchanged. |
| Broader verification | **PASS**: 754 full uncached race tests/subtests across seven packages, vet and formatting; exact-head CI artifacts also report 754 Go events, 26 Docker, 38 recovery and 19 consumer checks. Pinned writer qualification remains 20 observations/32 model cases. These units overlap and are not additive. |
| Independent review | **PASS** exact-head runtime review: owner reports 18 focused controls plus five independent probes, and base failures reproduce while candidate refusals prevent sidecars. Root's separate code/provenance audits are **CLEAR**, verify four source hashes and all 28 prior evidence files, and rerun no workloads. |
| Remaining limits | **NOT RUN** for live allocation/provider acceptance, physical exhaustion, host/power loss and complete writer/heap bounds. Later output/ledger I/O can leave orphans or uncertain durability. Snapshot, watchdog and recovery behavior remain unchanged. Whole-root capacity **UNKNOWN**, `quota_enforced:false`; fifth headroom witness remains **FAIL**. |

Implementation report SHA-256:
`6bd2a2110c5111d71e8ae1118ff9463e11bed1e041ab8ad83061e72f490fd2c6`.
Focused passing log SHA-256:
`2c8297e92ba3194d976a8e7979d75fcf72b5328a1436ef308c928e62d58dccd8`.
Original failing log SHA-256:
`3464820c95330aab2024ddd9befa95245dc6f3cc13a249a49ae350a7c2914264`.

At #16 acceptance, Waypoint's active CI broker remained
`5827c84e9952cc67b85e91ceff4282e0ead6923b`.
The subsequent adoption qualification compares old/new executable behavior and old
authority/checkpoint formats in disposable state before changing that pin.
Do not infer upgrade compatibility from tests that use one binary throughout;
native-v3/consumer-v4 state is outside the local-v2 consumer adoption contract.
Belay, accepted stores, dirty worktrees, Ben's assignments and live choices remain
outside this change.

## Fixed guard publication slots

Waypoint [#43](https://github.com/EduCloud-Ecosystem/waypoint/pull/43) merged as
`5f2b21f1535702f9c18592b15e61c4c347d93558` from independently reviewed head
`b063dc99ffdde60e75af7a1862538ab51eb4ebb3`. Both share tree
`20350883ac03dd0ea6609163fb8713d0cb1a0d28`.
[Exact-head CI 39113340974](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39113340974)
passed controls and actual Docker; optional clean source builds were skipped.
[Post-merge CI 39113820730](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39113820730)
passed the same two jobs at the merge revision; clean source builds were skipped.
The [profile contract](https://github.com/EduCloud-Ecosystem/waypoint/blob/b063dc99ffdde60e75af7a1862538ab51eb4ebb3/research-workspace/BOUNDED-GUARD-PUBLICATION.md)
and [candidate packet](https://github.com/EduCloud-Ecosystem/waypoint/blob/b063dc99ffdde60e75af7a1862538ab51eb4ebb3/research-workspace/evidence/2026-10-18/guard-publication/acceptance.json)
retain the original failures and source bindings. The packet's review-pending
fields describe its pre-review capture; the subsequent review/merge results here
do not rewrite that artifact.

Fresh `--bounded-guard-publication` state uses distinct v3 profile/authority and
v4 guard bindings. Current publication plus fixed ordinary and safety scratch
slots replace recurring randomly named guard candidates only in this profile.
Exclusive no-follow creation, exact file/incarnation verification and ordered
file/directory durability barriers preserve residue rather than adopting or
deleting it. Each safety action requires fresh intent. Cached durability applies
only to the exact current incarnation; every mutation still rereads residue,
receipts and holds, including scratch left by another process without a new
current publication. Takeover qualification occurs before business transactions.

| Control or gap | Result and limit |
| --- | --- |
| Original reviewed candidate | **FAIL preserved** at `cf8befca`: cancellation, revocation, closure or expiry released the claim token before final publication checking; an unrelated cross-process safety publication also blocked request preparation. Initial passing CI did not establish acceptance. Exact original source/witnesses and four candidate artifacts remain. |
| Corrected candidate | **PASS**: 368 local automated controls include 34 guard-publication tests and 14 nested bounded-export controls. Owner independent re-review passed 34 publication tests and 14 adversarial controls; deliberately reverting either correction reproduces failure. Counts overlap and are not additive. |
| Root independent review | **PASS/CLEAR** at the exact head: five focused regressions plus the original cross-process replay. Takeover succeeds before the request effect; inside business SQL it still refuses with zero barrier calls. Late cancellation prevents dispatch; commit/close and takeover failures retain uncertainty. No provider or Docker calls in these probes. |
| Provenance | **PASS**: 45 source and 55 evidence hashes, all 248 earlier evidence files and the unchanged root failure witness verified. Head and merge trees match. |
| Logical bound | Conditional sum of at most three 4 MiB named guard payloads, **12 MiB**, for fresh controlled state. Excludes SQLite/WAL/SHM, metadata, unlinked open files, physical allocation, memory/time, other writers and available capacity. |
| Remaining acceptance | New-profile actual provider, manual/operator, physical exhaustion and power-loss controls **NOT RUN**. Existing Docker CI covers compatibility. Whole-store capacity remains **UNKNOWN**, quota admission **NO-GO**, and the fifth headroom witness **FAIL**. |

Accepted packet SHA-256:
`68c44555521f543edabe6c0fe84fe736d2d702e5dd6dbfdde5b28e2b052358db`.
Candidate source manifest SHA-256:
`228f26e33d1f38e4585e20c3945cdea456c9b888a8739b101d3cd5c2bbde6383`.
Root independent corrected-head review record SHA-256:
`bc9f72f5a7a2a2a7011786fb3043fb8713a71388d3555b4405d2838e3e232d63`.
Original cross-process failure witness SHA-256:
`edcd054d10d888db829975d672347613edccabc1259d12fef742e36a291cbbbc`.

Exhaustion intentionally sacrifices availability: failed revocation can leave
access active, and failed settlement retains debt. Existing profiles/defaults,
finite OIDC/restore refusals, disabled source candidates and the active broker
pin remain unchanged. This is neither accepted-store migration nor whole-store
quota implementation.

## Two-version broker qualification

Waypoint [#44](https://github.com/EduCloud-Ecosystem/waypoint/pull/44) merged as
`2317eac63a0bad0d691457b0cde2de14bf6bcc7f` from final reviewed head
`968d0f1c6be4abf1c5b6e3334922ef4c457189b5`. Both share tree
`303a241ebbf153b1acff249823d77ba728e128aa`.
[Final-head CI 39114361047](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39114361047)
passed controls and actual Docker; clean source builds were skipped. CI uses the
unchanged baseline broker and is not a new candidate upgrade workload.
[Post-merge CI 39114499924](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39114499924)
passed those same two jobs at the merge revision; clean source builds were skipped.
The [protocol](https://github.com/EduCloud-Ecosystem/waypoint/blob/968d0f1c6be4abf1c5b6e3334922ef4c457189b5/research-workspace/BROKER-UPGRADE-QUALIFICATION.md)
and [final integration record](https://github.com/EduCloud-Ecosystem/waypoint/blob/968d0f1c6be4abf1c5b6e3334922ef4c457189b5/research-workspace/evidence/2026-10-18/broker-upgrade/integration-after-pr43/README.md)
separate the actual original workload, later corrections and retrospective checks.

The immutable baseline is `5827c84e9952cc67b85e91ceff4282e0ead6923b`; the
candidate is accepted Outfitter #16 merge
`5446438985e31cb739f2048a2aa2176918831a7e`. The builder exports all pinned
production Git sources, disables dependency downloads and records source/build/
binary manifests. Local Go build metadata did not provide a VCS stamp; adjacent
manifests provide integrity evidence, not independent executable authenticity or
a claim of bit-identical builds across directories.

| Control or gap | Result and limit |
| --- | --- |
| Original local workload | **PASS** for 45 unique controls at `89084a70f7341fc11054b9d620d858c214787ced`. Seven sequential Docker attempts: two baseline, five candidate; each 1 CPU, 256 MiB, 64 PIDs, 30 seconds and 65,536 output bytes. Each final receipt records verified cleanup, no unresolved liability and 30 CPU-seconds reserved/charged as an estimated upper bound: **210 total**. No image pull or automatic retry. |
| Consumer/recovery behavior | **PASS** for ordinary and guarded authority/history reads, exact idempotent initialization, old checkpoints to held replacements, stale activation refusal before seal, source-fenced cutover, current revocation, no replay and cumulative charges. Fresh bounded-export Python/R and finite-restore refusal also checked. Four public synthetic bundles verify. |
| Failed workload distinction | **FAIL preserved** at Waypoint independent validation for deliberately obstructed diagnostic output; the broker workload succeeded and retained its 30 CPU-second charge. No result metrics were published. This is one of the seven attempts, not an eighth. Two queued cancellations add no execution charge. |
| Harness defects | **FAIL preserved**: dangling output symlink handling, interrupted final reporting and the final-accounting false pass. Independent fake-caller probes converted 210 charges to zero while the original checker accepted the report, normally and under optimized Python. Exact old source, red probes/logs and original report remain unchanged. One trailing space in a raw failed-test log is intentionally preserved; source/document whitespace checks pass. |
| Corrected oracle | **PASS**: 16 focused controls normally and under optimized Python, included in 384 combined controls. Seven fixed prelaunch bindings identify request/project/image, state role/path hash and broker/request hashes. Final admission/execution/cleanup flags, strict integer 30/30 charges, provenance and 210 total must agree; failure markers and rejected later receipts cannot erase or replace prior valid observations. |
| Retrospective validation | **PASS**: seven retained actual final-status receipts match original private request/config/ledger/binary identities and the corrected accounting checks. These bindings are retrospective: the original run did not record the new prelaunch fields. Zero additional local broker/Docker operations; no final-source candidate workload claim. |
| Independent review/provenance | **CLEAR**: independent broker review ran 16 controls in both modes and 77 accounting mutations; separate root source/provenance review verified final changes. Final manifest binds 25 scoped source, 21 test and seven evidence files; all 304 accepted #43 evidence files and 31 prior qualification packet files remain exact. Both earlier integration documents are archived unchanged. Production modules match accepted #43. |
| Outside the execution claim | Native-v3/consumer-v4 and unresolved ledgers are explicit synthetic read/refusal fixtures, not executed or settled provider workloads. Their uncertainty remains separate from seven actual attempts' cleanup. Hosted identity, live allocation, native execution, physical capacity and whole-writer bounds are **NOT RUN/UNKNOWN** as applicable. |

Original workload report SHA-256:
`b59a8c9c16c5ff89d1b47a3cdc27d6b2766c7eeda40169094967fcbfc833143f`.
Original qualification manifest SHA-256:
`ef0758689dd1d1c9ffb711cba7f352f71649f329bc27005578ed1bc56088d149`.
Accounting-correction manifest SHA-256:
`88cabd278b3b6ba24e3d6c64d26b12d18f91eb4fa0ddddc866de8cf20a60fae9`.
Final integration manifest SHA-256:
`abf4cb8fad61302b0026e9541cdf13ca7bdd41f71ed028119b1374a77b64d494`.
The integration merge carries a DCO `Signed-off-by` trailer, not a cryptographic
signature; the original imprecise wording is preserved with its correction.

No active pin, workflow, runtime/profile/default, accepted store or historical
qualification changed in #44. Separate #45 below adopts the candidate only in
standard Docker CI; optional clean source builds retain the
baseline. Waypoint separately prepares a fresh-profile SQLite reader-ownership
design for root review. Neither work authorizes a checkpoint policy, quota,
accepted-state migration, new service charge or real-data pilot admission.

## Standard Docker CI broker adoption

Waypoint [#45](https://github.com/EduCloud-Ecosystem/waypoint/pull/45) merged as
`d84311621653e2d8e853092cae7c90d0eea02098` from reviewed head
`e16bcd3ad7d28cf6a56845621e65ca38ac526923`. Both share tree
`708be7b0bc3263c2c783a1a1ce0d3be2ac6fda7f`. Exactly one standard `actual-docker`
checkout pin changes to Outfitter `5446438985e31cb739f2048a2aa2176918831a7e`,
with a short provenance/operator note. Optional clean source builds retain
`5827c84e9952cc67b85e91ceff4282e0ead6923b` and all historical evidence stays exact.

[Exact-head CI 39114639604](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39114639604)
and [post-merge CI 39114941093](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39114941093)
passed controls and actual Docker; optional source builds were skipped.
Independent broker review and root scope review are **CLEAR**. The head-CI
artifact audit verifies all nine public files, 41 HTTP checks with recorded
cleanup, 25 recovery checks, 12 guard checks, two successful replays with 60
conservative charged CPU-seconds and five valid bundles. The original failed
historical run remains **NOT RUN** for replay. The suite has 384 controls; these
counts overlap. Forty-eight HTTP and eighteen recovery source hashes match
the exact checkout, also overlapping.

The CI log confirms the selected Outfitter commit, and HTTP/recovery reports
agree on broker binary SHA-256
`bf192806374b348673ef0de171f0866d8c6559c06e12a01d09d7bfa19843bc8f`.
The [preserved public packet](evidence/2026-10-18-ci-broker-adoption/README.md)
retains the reports, bundles, original audit source, metadata and CI log beyond
GitHub's configured fourteen-day artifact retention. Artifact audit SHA-256:
`7a609daf40a8f536f2fcf81efe0838c07a4d50d9dab1f4e494512d5d01b7a35a`.
The frozen audit script records its original path and is not a new portable
operator command. No local broker/Docker workload was repeated for this PR.

This accepts standard CI integration only. No operator's local broker, accepted
state, production/profile/default route, image promotion or cloud/native
execution changes. Existing CI does not establish finite-v3 provider acceptance,
new browser/human acceptance or complete storage capacity. Waypoint's next
scoped task remains the fresh-profile SQLite reader-ownership design; root
design review precedes implementation and checkpoint policy remains outside it.

## SQLite ownership design review

The SQLite ownership proposal received **narrow implementation GO**, not
runtime acceptance, after root and independent review of design-only commit
`8ed88799deba887f11c190381f3101bb8acb3e00`. Proposal SHA-256:
`21f68b9c546136d0ccf2df96d6f69d84909dd2ebdacb32e5d9beba5e562c1012`;
canonical fresh-v4 policy SHA-256:
`ed235fd6d6bb3c10632c0c5dc2bb20c8d3cb9076ebb157c71c1cc9c8072a656e`.
Independent review verified 42 connection/factory sites, two backup sites and
all 402 preserved base files, including 343 evidence files. No runtime/provider
tests ran in this design review. The original remains preserved. Pre-code commit
`4606cc6076999c6bae507bdb6beab4bbd0b0819a` records the required resolved-root hold,
one-note-per-token and keyed-uniqueness clarifications and accepted #45 base
integration; its proposal SHA-256 is
`5b03af41faa8b22830e9af792f185b0716867fd4918075389c2732dc1264ebb2`.
The canonical policy hash is unchanged. The capacity decision records the explicit
ownership-failure safety-denial tradeoff; it grants no checkpoint/drain gate,
whole-store capacity, automatic restart or accepted-state migration.

## Scoped SQLite ownership implementation

Waypoint [#46](https://github.com/EduCloud-Ecosystem/waypoint/pull/46) merged as
`0efc6fd734e7f812cabc3822d2ea93b8c1063752` from reviewed head
`40fe12e62b98f1109cffbe76485d31abf218171b`; both share tree
`de40bb415e570b4ef2136263fad9ba5e6ea50773`. Runtime and tests remain identical
to `43890cbf10a02cd522da627f6ea5a841820a4762`. The later `b2972b2` commit adds
evidence only; the final four-file correction changes current documentation and
provenance without rewriting the frozen qualification or earlier reviews.

The fresh `--scoped-sqlite` profile uses mode `local-finite-public-data-v4`,
authority v4, guard v5 and SQLite user version `0x45464134`. It retains the
reviewed policy hash above. Scoped owners acquire the guard before SQLite,
validate authority and bounded results in one snapshot, and close online
readers before artifact/ZIP/HTTP or provider waits. Separate backup owners keep
their validated immediate source reservation; failed cleanup prevents final
manifest publication. Single-use owners, exact deterministic query contracts,
primitive bindings and detached results constrain the application capability.

| Control or gap | Result and evidence boundary |
| --- | --- |
| Local suite | **PASS**: 433 tests with ResourceWarning treated as an error; JavaScript syntax passed. Includes 49 v4 ownership controls. |
| Frozen qualification | **PASS**: 49 controls and all 29 deliberately broken variants detected, including real two-process contention, same-snapshot bounds, first-error/cleanup handling, full logical-cap safety and both #43 regressions. Deliberate mutation failures are detection evidence, not accepted runtime failures. |
| Independent review | **CLEAR**: fifteen reproduced findings resolved, with original sources, HOLD reviews and witnesses retained. Root independently re-ran the 49 ownership controls at `b2972b2` in 39.422 seconds; runtime/test identity carries to the final documentation-only head. A second source review found no new substantive defect. Counts overlap and must not be added. |
| Final CI | **PASS**: [39120244631](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39120244631) at `40fe12e6`, controls and actual Docker. Optional clean source builds **SKIPPED**. Existing Docker CI exercises older profiles; it is compatibility evidence, not v4 provider qualification. |
| Preservation | **PASS**: 375 current artifact bindings match. All 343 historical evidence files and 395 preserved pre-code files remain byte-identical; the eight other pre-code files are the reviewed runtime changes. Qualification captures 91 source files; independent review captures 517 matching archive members. |
| Failures retained | **FAIL originally, corrected**: cleanup-before-manifest, primary-error loss, caught cursor/native-effect failures, owner reuse/thread misuse, role/script/root/validation bypass, ended snapshots, diagnostic retry, duplicate projections, lost backup reservations, nondeterministic query bounds and disguised SQL strings. Earlier qualification fixture failures and reviewer-check errors remain separately labeled. |
| Holds and liability | **PASS** within the application contract: uncertainty holds every Store/thread at the same resolved root, including safety actions; no constructor/status reset. One diagnostic allowance per existing token cannot create an intent or business writer. Failed revocation cannot certify access removal; failed settlement cannot discharge debt. This is not global quiescence. |
| Unqualified boundaries | **NOT RUN**: v4 actual Docker/provider/browser, human/second-operator acceptance, power-loss/VFS and selected-host capacity. Finite OIDC/restore still refuse. Whole-store capacity stays **UNKNOWN**, quota enforcement **NO-GO/false**, and the frozen fifth-headroom witness **FAIL**. No checkpoint/drain, journal/page, migration, deletion or default change. |

Qualification archive SHA-256:
`cbb0b9242cd45d5aec1d0c356b6f39f90f7efc2ac533d068999dd90c12e75d75`.
Independent runtime review SHA-256:
`baea5b37f265c97480efc0e2e70ee249e28f9b6ac72312ec6e5f788db72369c7`.
Final provenance SHA-256:
`75b24e5cf6f27a0cfd16066e859a351ff2da9c337040faafe2504c1e8a71d37a`.
Documentation-correction SHA-256:
`934d7937377dea05d109a3e09a7b96a14797eba9cd0832e561dc712e7f19fc49`.
[Post-merge CI 39120446555](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39120446555)
also passed controls and actual Docker on the identical merged tree; optional
source builds were skipped. The [coordinating review record](evidence/2026-10-18-scoped-sqlite-coordination/review.json)
retains the separate 49-control log and exact-head CI result.

The coordinating audit corrected a stale current claim that the original replay
cleanup gate remained unresolved. PR32's accepted later observation verifies
the exact container absent, cleanup complete, liability resolved and 30
CPU-seconds conservatively charged. The original failed workload and saved
unknown-cleanup receipt remain unchanged; no refund or candidate promotion
follows. Historical proposal/review wording stays frozen with its source.

## Remaining decisions and next qualification

Next is one bounded qualification-only v4 exercise through production init,
loopback HTTP, Worker, independent Python/R validation and export, owned by
Waypoint with independent Outfitter accounting review. Use two fresh synthetic
projects and already available reviewed images, at most four sequential
30-second attempts and 120 conservative CPU-seconds total. Require prelaunch
identity binding, exact final accounting/cleanup and zero dispatch for queued
cancellation/current-access refusal. Preserve every failure without automatic
retry, refund or a fifth attempt. The four-attempt allowance spans the whole
exercise, including interruption/restart; a new output directory cannot renew it.
The 120 CPU-seconds describe conservative reservations/charges, not total host
overhead or proof that unknown work has terminated. Missing approved existing images/capacity means
NOT RUN. No runtime/profile/default change or purchase is part of this slice.
Independent human reproduction, host/cohort/operator selection and storage,
retention/recovery acceptance remain separate gates after it.

Follow the [sequenced build backlog](../strategy/research-pilot-build-backlog.md)
and [capacity/spending decision record](../decisions/2026-10-17-research-pilot-capacity.md).
No new service subscription is assumed necessary for the current local phase.
Record PASS/FAIL/NOT RUN per control; preserve failed attempts and unknowns.
Kubernetes is an optional post-P1 evaluation before custom multi-host expansion,
not a replacement for Docker or permission to purchase a cluster. Ben's existing
Outfitter issues and assignments remain unchanged. Belay and `portage-local`
remain outside this work.
