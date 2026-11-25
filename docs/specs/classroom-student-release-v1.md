# Classroom student-release gate record

Tracking: [EduCloud #56](https://github.com/EduCloud-Ecosystem/educloud/issues/56). Updated November 14, 2026. Machine-readable owners, statuses and source pins: [classroom-student-release-v1.json](classroom-student-release-v1.json).

**Decision: ready for bounded local INFO 511 NHANES instructor testing; student admission remains closed.** The native notebook → live Belay-classroom hint through Portage → explicit four-file submission → Cairn receipt and separate grading path passed eight checks. It produced 192 rows, rejected the wrong output 0/4, accepted the correct CSV 4/4, refused changed previews and recovered receipts after restart. Three completed OpenRouter/OpenAI requests reported USD0.0036236, zero SDK retries and no new unresolved usage. Missing-checkpoint, expired and disabled help added no attempts. All owned services cleaned up. This is synthetic feasibility using a public extract and operator-authored answers, not instructional or student acceptance.

Start the [finite instructor launcher](https://github.com/EduCloud-Ecosystem/waypoint/blob/codex/nhanes-live-tutoring/course-workspace/NHANES-LIVE-TESTING.md). The final one-second human launch-path control passed with zero model requests, preserved the completed notebook cell and cleaned up. Exact source, environment, failed attempts, accounting and merge/CI status are retained in [the NHANES evidence record](../evidence/nhanes-classroom-live-2026-11-14.json). The historical USD0.025 unknown liability remains separate. Cairn PR40, Portage PR18 and Waypoint PR69 are merged with reviewed/tested trees matching their merges. All 14 applicable Waypoint PR checks passed; the manual continuity check was skipped. Four automatic Waypoint post-merge workflows were still running/queued at handoff; no post-merge pass is implied.

## Work assigned now

| Gate | Owner | Concrete next action | Acceptance needed |
|---|---|---|---|
| Runtime and R reliability | Existing Waypoint chat | Merged HTTPS-to-WSS fix; next prepare windowed diagnostics and qualify the pinned Rocker/editor candidate | Exact candidate, meaningful failure controls, Python/R as required by the selected course, save/restart and cleanup. Historical cause and current risk evidence reported separately. |
| Course package | Classroom coordinator; Greg selects and accepts content | NHANES native/live workflow passed; Greg reviews the finite instructor test | Run the chosen task through notebook, hint/refusal, saved files, explicit receipt and instructor review. Echo output alone is insufficient. |
| Hosting and real sign-in | Waypoint chat; host/identity administrators to be named | Prepare actual-host acceptance from existing runbooks after host and identity references are supplied | TLS, current admission, canonical identities, cross-user/course denial, revocation and restart on the selected deployment. |
| Data and student tutoring route | Classroom coordinator; Greg/institutional reviewers decide allowed flow | Record each store and outbound destination, then select and qualify the actual endpoint/profile | Student data must not inherit the synthetic OpenRouter authorization. Verify configured routing, refusals, real transport/retry accounting and unresolved liabilities. |
| Instructional quality | Greg or named instructor reviewer | Review the fixed cases below using the accepted assignment and an approved finite inference window | Independent human assessment, retained poor outputs, useful hints, no automatic grading or submission, usable non-AI completion. |
| Recovery and operating capacity | Waypoint chat; primary and backup operators to be named | Actual-host quota/reboot/backup/second-worker restore and workload rehearsal | Measured admission cap, current-policy restore, retained files, revoked-user denial, approved RPO/RTO, cleanup and usable export/teach-out. |
| Desktop accessibility | Human reviewer to be named, supported by engineering | Keyboard, screen-reader and zoom walkthrough of essential tasks | Record browser/assistive technology versions, errors and fixes; automated axe passes do not close this gate. Phone testing is deferred. |
| Pilot admission | Greg and named operating owners | Complete the release card below and review all included critical gates | Explicit acceptance of exact source, image, environment, course, cohort and allowed data; no admission from a green commit alone. |

The runtime chat owns its source branch and evidence. The classroom coordinator owns this record and the cross-component course/data contract. No collaborator is assigned an institutional or operator role merely because they have repository access. Dirty primary checkouts, historical evidence and mobile work are preserved.

## R direction

Greg requested Rockerverse containers if R is not working well in VS Code. Rocker is the preferred alternative to evaluate, while first locating the failing layer. The retained historical error was a Jupyter/CHP WebSocket handshake failure before R execution; it is not evidence that VS Code or R itself caused it.

The official [Rocker image documentation](https://rocker-project.org/images/versioned/rstudio) distinguishes the RStudio, tidyverse and verse images. `rocker/verse` includes RStudio Server plus publishing/TeX dependencies. Use the pinned candidate below only if the selected course/editor needs R; do not silently add RStudio as another ungoverned service or assume a different base image fixes transport. Retain admission, resource limits, saved-work ownership, expiry and cleanup conformance. The Waypoint owner has pinned a metadata-only Linux/amd64 candidate and its conformance checks; no image pull or runtime switch has occurred. Current source inspection found no R installation or R extension in `ide-pilot/Dockerfile`; this is an unimplemented R/editor combination, not a demonstrated R engine defect. A headless `r-ver` base alone does not supply VS Code integration or authorize an RStudio service.

A Python-only pilot may omit R only through an explicit course-scope decision. That would not erase the historical failure or waive qualification of shared transport and recovery paths.

## Independently inspected runtime checkpoint

Waypoint branch `codex/waypoint-runtime-release`, commit [100fdfa2317e1ce7705e0bbd94276770ba304723](https://github.com/EduCloud-Ecosystem/waypoint/commit/100fdfa2317e1ce7705e0bbd94276770ba304723), is based on merged `946f11bf0e64b7230b92631607e88e7c2dc4d4db`. It merged through [Waypoint #68](https://github.com/EduCloud-Ecosystem/waypoint/pull/68) at `96cc2b8c1922f06bb28933908d426a2efa849599`. All 14 applicable PR checks passed; manual continuity was skipped. The reviewed head, PR test merge and main merge have the identical tree `d9d1f2c1241aeda84e1920f20041260c928619fa`. No deployment occurred. Its structural HTTPS-to-WSS conversion preserves the origin/path and leaves the single kernel request, handshake and timeout unchanged.

The coordinator inspected the patch, controls and committed synthetic report and matched all four tested file hashes to that commit. The report correctly retains dirty-at-test provenance. The owner reports three new regression tests passing and 44 of 46 fixture checks passing, with two retained skips (host Docker SDK absent and Linux/root ownership). These unit results were not independently rerun. The inspected runtime report records exactly one bounded loopback TLS/proxy attempt: verified 101 upgrade, refused upstream 503 with one transport diagnostic, application 503 with no additional transport diagnostic, and verified cleanup. This does not execute a kernel or prove the historical 503 cause.

Later PR CI ran 763 policy tests (762 passed, one browser-dependency skip; a separate browser job passed). The coordinator inspected worker-channel, authenticated and enrollment reports with 17, 12 and 10 passing phases, respectively, verified cleanup and matched all 28/15/20 recorded source hashes. These exercise the existing Python/R image on synthetic CI infrastructure; independent-host recovery and Rocker/editor readiness remain open. [Merge evidence](../evidence/classroom-student-release-2026-11-14.json) retains source/image pins, CI links and report digests. All four automatic main workflows subsequently passed at `96cc2b8`. The coordinator also independently inspected the main worker/authenticated/enrollment reports: 17/12/10 passing phases, verified cleanup and all 28/15/20 source hashes matched. The earlier pending snapshot is retained in the evidence record.

The Rocker candidate is `docker.io/rocker/r-ver:4.6.2@sha256:3adf31fa5c953bdee2709023366d1bfba306e6dcbe8eb34bf8a668119e37d2ca` for Linux/amd64. Its recorded registry metadata is inspected; no Rocker runtime is accepted. Pin course packages separately. If VS Code R tooling remains unsuitable, qualify Rocker RStudio with the same admission, storage and lifecycle controls; choose tidyverse/verse when course requirements justify their additions.

Implementation and acceptance boundaries are in Waypoint `docs/runtime-student-release-plan.md`, with committed records under `docs/evidence/2026-11-14-runtime-release/`. Next engineering is windowed diagnostics and role-specific host inventory/installation, followed by encrypted worker-channel transfer and independently verified host fencing. Actual-host recovery, R execution and student admission remain open. The historical evidence packet is preserved.

## Concrete gaps found during intake

1. The connected browser proof uses a small fixed synthetic example. Greg selected the existing INFO 511 NHANES task on November 14. Its manifest still has source-bound/runtime-pending markers and unbound assignment IDs. Selection does not activate historical bindings or establish instructional/runtime acceptance; Lab 3 and INFO 557 are not the selected pilot task.
2. The live notebook/OpenRouter adapter intentionally permits only a fixed synthetic context and a finite transport window. It is not a general student tutoring endpoint. Portage's separate student registry contains unverified model metadata and environment references; its generated proxy configuration has retries. A configured registry is not evidence of a reachable, approved endpoint or complete retry accounting.
3. Synthetic login and local restore do not establish real identity, student-data hosting, separate-host recovery, support coverage or accessibility acceptance. Existing allocation, API key and IRB statements do not fill those records automatically.
4. The data-destination policy in the primary umbrella checkout contains dated implementation statements. Treat it as the current repository constraint to review, not a fresh compliance finding or proof that every documented control exists. Do not change destination policy or classify linked student work as public to make a pilot pass.

The November 14 checks below describe the tutoring-enabled configuration. The instructor subsequently selected the [AI-free profile for the first classroom pilot](../pilot/AI_FREE_FIRST_PILOT.md). Belay and Portage qualification still applies when a course enables tutoring.

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

Greg selected INFO 511 with the existing NHANES task. AWS is intended but no host is selected. Shibboleth/SAML is a probable future identity path; allowlisted GitHub with SSH was suggested as an interim option. Cohort size remains unanswered. These statements do not select a live issuer, host or student data route.

## Evidence and boundaries

Current Waypoint source/merge and component pins are in the adjacent JSON. The retained local packet is under `/Users/gregchism/.codex/worktrees/classroom-live-notebook/waypoint/output/classroom-reliability-v1/`; the fresh synthetic run is under `output/playwright/classroom-synthetic-2026-11-13/` in the same worktree. Private raw evidence is not copied into this repository.

Use Waypoint `course-workspace/rehearsal/TESTING-CHECKLIST.md`, `HOSTED-PILOT.md`, `RECOVERY.md` and `OPERATIONS.md` as the acceptance procedures. Actual Brightspace grade delivery is a separate gate only if included in scope; ordinary repository receipts are not grade publication. Outfitter native placement is separate unless selected; a pre-provisioned approved host can support the desktop pilot without claiming broker acceptance. Original Belay, physical mobile integration and colony research remain outside this work.

## Integration and deployment checkpoint

This release record is integrated separately from the older unmerged full-stack history, which remains preserved on `codex/student-release-gates-v1` at `8d02617a018ff81bde8533f9c144c726bb6e7e11`. The integration branch starts at umbrella main `923bb8f1014fee67bcd45352b4580a332b31e708`.

No hosted deployment target is verified: Waypoint has no GitHub deployment records, and its runtime owner confirms no existing accepted nonstudent host. The finite local reviewer and deferred mobile container are not persistent hosted deployment targets. A deployment still needs the selected host/identity and applicable release configuration; merging this record does not activate student access.

## Selected course and interim sign-in direction

The selected package is `info511-nhanes-wrangling-v1` at Waypoint `96cc2b8`, with its exact manifest digest in the adjacent JSON. It produces a 192-row table from the selected public NHANES files, with notebook, CSV, explanation and assistance statement submitted explicitly. The selected native desktop flow is now qualified under synthetic identities, including one prepared live hint, no-AI completion, wrong-output and changed-preview controls. The source-fixed live window is separately bounded; no real learner data or cloud deployment is included.

The recommended interim architecture is GitHub browser login through Keycloak, feeding the existing OIDC consumer. Enrollment remains a separate explicit course grant tied to stable subjects; an account's display username is not durable authority. SSH stays operator access, not browser sign-in or roster admission. Later, Shibboleth can connect through a SAML broker, with explicit verified account linking so a login change does not silently create a second learner identity. [Keycloak supports GitHub and SAML brokering](https://www.keycloak.org/docs/latest/server_admin/); the actual realm/client, admission mapping, revocation and migration still need configuration and acceptance. This is a recommendation, not a claim that either identity path is deployed.

AWS host selection, DNS/TLS, operator, resource envelope, backups, actual identity configuration and initial cohort remain pending. The selected public dataset does not make student submissions or tutoring payloads public. A bounded local instructor desktop rehearsal can proceed independently of those hosted/student decisions; it must retain its own finite start/stop and cleanup evidence.
