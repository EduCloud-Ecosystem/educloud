# Streaming Python/R summaries — source acceptance

October 19, 2026. Waypoint #54 supplies separately identified, disabled streaming
Python/R scientific candidates and an independently authored checker. This is
bounded source/test preparation for A2/A3, not an upload, execution adapter,
actual measurement, trusted cleanup or participant-pilot qualification.

Reviewed head `5aede6e464f0079fd6e9ffd6e40207d0bbd4a9f3` in
[Waypoint #54](https://github.com/EduCloud-Ecosystem/waypoint/pull/54) merged as
`a3c2104e4f01af1a59e9b244452d6109086f1a00`; both trees equal
`5c5ffbcb0bacae751280baedbc873e656955b3e1`. Workload, checker, tests,
fixtures and candidate catalog bytes match locally tested `bd484845`; only the
CI dependency setup and narrative differ among those original paths.

The [evidence index](evidence/2026-10-19-streaming-summary-source/acceptance.json)
binds immutable component sources, original failures, local controls and hosted
artifacts. Protected archive hashes do not imply public download availability,
compiler attestation or qualified deployment resources.

## Delivered boundary

The explicit `summary-fixed6-csv` version 1 profile uses the existing
`summary-python` and `summary-r` manifest families, with new candidate environment
and code identities. Its registry validates exact source bytes without importing
or executing them. Ordinary recipes, environment catalog, AS1, v1/v2 validators,
fixtures, approved previews and dispatch defaults retain their original bytes.
No Store, Worker, provider, HTTP or execution-capability path is enabled.

The accepted scientific grammar is deliberately narrower than the general v2
5,000,000,000-byte metadata ceiling: ASCII `group,value`, no quoting or extra
columns, exact LF/CRLF termination, at most 128 groups of 64 bytes, six decimal
places and absolute value at most one trillion. At most one million 88-byte
records plus a 13-byte header imply **88,000,013 effective input bytes**. This is
a source-derived limit, not an executed million-row workload, 5 GB support,
measured RSS, throughput, available capacity or a task-memory guarantee.

Bounded reads retain group counts, sums and extrema, with no materialized value
list or spill. Python uses exact scaled integers. R uses five radix-one-million
limbs for sums and six for rounded mean numerators, with bounded exact double
intermediates. Baseline uses all rows; alternative removes one minimum and one
maximum in groups containing at least five rows. Global means weight retained
counts. Means are canonical twelve-place decimal strings with ties to even.

The checker was authored separately from the new workload implementations,
without reading, importing or copying them. The coordinator reviewed its frozen
source before integrating it. Its own bounded byte lexer, Decimal anchored sums
and Fraction interval/parity oracle compare the output against the original
sample. Self-consistency and exit zero alone cannot establish quality. The
closed report contains only schema, status and a fixed reason; interrupted or
unavailable evidence stays unknown.

Workload and checker each receive `INPUT CONDITION EXPECTED_ROWS`. The workload
may read the exact sample from stdin; the checker requires a trusted input path
and reserves stdin for bounded workload JSON. Both require the exact requested
row count through EOF, with no ignored tail or sampling/seed claim. A later
reviewed input-view policy must bind actual selection before multi-size use.
A path passed to these native offline commands does not prove owned-file identity.

The shared two-phase output allowance remains 65,536 bytes. Candidate partitions
total 62,976 bytes; the conservative 40,496-byte workload serialization bound
uses some scientifically incompatible simultaneous maxima and is not a claimed
executed dataset. Valid large forms and actual tiny commands are separate
controls. Raw groups, values, output, stderr, paths and content hashes remain
ephemeral and cannot become durable receipts, A4 evidence or A5 packet content.
All capability, runtime, cleanup and live-authorization flags remain false.

## Verification and provenance

| Evidence | Result and exact scope |
| --- | --- |
| Independent final review | **CLEAR:** root scientific/source review and separate file/evidence/CI audit. All 1,338 final bindings match Git; 901 earlier evidence files remain unchanged. |
| Local actual Python/R/checker | **PASS:** final isolated selection ran 55 methods, zero FAIL/ERROR/SKIP, in 6.948 seconds. All 1,320 complete before/after source bindings match the immutable tested tree. Small synthetic input only. |
| Exact final hosted controls | **PASS:** [39370474356](https://github.com/EduCloud-Ecosystem/waypoint/actions/runs/39370474356) ran 660 methods, 658 PASS / zero FAIL/ERROR / two inherited pure-validator SKIP in 132.038 seconds. All 55 streaming methods passed, including actual R and cross-checker commands. Subset counts overlap. |
| Hosted R dependency | **PASS:** Ubuntu 24.04.5 distro binary `r-base-core` 4.3.3-2build2 amd64, Rscript 4.3.3; package/installation and frontend hash/version artifacts retained. Preflight's candidate-runtime NOT RUN precedes the actual tests; it does not replace their evidence. |
| PDF regression | **PASS:** eleven methods without skips in 2.772 seconds, from the actual job log. No new PDF output artifact was viewed or retained. |
| Ordinary hosted Docker | **PASS:** unchanged baseline broker `54464389`, 41 HTTP / 25 recovery / 12 guard checks; two historical replays and 60 conservative CPU-seconds. Five bundle member sets/hashes and 72 ordinary source bindings verified. The original failed replay remains NOT RUN. These are older recipes, not the new execution adapter. |
| Optional source builds | **SKIPPED:** unchanged explicit gate. |
| Operational assessment / canonical runtime | **NOT RUN / OPEN:** actual resources, enforcement, measurements, cleanup and participant qualification. This canonical docs-only change has no configured umbrella CI. |

The checker originated at `1bc3f41fbae007bfda9498bf1957a984339efd7c` and was
integrated as `527ebf7afe939626b9ef32b969511b8df9d0f1b5`, with byte-identical
source and independent literal fixtures. Its separate 27-method pass and eight
actual checker commands overlap the later combined selection and are not added
to it. The full prior 605-method regression was not repeated locally; unchanged
runtime paths receive their configured hosted regression.

Native local Python 3.14.5 and R 4.6.0 records bind frontend paths, hashes and
versions. They do not attest their full transitive installations, a container
image or a deployment host. Earlier parent test processes used minimal recorded
environments with `PYTHONPATH`, without isolated mode. Only the final parent
used `-I -B` and the exact trusted-root bootstrap. All Python workload/checker
children used isolated mode; R children used `--vanilla`. Explicit environment
overrides and inherited-name boundaries remain recorded without secret values.

## Retained failures and remaining work

The original integrated 25-method run remains **FAIL**: 24 passed, one failed
method with one failed subcase. The negative fixture appended LF to a trailing
CR, producing a valid CRLF record. The test-only correction used an internal
CR and added actual valid/invalid paired CLI controls; all 28 methods passed.
Neither workload algorithm changed. Those selections overlap the final 55
methods and are not relabeled as its isolated rerun.

The first hosted run `39370145454` at `f03cc67` remains **FAIL** because R was
absent (`RSCRIPT_UNAVAILABLE`). Its controls/helper builds/PDF did not run. Its
separate ordinary Docker job passed and does not qualify the streaming candidate.
The subsequent bounded dependency repair installs only the runner distro binary
`r-base-core` package without recommended extras, with finite package operations
inside the existing ten-minute job. Package candidate/installed versions,
distro and interpreter provenance are retained; these are version provenance,
not immutable runtime attestation. No local dependency installation, new service
or source build was performed.

Exactly two original raw failure logs retain their trailing spaces: one local
unittest line and seven CI job-log lines. Scoped source/docs whitespace checks
exclude those exact immutable logs; no whole-patch whitespace PASS is claimed.
The coordinator also retained a file-audit correction: the raw final unittest
log ends in one LF after `OK`, while its first checker expected two. The actual
log hash and all 1,320 immutable source bindings were correct; no product failure
or additional test run follows from that checker error.

Next, complete the existing Outfitter execution authority's permanent slot
claims, measurement and reader/watch/collector lifecycle; then separately review
the typed Waypoint execution and actual-provenance A4/A5 integration. Streaming
source does not supply an enforced aggregate writable-storage mechanism, faithful
resource counters, actual image/code installation, random sampling or cleanup.
A 10 GB tmpfs under 1 GiB task memory remains insufficient. No new ledger,
scheduler, queue or portal is needed.

The [milestone](../strategy/researcher-instructor-pilot.md) and
[planning budget](../strategy/researcher-instructor-pilot-budget.md) still require
actual allocation/hosts/operators/window and a separately released finite native
allowance. Encryption/key custody, spool/swap/crash/backup exclusions, independent
expiry/termination/revocation/deletion under faults, second operator/machine,
accessibility and whole-service privacy remain open. Historical quota NO-GO,
fifth-headroom FAIL, exhausted v4 allowance, unresolved liabilities and disabled
source candidates remain unchanged. No purchase, live provider use, model
download, private/student data, production deployment or default routing change
is authorized. Docker/Compose on OrbStack stays baseline; K8s/PAIR remain optional.
