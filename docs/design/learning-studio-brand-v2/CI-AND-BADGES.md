# Advisory review and open-source badges — 2026-11-15

## Public repository badges

All ten public EduCloud repositories now have merged README badge blocks. Private HOST and portage-local were untouched. Badges link to the actual license and issue tracker, existing CI/test workflow, and contribution guide when one exists. Sonar and CodeRabbit appear only on belay-classroom, Cairn and Waypoint, explicitly advisory. No coverage percentage, release, security certification or deployment readiness was invented. Original Belay received README badges only, not new analysis tooling.

| Repository | Merged README PR | Merge commit |
| --- | --- | --- |
| educloud | [#66](https://github.com/EduCloud-Ecosystem/educloud/pull/66) | `ab8e7951cf61cc9739aa7b2b9ddc78097bb56c68` |
| belay-classroom | [#11](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/11) | `59bb84c6cd6d91af773417bd0e42acb0eb0d8eea` |
| cairn | [#45](https://github.com/EduCloud-Ecosystem/cairn/pull/45) | `2d8721b604bfd7aafb9fa03986f38c1ff90ea9fd` |
| waypoint | [#74](https://github.com/EduCloud-Ecosystem/waypoint/pull/74) | `dfdd8c696ef13885cad45ef824efacdf0ea4fa7b` |
| portage | [#19](https://github.com/EduCloud-Ecosystem/portage/pull/19) | `084d135dfef6b54435c911cdab38c30034189d3c` |
| outfitter | [#24](https://github.com/EduCloud-Ecosystem/outfitter/pull/24) | `cc3ea6f1a9bc5ef4f03c5d3ee61acb3d682fc472` |
| belay | [#28](https://github.com/EduCloud-Ecosystem/belay/pull/28) | `449c9266b68570419fae874768c7b4e89c4d74d9` |
| assignment-template | [#2](https://github.com/EduCloud-Ecosystem/assignment-template/pull/2) | `23815b61b2102c0430edd3c8eff5cdc18fdb89a0` |
| portage-CR | [#1](https://github.com/EduCloud-Ecosystem/portage-CR/pull/1) | `b53d4c952560552b086fe6e58a33774de337218d` |
| verifier-contract | [#1](https://github.com/EduCloud-Ecosystem/verifier-contract/pull/1) | `f85bd9ce8ed3282a641bf54c2af94b236d553060` |

Portage's follow-up [#20](https://github.com/EduCloud-Ecosystem/portage/pull/20) uses `event=pull_request` because its CI does not run on main-branch pushes; the returned SVG says passing. The assignment-template autograder is manually dispatched and returns no status; portage-CR has no workflow, so it has no CI badge. Outfitter's main workflow badge returned failing. These are actual service states, not suppressed failures. The README-only Outfitter and original Belay merges do not certify their still-running application tests; no application code changed in those PRs.

Validation: read all ten README blocks at their merge commits; verified linked repository files and workflows; downloaded actual badge SVGs. Python urllib was refused (403) by Shields, then curl successfully returned all requested license/issue/static SVGs. Retained acquisition, exact PR heads, merge records and responses: `/tmp/educloud-badges-20261115/`. No provider inference or cloud deployment was performed.

## Sonar test scope

Explicit source/test classification merged in belay-classroom [#10](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/10), Cairn [#43](https://github.com/EduCloud-Ecosystem/cairn/pull/43) and Waypoint [#72](https://github.com/EduCloud-Ecosystem/waypoint/pull/72). Both roots are `.`; matching test inclusions and source exclusions prevent double indexing while retaining test analysis. Candidate inventories were 93/271, 128/318 and 163/1348 test/source files respectively. The latest Belay automatic scanner context independently displayed these properties. No quality threshold or required-check protection was weakened.

## Initial finding triage

The downloaded Sonar BUG/VULNERABILITY counts (58 Belay classroom, 116 Cairn, 365 Waypoint) are scanner classifications, not verified vulnerability counts or a completed audit. A bounded review of nine prioritized security claims classified six as not actionable on inspected evidence and three as needing further ownership/input-boundary review. The latter concern local-dev static root symlinks and operator-owned recovery/authority input paths. No broad security clearance or source-system dismissal was issued.

Four actionable CodeRabbit Studio findings were implemented: refreshed assignment metadata, grade-revision-aware history refresh (including stale in-flight responses), single-flight assignment retries and consuming appearance handoffs once. Cairn source `240b8b9c9f802e759175f6941b34c194f780e84c`; Waypoint application/test changes `febf0b74db9890224118a7aac02d338855efc2ed`. Seven provider-disabled browser controls passed against the actual Cairn fixture; metadata/history and assignment-retry cases use injected API observations and do not constitute actual grading acceptance. Cairn API tests also passed. The three standalone theme scripts have identical behavior.

Waypoint's advisory Sonar gate still flags intentional duplicated standalone theme assets, test assertions within a failure-recording handler, and the roster checkpoint fetch. The handler records failures and exits nonzero; it does not convert assertions to a pass. The roster destination is same-origin, authenticated profile fields are encoded as path segments, and redirects are rejected; no cross-origin forgery was established. These remain visible findings, not silently suppressed or treated as a production security certification.

A fresh integrated rehearsal at Waypoint `febf0b7` failed because its observer read a temporarily empty notebook during Jupyter's write. The failed result and cleanup success were retained at `output/nhanes-instructor-20261115T201012Z-98370/result.json`; zero model requests. Waypoint `d75b90e` preserves the original 15-second bound, counts incomplete reads and waits for complete executed authored cells. Final integrated verification and source merge status are recorded below when observed.

## Post-review integrated result

Waypoint `d75b90e57eea5c74f6b30b7275f0a5ca50aeceb4` with Cairn `240b8b9c9f802e759175f6941b34c194f780e84c` passed all 13 actual local synthetic NHANES controls, 200.51 seconds, zero model transports, cleanup true. The v2 evidence records the prior failed save observation and seven supplemental UI controls. Waypoint documentation-only descendant `9b815043c8ec9162463fcc0ef2d4ef44b86255fe` publishes the record; it does not change the tested application tree. Cairn #44 merged after all CI and advisory reviews completed successfully. Waypoint #73 retains its advisory Sonar failure; other component CI and merge state must be checked at the final head. No new student deployment or live model call was performed.

Final merge/protection/maintenance evidence is recorded in [the pilot rollout](../../development/PILOT_ROLLOUT_V1.md). Waypoint #73 is merged with applicable deterministic CI passed, manual continuity skipped and the advisory Sonar failure retained.
