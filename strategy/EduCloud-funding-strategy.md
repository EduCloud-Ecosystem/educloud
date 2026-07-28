# EduCloud — Diversified Funding Strategy

> **Name note (July 2026).** Module names have settled
> (Cairn/Belay/Waypoint/Portage/Outfitter) — see `SYSTEM.md` §1; prior names
> (Quad/Sol/Commons/claude-lanes/HOST) appear below unrevised.

*June 2026 · ranked by viability, not by lane · companion to the business plan and financial model*
*Updated July 2026: master funding calendar added (§2); PESOSE corrected to the confirmed NSF 26-506 Track 1 deadline of March 2, 2027; NLnet call cadence and Spencer cycle added from funder sites.*

## 0. The problem this solves

The current plan leans on NSF for nearly all major lifting (IUSE → PESOSE → IDSS). That's a concentration risk on one funder in a turbulent federal environment — slow cycles (6–9 months to decision), low hit rates (~20–30%), and political exposure. The fix is a portfolio: several independent lanes, each viable on its own, sequenced so that cheap, fast asks come first and no single rejection is fatal. NSF stays in the plan — it just stops being the plan.

**One dependency first:** most private foundations can only grant to a 501(c)(3) vehicle. The **fiscal sponsor** (Open Source Collective / Software Freedom Conservancy) is therefore not just an entity formality — it is the key that unlocks the entire philanthropy lane. It moves further up the critical path.

---

## 1. The lanes, ranked by viability

### Lane A — Science/OSS philanthropy: **Sloan Foundation** (highest near-term priority)

The Alfred P. Sloan Foundation runs active programs squarely on EduCloud's mission: its **Open Source in Science** program funds "tooling, institutions, economic models, and incentives around the production, maintenance, and adoption" of open source in research — explicitly *not* individual dev projects but the institutions and practices around them, which is exactly what the EduCloud foundation + Registry + training story is. Its sister **Better Software for Science** program covers the same ground from the software-practice side, and Sloan has funded **university OSPOs at ~$685–750K over two years** (Johns Hopkins, GW, RIT, SLU — the JHU OSPO got a fresh $750K in *January 2026*, so the program is alive right now).

- **Why it's the top pick:** the entry cost is a **two-page letter of inquiry** to technology@sloan.org, rolling, no deadline. Highest expected value per hour of effort of anything on this list. Sloan money also de-risks you in NSF reviewers' eyes (it reads as external validation).
- **Two distinct asks possible:** (1) the EduCloud managing organization / Registry as open-science infrastructure (via the fiscal sponsor); (2) an **OSPO-flavored institutional grant** through your university — at Willamette, "stand up the OSPO for a new School of Computing, with EduCloud as its anchor project" is precisely the institutional-ecosystem story Sloan's OSPO program funds, and it doubles as your faculty-pitch capacity-building story.
- **Realistic size/odds:** $250–750K / 2 yrs; LOI-to-grant odds for a well-matched project are materially better than NSF panel odds, and you learn fast.

### Lane B — Earned revenue (the only lane you fully control)

This is the lane that makes the foundation *durable*, and there's a fresh, directly-on-point precedent: **CUNY's Transfer Explorer in 2026 moved from a fully grant-funded pilot to a grant-subsidized paid service, run on a nonprofit basis, with the Gates Foundation paying first-year onboarding fees for new institutions.** That is exactly EduCloud's model: open core, self-host free forever, and a hosted/managed tier whose early adopters are subsidized by philanthropy until fees carry it. The closest operating comp is **2i2c** (nonprofit managed JupyterHub for universities — grants + service fees); the **Carpentries** (workshop fees + institutional memberships) is the model for the training side.

Concrete revenue products, in order of how soon they can exist:
1. **GHC migration services** (now → Fall 2026): paid migration assistance while the Aug 28 sunset panic is live. Small dollars, but immediate, and every engagement creates an adopter, a case study, and a letter.
2. **Hosted tier** (2027): managed EduCloud for departments with no IT capacity — priced per-course or per-institution; philanthropy-subsidized onboarding for under-resourced institutions (the Transfer Explorer/Gates pattern, and it *solves your own Matthew-Effect worry* rather than fighting it).
3. **Institutional memberships / consortium** (2027+): Carpentries-style annual memberships granting support, governance voice, and training seats.
4. **Training revenue**: paid instructor workshops (you already run Carpentries pedagogy through MESA).
5. **Support contracts** for self-hosters (SLAs for institutions that want self-host + a throat to choke).

Honest sizing: $10–50K in year one, $75–250K/yr by year three if the hosted tier lands. Not fast money — but it's *unrestricted*, compounding, and the thing every funder asks about ("what's your sustainability model?") becomes an answer you're already executing.

### Lane C — Education philanthropy (the IUSE-thesis funders, without the federal cycle)

Three funders map almost one-to-one onto EduCloud's education thesis:

- **ECMC Foundation** — one of the only national funders focused *exclusively* on postsecondary success for underserved students, with **transfer** as a named priority (they publish the "Transfer Playbook"); typical grants $500–800K; funds capacity building, model development, research/evaluation; also has a venture arm if a service entity ever emerges. The Pima→UArizona / Chemeketa→Willamette pilots with equity outcomes are a textbook ECMC concept paper.
- **Ascendium Education Group** — large ($58M+ rounds), funds community-college infrastructure, evidence-based postsecondary practice, **and postsecondary education in prison** — meaning the Design-E carceral vision, which today is only a talk-track, has a named funder lane when it matures. Offline-capable, self-hosted, privacy-preserving infrastructure is a genuine differentiator in the prison-education space (connectivity and surveillance constraints are the central technical problem there).
- **Gates Foundation (postsecondary success)** — funds transfer-credit infrastructure at scale and, per Transfer Explorer, will *pay onboarding fees* for institutions adopting nonprofit ed-infrastructure services. Hardest of the three to cold-approach; usually arrives via intermediaries (Ithaka S+R, CCRC, Aspen) — which is a reason to publish the pilot results where those intermediaries will see them.
- Also real, second-ring: **Hewlett (Open Education)** — funds OER infrastructure and practice, and recently funded BCcampus work that includes **an AI tutor for openly licensed materials** (precedent for the tutor under open-education framing; EduCloud's CC-licensed materials requirement makes it eligible); **Lumina** (attainment/equity); **Spencer** (education research, small grants ~$50K — could fund the learning-outcomes study independent of IUSE); **Michelson 20MM** (open courseware + smart justice — small, but sits exactly at the OER×carceral intersection).

Timing: these funders want *evidence*, so the right ask follows the Fall 2026 pilot — concept papers out in **Spring 2027** with pilot data. Typical award $250K–$750K, decision in 3–5 months (half the NSF cycle).

### Lane D — Federal, kept but right-sized

- **NSF IUSE (~Jan 20, 2027) and PESOSE Track 1 (Mar 2, 2027)** stay exactly as planned — they're well-matched and the proposals are drafted. The change is framing: they're now two shots out of many, not the spine.
- **Dept. of Education (FIPSE / IES)** — a possible lane for the transfer/pilot work, but discretionary ED programs are at least as politically exposed as NSF right now; monitor, don't depend.
- **ACCESS / Jetstream2** — in-kind compute; already planned; effectively removes the infrastructure line from every budget, and (July 2026 update) doubles as the fall test substrate for the component and full-implementation test gates.
- Rule of thumb going forward: **federal ≤ 50% of any year's budget** once other lanes open.

### Lane E — OSS-infrastructure funds (honest assessment: mostly *later*)

- **Sovereign Tech Agency** (Germany; ~€25M deployed) funds *foundational, widely-depended-on* open components — an application-layer education platform isn't that today. Revisit if/when a Registry metadata standard or the grading-spec becomes shared infrastructure other projects depend on. Their **Fellowship** (maintainer funding; 2026 round closed in April) is a future option for a maintainer, not the org.
- **NLnet / NGI Zero Commons Fund** — funds open-internet commons projects worldwide in €5–50K slices; plausible for a *specific* privacy or federation component (e.g., the privacy-preserving roster protocol), not core operations. Cheap to apply; worth one targeted shot in 2027. **Call cadence (verified July 2026): open calls recur roughly every two months — the current call closes August 1, 2026, with subsequent calls expected October 1 and December 1 and onward.** Target the first call after the Registry MVP ships.
- **GitHub Accelerator / Open Source Pledge / OpenSSF** — monitor; episodic and crowded.
- Net: this lane is real but **structurally mid-2027+** for EduCloud. Don't spend summer 2026 here.

### Lane F — Strategic/corporate (distribution and in-kind more than dollars)

- **GitLab** is the interesting one: every GHC refugee EduCloud routes onto a GitLab adapter is a GitLab win. Their education program + open-source partnership channel could yield sponsorship, credits, co-marketing — and it directly funds the *GitLab adapter* work. Worth a conversation the moment the adapter ships (July 2026 note: the adapter has shipped; open the conversation).
- **Cloud credits** (AWS Educate, Google, Azure, DigitalOcean OSS credits) — standard, stackable, in-kind; apply once the hosted pilot starts.
- **GitHub "partner solution" listing**: GitHub is actively steering retiring-Classroom users to named partner solutions. Getting EduCloud listed is distribution, not dollars — but it may be worth more than a grant. Investigate the listing criteria now, before the sunset.
- **Crowd/community** (Open Collective, GitHub Sponsors): turn on at fiscal-sponsor launch; expect noise-level dollars ($5–20K/yr) but maximal optionality — and funders read a healthy donor count as community proof.

---

## 2. The funding calendar — every date in one place

*Chronological. Dates marked [verify] should be re-checked on the funder's site the week you act; NSF internal deadlines follow UArizona OSP practice of 3–5 business days before the sponsor deadline (see `grants/PESOSE-Track1/SEPTEMBER-sprint-plan.md` §Deadline math).*

| Date | Program / action | Amount | Status & notes |
|---|---|---|---|
| **Rolling — send now (Jul 2026)** | Sloan Open Source in Science LOI (technology@sloan.org) | ask $450K / 24 mo | Drafted (`foundations/Sloan-OpenSource-in-Science-LOI.md`); no deadline; fiscal-sponsor application should be in progress |
| **Now (~2-week turnaround)** | NSF ACCESS Discover allocation | in-kind compute | Removes compute lines from both NSF budgets; fall test substrate for JS2 test gates |
| **Before Aug 28, 2026** | GitHub partner-solution listing inquiry; GHC migration-services window opens | distribution / first revenue | Criteria to investigate now; sunset panic is the market moment |
| **Aug 1, 2026** (then ~every 2 months: Oct 1, Dec 1, …) | NLnet NGI Zero Commons Fund open-call closes | €5–50K (ask €42K) | Skip 2026 calls; target the first 2027 call after the Registry MVP ships [verify call dates at nlnet.nl] |
| **Fall 2026** | Cloud-credit applications (AWS / Google / Azure / DigitalOcean OSS) | in-kind | File when the hosted pilot starts |
| **Fall 2026** | GitLab education/partnership conversation | sponsorship / in-kind | Adapter has shipped; open the conversation |
| **~Dec 15, 2026** | Internal milestone: both NSF packages complete for OSP review | — | Self-imposed; keeps January achievable |
| **~Jan 13–15, 2027** | UArizona OSP internal deadline for IUSE (3–5 business days prior) | — | Confirm with OSP early fall |
| **~Jan 20, 2027** [verify] | **NSF IUSE: EDU — ESL Level 1** (NSF 23-510, January window) | ≤$400K / 3 yr (~$399K drafted) | Draft + budget written; anchor pair to finalize by Dec |
| **~Feb 23–25, 2027** | UArizona OSP internal deadline for PESOSE | — | Confirm with OSP early fall |
| **Mar 2, 2027** | **NSF PESOSE Track 1** (NSF 26-506) | ≤$300K / 1 yr (~$290K drafted) | Draft + budget written; reframed from the abandoned Sept 1, 2026 acceleration |
| **Spring 2027** (with pilot data) | ECMC concept paper | ask $550K / 30 mo | Drafted; 3–5 mo decision cycle; fiscal sponsor required |
| **Spring 2027** (with pilot data) | Ascendium concept paper | ask $650K / 36 mo | Drafted; warm path preferred |
| **Spring 2027** (with pilot data) | Hewlett Open Education LOI | ask $300K / 24 mo | Drafted; invitation-driven — route via OER community warm intro |
| **~Apr 15, 2027** [verify] | Spencer Small Research Grants (spring cycle; ~3 cycles/yr) | ≤$50K / 18 mo | First cycle after pilot data; university as grantee; check spencer.org/application-deadlines |
| **Mid-2027** | Hosted-tier design; Gates via intermediaries (Ithaka S+R / CCRC / Aspen) | onboarding-fee model | No deadline; published pilot results are the entry ticket |
| **2027, first call post-Registry-MVP** | NLnet NGI application | €42K | Drafted (`foundations/NLnet-NGI-application.md`) |
| **Conditional** | Sloan OSPO institutional LOI (Willamette) | ask $700K / 24 mo | Only after any move; institutional sponsorship required |
| **2028 cycle** [verify] | **NSF PESOSE Track 2** | ~$1.5M / 2 yr under predecessor-program parameters | Confirm Track 2 terms in NSF 26-506; positioning starts after Track 1 |
| **July cycle, year TBD** [verify] | NSF IDSS via MESA | — | From the team roadmap; verify solicitation and year |
| **Watch** | Sovereign Tech Fellowship (2026 round closed April) | maintainer funding | Watch for the 2027 round; org-level fit is still "not yet" |

---

## 3. The portfolio, sequenced

> Ready-to-adapt drafts for every grant ask below live in `grants/foundations/` (one file per solicitation, in each funder's expected format, with [verify] flags on process details).

| When | Action | Lane | Cost | Realistic outcome |
|---|---|---|---|---|
| **Now (June–July 2026)** | Fiscal sponsor application — *unlocks all philanthropy* | — | days | the 501(c)(3) vehicle |
| Now | **Sloan LOI** (2 pages, technology@sloan.org) — managing-org/Registry framing | A | ~2 days | invited full proposal at decent odds; feedback either way |
| Now | Investigate **GitHub partner-solution listing**; open **GitLab** conversation (adapter shipped) | F | hours | distribution; possible sponsorship |
| Now | Turn on **Open Collective / GitHub Sponsors** at sponsor launch | F | hours | trickle + community signal |
| **Fall 2026** | Run pilots; sell **GHC migration services** around the Aug 28 sunset | B | built-in | first revenue + adopters + letters |
| Fall 2026 | Apply for **cloud credits**; file ACCESS (already planned) | F/D | hours | in-kind infrastructure |
| **~Jan 20, 2027** | **IUSE Level 1** (NSF 23-510) — first federal shot | D | drafted | decision mid/late 2027 |
| **Mar 2, 2027** | **PESOSE Track 1** (NSF 26-506) — second federal shot | D | drafted | funds governance/sustainability incl. the foundation decision |
| **Spring 2027** | **ECMC + Ascendium concept papers** with pilot data; **Hewlett** if the tutor/OER framing is ready; **Spencer** small grant (~Apr 15 cycle) for the learning study | C | ~2 wks each | 3–5 month decisions, $250–750K class |
| Spring 2027 | If at Willamette: **Sloan OSPO-track institutional ask** | A | with the university | $500–750K class, institutional |
| **Mid-2027** | Design the **hosted tier** with philanthropy-subsidized onboarding (Transfer Explorer model); pitch Gates *via intermediaries* with published pilot results | B/C | real product work | the sustainability engine |
| 2027+ | **NLnet** targeted component ask (first call after Registry MVP); **Sovereign Tech** only if a component becomes shared infrastructure; **PESOSE Track 2 / IDSS** as planned | E/D | modest | upside, not load-bearing |

## 4. What this does to the risk profile

Under the NSF-only plan, a bad day at two panels (a ~50–65% joint-failure scenario at typical hit rates) leaves the project on personal time and MESA scraps until 2028. Under the portfolio: Sloan is decided *before* the NSF submissions (and strengthens them); migration-services revenue and donations exist regardless of any panel; ECMC/Ascendium decisions land mid-2027 on independent criteria; and the hosted tier compounds quietly underneath. The realistic failure mode shifts from "no funding" to "slower than hoped" — which the bootstrap (MESA appointment + personal time + ACCESS compute) already covers.

Three honest caveats. First, philanthropy is relationship-driven: the LOIs are cheap, but the grants follow conversations, intermediaries, and published results — budget Cruze's time for cultivation, not just writing. Second, earned revenue is slower and harder than every plan assumes; treat year-one numbers as learning, not budget. Third, several funder details above (program status, typical sizes, deadlines) move constantly — re-verify each against the funder's site the week you act on it; the calendar in §2 marks the entries most likely to move.

## 5. The one-paragraph version

File the fiscal sponsorship now because it unlocks everything else; send the two-page Sloan LOI this month because it's the highest-EV ask in the field and it's essentially free; sell migration help during the GHC sunset because it converts the market moment into revenue, adopters, and letters at once; submit IUSE (Jan 20, 2027) and PESOSE Track 1 (Mar 2, 2027) as planned but as two bets among many; take pilot data to ECMC, Ascendium, Hewlett, and Spencer in Spring 2027 where the decision cycles are half NSF's; and build the philanthropy-subsidized hosted tier on the Transfer Explorer precedent so that by 2028 the foundation has an engine that doesn't ask anyone's permission.
