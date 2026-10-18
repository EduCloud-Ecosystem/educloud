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
| Research-store logical growth | Waypoint #39 accepts the offline writer contract; #40 finite authority; #41 SQLite/guard qualification; #42 bounded export; #43 fixed guard publication slots; #46 scoped SQLite ownership in fresh v4. Outfitter #15 qualifies writer counterexamples and #16 prevalidates serialization. Waypoint #44 qualifies two broker versions; #45 adopts the candidate in standard Docker CI only. This is not whole-store capacity. | Next: bounded v4 qualification through existing local Docker/HTTP, with at most four sequential attempts. Finite OIDC/restore refuse. WAL, other scratch, broker writers and destination peaks remain UNKNOWN; no checkpoint/journal policy, quota wiring or accepted-store migration. |
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
broker storage-writer qualification is accepted in [#15](https://github.com/EduCloud-Ecosystem/outfitter/pull/15).
The disposable witnesses
distinguish implemented per-save limits from proposed bounds and
UNKNOWN peaks, account for current plus temporary generations and retry residue,
and avoid inferring all writers have stopped from parent exit or settled compute.
The active broker pin remains unchanged pending separate integration acceptance.
Broader enforcement requires a reviewed concrete protocol before wiring; this
assignment does not enable quotas, recovery, migration, deletion or default
journal changes.

Waypoint [#42](https://github.com/EduCloud-Ecosystem/waypoint/pull/42) implements
the reviewed export read-lifetime design: capture a bounded
manifest, close the SQLite reader before artifact I/O, verify captured content,
build the bundle, then recheck exact metadata and current local authority before
returning bytes. The final check is the authorization point; locks/readers must
not span HTTP streaming. Changes or read failures refuse without automatic retry,
partial publication or accounting mutation. Independent code review and
exact-head/post-merge CI passed, with existing profiles and identity/recovery
refusals preserved. This is a narrow reader fix,
not an all-reader census, checkpoint policy or WAL/capacity guarantee. Guard
scratch slots and engine ceilings remain separate later decisions.

The reviewed `init --bounded-export` contract uses mode
`local-finite-public-data-v2`, policy `educloud-finite-authority-v2` with
`export_protocol: educloud-bounded-export-v1`, guard v3 and database marker
`0x45464132`. Existing v1/default behavior remains separate; mixed, missing or
downgraded binding tuples refuse, including direct restore entry points. Offline
runtime acceptance is recorded in the research acceptance record. Original proposal SHA-256
`eabfa3fd139c98785d168415ba3aaf7ba6be0beb35c7fde815806ad0de4f23d9` received two
clarifications before coding; corrected proposal SHA-256
`8fa312c32da9e96a8067b0e8ddb964d4eb81d5ac94efda72caff681141a4d6c2`.
Final equality proves current exact state, not detection of a transient change
later reverted. Files copied and verified earlier are the artifact snapshot;
subsequent file changes cannot alter those bytes. The final private comparison
includes cancellation and session/user/membership fields without publishing them.
No database reader or guard lock spans artifact reads, ZIP construction or HTTP
streaming; the new helper requires a session token and rejects subject-only
publication. The implemented contract SHA-256 is
`e3023285a5424d0e289a6cb847b0fb96842f03252bf396cf256467841d3154c0`.

Waypoint [#43](https://github.com/EduCloud-Ecosystem/waypoint/pull/43) implements
the separately reviewed fresh opt-in guard publication profile: fixed ordinary and
safety scratch roles under the existing
guard lock, exclusive no-follow creation and no adoption, overwrite or deletion
of residue. Ordinary failure notes must not consume the safety slot. Define
exact-incarnation binding, restart/post-rename uncertainty and explicit safety
slot exhaustion that fails while retaining debt rather than bypassing intent.
Current plus two 4 MiB candidates could bound this logical guard family to
12 MiB only for fresh controlled state. This conditional named-payload bound
excludes SQL/WAL and other writers. Preserve existing profiles/defaults,
OIDC/restore refusals and historical evidence. No quota admission, cleanup or
new capacity ledger belongs in this design.

Reviewed proposal SHA-256:
`d6024965ee196cde9a0ad8773600e3ae54338c71e5aedf8c0784741d792969a3`.
Corrected pre-code contract SHA-256:
`d9fa59065b8f8a831c58b4af58f7ab02e96b085d85453bdf963e98ac7bf8a78a`.
The required correction caches only durability qualification of the exact
current incarnation, never permission, receipt outcomes or namespace cleanliness.
Every mutation/publication must recheck relevant residue and holds under the lock
even when current bytes are unchanged. Qualification must include process B
observing new failed scratch left by A without replacing current. Takeover
barriers precede business transactions. Unresolved essential intent cannot be
borrowed; ordinary failure notes cannot consume the safety slot. Exhaustion
explicitly sacrifices availability: failed revocation may leave access active,
and failed settlement retains debt. This tradeoff is accepted only for the fresh
opt-in profile. Corrected head `b063dc99` passed 368 local controls, independent
runtime reviews and exact-head CI and merged as `5f2b21f1`. Review reproduced and
fixed premature cancellation-token release and blocked request preparation after
an unrelated process published; original failures remain preserved. Actual new-profile
provider, physical-exhaustion and human acceptance remain NOT RUN.

After Outfitter #15 qualification acceptance, independent design review cleared
the separate narrow ledger/output serialization fix implemented in
[#16](https://github.com/EduCloud-Ecosystem/outfitter/pull/16). Inside the existing ledger
transaction, compute output digests and encoded lengths before sidecar effects;
validate each diagnostic-success and diagnostic-failure record form, then the
largest mixed-outcome ledger using all native/consumer fields and existing limits.
Retain only one encoded output buffer at a time. Persist outputs sequentially and
publish the validated forms matching those outcomes. Diagnostic failure retains
conservative accounting. Tests must prove mixed failures and invalid/oversized
plan refusal before output-file effects. Later I/O failure can still leave
orphans or uncertain publication; no repeated-scratch or all-writer bound follows.
Keep the active Waypoint broker pin unchanged pending separate integration
qualification. No new capacity ledger, quota, snapshot/watchdog/cutover redesign,
provider default or live allocation work belongs in this fix. Exact-head runtime
review and exact-head/post-merge CI passed. Existing per-record and
whole-ledger limits are unchanged, and the two original failures remain retained.

Before adopting the candidate broker, qualify the actual Waypoint consumer with
two immutable binaries: existing `5827c84e9952cc67b85e91ceff4282e0ead6923b` and
Outfitter #16. Existing one-binary recovery tests do not prove old-authority or
old-checkpoint compatibility. Use disposable synthetic state to prove unchanged
local-v2 identity/accounting/diagnostics, old checkpoint to held replacement,
source fencing, stale/unknown refusal and exact receipt validation. Native-v3 and
consumer-v4 states are outside this Waypoint adoption contract; do not strip or
downgrade them. Preserve historical broker pins and failed controls. This is
preparation for a separate reviewed integration/pin PR, not an active pin change,
accepted-store migration, live provider permission or broader storage guarantee.

That qualification is accepted in Waypoint #44, reviewed head `968d0f1c`, merge
`2317eac6`. The original run at `89084a70` recorded 45 controls and seven
sequential attempts with verified cleanup and 210 conservative CPU-seconds.
Review corrected a checker false pass that accepted final zero-charge refusals.
Sixteen focused controls, 384 combined tests, exact-head CI and retrospective
validation of the seven retained receipts pass; the original workload was not
rerun or relabeled. Native/consumer fixtures remain outside actual execution.
The separate standard `actual-docker` CI broker pin update merged in Waypoint
#45 as `d8431162`, reviewed head `e16bcd3a`, selecting
`5446438985e31cb739f2048a2aa2176918831a7e`. Exact-head CI and artifact inspection
passed its existing HTTP/replay/recovery/guard checks. Optional clean source
builds stay on `5827c84` and historical manifests remain untouched. This is CI
adoption, not an accepted-store upgrade or finite-v3 provider qualification.

Waypoint separately owns a concrete design for fresh-profile SQLite connection
ownership. Short online reads must follow guard-before-database order, return
bounded materialized results and close before artifact, HTTP or provider waiting.
Preserve dispatch's final authorization fence and the offline checkpoint's
distinct frozen-source consistency boundary. Open/read/close failures cannot
certify quiescence or reclaimed capacity; external readers can still retain WAL.
Root and independent design review give **narrow implementation GO** for the
fresh v4 profile at proposal SHA-256
`21f68b9c546136d0ccf2df96d6f69d84909dd2ebdacb32e5d9beba5e562c1012`,
canonical policy `ed235fd6d6bb3c10632c0c5dc2bb20c8d3cb9076ebb157c71c1cc9c8072a656e`.
Accept the rejection-only bootstrap discriminator and an explicit new
availability tradeoff: actual unconfirmed open/cleanup holds normal readers and
writers, including safety calls, for the same resolved root within that process.
Constructor/status calls cannot clear the hold; different roots stay independent.
Clean full-cap safety operations must remain available. Failed revocation cannot
claim access removal, and failed settlement cannot discharge debt.

One original-role diagnostic exception is allowed per existing operation token,
never per nested owner. It cannot create intent, open business SQL, run a barrier
or recursively log its own failure. Untokened startup/barrier failures remain
held without inventing an origin note. Keyed lookups enforce uniqueness; a
bounded claim selection must still choose one of multiple queued runs. Preserve
v0–v3 and shared-helper behavior, same-snapshot binding checks, dispatch/export
fences and offline source consistency. Preserve the original proposal, add these
clarifications and refresh provenance on accepted #45 before runtime changes.
The clarified pre-code contract is recorded at
`4606cc6076999c6bae507bdb6beab4bbd0b0819a`, proposal SHA-256
`5b03af41faa8b22830e9af792f185b0716867fd4918075389c2732dc1264ebb2`;
the canonical policy hash is unchanged. The implementation is accepted locally
in Waypoint [#46](https://github.com/EduCloud-Ecosystem/waypoint/pull/46), reviewed
head `40fe12e62b98f1109cffbe76485d31abf218171b`, runtime
`43890cbf10a02cd522da627f6ea5a841820a4762`. The 433-test suite includes 49 ownership
controls; frozen qualification detects all 29 deliberate regressions.
Independent source/evidence reviews, a separate 49-control recheck and final-head
CI pass after fifteen retained review findings were corrected. These overlapping
counts establish the local application contract, not physical capacity or v4
Docker/provider acceptance. Current documentation also corrects a stale cleanup
claim: PR32's later observation resolved that resource/accounting state with
30 CPU-seconds conservatively charged; the original failed receipt stays exact.

The ownership-failure hold is not a reader-drain/checkpoint admission policy or
cross-process quiescence proof. No automatic checkpoints, page caps, journal
changes, retry, deletion, quota arithmetic or checkpoint/drain safety-write
denial policy is authorized here. Those require separate concrete design review.
Independent runtime review and exact-head CI passed within the scope above.
This local slice needs no host selection or purchase and does not close the fifth
headroom failure or physical-capacity gate.

The next qualification-only increment uses fresh v4 state, production HTTP/Worker
paths, two synthetic projects and already available reviewed Python/R images.
Allow at most four sequential broker attempts, each at the existing 1 CPU,
256 MiB, 64 PID, 30-second and 65,536-output-byte limits: at most 120 conservative
CPU-seconds. Bind identities before launch; require exact final receipts, full
charges and verified cleanup. Preserve failed attempts without retry, refund or
a fifth attempt. The allowance spans interruptions/restarts and cannot be renewed
by choosing a new output directory. Its 120 CPU-seconds describe conservative
reservations/charges, not host overhead or termination proof after unknown cleanup.
Queued cancellation and current-access refusal must produce no
dispatch. No image pull, runtime redesign, new profile, source promotion or
accepted-state change belongs in this slice. Unavailable approved images or
capacity means NOT RUN. This is an existing local execution budget, not new
spending approval, provider pricing or selected-host capacity acceptance.

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
