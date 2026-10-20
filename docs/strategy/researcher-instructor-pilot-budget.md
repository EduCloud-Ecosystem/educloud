# Provisional pilot budget and release gates

Greg approved this envelope for planning on October 19, 2026. It supports the
[researcher and instructor milestone](researcher-instructor-pilot.md), using
existing allocations first. It does not select resources or authorize a live
test, provisioning, spending, authentication to a provider, model acquisition or
data admission.

| Planning item | Approved provisional envelope |
| --- | --- |
| Operating window | 14 days after implementation and operational prerequisites pass; dates unselected. |
| CPU | 4,000 CPU SUs total; staged release, not a granted runtime allowance. |
| GPU | 3,000 GPU SUs, released separately for a justified later workflow; no always-on GPU or prerequisite for the Python/R CPU journey. |
| Volume capacity | Up to 500 GB proposed, subject to free quota, storage policy and qualification; no capacity or per-upload acceptance claim. |
| New infrastructure purchases | Target $0, conditional on existing allocations, capacity and institutional support; no purchase approval. |
| People | 62–102 people-hours for setup, qualification, exercise and support, excluding unfinished development. Staffing availability and loaded labor costs remain unselected. |

CPU and GPU entitlements stay separate. No current balance, free quota,
allocation expiry, PI-approved scope or commitment to other users is established
by these ceilings. They are neither measured consumption nor provider-enforced
maximum charges. Keep reservations, actual measurements, conservative charges,
unknown exposure and unresolved cleanup liabilities separate. Do not renew an
exhausted prior allowance or roll deadlines forward automatically.

## Release decisions

Before the first live test, select the actual allocation and confirm its scope,
membership, expiry, current balance and competing commitments. Name the control
host, worker, independent cleanup host, private route, credential custody,
primary and independent operators, attended window, latest admission and expiry.
Bind the immutable release/image, exact worker flavor, admitted data category,
finite native-unit allowance and failure/late-effect/cleanup procedure. Independent
cleanup requires evidence for the failure domain being tested; another VM name
does not establish it.

The proposed existing CPU lifecycle micro-test retains its separate live approval
gate: one worker create, at most ten minutes and a one-SU **worker** reservation.
That reservation does not cover control or rescue hosting, storage or other
incremental costs. Their coverage must be explicit before approval. Any approved
micro-test consumption counts within the 4,000 CPU-SU plan, rather than adding
an unbounded allowance. It exercises its dedicated operator contract, not
production assessment upload readiness.

Release the larger CPU participant exercise only after its reviewed software,
storage, measurement and independent cleanup controls pass. Keep the GPU phase
separate until its named use case, pinned workload/model, licensing, counters,
finite window and cleanup are reviewed and explicitly approved. Selecting a host
or approving this planning envelope cannot activate currently disabled code.
Live Jetstream2 still requires Greg's separate approval.

## Current software limits

The accepted benchmark-manifest/v1 profile supports summary Python/R, one
analysis stage, no additional dependencies, CPU-only `local_docker` hardware,
at most three fitting sizes plus one held out, up to three repetitions and sizes no
greater than 1,000 rows. Each manifest has at most twelve attempts, a fixed
30-second timeout per attempt, total CPU ceiling of attempts × 30 seconds, 256 MiB task
memory, at most 128 MiB scratch and 64 KiB output. Host RAM/CPU sizing is separate
from these task limits. A smaller fitting/repetition design needs its explicit
reviewed approval. See the
[accepted validator](https://github.com/EduCloud-Ecosystem/outfitter/blob/de65bdab9303395226ebfb35e0e0740ab19b4d8e/internal/assessment/manifest.go).

The separately versioned [v2 CPU metadata codec](../research/2026-10-19-large-cpu-source-acceptance.md)
is accepted as pure source preparation: one CPU, up to 1800 seconds per attempt,
32 MiB–1 GiB task memory, 5,000,000,000 input bytes, 1,000,000 rows,
65,536 output bytes and 10,000,000,000 aggregate scratch bytes. At most twelve
slots imply at most 21,600 conservative CPU-seconds. These ceilings grant no
execution or capacity. The [streaming code and independent checker source](../research/2026-10-19-streaming-summary-source-acceptance.md)
are accepted for a narrower 88,000,013-byte scientific grammar, with all runtime
readiness flags false. Real aggregate storage enforcement, actual-code execution,
owned-scope/authority bindings, counters and operational qualification remain
required. GPU is unsupported/null. The ordinary runtime
and v1 limits above are unchanged.

The [execution/checked-cleanup source increment](../research/2026-10-19-execution-source-acceptance.md)
adds disabled test-only v7 authority and synthetic sequential-process controls.
It does not select resources, activate production, install the scientific adapter
or qualify aggregate storage, measured counters or independent cleanup. Source
acceptance does not release any of the planning allowances above.

The planning packet's longer tasks, larger inputs and optional GPU workload are
not executable through the current accepted assessment path. An aggregate
multi-session attempt budget is not one manifest's allowance. Choose an appropriate bounded current workload or
implement and review a separately versioned/profiled extension before relying
on those capabilities. Preserve imported v1 identities and exact digests; no
configuration toggle silently broadens them.

Production temporary uploads remain unconditionally disabled. Actual host and
delegated resource controls, encryption/key custody, spool/swap/crash/backup
exclusions, independent expiry/termination/revocation/deletion, measurement
validation, second-operator exercises and whole-service privacy acceptance remain
open. Use synthetic or approved public inputs first; no private/student-data or
FERPA acceptance follows from this budget. Independent implementation continues
while allocation, host, operator and exact live-window decisions are prepared.
