# EduCloud — Adopter & Letter-of-Collaboration Recruitment Kit

*Working document · June 2026 · the tool that turns your drafts into submittable proposals*

---

## Why this is the priority now

Both proposals are drafted. The binding constraint is no longer writing — it's people:

- **PESOSE Track 1 requires a minimum of three (up to five) letters of collaboration** from *external* users or contributors — not the team — and each must describe how they **have** used or contributed to EduCloud and **will continue** to. These letters only exist if real people use or contribute to EduCloud during the **Fall 2026 pilots**.
- **IUSE ESL Level 1** needs a committed **community-college / transfer partner** (co-PI or collaborator) to anchor the transfer-pathway study.

The honest version: this is an **adoption** task first and a letters task second. You cannot solicit a credible letter from someone who hasn't used or built on the project. So the work that starts now is getting the right people genuinely using and contributing — the letters follow in winter. Lead time is the whole point; that's why this comes before tightening budgets or building calendars.

---

## What each program actually requires

**PESOSE Track 1 — letters of collaboration (hard requirement).** Three to five, from current external users/contributors not related to the team. Each (≤ 2 pages, no required PAPPG format) must state: how they have contributed/used, how they will continue to contribute to the ecosystem's development, and their name, affiliation, and relationship to you. **Plus**, optionally, **one facilities letter** if EduCloud will rely on institutional infrastructure (e.g., CyVerse/ACCESS compute) after the award.

**IUSE ESL Level 1 — partner + participants.** A standard collaboration letter from a community-college/transfer partner, ideally as a co-PI or named collaborator, and the required **List of Project Participants** supplementary document. (IUSE doesn't mandate PESOSE-style substantive letters, but a real partner is the spine of the transfer framing.)

---

## Who to approach, and what role each plays

| Prospect type | Becomes | Serves |
|---|---|---|
| MESA cohort instructors / Educator Fellows | Pilot users | PESOSE user-LOCs; IUSE pilot sites |
| A community college / transfer-serving program | Partner (co-PI/collaborator) + pilot | **IUSE partner** + PESOSE user-LOC |
| Carpentries / RSE community members | Contributors | PESOSE contributor-LOCs |
| Privacy-/sovereignty-sensitive departments; Forgejo/GitLab self-hosters | Pilot users | PESOSE user-LOCs |
| 1–2 developers (good-first-issues, the GitLab adapter) | Contributors | PESOSE contributor-LOCs |
| UArizona / CyVerse infrastructure contact | Facilities provider | PESOSE facilities LOC |

Aim to line up **8–10 prospects** to reliably yield the 3–5 PESOSE letters plus the IUSE partner — some won't convert, and you want users *and* contributors represented.

---

## Recruitment timeline (now → submission)

- **Jun–Aug 2026.** Identify 8–10 prospects from the table above. Send outreach (templates below). Confirm Fall 2026 pilot courses and 1–2 contributors. Open the community-college partner conversation. Identify the facilities-letter contact.
- **Sep–Dec 2026.** Pilots run; contributors land first pull requests; you gather usage and nurture the relationships. Keep light notes on what each person actually did — you'll hand it back to them when requesting letters.
- **Dec 2026–Jan 2027.** Request the IUSE partner letter; **submit IUSE (≈ Jan 20)**.
- **Jan–Feb 2027.** Request the 3–5 PESOSE letters — now backed by real Fall use/contribution — and the facilities letter; **submit PESOSE (Mar 2)**.

---

## Templates

*(Replace `[brackets]`; keep them short — short asks get answered.)*

### 1 — Pilot-adopter outreach (instructor)

> **Subject:** Piloting an open-source GitHub Classroom replacement this fall?
>
> Hi `[Name]`,
>
> With GitHub Classroom shutting down this August, I've built `[EduCloud]` — an open-source, self-hostable autograder for version-controlled assignments that, unlike the commercial replacements, keeps student data out of any third-party platform. I'm running pilots this fall and would love to include `[your course / your program]`.
>
> I'd handle setup and support; you'd get autograded assignments, no per-seat cost, and student records that stay yours. Could we grab 20 minutes `[this week / next]`?
>
> (If it works well for you, I may later ask for a brief letter of collaboration for an NSF proposal — entirely optional, and only if you've found it useful.)
>
> Thanks, `[Greg]`

### 2 — Contributor outreach (RSE / developer)

> **Subject:** Contributing to `[EduCloud]` (open-source autograding)?
>
> Hi `[Name]`,
>
> `[EduCloud]` is an open-source, host-agnostic autograder (AGPL/Apache, DCO) that works across GitHub, GitLab, and self-hosted Forgejo. I'm growing the contributor community ahead of an NSF ecosystem proposal, and thought `[the GitLab adapter / documentation / a good-first-issue]` might be up your alley.
>
> Repo and open issues: `[link]`. Happy to pair on a first PR if useful. If you end up contributing, I may later ask for a short letter of collaboration for the proposal.
>
> `[Greg]`

### 3 — Community-college / transfer partner (IUSE)

> **Subject:** Partnering on an NSF proposal — transfer pathways in computing
>
> Hi `[Name]`,
>
> I'm preparing an NSF IUSE proposal studying how an open-source, privacy-preserving autograding tool affects learning, engagement, and persistence in introductory computing — with a specific focus on two-year-to-four-year transfer students. Given `[your college's role in the transfer pipeline / your work with these students]`, I'd love to have `[you / your program]` as a partner: piloting in a course and helping shape the study, with `[co-PI effort / a subaward]` budgeted in the proposal.
>
> Could we talk in the next couple of weeks? The submission is in January, so there's time to design this together.
>
> `[Greg]`

### 4 — PESOSE letter-of-collaboration request (to an existing user/contributor)

> **Subject:** A favor — letter of collaboration for an NSF (PESOSE) proposal
>
> Hi `[Name]`,
>
> Thank you for `[piloting EduCloud in your fall course / your work on the GitLab adapter]`. I'm submitting an NSF PESOSE proposal (due March 2) to grow EduCloud into a sustainable, secure open-source ecosystem, and the program requires letters of collaboration from external users and contributors like you.
>
> Would you be willing to write a short one? It can be on your letterhead, **max two pages**, and should briefly cover:
> 1. how you've used or contributed to EduCloud,
> 2. how you plan to continue contributing to its development, and
> 3. your name, affiliation, and relationship to me/the team.
>
> To make it easy, I'll send a few bullets summarizing what you've done that you're welcome to draw from. I'd need it by `[date]`.
>
> Grateful for it — `[Greg]`

*(Then actually send them 3–4 bullets recapping their involvement. A scaffolded request gets a faster, stronger letter.)*

### 5 — Facilities letter request (UArizona / CyVerse)

> **Subject:** Facilities letter for an NSF PESOSE proposal — compute/infrastructure
>
> Hi `[Name]`,
>
> For my NSF PESOSE proposal I need a brief letter of collaboration describing the infrastructure EduCloud will rely on after the award — `[e.g., CyVerse/Jetstream2 compute and ACCESS allocations for sandboxed grading]`. Could you provide a short letter describing the extent and term of that provision? I can supply the specifics to reference. Needed by `[date]`.
>
> Thank you, `[Greg]`

---

## What makes a strong letter (and what sinks one)

**Strong:** specific about *actual* use or contribution (a course taught, a PR merged, an adapter tested); a concrete commitment to keep contributing; name, affiliation, and relationship stated; on letterhead. These read as evidence of a real ecosystem.

**Weak or risky:** a vague endorsement with no sign the writer has actually used the software; a letter from someone effectively on your team (reviewers will discount it, and PESOSE explicitly excludes related parties); identical boilerplate across letters. For PESOSE specifically, a letter that praises the *idea* but shows no *use or contribution* fails the requirement.

---

*Once outreach is in motion, the natural follow-on is a single funding-and-build calendar tying these letters, the two deadlines, the IP waiver, and the prototype into one sequenced view — the operational command sheet for the next 9 months.*
