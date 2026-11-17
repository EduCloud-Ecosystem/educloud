# OpenBao local pilot adoption review — November 16, 2026

Greg authorized review, service identity and recovery custody, integration when
ready and another full classroom workflow. This follow-up integrates an optional
local instructor path; it does not replace the default working pilot, merge the
component branches, deploy a host or open student admission. The existing manual
readiness source pins remain unchanged.

## Decision and responsibilities

Portage owns the provider credential and reads it from TLS-protected, loopback-only
OpenBao before request admission. Its named `portage-classroom` AppRole can read
one path. Single-use login credentials and their delivery wrapper expire after
60 seconds; service tokens last at most 20 minutes and cannot self-renew. Bootstrap
root is revoked before the classroom process starts. Waypoint receives only the
service connection/token reference; learners and Belay do not receive a provider
key, root token or recovery package. Course authority and cost accounting remain
with their existing components. OpenBao is optional infrastructure, not a new
admission, grading, reservation or privacy-compliance authority.

Greg chose an institutional password manager plus a separately held backup for
recovery custody. A private import record is staged outside Git and runtime output.
It holds the unseal share and scoped recovery-operator password, not bootstrap
root. The staging file is plaintext with owner-only access, not an encrypted vault.
Actual institutional-vault import and independent backup have not been confirmed.
No connected password-manager integration is available to verify those steps.

Recovery starts with admission stopped. A cold Raft backup is restored separately
from the Portage accounting ledger. A fresh operator process unseals the service,
invalidates restored service tokens and pending login credentials, and prepares a
new service handoff. Restoring secrets does not erase outstanding usage or extend
course access. Local tests check actual recovery, not merely backup-file existence.

## Source and rollback map

| Component | Tested application source | Local branch |
| --- | --- | --- |
| Portage | `124da40b12e6422a0106181c14a60c622ec53927` | `codex/openbao-local-trial` |
| Waypoint | `3c8232c405b5190dc554bea31f9d631accb077fd` | `codex/waypoint-openbao-local-trial` |
| Cairn | `533c16a414b9fef1979d0de783b3436f31dd03a7` | unchanged |
| belay-classroom | `c5a27073e74b9eeb7ab697190915378b50132883` | unchanged |

The original Portage `b72881f`/Waypoint `de70188` pilot remains the source rollback;
its launchers and provider key were not changed. The new path remains opt-in on
separate branches. Evidence and remaining controls are recorded in the adjacent
[verification record](../../pilot/evidence/openbao-adoption-2026-11-16.json).

## Before persistent/default adoption

1. Import the private package into the restricted institutional password manager,
   verify retrieval, and verify a separately held backup. Remove the plaintext
   staging copy after both are confirmed. Greg owns this custody decision; do not
   silently nominate a second custodian or publish the package.
2. Review/merge the component changes and verify CI at the selected final heads.
3. On the selected maintained host, use separate OS service identities, accepted
   TLS renewal, recovery custody and capacity/restore/cleanup controls. This local
   fixture uses the operator OS account, one unseal share, and a one-day test TLS
   certificate. It does not qualify hostile student-code isolation or long-lived
   production operation.
4. Complete the existing human instructional, identity and data-use release gates.

The bounded local synthetic notebook/tutor/submission verification is useful now;
those later deployment requirements do not turn it into scientific, compliance or
student acceptance.

References: [AppRole](https://openbao.org/docs/auth/approle/),
[wrapped credential delivery](https://openbao.org/docs/concepts/response-wrapping/),
[token revocation](https://openbao.org/docs/internals/token/).


## Verified local results

The optional integration passed at the application pins above: 20 actual OpenBao
identity/custody controls, 13 unpaid browser controls and eight live classroom
controls. Portage regressions: 599 passed, nine skipped (six missing sibling
verifier integrations and three optional Belay-environment tests); five focused
Waypoint tests passed. Earlier broad Waypoint suites remain historical evidence,
not a claim of rerunning all of them for this pin-only companion change.

The live run made three actual model requests with zero SDK retries and
$0.0035944 provider-reported cost. Provider-internal retries are unobservable.
No new unknown usage remained; the historical $0.025 liability is still retained.
The NHANES fixture scored 4/4 and the deliberate wrong-output control failed.
Four saved files matched the repository receipt, which survived restart. The
receipt screenshot was also visually inspected.

After the classroom workflow, the actual Bao store was cold-restored. A fresh
operator process recovered it, invalidated the retired service token and verified
the provider credential without further inference. The independent accounting
file stayed byte-identical. Three classroom credential reads are recorded
separately from one denied retired-token read and one successful recovery read.
The credential/recovery-material leak scan passed; all owned services closed.

An initial unpaid browser run failed because Docker stopped during repository
preparation; cleanup could not finish then. Docker was started again, only the
failed fixture's labeled resources were removed, and Cairn's recovery inventory
verified zero remaining resources. The original failure remains unchanged beside
a separate successful cleanup-recovery record. No paid work was replayed.

Full sanitized evidence, source/environment/image pins and raw-result hashes are
in the verification JSON. Reproduction uses the same entrypoint/arguments as the
prior run plus `--custody-export`; the exact successful command is retained at
`output/openbao-trial/adoption-live-command.sh` in the Waypoint worktree. It is a
record, not standing permission for another paid run.

The private operator handoff for this retained local rehearsal is
`/Users/gregchism/Library/Application Support/EduCloud/OpenBao Recovery/classroom-adoption-01/HANDOFF.md`.
Importing a rehearsal package must not be treated as custody for a later hosted
instance. Generate and escrow that instance's own material at provisioning.
