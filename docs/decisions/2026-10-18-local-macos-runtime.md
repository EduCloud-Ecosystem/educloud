# Local macOS runtime: OrbStack

Date: 18 October 2026. Scope: this operator's macOS development host. **Recorded
migration checks show completed engine cutover within the boundaries below.** Full
authentication workflows, logical restore and Kubernetes workloads remain NOT RUN.

OrbStack is the selected Docker-compatible engine for this host. Docker Compose
remains the application/development baseline. This host choice does not require
OrbStack on Linux, in CI or in cloud deployments, and does not change component
Docker interfaces, image/platform pins or provider admission rules. OrbStack's
[Docker documentation](https://docs.orbstack.dev/docker/), checked 18 October,
describes its Docker engine, Compose support and `orbstack` context; compatibility
documentation does not substitute for application-specific acceptance.

## Operator guidance

- Address this host with the explicit Docker context `orbstack`. Context/socket
  selection, engine settings, containers, networks and volume operations belong
  to the host owner. Do not silently fall back to another engine or change global
  contexts from a component test.
- Keep each application's existing Compose configuration and persistence model.
  An imported image or container snapshot is not proof that volumes, network
  bindings, secrets, health checks or application data are correct. Retain source
  originals and recovery evidence; later retirement is a separate host-owner
  decision.
- Keep private inventories, personal application names, host paths and credentials
  outside the repository. Publish aggregate outcomes and evidence hashes only.
- Treat unused development images as recoverable artifacts, not permanent local
  storage. On this shared engine, Kubernetes image garbage collection removed
  images during disk pressure even after an earlier image check passed. Monitor
  available space and preserve digest-identified recovery copies outside the
  managed image store. A changed garbage-collection setting is not a disk-capacity
  guarantee or permission to remove critical eviction safeguards.
- Preserve Outfitter admission, accounting, uncertainty and owned cleanup.
  Changing the host engine does not renew an execution allowance or reinterpret
  old receipts. The four-attempt v4 qualification remains exhausted; historical
  failed controls and image-promotion gates stay unchanged.

## Kubernetes stays a foundation

[EduCloud PR #33](https://github.com/EduCloud-Ecosystem/educloud/pull/33), merged as
`d713b2cc8f2cb64fc7ac7af72b979f3c644b728c`, adds offline preparation and recorded
local namespace/policy checks. The [operator evidence](../research/evidence/2026-10-18-local-kubernetes/infrastructure/README.md)
preserves the original timeouts and invalid probes alongside corrected checks.
Two namespaces/eight policy objects do not constitute an application deployment.
Workload gates remain closed, NetworkPolicy enforcement is UNKNOWN, and an
Outfitter Kubernetes execution adapter is NOT IMPLEMENTED. Keep databases and
existing apps on their current Compose path; no shared SQLite, PVC migration,
extra replicas or conversion of every app is implied.

## Recorded cutover checks

These aggregate results come from coordinating operator records on 18 October.
An independent evidence review cleared the final private records; the
documentation author did not repeat the migration checks. Private inventories and
operation identifiers are not published here. Counts describe this host at the
recorded checks; they are not new research workload attempts or a capacity grant.

| Check | Recorded result | Boundary |
| --- | --- | --- |
| Container preservation | All 51 source containers recreated; configuration comparisons PASS. | Explicit equivalence rules cover flags and Desktop display metadata. OrbStack log rotation uses `max-file=5`, `max-size=20m`. |
| Container state and health | 17 previously active containers running; 13 health checks PASS; 34 historical containers remain stopped. | The 13 health checks are a subset, not 51 application tests. |
| Pre-start volume preservation | All 57 trees (45 transferred + 12 existing), 129,395 files and 5,651,741,054 bytes passed exact file-hash comparison; all 45 transferred-volume root checks PASS. | Point-in-time preservation before destination services started; not a logical restore test. |
| Image identity after recovery | All 75 original/source image IDs and 147 ID/tag references PASS. All eight GC-deleted images recovered exactly. | Original OCI/provenance preservation is described separately below; rebuilding an approximation was not accepted. |
| Engine cutover and rollback material | Default Docker context/socket point to OrbStack. Docker Desktop is off, all source containers are stopped and source data is retained. | Later deletion or source retirement needs separate approval. Retained source data is not proof of a tested rollback. |
| Final runtime settings | Readback PASS at 19 October 00:18:19 UTC: context, socket, engine and default builder select OrbStack; Desktop autostart false; OrbStack `app.start_at_login` and `wait_for_container_stop` true. | Reboot/startup behavior NOT RUN; setting readback is not a reboot test. |
| Service smoke checks | Read-only SQL checks for both databases and HTTP checks for studio, mail, hub and gateway interfaces PASS. | Full authentication workflows and logical restore NOT RUN. |
| Existing Kubernetes foundation | Both restricted zero-pod namespaces retain their UIDs; two system Pods Ready, with four replacement system containers and four stopped predecessors retained. | No research/application Kubernetes workload was run. |

The temporary Desktop restart rewrote the Compose/Buildx plugin links. The coordinating
operator records restoration of OrbStack's bundled tools and verification of their selection:
Compose 5.5.0 and Buildx 0.37.2, with Docker CLI 29.5.3 and engine 29.8.2. These are
observed versions, not minimum versions imposed on other hosts. The final shared
stack health/port check passed while the operator held its maintenance lock;
the lock was then released.

Approximately **15 GiB free disk** was observed,
an outstanding capacity liability rather than a safe workload allowance. Monitor
space and obtain explicit approval for any cleanup of retained originals or
recovery material; this record authorizes no deletion.

## Retained failure and corrected recovery

The initial 45-image/51-snapshot mapping verification was followed by a concrete
retention failure: Kubernetes kubelet logs identified removal of eight unused
original images when disk usage reached 91%, above its 85% image-GC threshold.
That **FAIL remains a failure of image retention**, even though later recovery
passed. The coordinating operator records exact recovery of two images through source-engine
save/load, five through original BuildKit OCI graphs and one through an immutable
registry digest. All five complete OCI graphs and their original provenance
attestation hashes were preserved, using retained original full predicates rather
than a rebuild. The final identity check above is the corrected recovery PASS.
An incomplete source listing was not treated as proof of loss: direct inspection
confirmed the questioned image was present. The source engine was temporarily
restarted for image recovery only, with all source containers stopped, and was
turned off again after recovery.

The operator records changing the local image-GC high threshold to 100% and
maximum image age to zero while retaining the 5% critical-storage eviction
safeguards. After the configuration restart, two system Pods were Ready under
the same Pod UIDs with four replacement containers; the four stopped predecessor
containers were retained. This is an operator mitigation and system-component
observation, not Kubernetes workload qualification or evidence of sufficient
capacity. No general recommendation to disable eviction follows.

This documentation task has not inspected private inventories, contacted either
engine or run workloads. Full authentication, logical restore and reboot tests
remain NOT RUN. The cutover changes this host's engine only; it does not
change production, live allocations, student-data acceptance, routing, component
defaults or research promotion gates. NetworkPolicy enforcement remains UNKNOWN;
the full Outfitter Kubernetes adapter remains NOT IMPLEMENTED.

## Private evidence bindings

The private records remain outside the repository; these SHA-256 bindings
identify the reviewed records without publishing inventories or personal paths.
They do not make the private evidence publicly reproducible.

| Private record | SHA-256 |
| --- | --- |
| `startup-verified.json` | `b535b483bea926f3cc77b306c82e8422aa8249d137e9fddf47efe4f40ed1b9c8` |
| `post-start-smoke-verification.json` | `2ee8aa01fb9b78b31501c1fd154e7a4284e689926c31dab615c1ede2b0565d9b` |
| `original-orbstack-assets-verification-v2.json` | `9e28d99556f29e99edbcea8bc052862ecec35fd203db1940279b944b887f2918` |

## Licensing and spending

The coordinating operator recorded an OrbStack Pro trial with 29 days remaining on 18 October
2026. That is a dated observation, not an ongoing entitlement or a purchase.
[Official pricing](https://orbstack.dev/pricing), checked the same date, lists
Pro at **US$96 per user billed annually** (US$8/month equivalent). This is a
recurring list price, not an approved commitment or an all-inclusive quote.

[Official licensing](https://docs.orbstack.dev/licensing) distinguishes personal
noncommercial use from professional/business use, including work for nonprofit
entities; a generic educational purpose does not establish the personal-use
exception. The documentation describes a 30-day Pro trial. Before continued use
requires a paid license, confirm the operator's applicable terms, purchaser,
seat count and recurring exposure and obtain the specific spending decision.
No license or subscription purchase is recorded or authorized by this document.
