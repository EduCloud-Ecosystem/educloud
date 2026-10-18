# Local Kubernetes foundation

This offline tool prepares two synthetic namespaces for an operator-owned
OrbStack evaluation. It does not contact or change a cluster, move containers,
read credentials, or execute a workload. The accepted Docker backend remains
separate. See the [contract](../../docs/specs/local-kubernetes-evaluation.md).

Generate into a **new** directory. Supply your trusted private kubeconfig path,
the observed literal local endpoint, a fresh evaluation ID and an already
reviewed immutable image. The image appears only in a nonlaunchable review
envelope; it is not inspected or pulled. Example arguments below are illustrative,
not a resource selection or an image qualification:

```sh
python3 tools/local-kubernetes/evaluate.py render \
  --evaluation-id local-eval-001 \
  --server https://127.0.0.1:26443 \
  --kubeconfig /absolute/private/orbstack-kubeconfig \
  --pss-version v1.36 --architecture arm64 \
  --image example.invalid/review-only@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
  --output /absolute/new/evaluation-directory
```

Retain the returned manifest digest separately, then validate the bundle:

```sh
python3 tools/local-kubernetes/evaluate.py validate \
  --bundle /absolute/new/evaluation-directory \
  --expected-manifest-sha256 RETURNED_TRUSTED_DIGEST
```

`OFFLINE PASS` means the files match this generator's contract. It does not mean
the API accepted them or any isolation/resource/cleanup gate passed. Run tests
without a cluster:

```sh
python3 -m unittest discover -s tools/local-kubernetes -p 'test_*.py' -v
python3 -O -m unittest discover -s tools/local-kubernetes -p 'test_*.py' -v
```

## Host-owner verification

1. Verify `orbstack`, the explicit loopback endpoint and trusted kubeconfig refer
   to the intended existing local cluster. The tool never switches context.
   Kubeconfig authentication plugins/proxies remain the operator's trust boundary;
   a loopback proxy could point elsewhere. Do not disable TLS validation.
2. Validate the bundle against the digest retained at render. Read the JSON and
   `operator-plan.json`; execute only its individual argv arrays from the bundle
   directory. Never apply the entire directory or extract/submit the pod review.
   Dry-run each namespace, create it, dry-run its policy List and create that
   List, in order. A fresh namespace is required. Stop on existing objects or
   any failure; a partially created List is not safe to blindly retry.
3. Retain exact returned UIDs, resource specs, quota status and failures. Inspect
   the namespace's restricted labels and effective worker permissions. The
   impersonated permission check includes service-account groups; denied
   impersonation is NOT RUN, not evidence of denied worker access. Investigate
   any inherited API permissions before future workload evaluation.
4. Keep all workload gates closed. The quota allows zero pods (including retained
   terminal pod objects), controllers, PVCs, services and secrets. It allows the
   default plus named service account and the namespace's system root-CA ConfigMap.
   Those counts are metadata limits, not full cluster/storage/compute bounds.
   The policy is default-deny **intent**; Flannel/network enforcement remains
   UNKNOWN until independently qualified. No cluster-wide CNI/RBAC change is
   provided. No new Service or public endpoint is created.
5. Record infrastructure-only PASS/FAIL/NOT RUN observations separately. The
   generated manifest always remains the original offline record; do not edit it
   to claim runtime success. Inspect exact ownership/UIDs and all resource kinds,
   foreign objects and retained storage before any operator-owned retirement.
   No delete command or automatic cleanup is generated.

The wrapped pod design adds a scheduling gate and intentionally has no executable
handoff. Outfitter must own admission, per-attempt reservations and cleanup before
any future workload path can be added. Network, PID/output bounds, deadline
failure, image/platform availability, late effects and retained resource costs
remain unqualified. Neither a suspended/gated pod nor a namespace quota replaces
Outfitter accounting. No application database, shared SQLite, PVC or application
replica is proposed. The previous four-attempt v4 allowance remains exhausted.

Current disposition: **foundation preparation only; defer workload adoption**.
No purchase or subscription is needed to render/check this package. Host overhead,
available capacity, isolation and operational maintenance have not been measured.

The [offline evidence](../../docs/research/evidence/2026-10-18-local-kubernetes/README.md)
retains the initial alias-policy test failure and corrected checks.
