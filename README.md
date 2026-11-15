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

GitHub snapshot: 2026-11-15T20:26:11.389513+00:00. Refreshes are proposed by automation.
Check counts are observations at each listed main commit, including advisory tools; they are not a release verdict.

| Component | Pilot role | Main revision | Declared protocol | Observed checks | Open PRs |
| --- | --- | --- | --- | --- | --- |
| [educloud](https://github.com/EduCloud-Ecosystem/educloud) | Guide and release record | [ab8e7951](https://github.com/EduCloud-Ecosystem/educloud/commit/ab8e7951cf61cc9739aa7b2b9ddc78097bb56c68) | not installed | 0 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 2 |
| [belay-classroom](https://github.com/EduCloud-Ecosystem/belay-classroom) | Required for live tutoring | [59bb84c6](https://github.com/EduCloud-Ecosystem/belay-classroom/commit/59bb84c6cd6d91af773417bd0e42acb0eb0d8eea) | not installed | 4 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 0 |
| [cairn](https://github.com/EduCloud-Ecosystem/cairn) | Required for submission and grading | [22930438](https://github.com/EduCloud-Ecosystem/cairn/commit/229304381b7312bbb9bf2014c63b201132965e24) | not installed | 8 passed, 0 failed, 0 pending, 4 skipped/or/cancelled | 0 |
| [waypoint](https://github.com/EduCloud-Ecosystem/waypoint) | Required for notebook workspace | [dfdd8c69](https://github.com/EduCloud-Ecosystem/waypoint/commit/dfdd8c696ef13885cad45ef824efacdf0ea4fa7b) | not installed | 1 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 3 |
| [portage](https://github.com/EduCloud-Ecosystem/portage) | Required for governed live model calls | [97ef5cbd](https://github.com/EduCloud-Ecosystem/portage/commit/97ef5cbdf1fd10479de917203602ded3c42cda0e) | not installed | 0 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 8 |
| [outfitter](https://github.com/EduCloud-Ecosystem/outfitter) | Conditional on broker-managed compute | [cc3ea6f1](https://github.com/EduCloud-Ecosystem/outfitter/commit/cc3ea6f1a9bc5ef4f03c5d3ee61acb3d682fc472) | not installed | 2 passed, 0 failed, 0 pending, 0 skipped/or/cancelled | 0 |

Readiness is reviewed separately in [the evidence and release gates](pilot/readiness.json).
Outstanding: selected host/sign-in, approved data flow and retention, deployed backup/restore and cleanup, and human course acceptance.
The latest synthetic rehearsal passed 13 workflow controls and seven supplementary UI controls, with no model requests. It does not qualify restricted data or student admission.
<!-- educloud-pilot-status:end -->

## Product lines

**Learning Studio** is the classroom notebook/tutor/submission experience. **Inquiry** is a separate research-driven course/capstone experience. Research POC, benchmarking and agentic science have separate evidence and release gates; classroom tests do not establish scientific validity or a self-organization advantage.

[Historical status](EDUCLOUD-STATUS.md) and [release gates](docs/specs/classroom-student-release-v1.md) retain earlier decisions and failures. Use the dated README snapshot and linked source pins for current observations. Absence of checks, a passing badge, or an old local demonstration is not student deployment acceptance.
