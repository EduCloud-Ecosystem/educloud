# EduCloud Registry & Federation Layer

*A proposal scoped to EduCloud · Ben Markwart's principal contribution · June 2026*

> Hosting engine reconciled to **Coolify** (open-source, Apache-2.0, self-hostable PaaS). See `EduCloud-hosting-reconciliation.md` for the reconciliation with Ben's hosting-platform proposal.

## 0. What this is, and what it isn't

This is **not** a Posit Connect replacement, and it is **not** "EduCloud becomes a research cloud." It is EduCloud's **registry and federation layer**: a lightweight, self-hostable catalog of EduCloud objects, plus thin seams to mature hosting/compute systems that are already solved problems (and to MESA's infrastructure where it exists). EduCloud stays the *connective and registry* layer. It does not reimplement hosting or compute.

The pivot, stated honestly: keep the **principles** from Markwart's migration proposal — federate rather than rebuild, isolate per unit, static-is-static, privacy/FERPA gating as a launch criterion, honest accounting of cost — and keep the **Registry** as the genuine novelty. Scope the Fall build to a Registry MVP plus one deployment adapter plus Keycloak. Defer the full multi-system federation to a 2027+ roadmap. Keep all of it composable with — never a replacement for, or precondition of — the GHC-replacement core.

## 1. The gap it fills

EduCloud's core distributes and grades coursework. But coursework and research also need to be **published, discovered, reused, and connected**: dashboards, reports, apps, datasets, research compendia, courses, and eventually agents. Markwart's proposal makes the sharp observation that no single open-source system *catalogs and ties these together*. That catalog is the missing piece. The Registry is it.

## 2. Design principle: federate, don't rebuild

EduCloud already federates Git hosts behind a pluggable adapter (GitHub and Forgejo done; GitLab next). The Registry extends the **identical discipline** to deployment and compute: thin adapters to existing systems rather than reimplementations. This is the proposal's own conclusion — avoid years rebuilding solved infrastructure — turned into an architectural rule. It keeps scope bounded and, critically, it keeps EduCloud *out of MESA's lane*: where MESA provides sandboxes, compute, and identity, EduCloud rides them rather than competing.

| Capability | Federated to | Phase |
|---|---|---|
| Deployment / hosting | **Coolify** (open-source PaaS; Docker-based) | **Fall MVP** |
| Identity | Keycloak | **Fall MVP** |
| Static sites | Git host → CI → static (Quarto/MkDocs/Docusaurus) | **Fall MVP** (already EduCloud's pattern) |
| Workspaces | JupyterHub | 2027+ |
| HPC | Open OnDemand (+ MESA / Jetstream2) | 2027+ |
| Object storage | MinIO | 2027+ |
| Container registry | Harbor | 2027+ |
| Scaled search | OpenSearch | 2027+ |
| AI serving | vLLM / Ollama (+ MESA AI-Verde) | 2027+ |

EduCloud builds **none** of these. It builds the catalog and the seams.

## 3. The novel core — the EduCloud Registry

A lightweight, self-hostable catalog. Every object is a metadata record:

```
type:          course | project | dataset | artifact | compendium | agent
title:
owner:         (Git username — not PII)
organization:
description:
tags:
license:
links:         git_url, docker_image, deployed_url, dataset_path
```

Objects are browsable and searchable, and they **compose**: a "Neural Networks" course links its assignment repos, its dataset, its deployed dashboard, and (later) its AI tutor as one connected object graph. The seam into the GHC-replacement core is direct — a graded repo or a student capstone is *registered* as a shareable, discoverable object.

Principles preserved (and inherited from Markwart's runbook):

- **Self-hostable** — the Registry is a small service (EduCloud conventions: pure-Go or thin service + Postgres/SQLite), runnable by one operator.
- **Privacy-by-architecture** — metadata and Git usernames, never student PII; access-gated; no direct-download leaks. This is exactly the Phase 7/Phase 8 discipline in Markwart's proposal, generalized.
- **No lock-in** — `export` / `import`; the metadata format is an open contract.
- **Thin seams** — the Registry references deployments and datasets; it does not own them.

## 4. Identity — Keycloak

The pivot is right to replace the proposal's campus-only Shibboleth (correct for a UArizona contingency, wrong for a multi-institution commons) with **Keycloak**: local accounts, university SSO, Google/GitHub/ORCID, and partner identities in one system. It also lines up with EduCloud's federated-identity goal and with MESA's CILogon/Keycloak — another integration seam, not a rebuild.

## 5. Scope — the honest cut

**Fall 2026 — the MVP (Markwart's workstream, parallel to the GHC-replacement core):**

- Registry service: metadata model + store.
- Browse + search UI.
- A `register` CLI, with the metadata file as the contract.
- **Coolify** as the deployment engine, plus a thin **Coolify adapter** — the Registry drives Coolify's API to deploy a registered object and records its URL.
- Keycloak identity.
- The seam into the core: register a course / project / artifact.

**2027+ roadmap (federation breadth, phased — mirrors the pivot's Phases 2–4):** JupyterHub workspaces; Open OnDemand (HPC); MinIO (storage); Harbor (registry); OpenSearch (scaled search); AI serving; and the AI-agent-as-first-class-object framework.

**Deliberately out of scope:** EduCloud does not become a compute, HPC, or AI-serving platform. It integrates with those — and with MESA. Breadth is a roadmap, not a Fall promise.

## 6. Why "core feature by Fall" is real — and safe for the core

Two facts make it work without risking the migration window:

1. **It's scoped.** The Fall deliverable is a catalog service + one adapter + Keycloak — a focused build, not ten integrated systems.
2. **It's parallel.** Markwart owns the Registry while the founder finishes the GHC-replacement 1.0. The Registry composes through a thin seam; it is additive, never a precondition. The core ships first and still catches the migration window.

This is also why the pivot doesn't dilute EduCloud's identity: the GHC replacement stays the crisp, fundable core; the Registry is the ecosystem layer that *extends* it. The non-negotiable guardrail: **the Registry never gates or delays the 1.0.**

## 7. Funding fit

The Registry is precisely the kind of open interoperability primitive and ecosystem infrastructure **PESOSE** funds — an open catalog plus a federation of objects makes the ecosystem legible and reusable. It is Markwart's flagship deliverable and a concrete Track-1 ecosystem artifact. It is secondary to IUSE (judged on learning outcomes). It *strengthens* the ecosystem story rather than blurring it — provided scope stays at the registry/federation layer and does not creep into rebuilding hosting or compute.

## 8. Risks and the discipline that contains them

- **Scope creep — the dominant risk.** Bound Fall to Registry MVP + one adapter + Keycloak; everything else is roadmap. The pivot's own phasing supports this.
- **MESA / identity overlap.** Integrate, don't rebuild; ride MESA's compute, sandboxes, and identity. This sharpens the EduCloud↔MESA relationship instead of competing with it.
- **Maintainer / key-person load.** Markwart owns it; his own runbook already names single-administrator risk and mitigates it through documentation. The layer composes, it doesn't couple.
- **Displacing the core.** Hard guardrail: the Registry never delays the GHC-replacement 1.0.

## 9. What carries over from Markwart's original proposal

The engineer's instincts transfer intact: a reverse proxy as the single front door; static-is-static; per-unit isolation (now containers rather than systemd units); privacy/FERPA gating as explicit launch criteria; and honest accounting of operational cost and failure modes. The pivot keeps that discipline and swaps only the *implementation* (Shiny Server + per-app systemd → Docker/Coolify) and the *ambition* (host Shiny → host anything, plus catalog it).

## 10. Team

- **Ben Markwart** — principal contributor and owner of the Registry & federation layer; founding nonprofit member (governance/legal).
- **Contributors / advisors** — Tyson Swetnam (cyberinfrastructure and security advisory); adopting faculty across the pilot institutions; an open-source-governance advisor via the fiscal sponsor.
