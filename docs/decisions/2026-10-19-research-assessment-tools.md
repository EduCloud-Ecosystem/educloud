# Research assessment tools

Decision date: October 19, 2026. Adopt open execution and measurement components
behind existing EduCloud interfaces for the
[temporary assessment contract](../specs/research-assessment.md). Adoption here
means an implementation direction, not deployment or completed qualification.

## Execution and measurement

| Tool and primary source | Decision | Qualification boundary |
| --- | --- | --- |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | First optional Outfitter backend; Docker/Kubernetes lifecycle, commands, files and networking. Apache-2.0. | Dedicated disposable Linux workers with reviewed workloads. Pin revisions; qualify limits, cleanup and selected runtime before activation. The project's secure-container guide rejects gVisor plus its network-policy sidecar; do not drop network restrictions to work around this. |
| [BenchExec](https://github.com/sosy-lab/benchexec) | CPU, memory, time and subprocess measurement on Linux. Apache-2.0. | Delegated cgroups on controlled workers. Its nested-container examples are not permission to use privileged/unconfined shared-host containers. Periodic file-size checks are not hard storage quotas. |
| [ReFrame](https://github.com/reframe-hpc/reframe) | Portable benchmark definitions, sanity/performance checks and repeated comparisons. BSD-3-Clause. | Outfitter authorizes every execution; ReFrame does not own budgets or unrestricted scheduler access. Filter retained result metadata. |
| [Apptainer](https://apptainer.org/docs/user/latest/security.html) | Reviewed workloads on institutional HPC. | Default host integration does not provide the sole isolation boundary for arbitrary code. Follow the target site's execution policy. |
| [Snakemake](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html) / [Nextflow](https://docs.seqera.io/nextflow/reports) | Import established workflow definitions and measurements. | Parameters, labels, commands and reports can contain research content. Parse bounded known fields into receipts; do not persist raw reports or caches. |
| [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) / [repo2docker](https://jupyter.org/binder) | Optional interactive preparation and reproducible environments. | Keep uploads out of image builds/shared caches and qualify notebook checkpoints, access, networking and cleanup. |
| [vLLM benchmarks](https://github.com/vllm-project/vllm-bench) / [NVIDIA DCGM](https://docs.nvidia.com/datacenter/dcgm/latest/) | Inference throughput/latency/concurrency plus GPU memory/utilization. | Portage governs access/accounting. Task quality, warm/cold loading and counter availability must accompany throughput. Raw prompts/output traces are ephemeral. |
| [E2B Embed](https://github.com/e2b-dev/runtime/tree/main/embed) | Retain as alternate microVM evaluation. | Qualify host virtualization, TLS/front-door controls and disk/memory snapshot retention; do not assume GPU support or deletion from sandbox termination. |
| [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | Defer until a shared cluster is justified. | Its controller is not an isolation runtime; persistent identities, volumes and warm pools require separate retention controls. |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) | Later agent-policy candidate. | Resolve overlap with Portage, deployment maturity and telemetry before adoption. |
| [Daytona](https://github.com/daytonaio/daytona) | Exclude as the maintained open foundation. | The public repository notice states core development moved private in June 2026; historical source is not a maintained open product commitment. |

Use existing [Galaxy job metrics](https://docs.galaxyproject.org/en/master/admin/job_metrics.html),
[CyVerse VICE](https://docs.cyverse.org/deployment/06-applications/vice/) and
[Open OnDemand](https://www.openondemand.org/) through institutional adapters.
Galaxy's environment metrics can capture sensitive variables; restrict collectors.
VICE's Data Store mounts/staging require a specific temporary-only mode. Existing
portal deployment alone is not evidence of the assessment deletion contract.

## Slack findings and adjacent work

| Candidate | Incorporated scope |
| --- | --- |
| [ScrubData](https://github.com/justinkay/scrubdata) | Borrow inspectable transformation-history concepts. Defer source-code reuse until licensing is clear. Store reviewed method identifiers, not transformation outputs containing uploaded data. |
| [Lite-Harness](https://github.com/LiteLLM-Labs/lite-harness) and [AnyJev](https://github.com/nokia-applied-research/AnyJev) | Optional bounded agent/classification comparison fixtures after the core suite. Measure task quality and resource use; confidence is not calibration. No replacement of Portage routing/accounting. |
| [Agentic Identity Broker](https://github.com/zalando-incubator/agentic-identity-broker) | Evaluate user consent and scoped delegation before external-tool access. No generic agent-held institution-wide credentials. |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent) and [NDIF/NNsight](https://ndif.us/tools/) | Later scientific-tool and interpretability pilots with independently checked results and destination review. |
| [MESA DuckLake](https://github.com/idss-mesa/mesa-ducklake/blob/main/docs/dev/architecture.md) | Metadata interoperability with MESA's existing design. Do not retain temporary datasets, logs or content hashes in the catalog. |
| [CARC/VERDE discussion](https://idss-mesa.slack.com/archives/C0BQPS7FH50/p1792423085255369) and Temporal | Assess institutional ownership, existing service integration and orchestration needs before expanding hosted services. Discussion is not deployment acceptance. |
| Zensical | Preserve the bounded documentation pilot and reviewed navigation/content migration; do not convert the entire documentation estate as a prerequisite. |
| Modal | Preserve a separate synthetic comparison with explicit finite allowance and provider-specific measurements. It is an optional backend candidate, not a replacement for Ben's Docker/Jetstream2 work or proof of data-destination approval. |
| [Void](https://github.com/voidzero-dev/void) and [RRSI](https://github.com/google-research/rrsi) | Defer overlapping hosting and autonomous optimization. No self-modifying production benchmark or policy loop. |

## Selection rule

Qualify the smallest adapter that preserves existing admission, accounting,
identity and cleanup contracts. A new dependency must have an owner, pinned
version/license review, bounded execution surface and failure/deletion tests.
Measure sandbox/instrumentation overhead on the actual selected host. Product
claims or documentation examples are not local acceptance evidence.

Source review is dated October 19, 2026. Refresh licenses, runtime compatibility,
provider prices and allocation-program requirements when implementing or exporting;
never silently treat a historical comparison as current eligibility or pricing.
