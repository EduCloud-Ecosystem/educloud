# EduCloud status and computing-continuity priority

Reassessed October 6, with implementation/deployment status updated October 7,
2026 against current GitHub default heads, open PR metadata,
local working trees, and primary-source GitHub Education guidance. The original
July snapshot is preserved in `docs/research/2026-07-21-platform-status.md`.

## Decision

The first user-facing computing replacement is **browser Python/R coursework
with saved files and recoverability across hosts**. Finish the usable classroom
path around Cairn, the most complete EduCloud component, and adopt JupyterHub for
interactive computing. Do not require Belay, Portage or a new Outfitter broker
before learners can run notebooks.

Reliability means an accountable operator, funded baseline capacity, a portable
course image, durable homes, bounded resource use, and independently recoverable
backups. A second temporary credit offer is useful overflow, not continuity.

## Current component assessment

| Component | Verified main | Assessment and next completion gate |
|---|---|---|
| Cairn | 260984572cd29 | PRs #1–#3 merged. PR #3 preserves student login after denied operator requests; verified locally and in CI. The existing pilot still runs PR #2 (`ceaee433f3a3`); no production upgrade was made in this local-first pass. Workspace navigation, pinned instructor grading policy, read-only test files, provenance and operator per-step ceilings are implemented. Live host acceptance passed. HTTPS, retention and broader assessment/operational gates remain. |
| Waypoint | 0be6bfb5973a | PRs #1–#7 merged. Python/R workspaces, encrypted trial and institutional recovery, dedicated-worker configuration, hard XFS quotas and nginx/Keycloak preparation are implemented. Synthetic identity/course/revocation, institutional restoration, independent-worker trial recovery and quota/HTTPS checks passed. Real institutional identity, selected-host capacity and the actual backup account remain acceptance gates. |
| Outfitter | b2cbdcad5b05 | Specifications only. Defer generalized brokering; later adopt the running workspace lifecycle as the first consumer and add a second host only after recovery is proven. |
| Belay | 89f25971749f | Working tutoring core. New PR #12 proposes authenticated institution/class isolation; it is unmerged and its current check rollup is empty. PR #11 has changed since September's audit. Neither was accepted by this pass. Not required for the computing MVP. |
| Portage | 2ec86ad0447d | Working routing components, eight open PRs with unchanged heads. September's staff-profile renderer finding still applies to those exact heads. Not required for Python/R compute. |
| verifier-contract | 9a0a84f76b08 | Existing contract/conformance foundation. Keep the required consumer-matrix work on the release backlog; not a dependency of notebook availability. |
| educloud | 74a1ea4f78da | Prior reassessment, recovery, quota/HTTPS and authenticated course records merged; this follow-up records institutional workspace recovery. Original local strategy edits and unpublished commits are preserved. |

The October 6 baseline matched the September audit default heads. Cairn,
Waypoint and this umbrella have since advanced through the authorized merges.
Belay/Portage proposals remain separate from this release.

## GitHub Education: what changed and what remains

- GitHub Classroom retired August 28, 2026. The classroom-level Codespaces
  allowance for 50 students ended with it. Repositories and accounts remain.
- GitHub staff explicitly retained verified students' and educators' individual
  benefit: 180 core-hours and 20 GB of monthly storage allowance. Current student
  documentation still lists the personal benefit. At two cores, 180 core-hours
  is 90 running hours, not 180 hours on a two-core machine.
- Current billing documentation lists personal Free at 120 core-hours/15 GB-month
  and Pro at 180/20. Ordinary organization plans include no free Codespaces quota.
  Storage consumes allowance while a codespace exists; exhausted allowances can
  block use when no payment method is available.
- Copilot moved verified students to the distinct Copilot Student plan in March
  2026, with a changed model lineup. AI entitlements are separate from computing.
- Some Classroom integration documentation still describes the retired allowance
  beneath a retirement warning. That text does not supersede the explicit staff
  retirement notice. No official reinstatement was found in this review.

These are program-policy findings, not a check of Greg's or any student's actual
account status, billing settings, verification expiry or remaining allowance.

Sources checked October 6:
[Classroom retirement](https://github.blog/changelog/2026-08-27-github-classroom-deprecated/),
[GitHub staff benefit clarification](https://github.com/orgs/community/discussions/196615),
[individual student benefits](https://docs.github.com/en/education/about-github-education/github-education-for-students/about-github-education-for-students),
[current Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces),
[Copilot Student change](https://github.blog/changelog/2026-03-13-updates-to-github-copilot-for-students/).
The staff clarification is the May 28 comment in the linked discussion.

## Build sequence

1. Deliver the portable, one-course Python/R workspace and Cairn navigation.
2. Rehearse both kernels, own-file access, restart persistence and offline
   restore into a fresh namespace. Keep synthetic evidence separate from live
   institutional OIDC/TLS and actual second-host recovery.
3. Select the actual institution-controlled host, operator, capacity and backup
   destination. Enforce filesystem quotas, institutional roster/revocation and
   wildcard HTTPS before a real learner pilot. Separate this worker host from
   identity databases and other sensitive services.
4. Adopt Cairn's pinned instructor policy for each course, review its test harness
   and enforce aggregate execution, disk/output and isolation controls before
   relying on assessment results. The specific learner-manifest and per-step
   resource-ceiling findings are addressed by Cairn PR #2.
5. Run one real class and record availability, support effort, recovery time,
   concurrency and actual operating cost. Add Outfitter placement only when
   multiple provisioned backends create a demonstrated need.

The deployment and recovery implementation is in Waypoint `course-workspace/`;
Cairn's integration contract is `docs/course-workspaces.md`. Detailed rationale:
`docs/decisions/2026-10-06-computing-continuity.md`.

## Merged implementation and observed deployment

- [Cairn #1](https://github.com/EduCloud-Ecosystem/cairn/pull/1): workspace navigation.
- [Cairn #2](https://github.com/EduCloud-Ecosystem/cairn/pull/2): instructor grading authority and ceilings.
- [Waypoint #1](https://github.com/EduCloud-Ecosystem/waypoint/pull/1): notebook runtime/recovery.
- [Waypoint #2](https://github.com/EduCloud-Ecosystem/waypoint/pull/2): Linux archive permissions.
- [Waypoint #3](https://github.com/EduCloud-Ecosystem/waypoint/pull/3): minimal trial, bounded admission and resumable offline checkpoints.
- [Waypoint #4](https://github.com/EduCloud-Ecosystem/waypoint/pull/4): encrypted preserved-image recovery and dedicated-worker configuration.
- [Waypoint #5](https://github.com/EduCloud-Ecosystem/waypoint/pull/5): hard home quotas, quota-backed recovery and HTTPS/identity configuration.
- [EduCloud #1](https://github.com/EduCloud-Ecosystem/educloud/pull/1): priority/reassessment.

Cairn release `ceaee433f3a3ad12487824b132059fca10b7bc32` was built and
activated on the existing pilot host. The image's revision label and the running
container matched. HTTP health returned 200; anonymous classroom and grading-policy
requests returned 401. The served dashboard contains the new grading controls.
Application/database configuration was preserved, with a rollback image and
restricted on-host database/configuration snapshots retained before activation.
These snapshots are rollback preparation, not an off-host continuity solution.

The Go race suite, dashboard checks and real local browser policy-selection test
passed. The forged-score/read-only-policy Docker regression also passed **inside
the deployed Cairn container on the target Linux host**, using synthetic in-memory
records, without adding classroom data. Target data counts were unchanged.

Waypoint's [fresh linux/amd64 build/recovery run](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37586482789)
passed at PR #2's exact head. It executed both kernels, learner/network isolation,
workspace recreation, private offline archives, restore into fresh volumes and
overwrite refusal. The earlier run exposed Linux's chmod-after-chown restriction;
the fix sets archive permissions before transferring ownership without adding
capabilities. This complements the local arm64 rehearsal; it is not a cross-host
archive transfer or a live institution-authenticated notebook deployment.

## Deployment facts still requiring completion

The existing Cairn machine has 4 GB RAM and also hosts its database. It is not the
separate notebook worker. No remote notebook host/account/budget is recorded;
that connection/selection is pending from the operator. A local synthetic trial
is now available without buying infrastructure. No cloud purchase was made.

Cairn doctor reports no failures, with outstanding warnings for plain-HTTP
webhook configuration and unset grade retention. Existing operator authentication
remains enabled. The service still uses shared-kernel grading containers. Do not
read health/CI success as approval for real learner data without HTTPS, retention,
institutional policy and the relevant isolation/assessment review.

The notebook deployment still needs its dedicated worker, live Keycloak roster
and revocation tests, actual wildcard DNS/certificates, target-host quota/mount
and capacity acceptance, and an approved SFTP/S3 backup account. Synthetic quota,
HTTPS proxy and independent-runner recovery checks now pass, as recorded below. Existing Belay/Portage findings
remain outside this release.

## Minimal testing version and next completed build step

The operator trial is reduced to **one active synthetic learner**, one CPU and
1 GiB learner RAM, plus the separately capped 1 GiB Hub. It runs locally at no
additional hosting cost. The optional remote target is a separate 4 GiB / two
shared-vCPU / 80 GiB Ubuntu worker, using an SSH tunnel to the loopback-only
notebook port. DigitalOcean's Basic Regular bundled plan is $24/month before
taxes/backups as checked October 7 against its
[published pricing](https://www.digitalocean.com/pricing/droplets). The proposed
Droplet sizing has not been accepted on an actual 4 GiB worker.

Waypoint's `course-workspace/pilot.py` initializes private stable credentials,
starts/stops the trial without deleting files, and reports its status. The
[operator guide](https://github.com/EduCloud-Ecosystem/waypoint/blob/main/course-workspace/MINIMAL-PILOT.md)
contains local and SSH-tunnel setup. Test users alice/bob share a generated
password, with one active server at a time. This is not public student login.

The next continuity build step, `pilot.py checkpoint`, is implemented too: stop
the Hub and learner, archive the quiesced volumes with checksums and runtime image
metadata, then resume the previously running Hub. Failed backup attempts also
attempt to resume it. A previously stopped Hub remains stopped. Commands share
an operation lock, and existing archive paths and unrelated Hub containers are
refused. Direct Docker operations still require operator coordination.

Local arm64 acceptance passed at runtime commit `0da7491`: Python/R over notebook
WebSockets, inspected 1 GiB/one-CPU limits, blocked Internet access, a refused
second learner, file persistence through restart/checkpoint, and restored files
and kernels in fresh volumes. Thirteen unit tests passed, including failure
recovery and operation locking. The [fresh Linux amd64 run](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37668279326)
passed both the original two-user rehearsal and the new minimal-trial recovery
at that exact runtime commit. A real browser opened the Python/R launcher,
executed the Welcome notebook and saved its output; the CLI checkpoint then
resumed that Hub successfully. Checkpoint archives are private but remain local and unencrypted;
same-host restoration is not a second-host or off-host recovery claim.

## Encrypted recovery and hosted preparation (October 7)

The user selected **build and test locally first**. No Droplet, backup account,
public endpoint or institutional client was provisioned by this release.

Waypoint PR #4 packages quiesced files, private configuration, deployment scripts
and immutable Docker images into an encrypted Restic repository. Wrong keys,
ambiguous snapshot IDs, incompatible architectures and occupied restore targets
are refused. Backup status records failures and stale success; scoped retention
is previewed unless explicitly applied. Generated worker configuration and
systemd timers remain disabled until operator setup. Recovery currently supports
synthetic local-test deployments only; institutional migration is a further gate.

The [independent-worker rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37673554357)
passed at head `65d6188c2448a10ad06cac24e1161c3c9d5dd11f`; PR #4 merged as
`f99e7cebcb8d5e6db8083dfea92ba67be3ca343d`. Source and replacement jobs used
separate fresh Linux runners, transferring only the encrypted synthetic package
and metadata. The replacement rejected cached source images, restored saved files
and ran Python/R. This proves portable packaged recovery on that architecture;
it does not validate the future institution's backup account or service uptime.

Waypoint PR #5 merged as `0e92189689d0ad4af40131140d49651437f9491d` and
provisions hard byte/inode quotas on an administrator-prepared,
dedicated XFS mount. It never formats a physical device. Missing or stale health
status blocks new learner starts; actual limits remain enforced by the filesystem.
The synthetic Linux test exhausts a home, checks another learner can still write,
restores an encrypted quota-backed package and detects altered enforcement.
Ordinary backups from PR #4 remain supported.

The release also renders private nginx/Keycloak configuration. The client secret
is deliberately empty until installed by the operator. Actual nginx tests check
root/user TLS routes, redirect behavior, forwarded-header replacement, WebSocket
upgrades and unknown-host rejection. These are proxy tests, not an institutional
login or browser acceptance claim. Validation at runtime head `7649109` passed:
[quota-backed recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205120),
[nginx and unit checks](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205127),
and [independent-worker recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677205180).
The final documentation head `26128636b1151ed049c220cd1135c8504c391f37` was also
checked before merge: [quota](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747268),
[policy/proxy](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747049),
[recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37677747267).

The synthetic identity/course rehearsal is implemented (evidence below).
Institutional/OIDC encrypted recovery is now implemented with current-roster
configuration and fresh Hub sessions (evidence below). Hosted acceptance needs
the selected worker and backup account: real institution login/revocation,
wildcard certificates, reboot/mount behavior, load, recovery objectives and the
Cairn assignment/submission/grading path. Host disk/log monitoring, paging,
retention/departure procedures and institution-wide recovery acceptance remain work.
No Outfitter broker is needed to finish this first course.

## Authenticated course rehearsal (October 7)

The disposable harness uses real Keycloak, JupyterHub, Forgejo OAuth/repositories
and a pinned Cairn build. Cairn's Git-host login and the Hub's Keycloak login stay
separate. The browser follows Cairn's actual workspace link; notebook saving and
repository submission remain explicit separate actions.

The Forgejo/Cairn phase passed locally on macOS with a synthetic source-file
fixture: operator login, roster-only assignment acceptance, private repository
provisioning, student/operator and own-grade boundaries, and 10/10 versus 0/10
against the instructor's pinned tests. A learner's forged 999-point rubric had
no effect. The browser rehearsal exposed and verified the Cairn session fix in
[PR #3](https://github.com/EduCloud-Ecosystem/cairn/pull/3), merged as
`260984572cd2946ce8685c4d4b74d117c32fffea`. Its production pilot was not upgraded.

[Waypoint PR #6](https://github.com/EduCloud-Ecosystem/waypoint/pull/6) merged as
`8b0de72104940b8bdebac10010b00c1d085c4b91`. The final reviewed head
`91c4804d81bc57046839b4a434b6a0316073c404` passed the
[full Linux course rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782788),
[quota/recovery regression](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782945)
and [policy/HTTPS checks](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37688782865).
All 31 local unit tests passed. The accepted report records Cairn `260984572cd29`
and the actual GitHub PR merge checkout `60420007732a0e175589a797ce7a1f6826585573`.

Full acceptance verified Keycloak PKCE authentication, per-user HTTPS, real
Python/R kernel execution over WSS, explicit saved-file transfer, and correct
and incorrect pinned grading. Inspected screenshots show the saved `solution.py`
open in JupyterLab and the learner-visible instructor test with both grading
attempts. Authenticated peer file access, unrostered login, previous-session
access and respawn after roster removal were denied; no learner server remained
active, and the saved file survived revocation.
The notebook roster guard now returns an explicit 403 with an instructor-contact
message instead of converting an access denial into a generic server error.

The full harness creates its own disposable XFS image with hard quotas and a
short-lived fixture CA. Python/WSS clients and the Hub trust that CA explicitly;
the browser uses a fixture certificate exception. No certificate or hosts entry
is installed on the user's computer. The workflow publishes only bounded
synthetic evidence and screenshots after success, not fixture keys/databases.

This is not acceptance of an institutional realm, funded host, public DNS/TLS,
real backup account or class-size capacity. It requests grading explicitly;
automatic Forgejo push-webhook delivery, institutional identity-service recovery,
roster synchronization and automatic notebook submission remain separate work.

## Institutional workspace recovery (October 7)

[Waypoint PR #7](https://github.com/EduCloud-Ecosystem/waypoint/pull/7), merged as
`0be6bfb5973aff5764ec82d7f15d91b58bdad1b3`, extends encrypted Restic packages to OIDC courses. Recovery
requires a current operator-supplied roster and client credential while binding
the original issuer, client ID, public origin and home limits. All archived
homes survive, including retained work from removed learners. The replacement
starts with a new Hub database/cookie secret, so obsolete Hub sessions/tokens
are not recovered. No service starts automatically.

Final head `003e673c82343598b9a87462c22faad9c4465905` passed all 34 local unit tests
and these workflows:

- [Institutional recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362234):
  encrypted backup, destruction of source Hub/volumes/filesystem, current-roster
  restore on a fresh XFS filesystem, wrong-key/missing-current-config refusal,
  fresh Hub sessions, removed/unrostered and peer denial, saved files, Python/R,
  hard quota verification and active revocation with retained work after recovery.
  The successful report and browser screenshot of reopened coursework were inspected.
- [Independent-worker trial recovery](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362307):
  source backup and restoration on a separate clean runner passed.
- [Hard quotas](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362235),
  [complete course rehearsal](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362251),
  and [policy/HTTPS](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/37691362248): passed.

The institutional report records GitHub's tested PR merge checkout
`1201fe3efbdeca4b5bd2cb3362461b83c20f3bd3`; its saved image IDs are Hub
`sha256:e85c04026cfe2fe20ce09ddf5164ce646d4735a881fff64c30ac4259abae4df5`
and course `sha256:0e6ea23721d343dbed266e99884baf2c99e9d2033996abae1bb640cd726c22dd`.
See Waypoint `course-workspace/RECOVERY.md` for current-config requirements,
cutover, quota timers and backup/health service path updates.

The operator must supply genuinely current configuration; the tool cannot verify
its freshness. The IdP database/realm, DNS/TLS, CA trust and custom proxy/Compose
configuration remain separate dependencies. Institutional acceptance used an
independent surviving synthetic Keycloak instance on the same runner; it does
not establish institution-wide disaster recovery or acceptance of a real
SFTP/S3 account. No funded worker, public endpoint or production Cairn service
was changed.

The next local build should cover automatic repository-push grading delivery
and a bounded class-load rehearsal. Real-host acceptance still needs selected
worker/backup capacity, institutional identities, TLS, operational monitoring
and recovery objectives before admitting learners.
