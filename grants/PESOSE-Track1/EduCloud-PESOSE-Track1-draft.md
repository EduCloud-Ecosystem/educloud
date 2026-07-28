# PESOSE Track 1 — Project Description (Working Draft)

**Solicitation:** NSF 26-506 (Pathways to Enable Secure Open-Source Ecosystems)
**Track 1 — Scoping & Planning · ≤ $300,000 · up to 1 year · Project Description limit: 7 pages**
**Target deadline:** March 2, 2027 (NSF 26-506, Track 1) — updated July 2026; the September 1, 2026 acceleration was abandoned. The letters-of-collaboration mechanics in `SEPTEMBER-sprint-plan.md` still apply on the new calendar.
**Status:** working draft · `[bracketed]` items are yours to supply · prose to be tightened to 7 pages

---

## ⚠️ Compliance checklist (do not skip — several are hard requirements)

- [ ] **Title** must read exactly: `PESOSE: Track 1: <title>`
- [ ] **Project Summary** last line: `Keywords:` + 2–5 terms, semicolon-separated
- [ ] **Product pointer**: an in-line citation + References Cited entry pointing to the public repo — **no URLs in the Project Description body**
- [ ] **≥ 3 letters of collaboration** (max 5) from *external* users/contributors **not** on the team — *the gating item; secure NOW as forward-looking commitments from named Fall-2026 adopters (see `letters-of-collaboration-asks.md`), due Aug 7*
- [ ] If EduCloud will rely on institutional facilities/infrastructure post-award, **one LOC** describing that provision (e.g., UArizona/CyVerse or Willamette)
- [ ] **List of Project Personnel, Collaborators, and Partner Organizations** (tabular: Full name, Organization, Role)
- [ ] Budget includes **I-Corps for PESOSE** participation (mandatory for Track 1 awardees)
- [ ] No voluntary cost sharing (prohibited); F&A allowed at the institution's negotiated rate (no cap)
- [ ] Address the four Track 1 areas **and** the four Track 1 review questions (mapped in §§2–7 below)

---

## Title

**PESOSE: Track 1: EduCloud — Scoping a Secure, Privacy-Preserving Open-Source Ecosystem for Version-Controlled Assignment Distribution and Autograding**

*(Working name. If you settle on Quad or Cairn, change here and throughout.)*

---

## Project Summary (1 page — separate NSF document; draft below)

**Overview.** EduCloud is an open-source platform for teaching with code: it distributes programming assignments to per-student version-controlled repositories, collects them, and grades them in isolated, sandboxed containers. Unlike the tools it succeeds, EduCloud is self-hostable, works across multiple Git hosts, and is built so that student personal data never enters the system by design. With GitHub Classroom — the dominant tool of its kind — decommissioned in August 2026, hundreds of institutions face a forced migration with few privacy-preserving, self-hostable, no-cost options. This Track 1 project will conduct the scoping and planning needed to transition EduCloud from a working prototype with early adopters into a governed, secure, sustainable open-source ecosystem (OSE): ecosystem discovery, a governance and licensing model, a security and privacy risk plan, and a community-building strategy for users and contributors.

**Intellectual Merit.** The project advances understanding of how to govern and secure an OSE whose core function is the execution of untrusted, third-party (student) code at scale, and whose central value proposition is an *architectural* — not merely policy-based — privacy guarantee. It produces a transferable model for secure, privacy-preserving educational cyberinfrastructure and for the stewardship of a commons that must remain trustworthy to be adopted.

**Broader Impacts.** EduCloud lowers the cost and raises the privacy floor of computing education, with deliberate focus on community colleges, transfer pathways, and minority-serving institutions. It supplies the graded, version-controlled assignment layer for national data-science workforce training, and contributes a reusable secure-autograding pattern to the open-source community. By keeping student data out of commercial platforms, it strengthens institutional FERPA postures.

`Keywords:` education; cybersecurity; privacy; open-source ecosystems; workforce development

---

## Project Description (7 pages)

### 1. The open-source product, its status, and the problem

EduCloud [1] is a working open-source prototype that distributes coding assignments to per-student Git repositories, enforces deadlines, and autogrades submissions by executing tests inside ephemeral, isolated containers. Its design is defined by four commitments: **host-agnostic** operation through pluggable adapters (GitHub and self-hosted Forgejo/Gitea validated end-to-end; GitLab in progress); **privacy by architecture** — the system stores Git usernames and assignment state, never student personal data; **self-hostable-first** deployment (an embedded, zero-configuration data store by default, scaling to a server database); and **no lock-in** (complete export/import of project state, no proprietary formats). An optional, off-by-default tutoring and feedback layer (`Sol`) sits behind the deterministic grading harness and is never the final arbiter of a grade. A registry-and-federation layer — a lightweight, self-hostable catalog of courses, projects, datasets, and teaching artifacts with browse/search and a `register` CLI, federated through thin adapters to existing open-source deployment and identity infrastructure (Coolify; Keycloak) rather than rebuilt hosting — is in design as the ecosystem's interoperability primitive.

`[Update at submission with actual status]` Current dissemination is via the public repository under a split license — the control plane under AGPL-3.0, the interoperability primitives under Apache-2.0 — with contributions accepted under the Developer Certificate of Origin. The prototype is validated end-to-end across multiple Git hosts; `[N]` faculty across `[5+]` institutions of diverse types have **committed to pilot in Fall 2026**, and `[N]` external contributors have committed to the project. (Because this proposal is submitted at the start of the migration window rather than after it, adoption is evidenced by these binding commitments and the accompanying letters of collaboration rather than by completed pilots — appropriate to a planning-grant Track 1.) These external users and contributors are the source of the letters of collaboration accompanying this proposal — submitted as forward-looking commitments from named adopters and contributors who will pilot and contribute beginning Fall 2026.

**The problem.** GitHub Classroom, the dominant assignment-distribution and autograding tool in computing education, was decommissioned on August 28, 2026 [2]; new classroom creation had ended months earlier, and stored classroom data was deleted in September 2026. Every department that relied on it must migrate. The replacements the vendor directs users toward are commercial, hosted, per-seat services that place student data in third-party platforms — a poor fit for privacy- and sovereignty-sensitive institutions, for cost-constrained community colleges, and for the growing need to train a national data-science workforce on infrastructure that institutions can actually run themselves. No widely adopted successor is simultaneously self-hostable, host-agnostic, privacy-preserving by design, and free. EduCloud addresses precisely this gap — but a robust tool is not yet an ecosystem. The work this proposal scopes is the governance, security, sustainability, and community foundation required to make it one.

*(Addresses required elements: product pointer [1]; status/dissemination/user-and-contributor base; the problem. Maps to Track 1 review criterion 1: a societal/national need not currently being adequately met.)*

### 2. Ecosystem Discovery

Phase activities will rigorously test demand and define the ecosystem, building on (not assuming) the migration pressure created by the GitHub Classroom shutdown. We will: (a) conduct structured interviews and a survey of displaced educators, departmental IT decision-makers, and data-science training programs to characterize unmet needs, adoption barriers, and the true cost of switching — work front-loaded through the mandatory I-Corps for PESOSE customer-discovery activities; (b) segment and size the potential **user** community (computing and data-science instructors; privacy- and sovereignty-sensitive institutions; community colleges and transfer programs; national training programs such as `[MESA / CyVerse / the Carpentries]`); and (c) identify the potential **contributor** community (research software engineers, Carpentries instructors, and institutions that already self-host Forgejo or GitLab).

We will articulate why an OSE — rather than a company or a closed tool — is the correct vehicle. The argument is structural: a privacy guarantee is only credible if it is inspectable; a no-lock-in promise is only credible if the source is open; and long-term trust in infrastructure that runs untrusted code requires community oversight rather than a single vendor's assurances. Open-source is not incidental to EduCloud's value proposition; it is the mechanism that makes the value proposition believable.

*(Track 1 required area: Ecosystem Discovery.)*

### 3. Organization and Governance

EduCloud's IP is deliberately independent of any single institution, which makes a neutral steward both possible and necessary. Track 1 will scope and plan that steward through the following activities: (a) **entity and governance design** — evaluate and select a path from a near-term fiscal sponsor (e.g., a recognized open-source fiscal host) to a durable 501(c)(3) foundation that holds the trademark, governs the canonical codebase, and is eligible to receive grants and donations; draft an Ostrom-informed governance charter defining roles, decision processes, and the boundary between the commons and any future earned-revenue services; (b) **licensing and IP** — finalize the AGPL-3.0 (control plane) + Apache-2.0 (interoperability primitives) split and the DCO-based contribution model, and document the rationale and its anti-rug-pull properties; secure the project trademark; (c) **development and integration processes** — define the contribution, review, release, and maintenance workflows that a distributed contributor community will use; and (d) **metrics for long-term success** — define the indicators (adoption breadth, contributor growth and retention, security posture, financial self-sufficiency) against which the ecosystem will be judged.

A core scoping output is an explicit separation of concerns — who owns the code (the foundation), who administers grants (a university), and where funds and donations live (the fiscal sponsor, then the foundation) — engineered so that the project's institutional home can evolve without disrupting the ecosystem.

*(Track 1 required area: Organization and Governance. Maps to review criterion 2: long-term sustaining vision.)*

### 4. Risk Analysis / Security Plan

Security and privacy are not adjacent concerns for EduCloud; they are its core function and its core promise, which makes it an unusually direct fit for PESOSE's emphasis. Track 1 will produce a documented threat model and a security/privacy plan addressing:

- **Execution of untrusted code (the central risk).** EduCloud's defining technical task is running untrusted student code to grade it. We will specify a defense-in-depth sandbox — kernel-level isolation, runtime monitoring, egress filtering, and policy-based access control — and align it with established secure-execution infrastructure for untrusted AI- and human-generated code `[e.g., the MESA AI-Sandbox stack]`. We will follow CISA/NSA software-supply-chain guidance [3] and the Open Source Security Foundation best practices [4].
- **Supply-chain and release integrity.** Plans for software bills of materials (SBOMs), signed releases, dependency and vulnerability scanning, and reproducible builds — the "secure modification and release" and "chain of custody" the solicitation calls for.
- **Privacy as an architectural guarantee.** EduCloud's data-minimization design (Git usernames and assignment state, never student personal data) makes privacy a property of the architecture rather than of a policy that can be misconfigured. We will document the data model, its FERPA implications, and how the guarantee is preserved as the system scales.
- **Identity and access management.** Federated identity options (institutional SSO via CILogon/InCommon, or Git-host identity) with the privacy-minimal default preserved.
- **Quality assurance.** The deterministic grading harness, automated test and CI infrastructure, and review gates that protect correctness and security of new content.

*(Track 1 required area: Risk Analysis/Security Plan — the heart of a PESOSE proposal.)*

### 5. Community Building

A tool with one maintainer is not an ecosystem. Track 1 will plan the transition to a distributed community of users and contributors through: (a) **user engagement** — migration tooling and documentation that lower switching cost for departing GitHub Classroom users; integration into national training programs (`[MESA Tier 1–3 and Educator Fellows]`) so that the curriculum learners complete *is* delivered through EduCloud; and workshops in the Carpentries tradition; (b) **contributor growth** — a documented contributor ladder, "good first issues," DCO tooling, and targeted outreach to the research-software-engineering and Carpentries communities; (c) **convenings** — presence at SIGCSE, PEARC, and JupyterCon, and `[a community hackathon/sprint]`; and (d) **broadening participation** — deliberate engagement of community colleges, transfer-serving programs, and minority-serving institutions, consistent with the PI's own background and the project's equity goals. These activities are also the pipeline that produces the external users and contributors on whom a future Track 2 proposal — and this proposal's letters of collaboration — depend.

*(Track 1 required area: Community Building. Maps to review criterion 3: recruitment strategy for contributors and userbase growth.)*

### 6. Five-year vision and sustainability

Within five years EduCloud is a foundation-stewarded commons with a diverse contributor community and adoption across institution types, complemented — only if demand warrants — by an earned-revenue services arm (managed hosting and support) that funds maintenance without compromising the open core. The sustainability model layers grants (near term), institutional memberships, donations through the fiscal sponsor/foundation, and earned revenue (medium term); a preliminary financial model indicates a credible path to covering ongoing maintenance from non-grant revenue. Compute for adopters is met substantially through national cyberinfrastructure allocations rather than commercial cloud, which lowers the bar to self-sufficiency. This is the "missing middle" PESOSE targets: the distance between a promising open-source product and a secure, self-sustaining ecosystem others can safely build on.

*(Maps to review criterion 2: long-term sustaining vision.)*

### 7. Milestones, metrics, and evaluation plan

A 12-month, quarterly plan with an external evaluator `[name/role — secure a commitment before submission]` conducting formative and summative assessment:

| Quarter | Milestones | Metrics / deliverables |
|---|---|---|
| Q1 | I-Corps customer discovery; interviews/survey of displaced educators and IT decision-makers | ≥ `[40]` interviews; demand/segmentation report |
| Q2 | Governance + entity path selected; licensing/DCO finalized; trademark filed | Governance charter v1; licensing decision memo |
| Q3 | Threat model + security/privacy plan; SBOM/signed-release pipeline designed | Published threat model; security plan; data-model/FERPA memo |
| Q4 | Community-growth plan; adopter and contributor pipeline; Track 2 readiness package | ≥ `[N]` committed adopters; ≥ `[N]` external contributors; sustainability plan; Track 2 go/no-go |

Phase success is defined by delivering the four plans (governance, security/privacy, community, sustainability) and meeting readiness thresholds for a Track 2 proposal.

*(Maps to review criterion 4: specific, actionable milestones + evaluation plan.)*

### 8. Team and qualifications

`[PI name]` is `[Assistant Professor of Practice and Faculty Director of Instructional Computing at the University of Arizona]` — a role that includes leadership of instructional computing infrastructure (relevant to PESOSE's OSPO-leadership PI-eligibility pathway) — and serves as training/education lead on the NSF-funded MESA cyberinfrastructure project, giving the project direct access to a national training audience and to operations-grade cyberinfrastructure (compute, sandboxing, identity). The PI has prior NSF education funding `[IUSE: Quantum Inventioneers]`, built the EduCloud prototype, and brings a community-college/transfer background aligned with the project's broadening-participation goals. The proposing team is deliberately lean and matched to Track 1's deliverables. Co-PI `[A. Cruze — nonprofit, grant-writing, and program-development experience]` leads the Organization & Governance work, the sustainability plan, and the mandatory I-Corps for PESOSE participation. Senior personnel `[B. Markwart — research software engineer with nonprofit board-governance and legal experience (Cooper Center for Environmental Learning)]` leads the security/threat-model and governance documentation and the design of the registry/federation interoperability layer. Contributors and advisors outside the proposing team — preserving the external-letter pool — include `[MESA PI T. Swetnam (cyberinfrastructure and security advisory; brokers the facilities letter)]`, `[adopting faculty at five-plus institutions of diverse types]`, and `[an open-source-governance advisor via the fiscal sponsor]`. The qualifications, the working prototype, and the committed early adopters together make the case that this team can execute the scoping work and lead the resulting ecosystem.

*(Addresses required element 4: justification that the team is qualified.)*

### Intellectual Merit and Broader Impacts (explicit statement)

**Intellectual Merit.** EduCloud advances knowledge of how to govern and secure an open-source ecosystem whose core operation is executing untrusted third-party code and whose value rests on an architectural privacy guarantee — a model transferable to other secure, privacy-preserving educational and scientific cyberinfrastructure.

**Broader Impacts.** A free, self-hostable, privacy-preserving successor to GitHub Classroom serving displaced educators nationwide; a graded assignment layer for national data-science workforce training; deliberate broadening of participation among community colleges, transfer programs, and MSIs; a reusable secure-autograding pattern for the open-source community; and stronger institutional FERPA postures through data-minimizing design.

---

## References Cited (illustrative — complete before submission)

1. EduCloud open-source repository. `[in-line citation form; repository identifier in References — no URL in the Description body]`
2. GitHub. GitHub Classroom sunset and transition announcement, 2026. `[citation]`
3. CISA/NSA/ODNI. *Securing the Software Supply Chain: Recommended Practices for Developers*, 2022. `[citation]`
4. Open Source Security Foundation. Best Practices criteria. `[citation]`
5. `[Ostrom, governance of the commons]`
6. `[Reich, Failure to Disrupt — edtech adoption/equity]`
7. `[FERPA / student-data privacy reference]`

---

## What's still on you before this is submittable

1. **Three to five letters of collaboration** from real external users/contributors — the single hard gate. Secure them NOW as forward-looking commitments from named Fall-2026 adopters; asks go out the week of June 16 with an Aug 7 due date (`letters-of-collaboration-asks.md`). (Infrastructure reliance is covered by the separate facilities letter — CyVerse/Jetstream2, via T. Swetnam.)
2. **An external evaluator** — name and a short evaluation design; secure the commitment in June (not August).
3. **The 1-year, ≤$300K budget + justification** — drafted in the companion budget file (~$290K: PI + co-PI + fractional RSE + GRA + I-Corps travel + participant support + F&A, with headroom). Confirm institutional rates with UArizona OSP and the I-Corps budget specifics — in week one.
4. **Fill every `[bracket]`** — name/title, pilot institutions and counts, collaborators, the product citation, and the milestone numbers.
5. **Tighten to 7 pages** and confirm formatting against the current PAPPG and the PESOSE website's budget-prep guidance.
6. **Decide the name** (EduCloud / Quad / Cairn) before the trademark and the title are locked.
