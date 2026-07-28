# Contributing to Quad

Thanks for your interest in contributing! Quad is an open-source project, and contributions of all kinds are welcome.

## Ways to contribute

- **Host adapters** — new Git-host integrations behind the `pkg/adapter` interface (GitLab and beyond).
- **Registry & federation layer** — the object catalog, the `register` CLI, and deployment/identity adapters (Coolify, Keycloak) as this workstream lands.
- **Grading images & helpers** — prebuilt, pinned language images and build helpers for the sandboxed runner.
- **Core & dashboard** — the Go control plane and the React/TypeScript instructor and student UIs.
- **Documentation** — setup, self-hosting, privacy, and assignment-authoring guides.
- **Testing & triage** — reproducing issues, writing tests, improving determinism, and reviewing pull requests.

If you're not sure where to start, open an issue describing what you'd like to work on, or look for issues labeled `good first issue`.

## Before you start

- For anything beyond a small fix, **open an issue first** so we can agree on the approach. This matters especially for changes to the host-adapter or grading-spec contracts, the data model, or anything touching privacy or the project's non-negotiables.
- Be aware of the project's permanent refusals (see the README's "What Quad will not do"). Contributions that add surveillance features, ranked leaderboards, mandatory hosted dependencies, or authoritative AI grading are out of scope by design.

## Developer Certificate of Origin (DCO)

Quad uses the **Developer Certificate of Origin (DCO)** rather than a contributor license agreement. The DCO is a lightweight statement that you have the right to submit your contribution under the project's license. You certify it by adding a `Signed-off-by` line to each commit:

```
Signed-off-by: Your Name <you@example.com>
```

Add it automatically with `git commit -s`. By signing off, you agree to the terms of the DCO (https://developercertificate.org/).

> **Inbound = outbound.** Your contribution is licensed under the license of the directory it touches (see *Licensing of contributions* below). If and when the project establishes a neutral nonprofit steward, it may adopt a contributor agreement; any such change will be announced in advance. See [`GOVERNANCE.md`](GOVERNANCE.md).

## Licensing of contributions

Quad uses a split license, and **which license applies depends on the directory**:

| Path | License |
|------|---------|
| `cmd/`, `internal/` — the control plane | AGPL-3.0-or-later |
| `pkg/adapter`, `pkg/workspace`, `pkg/tutor`, `pkg/gradingspec` — the interoperability primitives | Apache-2.0 |

Please don't copy AGPL-licensed code into the Apache-licensed `pkg/...` seams. If you're unsure where new code belongs, ask in your issue or pull request.

## Development setup

```sh
git clone <repo-url>
cd quad
quad doctor      # verify your environment
# build, test, and local-instance instructions live in docs/
```

## Pull request process

1. Branch from `main`, make your change, and add or update tests.
2. Ensure the test suite and CI pass — **including the grading conformance and determinism checks** (a grader must produce the same result when run twice; a flaky grader is a trust bug).
3. Sign off your commits (DCO, above).
4. Open a pull request describing the change and linking the issue. Keep PRs focused and reasonably small.
5. A maintainer will review. Routine changes merge by lazy consensus; substantive ones follow the process in [`GOVERNANCE.md`](GOVERNANCE.md).

## Reporting security issues

Quad runs untrusted student code, so security matters. **Please do not report security vulnerabilities in public issues.** Instead, follow the responsible-disclosure process in [`SECURITY.md`](SECURITY.md) (or email the security contact listed there). We will acknowledge your report and work with you on a fix and a disclosure timeline.

## Code of conduct

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
