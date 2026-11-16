# EduCloud

A connected learning workspace: notebooks, governed AI tutoring, explicit submission and verifiable feedback. The current classroom pilot is **Learning Studio for INFO 511 NHANES**.

<!-- educloud-status-badges:start -->
[![License](https://img.shields.io/github/license/EduCloud-Ecosystem/educloud)](https://github.com/EduCloud-Ecosystem/educloud/blob/main/LICENSING.md)
[![Offline checks](https://github.com/EduCloud-Ecosystem/educloud/actions/workflows/resource-efficiency.yml/badge.svg?branch=main)](https://github.com/EduCloud-Ecosystem/educloud/actions/workflows/resource-efficiency.yml)
[![Open issues](https://img.shields.io/github/issues/EduCloud-Ecosystem/educloud)](https://github.com/EduCloud-Ecosystem/educloud/issues)
[![Contributing](https://img.shields.io/badge/contributions-guide-blue)](https://github.com/EduCloud-Ecosystem/educloud/blob/main/CONTRIBUTING.md)
<!-- educloud-status-badges:end -->

## Start here

- [How the components connect](docs/pilot/INTEGRATION.md): responsibilities, learner journey, contracts, recovery and release gates.
- [Shared implementation protocol](docs/development/PILOT_PROTOCOL_V1.md): one development and evidence standard across the six pilot repositories.
- [Automated maintenance](docs/development/MAINTENANCE.md): bounded checks and reviewable updates.
- [Contributing](CONTRIBUTING.md), [system contracts](SYSTEM.md), and [documentation index](DOCUMENTATION.md).

<!-- educloud-pilot-status:start -->
## Pilot status

**Local synthetic instructor testing: verified. Student deployment: pending.**

GitHub snapshot: 2026-11-16T18:45:22.051916+00:00. Refreshes are proposed by automation.
Check counts are observations at each listed main commit, including advisory tools; they are not a release verdict.

| Component | Pilot role | Main revision | Declared protocol | Observed checks | Open PRs |
| --- | --- | --- | --- | --- | --- |
| [educloud](https://github.com/EduCloud-Ecosystem/educloud) | Guide and release record | [b0db4bfa](https://github.com/EduCloud-Ecosystem/educloud/commit/b0db4bfa90909e1b814cf12ee2fb1db5b455bc24) | v1 matches | 2 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 4 |
| [belay-classroom](https://github.com/EduCloud-Ecosystem/belay-classroom) | Required for live tutoring | [9455a528](https://github.com/EduCloud-Ecosystem/belay-classroom/commit/9455a5283b6097e5b65e3269cc287efc23c8c277) | v1 matches | 5 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 0 |
| [cairn](https://github.com/EduCloud-Ecosystem/cairn) | Required for submission and grading | [1b6bf0d0](https://github.com/EduCloud-Ecosystem/cairn/commit/1b6bf0d04a63f546414aed98ed08f8d93734c45c) | v1 matches | 9 passed, 0 failed, 0 pending, 4 skipped/or/cancelled | 0 |
| [waypoint](https://github.com/EduCloud-Ecosystem/waypoint) | Required for notebook workspace | [df6ee645](https://github.com/EduCloud-Ecosystem/waypoint/commit/df6ee645556939819e4cd4b76bf6a544c0733cb2) | v1 matches | 4 passed, 0 failed, 4 pending, 1 skipped/or/cancelled | 1 |
| [portage](https://github.com/EduCloud-Ecosystem/portage) | Required for governed live model calls | [e3366502](https://github.com/EduCloud-Ecosystem/portage/commit/e3366502107e546f2651933e4549dd8da53c507a) | v1 matches | 1 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 8 |
| [outfitter](https://github.com/EduCloud-Ecosystem/outfitter) | Conditional on broker-managed compute | [bfc3ac48](https://github.com/EduCloud-Ecosystem/outfitter/commit/bfc3ac48acbae7fafb7893ee35a9332f848d5c15) | v1 matches | 3 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 0 |

Readiness is reviewed separately in [the evidence and release gates](pilot/readiness.json).
Outstanding: selected host/sign-in, approved data flow and retention, deployed backup/restore and cleanup, and human course acceptance.
Reviewed synthetic evidence: 13 workflow controls and 9 supplementary UI controls passed. Actual model requests in this evidence: 3. This does not qualify restricted data or student admission.
<!-- educloud-pilot-status:end -->

Scheduled maintenance currently produces verified **report-only artifacts**. Organization policy blocks bot-created PRs; automatic README publication is not enabled.

## Product lines

**Learning Studio** is the classroom notebook/tutor/submission experience. **Inquiry** is a separate research-driven course/capstone experience. Research POC, benchmarking and agentic science have separate evidence and release gates; classroom tests do not establish scientific validity or a self-organization advantage.

[Historical status](EDUCLOUD-STATUS.md) and [release gates](docs/specs/classroom-student-release-v1.md) retain earlier decisions and failures. Use the dated README snapshot and linked source pins for current observations. Absence of checks, a passing badge, or an old local demonstration is not student deployment acceptance.
