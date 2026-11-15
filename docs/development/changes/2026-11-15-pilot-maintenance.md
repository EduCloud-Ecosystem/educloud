# Pilot maintenance implementation record

Owner request: hold all pilot repositories to the same implementation standard;
make educloud the holistic integration/status guide and support high-quality
bounded agent maintenance. This authorizes the shared guidance, deterministic
verification and reviewable status automation. No runtime deployment or new model
inference is part of this change.

Scope: educloud, belay-classroom, Cairn, Waypoint, Portage and Outfitter. Preserve
existing application worktrees, original Belay and all private repositories.
Application-specific tests remain authoritative; shared checks do not replace them.

Implementation: a versioned identical protocol, per-component verification inventory,
root agent guidance and read-only CI, plus a central integration guide and generated
README snapshot with separate manual readiness. A scheduled main-only updater
proposes two allowlisted documentation files, explicitly requests CI and never
self-merges. Acquire only declared public metadata, with finite request/page limits.

Validation: offline verifier; status rendering and failure/injection controls;
actual public snapshot; component protocol check execution; inspect PR diffs and
merge/branch-rule state before declaring rollout complete. Record source/CI and
release state separately. Local synthetic instructor acceptance is independently
pinned and retains failures. See CI-AND-BADGES.md for the preceding review pass.

## Organization-policy finding

The first real maintenance run, 43758610325, collected and validated public metadata but failed when organization policy denied the bot PR. The repository-level enablement request returned HTTP 409; organization settings were not changed. The generated proposal branch and failed run remain evidence. The repair checks policy before remote writes and retains an artifact in report-only mode. The fallback and two-file write allowlist have dedicated offline controls. PR automation remains policy-blocked until explicitly enabled by the organization owner.
