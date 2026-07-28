# EduCloud — Business & Operating Plan

> **July 2026 correction.** PESOSE Track 1 is NSF 26-506, deadline **March 2,
> 2027**; September 1, 2026 references below are superseded. Module names have
> settled (Cairn/Belay/Waypoint/Portage/Outfitter) — see `SYSTEM.md`; prior
> names (Quad/Sol/Registry/Commons) appear below unrevised.

*Working draft · private planning · June 2026*
*Author: Greg Chism · Project name "EduCloud" is a working title (alternatives: Quad, Cairn)*

---

## 0. How to read this plan

You asked for a foolproof plan. No plan for a new venture is foolproof, and I won't pretend otherwise — so instead this is built to be **robust**: a low floor, a high ceiling, and few load-bearing assumptions, each named.

The design principle throughout is **decoupling**. The code, the money, the grant administration, and the home institution are deliberately separated so that any one of them can change — including your move from UArizona to Willamette — without breaking the others. That separation is what makes the plan survive contact with reality.

Two outcomes are defined up front so success isn't all-or-nothing:

- **Minimum viable success (the floor):** EduCloud is the stable, documented, self-hostable successor to GitHub Classroom, used by UArizona and a handful of other institutions, sustained by one or two grants plus fiscal-sponsor donations, maintained by you and a small community. This is a real, useful, durable project even if Willamette and the IDSS scale-up never happen.
- **Full vision (the ceiling):** a foundation-stewarded commons with an optional commercial hosting arm, anchoring Willamette's data-science program, integrated into a scaled MESA, with broad multi-institution adoption and a national workforce-development footprint.

Everything below is engineered so the floor is reached early and cheaply, and the ceiling is upside rather than a requirement.

---

## 1. Executive summary

EduCloud is an open-source, self-hostable, Git-host-agnostic platform for teaching with code: it distributes assignments to per-student repositories, collects them, and autogrades them in sandboxed containers. It is the natural successor to GitHub Classroom, which is being decommissioned on 28 August 2026 — with new sign-ups already closed — leaving every instructor and department currently dependent on it forced to migrate.

EduCloud differentiates on the things the commercial alternatives GitHub is steering users toward cannot easily match: it is free and open-source, runs on your own infrastructure (or national cyberinfrastructure), stores student usernames rather than personal data, works across GitHub, GitLab, and self-hosted Forgejo, and creates no lock-in. It doubles as the graded-assignment and assessment layer for the MESA training program, and as a CS/data-science education use-case on national cyberinfrastructure.

The plan: ship a deployable 1.0 through 2026; capture the Spring 2027 and Fall 2027 migration waves (Fall 2026 is treated as pilots only); fund the build through a diversified portfolio rather than NSF alone — Sloan (open-source-in-science philanthropy, the highest-EV near-term ask), earned revenue (GHC migration services now, a philanthropy-subsidized hosted tier on the Transfer Explorer precedent later), education philanthropy with pilot data (ECMC, Ascendium, Hewlett), and the laddered NSF strategy (ACCESS for compute, IUSE for people, PESOSE to stand up governance, IDSS via MESA for scale) as two-of-many bets plus fiscal-sponsored donations (see `EduCloud-funding-strategy.md` for the full ranked plan; federal capped at ~50% of any year once other lanes open); hold the IP in a fiscal sponsor now and a 501(c)(3) foundation later; and keep the home institution portable so flagship status can shift from UArizona to Willamette in Spring or Fall 2027 without disruption.

---

## 2. The opportunity

**A forced migration with a hard deadline.** GitHub Classroom decommissions on 28 August 2026; new classroom creation is already disabled as of May 2026; Classroom-specific data is deleted on 4 September 2026. Every department using it must choose a replacement within this cycle. This is a rare event: a large, captive, motivated user base compelled to switch on a known date.

**A real but beatable competitive field.** GitHub is directing departing users to named partner solutions (commercial autograders and classroom tools). EduCloud does not win by being first — it won't be — it wins on a value set those partners structurally can't offer: self-hostability, privacy-by-architecture, host-agnosticism, no lock-in, no per-seat cost, and the ability to run on institutional or national cyberinfrastructure. Many institutions will grab whatever is ready for Fall 2026, then re-evaluate when cost, data-privacy, and lock-in concerns surface — which is precisely the Spring/Fall 2027 window EduCloud targets.

**A captive first audience.** The MESA training program (Tiers 1–3, Educator Fellows; targeting ~500 trained across ~10 institutions) needs a graded/autograded assignment layer it does not currently have — it runs on self-paced notebooks and Carpentries workshops today. EduCloud is that layer, which means it has real users and a real deployment from day one, independent of the open-market migration.

**An equity angle that matches your background.** Self-hostability is itself an access filter, but a zero-IT path (managed/consortium hosting) plus a focus on community-college and transfer contexts turns EduCloud into a broadening-participation instrument — which strengthens every NSF narrative attached to it.

---

## 3. Product

EduCloud distributes assignments to per-student Git repositories, locks them at deadlines, and grades submissions by executing tests in ephemeral sandboxed containers. Its commitments are the product, not incidental:

- **Pluggable host adapters** — GitHub and Forgejo/Gitea working and validated end-to-end; GitLab next. The host-agnostic design is the moat the incumbents lack.
- **Privacy by architecture** — stores Git usernames, never student PII; no proctoring, no surveillance dashboards. This is both an ethical stance and a FERPA-positioning asset.
- **Self-hostable first** — embedded SQLite by default (pure-Go, zero-config), Postgres at institutional scale; one-command bring-up the target for non-experts.
- **Portable sandboxed grading** — host-neutral grading spec; documented sandbox swap (gVisor/Kata); reuses MESA's AI Sandboxes where deployed there.
- **No lock-in** — export/import of all project state; nothing proprietary in the data path.
- **Optional AI layer** — the Sol peer-tutor and AI-assisted grading sit *behind* the deterministic harness, off by default, never the final word on a grade.

**Current state:** GitHub adapter, Forgejo adapter, privacy-minimal store, provisioning queue, deadline locking, and sandboxed container runner are working. Remaining to a deployable 1.0: webhook-driven grading, GitLab adapter, an instructor/student dashboard (replacing curl/cookie workflows), a `doctor` preflight checker, one-command Docker Compose bring-up, a GitHub Classroom import path, and documentation.

**Licensing:** AGPL-3.0 control plane + Apache-2.0 interoperability primitives, contributions under DCO. (See §6 for why this combination is deliberate.)

---

## 4. Users, market, and competition

**Segments, in priority order:**

1. **MESA training cohorts** — captive, funded, your own program. First and most certain users.
2. **Privacy-/sovereignty-sensitive institutions** — universities and departments that can't or won't put student data in a commercial SaaS, or that already self-host Forgejo/GitLab. Underserved by GitHub's partners.
3. **Community colleges and transfer-heavy programs** — cost-sensitive, equity-relevant, and an NSF-favored audience; the constituency the hosted/consortium path is for.
4. **The broad GitHub Classroom exodus** — large but contested; realistically a Spring/Fall 2027 re-evaluation play, not a Fall 2026 land grab.
5. **The Carpentries / research-software-engineering community** — natural dissemination channel and contributor pool.

**Channels:** the MESA EOT program and CyVerse's ~13,000-user base; the Carpentries and RSE networks; conference presence (PEARC, SIGCSE, JupyterCon); GitHub's own community discussions where displaced users are actively seeking alternatives; lighthouse adopters producing public case studies.

**Competitive position:**

| Dimension | GitHub Classroom (retiring) | Commercial partners / Gradescope | nbgrader / Otter / INGInious | **EduCloud** |
|---|---|---|---|---|
| Status | Gone Aug 2026 | Active, paid | Active, point tools | New, building |
| Self-hostable | No | Mostly no | Yes (narrow) | **Yes, first-class** |
| Host-agnostic | GitHub-only | Varies | n/a | **GitHub/GitLab/Forgejo** |
| Privacy posture | Moderate | Variable; SaaS data | Local | **Usernames, not PII** |
| Lock-in | Moderate | High | Low | **None (export/import)** |
| Cost | Free (was) | Per-seat / license | Free | **Free OSS; pay only for hosting** |
| Runs on national CI | No | No | No | **Yes (ACCESS/CyVerse)** |

The honest read: EduCloud is not the most polished option in 2026, and won't capture instructors who need something turnkey *this* fall. Its durable advantage is the combination no commercial partner can replicate — open, self-hostable, host-agnostic, privacy-first, free — which becomes decisive as institutions hit the cost and data-governance walls of their hasty 2026 choices.

---

## 5. Business model and sustainability

EduCloud is structured as a **commons with an optional commercial arm** — the model that lets it take grants and donations as a public good while still building a path off perpetual grant dependence.

**Revenue streams, by phase:**

- **Grants (primary, near-term):** the NSF ladder in §9, administered by a university.
- **Donations and sponsorships:** via the fiscal sponsor now, the foundation later — individual, departmental, and corporate (e.g., infrastructure vendors).
- **Institutional memberships:** modest annual dues that buy roadmap input and support priority; the sustaining-member model that funds OSS foundations.
- **Earned revenue (medium-term, optional):** managed hosting for institutions that won't self-host, support/SLA tiers, migration and integration services, and paid training. Delivered through the foundation as an earned-revenue program (with unrelated-business-income-tax awareness) or, if it grows, through a PBC services arm.

**The "free to self-host, pay for convenience" line.** The software is always free and open. Revenue comes from removing the operational burden — hosting, support, integration — not from the software itself. This keeps the commons intact and the trust signal credible while still monetizing the thing institutions actually lack (capacity, not code).

**Cost structure.** People are essentially the entire cost. Compute is near-zero because it runs on ACCESS-allocated and CyVerse resources rather than commercial cloud. This is the single most important financial fact about EduCloud: a workforce-development OSS project whose marginal compute is subsidized can reach sustainability on modest revenue, because it is funding maintainers, not infrastructure.

---

## 6. Legal, IP, and governance

**The structure, in three separated layers (see §0):**

| Function | Holder (now) | Holder (durable) |
|---|---|---|
| Code ownership / stewardship | You; fiscal sponsor holds trademark | 501(c)(3) foundation |
| Grant administration | UArizona | UArizona, then Willamette (whichever is home) |
| Donations / funds | Fiscal sponsor (Open Source Collective) | Foundation (or permanent SFC membership) |
| Commercial services (optional) | — | PBC arm, licensing the name from the foundation |

**Path:** fiscal-sponsored project now → 501(c)(3) foundation as durable steward (funded by PESOSE Track 1) → optional PBC commercial arm only if a hosting/support business proves real. A PBC is explicitly **not** the primary vehicle — it forecloses most NSF funding, makes donations non-deductible, and recreates the centralization EduCloud is designed against. It earns a place only as a later services arm in the hybrid (the Mozilla Foundation/Corporation pattern).

**The gating item — the UArizona IP waiver.** Everything downstream assumes EduCloud's IP is independent of UArizona. Secure written acknowledgment, through tech transfer and counsel, that the project is outside the scope of your appointment, built on personal time. This is the single highest-priority action in the entire plan; until it exists, the entity structure, the Willamette move, and the no-lock-in promise are all at risk. (Not legal advice — confirm with counsel.)

**Licensing and the CLA question.** AGPL-3.0 core + Apache-2.0 primitives, contributions under DCO. DCO is the right trust signal: contributors assign nothing, and because no single entity aggregates copyright, no one can ever relicense or rug-pull. The cost is that DCO forecloses selling proprietary licenses to the AGPL core (no rights-holder can grant them). Recommendation: stay DCO; the split license already captures most of the open-core benefit (permissive primitives drive adoption; the AGPL core blocks proprietary forks). Revisit only if a PBC arm makes commercial licensing a genuine need.

**Governance.** A lightweight, Ostrom-informed charter from the start: defined roles, an explicit decision process, a contribution policy, and a clear boundary between the commons and any commercial activity. The foundation board formalizes this later. Governance that can survive the founder is itself a risk mitigation (§12).

**Founding team.** The managing organization is not a solo effort, which both de-risks it and strengthens the PESOSE case (Track 1 is largely about whether you can actually stand up a governed, sustainable organization). Beyond the founder/technical lead, the founding members include **Ben Markwart** — a research software engineer (UArizona CALES) building EduCloud's **Registry & federation layer** (see §8), his principal technical contribution, who brings nonprofit board-governance and legal experience (Cooper Center for Environmental Learning) directly relevant to incorporating the entity — and **Angela Cruze**, who brings extensive nonprofit, grant-writing, and program-development experience. Between them, governance/legal, sustainability, and program development are covered by people who have done them before. One constraint to track: as founding members, both are part of the proposing team and therefore are *not* eligible to write the external letters of collaboration PESOSE requires. Markwart's contributions, like the founder's, should enter the project under the same personal-time / DCO / IP-independence terms (his UArizona employment raises the same IP-clearance question as the founder's — confirm for his code too).

---

## 7. Home-institution strategy: UArizona now, Willamette flagship by 2027

**Now (UArizona).** UArizona is the natural near-term home: it is your employer, it leads MESA, and it can administer the first grants (IUSE, PESOSE). EduCloud ties into MESA's EOT mission here. UArizona's role is **employer + grant administrator + MESA context — not IP owner.**

**Transition (Willamette, Spring or Fall 2027).** If the remote tenure-track move lands, flagship status shifts to Willamette, where EduCloud anchors the data-science program's "Big Data & Human-Centered Computing" pillar. Willamette's regional cyberinfrastructure partners (PSU, UO) and faculty allies become part of the story.

**Why the shift is a non-event for the project — by design.** Because the IP lives in the fiscal sponsor/foundation and not in any university, moving institutions does not move the code, the trademark, or the governance. What moves is grant administration and your appointment. Concretely:

- **Hold new grants at the right institution for their timing.** A grant submitted in Jan 2027 could be administered by UArizona or Willamette depending on where you are by award time; sequence submissions to land where you'll be.
- **NSF allows awards to transfer between institutions**, but it is bureaucratic; prefer to *start* an award at the institution that will hold it, or use a subaward/co-PI bridge (UArizona ↔ Willamette) across the transition rather than transferring mid-stream.
- **The foundation is the stable anchor.** Even if both your appointment and the administering institution are in flux, the foundation/sponsor continuously holds the IP, the trademark, and the donations — so the project never goes homeless.

**Risk framing:** the Willamette move is *upside*, not load-bearing. If it doesn't happen, UArizona remains a viable home and the floor (§0) is unaffected.

---

## 8. Build timeline and roadmap

Anchored to June 2026. The technical build, the entity steps, and the funding actions are interleaved so each unlocks the next. Fall 2026 is deliberately a pilot, not a launch — there is not enough runway to be production-ready and win broad adoption for a semester starting in ~11 weeks.

| Window | Product | Entity / governance | Funding | Adoption |
|---|---|---|---|---|
| **Summer 2026** (now–Aug) | Webhook grading; GitLab adapter; dashboard MVP; `doctor`; one-command deploy; GHC import path; docs → **1.0-beta**. Markwart begins the **Registry & federation layer** (parallel workstream) | Secure **IP waiver**; apply to fiscal sponsor; settle the name + trademark; draft governance charter | File **ACCESS Discover**; scope + **write PESOSE Track 1** (target **Sept 1, 2026** — accelerated) | Stand up MESA + UArizona pilot course(s) |
| **Fall 2026** (Sep–Dec) | Harden to **1.0 GA**; per-test student feedback; push-to-regrade. **Registry MVP** (catalog + search + `register` CLI + Coolify adapter + Keycloak — Markwart) | Fiscal sponsor live; charter published | **PESOSE Track 1 submitted Sept 1**; write **IUSE** proposal (due ~Jan 20, 2027) | First real classroom use (UArizona + 1–2 lighthouse adopters); collect usage data |
| **Spring 2027** (Jan–May) | Stabilize; migration tooling; hosted-option pilot design; **federation breadth begins** (JupyterHub workspaces, Open OnDemand/HPC, MinIO — Markwart) | Begin **foundation** formation if PESOSE funded; **possible Willamette shift** | Submit **IUSE Level 1** (~Jan 20); PESOSE decision expected | Spring-2027 adopters; first case studies |
| **Summer 2027** | Sol/AI layer opt-in GA; **federation breadth GA** (workspaces, HPC, storage); scale testing | Foundation incorporated (PESOSE-funded) | **PESOSE Track 2** prep; **IDSS** positioning with MESA (July deadline) | Position as the established GHC successor |
| **Fall 2027 → 2028** | Hosted offering pilot; consortium path | **Willamette flagship** (if Fall 2027); optional **PBC** if hosting demand is real | **IDSS Category I** bid via MESA; philanthropic round | Multi-institution adoption wave; workforce metrics |

**The non-negotiable build target:** a genuinely deployable, well-documented 1.0 — one-command install, working autograding, GHC import — while the retirement is still driving migration. Everything else (AI layer, hosted offering) is sequenced after.

**On the Registry & federation layer.** Markwart's principal contribution (full proposal: `EduCloud-registry-federation-proposal.md`) is a pivot from a Posit Connect replacement to EduCloud's *registry and federation layer*: a lightweight, self-hostable catalog of EduCloud objects (courses, projects, datasets, artifacts, compendia, agents) plus thin seams to mature, already-solved hosting/compute systems — and to MESA's infrastructure — rather than reimplementing any of it. The novel piece is the **Registry** itself (the catalog); hosting is *federated, not rebuilt* (the same adapter discipline EduCloud uses for Git hosts). Scope is deliberately staged: a **Registry MVP** — catalog + search + a `register` CLI + one Docker/Coolify adapter + Keycloak identity — is a *core* feature targeted for Fall 2026, feasible because Markwart owns it as a workstream parallel to the GHC-replacement core, it composes through a thin seam, and it never gates the 1.0. The full federation (JupyterHub, Open OnDemand, MinIO, Harbor, OpenSearch, AI serving, agents) is a 2027+ roadmap. Three guardrails keep this from diluting EduCloud: integrate rather than rebuild (so it does not sprawl into MESA's compute/HPC/AI-serving lane); keep the GHC replacement the crisp, fundable core; and treat the Registry as the ecosystem layer that *extends* that core — which is also why it strengthens, rather than blurs, the PESOSE ecosystem case.

---

## 9. Funding plan

The strategy is a **ladder run in parallel, not series** — multiple applications in flight so that no single rejection stalls the project. Amounts are planning estimates; verify against current solicitations before each submission (NSF program terms and deadlines shift).

| Vehicle | Amount (est.) | Window | Purpose | Administered by |
|---|---|---|---|---|
| **ACCESS Discover** allocation | Free credits (≤1.5M) | Now; ~2-wk review | Grading + session compute | Project / PI |
| **NSF IUSE: EDU**, Level 1 | ≤ $400K / 3 yr | Submit ~Jan 20, 2027 | Buyout, RSE, community, pilots, assessment | UArizona → Willamette |
| **NSF PESOSE Track 1** | ≤ $300K / 1 yr | **Sept 1, 2026** (accelerated) | Stand up the managing org + governance + ecosystem plan (funds the entity itself) | UArizona / fiscal sponsor |
| **NSF PESOSE Track 2** | ≤ $1.5M / 2 yr | ~12–18 mo after Track 1 | Grow contributor base, governance, sustainability | Foundation / university |
| **Philanthropy** (Sloan, foundations) | ~$250K–750K | Rolling / LOI | OSPO, sustainability, staffing | Fiscal sponsor / foundation |
| **NSF IDSS Category I** (via MESA) | $10–30M / 5 yr (EduCloud = a slice) | ~July 2027 or 2028 | EduCloud as EOT pillar + use-case in MESA scale-up | UArizona (MESA lead) |
| **NSF SBIR/STTR** (only if PBC) | ~$305K Phase I / ~$1.25M Phase II | Pending reauthorization* | Productize a hosted offering | PBC arm |
| Donations / memberships | Variable | Ongoing | Sustainability | Fiscal sponsor → foundation |

*SBIR/STTR statutory authority lapsed 30 Sept 2025 and is under reauthorization uncertainty as of now; treat the for-profit channel as real but not currently dependable.

**Sequencing logic:** ACCESS removes compute from the cost equation immediately. IUSE or PESOSE Track 1 — whichever lands first — funds the first year of people; applying to both in parallel is the hedge. PESOSE Track 1 is special because it funds the act of standing up the foundation and deciding the entity question. IDSS via MESA is the scale event but is upside, not the spine. Your course buyout keeps you funded across any gap.

**Bridge:** between award cycles, fiscal-sponsor donations and a lean burn (you + a fractional RSE) sustain the project. The plan never requires two grants to land simultaneously.

---

## 10. Team and organization

**Now:** you — founder, technical lead, principal investigator, project director.

**First hire (funded by IUSE/PESOSE Track 1):** a research software engineer at 0.5–1.0 FTE to share maintenance and de-risk the key-person dependency. This is the highest-leverage hire and should be the first dollar spent on people other than your buyout.

**Second (as funding allows):** a part-time community/documentation/training coordinator — the role that converts a tool into an adopted project and feeds the MESA EOT metrics.

**Advisory:** an informal advisory group spanning MESA (Tyson Swetnam), a Willamette ally (e.g., the data-science faculty), and an OSS-governance voice (via the fiscal sponsor / SFC). Formalized as a board when the foundation incorporates.

**Collaborators:** MESA for the captive audience and CI; Willamette for the flagship home; the Carpentries/RSE community for contributors and dissemination.

---

## 11. Financials (illustrative)

A nonprofit/OSS operating budget, not a startup P&L. Figures are planning-grade.

**Year 1 (lean), annual direct costs:**

| Line | Est. |
|---|---|
| Your effort (course buyout + summer months) | ~$70K |
| RSE / software engineer (0.5–1.0 FTE) | ~$110K |
| Community / docs / training (0.25–0.5 FTE) | ~$45K |
| Travel & dissemination | ~$20K |
| Operations (project infra, services, legal/trademark, contractors) | ~$25K |
| Compute | ~$0 (ACCESS-subsidized) |
| **Direct subtotal** | **~$270K** |
| University F&A (~50% of applicable MTDC) | ~$110–130K |
| **Total** | **~$380–400K** |

This fuller-team year is roughly three times a single IUSE Level 1's annual (~$133K/yr), so it is funded by the *stack* — IUSE Level 1 + PESOSE Track 1 + donations — not by any one grant; the financial model shows the near-term stack covering ~76% of a three-year budget at this scale, the remainder from PESOSE Track 2 / philanthropy / the IDSS slice. For an IUSE-only floor, drop to ~1 summer month plus a part-time RSE or a graduate student and trim — that fits a single Level 1. The parameterized model (`EduCloud-financial-model.xlsx`) is the authoritative version of these numbers; this section is a summary.

**Years 2–3:** comparable or modestly growing direct costs, with the revenue mix diversifying — grants taper as earned revenue (hosting/support), institutional memberships, and donations ramp. Target: cover ~1–2 FTE of ongoing maintenance from non-grant revenue by Year 3–4, so the project is sustainable even between or after grants.

**Earned-revenue model (illustrative, optional):** managed EduCloud per-institution subscription roughly $5–25K/yr by size; support/SLA tiers; migration and integration services; paid training. Conservative, and only via the foundation program or PBC. The point is not a large business — it's a credible path to not depending on grants forever.

---

## 12. Risk register and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **UArizona IP waiver denied/delayed** | Medium | Critical | Pursue in writing now via counsel; frame as outside-scope/personal-time; this is the #1 gate — resolve before building further commitments |
| **GHC Fall-2026 window largely missed** | High | Medium | Target Spring/Fall 2027 as the real waves; treat Fall 2026 as pilots; use the shutdown as urgency narrative, not a hard GA date |
| **Adoption fails — instructors don't switch** | Medium | High | One-command deploy + GHC import tooling; lean on MESA captive audience; lighthouse adopters + case studies; Carpentries/RSE channels |
| **Key-person dependency (you)** | Medium | High | Fund an RSE from the first grant; recruit co-maintainers early; document everything; founder-independent governance |
| **A grant misses** | Medium | Medium | Parallel (not serial) applications; donations as bridge; buyout keeps you funded; plan never needs two grants at once |
| **Willamette move falls through** | Medium | Low | Foundation holds IP → home is portable; UArizona remains viable; floor (§0) unaffected |
| **MESA scale-up / IDSS doesn't materialize** | Medium | Low–Med | EduCloud's value is not contingent on IDSS; it stands alone; IDSS is upside |
| **Maintainer burnout / scope creep** | Medium | Medium | Enforce the anti-features discipline already in the design; modularity; community contributions; hosted revenue funds maintenance |
| **Competition (incumbents undercut; GHC reverses)** | Low–Med | Medium | Differentiation (self-host, privacy, host-agnostic, no lock-in, free) is durable; open-source community is the moat |
| **Sustainability after grants** | Medium | High | The hybrid earned-revenue + membership + donation model; subsidized compute keeps the bar low |

**On "foolproof":** the plan is robust because the floor is cheap and reachable, funding is parallelized, IP is decoupled from any institution, the first audience is captive, and scope is disciplined. The genuinely load-bearing items are few — chiefly the IP waiver — and all are named.

---

## 13. Critical path — what must be true

In order, the things that actually have to hold:

1. **The IP waiver is secured.** Gate for the entire structure.
2. **A deployable, documented 1.0 ships while the GHC retirement is still driving migration** (through 2026–2027).
3. **At least one of {IUSE, PESOSE Track 1} lands** to fund people — hedged by applying to both.
4. **ACCESS covers compute** — low risk, do it now.
5. **A fiscal sponsor is in place** for funds and donations.
6. **A handful of lighthouse adopters and real usage data exist by mid-2027** — feeding PESOSE Track 2, the IDSS case, and the Willamette pitch.

The Willamette flagship shift and the IDSS scale-up are explicitly *not* on this list. They are the ceiling. The floor is reached if items 1–6 hold, and items 1, 4, and 5 are largely within your direct control.

---

## 14. The next 90 days

Concrete, ordered, startable now:

1. **Open the IP-waiver conversation with UArizona tech transfer / counsel.** Nothing matters more. Get it in writing.
2. **File the ACCESS Discover allocation.** Removes compute from the budget; ~2-week turnaround.
3. **Apply to a fiscal sponsor** — Open Source Collective for funds handling; evaluate Software Freedom Conservancy for the durable home.
4. **Settle the name** (EduCloud / Quad / Cairn) and file the trademark through the sponsor.
5. **Finish the 1.0-beta build slice:** webhook grading, GitLab adapter, dashboard MVP, `doctor`, one-command deploy, GHC import path, docs.
6. **Stand up the UArizona/MESA pilot** for a Fall 2026 course.
7. **Decide the PESOSE Track 1 timing** (Sept 2026 vs Mar 2027) and start the proposal; begin the IUSE proposal in parallel for January.
8. **Publish a lightweight governance charter** and a public roadmap.

---

*This is a private planning document. Funding amounts and NSF deadlines are estimates to verify against current solicitations; entity and tax specifics require counsel. The author is not a lawyer or accountant.*
