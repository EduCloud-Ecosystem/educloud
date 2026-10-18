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
| Research-store logical growth | Waypoint #39 accepts the offline writer contract; #40 implements fresh local-key finite logical authority; #41 qualifies unchanged SQLite/guard write paths. This is not whole-store capacity. | Row/session/encoded-field limits and safety actions are qualified offline; finite OIDC and restore explicitly refuse. Next design bounded export-reader lifetime; Outfitter Docker writer qualification remains in review. Recurring WAL, replacement scratch, broker writers and destination peaks remain UNKNOWN; no quota wiring or accepted-store migration. |
| Source-image builds and independent reproduction | Use existing approved local/CI capacity first. | Source/base/package inputs, build resource envelope and second operator/machine. If unavailable, mark NOT RUN and prepare alternatives; do not buy hardware automatically. |
| Institutional worker/backup destination | No new host, storage plan or backup account selected here. | Named owner, data classes, cohort/concurrency, retention, measured recovery target, full resource bill and bounded pilot term. |
| Jetstream2 | Native-SU journal and simulated independent cleanup accepted in Outfitter #8; the local consumer bridge is accepted in #9. The blocked operator/rescue packet merged in #10, simulated two-process rescue in #11, metadata compatibility in #12 and one-attempt offline enforcement in #13. The reviewed supplemental operational packet in #14 recommends restricted private SSH and independent cleanup without selecting allocation/hosts/access. No live worker authorized here. | Verified allocation permissions, current rate/terms, maximum one CPU worker, explicit native-unit reservation, expiry and independent teardown. The proposed 1 SU allowance is not a provider-enforced charge ceiling. Quota/access is not capacity or permission to consume an allocation. Independent-host cleanup, terminal late effects, authenticated guest bootstrap, private execution/result transfer and live transport remain engineering/operational gates; approval alone cannot close them. |
| Kubernetes | Optional disabled evaluation; supported institutional-capacity discovery may begin. | Approved cluster/local environment and operator, finite attempt/accounting manifest, storage/restore/isolation plan, overhead/maintenance comparison. No cluster purchase or production change. |
| Direct local inference | Portage #10/#11 accepted the gateway and invocation-bounded synthetic protocol; #12 supplies the offline review packet; #13 fixes approval-expiry races. The later repeated-process failure is corrected offline in #15 with persistent authority/attempt slots; original failed evidence is retained. No approved installed model was identified and all twelve live qualification gates remain NOT RUN. | Assign an approved existing host, permitted installed model/template, operator and finite limits/window, with explicit existing-store grant registration. If unavailable, defer. Model acquisition or expanded capacity requires its own explicit decision; the software path requires no new subscription. Offline counters do not qualify real engine behavior or resource bounds. |
| Hosted inference candidate | Jetstream2's existing hosted API is recommended for a first synthetic/public shared pilot; this is not Greg's selection or authorization. Portage #14 accepts the pure fixture contract, without transport, credentials, ledger mutation or live eligibility. | Verify account access and permitted application/credential use, endpoint behavior, data destination, supported model identity, persistent request/usage bounds and operational owner. Preserve unknown remote work and distinguish unavailable engine internals from direct local qualification. No live API calls or default-route change. |
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

## Finite-authority engineering decision

The separate fresh opt-in local-key profile authorized after Waypoint #39 is
implemented and accepted in [#40](https://github.com/EduCloud-Ecosystem/waypoint/pull/40).
Its offline controls qualify logical row/session and serialized-field ceilings.
Initial engineering
limits are 128 total users, 20 total projects, 1024 membership rows, 1000 recorded
runs and 256 live sessions with eight per subject, retaining tighter existing
per-project/queue limits and eight-hour expiry. Revoked users, closed projects
and failed/interrupted runs still count toward history limits. These values are
test-profile policy, not measured disk fit, workload throughput, approved host
capacity or permission to execute 1000 broker runs.

Bind the versioned profile to the existing configuration/database/guard authority;
missing or unsupported bindings refuse. All entry points must enforce the same
limits, and restore must preserve them or explicitly refuse. New rows and
sessions are admissions. Existing-session access, logout, demotion/removal,
revoke/rotate, cancellation and conservative settlement retain their safety
behavior at the caps. Oversized terminal data must not refund unknown work or
fabricate success. No alternate capacity ledger, deletion, journal/default change
or accepted-store migration belongs in this increment. Checkpoints preserve the
finite binding; finite restore/cutover and OIDC explicitly refuse. Existing
Docker CI covers compatibility, not new finite-profile provider qualification.

Waypoint's source-pinned SQLite/guard bounded-write qualification is accepted in
[#41](https://github.com/EduCloud-Ecosystem/waypoint/pull/41); Outfitter's Docker
broker storage-writer protocol remains in review. The disposable witnesses
distinguish implemented per-save limits from proposed bounds and
UNKNOWN peaks, account for current plus temporary generations and retry residue,
and avoid inferring all writers have stopped from parent exit or settled compute.
The active broker pin remains unchanged pending separate integration acceptance.
Broader enforcement requires a reviewed concrete protocol before wiring; this
assignment does not enable quotas, recovery, migration, deletion or default
journal changes.

The next Waypoint design isolates export read lifetime: capture a bounded
manifest, close the SQLite reader before artifact I/O, verify captured content,
build the bundle, then recheck exact metadata and current local authority before
returning bytes. The final check is the authorization point; locks/readers must
not span HTTP streaming. Changes or read failures refuse without automatic retry,
partial publication or accounting mutation. Prepare an explicit fresh opt-in
version/binding contract for independent review before implementing; preserve
existing profiles and identity/recovery refusals. This is a narrow reader fix,
not an all-reader census, checkpoint policy or WAL/capacity guarantee. Guard
scratch slots and engine ceilings remain separate later decisions.

Whole-store quota admission remains **NO-GO**. SQLite/WAL/reader peaks, recurring
replacement/failure scratch, broker/watchdog ownership and restore destination
peaks need separate proof. The fifth failed headroom witness is retained. This
offline implementation needs no purchase or new user architecture decision; live
provider, selected host/model and operational decisions remain separate.

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
