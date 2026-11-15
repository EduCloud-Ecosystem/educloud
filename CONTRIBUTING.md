# Contributing to EduCloud

EduCloud is the coordination, integration and shared-contract repository. Start
with the [integration guide](docs/pilot/INTEGRATION.md) and the
[pilot protocol](docs/development/PILOT_PROTOCOL_V1.md). Component application
changes belong in that component's repository, with compatible revisions recorded
here. Research and classroom experiences have separate release gates.

Use a scoped issue/spec or owner-authorized change record, a `codex/` branch,
DCO sign-off (`git commit -s`), and a reviewable pull request. Preserve existing
checkouts and unrelated edits. Describe behavior, authority, tests, failures,
recovery and remaining gates. Automated reviewers are advisory, not release owners.

The umbrella is Apache-2.0; each component retains its actual license and path
exceptions. See [LICENSING.md](LICENSING.md). Do not copy code across license
boundaries or publish learner data, credentials or private research artifacts.

For maintenance changes, run:

```sh
python3 .github/educloud/verify.py
python3 -m unittest discover -s tests/pilot -v
python3 tools/pilot/status.py check
```

The status collector uses only allowlisted public GitHub metadata. Scheduled
maintenance proposes changes for review; it never merges, deploys, runs models or
updates manual readiness. Failed collection preserves the previous snapshot.
Report security concerns privately to the repository owner; do not publish
exploit details or personal data in an issue. Public automated findings require
source-based triage before any vulnerability or compliance claim.
