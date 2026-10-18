# SPDX-License-Identifier: Apache-2.0
"""Offline contract tests. No cluster, Docker or provider calls."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
loader = importlib.util.spec_from_file_location("evaluate", HERE / "evaluate.py")
evaluation = importlib.util.module_from_spec(loader)
loader.loader.exec_module(evaluation)


def configuration():
    return {
        "evaluation_id": "offline-fixture", "context": "orbstack",
        "server": "https://127.0.0.1:26443", "kubeconfig": "/operator/private/orbstack-kubeconfig",
        "pss_version": "v1.36", "architecture": "arm64",
        "image": "example.invalid/review-only@sha256:" + "a" * 64,
    }


class FoundationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / "bundle"

    def render(self):
        return evaluation.render(configuration(), self.output)

    def test_deterministic_round_trip_no_provider_access(self):
        with patch.object(subprocess, "Popen", side_effect=AssertionError("subprocess forbidden")), patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            first = self.render()
            second = evaluation.render(configuration(), Path(self.temp.name) / "other")
            report = evaluation.validate(self.output, first["manifest_sha256"])
        self.assertEqual(first, second)
        self.assertEqual(report["artifacts_checked"], 6)
        self.assertEqual(report["runtime"], "NOT RUN")
        self.assertIs(report["workload_launch_enabled"], False)
        self.assertEqual(self.output.stat().st_mode & 0o777, 0o700)
        self.assertTrue(all(p.stat().st_mode & 0o777 == 0o600 for p in self.output.iterdir()))

    def test_two_namespaces_separate_exact_projects_and_pss(self):
        files, _ = evaluation.build(configuration())
        names = set()
        for project in ("a", "b"):
            ns = json.loads(files[f"namespace-{project}.json"])
            name = ns["metadata"]["name"]
            names.add(name)
            self.assertEqual(name, f"educloud-eval-offline-fixture-{project}")
            labels = ns["metadata"]["labels"]
            self.assertEqual(labels["evaluation.educloud.org/project"], project)
            for mode in ("enforce", "audit", "warn"):
                self.assertEqual(labels[f"pod-security.kubernetes.io/{mode}"], "restricted")
                self.assertEqual(labels[f"pod-security.kubernetes.io/{mode}-version"], "v1.36")
            policies = json.loads(files[f"policy-{project}.json"])["items"]
            self.assertTrue(all(obj["metadata"]["namespace"] == name for obj in policies))
        self.assertEqual(len(names), 2)

    def test_zero_workloads_controllers_and_storage(self):
        files, _ = evaluation.build(configuration())
        for project in ("a", "b"):
            objects = json.loads(files[f"policy-{project}.json"])["items"]
            self.assertEqual([o["kind"] for o in objects], ["ResourceQuota", "LimitRange", "ServiceAccount", "NetworkPolicy"])
            hard = objects[0]["spec"]["hard"]
            for name in ("pods", "count/pods", "count/jobs.batch", "count/cronjobs.batch",
                         "count/deployments.apps", "count/statefulsets.apps", "count/daemonsets.apps",
                         "count/replicasets.apps", "count/replicationcontrollers", "persistentvolumeclaims",
                         "requests.storage", "services", "secrets", "requests.cpu", "requests.memory"):
                self.assertEqual(hard[name], "0", name)
            self.assertEqual(hard["count/serviceaccounts"], "2")
            self.assertEqual(hard["count/configmaps"], "1")  # Namespace root CA ConfigMap.
            self.assertIs(objects[2]["automountServiceAccountToken"], False)
            self.assertEqual(objects[3]["spec"], {"podSelector": {}, "policyTypes": ["Ingress", "Egress"], "ingress": [], "egress": []})

    def test_nonlaunchable_restricted_pod_review(self):
        files, _ = evaluation.build(configuration())
        review = json.loads(files["restricted-pod.review.json"])
        self.assertNotIn("apiVersion", review)
        self.assertNotIn("kind", review)
        self.assertIs(review["launch_enabled"], False)
        self.assertEqual(review["allowed_attempts"], 0)
        self.assertIsNone(review["outfitter_reservation"])
        for pod in review["pods_for_design_review_only"]:
            spec = pod["spec"]
            self.assertEqual(spec["restartPolicy"], "Never")
            self.assertEqual(spec["schedulingGates"], [{"name": "outfitter.educloud.org/durable-admission"}])
            self.assertEqual(spec["activeDeadlineSeconds"], 30)
            self.assertEqual(spec["terminationGracePeriodSeconds"], 5)
            self.assertIs(spec["automountServiceAccountToken"], False)
            self.assertTrue(all(spec[k] is False for k in ("hostNetwork", "hostPID", "hostIPC", "enableServiceLinks")))
            self.assertIs(spec["securityContext"]["runAsNonRoot"], True)
            self.assertGreater(spec["securityContext"]["runAsUser"], 0)
            container = spec["containers"][0]
            self.assertEqual(container["imagePullPolicy"], "Never")
            self.assertIs(container["securityContext"]["readOnlyRootFilesystem"], True)
            self.assertIs(container["securityContext"]["allowPrivilegeEscalation"], False)
            self.assertEqual(container["securityContext"]["capabilities"], {"drop": ["ALL"]})
            self.assertEqual(container["resources"]["limits"], {"cpu": "1", "memory": "256Mi", "ephemeral-storage": "64Mi"})
            self.assertEqual(spec["volumes"], [{"name": "scratch", "emptyDir": {"medium": "Memory", "sizeLimit": "16Mi"}}])
            self.assertNotIn("env", container)
            self.assertNotIn("ports", container)

    def test_command_plan_is_local_explicit_and_never_launches(self):
        files, _ = evaluation.build(configuration())
        plan = json.loads(files["operator-plan.json"])
        self.assertIs(plan["execute"], False)
        self.assertEqual(len(plan["commands"]), 14)
        for command in plan["commands"]:
            argv = command["argv"]
            self.assertEqual(argv[:5], ["kubectl", "--kubeconfig=/operator/private/orbstack-kubeconfig", "--context=orbstack", "--server=https://127.0.0.1:26443", "--request-timeout=30s"])
            self.assertFalse(any(token in argv for token in ("apply", "delete", "run", "exec", "patch", "replace")))
            self.assertNotIn("restricted-pod.review.json", argv)
            if "-f" in argv:
                self.assertRegex(argv[argv.index("-f") + 1], r"^(namespace|policy)-[ab]\.json$")
            if "--list" in argv:
                self.assertIn("--as-group=system:authenticated", argv)
                self.assertIn("--as-group=system:serviceaccounts", argv)

    def test_remote_ambiguous_or_credential_endpoints_refuse(self):
        endpoints = ["http://127.0.0.1:26443", "https://cluster.example:6443", "https://k8s.orb.local:26443",
                     "https://10.0.0.1:6443", "https://0.0.0.0:26443", "https://localhost:26443",
                     "https://127.0.0.1:26443/", "https://u:p@127.0.0.1:26443",
                     "https://127.0.0.1:26443?x=1", "https://127.0.0.1:26443#x",
                     "https://127.0.0.1:00080", "https://127.0.0.1", "https://127.0.0.1:65536",
                     "https://[::ffff:127.0.0.1]:26443", "https://[::]:26443", " https://127.0.0.1:26443"]
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint), self.assertRaises(evaluation.Refusal):
                evaluation.build({**configuration(), "server": endpoint})
        evaluation.build({**configuration(), "server": "https://[::1]:26443"})

    def test_configuration_types_unknown_fields_and_pins_refuse(self):
        cases = [dict(configuration(), context="remote"), dict(configuration(), pss_version="latest"),
                 dict(configuration(), pss_version="v1.35"), dict(configuration(), architecture="any"),
                 dict(configuration(), image="python:latest"), dict(configuration(), image="sha256:" + "a" * 64),
                 dict(configuration(), kubeconfig="relative"), dict(configuration(), kubeconfig="/tmp/../kubeconfig"),
                 dict(configuration(), kubeconfig="/tmp/evil\npath"),
                 dict(configuration(), evaluation_id="a"), dict(configuration(), evaluation_id="../unsafe"),
                 dict(configuration(), execution=True)]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(evaluation.Refusal):
                evaluation.build(case)
        for key in configuration():
            for value in (True, False, None, 1, 0.0, [], {}):
                with self.subTest(key=key, value=value), self.assertRaises(evaluation.Refusal):
                    evaluation.build({**configuration(), key: value})

    def test_existing_destination_and_symlink_refuse(self):
        self.output.mkdir()
        with self.assertRaises(FileExistsError):
            self.render()
        self.assertEqual(list(self.output.iterdir()), [])
        self.output.rmdir()
        self.output.symlink_to(Path(self.temp.name), target_is_directory=True)
        with self.assertRaises(FileExistsError):
            self.render()

    def test_partial_write_cannot_publish_complete_manifest(self):
        original = evaluation.write_new
        count = 0

        def interrupted(path, data):
            nonlocal count
            count += 1
            if count == 3:
                raise OSError("injected write failure")
            original(path, data)

        with patch.object(evaluation, "write_new", side_effect=interrupted), self.assertRaises(OSError):
            self.render()
        self.assertTrue(self.output.is_dir())
        self.assertFalse((self.output / "manifest.json").exists())
        self.assertEqual(len(list(self.output.iterdir())), 2)
        with self.assertRaises(FileExistsError):
            self.render()

    def test_missing_extra_changed_and_untrusted_bundle_refuse(self):
        result = self.render()
        trusted = result["manifest_sha256"]
        with self.assertRaises(evaluation.Refusal):
            evaluation.validate(self.output, "0" * 64)
        extra = self.output / "extra.json"
        extra.write_text("{}")
        with self.assertRaises(evaluation.Refusal):
            evaluation.validate(self.output, trusted)
        extra.unlink()
        artifact = self.output / "namespace-a.json"
        original = artifact.read_bytes()
        artifact.unlink()
        with self.assertRaises(evaluation.Refusal):
            evaluation.validate(self.output, trusted)
        artifact.write_bytes(original.replace(b"restricted", b"privileged"))
        with self.assertRaises(evaluation.Refusal):
            evaluation.validate(self.output, trusted)

    def test_rehashed_manifest_cannot_enable_or_fabricate_acceptance(self):
        self.render()
        path = self.output / "manifest.json"
        original = json.loads(path.read_bytes())
        mutations = [("workload_launch_enabled", value) for value in (True, 0, "false", "UNKNOWN", None)]
        mutations += [("allowed_attempts", value) for value in (1, False, -1, 0.0, "0")]
        mutations += [("offline_contract", "FAIL"), ("network_policy_enforcement", "PASS"), ("runtime_gates", {})]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                data = evaluation.encode({**original, key: value})
                path.write_bytes(data)
                with self.assertRaises(evaluation.Refusal):
                    evaluation.validate(self.output, evaluation.digest(data))

    def test_rehashed_artifact_metadata_does_not_relax_contract(self):
        self.render()
        manifest_path = self.output / "manifest.json"
        original = json.loads(manifest_path.read_bytes())
        for artifact_name, mutate in (
            ("policy-a.json", lambda obj: obj["items"][0]["spec"]["hard"].update(pods="1")),
            ("operator-plan.json", lambda obj: obj["commands"][0]["argv"].__setitem__(2, "--context=remote")),
            ("operator-plan.json", lambda obj: obj["commands"][0]["argv"].__setitem__(4, "--request-timeout=5s")),
            ("restricted-pod.review.json", lambda obj: obj.update(launch_enabled=True)),
        ):
            with self.subTest(artifact=artifact_name):
                artifact = self.output / artifact_name
                old_data = artifact.read_bytes()
                obj = json.loads(old_data)
                mutate(obj)
                data = evaluation.encode(obj)
                artifact.write_bytes(data)
                manifest = copy.deepcopy(original)
                manifest["files"][artifact_name] = {"sha256": evaluation.digest(data), "bytes": len(data)}
                raw = evaluation.encode(manifest)
                manifest_path.write_bytes(raw)
                with self.assertRaises(evaluation.Refusal):
                    evaluation.validate(self.output, evaluation.digest(raw))
                artifact.write_bytes(old_data)

    def test_special_files_refuse_without_waiting(self):
        result = self.render()
        trusted = result["manifest_sha256"]
        for name in ("manifest.json", "policy-a.json"):
            file = self.output / name
            original = file.read_bytes()
            file.unlink()
            os.mkfifo(file)
            with self.subTest(name=name), self.assertRaises(evaluation.Refusal):
                evaluation.validate(self.output, trusted)
            file.unlink()
            file.symlink_to(Path(self.temp.name) / "absent")
            with self.assertRaises(OSError):
                evaluation.validate(self.output, trusted)
            file.unlink()
            file.write_bytes(original)
        alias = Path(self.temp.name) / "alias"
        alias.symlink_to(self.output, target_is_directory=True)
        with self.assertRaises(OSError):
            evaluation.validate(alias, trusted)

    def test_duplicate_nonfinite_and_oversized_json_refuse(self):
        for data in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":Infinity}', b'{'):
            with self.subTest(data=data), self.assertRaises(evaluation.Refusal):
                evaluation.strict_json(data)
        self.render()
        path = self.output / "manifest.json"
        data = b" " * 131073
        path.write_bytes(data)
        with self.assertRaises(evaluation.Refusal):
            evaluation.validate(self.output, evaluation.digest(data))

    def test_cli_offline_round_trip_and_no_execution_subcommand(self):
        args = [sys.executable, str(HERE / "evaluate.py"), "render", "--output", str(self.output)]
        for key, value in configuration().items():
            if key != "context":
                args += ["--" + key.replace("_", "-"), value]
        process = subprocess.run(args, capture_output=True, text=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stderr)
        report = json.loads(process.stdout)
        check = subprocess.run([sys.executable, str(HERE / "evaluate.py"), "validate", "--bundle", str(self.output), "--expected-manifest-sha256", report["manifest_sha256"]], capture_output=True, text=True, timeout=5)
        self.assertEqual(check.returncode, 0, check.stderr)
        self.assertEqual(json.loads(check.stdout)["runtime"], "NOT RUN")
        for operation in ("apply", "launch", "enable", "delete"):
            forbidden = subprocess.run([sys.executable, str(HERE / "evaluate.py"), operation], capture_output=True, text=True, timeout=5)
            self.assertEqual(forbidden.returncode, 2)


if __name__ == "__main__":
    unittest.main()
