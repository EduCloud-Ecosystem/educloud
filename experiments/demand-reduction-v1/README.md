# E1: avoid inference before adding machines

This offline tool freezes a small paired experiment and screens imported,
content-free accounting and human review. It makes **no model, network, notebook
or cloud call**. It neither grants execution permission nor changes Portage.

The supplied 24 public/synthetic task proposals contain six course hints, six
source questions, six routine drafts and six data/code tasks. One data task is
the pinned public NHANES notebook, with a browser-versus-hosted ordinary-work
screen. A prose plan is not execution of that notebook. The task corpus and
rubrics still require independent instructor/reviewer approval.

Supported runtime: Python 3.12 or later, with only the standard library. New
Python code/tests use Apache-2.0; see [license scope](LICENSING.md) and [LICENSE](LICENSE).

## Distribution

The release artifact is an offline source/tool ZIP, with an immutable source
revision, explicit file manifest and SHA-256 checksums. It is not a hosted
application or an approved model service. From a clean committed source tree:

```sh
python3 experiments/demand-reduction-v1/release.py \
  --version v0.0.0-rc.1 --out /absolute/existing-parent/fresh-release
```

The output directory must be new. The version above is for a local trial.
From the output directory, run `shasum -a 256 -c SHA256SUMS` to verify the ZIP
and its `.spdx.json` sidecar. Extract the ZIP, keep its directory layout,
check the internal `RELEASE-MANIFEST.json`, and run the commands below from
the extracted root. The source release excludes local evidence stores,
credentials, model outputs and unrelated platform documents. Its tests
exercise the extracted tool and the expected unavailable roundtrip.
Release-candidate status does not grant endpoint permission or establish
measured performance.

### SPDX inventory

The [SPDX 2.3 JSON](https://spdx.github.io/spdx-spec/v2.3.1/) sidecar lists each
ZIP member, including the generated release manifest. It records the ZIP's
SHA-256 digest, the Git revision, file checksums, and the SPDX package
verification code. The ZIP is reproducible for a given version and revision.
The sidecar records its UTC creation time, so builds at different times can
produce distinct sidecars for the same ZIP.

Python source and tests report the Apache-2.0 identifiers present in their
headers. Package-wide licensing, file license conclusions, and unreviewed
catalog and documentation licensing use `NOASSERTION`. The SPDX document's
`CC0-1.0` data license applies to the SBOM metadata. The referenced NHANES
notebook and datasets, model services, and the operator's Python installation
are outside the ZIP inventory. E1 requires external Python 3.12+ and its standard
library. The inventory makes no assertion about the installed runtime's
dependency graph. See [license scope](LICENSING.md) for the source license.

CI validates the generated sidecar with the
[SPDX project's Python tools](https://github.com/spdx/tools-python). To repeat
validation locally, install the validator in a separate virtual environment:

```sh
python3 -m venv /absolute/path/to/spdx-validator
/absolute/path/to/spdx-validator/bin/python -m pip install spdx-tools==0.8.5
/absolute/path/to/spdx-validator/bin/pyspdxtools -i educloud-e1-v0.0.0-rc.1.spdx.json
```

Validation checks the SPDX document structure and relationships. The release
tests independently compare its inventory and hashes with the ZIP. The builder
and E1 tool use only the Python standard library.

The supplied candidate is explicitly a **draft prompt-only** comparison, with
the same facts and tutor policy in both arms. This harness does not implement
retrieval, template execution or a deterministic preprocessor. Freeze concrete
tool/material revisions and new task prompts before evaluating those changes.
The importer also supports a candidate that actually completes through ordinary
software with zero model calls. Source bundle preparation lives in Waypoint's
`course-workspace/classroom/BROWSER-BUNDLE.md` on `codex/browser-notebook-bundle-v1`.

## Prepare an unavailable experiment without spending

From this EduCloud checkout, use a fresh existing output directory:

```sh
python3 experiments/demand-reduction-v1/e1.py plan \
  --manifest experiments/demand-reduction-v1/tasks.json \
  --out /absolute/existing-directory/e1-plan.json
python3 experiments/demand-reduction-v1/e1.py template \
  --plan /absolute/existing-directory/e1-plan.json \
  --out /absolute/existing-directory/e1-results.json
python3 experiments/demand-reduction-v1/e1.py report \
  --plan /absolute/existing-directory/e1-plan.json \
  --results /absolute/existing-directory/e1-results.json \
  --out /absolute/existing-directory/e1-report.json
```

The last command writes `incomplete` and exits **1**, as intended: no endpoint,
execution permission, task review or measured results exist. Exit 0 from `plan`
means a plan was written, never permission to execute it. Exit 2 means malformed
or inconsistent input or an output already exists; no file is overwritten.
Inputs are bounded to 4 MiB and reject duplicate keys and nonfinite numbers.

The plan embeds the manifest, fixed ceilings, seed and exact 48-workflow paired
schedule. Pair order is randomized and counterbalanced (12 candidate-first,
12 baseline-first). Each task also has an ordinary alternative. SHA-256 binds
the plan and the report's imported results; these hashes are integrity checks,
not signatures or proof that observations happened.

## Interchange for an eventual authorized executor

An operator must supply separately reviewed endpoint/data permission, execution
authority and task review references, then freeze a **new** plan. Endpoint pins
identify the actual provider/model revision, tokenizer, runtime and sampling
configuration, not merely a fast/strong alias. All model-assisted workflows use
that same condition. A deterministic candidate and ordinary controls have a null
condition and zero attempts. No data/model license, campus allocation, account
creation or pooled-credit entitlement is inferred from a configured manifest.

Import the complete journal through the following contract. `template` produces
the row structure with missing values, not fabricated measurements:

- `evidence_kind`: `preparation`, `measured` or `fixture`. The empty template is
  preparation with an unobserved (`null`) actual order. Change to measured only
  when importing actual observations. Preparation/fixture evidence always prevents an
  observed screening pass, even if its invented numbers satisfy the gates.
- `capture`: separate application-attempt and external-dispatch completeness
  booleans, plus an evidence reference. Capture ordinary/hidden embedding,
  summary, title, repair and validator work too. A duplicated Belay/Portage
  record of one dispatch is one attempt, not two calls. Provider-internal retries
  may be unobservable and must not be described as independently counted.
- `actual_order`: the imported model-arm workflow order, matching the frozen
  schedule. A deviation is visible as incomplete rather than silently pooled.
- `setup`: operator/reviewer seconds, separate USD/hour rates and cost-basis
  evidence. Include preparation, analysis and unsuccessful work in staff limits.
  A zero labor rate requires a truthful explicit basis, not missing accounting.
- Each workflow records its exact identity, condition, terminal status,
  `completion_kind` (`model_assisted` or `deterministic`) and outcome evidence;
  task work-seconds including checking/correction, operator/reviewer seconds,
  `other_variable_cost_usd`, reconciled `variable_cost_usd`, human review and the
  completed artifact/output digest. Model-free candidates require their own
  deterministic completion evidence. Ordinary controls never have model attempts.
- Each attempt has a globally unique application identity, terminal outcome,
  zero/one observable external dispatch, actual **split** input/output tokens,
  actual observed/reconciled model USD, separate unresolved cost hold and evidence.
  Estimates/unknown costs have null `actual_cost_usd`; keep their estimate details
  in the referenced ledger, never add estimates or reserves to actual charges.
  Total-token-only records cannot prove the per-input/per-output ceilings.
- Reviews use an opaque reviewer ID and independent evidence, useful-completion,
  severe-regression and critical-failure judgments. Model self-grading and valid
  JSON are not substitutes. Do not label an unsuccessful terminal outcome useful.
- `ai_off_journey` binds at least one useful ordinary workflow to equal saved,
  reopened and exported artifact hashes and an observation reference. Combined
  with dispatch-capture evidence this supports a zero-call journey; hashes alone
  cannot show that an actual browser reopened or that no network call occurred.

Every reference is `{ "reference": "opaque-evidence-location", "sha256":
"64-lowercase-hex-digits" }`. This tool validates format/binding, **does not fetch,
open, authenticate or independently review referenced evidence**. Keep restricted
evidence in its authorized store. Results contain no prompts, outputs, learner
identities, credentials or private tutor text; reference hashes and opaque IDs
are sufficient. A declared public/synthetic scope still needs actual content
review. This importer cannot discover omitted attempts from a dishonest journal.

## Accounting and screening

Per-workflow compared variable cost is checked against this calculation:

```text
sum(actual observed model charges)
  + operator_seconds * operator_usd_per_hour / 3600
  + reviewer_seconds * reviewer_usd_per_hour / 3600
  + other_variable_cost_usd
```

Other variable costs include any ordinary tool/storage/compute charges once,
excluding the model and labor components already listed. Fixed service and
one-time engineering costs need separate reporting; setup staff time is retained
and counted against the staff ceiling, not allocated away into task savings.
Known unresolved holds and unknown-hold counts appear separately from actual
charges. A lost terminal response/usage remains unresolved until reconciled.

Ceilings: 48 model-arm workflows, two attempts each, 96 attempts total, 4,096
input/512 output tokens per call, four operator hours, two reviewer hours and
$10 actual model charges plus retained known liability. Denied attempts count
conservatively against the attempt limit even without an external dispatch.
This is an **offline audit of limits**, not a live admission controller. A future
executor must stop before dispatch using Portage's current admission/ledger.

A screening pass requires full evidence, no critical failure/severe regression,
at least as many useful candidate completions as baseline, a useful ordinary
zero-call save/reopen/export journey, and at least 20% lower total task time or
cost per useful completion. The other measure may increase at most 5%, an explicit
**proposed preregistered interpretation** of “no material deterioration.” Review
this margin before running; changing it requires a new version, not post-hoc
tuning. Checking/correction time and failed workflows remain included. A
zero-priced baseline cannot produce a manufactured percentage cost saving.

Known denied/unavailable/failed/timed-out/cancelled/abandoned outcomes are retained and counted as
nonuseful, with their costs and human effort. Unknown outcomes or missing usage,
review, price basis, permission/configuration or capture remain `incomplete`.
Known ceiling/policy/efficiency failures produce `screening_fail`. Reports retain
per-arm outcomes/tokens/attempts and task-level paired differences. This small
screen does not estimate campus effectiveness or statistical noninferiority.

## Existing integration boundary

Portage's observed `codex/openrouter-instructor-walkthrough-v1` at
`9298030d2aef6f011ae2b2720bca2e961bb1c866` already has finite source-fixed
synthetic guards and durable monetary liabilities. Its two tier aliases can
reach the same actual model. Do **not** widen those guards or reuse that run's
permission/budget for this corpus. Future E1 execution needs its own finite
reviewed envelope through current gateway membership, admission and accounting.
No runtime executor is supplied here.

## Verification

```sh
python3 -m unittest discover -s experiments/demand-reduction-v1 -p 'test_*.py' -v
```

The unit data exercise fabricated measurements and deliberate failures only.
They do not establish actual model quality, latency, savings or permission.
The coordinated [change record](../../docs/specs/resource-efficiency-v1.md)
records exact worktrees, checks, retained failures and remaining gates.
