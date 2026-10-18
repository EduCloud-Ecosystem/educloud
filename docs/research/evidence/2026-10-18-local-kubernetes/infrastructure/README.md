# Local foundation: operator observation and timeout correction

The host owner used the frozen `5686eb317df3bcd5bdbd08834518ad1186ece5a2`
bundle, manifest SHA-256
`74d0a56b1835389b88deaa78884003738eaa807956da2ab21685107bf8a244b2`,
against the explicitly pinned local OrbStack endpoint/context. The renderer did
not execute these operations. Original bundle bytes and the initial offline
evidence remain unchanged; the earlier evidence manifest's source hashes refer
to `5686eb3`, not the corrected source. This is a separate observation, not a
relabelling of that offline record.

The retained operator records show:

- Two namespaces and eight policy objects created, with exact UIDs in
  `operator-observation.json`. Namespace-generated default accounts/root-CA
  ConfigMaps are outside that ten-object count.
- Fourteen final command records succeeded. Two earlier policy validation
  attempts timed out fetching local OpenAPI data with the original five-second
  deadline. Validation was not disabled. The host owner explicitly used a
  30-second timeout for subsequent commands; the renderer now defaults to that
  same finite request deadline. Pod termination grace remains five seconds.
- Both namespaces rejected a valid Pod server dry-run for exceeding zero quota.
  Both initially attempted Pod Security negative probes were schema-invalid
  (`privileged: true` with `allowPrivilegeEscalation: false`): those two FAIL
  records remain visible. Corrected `hostPID: true` negative probes were rejected
  specifically by restricted Pod Security v1.36 in both namespaces.
- Targeted worker checks returned `no` for create Pods, get Secrets and create
  Jobs in both namespaces. The zero-workload observations contained no objects
  in the queried workload/storage/service/secret kinds. This is six targeted RBAC
  denials and two empty observations, not proof of universal isolation or every
  possible API permission.

There are twelve passing control rows and two retained failing control rows.
These and the command counts overlap. The host owner identifies the Pod probes
as **server dry-runs only**; full submitted request bodies are not in this packet.
No actual Pod/Job/workload was created or executed. Namespace-b quota usage
counters lagged its object inventory for LimitRanges and service accounts; quota
status is not a settled capacity census. The initial ordinary stdout parser
failure is recorded separately in the observation: policy creation outputs are
a stream of JSON objects, not one JSON document.

`operator-source-hashes.json` binds the eighteen original private operator records
and seven frozen bundle files. Raw command records remain with the operator;
credentials/kubeconfig were not read or published. The public observation keeps
the relevant failed responses. This reporting agent inspected files only and did
not contact an engine or repeat any operator test.

`normal.log` and `optimized.log` record fifteen offline tests each on the corrected
source (overlapping), including rejection of a rehashed five-second plan. The new
`manifest.json` binds corrected source and this supplemental evidence. All original
offline evidence remains byte-identical.

**Boundary:** infrastructure creation and these admission/permission denials are
observed. Workload execution is **NOT RUN**, NetworkPolicy enforcement and whole-
store capacity are **UNKNOWN**, and an Outfitter Kubernetes adapter is **NOT
IMPLEMENTED**. The old v4 allowance remains exhausted. No image promotion,
database migration, new execution allowance or general cluster-adoption claim is
made. Image/platform availability, actual isolation, bounded output/PIDs/lifetime,
durable attempt accounting, cleanup/late effects and recovery remain gates.
