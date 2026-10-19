# Research sandbox and allocation readiness

Authorized October 19, 2026. This contract extends the accepted
[research workspace](research-workspace-pilot.md) with a separate temporary
assessment mode. The delivery sequence is in the
[build backlog](../strategy/research-pilot-build-backlog.md); the
[tool decision](../decisions/2026-10-19-research-assessment-tools.md) identifies
reused tools and their qualification limits. Authorization to build is not
acceptance of a deployed service or permission to admit private data.

## User journey and ownership

Temporary upload → reviewed workload → actual-resource benchmark → validated
resource estimate → researcher-reviewed ACCESS or NAIRR preparation packet.
An upload alone cannot establish compute demand. The user must describe the
analysis, software, experiment count, quality requirement and intended scale.
Research and instructional assessments have distinct forms and packet templates.

| Component | Authority |
| --- | --- |
| Waypoint | Assessment requests, current project membership, upload sessions, comparison, retention preview and report export. |
| Outfitter | Execution admission, reservations, bounded attempts, cancellation, provider reconciliation and resource/data cleanup. |
| Portage | All model access, destination restrictions, inference allowances and usage accounting. |
| Cairn | Course authority when an assessment is instructional. |
| EduCloud | Versioned cross-component contracts, program requirements and acceptance evidence. |

Adapters extend existing authorities. A benchmark tool cannot create an
independent queue, budget ledger or execution bypass. Ben's Docker/Jetstream2
issues and assignment remain unchanged. Belay and portage-local are outside this
implementation. Existing study bundles and AI conversation-retention policies
remain separate; assessment deletion must not erase historical pilot evidence.
The old bundle exporter, which includes source bytes, is forbidden in this mode.

## Temporary-data contract

Before accepting bytes, show the destination, maximum upload/scratch size,
absolute expiry, deletion behavior and the measurements proposed for retention.
Create isolated encrypted scratch with a per-assessment access boundary. Prepare
reviewed dependencies and images before admitting data. Uploads must stream into
that boundary, including interrupted/multipart uploads; proxy/framework spool
files cannot escape it. Data classification and destination admission remain
subject to the existing data-destination policy.

Upload content, intermediate datasets, generated outputs, notebook checkpoints,
stdout/stderr and workload logs are ephemeral. Never place them in database
rows, image layers/build contexts, shared caches, snapshots, persistent backup
sets, browser caches, telemetry or model traces. Use no-store responses and no
service-worker caching for assessment surfaces. File names, free text, labels,
parameters, hashes and error messages can disclose source content; they are not
retained merely because they are called metadata. Source hashes are not default
retained identifiers. Reproducibility uses reviewed software identifiers,
methods and re-upload instructions.

The lifecycle is `preparing → accepting → sealed → running → cleaning → closed`.
Cancellation, expiry, failed upload and any execution failure converge on
`cleaning`. Terminate work and revoke read/write credentials before removing
scratch. A crash-safe independent expiry/reconciliation path must also run when
the request server or worker is unavailable. A failed or uncertain cleanup yields
`cleanup_unresolved`: access remains revoked, the worker/storage scope is
quarantined, liabilities remain visible and reuse is denied. Only independently
verified removal permits `closed`. A delete request or absent process alone is
not removal evidence. Clock rollback, restart and duplicate callbacks cannot
extend expiry or revive permissions.

Deletion covers all replicas and temporary transfer destinations, including
provider disks, attachments, object uploads, caches and snapshots. Receipts
record the observed scopes and verification method without raw paths or content.
Encrypted storage does not alone prove deletion or protection of plaintext in
memory, swap, crash dumps or privileged access. Qualification must test these
boundaries and the relevant backup exclusions on the selected host. Until then,
only public/synthetic fixtures may enter the assessment path.

Retained information is a closed allowlist: opaque assessment/project/attempt
IDs; reviewed workload/environment/tool versions; approved hardware descriptors;
normalized measurements with units and provenance; bounded failure categories;
reservation/charge references; cleanup receipts; and user-approved report text.
Free-form tool output and unknown fields are rejected, not copied through.
Preview the exact retained record before finalizing a report. User narrative is
an explicit editable report field, never an automatically retained excerpt of
uploaded data. If the user declines retention or leaves before preview, discard
the draft and keep only the minimum operational cleanup/accounting receipt
required by policy. Reproduction after cleanup requires a new authorized upload.

## Workload preparation

Collect objectives, stages, software and licensing, input dimensions and growth,
experiment/replicate counts, deadline, quality thresholds and acceptable failure
rates. Instructional intake also collects enrollment, simultaneous sessions,
assignment frequency, deadline peaks, idle behavior, per-student storage,
accessibility/support needs and fallback capacity. Separate these user assumptions
from observations.

Offer Python/R analysis, document processing, ML training and LLM inference
templates. Researcher scripts and containers require review and immutable
approved digests before execution; changing a script invalidates review. Default
network access is denied. Any dependency/model acquisition precedes data
admission. Network exceptions require destination-specific review through the
existing authorities. Do not send research data to a model to generate the
workload by default.

Record the sampling method, dimensions, exclusions and known skew. Convenient
samples must not silently represent the full dataset. Correctness checks and
scientific/task-quality criteria are supplied independently of the measured
implementation. A fast but invalid result is a failed attempt.

## Benchmark contract version 1

A versioned `educloud.benchmark-manifest/v1` binds the opaque assessment and
project, pathway, reviewed workload digest, template/stages, environment image
and dependency/model versions, approved hardware configuration, measurement
method/version, sample sizes/repetitions, held-out size, fixed seeds where
applicable, quality checks, expiry and existing Outfitter reservation references.
It declares a finite maximum number of attempts and resource ceilings. Neither
manifest creation nor a tool-generated job grants execution authority.

Default design: three sample sizes with three repetitions each, plus a separate
held-out size with three repetitions when the approved allowance permits.
The user can approve a smaller finite design; incomplete coverage remains
explicitly provisional. Failed, timed-out and out-of-memory attempts consume
attempts and remain represented by sanitized categories. No automatic retry may
exceed admission. Held-out observations cannot also be fitting observations.

Each `educloud.measurement-receipt/v1` binds manifest version/digest, attempt and
stage, reservation, immutable environment, hardware, measurement method and
cleanup receipt. Record observations with unit, scope, availability and source:

- CPU consumed seconds, peak memory bytes, scratch/output peak bytes and I/O.
- GPU count/model, allocated duration, measured GPU memory/utilization and
  completed work. Unavailable counters are unknown, never zero.
- Setup, image/model loading, transfer, queue, execution and cleanup duration.
- Valid completed units, independent correctness/task-quality results and
  bounded failure category. Keep unsuccessful denominators visible.
- Sandbox and instrumentation overhead measured against a matched baseline.

Keep three separate fields/groups for measured consumption, reserved ceilings
and provider-reported charges. Each has its own provenance and unit. A full
reservation charge is not a CPU-utilization measurement. Process RSS is not
whole-job peak memory; allocated GPU-hours are not utilization-adjusted GPU
hours. Preserve the measurement semantics of cgroups, scheduler and GPU tools.
Unknown or unsupported measurements cannot become populated estimates.

A versioned `educloud.cleanup-receipt/v1` records opaque owned scope identifiers,
termination/access-revocation status, deletion checks, observation time/method,
remaining liabilities, independent verifier identity and outcome
`verified | unresolved`. Keep a failed receipt immutable; append reconciliation
evidence rather than rewriting failure into success. Authorization and
cryptographic/trusted-source receipt validation are component responsibilities;
a structurally valid JSON receipt is not proof of an actual run.

## Execution and measurement adapters

Start with the accepted reviewed Python/R path. BenchExec runs only on a
controlled Linux worker with delegated resource controls. Do not disable
shared-host confinement or grant privileged nested containers to make it work.
Use ReFrame for portable definitions, correctness checks, repetition and
comparison; dispatch remains mediated by Outfitter. Qualify OpenSandbox as an
optional disabled backend on dedicated disposable Linux workers before enabling
it. Stronger isolation is a separate runtime qualification.

Import Snakemake/Nextflow definitions and reports through bounded, sanitized
parsers. Do not retain raw workflow reports, commands, parameters or caches.
Apptainer provides reviewed HPC environment portability, not the sole boundary
for arbitrary code. Optional JupyterHub/repo2docker preparation must keep uploads
out of builds, notebooks retained elsewhere and shared caches. vLLM/DCGM
measurements remain governed by Portage admission and model policy. Existing
Galaxy, VICE and Open OnDemand installations connect through adapters with
explicit retention contracts; no second complete portal is required.

## Deterministic estimation and comparison

Fit or select an explicit stage-level scaling model from valid observations.
Record the method/version, selected inputs, excluded failures, coefficients,
units and rounding. Compare predictions against held-out observations and report
absolute/relative error and the tested range. Report repeat variability and
sensitivity to user assumptions separately from prediction uncertainty; do not
label a three-run min/max range a statistical confidence interval.

Total demand combines per-stage measured work at planned scale, stage execution
counts, experiment/repetition counts and explicit setup/transfer/idle/retry
assumptions. Avoid double-counting shared setup or multiplying peak memory by
runtime. Class schedules model concurrency/peak storage separately from total
CPU/GPU consumption. Missing stages or untested hardware remain unknown.
Extrapolation, poor held-out accuracy, insufficient samples and out-of-memory
boundaries must visibly limit the estimate. Unsupported scenarios are provisional
and cannot receive a readiness pass.

CPU-hours, allocated GPU-hours, node-hours, peak memory, storage capacity/time,
provider service units, ACCESS credits and dollars remain distinct. Conversion
rules include provider/resource/version, effective date, source and formula.
Never infer dollars from credits or utilization from reservations. Compare
resources only with clearly labeled measurement provenance: local Mac,
synthetic adapter, actual target CPU or actual target GPU. An architectural
analogue may support a qualified provisional estimate, not target acceptance.

## Allocation preparation and exports

Produce an editable project narrative, traceable benchmark/scaling report,
preferred/alternative resource justification, software/accounts/staffing/access
readiness checklist, program-specific PDF and matching submission-field
worksheet. Preflight exports against the same approved retained record; raw
uploads, tool logs and hidden fields are forbidden. Preserve editable source
alongside the PDF. Researchers review claims and submit applications themselves.

Refresh the selected program's official requirements, eligibility, resource
availability and conversion terms before final export. Record fetched/reviewed
date and source version; if refresh fails, allow a clearly labeled draft and
prevent a current-requirements-ready claim. Require a human review of both
scientific claims and the selected resource/form correspondence.

- [ACCESS](https://allocations.access-ci.org/prepare-requests): tier-specific
  narrative and performance evidence; larger requests need stronger scaling
  evidence, preferably on the requested resource. Do not flatten all tiers
  into one template.
- [NAIRR research](https://nairrpilot.org/nairr-pilot-proposal-instructions):
  justified resource estimates grounded in prior experience or benchmarks,
  computational work and unit costs, software/data/support readiness and
  resource choice. Keep the preferred resource consistent across form and PDF.
- [NAIRR Classroom](https://nairrpilot.org/opportunities/education-call): a
  distinct educational template with enrollment, teaching schedule, per-student
  resources, access methods and instructor/TA support. Do not treat a research
  request as a classroom request with a different title.

Portage may explain measurements or draft prose from approved metadata. All
calculations, status decisions and evidence classifications remain deterministic.
Neither an export nor the use of open tools establishes FERPA readiness.

## Acceptance matrix

| Gate | Required evidence |
| --- | --- |
| Isolation | Two projects cannot access one another's uploads, execution, retained measurements, report previews or cleanup scopes. Test revoked and expired sessions. |
| Lifecycle | Completion, cancellation, expiry, worker/server crashes and interrupted uploads leave no accessible source residue. Exercise independent reaping, restart and unresolved cleanup quarantine. |
| Content exclusion | Seed identifiable synthetic markers; inspect logs, exports, caches, image layers, browser state, backup inventories and model traces for leakage. Verify encrypted scratch configuration on the actual host. |
| Accounting | Compare worker measurements with independent cgroup/scheduler/provider evidence. Declare metric-specific tolerances before qualification; discrepancies fail reconciliation and remain visible. |
| Estimation | Independent calculations and held-out sizes test predictions; missing metrics, failed/OOM attempts and extrapolation cannot produce an unsupported readiness pass. |
| Actual resources | CPU and GPU runs on the selected target configurations, immutable environments, workload quality checks and measured overhead. Local or simulated success cannot close this gate. |
| Reproduction | A second operator on another machine reproduces the workflow without core edits, records help/time and cleanup evidence. |
| Usability | A researcher and instructor separately produce understandable, traceable packets, including manual accessibility checks. |
| Service readiness | Institutional identity/destination approval, operational ownership, capacity, retention/backup checks and whole-service FERPA acceptance before education records. |

Live qualification still needs a selected allocation, worker/cleanup hosts,
model where applicable, named operator, time window and finite allowance.
Prepare the exact run packet while those choices remain unresolved. The
implementation must preserve these gates as open rather than promoting existing
synthetic evidence.
