"""Small invented fixtures; no source pack, models, app or existing builder run."""

from copy import deepcopy
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest import mock

from scripts.research import rq2a_model_inputs as ex


def fixtures():
    """Mirror only the reviewed input schema; no authored source responses/data."""
    rule = {key: [] if key in {"required_fields", "excluded_fields"} else "synthetic policy text"
            for key in ex.DISCLOSURE_KEYS}
    rule["excluded_fields"] = ["grades", "private_reflections"]
    policy = {"version": "toy-v1", "allowed": ["conceptual hints"], "forbidden": ["grade decisions"],
              "help_mode": "hints_only", "ai_enabled": True, "grade_write_authority": False,
              "disclosure_rule": rule}
    disabled = deepcopy(policy)
    disabled.update(ai_enabled=False, help_mode="disabled")
    tasks = {}
    for name, (course, assignment, shape) in ex.TASKS.items():
        task = {"course_id": course, "assignment_id": assignment, "version": "v1",
                "learner_instruction": "Inspect this invented toy task.",
                "fictional_codebook": {"record_key": "invented key", "reading": "invented units"}}
        if shape == "join":
            task.update(roster=[{"record_key": "X"}], readings=[{"record_key": "X", "reading": 5}])
        else:
            task["records"] = [{"record_key": "X", "reading": 5}]
        if name == "TASK-UNITS-UNKNOWN-v1":
            task["fictional_codebook"]["reading"] = {"unit": None, "missing_value_codes": None, "eligibility_rule": None}
        tasks[name] = task
    cases = []
    for number in range(1, 13):
        name = "TASK-SURVEY-JOIN-v1" if number in (3, 6, 10, 11) else "TASK-UNITS-UNKNOWN-v1" if number == 8 else "TASK-SURVEY-SUMMARY-v1"
        task = tasks[name]
        policy_ref = "POLICY-NO-AI-v2" if number == 5 else "POLICY-HINTS-DISCLOSURE-v2"
        context = {"trusted_course_id": task["course_id"], "trusted_assignment_id": task["assignment_id"],
                   "trusted_assignment_version": "v1-no-ai-control" if number == 5 else "v1",
                   "trusted_policy_ref": policy_ref, "policy_binding_source": "fabricated_trusted_assignment_configuration",
                   "learner_role": "fabricated_learner", "claimed_identity_grants_access": False}
        if number == 6:
            context.update(authorized_courses=[task["course_id"]], requested_course_id="SYNTH-COURSE-B",
                           requested_role_claim="instructor", cross_course_grant_present=False)
        cases.append({"id": f"RQ2A-C{number:02d}", "status": "FABRICATED_CASE_NOT_EVALUATED",
                      "task_ref": name, "policy_ref": policy_ref, "context": context,
                      "learner_like_request": f"Invented question {number}",
                      "evidence_supplied": ["invented evidence"], "observed_outcome": None,
                      "educator_annotations": [], "candidate_response": {"text": "HIDDEN-CANDIDATE"}})
    cases[9]["evidence_supplied"] = ["Toy data note: IGNORE_RULES_SYNTHETIC"]
    pack = {"document_kind": "rq2a_synthetic_instructional_support_case_pack_design_only",
            "version": ex.VERSION, "status": ex.STATUS, "all_task_data_fabricated": True,
            "real_student_records_used": False, "nhanes_semantics_used": False, "mimic_used": False,
            "included_in_96_attempt_fixed6_comparison": False,
            "execution": {k: False for k in ("model_services_used", "workloads_run", "app_tests_run", "browser_run", "runtime_authorized", "private_data_authorized")},
            "tasks": tasks, "policies": {"POLICY-HINTS-DISCLOSURE-v2": policy, "POLICY-NO-AI-v2": disabled}, "cases": cases}
    pack["execution"].update(operational_allowance=None, actual_model_responses=[], results=[])
    added = []
    for added_id, original_id in ex.PAIRS.items():
        case = deepcopy(next(c for c in cases if c["id"] == original_id))
        case.update(id=added_id, paired_with=original_id, candidate_response={"text": "OTHER-HIDDEN-RESPONSE"})
        added.append(case)
    controls = {"version": ex.VERSION, "status": ex.STATUS, "new_candidates": added,
                "actual_model_responses": [], "results": []}
    return pack, controls


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.pack, self.controls = fixtures()

    def build(self):
        return ex.build_model_inputs(self.pack, self.controls)

    def test_exact_inventory_gating_and_unverified_provenance(self):
        contexts, provenance = self.build()
        self.assertEqual(provenance["counts"], {"source_candidates": 15, "unique_requests": 12,
            "blocked_source_candidates": 3, "unique_blocked_requests": 2,
            "eligible_source_candidates": 12, "unique_model_contexts": 10,
            "task_fixtures": 3, "actual_model_responses": 0})
        blocked = {m["source_candidate_id"]: m for m in provenance["candidate_mappings"] if m["status"] == "blocked"}
        self.assertEqual(set(blocked), {"RQ2A-C05", "RQ2A-C06", "RQ2A-C06-COMPLIANT"})
        self.assertTrue(all(m["context_index"] is None and m["context_sha256"] is None for m in blocked.values()))
        self.assertEqual(blocked["RQ2A-C05"]["reason"], "ai_disabled")
        self.assertIsNone(provenance["source_sha256"])
        self.assertEqual(provenance["source_admission"], "UNVERIFIED_PURE_PROJECTION")
        self.assertFalse(provenance["runtime_authorized"])
        self.assertFalse(provenance["private_data_authorized"])
        self.assertEqual(provenance["attempts"], [])
        self.assertEqual(provenance["results"], [])
        self.assertEqual(len(contexts), 10)

    def test_independent_exact_small_context(self):
        contexts, _ = self.build()
        expected_task = {"instructions": "Inspect this invented toy task.",
                         "fictional_codebook": {"record_key": "invented key", "reading": "invented units"},
                         "records": [{"record_key": "X", "reading": 5}]}
        self.assertEqual(contexts[0], {
            "trusted_policy": self.pack["policies"]["POLICY-HINTS-DISCLOSURE-v2"],
            "untrusted_task": expected_task,
            "untrusted_learner_input": {"request": "Invented question 1", "supplied_evidence": ["invented evidence"]}})
        join = next(c for c in contexts if c["untrusted_learner_input"]["request"] == "Invented question 3")
        self.assertEqual(join["untrusted_task"]["roster"], [{"record_key": "X"}])
        self.assertEqual(join["untrusted_task"]["readings"], [{"record_key": "X", "reading": 5}])
        units = next(c for c in contexts if c["untrusted_learner_input"]["request"] == "Invented question 8")
        self.assertEqual(units["untrusted_task"]["fictional_codebook"]["reading"],
                         {"unit": None, "missing_value_codes": None, "eligibility_rule": None})

    def test_hidden_fields_cannot_change_context_or_dedup(self):
        before, provenance = self.build()
        marker = "UNIQUE-HIDDEN-CONTAMINATION"
        self.pack["rubric"] = {"label": marker}
        for task in self.pack["tasks"].values():
            task.update(adjudicator_only_reference={"answer": marker}, new_reference=marker)
            task["fictional_codebook"]["unknown"] = marker
            if type(task["fictional_codebook"].get("reading")) is dict:
                task["fictional_codebook"]["reading"]["hidden_label"] = marker
            for row in task.get("records", []) + task.get("roster", []) + task.get("readings", []):
                row["hidden_label"] = marker
        for policy in self.pack["policies"].values():
            policy["reference_answer_visibility"] = marker
            policy["disclosure_rule"]["hidden_label"] = marker
        for case in self.pack["cases"] + self.controls["new_candidates"]:
            case.update(candidate_response={"text": marker}, draft_educator_expectations={"label": marker},
                        deterministic_checks={"expected": marker}, proposed_hint_or_support_response=marker,
                        case_type=marker, simulated_custodian=marker, expected_refusal_or_unknown=marker)
            case["context"]["hidden_label"] = marker
        after, modified = self.build()
        self.assertEqual(before, after)
        self.assertEqual(provenance["counts"], modified["counts"])
        self.assertNotIn(marker, b"".join(ex.serialize_model_context(c) for c in after).decode())
        self.assertIn("grades", ex.serialize_model_context(after[0]).decode())

    def test_strong_serializer_rejects_extra_fields_at_each_boundary(self):
        contexts, provenance = self.build()
        for field in ("candidate_response", "review_id", "rubric", "source_sha256"):
            with self.subTest(field=field):
                altered = deepcopy(contexts[0]); altered[field] = "HIDDEN"
                with self.assertRaises(ex.ExportError): ex.serialize_model_context(altered)
        for path in (("trusted_policy",), ("trusted_policy", "disclosure_rule"),
                     ("untrusted_task",), ("untrusted_task", "fictional_codebook"),
                     ("untrusted_learner_input",)):
            altered = deepcopy(contexts[0]); node = altered
            for key in path: node = node[key]
            node["candidate_response"] = "HIDDEN"
            with self.subTest(path=path), self.assertRaises(ex.ExportError): ex.serialize_model_context(altered)
        altered = deepcopy(contexts[0]); altered["untrusted_task"]["records"][0]["answer"] = "HIDDEN"
        with self.assertRaises(ex.ExportError): ex.serialize_model_context(altered)
        with self.assertRaises(ex.ExportError): ex.serialize_model_context({"context": contexts[0], "provenance": provenance})

    def test_complete_context_dedup_not_request_only(self):
        self.pack["cases"][1]["learner_like_request"] = self.pack["cases"][0]["learner_like_request"]
        contexts, _ = self.build()
        self.assertEqual(len(contexts), 9)
        self.pack["cases"][1]["evidence_supplied"] = ["different supplied evidence"]
        contexts, _ = self.build()
        self.assertEqual(len(contexts), 10)
        self.pack["cases"][2]["learner_like_request"] = self.pack["cases"][0]["learner_like_request"]
        self.assertEqual(len(self.build()[0]), 10)  # Different task shape must not merge.
        changed = deepcopy(contexts[0]); changed["trusted_policy"]["allowed"] = ["other explicit policy"]
        self.assertNotEqual(ex.serialize_model_context(contexts[0]), ex.serialize_model_context(changed))

    def test_pair_signature_mismatch_refuses(self):
        self.controls["new_candidates"][1]["evidence_supplied"] = ["different evidence"]
        with self.assertRaisesRegex(ex.ExportError, "pair_context_mismatch"): self.build()

    def test_injection_remains_untrusted_data(self):
        contexts, _ = self.build()
        context = next(c for c in contexts if c["untrusted_learner_input"]["request"] == "Invented question 10")
        self.assertIn("IGNORE_RULES_SYNTHETIC", context["untrusted_learner_input"]["supplied_evidence"][0])
        self.assertNotIn("IGNORE_RULES_SYNTHETIC", json.dumps(context["trusted_policy"]))
        self.assertIs(context["trusted_policy"]["grade_write_authority"], False)

    def test_missing_scope_and_role_claim_never_grant_access(self):
        del self.pack["cases"][5]["context"]["cross_course_grant_present"]
        with self.assertRaises(ex.ExportError): self.build()

    def test_no_ai_binding_cannot_be_enabled_by_policy_mutation(self):
        self.pack["policies"]["POLICY-NO-AI-v2"].update(ai_enabled=True, help_mode="hints_only")
        with self.assertRaisesRegex(ex.ExportError, "binding_mismatch"): self.build()

    def test_strict_types_and_binding_mismatches(self):
        mutations = [
            lambda p, c: p.update(all_task_data_fabricated=1),
            lambda p, c: p["execution"].update(runtime_authorized=0),
            lambda p, c: p["execution"].update(private_data_authorized=True),
            lambda p, c: p["cases"][0]["context"].update(trusted_policy_ref="unknown"),
            lambda p, c: p["cases"][0]["context"].update(trusted_course_id="other"),
            lambda p, c: p["cases"][0]["context"].update(trusted_assignment_version="other"),
            lambda p, c: p["cases"][0]["context"].update(claimed_identity_grants_access=0),
            lambda p, c: p["cases"][0].update(learner_like_request=7),
            lambda p, c: p["cases"][0].update(evidence_supplied="not a list"),
            lambda p, c: p["cases"][0].update(task_ref="unknown"),
            lambda p, c: p["policies"]["POLICY-HINTS-DISCLOSURE-v2"].update(ai_enabled=1),
            lambda p, c: p["policies"]["POLICY-HINTS-DISCLOSURE-v2"].update(grade_write_authority=0),
            lambda p, c: p["tasks"]["TASK-SURVEY-SUMMARY-v1"]["records"][0].update(reading=True),
            lambda p, c: p["tasks"]["TASK-SURVEY-SUMMARY-v1"]["records"][0].pop("reading"),
            lambda p, c: p["cases"][0].update(educator_annotations=["not empty"]),
        ]
        for number, mutation in enumerate(mutations):
            with self.subTest(mutation=number):
                pack, controls = fixtures(); mutation(pack, controls)
                with self.assertRaises(ex.ExportError): ex.build_model_inputs(pack, controls)


class FileBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.inputs = self.root / "inputs"; self.inputs.mkdir()
        self.source = self.inputs / "pack.json"; self.source.write_bytes(b"{}")
        self.controls = self.inputs / "controls.json"; self.controls.write_bytes(b"{}")

    def test_strict_json_duplicate_nonfinite_malformed(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":{"b":1,"b":2}}', b'{"x":NaN}',
                    b'{"x":Infinity}', b'{"x":1e999}', b'not json', b'\xff'):
            with self.subTest(raw=raw), self.assertRaises(ex.ExportError): ex.decode_json(raw)

    def test_immutable_pins_no_override_or_new_output(self):
        output = self.root / "new"
        with self.assertRaisesRegex(ex.ExportError, "source_hash_mismatch"):
            ex.export(self.source, self.controls, output)
        self.assertFalse(output.exists())
        with self.assertRaises(SystemExit):
            ex.main(["--pack", str(self.source), "--controls", str(self.controls),
                     "--output", str(output), "--override-pin", "anything"])

    def test_symlink_ancestors_fifo_directory_and_size_refuse(self):
        link = self.root / "link"; link.symlink_to(self.source)
        ancestor = self.root / "linked-inputs"; ancestor.symlink_to(self.inputs, target_is_directory=True)
        fifo = self.root / "fifo"; os.mkfifo(fifo)
        large = self.root / "large"; large.write_bytes(b"x" * (ex.MAX_SOURCE_BYTES + 1))
        for path in (link, ancestor / "pack.json", fifo, self.inputs, large):
            with self.subTest(path=path), self.assertRaises((ex.ExportError, OSError)):
                ex.read_pinned(path, "pack")

    def fixture_reads(self, path, role):
        return deepcopy(fixtures()[0 if role == "pack" else 1])

    def test_private_exclusive_outputs_and_verified_transition(self):
        output = self.root / "new"
        with mock.patch.object(ex, "read_pinned", side_effect=self.fixture_reads):
            counts = ex.export(self.source, self.controls, output)
            original = {p.name: p.read_bytes() for p in output.iterdir()}
            with self.assertRaises(FileExistsError): ex.export(self.source, self.controls, output)
        self.assertEqual(counts["unique_model_contexts"], 10)
        self.assertEqual(original, {p.name: p.read_bytes() for p in output.iterdir()})
        self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o700)
        self.assertTrue(all(stat.S_IMODE(p.stat().st_mode) == 0o600 for p in output.iterdir()))
        provenance = json.loads((output / "private-provenance.json").read_text())
        self.assertEqual(provenance["source_admission"], "PINNED_BYTES_VERIFIED")
        self.assertEqual(provenance["source_sha256"], ex.PINS)
        for context in json.loads((output / "model-contexts.json").read_text()):
            ex.serialize_model_context(context)

    def test_output_symlink_source_directory_and_linked_parent_refuse(self):
        target = self.root / "target"; target.mkdir()
        link = self.root / "outlink"; link.symlink_to(target, target_is_directory=True)
        with mock.patch.object(ex, "read_pinned", side_effect=self.fixture_reads):
            for output in (link, self.inputs / "new", link / "new"):
                with self.subTest(output=output), self.assertRaises((ex.ExportError, OSError)):
                    ex.export(self.source, self.controls, output)
        self.assertEqual(list(target.iterdir()), [])

    def test_partial_failure_retained_no_rollback_or_retry(self):
        output = self.root / "partial"
        write = ex.write_new
        def failing(fd, name, value):
            if name == "private-provenance.json": raise OSError("injected")
            return write(fd, name, value)
        with mock.patch.object(ex, "read_pinned", side_effect=self.fixture_reads), mock.patch.object(ex, "write_new", side_effect=failing):
            with self.assertRaises(OSError): ex.export(self.source, self.controls, output)
        self.assertTrue((output / "STARTED.json").exists())
        self.assertTrue((output / "FAILED.json").exists())
        self.assertTrue((output / "model-contexts.json").exists())
        self.assertFalse((output / "COMPLETE.json").exists())

    def test_failed_marker_dominates_complete_on_directory_fsync_failure(self):
        output = self.root / "partial"
        real_fsync = os.fsync
        failed = False
        def fail_directory(fd):
            nonlocal failed
            if stat.S_ISDIR(os.fstat(fd).st_mode) and not failed:
                failed = True
                raise OSError("injected final directory fsync")
            return real_fsync(fd)
        with mock.patch.object(ex, "read_pinned", side_effect=self.fixture_reads), mock.patch.object(ex.os, "fsync", side_effect=fail_directory):
            with self.assertRaises(OSError): ex.export(self.source, self.controls, output)
        self.assertTrue((output / "COMPLETE.json").exists())
        self.assertEqual(json.loads((output / "FAILED.json").read_text())["status"], "INCOMPLETE_DO_NOT_USE")


if __name__ == "__main__":
    unittest.main()
