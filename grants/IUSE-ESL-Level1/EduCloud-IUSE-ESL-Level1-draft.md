# IUSE: EDU — ESL Level 1 — Project Description (Working Draft)

**Solicitation:** NSF 23-510 (Improving Undergraduate STEM Education: EDU)
**Track:** Engaged Student Learning (ESL), **Level 1** · ≤ $400,000 · ≤ 3 years · Project Description limit: 15 pages (per PAPPG)
**Target deadline:** third Wednesday in January 2027 (~Jan 20, 2027)
**Status:** working draft · `[bracketed]` items are yours to supply · expand to 15 pages

---

## ⚠️ Compliance checklist

- [ ] All four IUSE "musts": strong rationale/evidence base; contributes to exemplary undergrad STEM ed; **adds to knowledge of what works**; measures progress
- [ ] The five expected **project elements** present (mapped in §§2–8): knowledge base; evaluation plan; research questions; dissemination plan; sustainability
- [ ] **Creative Commons license** on new instructional materials **and** an open IP license on code (IUSE requirement — EduCloud already complies; state it)
- [ ] **Evaluation plan** with dedicated personnel (external evaluator, qualified team member, or advisory board)
- [ ] Both merit criteria fully addressed: Intellectual Merit **and** Broader Impacts
- [ ] Supplementary docs: **Project Data Form** (DUE); **List of Project Participants** (name, affiliation, role; excludes PI/co-PI/senior personnel, students, and unnamed people)
- [ ] **IRB / human-subjects** plan for the education study (students as research participants)
- [ ] No student scholarships (not supported by IUSE); cost sharing prohibited; F&A at negotiated rate (no cap)
- [ ] PI on ≤ 3 IUSE proposals this Oct 1–Sep 30 window

---

## Title

**IUSE ESL Level 1: Learning in the Open — Privacy-Preserving, Version-Controlled Autograding to Improve Engagement and Persistence in Introductory Computing, with a Two-Year–to–Four-Year Transfer Focus**

*(Working title. Swap project name once settled.)*

---

## Project Summary (1 page — separate NSF document; draft below)

**Overview.** Introductory computing and data-science courses increasingly rely on automated assessment, yet the dominant tool for distributing and autograding version-controlled assignments — GitHub Classroom — was decommissioned in 2026, and the commercial replacements are hosted, per-seat services that place student data in third-party platforms. This Engaged Student Learning Level 1 project develops, adapts, and studies an alternative pedagogy built on EduCloud, an open-source system that delivers assignments through authentic version-control workflows, returns rapid formative autograded feedback, and is engineered so student personal data never enters the system. The project pilots this pedagogy in introductory computing/data-science courses at `[a four-year institution and a partnering community college]` and studies its effect on student learning, engagement, persistence, and help-seeking, with particular attention to two-year-to-four-year transfer students.

**Intellectual Merit.** The project generates knowledge about how rapid formative feedback, authentic version-control practice, and a privacy-preserving (non-surveilling) assessment environment — with optional AI tutoring used as formative scaffolding — affect learning, engagement, and persistence in introductory computing, and whether a portable, shared assignment system supports continuity for transfer students. As an early-stage, exploratory study adapting evidence-based feedback and mastery pedagogies to a novel learning system, it adds transferable evidence to computing-education research.

**Broader Impacts.** A free, self-hostable, privacy-preserving learning system lowers cost and surveillance barriers for under-resourced institutions and vulnerable students, and is studied explicitly in a community-college and transfer context. New instructional materials are released under Creative Commons and the platform under an open license, enabling adoption and replication across institution types, and the work supplies a graded, version-controlled assignment layer for national data-science workforce training.

`Keywords:` computing education; formative feedback; autograding; transfer pathways; broadening participation

---

## Project Description (15 pages)

### 1. Motivation, rationale, and goals

Automated assessment of code — autograding — has become central to scalable, high-feedback instruction in computing and data science. Until 2026 the dominant tool for distributing and autograding version-controlled assignments was GitHub Classroom; its decommissioning forces hundreds of programs to adopt new tools, and the replacements they are being directed toward are commercial, hosted, per-seat services that store student work and identity in third-party platforms. This moment is both a disruption and an opportunity: a chance to ask not merely *which tool replaces the old one*, but *what pedagogy and what learning environment best serve students* — especially students for whom cost, data surveillance, and discontinuity across institutions are real barriers.

This project develops, adapts, and studies an Engaged Student Learning approach built on **EduCloud**, an open-source assignment-distribution and autograding system [1] designed around three pedagogically consequential properties: (a) students do authentic work in version-controlled repositories, the same practice used in professional software and data work; (b) submissions receive rapid, iterative, per-test formative feedback with the ability to revise and re-submit; and (c) the system is engineered so that student personal data never enters it — there is no proctoring, no surveillance dashboard, and identity is minimized by design. An optional tutoring layer offers formative scaffolding and is never the basis of a grade. Because the system is free and self-hostable, it is accessible to community colleges and under-resourced programs that cannot adopt per-seat commercial tools.

The project's goals are to (1) adapt and implement this pedagogy in introductory computing/data-science courses across institution types, (2) study its effect on learning, engagement, persistence, and help-seeking, with explicit attention to two-year-to-four-year transfer students, and (3) generate transferable knowledge and openly licensed materials that other programs can adopt and replicate. This is appropriate for ESL Level 1 as an early-stage, exploratory study and an adaptation of evidence-based pedagogies in novel environments and on a small scale, and it directly instantiates two approaches the solicitation names: investigation of a novel instructional learning system (cyberlearning), and a collaboration between two-year and four-year institutions supporting transfer pathways.

### 2. Knowledge base for the project

The design is grounded in established findings that the project adapts to a new learning system and studies in a new population.

- **Formative feedback and frequent low-stakes practice** improve learning when feedback is timely, specific, and revisable `[Black & Wiliam 1998; Shute 2008]`. Autograding operationalizes this at scale by shortening the feedback loop and enabling iteration; reviews of automated feedback in computing education document both benefits and design pitfalls `[Keuning et al.; Messer et al. systematic review of autograding]`.
- **Mastery- and specifications-oriented assessment** — revise-and-resubmit toward a standard — supports persistence and reduces the penalty of early failure `[Bloom mastery learning; Nilson, specifications grading]`.
- **Authentic version-control practice** in coursework builds transferable professional competence and is increasingly expected in computing/data-science curricula `[citations]`.
- **Surveillance, privacy, and affect**: proctoring and surveillance-heavy environments are associated with student anxiety and inequitable effects on marginalized students; reducing surveillance is plausibly protective of belonging and engagement `[citations]`.
- **Transfer-student success and equity in computing**: two-year-to-four-year transfer students face discontinuities in tools, expectations, and belonging; computing education exhibits persistent equity gaps `[Margolis & Fisher; transfer-pathway literature]`.
- **Edtech adoption and equity**: technology amplifies existing pedagogy and capacity rather than substituting for them, which motivates a design that lowers activation energy for good practice and is studied in real, varied classrooms `[Reich, Failure to Disrupt; Toyama]`.
- **Prior NSF work**: the PI's `[IUSE: Quantum Inventioneers]` and role in the NSF `[MESA]` cyberinfrastructure project provide relevant track record, infrastructure, and a workforce-training context. `[Summarize relevant findings and lessons learned.]`

The gap this project addresses: the above pedagogies are well-evidenced individually, but their combination in a *privacy-preserving, self-hostable, version-control-native* learning system — and their effect on transfer and community-college students specifically — is not established.

### 3. Project design and activities

**The pedagogy under study.** Across participating courses, instructors deliver assignments through EduCloud so that students (a) work in individual version-controlled repositories; (b) receive rapid per-test formative feedback and may revise and re-submit toward mastery; (c) work in an environment with no surveillance and no collection of personal data; and (d) may opt into formative AI tutoring that scaffolds but never grades. Instructor practices and assignment designs are adapted collaboratively, not imposed, recognizing that the tool amplifies existing pedagogy.

**Implementation and adaptation across settings.** The pedagogy is implemented in introductory computing/data-science courses at `[the four-year institution]` and adapted at `[a partnering community college / transfer-serving program]`, supported by the Fall 2026 / Spring 2027 pilots that also yield preliminary data. The cross-setting design tests transferability into a novel environment and foregrounds the two-year-to-four-year pathway: shared, portable assignment and feedback structures are studied as a mechanism for continuity for transfer students.

**Engaged student learning focus.** Activities target engagement and learning directly (iterative feedback, authentic practice, reduced-anxiety environment) and indirectly (light-touch instructor professional development and shared assignment designs).

### 4. Research questions

The study poses aligned, answerable questions:

- **RQ1 (learning & persistence).** How does EduCloud-enabled formative, revisable autograded feedback with authentic version-control practice affect student learning outcomes and course persistence in introductory computing/data science?
- **RQ2 (privacy, anxiety, belonging).** Does a privacy-preserving, non-surveilling assessment environment affect student anxiety, sense of belonging, and engagement — and do effects differ for first-generation, transfer, and historically underrepresented students?
- **RQ3 (AI scaffolding).** When the optional tutor is used as formative scaffolding, how does it affect help-seeking and learning, and under what conditions is it beneficial versus counterproductive?
- **RQ4 (transfer continuity).** How does a shared, portable assignment/feedback system relate to two-year-to-four-year transfer students' continuity, preparedness, and success?

Each question is answerable through data generated by the project (course-performance data, validated surveys, platform interaction logs, and interviews), consistent with NSF's expectation that knowledge be generated through study and/or evaluation.

### 5. Evaluation plan

`[External evaluator — name/role — secure before submission]` will lead formative and summative evaluation, distinct from but complementary to the research questions, with dedicated effort. The mixed-methods design includes: pre/post measures of learning (course assessments and, where available, a validated concept inventory); persistence and completion metrics; validated surveys of engagement, belonging, and anxiety; platform interaction and help-seeking logs; and instructor and student interviews. Analyses disaggregate outcomes by transfer status, first-generation status, and demographic group to surface differential effects. Formative evaluation feeds back into instructor practice and assignment design each term; summative evaluation assesses goal achievement and outcomes. The data-management and analysis plan specifies instruments, timeline, and methods, and the study will be pre-registered `[OSF]` where appropriate.

### 6. Broadening participation

Equity is the project's organizing concern, not an addendum. The community-college and transfer focus targets the populations where computing-education gaps are widest; the privacy-preserving design is protective of vulnerable students; and the free, self-hostable model removes a cost barrier that excludes under-resourced institutions from current tools. The PI's own community-college/transfer background informs the design and partnerships. `[Name partner institutions and the transfer pipeline.]` The work aligns with national STEM talent-development goals and supplies infrastructure for data-science workforce training reaching `[MESA]` audiences.

### 7. Dissemination plan

Findings and materials reach researchers and educators through: presentations at SIGCSE, PEARC, and `[JupyterCon]`; publications in computing-education and STEM-education venues; engagement with the Carpentries and research-software-engineering communities; and study registration. Consistent with IUSE requirements, **new instructional materials are released under a Creative Commons license and the platform under an open-source license** (the project's software already uses an AGPL-3.0/Apache-2.0 split with documentation under Creative Commons) — enabling adoption, adaptation, and conceptual replication across institution types.

### 8. Sustainability

Project efforts persist beyond the award through deliberate design. The software is open-source, modular, self-hostable, and low-cost, with adopter compute met through national cyberinfrastructure rather than purchased hardware — so continuation does not depend on this award's budget. Longer-term stewardship is being established through a separate effort to form a managing organization and sustainability model for the open-source ecosystem `[cross-reference the PESOSE Track 1 effort]`, and through institutional adoption and a contributor community. Instructional materials, released openly, remain available and adaptable independent of the platform's evolution.

### 9. Team and qualifications

`[PI name]` is `[Assistant Professor of Practice and Faculty Director of Instructional Computing]`, leads training/education for the NSF `[MESA]` project, holds prior NSF education funding `[IUSE: Quantum Inventioneers]`, built the EduCloud prototype, and brings a community-college/transfer background central to the project's equity aims. The funded team is deliberately lean: a transfer-success / data-science-education research co-PI `[UArizona anchor: R. Deil-Amen — transfer-student-success research, the Pima–UArizona STEM Bridge · Willamette anchor: H. Kitada Smalley — data-science-education research, experimental design, prior $2M federal education grant]`; a community-college partner co-PI `[UArizona anchor: Pima CC, the CIS 129/185 intro-Python sequence · Willamette anchor: Chemeketa CC, the Salem-area transfer pipeline]`; and an external evaluator `[UArizona anchor: the CRED team · Willamette anchor: external evaluator TBD]` — the cross-role collaboration (instructors, administrators, education researchers) that IUSE values. Unfunded contributors across adopting institutions deepen specific threads `[e.g., L. Cordova — guardrailed-LLM tutoring research — and F. Agbo — intro-Python pedagogy and broadening participation — at Willamette; M. Doğucu (Harvard); R. Bhalerao (Northeastern); G. Dogan (UNCW); W. Burleson (UArizona)]`. `[Write the final text to the submitting anchor: UArizona near-term; Willamette after the flagship shift.]`

### Intellectual Merit and Broader Impacts (explicit statement)

**Intellectual Merit.** The project advances understanding of how formative, revisable feedback; authentic version-control practice; a privacy-preserving learning environment; and optional AI scaffolding jointly affect learning, engagement, and persistence in introductory computing — and whether portable shared infrastructure supports transfer-student continuity. It contributes transferable, openly disseminated evidence and instruments to computing- and STEM-education research.

**Broader Impacts.** Improved learning and persistence for under-served computing students; a free, privacy-preserving learning system adoptable by community colleges and under-resourced programs; explicit study and support of two-year-to-four-year transfer pathways; openly licensed materials enabling replication; and contribution to national data-science workforce development and broadening participation.

---

## Timeline (3 years)

| Year | Activities | Data / deliverables |
|---|---|---|
| 1 | Adapt pedagogy and assignment designs; baseline; first implementation at both sites; instrument and IRB setup | Baseline data; instruments; formative findings |
| 2 | Full implementation across settings; iterate; mid-study analysis | Learning/persistence/engagement data; interim report; conference presentation |
| 3 | Final implementation; summative analysis; dissemination; openly licensed materials released | Summative findings; publications; released materials and study registration |

---

## References Cited (illustrative — complete and verify before submission)

1. EduCloud open-source repository. `[in-line citation; repository identifier in References — no URL in body]`
2. `[Black & Wiliam (1998), formative assessment]`
3. `[Shute (2008), focus on formative feedback]`
4. `[Keuning et al. / Messer et al., automated feedback & autograding reviews]`
5. `[Nilson, specifications grading; Bloom, mastery learning]`
6. `[Margolis & Fisher, equity in computing]`
7. `[Reich, Failure to Disrupt]`
8. `[Transfer-pathway / community-college success literature]`
9. `[GitHub Classroom sunset announcement, 2026]`

---

## What's still on you before this is submittable

1. **External evaluator** — name + a short evaluation design with dedicated budget (required).
2. **Community-college / transfer partner** — a committed partner institution and instructor, and a collaboration plan (the heart of the transfer-pathway framing). `[UArizona anchor: Pima CC — get the CIS 129/185 instructor via E. Halvorson-Otts · Willamette anchor: identify the Chemeketa CC partner.]` A multi-institution version would be a collaborative proposal.
3. **IRB / human-subjects plan** — the study involves students as research participants; line up IRB review early.
4. **The ≤ $400K / 3-yr budget** — see the companion budget file; it is intentionally *leaner* than the multi-year operating model (a single IUSE Level 1 is ~$133K/yr).
5. **Supplementary documents** — Project Data Form (DUE) and List of Project Participants.
6. **Complete the literature base** — replace bracketed citations with the actual evidence you'll build on, including a real summary of your prior NSF work.
7. **Fill every `[bracket]`** and expand to the 15-page limit.

> **On PESOSE vs IUSE:** these are complementary, not redundant. PESOSE funds the *ecosystem* (governance, security, sustainability); IUSE funds the *learning research* (does this pedagogy improve outcomes?). They can share infrastructure and pilots but must tell different stories to different review panels — which these two drafts do. Note the 3-proposal-per-year IUSE limit if you submit other IUSE proposals.
