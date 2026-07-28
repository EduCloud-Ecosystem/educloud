# Quad

> **Quad** *(working name)* — an open-source platform for distributing, collecting, and auto-grading coding assignments backed by Git repositories. The GitHub Classroom workflow, rebuilt to be **host-agnostic, privacy-minimal, and self-hostable**.

<!-- badges: license · build · docs — add when available -->

## Why Quad

GitHub Classroom is being decommissioned — sign-ups are already disabled, with full shutdown on **August 28, 2026** and final data deletion on September 4. The successors split into thin GitHub-only clones and closed, hosted commercial products. None of them is open-source *and* works against self-hosted Git *and* stores almost no student data *and* can be run by the institution itself.

That combination is the point. After being burned by platform risk, educators need a tool they can **trust**: one that runs on infrastructure they control, keeps no student PII, and locks them into nothing.

## Principles

- **The Git host is a pluggable adapter.** Everything host-specific lives behind one interface. Ships with GitHub and Forgejo/Gitea; GitLab is additive, not a rewrite.
- **Privacy by architecture, not by policy.** The control plane stores Git usernames, not student identities. Real names and SIS IDs never reach the server; the durable identity anchor is the host's numeric user id.
- **Self-hostable first.** The common case is one binary on an embedded store — no external services required. Postgres is for scale, not a prerequisite for trying it.
- **Portable autograding.** Grading is a host-neutral spec run in our own sandboxed runners — not locked to any CI provider.
- **Interoperable, no lock-in.** CSV roster import/export, full data export, a documented data model, an open adapter SDK, and a clean SQLite → Postgres path.

## Status

Quad is in active development.

- **Done — Control plane + GitHub adapter.** The full vertical slice (OAuth join → roster → repo provisioning from a template → sandboxed grading) works end-to-end.
- **Done — Forgejo/Gitea adapter.** Shipped and validated against a self-hosted instance, proving the host-agnostic thesis end-to-end.
- **Next — GitLab adapter.**
- **In progress — Student feedback loop, webhook-triggered grading, and a one-command importer for existing GitHub Classroom courses.**
- **In design — Registry & federation layer** (catalog + `register` CLI + Coolify deployment adapter + Keycloak identity), a parallel workstream that never gates the core.

See [`docs/`](docs/) for the full roadmap.

## How it works

A Go control plane owns the data model and orchestration; thin per-host **adapters** talk to GitHub, Forgejo/Gitea (and soon GitLab); a durable, rate-limit-aware **queue** provisions repositories at class scale; and untrusted student code is graded in **ephemeral, sandboxed containers**. A React/TypeScript dashboard serves instructors and students. Storage is embedded SQLite by default, Postgres at scale.

The project is organized around four stable, openly licensed seams — `pkg/adapter`, `pkg/workspace`, `pkg/tutor`, `pkg/gradingspec` — each with plural implementations behind it.

**Registry & federation layer (in design).** A parallel workstream adds a lightweight, self-hostable **Registry** — a catalog of courses, projects, datasets, and teaching artifacts, with browse/search and a `register` CLI — federated to existing open-source infrastructure rather than rebuilding it: **Coolify** for deployment, **Keycloak** for identity. It composes with the core through a thin seam, follows the same privacy rules (metadata and Git usernames, never student PII), and never gates a release.

## Quick start

```sh
quad doctor      # preflight your environment
quad up          # bring up a local instance (one binary, durable by default)
```

Full setup and self-hosting guides live in [`docs/`](docs/).

## Privacy

Quad is built so that the server **cannot** become a student-records system. It stores Git usernames keyed to the host's numeric user id; it does not store names, SIS identifiers, or plaintext email. Self-hosting keeps every record on infrastructure the institution already stewards. A data inventory generated from the schema lives in [`docs/privacy`](docs/privacy).

## What Quad will not do

Some refusals are permanent, because trust is the product:

- No proctoring, keystroke logging, or webcam monitoring.
- No student-vs-student leaderboards or ranked cohort comparisons.
- No instructor surveillance dashboard by default — instructor views are class-level aggregates.
- No AI as the final word on a contested or consequential grade.
- No required cloud account or mandatory hosted dependency.

## License

Quad uses a deliberate split:

- **AGPL-3.0-or-later** for the control plane (`cmd/`, `internal/`).
- **Apache-2.0** for the interoperability primitives (`pkg/adapter`, `pkg/workspace`, `pkg/tutor`, `pkg/gradingspec`) — so others can build adapters and integrations without friction.

See [`LICENSE`](LICENSE) and the per-directory notes in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Governance & sustainability

Quad is an independent open-source project on a deliberate path to a sustainable, neutrally governed ecosystem — not a single-vendor or single-institution tool. Project copyright is held independently of any university; the project is (or is becoming) fiscally hosted by a 501(c)(3) open-source sponsor, with grant support for development, community, and a shared, no-cost compute commons for autograding. See [`GOVERNANCE.md`](GOVERNANCE.md).

## Get involved

Contributions of all kinds are welcome — new host adapters, language grading images, docs, testing, and triage. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

## Acknowledgments

*Affiliations, funders, and the project's managing-organization home to be listed here.*
