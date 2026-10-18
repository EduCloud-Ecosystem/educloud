#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Offline, zero-workload local Kubernetes foundation renderer and checker."""
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import urlsplit

FORMAT = "educloud-local-kubernetes-foundation-v1"
LABEL = "evaluation.educloud.org"
ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "docs/specs/local-kubernetes-evaluation.md"
ARTIFACTS = (
    "namespace-a.json", "policy-a.json", "namespace-b.json", "policy-b.json",
    "restricted-pod.review.json", "operator-plan.json",
)
GATES = (
    "cluster_identity_and_capacity", "server_schema_and_admission",
    "effective_service_account_permissions", "network_policy_enforcement",
    "image_platform_and_availability", "outfitter_attempt_accounting",
    "process_output_and_lifetime_bounds", "owned_cleanup_and_late_effects",
    "storage_restore_and_retained_costs", "equivalent_python_r_workloads",
)


class Refusal(ValueError):
    pass


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise Refusal(message)


def strict_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def constant(_):
        raise Refusal("nonfinite JSON value")

    try:
        return json.loads(data, object_pairs_hook=pairs, parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise Refusal("invalid JSON") from exc


def configuration(value):
    fields = {"evaluation_id", "context", "server", "kubeconfig", "pss_version", "image", "architecture"}
    require(type(value) is dict and set(value) == fields, "exact configuration fields required")
    require(all(type(v) is str for v in value.values()), "configuration values must be strings")
    require(re.fullmatch(r"[a-z0-9][a-z0-9-]{4,22}[a-z0-9]", value["evaluation_id"]), "evaluation ID must be 6-24 lowercase DNS characters")
    require(value["context"] == "orbstack", "only the orbstack context is supported")
    require(value["pss_version"] == "v1.36", "this contract pins Pod Security v1.36")
    require(value["architecture"] in {"amd64", "arm64"}, "explicit Linux architecture required")
    image = value["image"]
    require(len(image) <= 256 and re.fullmatch(r"[a-z0-9][a-z0-9./:_-]*@sha256:[0-9a-f]{64}", image), "reviewed repository@sha256 image required")
    path = value["kubeconfig"]
    require(0 < len(path) <= 1024 and path.startswith("/") and ".." not in Path(path).parts and all(ord(c) >= 32 and ord(c) != 127 for c in path), "absolute explicit kubeconfig path required")
    endpoint = value["server"]
    require(len(endpoint) <= 100, "API endpoint too long")
    try:
        parsed = urlsplit(endpoint)
        address = ipaddress.ip_address(parsed.hostname or "")
        port = parsed.port
        host = f"[{address}]" if address.version == 6 else str(address)
        local = address.is_loopback and (address.version == 4 or str(address) == "::1")
        require(parsed.scheme == "https" and local and type(port) is int and 1 <= port <= 65535 and endpoint == f"https://{host}:{port}", "explicit HTTPS literal loopback endpoint required")
    except ValueError as exc:
        raise Refusal("explicit HTTPS literal loopback endpoint required") from exc
    return dict(value)


def metadata(config, name, project, *, namespace=None):
    result = {"name": name, "labels": {
        f"{LABEL}/id": config["evaluation_id"],
        f"{LABEL}/project": project,
        "app.kubernetes.io/managed-by": "educloud-local-evaluation",
    }}
    if namespace is not None:
        result["namespace"] = namespace
    return result


def objects(config, project):
    namespace = f"educloud-eval-{config['evaluation_id']}-{project}"
    meta = metadata(config, namespace, project)
    for mode in ("enforce", "audit", "warn"):
        meta["labels"][f"pod-security.kubernetes.io/{mode}"] = "restricted"
        meta["labels"][f"pod-security.kubernetes.io/{mode}-version"] = config["pss_version"]
    ns = {"apiVersion": "v1", "kind": "Namespace", "metadata": meta}

    def item(kind, name, api="v1", **values):
        return {"apiVersion": api, "kind": kind,
                "metadata": metadata(config, name, project, namespace=namespace), **values}

    zero = {key: "0" for key in (
        "pods", "count/pods", "requests.cpu", "requests.memory", "limits.cpu",
        "limits.memory", "requests.ephemeral-storage", "limits.ephemeral-storage",
        "persistentvolumeclaims", "requests.storage", "services", "secrets",
        "count/jobs.batch", "count/cronjobs.batch", "count/deployments.apps",
        "count/statefulsets.apps", "count/daemonsets.apps", "count/replicasets.apps",
        "count/replicationcontrollers",
    )}
    # Count the default service account as well as our explicit account.
    zero.update({"count/serviceaccounts": "2", "count/configmaps": "1",
                 "count/resourcequotas": "1", "count/limitranges": "1",
                 "count/networkpolicies.networking.k8s.io": "1"})
    resources = {"cpu": "1", "memory": "256Mi", "ephemeral-storage": "64Mi"}
    policies = {"apiVersion": "v1", "kind": "List", "items": [
        item("ResourceQuota", "disabled-workloads", spec={"hard": zero}),
        item("LimitRange", "reviewed-container-limits", spec={"limits": [{
            "type": "Container", "max": resources, "default": resources,
            "defaultRequest": resources,
        }]}),
        item("ServiceAccount", "synthetic-worker", automountServiceAccountToken=False),
        item("NetworkPolicy", "deny-all-intent", "networking.k8s.io/v1", spec={
            "podSelector": {}, "policyTypes": ["Ingress", "Egress"], "ingress": [], "egress": [],
        }),
    ]}
    pod = {"apiVersion": "v1", "kind": "Pod",
           "metadata": metadata(config, "unreserved-review-only", project, namespace=namespace),
           "spec": {
               "os": {"name": "linux"},
               "nodeSelector": {"kubernetes.io/os": "linux", "kubernetes.io/arch": config["architecture"]},
               "schedulingGates": [{"name": "outfitter.educloud.org/durable-admission"}],
               "serviceAccountName": "synthetic-worker", "automountServiceAccountToken": False,
               "enableServiceLinks": False, "restartPolicy": "Never",
               "activeDeadlineSeconds": 30, "terminationGracePeriodSeconds": 5,
               "hostNetwork": False, "hostPID": False, "hostIPC": False,
               "securityContext": {"runAsNonRoot": True, "runAsUser": 65532,
                                   "runAsGroup": 65532, "fsGroup": 65532,
                                   "seccompProfile": {"type": "RuntimeDefault"}},
               "containers": [{"name": "synthetic-worker", "image": config["image"],
                               "imagePullPolicy": "Never",
                               "command": ["/REQUIRES_OUTFITTER_REVIEWED_HANDOFF"],
                               "resources": {"requests": resources, "limits": resources},
                               "securityContext": {"allowPrivilegeEscalation": False,
                                                   "privileged": False, "readOnlyRootFilesystem": True,
                                                   "capabilities": {"drop": ["ALL"]}},
                               "volumeMounts": [{"name": "scratch", "mountPath": "/tmp"}]}],
               "volumes": [{"name": "scratch", "emptyDir": {"medium": "Memory", "sizeLimit": "16Mi"}}],
           }}
    return ns, policies, pod


def build(config):
    config = configuration(config)
    files = {}
    commands = []
    reviews = []
    prefix = ["kubectl", f"--kubeconfig={config['kubeconfig']}", "--context=orbstack",
              f"--server={config['server']}", "--request-timeout=5s"]
    for project in ("a", "b"):
        ns, policies, pod = objects(config, project)
        namespace = ns["metadata"]["name"]
        files[f"namespace-{project}.json"] = encode(ns)
        files[f"policy-{project}.json"] = encode(policies)
        reviews.append(pod)
        for name in (f"namespace-{project}.json", f"policy-{project}.json"):
            commands.append({"phase": f"dry-run {name}", "argv": prefix + ["--namespace=" + namespace, "create", "--dry-run=server", "-f", name, "-o", "json"]})
            commands.append({"phase": f"create {name} only after reviewed dry-run", "argv": prefix + ["--namespace=" + namespace, "create", "-f", name, "-o", "json"]})
        commands.append({"phase": "read exact foundation objects and UIDs", "argv": prefix + ["--namespace=" + namespace, "get", "resourcequota,limitrange,serviceaccount,networkpolicy", "-o", "json"]})
        commands.append({"phase": "read namespace UID and Pod Security labels", "argv": prefix + ["get", "namespace", namespace, "-o", "json"]})
        commands.append({"phase": "inspect effective worker permissions; forbidden impersonation is NOT RUN", "argv": prefix + ["--namespace=" + namespace, "auth", "can-i", "--list", f"--as=system:serviceaccount:{namespace}:synthetic-worker", "--as-group=system:serviceaccounts", f"--as-group=system:serviceaccounts:{namespace}", "--as-group=system:authenticated"]})
    files["restricted-pod.review.json"] = encode({
        "format": FORMAT + "-pod-review", "launch_enabled": False,
        "outfitter_reservation": None, "allowed_attempts": 0,
        "network_denial": "UNKNOWN", "pid_limit": "NOT IMPLEMENTED",
        "output_limit": "NOT IMPLEMENTED", "pods_for_design_review_only": reviews,
    })
    files["operator-plan.json"] = encode({
        "format": FORMAT + "-operator-plan", "execute": False,
        "working_directory": "reviewed bundle directory",
        "preconditions": [
            "Validate this bundle against its separately retained manifest digest.",
            "Verify the context, TLS, loopback endpoint and trusted kubeconfig identify the intended local cluster; no remote proxy/tunnel.",
            "No workload creation access, existing namespace adoption, or workload execution is allowed.",
            "Run each argv separately in order. Stop on any failure. Keep returned UIDs and failures; do not retry an uncertain create.",
            "Review the entire effective service-account permission list; no read/write grant is assumed safe.",
        ],
        "commands": commands,
        "cleanup": "No generated delete command. Inventory exact UIDs, all resource kinds, foreign objects and retained storage before operator-owned targeted retirement.",
    })
    manifest = {
        "format": FORMAT, "configuration": config,
        "generator_sha256": digest(Path(__file__).read_bytes()),
        "spec_sha256": digest(SPEC.read_bytes()),
        "files": {name: {"sha256": digest(data), "bytes": len(data)} for name, data in files.items()},
        "workload_launch_enabled": False, "allowed_attempts": 0,
        "outfitter_authority_changed": False, "v4_allowance_reused": False,
        "offline_contract": "PASS", "runtime_gates": {gate: "NOT RUN" for gate in GATES},
        "network_policy_enforcement": "UNKNOWN", "whole_store_capacity": "UNKNOWN",
        "decision": "DEFER workload adoption; foundation only",
    }
    return files, encode(manifest)


def write_new(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def render(config, output):
    files, manifest = build(config)
    output = Path(output)
    output.mkdir(mode=0o700)  # Existing/partial directories are never reused.
    for name, data in files.items():
        write_new(output / name, data)
    write_new(output / "manifest.json", manifest)  # Completeness marker last.
    return {"status": "OFFLINE PASS", "manifest_sha256": digest(manifest),
            "workload_launch_enabled": False, "runtime": "NOT RUN"}


def read_regular(directory_fd, name, limit=131072):
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory_fd)
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1 and info.st_size <= limit, "bounded regular file required")
        data = stream.read(limit + 1)
        require(len(data) <= limit, "file exceeds bound")
        return data


def validate(bundle, expected_digest):
    require(type(expected_digest) is str and re.fullmatch(r"[0-9a-f]{64}", expected_digest), "trusted SHA-256 required")
    directory_fd = os.open(bundle, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        require(set(os.listdir(directory_fd)) == set(ARTIFACTS) | {"manifest.json"}, "unexpected or missing bundle entries")
        raw = read_regular(directory_fd, "manifest.json")
        require(digest(raw) == expected_digest, "trusted manifest digest mismatch")
        manifest = strict_json(raw)
        require(type(manifest) is dict, "manifest object required")
        files, expected = build(manifest.get("configuration"))
        # Byte equality preserves booleans versus 0/1 and rejects additional fields.
        require(raw == expected, "manifest differs from the current offline contract")
        for name, expected_data in files.items():
            require(read_regular(directory_fd, name) == expected_data, f"altered artifact: {name}")
    finally:
        os.close(directory_fd)
    return {"status": "OFFLINE PASS", "manifest_sha256": expected_digest,
            "artifacts_checked": len(ARTIFACTS), "workload_launch_enabled": False,
            "runtime": "NOT RUN", "network_policy_enforcement": "UNKNOWN"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    create = commands.add_parser("render", help="write a new offline foundation bundle")
    for field in ("evaluation-id", "server", "kubeconfig", "pss-version", "image", "architecture", "output"):
        create.add_argument("--" + field, required=True)
    check = commands.add_parser("validate", help="verify exact offline contract and trusted digest")
    check.add_argument("--bundle", required=True)
    check.add_argument("--expected-manifest-sha256", required=True)
    args = vars(parser.parse_args(argv))
    try:
        if args.pop("operation") == "render":
            output = args.pop("output")
            result = render({**args, "context": "orbstack"}, output)
        else:
            result = validate(args["bundle"], args["expected_manifest_sha256"])
        print(json.dumps(result, sort_keys=True))
        return 0
    except (Refusal, OSError, RecursionError) as exc:
        print(json.dumps({"status": "REFUSED", "error": str(exc), "runtime": "NOT RUN"}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
