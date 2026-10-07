# EduCloud status and computing-continuity priority

Reassessed October 6, 2026 against current GitHub default heads, open PR metadata,
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
| Cairn | 641ea4318b70 | Most complete classroom product; existing host adapters, student views and operations paths. [Draft PR #1](https://github.com/EduCloud-Ecosystem/cairn/pull/1) adds per-class workspace navigation. Grading-manifest authority and resource-ceiling audit findings remain release gates for authoritative grades. |
| Waypoint | e5baceb4ebe6 | Existing local hosting/identity proof; [draft PR #1](https://github.com/EduCloud-Ecosystem/waypoint/pull/1) adds JupyterHub Python/R workspace deployment and offline recovery. This is the supporting compute path, not a completed institutional hosting service. |
| Outfitter | b2cbdcad5b05 | Specifications only. Defer generalized brokering; later adopt the running workspace lifecycle as the first consumer and add a second host only after recovery is proven. |
| Belay | 89f25971749f | Working tutoring core. New PR #12 proposes authenticated institution/class isolation; it is unmerged and its current check rollup is empty. PR #11 has changed since September's audit. Neither was accepted by this pass. Not required for the computing MVP. |
| Portage | 2ec86ad0447d | Working routing components, eight open PRs with unchanged heads. September's staff-profile renderer finding still applies to those exact heads. Not required for Python/R compute. |
| verifier-contract | 9a0a84f76b08 | Existing contract/conformance foundation. Keep the required consumer-matrix work on the release backlog; not a dependency of notebook availability. |
| educloud | c1b1e9cea7f7 | Public status was stale; this reassessment and decision refresh it. Original local strategy edits and unpublished commits are preserved. |

The six core module default heads have not changed since the September audit.
This does not mean no work occurred: Belay has an additional open identity PR,
and its UI PR was updated. Open proposals are not shipped behavior.

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
4. Close Cairn's assessment-integrity findings before relying on its grades.
5. Run one real class and record availability, support effort, recovery time,
   concurrency and actual operating cost. Add Outfitter placement only when
   multiple provisioned backends create a demonstrated need.

The deployment and recovery implementation is in Waypoint `course-workspace/`;
Cairn's integration contract is `docs/course-workspaces.md`. Detailed rationale:
`docs/decisions/2026-10-06-computing-continuity.md`.

## Implementation and validation from this reassessment

Both implementation PRs are drafts; nothing is merged or publicly deployed.
Cairn's full Go race suite passed, followed by the API race suite with added
removed-roster coverage. Waypoint's five policy tests and complete synthetic
continuity verifier passed: Python/R kernel execution, learner separation,
runtime/network checks, workspace recreation, live-backup refusal, new-namespace
restore and overwrite refusal. Playwright confirmed the browser launcher and
retained files. This was linux/arm64 on local Docker Desktop, with two synthetic
learners. It is not second-physical-host recovery, class-scale acceptance, or
live institutional authentication. See the Waypoint PR's VALIDATION.md.
