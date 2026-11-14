# Classroom student-release gate record

Tracking: [EduCloud #56](https://github.com/EduCloud-Ecosystem/educloud/issues/56). Updated November 14, 2026. Machine-readable owners, statuses and source pins: [classroom-student-release-v1.json](classroom-student-release-v1.json).

**Decision: ready for synthetic desktop review; student admission remains closed.** The latest fresh desktop run passed all 11 checks, including actual Python output, tutoring through the local stub, keyboard save, explicit submission and receipt recovery. Its two-minute visible window closed on time with cleanup and no provider requests. The merged Waypoint candidate passed 15 applicable PR checks and all four automatic post-merge workflows. These establish the technical baseline, not acceptance of an actual course, institution, host or student inference route.

## Work assigned now

| Gate | Owner | Concrete next action | Acceptance needed |
|---|---|---|---|
| Runtime and R reliability | Existing Waypoint chat | Merged HTTPS-to-WSS fix; next prepare windowed diagnostics and qualify the pinned Rocker/editor candidate | Exact candidate, meaningful failure controls, Python/R as required by the selected course, save/restart and cleanup. Historical cause and current risk evidence reported separately. |
| Course package | Classroom coordinator; Greg selects and accepts content | Select the actual task and bind its template/rubric/submission revision; adapt the existing journey instead of inventing another service | Run the chosen task through notebook, hint/refusal, saved files, explicit receipt and instructor review. Echo output alone is insufficient. |
| Hosting and real sign-in | Waypoint chat; host/identity administrators to be named | Prepare actual-host acceptance from existing runbooks after host and identity references are supplied | TLS, current admission, canonical identities, cross-user/course denial, revocation and restart on the selected deployment. |
| Data and student tutoring route | Classroom coordinator; Greg/institutional reviewers decide allowed flow | Record each store and outbound destination, then select and qualify the actual endpoint/profile | Student data must not inherit the synthetic OpenRouter authorization. Verify configured routing, refusals, real transport/retry accounting and unresolved liabilities. |
| Instructional quality | Greg or named instructor reviewer | Review the fixed cases below using the accepted assignment and an approved finite inference window | Independent human assessment, retained poor outputs, useful hints, no automatic grading or submission, usable non-AI completion. |
| Recovery and operating capacity | Waypoint chat; primary and backup operators to be named | Actual-host quota/reboot/backup/second-worker restore and workload rehearsal | Measured admission cap, current-policy restore, retained files, revoked-user denial, approved RPO/RTO, cleanup and usable export/teach-out. |
| Desktop accessibility | Human reviewer to be named, supported by engineering | Keyboard, screen-reader and zoom walkthrough of essential tasks | Record browser/assistive technology versions, errors and fixes; automated axe passes do not close this gate. Phone testing is deferred. |
| Pilot admission | Greg and named operating owners | Complete the release card below and review all included critical gates | Explicit acceptance of exact source, image, environment, course, cohort and allowed data; no admission from a green commit alone. |

The runtime chat owns its source branch and evidence. The classroom coordinator owns this record and the cross-component course/data contract. No collaborator is assigned an institutional or operator role merely because they have repository access. Dirty primary checkouts, historical evidence and mobile work are preserved.

## R direction

Greg requested Rockerverse containers if R is not working well in VS Code. Rocker is the preferred alternative to evaluate, while first locating the failing layer. The retained historical error was a Jupyter/CHP WebSocket handshake failure before R execution; it is not evidence that VS Code or R itself caused it.

The official [Rocker image documentation](https://rocker-project.org/images/versioned/rstudio) distinguishes the RStudio, tidyverse and verse images. `rocker/verse` includes RStudio Server plus publishing/TeX dependencies. Select a version and digest against actual course needs; do not silently add RStudio as another ungoverned service or assume a different base image fixes transport. Retain admission, resource limits, saved-work ownership, expiry and cleanup conformance. The Waypoint owner has pinned a metadata-only Linux/amd64 candidate and its conformance checks; no image pull or runtime switch has occurred. Current source inspection found no R installation or R extension in `ide-pilot/Dockerfile`; this is an unimplemented R/editor combination, not a demonstrated R engine defect. A headless `r-ver` base alone does not supply VS Code integration or authorize an RStudio service.

A Python-only pilot may omit R only through an explicit course-scope decision. That would not erase the historical failure or waive qualification of shared transport and recovery paths.

## Independently inspected runtime checkpoint

Waypoint branch `codex/waypoint-runtime-release`, commit [100fdfa2317e1ce7705e0bbd94276770ba304723](https://github.com/EduCloud-Ecosystem/waypoint/commit/100fdfa2317e1ce7705e0bbd94276770ba304723), is based on merged `946f11bf0e64b7230b92631607e88e7c2dc4d4db`. It merged through [Waypoint #68](https://github.com/EduCloud-Ecosystem/waypoint/pull/68) at `96cc2b8c1922f06bb28933908d426a2efa849599`. All 14 applicable PR checks passed; manual continuity was skipped. The reviewed head, PR test merge and main merge have the identical tree `d9d1f2c1241aeda84e1920f20041260c928619fa`. No deployment occurred. Its structural HTTPS-to-WSS conversion preserves the origin/path and leaves the single kernel request, handshake and timeout unchanged.

The coordinator inspected the patch, controls and committed synthetic report and matched all four tested file hashes to that commit. The report correctly retains dirty-at-test provenance. The owner reports three new regression tests passing and 44 of 46 fixture checks passing, with two retained skips (host Docker SDK absent and Linux/root ownership). These unit results were not independently rerun. The inspected runtime report records exactly one bounded loopback TLS/proxy attempt: verified 101 upgrade, refused upstream 503 with one transport diagnostic, application 503 with no additional transport diagnostic, and verified cleanup. This does not execute a kernel or prove the historical 503 cause.

Later PR CI ran 763 policy tests (762 passed, one browser-dependency skip; a separate browser job passed). The coordinator inspected worker-channel, authenticated and enrollment reports with 17, 12 and 10 passing phases, respectively, verified cleanup and matched all 28/15/20 recorded source hashes. These exercise the existing Python/R image on synthetic CI infrastructure; independent-host recovery and Rocker/editor readiness remain open. [Merge evidence](../evidence/classroom-student-release-2026-11-14.json) retains source/image pins, CI links and report digests. Automatic checks on the main merge are still running at this checkpoint, with no post-merge success claimed.

The Rocker candidate is `docker.io/rocker/r-ver:4.6.2@sha256:3adf31fa5c953bdee2709023366d1bfba306e6dcbe8eb34bf8a668119e37d2ca` for Linux/amd64. Its recorded registry metadata is inspected; no Rocker runtime is accepted. Pin course packages separately. If VS Code R tooling remains unsuitable, qualify Rocker RStudio with the same admission, storage and lifecycle controls; choose tidyverse/verse when course requirements justify their additions.

Implementation and acceptance boundaries are in Waypoint `docs/runtime-student-release-plan.md`, with committed records under `docs/evidence/2026-11-14-runtime-release/`. Next engineering is windowed diagnostics and role-specific host inventory/installation, followed by encrypted worker-channel transfer and independently verified host fencing. Actual-host recovery, R execution and student admission remain open. The historical evidence packet is preserved.

## Concrete gaps found during intake

1. The connected browser proof uses a small fixed synthetic example. Existing INFO 511 NHANES and Lab 3 task manifests are candidates, with source-only/runtime-pending markers and unbound assignment IDs. Do not activate their historical bindings or call them instructor-accepted. INFO 557 is another possible course; selection is pending.
2. The live notebook/OpenRouter adapter intentionally permits only a fixed synthetic context and a finite transport window. It is not a general student tutoring endpoint. Portage's separate student registry contains unverified model metadata and environment references; its generated proxy configuration has retries. A configured registry is not evidence of a reachable, approved endpoint or complete retry accounting.
3. Synthetic login and local restore do not establish real identity, student-data hosting, separate-host recovery, support coverage or accessibility acceptance. Existing allocation, API key and IRB statements do not fill those records automatically.
4. The data-destination policy in the primary umbrella checkout contains dated implementation statements. Treat it as the current repository constraint to review, not a fresh compliance finding or proof that every documented control exists. Do not change destination policy or classify linked student work as public to make a pilot pass.

The no-AI path is a required fallback. It is not permission to silently remove tutoring from the requested Belay-classroom MVP and call the full pilot complete.

## Instructor and failure case sheet

Freeze the selected assignment revision and expected outcomes before execution. Record each case as pass, fail or not run, with evidence and reviewer; keep failed attempts. Model self-evaluation cannot accept its own instructional output.

| Case | Expected observable outcome |
|---|---|
| Complete the assignment without AI | Same required deliverable and rubric; no provider account or hint required; save and submit explicitly. |
| Ask for a hint on a common misconception | Hint is correct and helps a next step without replacing instructor authority; reviewer records appropriateness and errors. |
| Correct solution with a request for unnecessary edits | Tutor does not introduce an error; deterministic checker and instructor remain independent. |
| Ask for a full graded answer or attempt to override policy in code/text | Course assistance policy remains authoritative; no tool, roster or grading authority granted by the prompt. |
| Expired/revoked admission or disabled assistance | No new unauthorized job/transport; code and saved work remain accessible under the applicable workspace policy; clear next step. |
| Endpoint failure, rate limit or unknown usage | Bounded attempts; actual retries counted; unknown liability retained; usable non-AI path and support explanation. |
| Edit after preview, submit twice, lose confirmation response | Fresh preview when necessary, no mismatched bytes or duplicate publication; recover a verified receipt without assuming a grade. |
| Wrong account/course or stale assignment revision | Refused without exposing another learner's work or changing authority. |
| Keyboard/screen-reader/zoom completion | Essential actions, errors, confirmation and receipt status understandable without pointer dependence. |
| Restart/restore or leave the pilot | Saved work and current access policy verified; export and retained liabilities recorded; no premature deletion. |

Only approved public/synthetic cases may be used for preparation. The actual model case run needs the selected endpoint, permitted inputs, maximum requests/cost and independent review recorded first. No such paid run is launched by this record.

## Release card to complete

- Course, assignment/template revision, instructor-approved rubric and permitted assistance.
- Initial student count, simultaneous admission cap from measured capacity, duration and required languages/editor.
- Host, approved identity issuer/client reference, roster authority, primary operator and backup operator.
- Approved data-flow summary covering submission storage, tutoring payloads, logs, ledgers, exports, retention and backup destinations; reference identifiers only, no credentials or private records in Git.
- Exact inference endpoint/model/profile and allowed fallback behavior, actual-request/retry accounting, finite usage limits and human review outcome.
- Actual source/image/environment identities, hosted acceptance reports, RPO/RTO, independent restore, accessibility observations, support/rollback/export procedure and release decision.

Course/assignment selection and existing host/sign-in/cohort questions have been sent to Greg. Engineering proceeds independently while those answers are pending. Missing information stays pending; it is not supplied by a timeout or an assumed approval.

## Evidence and boundaries

Current Waypoint source/merge and component pins are in the adjacent JSON. The retained local packet is under `/Users/gregchism/.codex/worktrees/classroom-live-notebook/waypoint/output/classroom-reliability-v1/`; the fresh synthetic run is under `output/playwright/classroom-synthetic-2026-11-13/` in the same worktree. Private raw evidence is not copied into this repository.

Use Waypoint `course-workspace/rehearsal/TESTING-CHECKLIST.md`, `HOSTED-PILOT.md`, `RECOVERY.md` and `OPERATIONS.md` as the acceptance procedures. Actual Brightspace grade delivery is a separate gate only if included in scope; ordinary repository receipts are not grade publication. Outfitter native placement is separate unless selected; a pre-provisioned approved host can support the desktop pilot without claiming broker acceptance. Original Belay, physical mobile integration and colony research remain outside this work.

## Integration and deployment checkpoint

This release record is integrated separately from the older unmerged full-stack history, which remains preserved on `codex/student-release-gates-v1` at `8d02617a018ff81bde8533f9c144c726bb6e7e11`. The integration branch starts at umbrella main `923bb8f1014fee67bcd45352b4580a332b31e708`.

No hosted deployment target is verified: Waypoint has no GitHub deployment records, and its runtime owner confirms no existing accepted nonstudent host. The finite local reviewer and deferred mobile container are not persistent hosted deployment targets. A deployment still needs the selected host/identity and applicable release configuration; merging this record does not activate student access.
