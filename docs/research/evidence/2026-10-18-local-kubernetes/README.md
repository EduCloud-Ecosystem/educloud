# Local Kubernetes foundation — offline evidence

Base: EduCloud `537d558e87adbe207042a10269f6b720cabfa970`. This packet qualifies
the [offline renderer](../../../../tools/local-kubernetes/README.md), not a
Kubernetes backend, host migration or cluster deployment.

`verification.json` records 15 unittest methods passing normally and under
optimized Python. These are the same controls, not 30 independent controls.
Logs retain individual test names. The tests include endpoint/pin/type refusals,
two-project separation, zero workload/controller/storage admission, exact
security settings, fixed context/server command plans, tampering including
rehashed truthy flags, special files, retained partial writes and no subprocess
or network access from the renderer/validator. CLI tests use only local Python
subprocesses. No kubectl, Docker, provider, model or cluster operation ran.

`initial-test-failure.json` is a concise ordinary implementation-test observation:
the Python version accepted a mapped-IPv6 loopback alias that this narrow contract
intended to refuse. Explicit IPv6 `::1` checking corrected it. This was not a
runtime/provider failure or research control, and transient source copies are
not archived. Previously accepted research evidence is unchanged.

`manifest.json` binds the final source and evidence bytes. This is integrity
metadata, not cryptographic signing or permission to execute. No active source,
catalog/image promotion, accepted store, provider budget or workload allowance
changed. The previous four-attempt v4 allowance remains exhausted.

All actual cluster schema/admission, RBAC, network enforcement, image availability,
resource bounds, accounting, cleanup, restore and workload comparison controls
remain **NOT RUN**. Network enforcement and whole-store capacity are **UNKNOWN**.
The host owner can independently review/render the package and observe only its
namespace/policy infrastructure with pinned local commands. Record those later
observations separately; do not relabel this offline evidence.
