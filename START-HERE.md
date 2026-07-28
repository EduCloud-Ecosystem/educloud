# EduCloud — Project Folder

*Start here · June 2026*

> **July 2026 update.** Names are settled: Cairn (was Quad), Belay (was Sol),
> Waypoint (was the “HOST”/Registry), Portage (was Commons/claude-lanes),
> Outfitter (new) — see `SYSTEM.md` for the canonical definition and shared
> contracts, `DOCUMENTATION.md` for the current document index, and
> `EDUCLOUD-STATUS.md` for priorities. **PESOSE correction:** the September 1,
> 2026 acceleration was abandoned; PESOSE Track 1 is NSF 26-506, deadline
> **March 2, 2027** (UA internal ~mid-Feb). Text below is otherwise unrevised
> June material.

This folder holds the strategy, funding, proposal, and architecture materials for EduCloud — the open-source, self-hostable, privacy-preserving successor to GitHub Classroom (working name; alternatives Quad/Cairn), with a Coolify-based hosting/federation layer and the EduCloud Registry on top. Two near-term funding targets anchor everything: **IUSE ESL Level 1** (≤$400K/3yr, ~Jan 20, 2027) and **PESOSE Track 1** (≤$300K/1yr, Mar 2, 2027). Both grants exist in two versions — **UArizona-anchored** (near-term) and **Willamette-anchored** (after the flagship move) — detailed in the team & roadmap doc.

## Folder map

```
educloud/
├── START-HERE.md                              ← you are here (index + next steps)
│
├── strategy/
│   ├── EduCloud-business-plan.md              master business & operating plan
│   ├── EduCloud-financial-model.xlsx          parameterized model — edit the blue cells
│   ├── EduCloud-funding-strategy.md           diversified funding portfolio, ranked by viability — NSF becomes two bets among many
│   ├── EduCloud-team-funding-roadmap.md       two-anchor grant teams + founding team + integrated timeline
│   └── willamette-pitch.md                    Willamette positioning — names the faculty bench + Chemeketa pilot
│
├── grants/
│   ├── PESOSE-Track1/                          (deadline March 2, 2027 — Sept 1 acceleration abandoned; see banner above)
│   │   ├── SEPTEMBER-sprint-plan.md           critical path, week-by-week, full NSF checklist
│   │   ├── letters-of-collaboration-asks.md   the gating item — templates + recipients + emails, send now
│   │   ├── EduCloud-PESOSE-Track1-draft.md    Project Description — March 2, 2027 target
│   │   └── EduCloud-PESOSE-Track1-budget.md   1-yr ≤$300K budget (~$290K) — lean team
│   ├── IUSE-ESL-Level1/
│   │   ├── EduCloud-IUSE-ESL-Level1-draft.md  Project Description — target ~Jan 20, 2027
│   │   └── EduCloud-IUSE-ESL-Level1-budget.md 3-yr ≤$400K budget (~$399K) — anchor-flexible
│   ├── foundations/                           non-NSF drafts, one per solicitation (see its README for send order)
│   │   ├── README.md                          the send-order map
│   │   ├── Sloan-OpenSource-in-Science-LOI.md SEND NOW — the 2-page flagship ask
│   │   ├── ECMC-concept-paper.md              Spring 2027, with pilot data
│   │   ├── Ascendium-concept-paper.md         Spring 2027, with pilot data
│   │   ├── Hewlett-OER-LOI.md                 Spring 2027 — Sol/OER framing
│   │   ├── Spencer-small-research-grant.md    ≤$50K research hedge if IUSE misses
│   │   ├── NLnet-NGI-application.md           2027 — Registry standard component ask
│   │   └── Sloan-OSPO-Willamette-LOI.md       conditional on the Willamette move
│   └── EduCloud-adopter-LOC-recruitment-kit.md  adopter/contributor recruitment + letter templates
│
├── architecture/
│   ├── EduCloud-registry-federation-proposal.md   Markwart's principal contribution — the Registry
│   └── EduCloud-hosting-reconciliation.md          reconciliation → Coolify as the hosting engine
│
├── onboarding/
│   ├── John-Chen-orientation.md               read-in for John Chen (early collaborator; PESOSE now targets March 2, 2027)
│   ├── EduCloud-Brief-for-Ben-Markwart.docx   formal brief: project, Sept timeline, Ben's role, CALES F&A + benefits
│   └── EduCloud-Brief-for-Ben-Markwart.pdf    same, send-ready PDF
│
├── mesa/
│   ├── educloud-mesa-integration.html         interactive MESA integration page (incl. Registry)
│   └── educloud-mesa-pitch.pdf                one-page pitch for Tyson (incl. Registry)
│
└── project-docs/
    ├── README.md                              repo README (current — incl. Registry layer)
    ├── GOVERNANCE.md                          governance (current — incl. founding stewards)
    ├── CONTRIBUTING.md                        contribution guide (current — DCO, license split, Registry)
    └── diagrams/
        ├── quad-roadmap.svg                   funding/launch roadmap (dates corrected)
        └── quad-mesa-integration.svg          EduCloud × MESA architecture (+ Registry note)
```

Everything in this folder is current as of this revision.

## Actionable next steps

**Do now — the gates (this summer):**
1. **IP waiver.** UArizona tech transfer + counsel: written acknowledgment that EduCloud is outside your appointment, built on personal time. Cover **Markwart's Registry/federation code** under the same personal-time / DCO terms. *Nothing downstream is safe until this exists.*
2. **File the ACCESS Discover allocation** (~2-week turnaround) — removes compute from both budgets.
3. **Apply to a fiscal sponsor** *(now also the key that unlocks the entire philanthropy lane — most foundations require a 501(c)(3) vehicle)* (Open Source Collective for funds; assess Software Freedom Conservancy for durability). Markwart (legal) + Cruze (nonprofit) lead; lock the founding team.
4. **Decide the name** (EduCloud / Quad / Cairn) → file the trademark through the sponsor.
5. **Ship the 1.0-beta** — webhook grading, GitLab adapter, dashboard, `doctor`, one-command deploy, GHC import, docs — by end of summer. In parallel, **Markwart starts the Registry & federation layer** (Coolify + Keycloak + catalog) as a workstream that never gates the 1.0.
5a. **Send the Sloan two-page LOI** (technology@sloan.org — Open Source in Science framing) and **investigate GitHub's partner-solution listing**; both are near-free and high-leverage (see `EduCloud-funding-strategy.md`).

**Line up people (this summer):**
6. **The IUSE anchor pair** — UArizona path: email **Regina Deil-Amen** and **Emily Halvorson-Otts** (ask her for the Pima CIS 129/185 instructor). Willamette path: open the **Kitada Smalley** conversation and scout the **Chemeketa** partner.
7. **External letter-writers** — pick the strongest ≤5 from the pool (Oregon Tech, Willamette, Furman, Doğucu/Harvard, Bhalerao/Northeastern, Dogan/UNCW, plus the non-submitting home institution) and confirm them as Fall-2026 adopters; plus the **facilities letter** via Tyson (CyVerse/Jetstream2).
8. **Confirm the lean grant teams** — Cruze (co-PI, PESOSE; affiliation?), Markwart (senior, PESOSE), the IUSE co-PIs per anchor, and the evaluator (CRED at UArizona / external at Willamette). Everyone else stays a contributor — by design.

**Then (Fall 2026 → submission):**
9. **Run the pilots** — the two-year→four-year pipeline (Pima→UArizona or Chemeketa→Willamette) plus the four-year adopters — and **log each participant's involvement** for their letters.
10. **Write both proposals from the drafts** → submit **IUSE Level 1 (~Jan 20, 2027)** and **PESOSE Track 1 (Mar 2, 2027)**.

---

*Planning estimates and NSF dates should be re-verified against current solicitations before submission; entity/tax and IP specifics require counsel.*
