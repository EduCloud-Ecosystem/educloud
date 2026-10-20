# Researcher and instructor pilot milestone

Product direction approved October 19, 2026. EduCloud's next product milestone
is one researcher and one instructor independently completing the full Python/R
journey on qualified resources. The existing research and classroom intake paths
stay distinct. The [assessment contract](../specs/research-assessment.md),
[temporary-data contract](../specs/assessment-owned-data.md) and
[sequenced backlog](research-pilot-build-backlog.md) govern implementation.

## Complete journey

1. The participant completes the appropriate research or classroom intake,
   identifies a project and explains the scientific or instructional task.
2. The participant reviews the workload, temporary input, retention preview,
   proposed limits and resource eligibility. Upload begins only after the
   actual storage, access, encryption and independent cleanup gates pass.
3. An actual-resource Python/R benchmark produces bounded measurements and
   quality checks. Failed attempts, OOM, unsupported counters and unknowns stay
   visible. Reservations and conservative charges remain distinct from measured
   consumption; a synthetic estimate cannot stand in for an actual observation.
4. The participant receives an uncertainty-aware resource estimate or comparison,
   including held-out error, repeat variability, exclusions and limits on scaling.
   The implementation reuses the merged estimator and receipt contract.
5. The participant understands and edits a matching allocation packet, narrative
   and worksheet. Reuse the merged preview/approval/export path and supported
   program profiles. Current requirements and scientific correspondence must be
   reviewed before application readiness; draft generation is not submission.
6. Independent qualified controls establish the required denial, termination,
   access revocation and deletion outcomes, including faults. Unknown cleanup
   remains unresolved. A test file observed absent is insufficient for verified
   cleanup or contract closure.

Completion means an observed end-to-end exercise by each participant without
developer intervention, together with the required operator, second-machine,
manual accessibility and whole-service acceptance evidence. A passing component
test, developer demonstration or editable draft alone does not complete it.
The initial exercises may use synthetic or approved public inputs on actual
qualified resources; this milestone does not authorize private/student data.

## Measurements and acceptance

Record results separately for the researcher and instructor, including failures,
denominators, assistance and missing measurements. Establish the pilot's review
thresholds before its operational exercise; no unmeasured performance or accuracy
target is implied by the current source implementation.

| Measure | Required record |
| --- | --- |
| Time to a valid run | Intake-to-first-valid-result timestamps, with the quality criterion, failed attempts and operational waiting time visible. |
| Estimate error | Held-out predicted versus actual consumption/duration in the same units, variability, exclusions and unsupported dimensions. No fitting on held-out observations. |
| Budget adherence | Approved per-attempt ceilings and finite native-unit allowance compared with recorded reservations, measured use and conservative charges as separate quantities; unknown exposure stays visible. |
| Cleanup outcomes | Independent observations for denial, writer/process drain, revocation and deletion under normal and fault conditions, with unresolved liabilities retained. |
| Independent completion | Each participant's full workflow, assistance or failure points and understandable final packet; record whether developer intervention was needed. |
| Accessibility | Manual completion evidence and discovered barriers for the supported participant/operator workflow; automated checks are supplementary. |

## Delivery and ownership

The coordinator reviews, integrates and merges through existing sole component
owners. Outfitter's [disabled owned-data source is accepted](../research/2026-10-19-owned-data-source-acceptance.md).
The [connected Waypoint AS1 source is accepted](../research/2026-10-19-as1-source-acceptance.md)
with production content disabled. Next connect larger-profile execution and
actual measurement through
the existing execution authority as resources become qualified, reuse A4/A5 for
validated estimates and exports, and complete the participant/operator exercises.
Do not rebuild the estimator, export pipeline, portal, scheduler or ledger.

Waypoint owns intake, current authorization, session metadata and user-facing
handoff. Outfitter owns the existing resource/data lifecycle and measurement
authority. Existing Belay development, Ben's assignments, Cairn and Portage
boundaries remain intact. A future governed AI workspace is a separate product
path. AI, agent infrastructure, Kubernetes and PAIR are optional and are not
prerequisites for completing this Python/R pilot.

## Optional tools and operational decisions

The [approved provisional budget](researcher-instructor-pilot-budget.md) records
the staged planning ceilings and exact allocation/host/operator decisions still
required. It adds no live-test, resource-selection or spending approval.

Adopt an optional tool only with all four items recorded: a named participant or
operator workflow, an unmet capability in the current platform, a measurable
acceptance benefit and an identified maintenance owner. Otherwise defer it as a
research candidate. A favorable comparison or available integration is not a
delivery commitment. Zensical documentation and Modal comparison remain separate
bounded pilots and cannot add dependencies to the core journey.

Before dependent operational work, present Greg with the proposed resource,
operator/cleanup owner and time window, a finite allowance in native units,
measured assumptions and remaining unknowns, alternatives and the acceptance
benefit. Continue independent implementation while a decision is pending.
No resource, spend, subscription, live allocation, model download/inference,
production deployment or private-data/FERPA approval is inferred from this
direction. Live Jetstream2 requires Greg's separate approval. Preserve the
existing upload, host, encryption, independent cleanup, recovery and allowance
gates; Docker/Compose on OrbStack remains the baseline.
