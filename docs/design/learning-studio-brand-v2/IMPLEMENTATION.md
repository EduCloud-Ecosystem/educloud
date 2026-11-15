# Studio Classic implementation handoff — 2026-11-15

Local synthetic instructor testing is ready. This is not a public deployment, student admission, a new live-provider acceptance, or a human accessibility certification.

| Component | Worktree | Branch | Base | Current commit |
| --- | --- | --- | --- | --- |
| Waypoint | `/Users/gregchism/dev/.educloud-worktrees/waypoint-studio-classic-v1` | `codex/studio-classic-v1` | `df2f26569d488d16aa5ddad8059a47d441606171` | `6a550b6` (application tested at `c554bfcc2be6bcfadf048acec23af61e80954d31`; subsequent commit adds evidence and supplemental harness) |
| Cairn | `/Users/gregchism/dev/.educloud-worktrees/cairn-studio-classic-v1` | `codex/studio-classic-v1` | `46c963b59feb67324714e308e8243c779cb14a81` | `a6322abfa687a206e659e8e874134ad8effad8b1` |

These branches preserve the independent audit fixes and original worktrees. The audit chat continues its separate base-PR CI work. Its later Waypoint `9d936d9` is a compatibility fix for older inline checksums in another rehearsal; the new Classic test uses the newer disclosure markup. It is not incorporated into this branch yet. The app-managed worktree creation tool stalled twice; local isolated Git worktrees were used instead.

Implemented: Light/Dark/System across the native notebook, embedded tutor, saved-file picker, Cairn student pages and built instructor console; default Light; appearance enum only in local storage/cross-origin handoff. Sharing destination is adjacent to the hint action; declaration reminders are explicit. Required checkpoint disables Ask and remains server enforced. A loading race in Back navigation was found and fixed. Result-detail errors have a keyboard retry; refresh preserves expanded history/focus. Automated checks and instructor-reviewed grades are labeled separately.

Verification: 13 actual local synthetic NHANES integration controls passed, including native kernel output of 192 rows, required checkpoint refusal with no admission, a stub hint, natural tutor expiry followed by save/submission, wrong CSV 0/4, correct CSV 4/4, four byte-exact published files, changed-payload 409 and receipt persistence after restart. Zero provider requests; cleanup succeeded. Four separate actual Cairn fixture controls covered injected detail 503 recovery, stable history, student modes/persistence and instructor dark mode/reflow. 764 Waypoint tests, Cairn API tests, dashboard build and 25 dashboard tests passed. Failures and private raw evidence remain retained; see Waypoint `docs/studio-classic-verification-v1.json` and `docs/studio-classic-testing-v1.md`.

Run `course-workspace/launch-nhanes-instructor.command --stub` from the new Waypoint worktree for a finite synthetic review; `--verify-stub` reruns the controls. The separately authorized `--live` mode retains its explicit prepared-question action and finite provider limits. No live model request was made in this implementation pass. Production host, identity integration and student release remain separate gates. Component source changes are local commits, not merged or deployed.

## CI tool decision

Use SonarQube Cloud's OSS plan for public, OSI-licensed component repositories. Start with Cairn and Waypoint, then extend after triage; retain existing deterministic tests, race checks, dependency/container checks and workflow checks. Make initial quality reports advisory, then gate new code once coverage mapping and false positives are understood. CodeRabbit should be an advisory pilot, not merge authority; measure actionable findings, noise and reviewer effort before wider adoption. No subscription or CI app was installed in this pass.

The official pricing page accessed on 2026-11-15 advertises free OSS eligibility for public OSI-licensed repositories; paid Team starts at $34/month for 100k private LOC. Enterprise is unnecessary for this pilot. Source: https://www.sonarsource.com/plans-and-pricing/ . Public CodeRabbit review offering: https://www.coderabbit.ai/faq . Recheck terms before subscribing.

## Public repository and license changes

Greg narrowed publication to `educloud` and `belay-classroom`; both were changed from private to public and verified through GitHub. `portage-local` and `HOST` remain private. A redacted Gitleaks 8.30.1 check of all advertised branch/tag history found candidates that were reviewed as SHA256 file manifests and test-control names, not credentials. This bounded check is not a comprehensive privacy or security certification.

Only public `educloud` and `assignment-template` lacked root licenses. Apache-2.0 was added using the existing experiment license verbatim, consistent with the umbrella's governance convention. LICENSING.md preserves third-party, dataset, separately licensed component and learner-work rights. License-only PRs merged: educloud #65 (`1eb2423d6fd1edfcbfcd81d573279e5548370bde`), assignment-template #1 (`23da5b6fad5da554a32e56cde781ef00e34437d6`). Existing component licenses were not replaced. The connected GitHub app lacked branch-write scope; the authenticated GitHub CLI completed the authorized changes.
