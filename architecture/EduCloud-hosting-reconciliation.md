# Reconciling the Hosting Platform with EduCloud

*June 2026 · reconciles Ben Markwart's "Team Application Hosting Platform" proposal with `EduCloud-registry-federation-proposal.md`*

## The two inputs

**Ben's new proposal** ("Team Application Hosting Platform") generalizes his Posit Connect work from "re-host this specific portfolio" to "stand up durable, shared hosting infrastructure with a documented onboarding path, so publishing the next app is a routine procedure rather than a project." That goal is exactly right. But the *implementation* is the same hand-rolled stack as before: one Linux server, nginx reverse proxy, Shiny Server OSS for R, a per-app systemd service (uvicorn/gunicorn) for each Python app, static files served by nginx, OIDC bolted on via oauth2-proxy, with the onboarding contract, the port registry (`PORTS.md`), and the per-app proxy blocks all maintained by hand. The proposal itself flags this and defers containers — "ShinyProxy or similar" — to a "generation two."

**Our version** says: don't rebuild solved infrastructure; federate mature OSS for hosting and build the novel **Registry** (the catalog) on top, behind thin seams, preserving self-host / privacy / no-lock-in.

**The instruction:** reconcile the two, lean on what already exists, specifically [Coolify](https://github.com/coollabsio/coolify).

## The finding

**Coolify already is the platform Ben's proposal hand-builds.** It is an open-source, **Apache-2.0**, self-hostable PaaS (Heroku/Netlify/Vercel alternative; ~56k stars, v4, single-command install) that manages applications, databases, and 280+ one-click services on your own servers over SSH — with an explicit **no-lock-in** guarantee (all configuration lives on your server; remove Coolify and your resources keep running) and a documented HTTP API. As maintained software it provides the reverse proxy, automatic TLS, per-app container deployment (from a Git repo, a Dockerfile, a compose file, or a buildpack), environment/secret management, a web UI, multi-server support, and lifecycle/teams.

So the reconciliation is straightforward and it's the one you pointed at: **adopt Coolify as the hosting engine instead of hand-rolling nginx + Shiny Server + systemd.** This isn't a rejection of Ben's proposal — it's "federate, don't rebuild" applied to it, and it delivers Ben's *own* generation-two end-state (containers, real isolation) now, at generation-one effort, without a Java gateway to run.

## What Coolify already does vs. what the proposal hand-builds

| Ben's hand-rolled platform | Coolify (adopt) |
|---|---|
| Single front door: nginx + TLS via certbot | Built-in proxy + automatic Let's Encrypt TLS |
| Per-app process management + isolation: Shiny Server supervision; one systemd unit per Python app | One **container per app**, supervised, auto-restart, resource limits (`MemoryMax`/`CPUQuota` equivalent) |
| The onboarding *contract*: self-contained dir + declared env + externalized secrets + routing/owner | A Coolify "application" *is* that contract, enforced by software: Git repo or Dockerfile + env/secrets UI + domain/path + project/team owner |
| Port registry (`PORTS.md`) + templated systemd unit + per-app nginx block | Assigned and routed automatically |
| Push-button publishing: `scp` + `restart.txt` | Git-push / webhook auto-deploy |
| Secrets in mode-600 `.env` loaded by the unit | Environment/secret management in the UI, injected at deploy |
| Lifecycle/ownership: twice-yearly manual review | Projects/teams + (with our layer) the Registry's `owner`/`status` metadata |
| Auth at the proxy: oauth2-proxy / Keycloak | Unchanged — put oauth2-proxy/Keycloak in front; this part of the proposal carries over as-is |
| "Generation two": containers via ShinyProxy, deferred | Coolify is containerized **now** |

## What carries over from Ben's work — keep all of it

The pivot keeps the engineer's instincts, which are the valuable part:

- **The onboarding contract as a concept.** It's the right mental model and it maps one-to-one onto Coolify's application model. Keep it as EduCloud's "how to publish" guide, rewritten in Coolify terms (point your repo, declare your env, set your domain and access rule, name an owner).
- **The privacy / FERPA discipline.** Localhost-only or access-gated, externalized secrets, the no-direct-download check, the data-steward sign-off as a launch gate — all still apply. Coolify deploys containers; you still gate access and externalize secrets exactly as Ben specifies.
- **Honest operations accounting and single-point-of-failure thinking.** Still true. Coolify *reduces* the per-app plumbing you maintain by hand, but you now maintain Coolify and the host — the operating commitment doesn't vanish, it moves up a layer.
- **First tenants as the proving ground.** The CALES portfolio (Shiny, Dash, static) becomes the first set of apps deployed through Coolify, validating the path. R/Shiny needs a container image, but a single templated Shiny Dockerfile covers the portfolio and then each app is just another Coolify application.

## The one nuance worth stating plainly

Ben deferred containers for three honest reasons: every developer must containerize first, Docker plus a Java gateway adds admin load, and containers cost memory per session. With Coolify: many apps (Python web, static, Node) deploy via **buildpacks with no hand-written Dockerfile**; there is **no Java gateway** — Coolify is the admin surface; and the memory cost is real but modest and is what buys the **true isolation** that resolves his own "shared-host isolation limits" risk (apps sharing one OS and R library, developers with broad shell visibility). For R/Shiny, the one-time templated Dockerfile is the only added step. Net: Coolify *lowers* the operational burden Ben was protecting against while giving him the isolation he wanted in generation two.

## The unified architecture

- **Host / deploy:** **Coolify** — the engine. (Adopt.)
- **Identity:** Keycloak / oauth2-proxy in front — Ben's Phase 7, unchanged. (Adopt.)
- **Static:** Git host → CI → static site — EduCloud's existing pattern (Coolify can also serve static). (Adopt.)
- **Catalog — the layer EduCloud actually builds:** the **EduCloud Registry**. Objects (course / project / dataset / artifact / compendium / agent) with metadata, browse + search, and a `register` CLI. Its deployment adapter is the **Coolify adapter** — the Registry drives Coolify's API to deploy an object and records the resulting URL back onto it.
- **Core:** the GHC-replacement core composes through the Registry — a graded repo or a student capstone registers as an object, and an object can be deployed via Coolify.
- **2027+ breadth:** JupyterHub (workspaces), Open OnDemand (HPC; ride MESA / Jetstream2), MinIO (storage), Harbor, OpenSearch, AI serving — integrated, never rebuilt.

## Adopt vs. build — sharpened

- **Adopt (existing OSS):** Coolify (deploy/host), Keycloak/oauth2-proxy (auth), Git hosts (already there); later JupyterHub, Open OnDemand, MinIO, Harbor, OpenSearch, AI serving.
- **Build (EduCloud's distinctive value):** the **Registry** — metadata model, browse/search, `register` CLI, and the **Coolify adapter**; the **GHC-replacement core**; and the thin glue (the onboarding guide in Coolify terms, the seam between core ↔ Registry ↔ Coolify).

The practical effect: the Fall build is *less* custom code than the hand-rolled platform, because the hosting plumbing becomes Coolify configuration rather than maintained shell/systemd/nginx. The novel engineering concentrates where EduCloud is actually differentiated — the Registry.

## Scope / Fall (shape unchanged, now concrete)

- **Fall 2026 — Markwart's workstream, parallel to the GHC core:** stand up Coolify as the deploy engine; Keycloak identity; **Registry MVP** (catalog + search + `register` CLI + the Coolify adapter); onboard the CALES portfolio as the first tenants (incl. the templated Shiny Dockerfile) as the proving ground.
- **2027+:** federation breadth.
- **Guardrails (unchanged):** integrate, don't rebuild (stay out of MESA's compute/HPC/AI-serving lane); the GHC-replacement core stays first; the Registry never gates the 1.0.

## Bottom line

Ben's goal, his onboarding contract, and his privacy discipline are right and survive intact. The implementation should be **Coolify**, not hand-rolled nginx/Shiny-Server/systemd — it is his own stated end-state, available now as Apache-2.0, no-lock-in software with an API the Registry can drive. EduCloud's distinctive build sits on top: the **Registry**. Less custom code, stronger isolation, a cleaner story.
