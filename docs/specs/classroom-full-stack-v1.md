# EduCloud classroom integration v1

Tracking: https://github.com/EduCloud-Ecosystem/educloud/issues/56

2026-11-12 continuation: [System One shadow pilot](system-one-pilot-v1.md)
adds typed advisory decisions to synthetic Portage/Belay traffic. See its source
map and validation record; it does not alter the historical evidence below or
establish trained-model or live-classroom acceptance.

Current checkpoint (2026-11-10): Waypoint draft PR59 at
`3ec286f5d41e857622d9b24f23b3c31e6f248605` passes the local synthetic notebook
journey, including native editor Save, optional stub tutoring, refused help,
no-AI explicit submission and receipt/reopen after restart. Exact-head hosted CI
is tracked separately in the adjacent JSON. This is ready for an independent
human synthetic walkthrough; institutional login, live GenAI, portable image
distribution, merge and deployment remain separate gates. The source maps and
intermediate checkpoints below preserve history; the latest presenter section
and validation JSON identify the active integration pins.

Greg selected **Belay-classroom** as the classroom pilot application. Original
Belay is excluded from this implementation. Reuse the existing classroom/notebook,
submission/review, inference gateway and compute broker before adding new services.

## One acceptance journey

Synthetic sign-in and current course admission → notebook work → governed tutor
through Portage → explicit saved-file submission → instructor review/export →
verified owned-resource cleanup. Saving is not submission; tutoring and compute
success are not grading; a placement receipt is not course admission. Independent
human assessment and actual learner/institutional acceptance remain separate.

## Ownership and source map

| Repository | Pinned source | Checkout/branch | Purpose |
| --- | --- | --- | --- |
| educloud | 5c0092a81e65f25c84e0b390c4f48b5e814a3e6f | `/Users/gregchism/dev/.educloud-worktrees/educloud-classroom-full-stack-v1`, `codex/classroom-full-stack-v1` | Program coordination and shared boundaries |
| belay-classroom | dba982c3a20241a14f1322fa3acf38261442ba88 | `/Users/gregchism/dev/.educloud-worktrees/belay-classroom-classroom-full-stack-v1`, `codex/classroom-full-stack-v1` | Classroom provider connection; notebook work already merged into this base |
| portage | 79742746b10ace18e498111dd5a8f3227edd995c | `/Users/gregchism/dev/.educloud-worktrees/portage-classroom-full-stack-v1`, detached and unchanged | Actual gateway/ledger dependency for synthetic acceptance |
| waypoint | 5c9df179a3f914e5ae9e6038f2bf7b95bf6bf824 | Existing `/Users/gregchism/dev/.educloud-worktrees/waypoint-classroom-notebook` at source parent 1e588874051bd97733d7f292c88e158fc3a6077b, unchanged | Reuse notebook workflow; select a new worktree before further edits |
| cairn | 04a9fe0a80f66ae5fa9da224b4be10aa184f9956 | Existing `/Users/gregchism/dev/.educloud-worktrees/cairn-cw1-csv-evidence` at source parent 9d7dca579d86fca1c2df00bd6711765e013d0974, unchanged | Reuse explicit submission and CSV review; select a new worktree before edits |
| outfitter | 6a974671f008640ddccd32547131ca6e696fefa4 | Existing `/Users/gregchism/dev/.educloud-worktrees/outfitter-consumer` at older 2f5f4c63efc229d1c6fe9370e0ec40277cef9b3b, unchanged | Review compatible placement/consumer integration before selecting implementation base |

Published pins are source review anchors, not blanket runtime acceptance or an
instruction to use the newest revision. Waypoint/Cairn selected source behavior
was inspected in the prior status review. The later Outfitter helper release does
not by itself establish native course-worker compatibility. Its actual base must
be selected against the consumer and the existing #1–#5 work, preserving ownership.

Primary checkouts contain unrelated changes and/or lag published code. None was
reset, cleaned, switched or staged. Existing worktree namespaces are preserved.

## Component boundaries and sequence

1. **Belay-classroom + Portage:** opt-in application credential and trusted
   classroom scope; actual SDK/gateway synthetic controls; no direct-provider
   fallback. Belay keeps safety, queue and conservative local holds. Portage keeps
   inference admission/accounting. Per-attempt receipt/status and monetary
   cutover remain missing. Portage requires opaque labels of 8–128 alphanumeric,
   underscore or dash characters; existing `edu:2` labels need an accepted trusted
   binding, not a local hash or invented identity.
2. **Waypoint + Cairn:** bind institutional issuer/subject to canonical opaque
   learner/course/assignment versions; current grants and revocation; preserve
   notebook save/reopen, explicit selected-file submission, instructor review and
   export. Reuse existing interfaces wherever possible.
3. **Outfitter + Waypoint:** versioned operator-reviewable placement handoff;
   verify current capacity/isolation/identity/lifetime before admission. Retention
   or export must survive the selected lifetime. Outfitter alone owns provider
   lifecycle, reservations, uncertain liabilities and cleanup. Existing issues
   #1–#5 and bmarkwart's assignment are preserved.
4. **Combined pilot:** synthetic browser journey, failure controls, independent
   reviewer/operator, human assessment/accessibility and operational recovery.
   Actual model and native-provider qualification are separate finite gates.

Core classroom MVP: Belay-classroom, Waypoint, Cairn and Portage, plus an approved
inference endpoint and host. Outfitter is required for the full-stack automated
placement/expiry/cleanup milestone; a pre-provisioned host can support preliminary
classroom testing without claiming that milestone complete.

## Current limits

The first implementation slice adds a provider adapter and executable synthetic
connection controls; it does not complete the entire stack. The pinned Portage
text-only gateway strips response_format and temperature. Engine format negotiation,
authenticated no-dispatch/accounting receipts and real model capabilities require
further integration. Do not remove local unknown holds based on an HTTP error or
an aggregate usage response.

No model/cloud/production execution, private learner/IRB data, automatic merge,
or stopped research panel is authorized by this program record. Work is ordinary
application integration, distinct from colony experiments. Existing research
protocols and evidence remain untouched.

## Collaboration

RozhinYs has pending invitations to all six repositories. The pre-existing
Belay-classroom admin invitation is preserved; five new invitations request write
access. Invitations are not active access until accepted. No original Belay
membership or issue was changed. Component issues are linked in the adjacent JSON.

## First slice delivered for review

Belay-classroom commit `b4b2c3c58539b8b7258cd61bfd9c911ffcddab25` is pushed in
[draft PR #5](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/5).
Local: 16 focused integration passes, full SQLite 1,082 passes / 20 skips, zero
failures; lint/format/mypy pass. Hosted actual-component integration, SQLite,
PostgreSQL and quality checks all completed SUCCESS. The adjacent validation JSON
records exact run/job/step results. Earlier local failures and cancelled superseded
push CI remain preserved; passing final results do not rewrite those histories.

Coordination is in [draft PR #57](https://github.com/EduCloud-Ecosystem/educloud/pull/57).
Neither PR is merged or deployed. Identity binding, presenter integration, receipt
cutover and native-provider/human acceptance remain open; no whole-stack completion
is claimed.

## Next consumer slice: roster identity and grant generation

The development continuation owns
`/Users/gregchism/dev/.educloud-worktrees/belay-classroom-roster-identity-v1`,
branch `codex/classroom-roster-identity-v1`, based on the existing provider head
`b4b2c3c58539b8b7258cd61bfd9c911ffcddab25`. This work is stacked on classroom PR5;
it does not modify original Belay or the provider dependency worktree.

The proposed consumer contract accepts an existing 32-character lowercase hex
Cairn roster ID unchanged when trusted authorization explicitly selects
`learner_id_kind: cairn_roster_v1`. It also requires a 32-character lowercase hex
`grant_generation`, supplied and never reused by the trusted authority. It does
not mint learner identities, hash legacy labels, or trust browser-selected scopes.
Legacy authorization and execution references remain compatible.

A changed generation invalidates old execution references and prevents the new
grant from retrieving or publishing the old unsaved job. Reservations, accounting
and uncertain liabilities remain intact. This is a consumer mechanism, not a
complete revocation service: restoring an identical old authorization file still
restores its reference. The Waypoint/Cairn producer must implement durable grant
issuance, freshness/deadlines, monotonic revocation, rollback prevention and verified
issuer/subject-to-roster binding before this can support a live course.

The existing Cairn roster format is implementation evidence. Selecting it as a
cross-component label and the new generation field remains a proposed interface
for review; no live authority integration or institutional enrollment acceptance
is claimed. Legacy Quad payloads and the historical synthetic notebook bridge
retain their existing contracts.

The next useful integration outcome after this consumer review is the trusted
producer/export path, with stale/missing/conflicting authority refusal and
revocation/regrant controls across both Belay-classroom and Portage. Keep operator
CLI/file steps where sufficient; do not create a second roster authority.

Consumer implementation is now published at commit
`0be46ae9a3154e9f9e17917cc8a6d6d3aafe8433` in
[draft classroom PR #6](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/6),
stacked on PR #5. Fresh hash-locked local validation: 229 focused passes; full
SQLite 1,112 passes and 20 explicit skips, zero failures/errors; lint/format/mypy
pass. Actual Portage gateway/SDK/ledger paths use a synthetic upstream. Hosted
results are tracked separately in the adjacent validation JSON. This remains
unmerged and undeployed; source/CI evidence does not establish course readiness.

Next executable integration gate: pin the authoritative Waypoint/Cairn producer
revisions and implement the smallest trusted enrollment export consumed here.
Use one synthetic principal and existing Cairn roster entry; prove that revoked,
stale, conflicting and rolled-back authority cannot dispatch work. Then exercise
one notebook-to-tutor-to-explicit-Cairn-submission journey, preserving distinct
submission confirmation, grading/result verification and resource cleanup.

Hosted integration run [42537799758](https://github.com/EduCloud-Ecosystem/belay-classroom/actions/runs/42537799758)
succeeded at the exact PR6 head. Downloaded JUnit independently confirms all
21 actual-Portage synthetic controls passed, zero skips/errors/failures. Main
SQLite/PostgreSQL/quality CI remains in progress at this checkpoint; the earlier
push run was superseded/cancelled, not reclassified as a pass.

## Finite enrollment producer/consumer delivered for review

Cairn [draft PR #38](https://github.com/EduCloud-Ecosystem/cairn/pull/38),
`0cf3158fdf5bbbecc52d3cc9cd88ef33bdfb63fc`, exports finite grants from a consistent,
read-only snapshot of the existing SQLite roster and assignment records. The
operator explicitly reviews the Waypoint issuer/subject-to-Cairn immutable account
binding and the assignment/exercise mapping. No inferred username/email join is
allowed. Output excludes host account IDs, usernames, grades and learner content.

Belay-classroom [draft PR #7](https://github.com/EduCloud-Ecosystem/belay-classroom/pull/7),
`656d6ec1e4be5f9ef7267f5a2bb5145a90238dfe`, is stacked on PR6. It consumes this
proposed versioned interface: `authority` with `schema_version=1`, `authority_id`,
`issuer`, `audience`, monotonically increasing `revision`, `issued_at`, `expires_at`;
existing `subjects` and `exercise_versions`; roster members with `grant_generation`.
The authority ID is pinned during explicit consumer-watermark initialization.

Cairn owns issuance history and preserves unchanged grant generations, rotating
on observed withdrawal, binding change or expiry gap. Belay checks finite lifetime
(maximum 300 seconds), current signed identity and durable rollback history at HTTP
and worker boundaries. Older revisions, same-revision conflicts, wrong authority,
missing history and legacy downgrade fail closed. The CLI/file handoff does not
create a new roster service or change Waypoint admission, Cairn submission/grading,
Portage budgets/accounting or Outfitter lifecycle authority.

Verified local evidence: producer build/vet/full race and dashboard typecheck,
25 tests/build pass. Consumer full backend 1,132 passed, 22 explicitly skipped;
lint/format/mypy pass. The separate native-component evaluator passes all 22 checks
without skips, including actual signed identity, current worker recheck, Portage
SDK/gateway/ledger transport, revocation/replay refusal and regrant. The two native
fixture tests skipped in the ordinary suite are executed by this evaluator.
Initial refused fixture mutations, mismatched Portage scope and the existing
synthetic-runner CLI timeout remain preserved; no failed control is erased.

Cairn's exact-head hosted main CI, recovery rehearsal and synthetic Outfitter
consumer workflows succeeded. The adjacent JSON tracks the new consumer's hosted
checks separately. These remain draft, unmerged and undeployed changes.

This is an operator-mediated synthetic enrollment path. Automatic institutional
identity linking and live IdP qualification remain open. Revocation between exports
is bounded by the original expiry; a remove/reactivate event between observations
is not detected. A privileged rollback of both issuance and consumer history is not
prevented. Portage account/budget setup and its current-membership responder remain
separate operator-managed controls; the acceptance responder is synthetic.

Next observable outcome: replace the historical Waypoint presenter's fixed test
identity with an explicit roster-bound profile and finite credential lifecycle,
then verify notebook -> private tutor -> selected saved-file submission -> Cairn
receipt/reopen. Preserve result verification and owned-resource cleanup as separate
checks. No model launch, institutional enrollment or live provisioning is implied.

Final hosted result at the exact PR7 head: SQLite, PostgreSQL, quality, Portage
and native enrollment workflows all succeeded. Downloaded native-enrollment
JUnit independently confirms 22/22 controls passed with no skips/errors/failures
(run 42547539745). The superseded push CI cancellation remains recorded.
The current integration increment is ready for code/interface review; the
notebook journey and real classroom launch remain unqualified.


## 2026-11-10 roster presenter and synthetic integrated journey

Waypoint [draft PR59](https://github.com/EduCloud-Ecosystem/waypoint/pull/59)
is at `fb53908077651121aabe194c77d6a50454878300`; implementation is
`1fdbcdc` (full pin and content hashes in the adjacent validation record).
Worktree: `/Users/gregchism/dev/.educloud-worktrees/waypoint-classroom-roster-presenter-v1`,
branch `codex/classroom-roster-presenter-v1`, based on merged
`5c9df179a3f914e5ae9e6038f2bf7b95bf6bf824`. No application edits were made to
Cairn, Belay-classroom, Portage, Outfitter, original Belay or their active owners'
checkouts. The dependent Cairn/Belay revisions remain the draft pins above.

The existing notebook proxy now accepts an explicit private roster profile,
current grant generation and finite server-held credential. The browser never
chooses its learner identity or receives the bearer token. Operator-disabled or
expired help cannot admit work. A small optional-hints page reuses Belay job
recovery and links to the existing saved-file submission bridge and human help.
No new enrollment service, registry, provider or grading authority was added.

Local acceptance: 742 course tests, four notebook snapshot checks, and the native
synthetic journey pass. The journey exercises actual Forgejo OAuth and Cairn
roster/assignment records, Cairn's exporter, signed Belay HTTP/jobs/worker, native
Jupyter selected-cell capture, optional deterministic stub help, expired and
disabled refusal, no-AI selected-file preview/confirmation, a real repository
receipt, byte-identical reopening, and receipt recovery after restart and explicit
student re-login. Keyboard/axe and desktop/390px inspection pass. Saving itself is
through the authenticated Contents API; manual save-button interaction is not
claimed. One job, one queue attempt and three stub attempts settled; no model
transport, SDK retry, paid call or inference occurred. Owned cleanup was verified.

Four failed integration runs and the original test-fixture failure are retained.
Corrections were the launcher configuration/packaged extension fixture, request
schema, isolated notebook kernel chooser, and the actual student re-login route.
The scope's four correction rounds are complete. No stopped research was resumed.
The new runbook is `course-workspace/ROSTER-PRESENTER.md`; the finite start/check/
stop evaluator and complete Python dependency lock are in `rehearsal/roster_presenter*`.
Private fixture evidence remains in the worktree output directory; the committed
record exposes allowlisted results/hashes only. Do not publish raw credentials,
course databases or private logs.

Remaining gates are explicit. Human usability is not accepted: rendered review
found that initial capture wording still says nothing was sent after a hint, and
the policy banner remains hints-permitted after a credential refusal. Correct
those states and exercise manual save interaction in the next bounded slice.
The HTTP refusal and saved-work controls passed. Institutional SSO, the actual
U of A GenAI interface, Portage operational membership/budget setup and live
hosting/Outfitter remain separate. Cross-machine reproduction needs distribution
of the two pinned local images; rebuilding the checkout image currently uses
mutable package acquisition. The stub is no evidence of educational quality.

Hosted workflows were pending at publication; use the adjacent JSON's exact-head
snapshot, not the local pass, to determine CI status. These are draft, unmerged,
undeployed changes. Next executable step: review this stack, close the specific
presenter usability controls, inspect exact-head CI, then perform a human synthetic
walkthrough. No real learner data or model endpoint is needed for that next gate.


### Presenter follow-up completed; current review checkpoint

Final Waypoint head: `3ec286f5d41e857622d9b24f23b3c31e6f248605`;
implementation follow-up: `349d734` (full hash in the adjacent JSON).
Cairn `0cf3158fdf5bbbecc52d3cc9cd88ef33bdfb63fc` and Belay-classroom
`656d6ec1e4be5f9ef7267f5a2bb5145a90238dfe` were rechecked unchanged/clean.
The current branch/worktree remains `codex/classroom-roster-presenter-v1` in the
Waypoint worktree named above. No ownership transfer or merge occurred.

The earlier stale wording and unexecuted native Save controls are now resolved.
A refused request updates the help notice and disables further asks while keeping
code/question intact. Capture text no longer says nothing was sent after a hint.
The actual Jupyter file editor is clicked, edited and saved with its keyboard
command; the saved bytes then pass the unchanged preview, confirmation, receipt,
reopening and restart controls. The restored kernel chooser is handled through
its ordinary No Kernel action. No notebook code or model endpoint is executed.
Screenshots were independently inspected after the final run.

There are two passing complete journeys (the earlier API-save path and final
native-editor path), six retained failed journeys, and the original test-fixture
failure. The explicit follow-up scope and its extensions are recorded before
execution in the scope JSON; original completed allowances were preserved.
Preparation, failure and reviewer effort are not a research performance result.
Final application accounting remains one completed job, a settled queue attempt
and three settled deterministic stub attempts, with zero external transport or
SDK retry. All owned runtime resources were cleaned after every attempt.

Final-head hosted CI is still in progress at this checkpoint; completed HTTPS,
maintenance, ownership/recovery checks are distinct from unfinished workflows.
The manually dispatched continuity job is skipped, not a pass. The next useful
step is dependency/interface review plus an independent human synthetic
walkthrough with `ROSTER-PRESENTER.md`. There is no remaining observed failure in
the final local journey. Human usability, cross-machine image delivery,
institutional SSO and the approved live GenAI endpoint remain unqualified.
