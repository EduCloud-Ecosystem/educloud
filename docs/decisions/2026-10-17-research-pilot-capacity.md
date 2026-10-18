# Research pilot capacity and spending decision

Date: 17 October 2026. Status: **continue local implementation; no new paid
service selected or approved by this record**.

The user authorized platform buildout and asked that paid dependencies be fully
prepared and surfaced before they create cost. The present Python/R workflow,
portable evidence and local recovery use existing tools/capacity. No additional
service subscription is assumed necessary for this phase. This is a scope choice,
not a claim that machines, electricity, labor or existing accounts are cost-free.

The next capacity decision follows measured requirements and the
[sequenced backlog](../strategy/research-pilot-build-backlog.md). Docker stays the
baseline. Kubernetes is an optional evaluation after P1 and before custom
multi-host expansion; it is not an adoption, managed-cluster or migration decision.

## Current decisions

| Dependency | Current disposition | What must be prepared before spending or live use |
| --- | --- | --- |
| Local Python/R and recovery work | Continue within existing approved capacity and finite test budgets. | Exact image/platform, bounded workload, disk/output needs and cleanup; record actual capacity limits rather than infer them from green unit tests. |
| Source-image builds and independent reproduction | Use existing approved local/CI capacity first. | Source/base/package inputs, build resource envelope and second operator/machine. If unavailable, mark NOT RUN and prepare alternatives; do not buy hardware automatically. |
| Institutional worker/backup destination | No new host, storage plan or backup account selected here. | Named owner, data classes, cohort/concurrency, retention, measured recovery target, full resource bill and bounded pilot term. |
| Jetstream2 | Native-SU journal and simulated independent cleanup accepted in Outfitter #8. Continue the local synthetic consumer bridge; no live worker authorized here. | Verified allocation permissions, current rate/terms, maximum one CPU worker, explicit SU ceiling, expiry and independent teardown. Quota/access is not capacity or permission to consume an allocation. |
| Kubernetes | Optional disabled evaluation; supported institutional-capacity discovery may begin. | Approved cluster/local environment and operator, finite attempt/accounting manifest, storage/restore/isolation plan, overhead/maintenance comparison. No cluster purchase or production change. |
| Inference | Portage #10/#11 accepted the finite gateway and synthetic qualification controls. Live qualification remains NOT RUN; an offline review packet is next. | Assign an approved existing host, permitted installed model/template, operator and finite limits/window. If unavailable, defer. Any paid API, model acquisition or expanded plan requires its own explicit decision; the software path requires no new subscription. |
| PAIR / multi-node hardware | Separate experiment; deferred without two approved available machines. | Separate finite protocol and adoption evidence. No hardware purchase or default-route change. |

No current vendor prices, discounts, availability guarantees or entitlement
amounts are asserted in this record. An older status document's historical price
is not an approved quote for a new deployment.

## Reviewable cost packet

Prepare all implementation that can be tested without the paid dependency, then
fill this packet before asking Greg for the final spending decision. Keep secrets
and account credentials outside Git. Unknown fields block purchase/provisioning;
they are not treated as zero.

| Required field | Reviewable content |
| --- | --- |
| Need and alternatives | Concrete workload/control requiring the dependency; why existing capacity is insufficient; no-spend/deferred option and its limitation. |
| Exact resource | Provider, account/allocation owner, product/SKU, region, CPU/RAM/GPU if relevant, storage type/capacity, network/egress and architecture. |
| Primary-source terms | Official rate/terms URL or operator-provided institutional quote, retrieval date, currency, billing interval, eligibility/credit expiry and known exclusions. Recheck immediately before commitment. |
| Finite request | Maximum count/concurrency, test or pilot start/end, execution allowance in native units, storage retention, teardown deadline and maximum lifetime. |
| Full exposure | One-time and recurring totals; compute, persistent storage, snapshots/backups, idle/control-plane charges, transfer, taxes/fees where known, overage and auto-renewal. Unknown exposure remains explicit. |
| Controls | Admission and provider budget limits, independent cleanup, alert threshold, stop rule, failure/reconciliation procedure, and how unresolved resource charges stay visible. |
| Operations | Named service/billing owner, support and credentials plan, backup/restore responsibility, data approval and retirement/export procedure. |
| Decision | Exact maximum initial and recurring amount/native-unit allowance, approved term and resources, approver/date, and conditions. No approval is inferred from engineering authorization or account access. |

At the spending boundary, tell Greg what is ready, what exact action would incur
cost, the ceiling and recurring exposure, and the no-spend alternative. Wait for
the specific commitment authorization. Do not purchase, subscribe, increase a
plan, provision new paid infrastructure, or launch a live allocation test while
that decision remains absent. Continued local/mocked implementation does not
need to stop for an unrelated missing purchase decision.

## What this record does not approve

No new cloud purchase, live allocation test, production deployment, Kubernetes
adoption, private participant/student data, or stronger isolation claim. No new
message to a contributor or reassignment of Ben's Outfitter issues. Scientific
study design/consent and institutional destination/retention approval remain
separate from successful runtime checks.
