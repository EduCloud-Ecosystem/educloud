# EduCloud: Orientation for John Chen

> **July 2026 correction.** PESOSE Track 1 is NSF 26-506, deadline **March 2,
> 2027**; September 1, 2026 references below are superseded. Module names have
> settled (Cairn/Belay/Waypoint/Portage/Outfitter) — see `SYSTEM.md`; prior
> names (Quad/Sol/Registry/Commons) appear below unrevised.

*A read-in for early collaboration. June 2026.*

This orients you on EduCloud: what it is, where it stands, the timeline, and the grant strategy. It also flags the one decision where your read would be most valuable, which is whether to take PESOSE Track 1 to the September 2026 deadline rather than March 2027. It is meant to stand on its own. The deeper documents it points to are in the shared folder if you want them. Section 5 is the one to read closely.

## 1. What EduCloud is

On August 28, 2026, GitHub retires GitHub Classroom, the tool thousands of computing and data-science courses use to distribute, collect, and autograde version-controlled assignments. GitHub is steering instructors toward commercial replacements, and no community-governed open alternative exists. That is the opening.

EduCloud is an open-source, self-hostable, Git-host-agnostic successor. It is licensed AGPL-3.0 at the core, with Apache-2.0 interoperability primitives. It handles assignment distribution, collection, and sandboxed autograding, and it rests on five load-bearing principles:

- **Pluggable host adapters** (GitHub and Forgejo are done, GitLab is next), so it is never locked to one forge.
- **Privacy by architecture.** It stores Git usernames, never student records, which removes the FERPA and data-sharing negotiation that kills most cross-institutional tooling.
- **Self-hostable first:** one operator, commodity hardware, one-command deploy.
- **Portable sandboxed autograding.**
- **No lock-in,** through export and import and open formats.

On top of the core sits the EduCloud Registry, Ben Markwart's contribution. It is a lightweight, self-hostable catalog and metadata standard that makes courses, assignments, datasets, and artifacts discoverable across institutions. It federates mature open systems (Coolify for hosting, Keycloak for identity, JupyterHub later) behind thin adapters rather than rebuilding them.

The IP is held by an independent nonprofit, a fiscal sponsor now and a 501(c)(3) later, not the university. It was built on personal time and is deliberately portable and genuinely community-owned.

## 2. Where it stands (June 2026)

Honest status: a working prototype, not yet a shipped 1.0. Adoption is committed but not yet demonstrated.

- **Core.** The GitHub and Forgejo adapters are complete and live-validated, which proves the host-agnostic thesis end to end. The durable embedded store, provisioning worker, and OAuth all work. The 1.0-beta is targeted for the end of summer 2026 (webhook grading, GitLab adapter, dashboard, one-command deploy, GHC import).
- **Registry and hosting.** Scoped. Coolify is adopted as the hosting engine, reconciled from Ben's hosting proposals on the principle of adopting mature open source rather than hand-rolling. The Registry MVP is targeted for Fall 2026 as a workstream parallel to the core, so it never gates the 1.0.
- **Entity and team.** The founding team is in place: Greg (founder and technical lead), Ben Markwart (Registry, plus nonprofit board governance and legal), and Angela Cruze (nonprofit, grants, and program development). The fiscal-sponsor application and the UArizona IP waiver are both in progress.
- **Adoption.** Five faculty adopters across institution types (R1, liberal arts, regional public, and a community-college pipeline) are committed to Fall 2026 pilots, along with a two-year to four-year transfer pilot (Pima to UArizona via the STEM Bridge, or Chemeketa to Willamette).

## 3. Timeline

| Window | What happens |
|---|---|
| Summer 2026 | Ship 1.0-beta; secure IP waiver; fiscal sponsor; Registry workstream begins; PESOSE sprint |
| Sept 1, 2026 | Submit NSF PESOSE Track 1 (accelerated; see Section 5) |
| Fall 2026 | 1.0 GA; pilots run; Registry MVP; gather usage evidence and letters |
| ~Jan 20, 2027 | Submit NSF IUSE ESL Level 1 |
| 2027 and beyond | Federation breadth; foundation incorporated; possible flagship shift to Willamette |

## 4. Grant strategy and timeline

The recent change is moving off an NSF-only plan, which was a concentration risk in this environment, to a diversified portfolio in which NSF is two bets among many:

- **Sloan (Open Source in Science).** A two-page letter of inquiry, going out now. Highest near-term expected value. It funds the managing organization and the Registry-as-standard rather than features.
- **Earned revenue.** GHC migration services now, and a philanthropy-subsidized hosted tier later, on the model CUNY's Transfer Explorer validated in 2026.
- **Education philanthropy.** ECMC, Ascendium, Hewlett, and Spencer, with Fall 2026 pilot data, in Spring 2027.
- **NSF, your lane.** IUSE ESL Level 1 (about $400K over three years, around January 2027), anchored on the transfer-bridge learning study. PESOSE Track 1 (about $300K over one year, the planning grant for the managing organization), now accelerated to September 2026.
- **Later:** NLnet for a Registry-standard component, then PESOSE Track 2 or NSF IDSS via MESA.

Full detail is in `funding-strategy.md`. The drafted PESOSE Track 1 Project Description and budget are in `grants/PESOSE-Track1/`, and `grants/foundations/` holds the non-NSF drafts.

## 5. The decision where your read matters most. PESOSE Track 1: September 2026 or March 2027?

Our plan was March 2, 2027. We are now preparing for the earlier September 1, 2026 deadline instead, on one assumption that we need you to confirm: that forward-looking letters of collaboration from committed adopters satisfy a Track 1 planning proposal. You have run a recent award in this program, so your read settles it.

Why we had defaulted to March: Track 1 requires at least three external letters of collaboration from users or contributors outside the team, each stating how they have used or contributed and how they will continue. We judged that we could not show demonstrated usage before the prototype ships in late summer and the Fall pilots run.

Why September now looks viable, and where your experience is decisive:

- Track 1 is a planning and scoping grant (ecosystem discovery, organization and governance, risk and security plan, community building). It is not a demonstration of a mature ecosystem, so the evidence bar may simply be lower than we assumed.
- The Project Description and budget are already drafted.
- The prototype should be demoable by late summer, and five adopters are already committed for Fall.
- If forward-looking letters, meaning committed pilot partners attesting they will adopt and test in the coming term, satisfy a Track 1 planning proposal, September is achievable.
- Acceleration. A September submission means roughly mid-2027 funding instead of roughly early 2028 for March. That is a six-to-nine-month head start on standing up the managing organization, during the exact window when the GitHub Classroom sunset is driving migration.

The case for holding to March, so you have both sides:

- Completed Fall pilots would yield letters describing demonstrated usage rather than intent, which is a materially stronger proposal.
- I-Corps is mandatory for Track 1 awardees, and the September runway to prepare it is tight (about eleven weeks total, alongside letters and supporting documents).
- A thin September attempt risks a weak first impression, though Track 1 is resubmittable.

The crux question for you: for a Track 1 planning proposal, do the letters of collaboration need to evidence prior usage, or do credible forward-looking commitments from named pilot adopters suffice? And how would a panel weigh a strong plan with committed-but-early adoption against waiting a cycle for demonstrated use? If forward-looking letters carry the day, September is worth taking, and your involvement would itself reduce the risk.

We have started the September preparation so that nothing is lost either way. If your read is cautious, the fallback to March 2027 is clean, since every artifact carries over and simply gains Fall pilot data.

## 6. The team, and where you might fit

The grant teams are deliberately lean: a PI plus one or two co-PIs who do core work, with everyone else a contributor. There are two anchor versions depending on whether the work is submitted from UArizona (near term) or Willamette (after a possible move).

Natural ways you could engage, in rough order of fit:

- **PESOSE strategy advisor or mentor,** immediately, on the September question and the proposal itself.
- **Co-PI or senior personnel on PESOSE.** Your ecosystem, sustainability, and open-source experience maps directly onto Track 1's core. One tradeoff to name: if you join the proposing team you cannot also be an external letter writer. A co-PI who has run the program is worth far more than one letter.
- **Technical or pilot collaborator** on the broader effort.

What we would value most right now is your read on Section 5, and whether you would want a defined role on the PESOSE effort.

## 7. If you want to go deeper (shared folder)

- `EduCloud-business-plan.md`: the full strategy (problem, product, model, IP and governance, risks).
- `EduCloud-funding-strategy.md`: the diversified funding portfolio, ranked and sequenced.
- `EduCloud-team-funding-roadmap.md`: team rosters and the integrated timeline.
- `grants/PESOSE-Track1/`: the drafted Project Description and budget, plus the September sprint plan and the letters-of-collaboration kit. Most relevant to you.
- `architecture/`: the Registry proposal and the Coolify hosting reconciliation.
