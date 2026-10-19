# Research workspace pilot

Implementation scope authorized 17 October 2026. The first deliverable is a
local research-project workflow: create a project, run reviewed Python/R
conditions against public or synthetic data, compare descriptive results, and
export an inspectable evidence package. It does not admit private participant
records, promise scientific validity, or provision cloud resources.

The [acceptance record](../research/2026-10-17-research-pilot-acceptance.md)
pins the merged P0 baseline and P1 portability/recovery implementation.
The following P1 interface requirements are design constraints, not a claim that
every remaining acceptance gate has passed.

## Temporary assessment extension

The October 19 [research assessment contract](research-assessment.md) adds a
separate temporary-data mode using this execution foundation. Its exports retain
approved measurements and methods, never uploaded source bytes or raw workload
logs. The retained study-bundle behavior below remains the historical pilot
contract and must not be reused for temporary assessments. Existing evidence is
preserved; new cleanup, actual-resource and institutional acceptance gates remain
open. Measured consumption will be recorded separately from the conservative
allowance charging described below.

## Module responsibilities

- Waypoint owns project membership, run requests, immutable input/recipe
  lineage, the local browser surface and project evidence export.
- Outfitter owns compute reservations, bounded Docker execution, conservative
  accounting, cancellation, reconciliation and owned-resource cleanup.
- Portage remains the sole inference-policy/accounting authority when AI is
  subsequently connected. This initial recipe makes no model calls.
- Cairn remains the authority for connected courses; a research project does
  not require a classroom. Belay remains with its developer and is unchanged.
- MESA's proposed document application owns document-specific source QA,
  annotation and adjudication. This workspace does not duplicate that workflow.

The initial Docker broker extends Ben's Outfitter work and is followed by a
Jetstream2 read-only preflight and provider seam. Cloud
execution still requires verified allocation/resource access, an explicit
finite allowance, independent expiry/cleanup and a supported live adapter.
Local Docker CPU-second ceilings are not Jetstream2 service units or dollars.

## First supported workflow

1. An operator creates a private local workspace and opaque collaborator keys.
2. A researcher records a question, success criterion, finite compute allowance
   and end date. Owner/editor/viewer membership is server-authoritative.
3. The researcher supplies a bounded `group,value` CSV and selects a reviewed
   Python or R recipe and a baseline or alternative condition.
4. A durable queue rechecks current access and project dates before dispatch.
   Outfitter reserves a finite maximum before any Docker effect. Execution has
   no network, a non-root user, read-only input/recipe mounts, bounded memory,
   process count, output, CPU and wall-clock lifetime.
5. Waypoint validates the complete broker receipt and checks actual numerical
   output independently. A failed or interrupted attempt remains in the record.
6. Authorized members inspect descriptive comparisons and download an evidence
   bundle containing selected input/recipe/result bytes, versioned metadata,
   checksums, methods, failure/gap records and RO-Crate-style metadata.
7. Closing a project prevents new work, cancels outstanding work and preserves
   authorized inspection/export. Deletion and institutional records schedules
   are separate future controls, not inferred from project closure.

## Limits that remain visible

The local identity adapter binds to loopback only and is not Keycloak or campus
SSO. Membership management through this pilot does not establish institutional
authorization. The current control/metadata store uses SQLite on local disk;
shared hosting or network-mounted SQLite is outside this release.

Docker is a reviewed-local execution tier. Its external watchdog survives the
submitting process, but loss of the watchdog/host is not provider self-expiry.
Every placement explicitly opts into this supervised-reaper limitation. Keep
that distinction separate from a future accepted Jetstream2 worker lifecycle.

Accounting conservatively charges the full admitted CPU-time ceiling after
verified cleanup. It is not a measured CPU-utilization, financial-cost or
provider-settled charge. Uncertain work retains its liability. Never silently
retry interrupted work, restore old allowances, or reinitialize lost authority.

The reviewed demonstration compares all values with per-group trimming when
at least five observations exist. It does not select an appropriate scientific
method for a researcher. A passing numerical check proves this bounded recipe's
behavior, not study validity, efficacy, statistical significance or generality.

Project metadata, memberships, keys, session records, input/output files,
broker journals and exports have separate access and retention implications.
The pilot permits public/synthetic inputs and synthetic subjects only. Private
research data and human-participant records require a separately reviewed
whole-service destination/retention/approval contract. Exports exclude keys,
sessions, membership lists, raw logs and absolute host paths; restricted source
bytes must never be made public merely because a bundle can be generated.

## Portable environment and replay boundary

Waypoint owns a versioned reviewed-environment catalog: recipe identity/hash,
runtime/dependencies (including an explicit no-extra-packages statement), platform,
immutable image, resource limits, method/condition and declared result tolerances.
Missing source/build provenance and untested clean builds stay explicit. Existing
image execution does not prove image reconstruction.

Study bundles retain input, recipe, parameter and environment lineage, result
hashes, methods, status and missing/failed evidence. Inspection verifies bounded
archive structure and payloads without executing bundled code. Execution is a
separate explicit operation limited to trusted reviewed recipes and immutable
images, with a fresh finite Outfitter project/reservation. A separately retained
trusted digest detects whole-bundle replacement; embedded checksums alone do not
establish authenticity. Historical failure and unselected runs remain visible,
and historical recipe bytes are not silently replaced by a corrected version.

## Coordinated local recovery boundary

Waypoint takes its offline service locks and a consistent SQLite/artifact/config
point. Outfitter takes a validated ledger/output checkpoint under its transaction
lock and returns its checkpoint identity and exact authority fingerprint.
The caller retains that digest in a private trusted recovery manifest. Existing
destinations and partial checkpoints are not silently overwritten.

Restore creates a held replacement. Broker allowances, settled charges and unknown
reservations retain their identities and values; no replay, refund or new
admission occurs. Waypoint invalidates restored sessions/credentials, retains
membership/revocation state, and requires current source database, artifact and
configuration agreement before reopening access. Unsupported deletion/retention
controls remain gates rather than being inferred from project closure.

Activation requires both current source authorities and matching recovery points.
Outfitter refuses in-flight or unresolved provider work; reconcile the source and
take a fresh checkpoint first. It durably fences source admission to the exact
destination before activating that destination. Waypoint retires source service
admission before enabling its replacement. A crash may leave both held/stopped,
and the exact same-pair retry is permitted; it must never create two admitting
authorities. Missing source or stale state remains held.

This is same-host local cutover, not remote disaster recovery. Canonical-path
binding cannot protect against privileged original-path rollback or a cloned
machine. Status and owned cleanup remain available on a fenced broker. Provider
settlement, stronger expiry and hosted recovery objectives require separate
acceptance. The executable broker interface is maintained in Outfitter
`specs/11-local-recovery.md`; Waypoint owns its service/artifact recovery interface.

## Acceptance and next expansion

Release evidence must distinguish unit/adversarial tests, actual local Docker
execution, browser interaction, remote CI and independent human reproduction.
Run two differently configured projects without core code changes, independently
check expected results, verify cancellation/budget/authorization failures, and
verify that exported bundles detect tampering and retain failed controls.

Next: finish the remaining clean environment builds and independent reproduction gates;
then evaluate the required P2 packages in the [sequenced backlog](../strategy/research-pilot-build-backlog.md).
Docker remains the baseline. An optional disabled Kubernetes evaluation may follow
P1 before custom multi-host orchestration; institutional capacity discovery can
begin earlier without authorizing access or provisioning. New paid dependencies
require a [prepared cost decision](../decisions/2026-10-17-research-pilot-capacity.md)
before incurring cost. Shared identity, storage/retention, stronger execution and
scientific/participant approvals remain separate gates. AI experiments and domain
applications integrate through explicit adapters.
