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

## Remaining decisions

Follow the [sequenced build backlog](../strategy/research-pilot-build-backlog.md)
and [capacity/spending decision record](../decisions/2026-10-17-research-pilot-capacity.md).
No new service subscription is assumed necessary for the current local phase.
Record PASS/FAIL/NOT RUN per control; preserve failed attempts and unknowns.
Kubernetes is an optional post-P1 evaluation before custom multi-host expansion,
not a replacement for Docker or permission to purchase a cluster. Ben's existing
Outfitter issues and assignments remain unchanged. Belay and `portage-local`
remain outside this work.
