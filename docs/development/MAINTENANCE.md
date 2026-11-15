# Maintaining the pilot reliably

The same [protocol](PILOT_PROTOCOL_V1.md) applies to educloud, belay-classroom,
Cairn, Waypoint, Portage and Outfitter. Different languages retain their actual
component tests; sameness means common acceptance rules, not replacing all suites
with a superficial shared command. Original Belay and private deployments are
outside this pilot protocol rollout.

## Installed controls

Each pilot repository has a root AGENTS entry, a byte-identical protocol copy,
a component-specific `.github/educloud/component.json`, a stdlib verifier and a
read-only `Pilot protocol / pilot-protocol` workflow. The verifier detects policy
copy drift, missing guidance and missing declared verification workflows. It does
not prove those workflows passed or validate their internal test quality.

Change the canonical protocol in educloud, record its digest/version and submit
reviewed updates to the component copies. Preserve stricter local guidance and
actual license boundaries. Required runtime CI, conformance and end-to-end tests
remain independent. Automated advisory findings are triaged by exploitability,
functional impact and evidence, not by counts.

## Central status maintenance

`pilot/components.json` is the public repository/workflow allowlist.
`pilot/readiness.json` records reviewed acceptance and open gates.
`pilot/status.json` contains bounded public GitHub observations. The README table
is generated from these files; editing metadata can never open student admission.

Run `python3 tools/pilot/status.py refresh`, then `... check`. Acquisition uses
30 finite GitHub API reads (five per component), 30 seconds per request, no hidden
retries, at most 100 check runs and 50 open PRs per component. Truncated pages are
labeled. An acquisition failure preserves the previous snapshot. Only allowlisted
public repositories are read; no issues' bodies, learner records, secrets or model
endpoints are used. The GitHub CLI and Python stdlib are sufficient. Declared protocol digests are compared with the central version; missing or divergent adoption stays visible. A matching declaration still needs its component verifier to pass.

The scheduled workflow runs every six hours or on explicit dispatch, times out
in 20 minutes and serializes runs. It can propose only `README.md` and
`pilot/status.json` on a new `codex/pilot-status-*` branch. An existing maintenance
PR prevents duplicate proposals. It never updates readiness, merges, provisions,
executes models or deploys. It uses the main checkout and pinned actions; no
untrusted PR code runs with write credentials. It explicitly dispatches the
protocol check for its branch because bot-token PR events may not trigger CI.
If GitHub disallows PR creation, the job fails visibly; do not silently change
organization permissions or claim the updater works.

## Agent implementation and review

Use the change-record template and component source/CI entry points. Separate an
implementation proposal from reviewer judgment; an agent must not approve its own
patch. Give any model-assisted maintenance a finite budget and narrow permissions
before invocation. Ordinary deterministic checks run without model inference.
Retain failures, retries, resource use and reviewer/coordination effort. Do not
introduce an automatic provider fallback or relax a gate to make a report green.

Release requires evidence at the selected source/environment pins, recovery and
rollback, approved data handling and human course acceptance. See the integration
guide and readiness record. The current local instructor test is not a selected
host deployment. Required-check configuration, workflow execution and actual
readiness are reported separately in the rollout record.
