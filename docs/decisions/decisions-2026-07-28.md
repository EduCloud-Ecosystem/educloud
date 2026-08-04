# Six decisions — sizing, evaluator, subscriptions, hardware

*2026-07-28. Answers to the six items raised against `remaining-work-2026-07-28.md`.
Research current as of today; every price and spec is cited. Where a number
could not be confirmed from a primary source, it says so.*

---

## 1. Waypoint host — minimum size

> **Revised a third time, 2026-07-29, after "why can't JS2 do all of this?"**
> **This block supersedes the two below it. Read this one.**
>
> **Short answer: JS2 can do all of it — until a real roster lands. Then it
> can't, and the line falls exactly where your architecture already draws it.**
>
> ### JS2 is better than both earlier options, for now
>
> This isn't a workaround. Jetstream2's docs have a section titled
> **"Always-On" Infrastructure**: *"an extremely common use case for
> Jetstream2 is hosting persistent or 'always-on' infrastructure for
> projects"*, and *"There are no restrictions on runtime for the Jetstream2
> CPU resource."* Classroom use is a **named allocation purpose** — Explore
> covers "small classes and training events," Discover covers "large classes"
> and "gateway development." Public IPv4 is standard, 80/443 are unrestricted,
> and Let's Encrypt works (launch via **Exosphere**, whose default security
> group opens inbound; Horizon and CLI default to egress-only and you'd have
> to add the ingress rule yourself).
>
> So against the droplet it wins on cost and ties on everything else. Against
> the local-VM-plus-tunnel plan it wins outright — it's genuinely always-on,
> which was the one thing local could never give you.
>
> ### The cost is a rounding error
>
> 1 SU = 1 vCPU-hour. A VM burns SUs whenever it's active (shelving is the
> only state that stops the meter — stopped still bills 50%).
>
> | Flavor | vCPU / RAM / root disk | SU/hr | One semester (~2,920 h) | % of Discover (1.5M) |
> |---|---|---|---|---|
> | m3.quad | 4 / 15 GB / 20 GB | 4 | 11,680 | 0.8% |
> | m3.medium | 8 / 30 GB / 60 GB | 8 | 23,360 | **1.6%** |
>
> Even against an **Explore** allocation (400,000 credits), an always-on
> m3.medium for a full year is 17.5%. Storage: 1 TB of volume storage comes
> with the allocation at no extra request.
>
> **Sizing note:** m3.small's 20 GB root disk is *below* Coolify's 30 GB floor
> and will fill with Docker images. Use **m3.medium** (60 GB root, zero fuss)
> or m3.quad plus an attached volume from the free 1 TB.
>
> ### The wall: FERPA — and you already wrote this down
>
> Jetstream2's own policy, verbatim:
>
> > "Ensure that data that must be protected by Federal security or privacy
> > laws (e.g., HIPAA, **FERPA**, ITAR, classified information, export
> > control, etc.) are **not stored on this system unless such storage and
> > usage is specifically authorized by the responsible University
> > administrator**... **The Jetstream2 system is not intended, by default, to
> > meet the security requirements of these laws or regulations.**"
>
> And your own `portage-hardware-options.md` already reached the same
> conclusion months ago: *"Jetstream2 is sovereign but not private, so real
> student records cannot go there. A local box is the only place they can
> run."*
>
> Cairn in production holds rosters, submissions, and grades — squarely FERPA
> education records. One compounding fact makes it worse: Jetstream2 states
> **"all users on an allocation have access to all resources on the
> allocation."** Add a TA to the allocation and they can reach everything.
> Per-user isolation isn't available to enforce.
>
> Note this is a *conditional* prohibition, not an absolute ban — JS2's text
> contemplates institutional authorization. But that's a conversation with
> UA's registrar or data steward with unknown lead time, and thirty days out
> from the shutdown is the wrong moment to start it.
>
> **One tempting path that doesn't work:** de-identifying Cairn the way the
> platform de-identifies inference payloads. The opaque
> `{course, assignment, student}` vocabulary works for inference because the
> model never needs a name. Cairn is the system of record — instructors grade
> named humans. Those are different problems and the attribution labels don't
> transfer.
>
> ### The revised sequence
>
> | When | Where | Cost |
> |---|---|---|
> | Now → pilot | **JS2 m3.medium.** Coolify + Keycloak + Cairn, synthetic data only. Public IP, real TLS, always-on. | **$0** |
> | Before real rosters | Move Cairn's record-of-truth to controlled infrastructure — the $24 droplet, UA-hosted, or a local box. JS2 keeps the inference tier. | $24/mo |
> | Pilot load | Resize if warranted | $48/mo |
>
> The migration isn't wasted work — it *exercises* the portability claim.
> Deploying to JS2 and then moving to a droplet is a live demonstration that
> "a Coolify application IS the contract," which is exactly what the
> self-hosting story needs and what PESOSE reviewers will ask about.
>
> ### Two things to check, and one allocation refinement
>
> - **Allocation expiry destroys VMs.** Not renewed within 10 days → all VMs
>   shelved; within 30 days → *"all resources (VMs, volumes, shares, images,
>   etc) on the allocation will be destroyed and will not be recoverable."*
>   The same schedule applies to running out of SUs. Keep backups off JS2.
> - **Which allocation do you actually hold?** Your hardware-options doc
>   references a **NAIRR** Jetstream2 allocation. NAIRR Start-Up is
>   128,000 SU for **3 months** and is AI-research-scoped — SUs aren't the
>   constraint, but the 3-month window and the scope both are, and hosting a
>   classroom app on it is a stretch. Check
>   `allocations.access-ci.org` → Credits + Resources.
> - **File ACCESS Explore, not Discover, to unblock this.** Explore needs only
>   an abstract (Discover wants a one-page description), and its 400,000
>   credits are ample for the host. That's a faster path to a running host
>   than the Discover request currently on the E0 list. Worth confirming
>   whether holding Explore complicates a later Discover request for the
>   inference tier.
>
> ---
>
> **Superseded — kept for the reasoning record.**
>
> **Revised again 2026-07-29, after "can we just simulate droplets?"**
>
> **Yes — and you already have. That's Waypoint Phase 1.5, and it's done:**
> local Coolify stack, Keycloak realm export, full visitor-auth round trip
> proven locally, five demo apps with instantiated Dockerfiles. The proof of
> concept you're asking for exists. So the real question isn't "can we
> simulate" — it's *what is left that a local simulation structurally cannot
> cover*, and the list is short and specific:
>
> 1. **Real TLS certificates.** Let's Encrypt needs a publicly-resolvable name.
> 2. **OIDC redirect flows over real HTTPS.** Cookie `Secure` and `SameSite`
>    behaviour, redirect-URI validation, and browser handling all differ
>    between `https://real.host` and `http://localhost`. This is the classic
>    worked-locally-broke-in-prod failure, and it sits exactly on Cairn's
>    Keycloak seam.
> 3. **Inbound GitHub webhook delivery.** Cairn's webhook receiver with secret
>    threading is already built, and GitHub must POST to a reachable URL to
>    exercise it at all.
> 4. **Always-on availability.** Students work nights and weekends; a Mac
>    sleeps.
>
> **Items 1–3 you can get for $0 with a tunnel.** Cloudflare Tunnel or —
> better, since it's already in your stack — **Tailscale Funnel** gives a
> public HTTPS URL with a real certificate pointing at a locally-running
> service. Pair it with Coolify installed in a local Ubuntu VM (Multipass,
> UTM, or OrbStack) rather than bare Docker Desktop, and you are exercising
> the actual install path, the actual TLS path, and the actual webhook path.
> That is a genuinely faithful simulation, not a stub.
>
> **Item 4 is the one that cannot be simulated, and it's the one the pilot
> needs.** So the sequence I'd run:
>
> | When | What | Cost |
> |---|---|---|
> | Now → mid-August | Local Ubuntu VM + Coolify + Tailscale Funnel | $0 |
> | Mid-August, or when Cairn's GHC import works | Provision `s-2vcpu-4gb`, do the real deploy once | $24/mo |
> | Before students touch it | Resize to `s-4vcpu-8gb` if load warrants — you'll know by then | $48/mo |
>
> **Be honest about what deferring buys, though: about $18.** The saving is
> trivial. The real reason to defer is *attention* — not spending thought on
> infrastructure while Cairn's GHC import is the critical path. That's a good
> reason. But it cuts both ways, and here's the counter-argument worth
> weighing: **deployment surprises are the classic thing that eats the last
> week.** If the first time you touch a real droplet is August 20 and
> Coolify's install has a surprise, you are debugging infrastructure during
> the week you should be migrating your own course. Mid-August is the latest
> I'd leave it, and earlier is cheap.
>
> **One option to reject explicitly:** running the Waypoint stack on the iMac
> instead of a droplet. It's always-on and free, but it puts Coolify,
> Keycloak, Cairn and a second Postgres on a 16 GB machine already running
> LiteLLM, Postgres, Ollama with a warm 7B, Qdrant, Open WebUI and SearXNG —
> and, worse, it couples Line P's personal infrastructure to Line E's class
> platform on one box. Your own roadmap keeps those lines separate by design.
> An experiment on the personal side should never be able to take down the
> platform a class depends on.
>
> ---
>
> **Revised 2026-07-29, after "we are just testing."** Correct call — the
> original number was sized for a Fall pilot that doesn't exist yet. **Start at
> `s-2vcpu-4gb`: 2 vCPU / 4 GiB / 80 GiB, $24.00/mo**, and resize to
> `s-4vcpu-8gb` ($48.00) before the pilot loads in late August. The pilot
> analysis below is unchanged and still governs that second step — read it in
> August, not now. What follows immediately is the testing-phase decision.
>
> ### Why $24 and not less
>
> The rung below is a trap. `s-2vcpu-2gb` is **$18 — only $6 cheaper for half
> the RAM and 20 GiB less disk.** That's the worst value on the ladder. The
> genuinely cheaper option, `s-1vcpu-2gb` at $12, gives up the second vCPU,
> which makes Coolify's UI sluggish during every deploy and makes grading
> builds crawl. Neither saving is worth the constraint on a box you're using to
> *find out whether the stack works*.
>
> The memory math for a test deployment — no students, no concurrent grading:
>
> | | Without Keycloak | With Keycloak |
> |---|---|---|
> | OS + Docker | ~400 MB | ~400 MB |
> | Coolify (app + its Postgres + Traefik) | ~550 MB | ~550 MB |
> | Cairn Go API + Postgres + static dashboard | ~460 MB | ~460 MB |
> | Keycloak, heap-capped for a handful of users | — | ~1,000 MB |
> | **Steady total** | **~1.4 GB** | **~2.4 GB** |
>
> At 4 GiB that leaves ~1.6 GB of headroom with Keycloak running — enough for a
> grading container without touching swap. At 2 GiB you'd have ~600 MB and
> Keycloak would not fit at all.
>
> ### The Keycloak question, which is worth asking now
>
> Keycloak is ~40% of the RAM budget at this scale, and there's a genuine
> tension in your own roadmap about whether it's needed yet. Line E's scale
> table says MVP identity is **"Cairn sessions, OIDC seam stubbed"** —
> Keycloak becomes the ecosystem provider at E3/Institutional. But E0's bullet
> says "Coolify and Keycloak live per the proven local build."
>
> Both can be true — Keycloak running on the host to prove the stack, with
> Cairn not yet depending on it. But if you defer Keycloak entirely until E3,
> `s-1vcpu-2gb` at **$12/mo** becomes genuinely viable for testing. That's the
> only way to get meaningfully below $24, and it's a roadmap decision rather
> than a budget one. I'd keep Keycloak and pay the $24 — proving the auth path
> early is most of what the host is for — but flagging it since it's the one
> lever that actually moves the number.
>
> ### The rule that makes starting small safe, and its one caveat
>
> DigitalOcean has two resize paths, and the difference matters more than the
> price:
>
> - **"CPU and RAM only"** — the default in the control panel and in `doctl`.
>   Leaves the disk untouched.
> - **"Disk, CPU, and RAM"** — grows the disk and is **permanently
>   irreversible**. DO's own warning: *"Because your Droplet's filesystem will
>   be expanded, this resize is not reversible."*
>
> The governing rule is *"you can resize to any plan that has an equal or
> greater amount of disk space as the original."* So if you start at 80 GiB and
> **never once check the disk box**, you can move up to `s-4vcpu-8gb` (160 GiB)
> for the pilot and back down afterward. The moment you take a disk-inclusive
> resize, your floor is permanently raised.
>
> **Caveat, stated because it's load-bearing:** DO's docs contradict themselves
> here. The resize how-to implies the down path works; a separate support page,
> "Can I make my Droplet smaller?", flatly says *"No, Droplets cannot be resized
> to a smaller plan"* — apparently written for the disk-expanded case, but it
> doesn't say so. **Do not build a budget that depends on scaling back down.**
> Plan $24 → $48 as one-way and treat the return trip as a bonus. If you want
> certainty, test it once on a throwaway droplet.
>
> Both resizes require a power-off, roughly a minute per GB of used disk.
> If you need more storage later, attach a block volume ($0.10/GiB/mo) rather
> than resizing the disk — that keeps the reversibility intact.
>
> ### Two things you must do at 4 GiB regardless
>
> 1. **Build the Vite dashboard off-box** — in CI, or locally, pushing an
>    image. The documented Coolify failure is a frontend build consuming
>    3.16 GB, which will not fit in your headroom. This is good practice at any
>    size; at 4 GiB it's mandatory.
> 2. **Add 2–4 GB of swap.** Coolify's own docs recommend it, and it converts a
>    would-be OOM kill into a slow minute.
>
> The `docker run --rm` grading pattern (below) matters *more* at 80 GiB than
> at 160 GiB, not less — that's the difference between flat disk usage and
> filling the box mid-semester.
>
> ### Cost over the run
>
> ~$24/mo now through August (≈$50 total), then $48/mo once the pilot loads.
> Skip backups while testing; add them ($9.60/mo) when real student work lands.
>
> **One argument for provisioning now rather than later:** Waypoint's Phase 1.5
> already proved the whole stack locally, so what the droplet actually buys is
> the three things you cannot test on your Mac — a public URL, real TLS, and
> real OIDC redirect flows over HTTPS. Those are exactly where deployment
> surprises live, and $24 to surface them in July rather than in the last week
> of August is cheap insurance.

---

### The pilot-scale analysis (for August, not now)

**Buy: DigitalOcean Basic Droplet, 4 vCPU / 8 GB / 160 GB — `s-4vcpu-8gb`,
$48.00/mo.** Add weekly backups at 20% (+$9.60). **All-in ~$57.60/mo.**

**The true minimum is 2 vCPU / 4 GB / 80 GB plus swap**, and I'd advise against
it. RAM binds first and it binds hard — Keycloak's own sizing doc puts base
usage at **1,250 MB** for one realm with cached sessions, which is ~30% of a
4 GB box before Cairn starts. The steady-state budget lands at ~3.0–4.2 GB
before a single student submits anything. Coolify's official floor (2 CPU /
2 GB / 30 GB) is for Coolify *alone* and does not survive contact with Keycloak.

What breaks at 4 GB, concretely:

- **The Vite production build OOM-kills a neighbour.** A documented Coolify case
  had a frontend build consume 3.16 GB on a 4 GB box and die with a JS heap
  error — and because Docker's OOM killer targets highest-RSS, the casualty is
  usually Keycloak or Postgres, not the build.
- **Zero grading headroom.** One Go compile in a sandbox (~0.5–1.5 GB) plus
  BuildKit eats the remaining margin. A deadline burst serialises into a queue
  that takes hours.

At 8 GB you get ~4 GB of burst headroom — one Vite build *or* 3–4 concurrent
grading slots at `--memory=512m`, without touching swap. Growth path for 2027 is
16 GB / 8 vCPU at $96/mo; prefer that to a second box until you need build
isolation.

**Skip Premium.** This workload is RAM- and compile-CPU-bound, not
sustained-IOPS-bound, so NVMe buys little. *Caveat, stated plainly:* I could not
confirm the current Premium price at this tier from a DigitalOcean primary
source — the live pricing page renders only the Regular table to a fetcher.
Third-party July 2026 sources put Premium AMD 8 GB/4 vCPU near $56/mo but mark
it an estimate. Verify in the control panel; the recommendation doesn't turn on
it. If you want more disk, a block volume at $0.10/GiB/mo is cheaper than the
Premium tier's bundled extra.

### The disk finding that actually matters

Disk risk is not Coolify's — it's the grading runner's design, and the delta is
enormous:

- **`docker build` per submission (the trap).** A `golang` base image is ~1 GB.
  At ~60 students × 5 assignments × ~3 resubmissions ≈ 900 builds/semester, even
  100 MB of unique layers per build is **90 GB/semester**; at 300 MB it's 270 GB.
  BuildKit cache mounts grow unbounded and are *not* reclaimed by
  `docker image prune`.
- **One pinned image per assignment + `docker run --rm` per submission.** Five
  images at ~1 GB, ephemeral layers that vanish on exit. **Under 10 GB, flat
  across the semester.**

Use the second pattern. With it, even 80 GB would do; the 160 GB is insurance
and Postgres/log room.

Two maintenance items that are easy to miss:

- Coolify's cleanup is **opt-in** (Servers → Configuration → Advanced → Force
  Docker Cleanup + cron; no default is set) **and it only cleans
  Coolify-managed containers** — your grading images are invisible to it. Run
  your own label-scoped prune nightly. Never run a naked `docker system prune -a`;
  it deletes images Coolify needs for rollback.
- Set container log rotation (`max-size: 10m`, `max-file: 3`). Unbounded
  json-file logs are the second-most-common way a grading host fills up.

### Hetzner is now the wrong answer, and more clearly than before

Hetzner repriced Cloud upward effective **15 June 2026**. The like-for-like US
plan, CPX31 (4 vCPU / 8 GB / 160 GB), went **€20.99 → €62.49/mo** — roughly
$68–73, i.e. *more* than DigitalOcean's $48 for identical specs. The cheap CX
line is **Germany/Finland only**, which is the wrong latency and the wrong
data-residency story for US student PII regardless. Moving off Hetzner was
correct and is now correct by a wider margin.

### One security note while you're building it

The grading runner needs the Docker socket, and mounting `/var/run/docker.sock`
puts your grader and Coolify's control plane on the same daemon at the same
privilege. Beyond the cpu/memory/pids limits already in Cairn, add
`--network=none`, `--read-only`, `--cap-drop=ALL`,
`--security-opt=no-new-privileges`, and a non-root user in the grading image.
Isolating the grader onto its own host is the right 2027 move, not a 2026 one.

---

## 2. Sloan — removed

Understood: no live programs, so the LOI can't be submitted. I've struck it from
E0's admin list. It was never on the critical path — the foundation sequence
(Hewlett, ECMC, Ascendium, Spencer, NLnet) is E2 work gated on pilot data, so
losing one name costs E0 nothing.

The one thing worth doing differently as a result: when E2 opens, **verify each
foundation's live call window before writing anything**, rather than working
from the assumed send-order. Sloan's absence suggests the list was built from
program history rather than current openings, and a second stale entry would
cost real writing time in the January–March crunch.

---

## 3. GitHub admin — one item left

Good. That leaves **`verifier-contract`** as the only repo still to create, and
it isn't needed until CC-P1 v2 runs in September, so it's off the critical path
entirely.

The practical consequence: **`portage-local`'s first push is unblocked right
now.** That was the item I flagged hardest — HB-0's entire output on one disk —
and if the private repo already exists, it's a one-command fix with nothing in
front of it.

---

## 4. Parity Bench evaluator

The roadmap line *"the evaluator is confirmed"* is ambiguous between two
different roles, and they need different answers. Both are below. **Worth
settling which you meant, because only one of them has a deadline.**

### 4a. The scoring evaluator — how bench tasks get judged

**Recommendation: score with the CC-P1 verifier contract, not an LLM judge.**

The platform's whole thesis is that no module trusts a model's self-report.
Using an LLM-as-judge inside the equity instrument would undercut precisely the
claim the bench exists to support, and a reviewer who noticed would be right to
discount the finding. Scoring through `verifier.code` and `verifier.science`
instead gives you three things at once: a defensible measurement, a **third
consumer of the verifier contract** (strengthening PESOSE's portability claim
beyond the two-consumers-in-two-languages target), and reason codes that make
per-task failure analysis mechanical rather than interpretive.

Where no deterministic verifier exists — explanation quality, pedagogical
appropriateness — use **blinded human rubric scoring with two independent raters
and a reported inter-rater reliability statistic**, not a model. Report the
split between machine-verified and human-rated tasks in the preregistration; a
mixed instrument is fine, a silently mixed one is not.

This also means the twelve-task pilot cut should not run before CC-P1 v2 lands,
or it will need re-scoring. That is a real sequencing dependency and it argues
for CC-P1 v2 in September rather than later.

### 4b. The external program evaluator — the IUSE requirement

NSF IUSE expects an independent external evaluator, named, with a letter of
collaboration in the package. Three sourcing routes, cheapest first:

| Route | Cost | Trade-off |
|---|---|---|
| Your institution's own evaluation unit | Lowest | Fast and cheap, but check independence — they cannot sit inside the project's reporting line, and a reviewer will look |
| A DBER or computing-education researcher at a peer institution | Low–moderate | Credible and collegial, but they need *evaluation* experience, not only research experience — these are different skills and reviewers know it |
| A dedicated STEM-education evaluation firm | Highest, most reviewer-legible | The names that recur on NSF STEM-ed awards are Horizon Research, SageFox Consulting, Inverness Research, EDC and WestEd. Verify current availability and fit — I'm naming category-typical firms, not vouching for a 2026 roster |

Budget 5–10% of total, which is the conventional band.

**The scheduling finding, and it's the actionable part:** an evaluator must be
committed *with a letter* before the ~January 20, 2027 IUSE deadline, and
evaluation firms book their January-deadline capacity during the fall. Approach
in **September 2026**. That makes this an **E1 item, not an E2 item** — my
earlier doc had it sitting with the grant-season work, which is too late.

One more sequencing point: the evaluator should review the **preregistration
before the pilot cut runs**, not after. A preregistration the evaluator first
sees at analysis time isn't independent, and the equity claim is the one finding
you most need to be unimpeachable.

---

## 5. S3 cancellations — and the Posit consolidation

**The headline: Posit's consolidation does not touch Posit Cloud (the hosted
IDE), and it is not a cancellation decision.** It belongs on a September
checklist, not on the S3 ladder.

Per Posit's **21 July 2026** post, four *publishing* products fold into Connect
Cloud:

| Service | Timeline |
|---|---|
| shinyapps.io | Migration tool in Connect Cloud ~**Sept 2026**; **automatic migration early 2027**; URL redirects preserved; **existing pricing and authorised-user counts held through 2029** |
| rpubs.com | New publishing ends 30 Jun 2027; content served to 31 Dec 2031 |
| quartopub.com | Publishing ends 31 Dec 2026; content served to 31 Dec 2031 |
| bookdown.org | Content served to 31 Dec 2031 |

*(Note a date discrepancy: the original January 2026 announcement said "end of
2026"; the July 2026 post moved automatic migration to early 2027. Treat the
later date as current.)*

What this means for the cancellation ladder:

- **Posit Cloud (the IDE) is unaffected.** Not in the consolidation list; still
  sold standalone; no deprecation entry in its changelog. If you're paying for
  it, decide on its own merits — the consolidation creates no urgency.
- **Paid shinyapps.io: no action, no price change until 2029.** Cancel it for
  your own reasons if you want; the consolidation gives you neither urgency nor
  penalty for waiting.
- **Free shinyapps.io gets strictly better** — Connect Cloud's free tier is
  4 GB RAM / 1 CPU against shinyapps' 1 GB, and migration is automatic.
- **The one thing that could cost you money.** On Connect Cloud, Free and Basic
  ($19/mo) make **all content public — including your account home page**.
  Private or gated sharing starts at **Enhanced, $59/mo**. If any current app
  relies on non-public access, that's a genuine new line item, not a migration.
  Worth checking before September.
- **No academic tier for Connect Cloud has been announced.** Posit's academic
  page still lists Posit Cloud and shinyapps.io free tiers and free teaching
  subscriptions for Workbench/Connect/Package Manager, but Connect Cloud appears
  nowhere on it. That's an unresolved gap for an instructor, not a confirmed
  loss — watch it.
- **Could not confirm:** whether Connect Cloud's free tier has an active-hours
  cap equivalent to shinyapps' 25 hrs/month. The comparison table omits the row
  and the system-limits doc documents only a 24 GiB disk quota. Verify before
  relying on it for a class.

**Net effect on S3:** unchanged. The cancellation ladder stays ChatGPT Plus,
Claude Pro, and Perplexity, each dated and evidence-gated against the paired
baseline. Posit is a 30-minute September migration check — I'd calendar it
alongside the evaluator outreach, since both land in the same week.

---

## 6. Hardware

**Recommendation: buy nothing with personal money. If the grant money is real
and time-bound, buy an ASUS Ascent GX10 at $3,266 rather than a DGX Spark at
$4,699 — same GB10 silicon, smaller SSD.**

### The market fact that dominates everything

We are at a cyclical price peak driven by the 2026 DRAM shortage, not by product
value. AI datacenters are absorbing roughly **70% of world memory output in
2026**, up from 20–30% in 2022. New fab capacity doesn't reach volume until
2027, with normalisation possibly 2028. Framework's own words: *"this is going
to be a challenging year and possibly even years for consumers."*

Concretely, this has already happened:

- **Framework Desktop 128 GB: $1,999 → $2,459 (Jan) → $3,449 today.** +73% for
  identical silicon.
- **DGX Spark: $3,999 → $4,699**, an 18% hike NVIDIA attributed to memory supply.
- **Apple deleted the 128 GB Mac Studio entirely.** The 512 GB option went in
  March; by May the maximum Mac Studio memory is **96 GB**. M5 Mac Studio is now
  expected around **October 2026**, delayed by the same shortage.

Beware any "2026 buyer's guide" still quoting Framework at $1,999 or GMKtec at
$1,800 — those are 2025 prices.

### The measured numbers that decide it

`gpt-oss-120b` MXFP4, independently measured:

| Machine | Price | Prompt processing | Token generation | Bandwidth |
|---|---|---|---|---|
| Framework Desktop 128 GB (Strix Halo) | $3,449 | **340 tok/s** | 34.1 tok/s | 256 GB/s spec, ~212 measured |
| DGX Spark / Ascent GX10 | $4,699 / **$3,266** | **1,723 tok/s** | 38.6 tok/s | 273 GB/s |
| Mac Studio M3 Ultra (256 GB unit) | $3,999+ (96 GB max now) | 864 tok/s | **70.8 tok/s** | 819 GB/s |

Bandwidth predicts token generation almost linearly. Prompt processing is
predicted by compute, which is why DGX Spark beats Strix Halo **5:1 on PP**
despite similar bandwidth.

**For agentic coding, PP is what you wait on** — large repo context, tool
results, long system prompts. That single fact is what kills the Strix Halo case
at its new price: you'd be paying DGX-Spark money for one-fifth the prompt
processing.

### Two Strix Halo problems specific to your setup

1. **An open Ollama bug breaks exactly your pattern.** Issue #16719 (filed
   14 June 2026, still open) — on gfx1151 the scheduler caps the GPU memory
   budget to *host free RAM* rather than the VRAM carveout, so loading a second
   model evicts the first even when both fit. Your entire local design is a warm
   steward plus a second model. A PR exists, unmerged.
2. **ROCm on gfx1151 is immature** — allocation bugs capping at 64 GB, Vulkan
   hangs on some models, gfx1100 rocBLAS running 2.5–6× faster than gfx1151, and
   VRAM exhaustion able to crash the whole machine via kernel driver error.

### What I'd actually do

**Nothing yet, and the roadmap already says so.** Line P's S5 rule is that
*"the hardware decision is made by the dashboard rather than by appetite."* The
market now independently argues for the same deferral, which means that rule was
written correctly and needs no change. The dashboard doesn't exist until S3
calibration produces it — so there is nothing to decide until roughly January.

Meanwhile the honest observation is that **the gap between your two Macs and
your goal is mostly software, not silicon.** A 30B-class model at ~40 tok/s is
the realistic daily driver on *any* of these boxes; the 120B model is the
occasional case. HB-0 through HB-2 will tell you empirically whether local
inference is worth $4k to you, at zero capital cost.

**Re-evaluate Q4 2026.** Three things land in that window and all improve your
position:

- **Gorgon Halo (Ryzen AI Max 400)** — up to 192 GB unified, OEM systems from
  Q3 2026. Incremental: bandwidth isn't much improved, so TG won't change much.
- **M5 Mac Studio, likely October** — M5 Max is already shipping in the MacBook
  Pro at **128 GB and 614 GB/s**, which is 2.4× Strix Halo's usable bandwidth,
  and you're already in the Mac ecosystem with Ollama running. This is the one
  I'd watch hardest.
- **Medusa Halo with LPDDR6** — leaked at ~80% more memory bandwidth. Leak, not
  confirmed, but it's the generation that actually fixes the bandwidth ceiling.

**Skip GPU builds.** Four used RTX 3090s is ~$6,000–7,000 all-in for 96 GB at
~1,400W, it's a build-and-maintain project rather than an appliance, and no new
consumer silicon arrives until 2027. The single-card 96 GB answer, RTX PRO 6000,
is $13,250 — three times a whole DGX Spark.

**The one thing that would change this advice:** if you believe 128 GB gets
*harder* to obtain rather than cheaper, buying now has option value — and Apple
deleting the 128 GB SKU is real evidence for that. But the hedge against that
risk is a GX10 on grant money, not a $3,449 Framework on yours.
