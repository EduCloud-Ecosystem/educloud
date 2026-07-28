# Quad Governance

This document describes how the Quad project is governed, how decisions are made, and how the project is stewarded and sustained. It is meant to be clear to contributors, adopters, and funders alike, and it will evolve as the community grows.

## Mission

Quad exists to give educators a trustworthy, open-source way to distribute and auto-grade coding assignments — host-agnostic, privacy-minimal, and self-hostable — so that no institution has to depend on a single vendor or platform to teach with Git.

## Project maturity

Quad is an early-stage project with a working core. It is currently led by a founding maintainer, with a deliberate, documented path toward distributed governance and a neutral, sustainable home as the contributor and adopter base grows. We would rather state that trajectory honestly than overclaim a community that does not yet exist.

## Roles

**Users / adopters.** Instructors and institutions running Quad. Their feedback, bug reports, and adoption stories directly shape priorities.

**Contributors.** Anyone who submits code, adapters, grading images, documentation, tests, or triage. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Maintainers.** Contributors with sustained, high-quality involvement who have been granted review and merge rights. Maintainers review contributions, steward the roadmap, and uphold these governance and conduct norms. New maintainers are invited by existing maintainers on the basis of demonstrated, ongoing contribution.

**Founding maintainer / project lead.** During this early phase, the founding maintainer holds final decision-making authority and is responsible for establishing the managing organization described below. As the maintainer group grows, decision-making moves to the maintainer model described next, and this role's authority is explicitly designed to taper.

## How decisions are made

- **Routine changes** proceed by *lazy consensus*: a proposal or pull request that draws no sustained objection from a maintainer within a reasonable review window may be merged.
- **Substantive changes** — architecture, the host-adapter or grading-spec contracts, the data model, licensing, governance, and the project's non-negotiables — are decided by maintainer consensus, discussed in the open via issues or RFCs.
- **Disagreements** are resolved by seeking consensus first; where consensus cannot be reached during this phase, the founding maintainer decides and records the rationale. As governance matures, an explicit maintainer-vote fallback replaces that role.
- **The project's refusals** — the anti-features listed in the README (no surveillance, no ranked leaderboards, no AI-as-final-word on grades, no mandatory hosted dependency, and the rest) — are governance-level commitments, not default settings. Changing one requires the substantive-change process and a public rationale.

## Licensing and IP stewardship

- Quad is released under a split license: **AGPL-3.0-or-later** for the control plane and **Apache-2.0** for the interoperability primitives (see the README and [`CONTRIBUTING.md`](CONTRIBUTING.md)).
- **Inbound license = outbound license.** Contributions are accepted under the license of the directory they touch, certified via the Developer Certificate of Origin (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
- **Project copyright is held independently of any single university or employer.** This is intentional: it keeps Quad portable and credibly neutral, consistent with its no-lock-in thesis.
- As the project formalizes a managing organization (below), it may transfer trademark, domains, and project assets to a neutral nonprofit steward, and may at that point adopt a contributor agreement. Any such change will be announced and documented in advance.

## Sustainability and the managing-organization roadmap

Quad's goal is to become a self-sustaining open-source ecosystem with neutral governance — not a project dependent on one person or one institution. The intended path:

1. **Independent stewardship (now).** Copyright held independently; the project hosted by a 501(c)(3) open-source fiscal sponsor for tax-deductible donations and a legal home for funds, with no separate entity to operate.
2. **Grant-supported growth.** External funding — including NSF programs for open-source ecosystems (POSE) and undergraduate STEM education (IUSE) — supports development, community building, training, and adoption, administered by an academic partner institution while the project retains independent copyright.
3. **A shared compute commons.** Autograding runs on a pooled, no-cost compute allocation (with bring-your-own and donated capacity), governed so that running out of credit can never block a student's required work.
4. **A formalized managing organization.** As adoption justifies it, the project establishes its durable governance home — joining an established open-source foundation or standing up a dedicated nonprofit — funded as an explicit, planned step rather than an afterthought.

**Founding stewards.** The organizing core pairs the founder / technical lead with founding members who bring nonprofit board-governance and legal experience (B. Markwart, also principal contributor of the registry & federation layer) and nonprofit, grant-writing, and program-development experience (A. Cruze) — so the managing-organization path is led by people who have run one. Founding members' code enters the project under the same personal-time / DCO / IP-independence terms as the founder's.

## Code of conduct

Participation in the Quad community is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). Maintainers are responsible for enforcing it fairly and consistently.

## Changes to this document

This document is versioned in the repository. Substantive changes follow the substantive-change process above and are recorded in the project history.
