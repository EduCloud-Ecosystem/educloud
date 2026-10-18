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
| Direct local inference | Portage #10/#11 accepted the finite gateway and synthetic qualification controls; #12 supplies the offline review packet; #13 fixes confirmed approval-expiry races. The concrete operator packet is prepared, but the inspected inventory identified no approved installed model; live qualification remains NOT RUN. | Assign an approved existing host, permitted installed model/template, operator and finite limits/window. If unavailable, defer. Model acquisition or expanded capacity requires its own explicit decision; the software path requires no new subscription. |
| Hosted inference candidate | Jetstream2's existing hosted API is recommended for a first synthetic/public shared pilot; this is not Greg's selection or authorization. A separate offline design/decision packet is being prepared. | Verify account access and permitted application/credential use, endpoint behavior, data destination, supported model identity, request/usage bounds and operational owner. Preserve unknown remote work and distinguish unavailable engine internals from direct local qualification. No live API calls or default-route change. |
| PAIR / multi-node hardware | Separate experiment; deferred without two approved available machines. | Separate finite protocol and adoption evidence. No hardware purchase or default-route change. |

Except for the dated published inference terms below, no current prices,
discounts, availability guarantees or entitlement amounts are asserted here.
An older status document's historical price is not an approved quote for a new
deployment.

## Inference host recommendation, not authorization

The [Jetstream2 hosted service](https://docs.jetstream-cloud.org/inference-service/overview/)
documentation, checked October 17, states that its inference API has no usage
charge or Jetstream2 SU consumption for ACCESS users. Its models can change and
the service can have maintenance interruptions. It processes data at IU and
administrators may inspect interactions. These are published service terms,
not measured performance, private/student-data approval, an uptime guarantee or
verified access for this pilot.

The [API access guide](https://docs.jetstream-cloud.org/inference-service/api/)
distinguishes an authenticated Open WebUI proxy from direct inference backends
restricted to Jetstream2/IU networks. Their API capabilities differ. An account
key is private and must not be shared; suitable application identity and
multi-user use remain to be confirmed. No key was obtained or endpoint tested.

For experiments needing controlled model versions, a dedicated GPU host remains
an alternative subject to allocation and independent-cleanup gates. Current
[instance specifications](https://docs.jetstream-cloud.org/general/vmsizes/)
list `g3.large` with 20 GB A100 GPU memory, 60 GB system RAM and 32 SUs/hour;
GPU entitlement is separate from CPU allocation. This is a sizing candidate,
not a resource reservation, benchmark, dollar price or approved purchase.
The existing M1/16 GB iMac is a candidate for small local Ollama tests; hardware
presence does not establish available capacity or measured model fit. Hosted
API evidence cannot replace the separate local engine qualification gates.

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
