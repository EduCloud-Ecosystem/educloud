# Local Kubernetes foundation evaluation

Status: implementation contract, 18 October 2026. This is the smallest local
slice of [P2-A](../strategy/research-pilot-build-backlog.md), authorized alongside
the host owner's Docker Desktop to OrbStack migration. It neither performs that
migration nor changes the accepted Docker execution backend. The exhausted
Waypoint four-attempt/120 CPU-second qualification is not an allowance here.

## Contract

`tools/local-kubernetes/evaluate.py` uses the Python standard library only. It
renders and checks files offline. It never invokes kubectl, Docker, a shell,
network transport, credentials, a provider or a workload. There is no execution,
enable, retry, cleanup or quota-increase subcommand.

`render` requires a new evaluation ID, an absolute operator-owned kubeconfig
path (not read), an explicit HTTPS literal loopback API endpoint, the observed
Pod Security minor version, a declared architecture and a reviewed immutable
image reference. Context is fixed to `orbstack`. The image is a design input,
not evidence of availability, provenance or permission to execute it. No image
pull occurs. This slice targets Pod Security v1.36; a different minor requires
review rather than silently using `latest`.

The new private output directory contains deterministic JSON:

- Two separate namespace objects: `educloud-eval-<id>-a` and `...-b`. Each has
  evaluation/project ownership labels and restricted enforce/audit/warn labels.
- One policy List per namespace: a quota denying all pods, Jobs, CronJobs,
  Deployments, StatefulSets, DaemonSets, ReplicaSets, ReplicationControllers,
  services, secrets and persistent-volume claims; a one-CPU/256 MiB/64 MiB
  ephemeral-storage container LimitRange; a service account with token automount
  disabled; and default-deny ingress/egress NetworkPolicy **intent**.
- A review-only envelope containing a future single Pod design. It is excluded
  from every command, has an Outfitter admission scheduling gate, `Never`
  restart/image pull, a 30-second active deadline, five-second grace, nonroot
  UID/GID, read-only root, RuntimeDefault seccomp, all capabilities dropped, no
  host namespaces/ports/paths, no credentials and only a 16 MiB memory emptyDir.
  It has no controller. This is not a reserved worker or a Docker conformance
  claim: deadline/grace is not independent expiry, ephemeral limits are not a
  storage guarantee, and no per-pod PID or output bound is implemented.
- An operator plan of argv arrays, never shell text: explicit kubeconfig,
  context, server and 30-second request deadline on every kubectl command.
  Namespaces and policy Lists have separate server-dry-run and create-only
  phases. Existing namespace refusal stops the procedure; no apply, adoption,
  cluster role, cluster setting, delete or broad cleanup command is generated.
- A manifest committed last, binding configuration, exact generated files,
  generator/spec hashes and all runtime gates as NOT RUN. It is an integrity
  record, not a signed approval or an Outfitter reservation.

`validate --bundle DIR --expected-manifest-sha256 HASH` requires a separately
retained digest, exactly the expected regular files, bounded reads with no
symlink/FIFO following, strict JSON with duplicate/nonfinite values refused,
and byte equality with the current generator's entire contract. Unknown fields,
altered flags/types/commands, missing files or modified limits refuse. Internal
hashes alone are not authenticity. The trusted digest must come from the
reviewed render, not be calculated from an unfamiliar replacement bundle.

All file creation is exclusive; no existing destination is overwritten. A write
failure retains a partial directory and cannot publish a complete manifest.
This is not an adversarial multi-user filesystem or power-loss recovery scheme.

The initial five-second API request timeout proved too short for local OpenAPI
discovery during host migration. The corrected default is 30 seconds; Pod grace
remains five seconds. The original bundle/source and failed observations stay
frozen. Validate historical bundles with their matching generator revision, not
by rewriting their hashes or silently upgrading their command plans.

## Operator boundary

The host owner first verifies that the named context and literal endpoint refer
to the intended existing local cluster, the private kubeconfig contains trusted
authentication configuration (including any credential plugins/proxy settings),
and no proxy/tunnel redirects it elsewhere. A loopback address alone cannot
attest cluster identity. Never weaken TLS or silently substitute a remote API.
Commands are proposals only; cluster admission/mutation must be observed by the
operator. Creation is sequential and nontransactional: retain exact returned
namespace/resource UIDs and every failure. Stop on any failure, unexpected
object, or mismatched label. A namespace exists briefly before its quota; do not
grant workload creation access or create workloads during this interval.

There is no new RoleBinding. Absence of a RoleBinding/token mount is not a proof
against inherited RBAC, anonymous API access or privileged cluster operators.
Record server dry-run, actual object/UID inventory, quota status, Pod Security
admission configuration and effective service-account permissions separately.
Infrastructure-only commands do not test pod rejection, CNI isolation or cleanup.

Before retiring anything, independently inventory the exact namespaces and their
UIDs, all namespaced resource kinds, foreign objects and retained storage. The
operator owns explicit targeted retirement; never delete by a broad label or
reuse a namespace containing unexpected state. No automatic deletion is provided.

## Still blocked

Outfitter retains durable admission, cumulative/native-unit budgets, stable
request/attempt identities, unknown liabilities and cleanup. Kubernetes quotas
are concurrent resource/object constraints, not its accounting authority. A
future adapter must reserve each possible start and retain ambiguous/late
effects without replay/refund; controller retries cannot manufacture attempts.
No broker adapter or usable budget is added here. No shared SQLite, PVC, host
mount, application replica, database migration, private data or service exposure
is proposed. Waypoint still owns identity and artifacts.

Runtime acceptance needs effective network denial (including DNS/metadata/host
paths), effective RBAC, immutable local image/platform identity, independently
bounded processes/output/lifetime, owned cleanup, failure/late-effect accounting,
resource/maintenance measurements and an adopt/defer/reject decision. OrbStack's
documented default Flannel does not establish NetworkPolicy enforcement; this
tool reports it UNKNOWN. No CNI replacement or cluster-wide component is added.
No new subscription or capacity is required by the offline package; actual
resource availability, recurring overhead and any incremental cost are unknown.

## Offline acceptance

Tests must cover deterministic rendering; exact two-project separation; zero
workload/controller/PVC quotas; security properties and nonlaunchable review
envelope; no subprocess/network usage; pinned local argv; rejection of remote,
credential-bearing, malformed and ambiguous endpoint inputs; changed/extra
files, flags, hashes and false/truthy values; special files and partial writes.
Run the oracle under normal Python and `python -O`; no correctness assertion may
depend on Python's `assert` statement. Preserve source hashes and honest offline
PASS/runtime NOT RUN evidence. These checks are not API-schema or cluster proof.

## Primary references

Checked 18 October 2026; these justify design choices, not local acceptance:

- [OrbStack Kubernetes](https://docs.orbstack.dev/kubernetes/): local cluster,
  shared image engine and default Flannel; no host state is inferred from docs.
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
  and [namespace labels](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/).
- [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/),
  [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/) and
  [service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/).
- [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  requires an enforcing network implementation; object acceptance is insufficient.
- [Pod scheduling gates](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
  and [Job starts](https://kubernetes.io/docs/concepts/workloads/controllers/job/).
