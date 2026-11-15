# Pilot standards rollout — 2026-11-15

The common implementation protocol is merged in all six pilot repositories. Byte-identical policy copies were independently fetched from their main commits. The protocol check passed on each main; API inspection confirmed active, matching branch rules: require a PR and an up-to-date `pilot-protocol` check from GitHub Actions (app 15368), block deletion/force pushes, no bypass actors. Existing component tests remain in place; Sonar and CodeRabbit remain advisory.

| Repository | Adoption PR | Inspected main | Ruleset |
| --- | --- | --- | --- |
| educloud | [#67](https://github.com/EduCloud-Ecosystem/educloud/pull/67) | `a7f59abbce40258a8da44980c3e2886513062f96` | 27330326 |
| belay-classroom | [#12](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/12) | `9455a5283b6097e5b65e3269cc287efc23c8c277` | 27330330 |
| cairn | [#46](https://github.com/EduCloud-Ecosystem/cairn/pull/46) | `e03cb42405ed14014150cc3d4e33df8679476bb8` | 27330332 |
| waypoint | [#75](https://github.com/EduCloud-Ecosystem/waypoint/pull/75) | `2112a380c99580b4aa250d4096bf6254d77c1f10` | 27330536 |
| portage | [#21](https://github.com/EduCloud-Ecosystem/portage/pull/21) | `e3366502107e546f2651933e4549dd8da53c507a` | 27330334 |
| outfitter | [#25](https://github.com/EduCloud-Ecosystem/outfitter/pull/25) | `bfc3ac48acbae7fafb7893ee35a9332f848d5c15` | 27330336 |

The shared check validates protocol/guidance/verification inventory, not application correctness. Path-filtered/manual application workflows are not magically made always-on required checks. Their relevant tests and integration evidence remain part of the implementation protocol. Zero additional required review approvals were configured; CODEOWNERS names the accountable owner. Bots do not gain merge/deploy authority.

## Actual maintenance execution

[Run 43759225489](https://github.com/EduCloud-Ecosystem/educloud/actions/runs/43759225489) succeeded at `a7f59abbce40258a8da44980c3e2886513062f96`. It ran 14 offline controls, collected 30 bounded public metadata responses, validated README/status agreement, uploaded artifact `14179232816` (`pilot-status-proposal`, 2803 bytes) and reported **REPORT ONLY** without repository writes. The downloaded artifact was inspected and its README was verified to differ only within the generated status block before this reviewed update. Artifact SHA-256s:

- `README.md`: `2d2a085aeb9bb6712d8f2e9e5b66e5ee61706edb504c620c6f0f70c6abf9f2f8`
- `pilot/status.json`: `4c27cc857a0942e882695612c4a25564fa28cca469797f4b1007c56c377236f7`

The schedule is every six hours; artifacts are retained for 14 days. The deployed job has read-only contents/actions/pull-request permissions. The organization disallows bot PR creation, and a repository-level enablement request returned 409. Organization policy was preserved. Automatic PR mode is dormant: enabling it requires an owner decision on organization policy plus a reviewed mode/permission change. This is not an automatically published README service.

Failures remain recorded: run 43758610325 failed opening a bot PR after successful collection; run 43758931667 produced an artifact but failed reading administrator-only permissions. The final job uses a reviewed local report-only declaration and needs no administrator API. The original generated branch and failed runs were preserved as evidence.

## Classroom source and evidence

Cairn #44 merged at `229304381b7312bbb9bf2014c63b201132965e24` after all CI/advisory checks passed. Waypoint #73 merged at `2112a380c99580b4aa250d4096bf6254d77c1f10` after 14 deterministic checks passed, manual continuity skipped, CodeRabbit passed; its advisory Sonar gate remained failed for the triaged duplication/assertion/request-destination findings. No threshold was weakened or finding hidden.

The tested Waypoint application `d75b90e57eea5c74f6b30b7275f0a5ca50aeceb4` and Cairn `240b8b9c9f802e759175f6941b34c194f780e84c` passed all 13 actual local synthetic NHANES controls, plus seven supplemental UI controls. Zero model requests; cleanup true. The failed incomplete-save observer run is retained. Git comparisons confirmed no application-tree differences between the reviewed Studio source and merged main (Waypoint course/research workspaces and Cairn cmd/internal/pkg/web). New workflow/governance files are separate changes, not a new runtime demonstration. See `pilot/readiness.json` and the pinned v2 acceptance record.

Student deployment remains gated by selected host/identity, approved data flow and retention, deployed recovery/cleanup and human course acceptance. Native Outfitter qualification is conditional on using its broker in the selected deployment. Research, restricted-data and scientific acceptance are separate.

## Local ownership and records

Work was performed in `/Users/gregchism/dev/.educloud-worktrees/educloud-classroom-full-stack-v1`, now on `codex/pilot-rollout-record`, and the owned Studio worktrees. `/Users/gregchism/dev/educloud` has extensive unrelated dirty work, including shared documents and untracked agent guidance; it was not overwritten or reset. The separate audit chat's `docs/audits/` namespace was preserved. Component adoption branches changed guidance/CI only through GitHub PRs, preserving local implementation checkouts.

Raw bounded acquisition, CI, merge, ruleset and artifact records are under `/tmp/educloud-protocol-20261115/`; badge acquisition is under `/tmp/educloud-badges-20261115/`; initial review and UI controls are under `/tmp/educloud-initial-triage-20261115/`. Durable source/evidence links above are the public handoff; temporary local paths are not promised permanent storage.
