#!/usr/bin/env python3
"""Offline projection of two immutable synthetic RQ2A sources; no model runner."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import stat
import sys


PINS = {
    "pack": "5aded4180b3e6dfa440f5b6eb1b966583b0c7fba485ea71da491d5186e3ed17c",
    "controls": "02da3f8b36bc36f42d039e850f6188dc37408e00c15b88d97fa850aa9d83837a",
}
MAX_SOURCE_BYTES = 256 * 1024
VERSION = "2026-10-30-draft-2"
STATUS = "PROPOSED_UNREVIEWED_BY_EDUCATORS"
TASKS = {
    "TASK-SURVEY-SUMMARY-v1": ("SYNTH-COURSE-A", "SYNTH-ASSIGN-A1", "records"),
    "TASK-SURVEY-JOIN-v1": ("SYNTH-COURSE-A", "SYNTH-ASSIGN-A2", "join"),
    "TASK-UNITS-UNKNOWN-v1": ("SYNTH-COURSE-C", "SYNTH-ASSIGN-C1", "records"),
}
POLICIES = {"POLICY-HINTS-DISCLOSURE-v2", "POLICY-NO-AI-v2"}
ORIGINAL_IDS = {f"RQ2A-C{i:02d}" for i in range(1, 13)}
PAIRS = {f"RQ2A-C{i:02d}-COMPLIANT": f"RQ2A-C{i:02d}" for i in (6, 10, 11)}
POLICY_KEYS = {"version", "allowed", "forbidden", "help_mode", "ai_enabled", "grade_write_authority", "disclosure_rule"}
DISCLOSURE_KEYS = {"version", "trigger", "required_fields", "excluded_fields", "learner_authored_explanation", "unclear_or_missing_policy", "denied_request"}


class ExportError(ValueError):
    """Content-free error code, safe to record without echoing source data."""


def require(condition, code="invalid_source"):
    if not condition:
        raise ExportError(code)


def obj(value):
    require(type(value) is dict)
    return value


def text(value):
    require(type(value) is str and 0 < len(value) <= 8192)
    try:
        value.encode("utf-8", errors="strict")
    except UnicodeError:
        raise ExportError("invalid_unicode") from None
    return value


def strings(value):
    require(type(value) is list and len(value) <= 64)
    return [text(v) for v in value]


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False,
                      sort_keys=True, separators=(",", ":")).encode("utf-8")


def decode_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate_json_key")
            result[key] = value
        return result

    def nonfinite(_):
        raise ExportError("nonfinite_json")

    def finite_float(value):
        result = float(value)
        require(math.isfinite(result), "nonfinite_json")
        return result

    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=unique,
                          parse_constant=nonfinite, parse_float=finite_float)
    except ExportError:
        raise
    except (UnicodeError, ValueError, RecursionError, OverflowError):
        raise ExportError("malformed_json") from None


def path_parts(path):
    p = Path(path)
    require(".." not in p.parts, "parent_path_not_allowed")
    return Path(os.path.abspath(p)).parts[1:]


def open_directory(parts):
    """Walk without following any symlink, including intermediate directories."""
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts:
            new = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = new
        return fd
    except BaseException:
        os.close(fd)
        raise


def read_pinned(path, role):
    require(role in PINS, "unknown_source_role")
    parts = path_parts(path)
    require(bool(parts), "invalid_source_path")
    parent = open_directory(parts[:-1])
    try:
        fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        before = os.fstat(fd)
        require(stat.S_ISREG(before.st_mode), "source_not_regular")
        require(before.st_size <= MAX_SOURCE_BYTES, "source_too_large")
        raw = bytearray()
        while len(raw) <= MAX_SOURCE_BYTES:
            block = os.read(fd, min(65536, MAX_SOURCE_BYTES + 1 - len(raw)))
            if not block:
                break
            raw.extend(block)
        after = os.fstat(fd)
        require(len(raw) <= MAX_SOURCE_BYTES, "source_too_large")
        require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns)
                == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns),
                "source_changed_during_read")
        require(hashlib.sha256(raw).hexdigest() == PINS[role], "source_hash_mismatch")
        return decode_json(raw)
    finally:
        os.close(fd)


def project_task(source):
    source = obj(source)
    out = {"instructions": text(source["learner_instruction"]), "fictional_codebook": {}}
    for key, value in obj(source["fictional_codebook"]).items():
        if key not in {"record_key", "cohort", "value", "reading"}:
            continue
        if type(value) is dict:
            require(key == "reading" and {"unit", "missing_value_codes", "eligibility_rule"} <= value.keys())
            out["fictional_codebook"][key] = {
                k: None if value[k] is None else text(value[k])
                for k in ("unit", "missing_value_codes", "eligibility_rule") if k in value
            }
        else:
            out["fictional_codebook"][key] = text(value)
    require(bool(out["fictional_codebook"]))
    for collection, keys in (("records", {"record_key", "cohort", "value", "reading"}),
                             ("roster", {"record_key"}), ("readings", {"record_key", "reading"})):
        if collection not in source:
            continue
        rows = source[collection]
        require(type(rows) is list and 0 < len(rows) <= 16)
        out[collection] = []
        for row in rows:
            row = obj(row)
            projected = {}
            for key in keys & row.keys():
                value = row[key]
                if key in {"value", "reading"}:
                    require(value is None or type(value) is int and abs(value) <= 10**9)
                    projected[key] = value
                else:
                    projected[key] = text(value)
            required = {"record_key"} if collection == "roster" else {"record_key", "cohort", "value"} if collection == "records" and "cohort" in out["fictional_codebook"] else {"record_key", "reading"}
            require(required <= projected.keys())
            out[collection].append(projected)
    require(("records" in out and "roster" not in out and "readings" not in out)
            or ("records" not in out and {"roster", "readings"} <= out.keys()))
    return out


def project_policy(source):
    source = obj(source)
    require(type(source["ai_enabled"]) is bool and source["grade_write_authority"] is False)
    require((source["ai_enabled"] is True and source["help_mode"] == "hints_only")
            or (source["ai_enabled"] is False and source["help_mode"] == "disabled"))
    rule = obj(source["disclosure_rule"])
    return {
        "version": text(source["version"]),
        "allowed": strings(source["allowed"]), "forbidden": strings(source["forbidden"]),
        "help_mode": source["help_mode"], "ai_enabled": source["ai_enabled"],
        "grade_write_authority": False,
        "disclosure_rule": {key: strings(rule[key]) if key in {"required_fields", "excluded_fields"}
                            else text(rule[key]) for key in DISCLOSURE_KEYS},
    }


def serialize_model_context(context):
    """Validate the exact nested schema; an envelope or extra field is rejected.

    This is a serialization boundary, not a semantic privacy filter. Only the
    pinned export path establishes the approved synthetic text's provenance.
    """
    context = obj(context)
    require(set(context) == {"trusted_policy", "untrusted_task", "untrusted_learner_input"},
            "invalid_model_context")
    policy = obj(context["trusted_policy"])
    require(set(policy) == POLICY_KEYS and set(obj(policy["disclosure_rule"])) == DISCLOSURE_KEYS,
            "invalid_model_context")
    require(project_policy(policy) == policy and policy["ai_enabled"] is True,
            "invalid_model_context")
    task = obj(context["untrusted_task"])
    require(set(task) <= {"instructions", "fictional_codebook", "records", "roster", "readings"},
            "invalid_model_context")
    reconstructed = dict(task)
    reconstructed["learner_instruction"] = task["instructions"]
    require(project_task(reconstructed) == task, "invalid_model_context")
    learner = obj(context["untrusted_learner_input"])
    require(set(learner) == {"request", "supplied_evidence"}, "invalid_model_context")
    text(learner["request"])
    strings(learner["supplied_evidence"])
    return canonical(context)


def internal_context(case, task, policy_ref):
    context = obj(case["context"])
    require(context["trusted_course_id"] == task["course_id"]
            and context["trusted_assignment_id"] == task["assignment_id"], "binding_mismatch")
    expected_version = "v1-no-ai-control" if case["id"] == "RQ2A-C05" else task["version"]
    require(context["trusted_assignment_version"] == expected_version
            and context["trusted_policy_ref"] == policy_ref
            and context["policy_binding_source"] == "fabricated_trusted_assignment_configuration",
            "binding_mismatch")
    require(context["learner_role"] == "fabricated_learner"
            and context["claimed_identity_grants_access"] is False, "invalid_trusted_context")
    out = {k: context[k] for k in ("trusted_course_id", "trusted_assignment_id", "trusted_assignment_version", "trusted_policy_ref")}
    scope_keys = {"authorized_courses", "requested_course_id", "requested_role_claim", "cross_course_grant_present"}
    present = scope_keys & context.keys()
    if case["id"] in {"RQ2A-C06", "RQ2A-C06-COMPLIANT"}:
        require(present == scope_keys, "incomplete_scope_context")
    if present:
        require(present == scope_keys, "incomplete_scope_context")
        out["authorized_courses"] = strings(context["authorized_courses"])
        out["requested_course_id"] = text(context["requested_course_id"])
        out["requested_role_claim"] = text(context["requested_role_claim"])
        require(type(context["cross_course_grant_present"]) is bool)
        out["cross_course_grant_present"] = context["cross_course_grant_present"]
        require(context["trusted_course_id"] in out["authorized_courses"], "binding_mismatch")
    return out


def build_model_inputs(pack, controls):
    """Pure transformation used by tests; CLI admission additionally pins bytes."""
    pack, controls = obj(pack), obj(controls)
    require(pack["document_kind"] == "rq2a_synthetic_instructional_support_case_pack_design_only")
    require(pack["version"] == controls["version"] == VERSION
            and pack["status"] == controls["status"] == STATUS)
    require(pack["all_task_data_fabricated"] is True)
    for key in ("real_student_records_used", "nhanes_semantics_used", "mimic_used", "included_in_96_attempt_fixed6_comparison"):
        require(pack[key] is False, "not_closed_synthetic_source")
    execution = obj(pack["execution"])
    for key in ("model_services_used", "workloads_run", "app_tests_run", "browser_run", "runtime_authorized", "private_data_authorized"):
        require(execution[key] is False, "not_closed_synthetic_source")
    require(execution["operational_allowance"] is None)
    require(execution["actual_model_responses"] == [] and execution["results"] == []
            and controls["actual_model_responses"] == [] and controls["results"] == [])
    tasks, policies = obj(pack["tasks"]), obj(pack["policies"])
    require(set(tasks) == set(TASKS) and set(policies) == POLICIES)
    for name, (course, assignment, shape) in TASKS.items():
        task = obj(tasks[name])
        require(task["course_id"] == course and task["assignment_id"] == assignment
                and task["version"] == "v1", "binding_mismatch")
        require((shape == "records" and "records" in task and "roster" not in task and "readings" not in task)
                or (shape == "join" and "records" not in task and "roster" in task and "readings" in task))
    original, added = pack["cases"], controls["new_candidates"]
    require(type(original) is list and type(added) is list and len(original) == 12 and len(added) == 3)
    for case in original + added:
        obj(case)
        text(case["id"])
    require({c["id"] for c in original} == ORIGINAL_IDS and {c["id"] for c in added} == set(PAIRS))
    by_id = {c["id"]: c for c in original + added}
    unique, contexts, mappings, request_keys, blocked_keys = {}, [], [], set(), set()
    pair_signatures = {}
    for case in original + added:
        require(case["status"] == "FABRICATED_CASE_NOT_EVALUATED"
                and case["observed_outcome"] is None and case["educator_annotations"] == [])
        task_ref, policy_ref = text(case["task_ref"]), text(case["policy_ref"])
        require(task_ref in tasks and policy_ref in policies, "unknown_binding")
        expected_policy = "POLICY-NO-AI-v2" if case["id"] == "RQ2A-C05" else "POLICY-HINTS-DISCLOSURE-v2"
        require(policy_ref == expected_policy, "binding_mismatch")
        task, policy = project_task(tasks[task_ref]), project_policy(policies[policy_ref])
        require(policy["ai_enabled"] is (policy_ref != "POLICY-NO-AI-v2"), "binding_mismatch")
        scope = internal_context(case, tasks[task_ref], policy_ref)
        learner = {"request": text(case["learner_like_request"]),
                   "supplied_evidence": strings(case["evidence_supplied"])}
        signature = canonical({"task": task, "policy": policy, "scope": scope, "learner": learner})
        pair_signatures[case["id"]] = signature
        request_key = hashlib.sha256(signature).hexdigest()
        request_keys.add(request_key)
        reason = None
        if policy["ai_enabled"] is False:
            reason = "ai_disabled"
        elif "requested_course_id" in scope and (scope["cross_course_grant_present"] is not True
                or scope["requested_course_id"] not in scope["authorized_courses"]):
            reason = "cross_course_not_authorized"
        mapping = {"source_candidate_id": case["id"], "task_ref": task_ref,
                   "policy_ref": policy_ref, "request_sha256": request_key,
                   "context_index": None, "context_sha256": None,
                   "status": "blocked" if reason else "exported", "reason": reason}
        if reason:
            blocked_keys.add(request_key)
        else:
            model_context = {"trusted_policy": policy, "untrusted_task": task,
                             "untrusted_learner_input": learner}
            encoded = serialize_model_context(model_context)
            if encoded not in unique:
                unique[encoded] = len(contexts)
                contexts.append(model_context)
            mapping.update(context_index=unique[encoded], context_sha256=hashlib.sha256(encoded).hexdigest())
        mappings.append(mapping)
    for case in added:
        require(case["paired_with"] == PAIRS[case["id"]]
                and pair_signatures[case["id"]] == pair_signatures[case["paired_with"]], "pair_context_mismatch")
    provenance = {
        "schema_version": "rq2a-offline-model-input-provenance/v1", "status": "OFFLINE_SYNTHETIC_ONLY",
        "runtime_authorized": False, "private_data_authorized": False, "operational_allowance": None,
        "source_sha256": None, "source_admission": "UNVERIFIED_PURE_PROJECTION", "source_version": VERSION,
        "counts": {"source_candidates": len(mappings), "unique_requests": len(request_keys),
                   "blocked_source_candidates": sum(m["status"] == "blocked" for m in mappings),
                   "unique_blocked_requests": len(blocked_keys),
                   "eligible_source_candidates": sum(m["status"] == "exported" for m in mappings),
                   "unique_model_contexts": len(contexts), "task_fixtures": len(tasks),
                   "actual_model_responses": 0},
        "candidate_mappings": mappings, "attempts": [], "results": [],
    }
    return contexts, provenance


def write_new(fd, name, value):
    raw = canonical(value) + b"\n"
    output = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=fd)
    try:
        os.fchmod(output, 0o600)
        with os.fdopen(output, "wb", closefd=False) as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(output)
    finally:
        os.close(output)


def export(pack_path, controls_path, output_path):
    pack = read_pinned(pack_path, "pack")
    controls = read_pinned(controls_path, "controls")
    contexts, provenance = build_model_inputs(pack, controls)
    provenance.update(source_sha256=dict(PINS), source_admission="PINNED_BYTES_VERIFIED")
    require(provenance["counts"] == {
        "source_candidates": 15, "unique_requests": 12, "blocked_source_candidates": 3,
        "unique_blocked_requests": 2, "eligible_source_candidates": 12,
        "unique_model_contexts": 10, "task_fixtures": 3, "actual_model_responses": 0,
    }, "unexpected_frozen_inventory")
    parts = path_parts(output_path)
    require(bool(parts), "invalid_output_path")
    absolute_output = Path("/", *parts)
    for source in (pack_path, controls_path):
        p = Path(os.path.abspath(source))
        protected = p.parent.parent if p.parent.name == "restricted-reference" else p.parent
        require(not absolute_output.is_relative_to(protected), "output_inside_source_directory")
    parent = open_directory(parts[:-1])
    fd = None
    try:
        os.mkdir(parts[-1], 0o700, dir_fd=parent)  # Existing path, including symlink, refuses.
        fd = os.open(parts[-1], os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
        os.fchmod(fd, 0o700)
        write_new(fd, "STARTED.json", {"status": "WRITING", "runtime_authorized": False})
        # Contexts have no envelope metadata. Revalidate immediately before writing.
        for context in contexts:
            serialize_model_context(context)
        write_new(fd, "model-contexts.json", contexts)
        write_new(fd, "private-provenance.json", provenance)
        write_new(fd, "COMPLETE.json", {"status": "OFFLINE_EXPORT_COMPLETE", "counts": provenance["counts"],
                                       "model_contexts_sha256": hashlib.sha256(canonical(contexts) + b"\n").hexdigest(),
                                       "private_provenance_sha256": hashlib.sha256(canonical(provenance) + b"\n").hexdigest(),
                                       "runtime_authorized": False})
        os.fsync(fd)
        os.fsync(parent)
        return provenance["counts"]
    except Exception:
        if fd is not None:
            try:
                write_new(fd, "FAILED.json", {"status": "INCOMPLETE_DO_NOT_USE", "reason": "output_write_failed"})
                os.fsync(fd)
            except OSError:
                pass  # STARTED without COMPLETE remains a visible incomplete export.
        raise
    finally:
        if fd is not None:
            os.close(fd)
        os.close(parent)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", required=True)
    parser.add_argument("--controls", required=True)
    parser.add_argument("--output", required=True, help="New directory with an existing real parent")
    args = parser.parse_args(argv)
    try:
        counts = export(args.pack, args.controls, args.output)
    except (ExportError, OSError, KeyError, TypeError, RecursionError, ValueError):
        print("RQ2A export refused or incomplete; retain any partial directory and inspect locally.", file=sys.stderr)
        return 1
    print(json.dumps({"status": "OFFLINE_EXPORT_COMPLETE", "counts": counts, "runtime_authorized": False}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
