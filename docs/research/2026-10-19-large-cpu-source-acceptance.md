# Larger CPU assessment metadata — source acceptance

October 19, 2026. Merged [Outfitter #20](https://github.com/EduCloud-Ecosystem/outfitter/pull/20)
adds a separately versioned, pure metadata validator for larger CPU assessments.
It is partial A2 preparation: no upload, execution, measured consumption,
storage capacity, trusted cleanup or participant-pilot qualification follows.
The [owned-data source acceptance](2026-10-19-owned-data-source-acceptance.md)
and all earlier v1 evidence remain unchanged.

Reviewed head `9cf556b024960422b960281f4afacc923afcc12f` merged as
`e0dc0249c818ab1d8b6c74a5555d9e1ec89c1900`; both trees equal
`ae4e3ec58783bde674d584adc73b37268267a18e`. The
[evidence index](evidence/2026-10-19-large-cpu-source/acceptance.json)
records source, log, artifact and checker bindings. Raw local artifacts remain
in the protected coordinator archive; their hashes do not imply a public
download or compiler attestation.

## Delivered boundary

The explicit `assessment-receipts` operation `validate_v2` accepts only the
closed v2 manifest/measurement/cleanup/receipt-set schemas. The immutable
`cpu-python-r-bounded` profile version 1 is separate from allocation-program
templates. Its [pinned specification](https://github.com/EduCloud-Ecosystem/outfitter/blob/9cf556b024960422b960281f4afacc923afcc12f/specs/22-assessment-large-cpu-codec.md)
defines one CPU, a 1–1800-second per-attempt timeout, 32 MiB–1 GiB task memory,
up to 5,000,000,000 input bytes, 1,000,000 rows, 65,536 output bytes and
10,000,000,000 aggregate scratch bytes per assessment. The process limit is 64.
At most twelve planned slots imply at most 21,600 conservative CPU-seconds.
These are metadata ceilings, not an execution allowance or available capacity.
Input, output and work partitions share the aggregate scratch ceiling; smaller
input does not enlarge work, and attempts cannot multiply the storage limit.

V1 validators, canonical bytes, owned-data controls/status, v6, ordinary runtime
defaults, ledger and provider paths retain their limits. Mixed versions and
implicit conversion refuse. The pure command now refuses invalid arguments
before inspecting an existing state directory. This fixes an inherited CLI
ordering issue without changing ordinary command behavior.

All imported observations remain unverified. Reservation provenance is exactly
`unverified_profile_reservation`; no legacy projection is added. Unknown
execution may retain the full CPU hold, or report the exact full conservative
charge after reported execution-resource cleanup. Execution stays unknown in
either case. No partial refund, active-state settlement, charge-plus-live-hold
double count or replay is inferred. This preserves existing accounting semantics;
imported claims cannot clear an actual ambiguous create, ownership or reader/
collector/cleanup hold. Provider charges remain unknown, and conservative CPU
charges never become measured utilization.

CPU counter scope distinguishes process from sandbox; duration distinguishes
execution-only from whole-attempt. Unsupported counters remain null, including
all GPU metrics. Every result keeps execution authority, actual-resource
acceptance and cleanup trust false. Structural cleanup IDs do not bind an actual
A1 broker authority or sealed-upload scope; a later execution contract must.

## Verification and provenance

| Evidence | Result and boundary |
| --- | --- |
| Final immutable review | **CLEAR:** coordinator and independent source/evidence reviews; 262 source bindings and 53 unchanged historical fixtures, including 19 pinned Waypoint fixtures. |
| Focused local controls | **PASS:** 381 assessment test/subtest events at accounting-corrected `8f1c56ed`; those source/fixture bytes are unchanged at final `9cf556b`. One final CLI test event covers 36 child calls, including three held-open-stdin state-directory variants. Static checks passed. These are focused non-race local checks, not a final full local suite. |
| Independent actual CLI | **PASS:** 47 isolated calls, eight positive and 39 negative, with 141 request/stdout/stderr payloads hash-checked. Exact v1/v2 outputs, smaller positive limits, rebinding of negative-case digests, accounting forms, null GPU measurements and false trust flags were checked. All 262 source files matched before/after. No workload, engine or large payload ran. |
| Exact final hosted CI | **PASS:** both jobs in [run 39362390204](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39362390204). Full race log: **1,335 PASS / 0 FAIL / 2 SKIP**, ten packages passed. The 381 assessment, 288 V2, 150 owned-data, 85 separate-process and 13 pipe events overlap. All 6,130 JSONL events match the retained job log; archive digests match GitHub. |
| Existing adapter regression | **PASS:** later actual baseline Docker lifecycle; 26 Docker, 38 recovery and 19 synthetic-consumer report checks. These do not execute the new larger assessment or measure its resource consumption. Provider self-expiry after host/watchdog/daemon loss remains unsupported. |
| Historical storage job | **PASS within its old counterexample scope:** pinned `5827c84e`, 22 events, 32 models and two optimized probes. Quota remains unenforced and available capacity UNKNOWN; no new workload or capacity credit. |
| Operational assessment | **NOT RUN / OPEN:** actual large inputs, benchmark dispatch/counters, independent scientific quality, qualified storage/cleanup, second operator and full participant/service acceptance. |

The two full-suite skips are the opt-in Docker test, exercised separately later,
and unsupported provider self-expiry. Local command records retain explicit
overrides, exits, times and hashes; other environment remains inherited.
Author tests did not retain their temporary executable/compiler identity.
DCO sign-off trailers are not cryptographic commit signatures.

The coordinator retained two successful Go builds with identical binary bytes,
source snapshots and build metadata. Both lack an embedded VCS revision even
with an explicit VCS-stamping build option. Two original pre-CLI checker runs
remain **FAIL** because they required that stamp; neither invoked CLI checks.
The corrected driver reused the exact retained binary for the 47 calls, with
manual source/build/binary binding and the missing stamp disclosed. This is not
full compiler attestation or a product failure rewritten into success.

## Retained failures and follow-through

The initial maximum-form run remains **FAIL: 367 PASS / 3 FAIL**, comprising two
failed leaves and their parent, with package failure overlapping. Longest
lifecycle forms and category spellings required corrected independent vectors;
the revised 371-event pass stays bound to earlier `ac3ff8e`. A later 381-event
pass belongs to `8f1c56ed`, not a relabeled rerun at final head. Original vector
indices and old fixture bytes remain preserved. The CLI ordering defect was
actually reproduced on two invalid/poison ledgers before the fix. A third final
marker-only v6-shaped fixture is malformed state, not a valid authority/runtime
witness. Source order establishes refusal before state inspection; no pre-fix
v6 lock mutation is claimed.

Next, finish Waypoint's disabled AS1 HTTP/Store/current-auth journey, then review
the concrete execution contract in the existing broker authority. Larger-input
use requires a bounded streaming recipe and independent checker, actual
aggregate writer/storage enforcement, measurement fidelity and exact owned
scope/authority bindings. A 10 GB tmpfs under 1 GiB task memory is insufficient.
Reuse A4/A5 through separately reviewed typed provenance and export integration;
neither a parser nor synthetic fixtures complete the
[researcher/instructor milestone](../strategy/researcher-instructor-pilot.md).

The [planning budget](../strategy/researcher-instructor-pilot-budget.md) grants
no live allowance. Allocation/hosts/operators/window, encryption and spool/swap/
crash/backup exclusions, independent expiry/termination/revocation/deletion and
whole-service acceptance remain open. Live Jetstream2 needs separate approval.
No purchase, provider use, model download, private/student data, deployment or
default routing change is part of this delivery. Docker/Compose on OrbStack
remains baseline; Kubernetes and PAIR remain optional gated evaluations.
