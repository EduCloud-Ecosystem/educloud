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

GitHub snapshot: 2026-11-15T20:33:47.241103+00:00. Refreshes are proposed by automation.
Check counts are observations at each listed main commit, including advisory tools; they are not a release verdict.

| Component | Pilot role | Main revision | Declared protocol | Observed checks | Open PRs |
| --- | --- | --- | --- | --- | --- |
| [educloud](https://github.com/EduCloud-Ecosystem/educloud) | Guide and release record | [65f3010b](https://github.com/EduCloud-Ecosystem/educloud/commit/65f3010b87e09ce60865edc5aa23a9605d105b37) | v1 matches | 1 passed, 1 failed, 0 pending, 0 skipped/or/cancelled | 2 |
| [belay-classroom](https://github.com/EduCloud-Ecosystem/belay-classroom) | Required for live tutoring | [9455a528](https://github.com/EduCloud-Ecosystem/belay-classroom/commit/9455a5283b6097e5b65e3269cc287efc23c8c277) | v1 matches | 3 passed, 0 failed, 2 pending, 0 skipped/or/cancelled | 0 |
| [cairn](https://github.com/EduCloud-Ecosystem/cairn) | Required for submission and grading | [e03cb424](https://github.com/EduCloud-Ecosystem/cairn/commit/e03cb42405ed14014150cc3d4e33df8679476bb8) | v1 matches | 9 passed, 0 failed, 0 pending, 4 skipped/or/cancelled | 0 |
| [waypoint](https://github.com/EduCloud-Ecosystem/waypoint) | Required for notebook workspace | [63104113](https://github.com/EduCloud-Ecosystem/waypoint/commit/631041130c3f3d42ef23d06f5c0a713cd18760af) | v1 matches | 2 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 3 |
| [portage](https://github.com/EduCloud-Ecosystem/portage) | Required for governed live model calls | [e3366502](https://github.com/EduCloud-Ecosystem/portage/commit/e3366502107e546f2651933e4549dd8da53c507a) | v1 matches | 1 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 8 |
| [outfitter](https://github.com/EduCloud-Ecosystem/outfitter) | Conditional on broker-managed compute | [bfc3ac48](https://github.com/EduCloud-Ecosystem/outfitter/commit/bfc3ac48acbae7fafb7893ee35a9332f848d5c15) | v1 matches | 2 passed, 0 failed, 1 pending, 0 skipped/or/cancelled | 0 |

Readiness is reviewed separately in [the evidence and release gates](pilot/readiness.json).
Outstanding: selected host/sign-in, approved data flow and retention, deployed backup/restore and cleanup, and human course acceptance.
The latest synthetic rehearsal passed 13 workflow controls and seven supplementary UI controls, with no model requests. It does not qualify restricted data or student admission.
<!-- educloud-pilot-status:end -->

Scheduled maintenance currently produces verified **report-only artifacts**. Organization policy blocks bot-created PRs; automatic README publication is not enabled.

## Product lines

**Learning Studio** is the classroom notebook/tutor/submission experience. **Inquiry** is a separate research-driven course/capstone experience. Research POC, benchmarking and agentic science have separate evidence and release gates; classroom tests do not establish scientific validity or a self-organization advantage.

[Historical status](EDUCLOUD-STATUS.md) and [release gates](docs/specs/classroom-student-release-v1.md) retain earlier decisions and failures. Use the dated README snapshot and linked source pins for current observations. Absence of checks, a passing badge, or an old local demonstration is not student deployment acceptance.
