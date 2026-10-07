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
| Cairn | ceaee433f3a3 | PRs #1 and #2 merged; deployed on the existing pilot host. Workspace navigation, pinned instructor grading policy, read-only test files, provenance and operator per-step ceilings are implemented. Live host acceptance passed. HTTPS, retention and broader assessment/operational gates remain. |
| Waypoint | dd968f4392b5 | PRs #1 and #2 merged. Python/R computing and recovery passed on local arm64 and fresh Linux amd64 CI, including a Linux archive-permissions fix. A separate notebook worker is not yet provisioned/deployed. |
| Outfitter | b2cbdcad5b05 | Specifications only. Defer generalized brokering; later adopt the running workspace lifecycle as the first consumer and add a second host only after recovery is proven. |
| Belay | 89f25971749f | Working tutoring core. New PR #12 proposes authenticated institution/class isolation; it is unmerged and its current check rollup is empty. PR #11 has changed since September's audit. Neither was accepted by this pass. Not required for the computing MVP. |
| Portage | 2ec86ad0447d | Working routing components, eight open PRs with unchanged heads. September's staff-profile renderer finding still applies to those exact heads. Not required for Python/R compute. |
| verifier-contract | 9a0a84f76b08 | Existing contract/conformance foundation. Keep the required consumer-matrix work on the release backlog; not a dependency of notebook availability. |
| educloud | db5593a11324 | Initial reassessment merged; this follow-up records actual deployment and outstanding compute infrastructure. Original local strategy edits and unpublished commits are preserved. |

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
separate notebook worker. No notebook host/account/budget is recorded; that
connection/selection is pending from the operator. No cloud purchase was made.

Cairn doctor reports no failures, with outstanding warnings for plain-HTTP
webhook configuration and unset grade retention. Existing operator authentication
remains enabled. The service still uses shared-kernel grading containers. Do not
read health/CI success as approval for real learner data without HTTPS, retention,
institutional policy and the relevant isolation/assessment review.

The notebook deployment still needs its dedicated worker, live Keycloak roster
and revocation tests, wildcard HTTPS, per-home quotas, capacity testing, encrypted
off-host backups and recovery on another host. Existing Belay/Portage findings
remain outside this release.
