# EduCloud classroom integration v1

Tracking: https://github.com/EduCloud-Ecosystem/educloud/issues/56

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
