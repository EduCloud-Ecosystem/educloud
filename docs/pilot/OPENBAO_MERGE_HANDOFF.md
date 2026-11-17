# OpenBao merge handoff — 2026-11-16

Scope: prepare source and CI, with **default activation closed**. No deployment,
new model requests, custody import or student admission occurred in this
preparation. All three PRs remain drafts without auto-merge.

| Component | Review | Proposed source | Purpose |
| --- | --- | --- | --- |
| Portage | [PR 22](https://github.com/EduCloud-Ecosystem/portage/pull/22) | `4e6eb8b14a230ddcfe8abf81d419d2ebbd4e28b1`, `codex/openbao-local-trial` | Optional credential source, service identity, recovery and Linux controls |
| Waypoint | [PR 77](https://github.com/EduCloud-Ecosystem/waypoint/pull/77) | `83aa20e7937a065cc920a7d0dbc343d996100ba4`, `codex/waypoint-openbao-local-trial` | Explicit optional NHANES consumer and preflight refusal |
| EduCloud | [PR 75](https://github.com/EduCloud-Ecosystem/educloud/pull/75) | `codex/openbao-merge-preparation`, based on `e56b6e1` | Adoption evidence, custody checklist and this handoff |

Local worktrees:

- Portage: `/Users/gregchism/.codex/worktrees/portage-openbao-trial/portage`
- Waypoint: `/Users/gregchism/dev/.educloud-worktrees/waypoint-openbao-local-trial`
- EduCloud: `/Users/gregchism/dev/.educloud-worktrees/educloud-openbao-merge`

The umbrella branch contains only OpenBao documentation/evidence. Unrelated
Studio status work and another owner's untracked audit directory are preserved.

## Verification and limits

Portage's exact proposed head passed all four hosted workflows. The downloaded
[Linux control artifact](https://github.com/EduCloud-Ecosystem/portage/actions/runs/43988778585)
was inspected: 22 transport/rotation and 20 identity/recovery controls passed,
both failure arrays were empty and cleanup was confirmed. Artifact `14285579636`
has SHA-256 `8b15edd57a42d85db237e62727bf0bd77679b0c2bd2419417f2485d7927085a9`.
It contains sanitized results/control logs, not recovery material, storage or
private TLS keys. CI makes no model requests. Artifact retention is finite.

Portage's `src/`, `integrations/` and `tests/` are identical to historically
live-tested `124da40`. The descendant adds current-main protocol files, checker
lint compatibility and synthetic CI. Historical live evidence retains its pins.

Waypoint passed eight focused NHANES tests locally. Sonar initially flagged a
preflight assertion. The fix uses explicit validation; its regression checks
nonzero exit, retained failure, no resource creation and zero requests. Sonar
passed at `83aa20e`. An optimized-Python test attempt stopped at the shared
runner's deliberate refusal of disabled assertions. That guard remains;
optimized mode is unsupported, not a passing test. The earlier Sonar failure
and older CI runs remain in GitHub history. Broader course/worker/recovery checks
must settle successfully at the proposed head before merge; PR 77 gives current
results. The dispatch-only continuity check is intentionally skipped.

EduCloud passed the protocol verifier, 16 status tests and generated-status
consistency before this documentation addition. Its PR check gives the final
documentation-head result. No readiness pins or generated pilot status changed.
CodeRabbit skips draft reviews; no completed review is implied. Portage's paid
review job is skipped with settings unchanged. Human review and branch rules
remain separate from passing CI. This is no new-head live classroom run.

## Merge order and activation gate

1. Review and merge Portage 22 first. Use a merge commit to preserve Waypoint's
   exact pinned producer as an ancestor; the repository permits this method.
   If squashing or rebasing, update and verify the consumer pin before its merge.
2. Confirm Waypoint 77's exact-head checks and review, then merge the optional
   integration. It changes neither the default launcher nor the static-key pin.
3. Merge EduCloud 75's instructions and historical evidence. Source integration
   is not activation, a student release or institutional acceptance.
4. Keep default activation closed until the **actual target instance** has
   verified custody and recovery under the [operator checklist](OPENBAO_CUSTODY_CHECKLIST.md),
   plus existing host, service isolation, certificate and course acceptance gates.

The current recovery package is a local rehearsal with a one-day certificate.
Putting it in a password manager cannot qualify a future hosted instance. That
instance needs its own package and verified independent recovery path. The prior
drill read a staged private file; it does not prove retrieval from Greg's vault
or separate backup. No secret values belong in this handoff or a PR.
