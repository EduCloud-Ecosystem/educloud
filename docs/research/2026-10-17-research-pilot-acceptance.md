# Research pilot acceptance — 17 October 2026

**P0 local baseline and P1 portability/recovery implementation: accepted and
merged.** Clean image builds and independent second-machine acceptance remain
**NOT RUN**. This record freezes the research-workspace release separately
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
| Clean Python/R builds from pinned source | **NOT RUN** | [Waypoint #27](https://github.com/EduCloud-Ecosystem/waypoint/issues/27). A separate bounded implementation chat has started; no successful build is inferred from dispatch. |
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

## Remaining decisions

Follow the [sequenced build backlog](../strategy/research-pilot-build-backlog.md)
and [capacity/spending decision record](../decisions/2026-10-17-research-pilot-capacity.md).
No new service subscription is assumed necessary for the current local phase.
Record PASS/FAIL/NOT RUN per control; preserve failed attempts and unknowns.
Kubernetes is an optional post-P1 evaluation before custom multi-host expansion,
not a replacement for Docker or permission to purchase a cluster. Ben's existing
Outfitter issues and assignments remain unchanged. Belay and `portage-local`
remain outside this work.
