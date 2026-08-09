# EduCloud ecosystem — shared conventions

This repo (`educloud`) is the umbrella of the EduCloud ecosystem: strategy,
platform-wide decisions, funding, governance, and the canonical definitions
every module repo implements against. It is not itself a module — it has no
`CC-<series>*` prompt series of its own. Module repos: `cairn`
(classroom/LMS), `belay` (AI tutor), `portage` (LLM routing engine),
`outfitter` (compute broker), `waypoint` (hosting/identity). `portage-local`
is a separate personal deployment, currently on hold — not part of this
ecosystem's active work.

## The platform invariant

No component trusts a model's — or a provider's — self-report. A
deterministic check decides success, always. Before citing a vendor's claim
(pricing, precision, model catalog, uptime, API behavior, grant/allocation
terms) as fact in a strategy doc or a decision record, verify it against the
primary source, not a summary or a marketing page. This repo is where
platform-wide claims get written down as settled for everyone else to build
against, which raises the cost of an unverified claim here more than
anywhere else in the ecosystem — a wrong fact in `educloud/SYSTEM.md` or
`DOCUMENTATION.md` propagates to six repos' worth of decisions.

## Where a decision belongs

This repo is where a decision spanning more than one module lives, so no
single module's repo becomes the de-facto owner of a platform-wide rule
(`docs/decisions/`, `docs/policy/`, `docs/specs/`). A decision that governs
only one module's own design belongs in that module's repo instead — e.g.
Waypoint's `docs/decisions/2026-08-08-analogue-scan.md` or Portage's
`docs/specs/13-routing-paradigm.md`. Outfitter's `specs/08` (isolation
tiers) is the one exception that proves the rule: it lives in Outfitter
because Outfitter provisions the compute, but it's normative for Cairn and
Belay too, so it's flagged as platform-level rather than being mistaken for
a broker-only concern.

## The CC-* prompt namespace — this repo owns the registry

Claude Code prompts across all six repos share one numbering namespace:
`CC-P*` (Portage), `CC-CA*` (Cairn), `CC-B*` (Belay), `CC-O*` (Outfitter),
`CC-W*` (Waypoint), `CC-HB*`/`CC-C*` (historical, closed series). **A
number means one thing platform-wide — collisions have happened twice
already** (CC-P9/P10 reused by accident, CC-C1 reused by accident). This
repo's `DOCUMENTATION.md` ("Prompt-number namespace" section) is the
registry of record for the highest number used in each series — when any
module repo mints a new prompt, that section here needs updating in the
same pass, not as a follow-up. If you're asked to scaffold a prompt for a
module repo from within this repo, still check that module's own
`docs/prompts/` directory directly rather than trusting the registry alone
— it can drift.

## Git conventions

- No `Co-Authored-By: Claude` trailers in this repo's commits. Check actual
  trailers, not prose: `git log -5 --format='%(trailers:key=Co-Authored-By)'`
  should print nothing — a plain `grep -c Co-Authored-By` over the log can
  false-positive on prose describing the convention (caught in Cairn by
  CC-CA5, 2026-08-09).
- Prefer new commits over amends; never force-push without being asked.

## Where things are

- `SYSTEM.md` — the canonical internal definition: names, module
  boundaries, the platform invariant, the eleven shared contracts, the
  scale table. Where an older doc conflicts, SYSTEM.md wins.
- `DOCUMENTATION.md` — the full doc index and the CC-* namespace tracker;
  keep this current whenever a doc moves, a module gains a new major doc,
  or a prompt series advances
- `EduCloud-White-Paper.docx` / `WHITEPAPER.md` — the platform definition
  for external audiences
- `LINE-E-ROADMAP.md` — execution roadmap E0–E4; the plan of record for
  sequencing across modules
- `EDUCLOUD-STATUS.md` — status snapshot; `DOCUMENTATION.md`'s "Known gaps"
  section is the more current version of the same thing — refresh both
  together, don't let one go stale while the other updates
- `strategy/`, `grants/` — funding and business-plan material
- `architecture/` — cross-module architecture memos
- `docs/decisions/`, `docs/policy/`, `docs/specs/`, `docs/research/`,
  `docs/strategy/` — cross-module decisions and research; see "Where a
  decision belongs" above before adding here
