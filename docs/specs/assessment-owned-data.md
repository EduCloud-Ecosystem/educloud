# Temporary assessment ownership — first implementation slice

Implementation contract, October 19, 2026. This narrows the approved
[assessment lifecycle](research-assessment.md) and
[A1/A2 backlog](../strategy/research-pilot-build-backlog.md). It authorizes
source implementation and disposable synthetic regression tests, not operational
uploads, trusted cleanup, actual measurements or a deployed service. The
[accepted preparation/export increments](../research/2026-10-19-assessment-preparation-acceptance.md)
remain unchanged.

## Boundaries and owners

Outfitter owns data scopes in its existing journal, locks and Watch/Reap
authority. Waypoint owns current user/project authorization, session metadata,
stream handoff, local denial and content-free inspection. There is no second
ledger, queue, worker or scheduler. No compute attempt, reservation, allowance or
provider record is invented for an upload-only session. Portage and Cairn need
no new execution path for this slice; Ben's assignments remain unchanged.

The retained study Worker is not an assessment backend. Its input snapshots,
raw results/diagnostics, output sidecars, exports and recovery copies remain
valid study behavior but must never receive temporary assessment content.

Production content admission is unconditionally disabled. Waypoint installs a
disabled assessment service and refuses content mutations at route recognition,
before its ordinary body reader or storage effects. Outfitter identifies
prepare/ingest/seal from fixed command arguments and refuses before reading
stdin. Any parsed control operation must match those arguments. No CLI flag,
environment/config/header, imported receipt, claimed encryption or public
boundary factory can enable positive admission. Status/cancel/reconcile parse
only bounded control metadata and cannot open access.

Positive tests inject a visibly synthetic boundary into the real lifecycle
functions. Separate Go test-helper commands exercise the real Watch/Reap and
ingest implementations; no alternate lifecycle or persistent test service is
introduced. The helper/injection factory is absent from production entry points.
All trust, actual-resource, upload and execution authority flags remain false.
Synthetic removal cannot reach contract `closed`; it remains denied and
`cleanup_unresolved` even when an owned test file is observed absent.

## Metadata and wire contract

Use an opaque, server-generated upload-session/owned-data `scope_id`, immutable
project and paired authority bindings, the exact canonical manifest/digest,
absolute expiry, owner/watch/writer epochs, generations and closed observations.
Keep the mapping to the original manifest assessment identity explicit; never
rewrite an imported manifest to change its identity or digest. Scope identity is
not an attempt or reservation. No caller filesystem path, original filename,
source-content hash, raw error, command, credential or content enters retained
session/journal/guard/receipt metadata.

Benchmark manifest v1 is unchanged and has no upload-ceiling field. Add
`declared_upload_ceiling_bytes` to the new session/control envelope. It must be a
strict positive bounded integer, no greater than `manifest.ceilings.scratch_bytes`
and the stricter injected boundary policy. Reject excess instead of clamping.
This is neither measured input size nor proof of physical storage capacity.
Scope expiry cannot exceed manifest expiry, project end, initiating
authorization expiry or stricter policy. Control/scope `expires_at` share the
manifest's canonical whole-second `YYYY-MM-DDTHH:MM:SSZ` representation and match
each other exactly; scope expiry may be earlier than the manifest. Select the
minimum allowed instant, round down to whole seconds and refuse if no future
lifetime remains. Broker-created creation/observation/high-water timestamps may
use exactly six fractional digits. Compare timestamp instants without changing
the original manifest serialization or rounding an expiry upward.

Reject duplicate/unknown keys, invalid identifiers, booleans substituted for
integers, overflow and nonfinite numbers. Bound control input/output, individual
stream chunks, live writers, metadata rows/encoding and observation history.
Retain earlier observations unchanged and keep cleanup eligible at admission
limits; these logical bounds do not qualify whole-store capacity or quotas.
Freeze the exact component codec and shared public control/status fixture before
Waypoint integration. Reply fields are observations, never permission to admit
production content. No attempt-bound measurement/cleanup receipt is fabricated.

## Ownership, process lifetime and denial

1. Commit the Waypoint session/control intent under existing authorization and
   guard/database fencing. Outfitter durably records ownership before directory
   creation, and records its one watch start before spawning it. Exact duplicate
   prepare returns metadata only; collisions refuse. Never hold global journal
   or SQLite locks across IPC, stream I/O, readiness waits or removal.
2. The existing Waypoint HTTP process owns the sole owner-lifeline write end;
   the per-scope watcher owns a separate sole watch-lifeline write end. Trusted
   launch code explicitly passes only the required descriptors and closes its
   temporary copies. The watch acknowledgement binds scope, authorities,
   generations, epochs and immutable deadline. A PID or stale ready file is not
   liveness evidence. Normal one-shot command exits are not owner restarts.
3. Ingest obtains the existing execution-lifetime and stable scope writer leases
   before irreversibly claiming its only writer. Check current bindings, owner
   and watch lifelines, denial and deadlines before claim/content I/O and between
   bounded operations. There is no upload replay. Exact length/EOF, sync/close
   and acknowledged durable completion precede sealing. A free lease or dead
   writer alone cannot establish successful upload.
4. Before stream handoff and between bounded transfers, Waypoint rechecks current
   session/project authority using existing fences. Cancellation, revocation,
   project closure, expiry, interrupted input and owner/watch loss latch denial.
   Logout conservatively denies nonterminal sessions initiated by that subject.
   Unknown acknowledgements lead only to status/cancel/reconcile, never another
   prepare/ingest effect. Local denial is not proof of remote revocation.
5. Cleanup acquires the same stable writer lease exclusively without waiting
   under the global journal lock, validates ownership and removes only the owned
   scope. An active/unknown writer or replaced/foreign/symlink/special scope
   remains unresolved. Unlink or process disappearance does not prove writer
   drain. Observe drain, access denial and removal independently; append bounded
   synthetic observations without converting them to trusted closure or reuse.

The trusted boundary may retain a named internal `filesystem_identity` tuple
for root/scope and stable writer/watch lease objects. Establish device/inode
identity from opened descriptors and compare it across acquisition; do not lock
a replaced inode while claiming exclusion against an old writer. Canonical
bounded decimal uint64 strings may represent internal identities without JSON
precision loss. Callers cannot supply these tuples, and public status excludes
them. Unknown/unsupported identity refuses; no truncation or path-based fallback
establishes ownership. These are local operational object identities, not
source-content hashes or independent-host proof.

Record one deadline against an injected shared clock epoch at initial prepare;
new commands never restart its duration. Enforce both wall expiry and that
immutable tick deadline. Rollback, changed/unknown epoch and restart uncertainty
deny admission. The real suspend-inclusive host clock is not selected or
qualified. Races with abrupt death or blocked system calls can leave in-flight
bytes/writers; retain uncertainty instead of promising immediate termination.
Local cooperating-process leases/pipes do not qualify host failure, hostile
privileged access or an independent cleanup failure domain.

## Fresh schemas and refusal of unsupported recovery

Use a fresh assessment-only Waypoint schema and fresh Outfitter version-6 data
profile through the existing stores/ownership machinery. No in-place migration,
ordinary production initializer or automatic promotion is authorized. Earlier
formats, digests and behavior remain unchanged. Test-only fresh paired-project
fixtures establish known metadata without creating a real compute grant.
Assert unchanged budgets, reservations, charges, run/native maps and meaningful
preexisting unresolved liabilities across every lifecycle/failure path.

Ordinary compute/native/consumer/project-init operations refuse assessment-only
state. Checkpoint, restore, activation, raw backup and study/content export refuse
before copying, destination creation or source sealing. Do not ignore the new
scope/session records or their cleanup liabilities to make old recovery work.
No automatic tombstone pruning or reuse is included. Same-path privileged
rollback and another restored admitting store remain unqualified risks.

## Delivery and evidence

The [connected AS1 source acceptance](../research/2026-10-19-as1-source-acceptance.md)
records merged Waypoint #53 after Outfitter #19. It accepts disabled source and
synthetic real-process/HTTP/Store checks only; operational gates below remain open.

The later [execution/checked-cleanup source acceptance](../research/2026-10-19-execution-source-acceptance.md)
records Outfitter #21's separate fresh test-only v7 execution authority. It keeps
permanent assessment/slot bindings, one-budget sequential phases and original
ownership closure. This does not migrate or activate v6/AS1, qualify independent
cleanup or grant production upload/execute authority. Its typed Waypoint
integration remains a separate implementation slice.

First deliver Outfitter's closed journal/lifecycle/codec, test-only project seed,
real process helpers and existing Watch/Reap branch. Then integrate Waypoint's
fresh session rows, current auth/guard hooks, disabled production routes and
connected synthetic HTTP/Store journey against the reviewed peer fixture.
Each component has one author; root independently reviews final immutable
source/evidence/CI and merges. Serialize full local suites and preserve failures.

Exercise two projects, revoked/expired/anonymous/viewer denial before bytes,
late authorization loss, concurrent writers, lost acknowledgements, scope/watch
loss before and after readiness, short/overlong/interrupted/blocked streams,
clock rollback/restart, root/lease replacement, foreign resources, I/O/journal
failure, observation saturation and unsupported recovery/export refusal.
Seed synthetic content/filename/hash/error markers and inspect retained stores,
guards, ledgers, diagnostics and exports for leakage. This is application-level
synthetic evidence, not OS/proxy/swap/backup or real-host deletion acceptance.

Worker and independent cleanup hosts, encryption/key lifecycle, proxy spool,
swap/crashdump/backup exclusions, storage/TTL policy, operator/window, operational
metadata retention and a fresh finite native-unit allowance remain unknown.
No purchase or resource request is established as necessary. These choices and
qualified implementation/evidence are required before operational enablement;
this source slice grants none of them. Actual A2 measurements, A6 reproduction,
accessibility and whole-service privacy gates remain open.
