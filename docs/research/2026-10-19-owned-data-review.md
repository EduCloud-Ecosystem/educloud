# Disabled owned-data review checkpoint

October 19, 2026. **HOLD for a hosted portability correction and final review.**
[Outfitter #19](https://github.com/EduCloud-Ecosystem/outfitter/pull/19) is a draft,
not a merged or operationally accepted lifecycle. This records immutable
candidate `7972ce8ea0d6e369ccb41a81ce11096ad0ce0dd6`, tree
`c8631401da2d322ad614251be61c2d5fa6c564cd`, against accepted base
`de65bdab9303395226ebfb35e0e0740ab19b4d8e`.

The [implementation contract](../specs/assessment-owned-data.md) remains the
boundary. Existing journal, locks, Watch and Reap own the disabled data scope.
Fresh version-6 fixtures and positive storage/clock constructors exist only in
test code. Production prepare, ingest and seal refuse before stdin or state
access. No switch or self-reported encryption can enable them. Upload-only
sessions add no compute attempt, reservation or grant. Existing charged and
unresolved accounting remains intact. Temporary content is disconnected from
the retained study Worker, snapshots and exports.

Three independent scoped source/fixture reviews are clear at this candidate,
including 215 inventory bindings, 11 canonical fixture pairs and the built
helper hashes. That source review does not override the failed hosted run.
The [checkpoint index](evidence/2026-10-19-owned-data-review/checkpoint.json)
retains exact pins, hashes, result counts and evidence limits.

| Evidence | Observed result and limit |
| --- | --- |
| Coordinator real subprocess/CLI integration | **PASS: 82 checks in seven isolated scenarios.** Actual test-built Broker/Store/Watch helpers complete prepare, status, ingest, seal and cancel. Short/overlong bodies fail; their unchanged-generation retries receive `ASSESSMENT_STALE`, so these root probes establish stale-generation refusal rather than independently isolating the writer latch. An unrelated live watcher pipe is refused; all three production content operations refuse with stdin still open and unread. Exact synthetic bytes, journal exclusion, surviving writer tombstone and unchanged accounting are checked. This is macOS synthetic evidence. |
| Corrected local affected packages | **PASS: 123 race-test/subtest events**, command-line and complete broker packages. Their log/source hashes are verified. Other packages' prior-head results are separate. |
| Default race-runtime refusal subset | **PASS: ten test/subtest events**, overlapping the affected suite. The later transcript supplement records `GORACE` unset and the exact original invocation; the log itself does not capture the command/environment. |
| Static checks and builds | **PASS, owner-recorded** vet, formatting, whitespace and production/test-helper builds. The retrospective transcript supplement preserves original command/completion references; it does not create a contemporaneous compiler/environment attestation. |
| Additional old/new binary refusal controls | **PASS, 12 owner-recorded predicates.** The original inline checker retained state fingerprints and boolean results. Raw per-call outputs/full environment were not saved; its later verbatim source archive was not rerun. |
| Earlier complete local suite at `79cf73f` | **FAIL: 1,020 passing, two failing and two skipped test/subtest events; nine packages passed and broker failed.** The watcher-lease failure and parent remain failed evidence. Corrected affected-package results do not turn this into a passing final full run. |
| Exact-candidate hosted regression | **FAIL:** [run 39354445924](https://github.com/EduCloud-Ecosystem/outfitter/actions/runs/39354445924), 952 passing, 74 failing and two skipped test/subtest events in the race stage. The independent storage-writer job passed. Subsequent build, Docker, recovery and consumer stages were **SKIPPED**. |
| Real host, encryption and independent cleanup | **NOT RUN / OPEN.** No engine workload ran on this Mac, no provider was called and no real content was admitted. |

The hosted failures largely stop at prepare with `ASSESSMENT_DENIED`; three
watch-ready controls also fail before their intended transition. Source review
identifies a likely portability defect: the opened anonymous-pipe check assumes
a zero link count, while Linux initializes the pipe inode with one. This is
source/evidence inference, not a coordinator Linux runtime reproduction. The
sole Outfitter author must correct the opened-descriptor boundary and prove
actual Linux lifecycle success while still rejecting named/unlinked FIFOs,
wrong-direction endpoints and unrelated live pipes. Broadening the check to
accept arbitrary FIFOs or skipping the positive Linux journey is insufficient.
Merge remains held pending that correction, immutable review and configured CI.

After this checkpoint, the Outfitter owner reported a separate actual local
probe admitting an unlinked named FIFO under the same zero-link rule on Darwin.
The coordinator has not independently rerun or bound that new probe log here;
it is an attributed finding, not an additional counted coordinator failure.
The correction must positively identify the kernel pipe object on both
platforms and reject named and unlinked FIFOs, retaining all direction, identity
and pairing checks. The original 82 check labels remain unchanged; their
stale-generation retry coverage limit above is an evidence correction, not a
new product failure.

Earlier actual failures remain retained: header body read-ahead; a three-byte
maximum-encoding undercount; a missing initialized sentinel after journal loss;
stale commit-time clock/lifeline observations; main/deferred close uncertainty,
including failed uncertainty publication followed by deferred success; direct
provider effects before version refusal; watcher-lease replacement; and valid
new metadata operations migrating an old journal before refusal. Separate
corrected controls are not replacements for those failed records. The earlier
unknown-command migration expectation was a checker error: the immutable base
already migrated that path. The initial legacy build's misplaced `-C` flag is
also retained as a build invocation error, not a product defect.

The successful synthetic path always leaves upload, execution, actual-resource
acceptance and cleanup-trust flags false. Even observed test-file removal stays
`cleanup_unresolved`; it is no proof of independent deletion, access revocation
or contract closure. Unknown writer/close/ownership/publication outcomes retain
holds, and the original manifest identity, digest, per-attempt reservations and
remaining liabilities survive.

The existing Waypoint owner is implementing its approved AS1 source/test slice
in a fresh worktree: the existing scoped Store/Owner/Guard, current authorization,
bounded metadata, atomic denial hooks and production-disabled routes. Its final
peer binding and connected HTTP acceptance wait for the corrected Outfitter
revision. It cannot use the old retained-data path or invent a second ledger.
Actual host/encryption/spool policy, independent expiry/termination/revocation/
deletion, A2/A3 measurements and A6 second-operator/whole-service qualification
remain open. No cost or operational selection is needed for the current coding.
