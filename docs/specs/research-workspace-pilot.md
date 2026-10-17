# Research workspace pilot

Implementation scope authorized 17 October 2026. The first deliverable is a
local research-project workflow: create a project, run reviewed Python/R
conditions against public or synthetic data, compare descriptive results, and
export an inspectable evidence package. It does not admit private participant
records, promise scientific validity, or provision cloud resources.

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

## Acceptance and next expansion

Release evidence must distinguish unit/adversarial tests, actual local Docker
execution, browser interaction, remote CI and independent human reproduction.
Run two differently configured projects without core code changes, independently
check expected results, verify cancellation/budget/authorization failures, and
verify that exported bundles detect tampering and retain failed controls.

After this local path is accepted: production identity and project membership;
full metadata/ledger/data recovery; institution-approved storage/retention;
arbitrary reviewed project packages behind a stronger execution contract;
supported asynchronous hosting; and a second researcher completing the runbook.
AI experiments and domain applications integrate through explicit adapters.
Participant feedback/consent and scientific evaluation remain study-owned.
