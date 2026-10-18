# Research pilot build sequence

Updated October 17, 2026 from the authorized implementation handoff. See the
[acceptance record](../research/2026-10-17-research-pilot-acceptance.md) for frozen
P0/P1 revisions and bounded local results. Package IDs below are local
planning labels, not additions to the shared CC-* prompt namespace.

## Sequence and ownership

| Order | Package | Owner / tracking | Exit evidence |
| --- | --- | --- | --- |
| P0 | Freeze the accepted local workflow | EduCloud; merged Waypoint #26, Outfitter #6, EduCloud #13 | Exact heads/images; two projects; retained failures; CI distinct from local/browser evidence. **PASS** for the bounded local baseline. |
| P1-A | Finish portable environments, trusted replay and coordinated recovery | Waypoint and Outfitter; merged Waypoint #30 and Outfitter #7 | Final heads/reports, scoped independent review and CI; held restore/no allowance revival; no duplicate effects. **PASS** within the local contract; broader gates remain below. |
| P1-B | Capture and rebuild the reviewed images from source | [Waypoint #27](https://github.com/EduCloud-Ecosystem/waypoint/issues/27), closed by merged [#31](https://github.com/EduCloud-Ecosystem/waypoint/pull/31) | **PASS** for native ARM64/AMD64 source construction and automated qualification: 49 checks per platform, two projects/both conditions and lineage. Four source candidates remain disabled. Human reproduction, promotion and durable image distribution remain separate gates. Original failures are retained. |
| P1-C | Independent second-operator exercise | [Waypoint #28](https://github.com/EduCloud-Ecosystem/waypoint/issues/28), unassigned | Second machine, no core edits, trusted bundle digest, exact results, supported restore, elapsed time/help and missing controls. **NOT RUN**. |
| P2-A | Evaluate optional Kubernetes backend | Outfitter execution/accounting; Waypoint artifacts/storage; EduCloud decision | Bounded isolated disabled prototype or blocked protocol; comparison, failures and adopt/defer/reject record. Starts after P1; existing institutional capacity discovery may proceed earlier. |
| P2-B | Durable Jetstream2 native-unit journal and independent cleanup | Existing [Outfitter #1–#4](https://github.com/EduCloud-Ecosystem/outfitter/issues/1), assigned to Ben; merged [PR #8](https://github.com/EduCloud-Ecosystem/outfitter/pull/8) | **PASS** for the local/simulated journal and cleanup implementation after two independent-review fixes. Final CI: 115 tests/subtests, 26 Docker checks, 38 recovery checks. Live provider, independent-host supervisor and settlement remain **NOT RUN**. |
| P2-C | One direct local inference qualification | Portage [#9](https://github.com/EduCloud-Ecosystem/portage/issues/9); merged PRs [#10](https://github.com/EduCloud-Ecosystem/portage/pull/10)/[#11](https://github.com/EduCloud-Ecosystem/portage/pull/11) | **PASS** for 95 synthetic qualification controls and final CI after readiness/reporting corrections. All 12 actual-engine gates remain **NOT RUN**. Await approved existing host/model/operator manifest; optional for Python/R. |
| P2-D | Shared institutional pilot | [Waypoint #29](https://github.com/EduCloud-Ecosystem/waypoint/issues/29), unassigned | Hosted synthetic identity/revocation, tested storage/retention/restore/capacity, accessible journeys and named service owners. |
| After execution contract | Synthetic coursework handoff | Existing [Outfitter #5](https://github.com/EduCloud-Ecosystem/outfitter/issues/5), Ben; Cairn and Waypoint consumers | Verified course authority, bounded owned worker, independent result and cleanup evidence; no live-course data implied. |

The three new Waypoint issues were created unassigned after checking for existing
issues; #27 is now closed by its source-build PR. Outfitter #1–#5 remain assigned to `bmarkwart`; no
assignment, issue state or contributor message was changed. Module-scoped changes
stay in focused component PRs. Parallel implementation must preserve component
ownership and exact integration pins.

## Next implementation slices

The continuing component chats own these focused increments after their current
PR reviews. An assignment below is not evidence that implementation or acceptance
has completed. Each increment receives independent review and final-revision
checks before merge. Existing issues stay open for their broader acceptance gates.

| Sequence | Component and tracking | Concrete next result | Remaining boundary |
| --- | --- | --- | --- |
| 1, complete | Waypoint, merged [#32](https://github.com/EduCloud-Ecosystem/waypoint/pull/32) | Hash-linked supplemental observation: exact container ID/name absent, matching ledger cleanup verified with no unresolved liability, 30 CPU-seconds conservatively charged. Original failed report/receipt unchanged. | No refund, replay, shared Docker restart or relabelling of the failed workload. |
| 2 | Waypoint [#29](https://github.com/EduCloud-Ecosystem/waypoint/issues/29) | Disposable local synthetic Keycloak/proxy sign-in; stable issuer/subject mapping; current identity and project membership checked at request, dispatch and publication; visible service loss, truthful logout and restore invalidation. Four identities/two projects, browser/API failure controls and credential-leak checks. | Loopback-only rehearsal, no hosted/private-data admission. Existing key mode stays separate. Manual accessibility, capacity, storage and institutional operational approval remain open. |
| 2, complete locally | Outfitter, merged [PR #9](https://github.com/EduCloud-Ecosystem/outfitter/pull/9), partial contract supporting existing [issue #5](https://github.com/EduCloud-Ecosystem/outfitter/issues/5) | Durable synthetic consumer preflight/run/status in the existing ledger. Final CI includes 19 actual consumer checks; duplicates return the receipt, changed bindings conflict and unknown work cannot redispatch. | No production Cairn Runner, automatic retry, new ledger or live Jetstream2 handoff. Local contract evidence cannot close the live-provider acceptance sequence or change Ben's assignment. |
| 2, complete offline | Portage, merged [PR #12](https://github.com/EduCloud-Ecosystem/portage/pull/12), supporting [issue #9](https://github.com/EduCloud-Ecosystem/portage/issues/9) | Hash-bound qualification/capacity review packet preserves tested identities, failures/skips, unknown liabilities and missing fields; 61 focused tests passed. | No engine/network/subprocess execution, model download or ledger mutation. Review output cannot grant execution, spending, promotion or hosted readiness. |
| 3 | Cairn local synthetic adapter; Outfitter contract | Assess and build the smallest opt-in disposable harness using actual Runner/PolicyRunner boundaries and durable job binding. Generic retries must not relaunch unknown work; deterministic Cairn checks retain grading authority. | No production configuration/default/runner change, deployment or real course records. Keep live/second-operator issue #5 gates open. |
| 3 | Portage operator decision | Produce a concrete packet from current read-only capacity/model evidence and the accepted tool; identify the minimum host/model/operator/window choices. | No engine start, model acquisition or live execution. Missing capacity remains a reason to defer. |
| 3 | Waypoint [#29](https://github.com/EduCloud-Ecosystem/waypoint/issues/29), after identity | Whole-store inventory and admission limits, then a read-only retention plan. Test byte/file/output limits and protect authority, unresolved jobs, failed controls and recovery dependencies. | Archive bounds alone are not store quotas. Deletion requires tested tombstone/restore reconciliation and an explicit retained-evidence policy. |

The source-image candidates remain disabled through these increments. Independent
human reproduction (#28), image retention/distribution, selected host/cohort,
support ownership and live provider/model qualification remain visible decisions.
Continue the local work without buying capacity to make those gates appear green.

## P2-A: optional Kubernetes evaluation protocol

Docker remains the default development and acceptance backend. Before building
custom multi-host orchestration, determine whether a supported institutional
cluster solves an actual pilot requirement. Record operator support, authorized
capacity, storage/network constraints and maintenance responsibility. Discovery
alone grants neither cluster access nor permission to create resources.

After P1, prepare an isolated, disabled-by-default prototype against existing
approved capacity or a disposable approved local environment. Its finite manifest
must record cluster/runtime versions, operator, two synthetic projects, reviewed
Python/R image and platform digests (registry-resolvable or verified import),
per-attempt CPU/memory/PID/output/lifetime caps, concurrency, cumulative allowance,
absolute test end time and owned teardown. No environment available means runtime
controls are **NOT RUN**; finish the design/protocol without purchasing a cluster.

| Control group | Required exercise and evidence |
| --- | --- |
| Equivalent workload | Same fixture inputs, two projects, Python/R baseline/alternative conditions and declared tolerances; export comparable methods, lineage and failed outcomes. Keep Docker controls passing. |
| Admission and attempts | Durable reservation before every possible execution, stable request plus attempt IDs, duplicate/ambiguous API response handling, and controller replacement/retry behavior. Any unreserved controller-created attempt fails qualification. Repeated completion cannot publish twice or refund another attempt. |
| Faults and cancellation | Pod loss, node loss, broker restart, API loss, cancellation, deadline expiry and ambiguous create. Preserve failure output and unknown liabilities; reconcile before retry/settlement. Label simulated local node loss separately from an independent host/control-plane failure. |
| Isolation | Cross-project resource, secret and artifact access; scoped service accounts/authorization; effective network denial; storage permissions and execution limits. A namespace label is not acceptance. Reviewed recipes only. |
| Consistent state | Explicit artifact transfer and single-writer or separately validated shared database design. No shared-network SQLite or extra application replicas without consistency acceptance. Coordinated restore retains current revocations/deletions and uncertain accounting before access reopens. |
| Cleanup and retained costs | Independent observation removes test-owned jobs/pods/disposable resources and preserves foreign resources/evidence. Report retained volumes, underlying VM charges and unsettled provider units separately from workload deletion. Resource quotas supplement the cumulative Outfitter ledger. |
| Measured decision | Compare completion time, throughput, idle/control-plane overhead, setup/recovery effort, recurring maintenance and operator availability against Docker. Record actual institutional requirement, PASS/FAIL/NOT RUN controls and recommend **adopt**, **defer** or **reject**. Migration requires an explicit later decision. |

The attempt-accounting requirement follows Kubernetes' documented possibility of
multiple program starts even with one completion and parallelism one.
[Job behavior](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
was checked October 17. Isolation also needs authorization, networking and
storage controls beyond namespaces, and network-policy enforcement depends on
its implementation. [Multi-tenancy guidance](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
was checked the same day. [Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
limit namespace resource/object consumption; this plan retains separate
cumulative allowance and native-SU accounting. These sources justify controls,
not a claim that any untested cluster currently meets them.

## P2-B: preserve the bounded Jetstream2 milestone

1. Extend the existing durable reservation pattern to a native-SU journal with
   immutable request/attempt ownership and absolute expiry. Do not translate local
   CPU-seconds into SUs or allocation credits without a verified rate/contract.
2. Implement an independent supervisor that recovers after both broker and worker
   loss. Mocked failure controls must cover ambiguous create, restart, timeout,
   cleanup failure, retained storage and foreign-resource refusal.
3. Prepare one CPU-worker live-test manifest: approved allocation/region, pinned
   image, network, dated flavor rate, named operator, concurrency one, finite SU
   ceiling, lifetime, teardown and independent observation. No GPU expansion.
4. Present the complete manifest before any live allocation consumption or new
   charge. Only separate approval permits the live lifecycle and subsequent
   synthetic Cairn/Waypoint handoff.

Existing tracking remains [#1 contract/preflight](https://github.com/EduCloud-Ecosystem/outfitter/issues/1),
[#2 broker/reservations/Docker](https://github.com/EduCloud-Ecosystem/outfitter/issues/2),
[#3 adapter/live worker](https://github.com/EduCloud-Ecosystem/outfitter/issues/3),
[#4 recovery/cleanup](https://github.com/EduCloud-Ecosystem/outfitter/issues/4),
and [#5 consumer handoff](https://github.com/EduCloud-Ecosystem/outfitter/issues/5).
The Kubernetes evaluation does not broaden these assignments.

## P2-C and P2-D: admission beyond one local operator

Portage qualification starts only with an approved available engine/model and
capacity. Record model revision, template, quantization, context/output limits,
endpoints and workload, then test identity/project attribution, destination/model
policy, exhaustion, concurrency, streaming/non-streaming cancellation and engine
loss. Missing usage remains reserved. Report latency, supported concurrency,
memory use and restart separately from task quality. No inference dependency is
added to the reviewed Python/R workflow.

Waypoint's shared pilot must test current synthetic identity and memberships
before dispatch/publication, whole-store limits, retention/deletion and restore,
and selected-capacity overload/failure behavior. Browser/manual accessibility,
new instructor/researcher completion, named support/retirement owners and approved
data destinations remain explicit gates. A source-fenced local replacement is
not acceptance of source-loss recovery on another host.

PAIR remains a separate optional experiment requiring two already available
trusted machines and its own finite comparison/adoption decision. Belay,
`portage-local`, MESA, Modal and the separate Zensical preview are not expanded by
this backlog. Do not add workflow platforms or tracking stacks until two concrete
workflows and a maintainer justify the dependency.
