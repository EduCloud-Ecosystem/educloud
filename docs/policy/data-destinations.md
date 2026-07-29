# Data destinations

*Where each class of EduCloud data may live, who stewards it, how long it is
kept, and how the rule is enforced rather than merely stated.*

**Status:** first version, 2026-07-29. Written ahead of CC-P2, whose Step 5
specifies this document, because the Fall 2026 pilot puts real student data in
scope before CC-P2 is scheduled to run.

**Not legal advice.** This follows the convention Cairn's DESIGN.md §10 already
sets. It is an engineering and operations artifact that makes decisions
explicit and testable. The named data steward makes the calls; this document
records them so they can be reviewed, audited, and enforced.

---

## 1. Two axes, deliberately kept apart

Most of the confusion in this area comes from collapsing two different
questions into one word. EduCloud keeps them separate:

| | Axis A — **inference payload** | Axis B — **record at rest** |
|---|---|---|
| The question | May this *content* be sent to that model deployment? | May this *record* be stored on that infrastructure? |
| Governed by | `data_classification` on each registry row | This document's destination tiers |
| Enforced by | **Config absence** — the lane's rendered `model_list` contains no deployment that would violate the rule | **Deployment location** — which host the service runs on, and who stewards it |
| Machine-checked | Yes, today: `portage/tests/test_scale2_profile.py` | Partly — see §7 |

**These do not substitute for each other, and that matters.** The platform's
opaque `{course, assignment, student}` attribution labels de-identify Axis A
payloads effectively, because a model never needs a name. They do **not**
de-identify Axis B records, because Cairn is a system instructors use to grade
named humans. A design that satisfies Axis A tells you nothing about Axis B.

---

## 2. Data classes

### Axis A — inference payloads

The enum already carried on every registry row (CW02 D15):

- **`public`** — course materials, templates, public documentation, synthetic
  data. May reach any deployment, including commercial endpoints.
- **`personal_sensitive`** — de-identified student coursework carrying only
  opaque attribution labels. May reach institutional sovereign compute. May
  **not** reach a commercial endpoint.
- **`regulated`** — content from which an individual student could be
  identified with reasonable certainty. **Has no deployment at any scale
  today.** See §4.3; that absence is deliberate and is the enforcement.

### Axis B — records at rest

- **R0 — Operational, non-personal.** Templates, assignment definitions,
  container images, version manifests, telemetry keyed to opaque labels.
- **R1 — Pseudonymous identifiers.** Git-host usernames, salted one-way email
  hashes, repo names. Indirect identifiers: not names, but resolvable to a
  person by someone holding the mapping.
- **R2 — Education records (FERPA).** A score, grade, or submission bound to an
  identifiable student. Cairn's `grades` table joined to `roster_entries` is
  R2, and Cairn's own DESIGN.md §10 says so plainly: *"a score tied to an
  identifiable student is an education record regardless of whether we store
  their legal name."*
- **R3 — Directly identifying student data.** Legal names, SIS IDs, plaintext
  student email. **EduCloud stores none of this by design** — Cairn's schema
  has no column for it, and the name↔username map lives in the instructor's
  browser (DESIGN.md §6), never server-side. R3 exists in this table only to
  name what is deliberately excluded.

**The class that governs a store is the highest class it contains.** Cairn's
database holds R1 and R2 together, so Cairn's database is R2.

---

## 3. Destination tiers

Ranked by compliance posture for R2 data, strongest first. This ranking is the
correction to an earlier assumption that a commercial droplet was the safe
default — for records, it is the weakest of the four.

| Tier | Example | Who stewards the infrastructure | Third party processes data? | Suitable for R2? |
|---|---|---|---|---|
| **D1 — Institutional** | UA-provided VM or managed host | The university | No | **Yes** — strongest posture |
| **D2 — Self-stewarded** | A machine owned and administered by the named data steward | The steward, personally | No | **Yes**, with the steward's authorization recorded |
| **D3 — Shared sovereign** | Jetstream2 under an ACCESS/NAIRR allocation | Indiana University, shared | Not commercial, but shared | **No** without written institutional authorization — see §4.2 |
| **D4 — Commercial cloud** | DigitalOcean, AWS, any rented IaaS | The vendor | **Yes** | **No** without vendor review and a data-processing agreement |

**Why D4 ranks below D3 for records.** University of Arizona requires formal
privacy and security review for third-party systems that process university
information, with the trigger depending on the data and use case. Published
requirements for systems touching student data include that contracts must
require applicable privacy and security standards, that vendors may be reviewed
or audited, and that the university may require evidence of security
certifications or independent assessments. A rented droplet running
self-hosted software still places a commercial vendor in the position of
processing and storing the records; standard IaaS terms of service are not a
data-processing agreement with FERPA terms.

This does **not** make D4 unusable — it makes it a procurement question rather
than a technical one, with a lead time that must be started early or not at
all.

**D3 is not commercial, but it is shared**, and Jetstream2's own policy is
explicit that the system *"is not intended, by default, to meet the security
requirements"* of FERPA and that such data must not be stored there *"unless
such storage and usage is specifically authorized by the responsible University
administrator."* A compounding fact: Jetstream2 states that **all users on an
allocation have access to all resources on the allocation** — so adding a TA to
the allocation grants them access to everything on it, and per-user isolation
is not available to enforce.

---

## 4. The rules

### 4.1 Records

1. **R2 lives on D1 or D2 only.** Education records stay on institutional or
   self-stewarded infrastructure. They do not reach shared or commercial
   infrastructure absent the authorization in §4.2.
2. **The LMS remains the system of record for official grades.** Cairn is a
   *working store*: it provisions repositories, runs grading, and exports
   scores. It is not the gradebook of record. This is the single decision from
   which most of the others follow, and it is stated here because it was
   previously implicit.
3. **R0 and R1 may live on any tier**, including D3 and D4. This is what makes
   a JS2-hosted test deployment with synthetic data entirely fine.
4. **R3 is not stored.** Any change that would introduce a legal name, SIS ID,
   or plaintext student email into a server-side store is a design defect, not
   a feature request. Cairn's schema comments already enforce this at the
   review level.

### 4.2 Authorization, when a rule is to be excepted

An exception to §4.1(1) requires all of:

- Written authorization from the responsible University administrator, naming
  the system, the data class, and the destination tier;
- A record of that authorization in this document's register (§6);
- A dated review, because authorizations do not survive silently.

*The named data steward for EduCloud's course deployments is Greg Chism, who
holds current certification for high-security and HIPAA data handling.* That
credential is a property of the operator, not of the infrastructure — it
strengthens the case for a D2 self-stewarded deployment materially, and it does
not by itself make a D3 or D4 system compliant, because the JS2 restriction is
about the system's security posture and its shared-access model.

### 4.3 Inference payloads

Carried forward from CC-P2 Step 5, and already implemented:

1. **Open coursework and research workloads route to institutional sovereign
   compute.** That is the Scale-2 profile's `openai`-route deployments.
2. **Sensitivity is a property of the workspace, set by a human, never inferred
   per request.** No classifier decides what is sensitive.
3. **The pin is enforced by which endpoints exist in the active
   configuration.** A student lane runs against a rendered `model_list`
   containing only sovereign deployments, so a misroute is impossible by
   construction rather than forbidden by policy.
4. **`regulated` has no deployment.** Identifiable student content has nowhere
   to be sent, deliberately. If a consumer needs one, it requires a D1/D2 local
   inference deployment — which is new hardware, not a config change.

---

## 5. Retention, deletion, and backups

**This section is new. Nothing in any of the five repositories currently
implements retention, purge, or deletion — the codebase was grepped on
2026-07-29 and has no such path.** Records accumulate indefinitely today. The
policy below is what should hold; the implementation is tracked in §8.

### Retention

| Class | Retained | Rationale |
|---|---|---|
| R2 — grades, submissions bound to a student | Until end-of-term export to the LMS is confirmed complete, then **purged from Cairn** | Cairn is a working store, not the record of truth. Once the LMS holds the official grade, Cairn's copy is redundant risk. |
| R1 — usernames, email hashes, repo names | Duration of the course section, plus one term for grade-dispute resolution | Shorter than institutional record schedules because Cairn is not the record of truth |
| R0 — templates, telemetry on opaque labels | Indefinite | No personal data |

Institutional retention schedules govern the LMS copy and take precedence over
anything here. This document governs only EduCloud's own stores.

**Purging grades from Cairn after export makes the white paper's claim literally
true.** That claim currently reads *"stores Git usernames and assignment state,
never student records"*, which the `grades` table puts slightly ahead of the
schema. A purge path closes that gap and is small work.

### Deletion on request

FERPA gives students rights of inspection and correction against the
institution's records. Because Cairn is a working store rather than the record
of truth, such requests are served from the LMS. Cairn must nonetheless support
removal of a roster entry and its dependent rows — currently it does not, and
that is a gap, not a decision.

### Backups

**A backup inherits the classification of what it contains, and its destination
is governed by the same tier table.** This is the rule most often missed: a
D1-hosted database backed up to commercial object storage has placed R2 data on
D4. Consequences:

- R2 backups go to D1 or D2 destinations only.
- Backups of a JS2-hosted deployment must live **off** Jetstream2 regardless of
  class, because allocation expiry destroys resources: not renewed within 10
  days shelves all VMs; within 30 days *"all resources (VMs, volumes, shares,
  images, etc) on the allocation will be destroyed and will not be
  recoverable."* The same schedule applies to exhausting the allocation's
  service units.
- Backup encryption at rest does not change a destination's tier. It reduces
  breach impact; it does not change who is processing the data.

---

## 6. Destination register

The operational record. This is the table to show a reviewer.

| Service | Highest class | Destination now | Destination at pilot | Steward | Authorization |
|---|---|---|---|---|---|
| Cairn — control plane + DB | R2 | D3 JS2, **synthetic data only** | **D1 or D2** — decision open, see §8 | Greg Chism | Pending; §4.2 applies |
| Coolify / Keycloak (Waypoint) | R1 | D3 JS2 | Follows Cairn | Greg Chism | — |
| Portage — LiteLLM proxy + Postgres | R0 | D2 personal (Line P) | D1/D2 alongside Cairn | Greg Chism | — |
| Portage — sovereign inference | Axis A `personal_sensitive` | D3 JS2 vLLM | D3 JS2 vLLM | Greg Chism | Permitted: de-identified payloads only |
| Portage — hosted-open inference | Axis A `public` | Commercial API | Commercial API | Greg Chism | Permitted: staff lane only, `public` only |
| Belay — tutoring | R1 + Axis A | Not yet deployed | TBD at instructor-mode alpha | Greg Chism | — |
| Telemetry (Portage) | R0 | Local, gitignored | Same | Greg Chism | — |
| Grade record of truth | R2 | **LMS** | **LMS** | University | Institutional |

---

## 7. How this is enforced

**Machine-checked today.**

- `portage/tests/test_scale2_profile.py` — 10 tests asserting the student
  inference lane contains no off-institution deployment, that disabling a row
  is not an isolation mechanism, that endpoints are environment references
  rather than literals, and that no `regulated` deployment exists. Verified in
  both directions: injecting an off-institution row fails four tests even when
  that row is disabled.
- `render_config.py --check` in CI re-renders both EduCloud lanes, so a
  hand-edit to a generated `model_list` fails the build.

**Convention, not yet enforced.**

- Axis B entirely. Which host a service runs on is a deployment fact that no
  repository test can observe. §8 proposes the smallest useful check.
- Retention and deletion — no implementation exists.
- Backup destinations — no implementation exists.

**Cross-references.** Cairn DESIGN.md §5, §6 and §10 (schema minimization,
browser-side name mapping, compliance posture); Belay PRIVACY.md;
`portage/config/profiles/scale2.educloud.md` (the Scale-2 lane split);
`educloud/SYSTEM.md` §4 shared contracts.

---

## 8. Open items

Ordered by what blocks the pilot.

1. **Decide Cairn's pilot destination: D1 or D2.** D1 (a UA-provided host) has
   the strongest posture and no procurement question. D2 (a machine the steward
   owns) is fully within the steward's control and is the option Cairn's own
   §10 calls *"the strongest FERPA story"* — and it doubles as the
   FERPA-safe local inference tier that `portage-hardware-options.md` already
   names as a hardware-purchase trigger. **Blocks the pilot; decide by
   mid-August.**
2. **Determine whether UA's third-party review is triggered** by the chosen
   destination, and start it if so. Lead time unknown; a D1 host likely avoids
   it entirely.
3. **Implement grade purge-after-export in Cairn.** Small, and it makes the
   white paper's claim exact.
4. **Implement roster-entry deletion** with dependent rows.
5. **Add a deployment manifest and a test.** The smallest useful Axis B check:
   a checked-in file declaring each service's destination tier and highest data
   class, plus a test asserting no R2 service is declared on D3 or D4 without a
   recorded authorization. Turns §6 from a table someone maintains into a table
   CI maintains.
6. **Reconcile the white paper** if item 3 is not done — soften *"never student
   records"* to match the schema.
7. **Fold into CC-P2 when it runs.** This document is CC-P2 Step 5's
   deliverable, arriving early. CC-P2 should adopt it rather than re-author it,
   and add the CI wiring in its Step 2 workflow.
