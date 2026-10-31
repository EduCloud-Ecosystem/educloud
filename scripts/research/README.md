# Offline RQ2A model-input export

Change/checkpoint, October 31, 2026. Checkout:
`/Users/gregchism/dev/.educloud-worktrees/educloud-rq2a-model-inputs`, branch
`codex/rq2a-model-inputs`, base `5c0092a81e65f25c84e0b390c4f48b5e814a3e6f`.
The additive implementation was transferred onto the current remote main;
unrelated primary-checkout changes and frozen inputs remain untouched. The
exporter, tests, this record and its documentation-index link form the change.

## Purpose and reuse

The corrected v2 human-review builder includes authored candidate responses and
rubric anchors. It must not be used to construct model inputs. This new stdlib
tool implements a separate explicit projection; it neither imports nor executes
the existing builder. Frozen case packs, review views and educator instruments
remain unchanged and outside Git.

The CLI accepts exactly the pack and controls whose SHA-256 values are compiled
into `rq2a_model_inputs.py`. There is no pin override. Each input is limited to
256 KiB, opened without following symlinks (including path ancestors), and
checked as a stable regular file. Duplicate JSON keys, nonfinite numbers and
malformed or non-synthetic/open-execution state refuse admission. This is not a
generic importer for private or new synthetic datasets.

## Export contract

Each object in `model-contexts.json` has only:

- `trusted_policy`: version, allowed/forbidden assistance, help mode, AI enabled,
  grade-write authority and the explicit minimal disclosure rule.
- `untrusted_task`: instructions, a selected fictional codebook and selected
  record/roster/reading fields. No computed reference answers.
- `untrusted_learner_input`: request and supplied evidence. Embedded instructions
  remain data; they cannot change the trusted policy.

Course, assignment and policy bindings are checked internally. Case/control,
pair/site/reviewer identifiers, source metadata, rubric, proposed labels,
assertions and authored or alternative responses do not enter these objects.
`serialize_model_context()` rejects envelopes and extra nested fields; it is not
a semantic privacy filter. The CLI pins establish text provenance. Pure
in-memory projection explicitly reports `UNVERIFIED_PURE_PROJECTION` with null
source hashes; only the pinned CLI path reports `PINNED_BYTES_VERIFIED`.

No-AI C05 and ungranted cross-course C06 requests emit no model context.
Canonical complete-context bytes deduplicate the C10 and C11 counterparts.
All 15 source candidates remain in `private-provenance.json`: 12 unique request
contexts, three blocked source candidates (two unique blocked requests), 12
eligible source mappings and ten emitted contexts, clustered by three tasks.
Source mappings are not extra model attempts. Provenance contains context
indices/digests, source hashes and gate reasons separately from model content.

All runtime/private-data authorization flags remain false, allowance null and
attempts/results empty. Gating is an offline decision, not evidence of actual
service isolation, dispatch or model behavior. The supplied evidence is authored
prose; this does not create an unseen or naturalistic evaluation set.

## Use and output custody

Run from the checkout with Python 3.9+ on a POSIX host supporting `O_NOFOLLOW` and
directory file descriptors:

```sh
python3 scripts/research/rq2a_model_inputs.py \
  --pack /absolute/path/to/restricted-reference/rq2a-case-pack-v2.json \
  --controls /absolute/path/to/restricted-reference/paired-compliant-controls.json \
  --output /absolute/path/to/a-new-private-directory
```

The parent directory must already exist and must not contain symlink ancestors.
The output must be new and outside the source directory (outside the whole
packet when its inputs are in `restricted-reference`). Existing outputs, even
partial ones, are never overwritten. Directory mode is 0700; files are 0600.

`STARTED.json` precedes output. Success writes `COMPLETE.json` with output hashes.
A write/fsync failure retains partial files and attempts `FAILED.json`; it never
deletes evidence or retries into that directory. **FAILED dominates COMPLETE**
if a final directory fsync fails after COMPLETE was written. A usable export
requires a successful CLI return, valid COMPLETE, matching output hashes and no
FAILED marker. Missing completion is incomplete even if failure recording also
fails. This is not an all-copy retention/deletion or crash-recovery guarantee.

Do not send the provenance, markers, review packet or a containing envelope to a
model. This change has no model/provider client, prompt runner, application or
runtime integration. No model use is authorized by producing these files.

## Verification and remaining work

Bounded pure offline tests:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Performed results on October 31:

- Initial 16 tests PASS in 0.034s. After strengthening the override test, adding
  nested contamination and no-AI binding controls: **17 tests PASS in 0.049s**.
  Each suite ran under a 25-second subprocess limit. No tests were skipped.
- One CLI export of the approved pinned sources: **PASS**, 0.098s enclosing tool
  wall time, under a 25-second subprocess limit. Counts matched 15/12/3/2/12/10;
  zero actual model responses. Verified output modes 0700/0600.
- Output retained at
  `/Users/gregchism/.codex/operations/rq2a-model-input-export-20261031-protocolreview`.
  Model-context file SHA-256:
  `46dd1574e546dc9415ef4d9d72bcdf9b60f2735adfb3a5e0b37aefee265f5a89`.
  Provenance SHA-256:
  `f4e38028691f6f33f83661756f5d68596b4e36d94f35e651a0956b859fcfb1ca`.
- Exporter source SHA-256:
  `fb94df14d94159d2464ab161695b544c68d0caf4b3e97efe343483a96c7b8e48`.
  Tests SHA-256:
  `a3fbd2f13ed73d51f32866a0f1cf4ea67f6fc4db723b6ed8e6e6c59c5876435b`.
- Parent verification after transfer onto current main: **17 tests PASS in
  0.042s**, under a 25-second limit; output hashes, counts and private modes
  independently rechecked without another model-input export.

Tests use tiny invented fixtures rather than adding source case content to Git.
They check hidden-marker exclusion, exact serialization, full-context dedup,
strict types/bindings, disabled/missing-grant paths, pins, nonregular/symlink/
oversized inputs, private exclusive outputs and retained partial failures.
Filesystem writer tests mock source admission explicitly; they are not extra
pinned CLI exports or evidence of real-data readiness.

Application/J2/runtime tests, benchmarks, inference/provider calls, educator
annotation, private-data access and institutional submission: **NOT RUN**.
Educator acceptance, model behavior, operational custody and any later execution
remain unresolved. Independent source review and a reviewable pull request
precede merge. A later model adapter must submit only one validated context,
retain per-task dependence and repeat authorization checks in its own scope;
this export does not activate it. This README is the bounded change record.
