# Computing continuity: finish the classroom path, adopt the notebook runtime

## User requirement

A reliable replacement for fleeting computing sources, with browser-based
Python/R coursework as the first use case. The user selected this over VS Code
workspaces and batch-only grading on October 6, 2026.

## Decision

Cairn is the most complete EduCloud component and remains the classroom and
assignment control plane. Add explicit per-class workspace navigation there.
Waypoint hosts a portable JupyterHub deployment using DockerSpawner, one course
per deployment, with a fixed Python/R image, persistent per-learner homes,
verified identities and course allowlists. It can run on owned or institutionally
funded Docker infrastructure without a GitHub Education entitlement.

Use established Jupyter components, rather than implement an IDE/session manager
in Outfitter. JupyterHub's [architecture](https://jupyterhub.readthedocs.io/en/stable/explanation/concepts.html)
already separates authentication, proxying and per-user servers.
[DockerSpawner](https://jupyterhub-dockerspawner.readthedocs.io/en/latest/)
supplies the container lifecycle. Its configuration is portable across Docker
hosts; portability is demonstrated by a recovery rehearsal, not assumed from
the existence of a Dockerfile.

## Boundaries

- The Cairn link grants no access and carries no student data or token. The Hub
  authenticates independently. Initial roster enrollment is an operator action;
  no automatic Cairn-to-Hub SSO or assignment synchronization is claimed.
- One maintained image contains Python, R and the selected course packages.
  Preserve the built image by immutable registry digest or image archive; source
  recipes and package locks alone do not freeze upstream OS repositories.
- Notebook compute can stop or be replaced without deleting the learner home.
  Persistent volumes are not backups. Recovery archives include the Hub database
  and home volumes; protect them as learner data and credentials, encrypt them
  off host, and test restoration regularly.
- Each learner has an internal network and no direct Internet egress in the
  pilot. Upload/download is the initial file-transfer path. Direct Git access,
  package installation and external datasets require an explicit later egress
  and credentials decision, not an accidental shared-host connection.
- Production uses HTTPS and per-user subdomains on a dedicated domain, following
  [JupyterHub's security guidance](https://jupyterhub.readthedocs.io/en/stable/explanation/websecurity.html).
  Do not co-host the Docker socket-bearing Hub with identity databases or unrelated
  sensitive services. Kernel isolation and disk quotas remain deployment gates.
- Existing Cairn grading findings remain unresolved and separately block trusted
  assessment. Notebook availability must not imply grading integrity.

## Component priorities

1. Cairn plus the Waypoint workspace recipe: a complete usable Python/R path.
2. Operations: funded capacity, institutional identity, storage quotas, backup
   destination, offboarding and an actual target-host recovery drill.
3. Outfitter: later, integrate or broker this known workload across a second
   host. Do not implement five provider adapters before proving continuity.
4. Belay/Portage: optional tutoring/inference after computing is dependable.

ACCESS/Jetstream2 or temporary cloud credits can supplement capacity. They do not
replace baseline ownership, a course-end handoff plan or backups. No provider
purchase, institutional configuration change or allocation application is made
by this implementation.

## Evidence and remaining acceptance

Waypoint's `course-workspace/VALIDATION.md` records exact tests and limits of the
local synthetic rehearsal. Cairn adds API tests for class scoping and safe
workspace destinations. Real learner deployment requires the independent live
OIDC, wildcard TLS, roster revocation, capacity and recovery gates described in
those repositories. A one-host pilot is not high availability or automatic failover.

## October 7 implementation update

The initial PRs are merged. Cairn's additional grading-policy change is merged
and deployed on its existing pilot host; it addresses the specific learner-owned
manifest and operator per-step ceiling findings referenced above. Waypoint's
notebook/recovery recipe also passed a fresh Linux amd64 CI rehearsal after a
Linux archive-permission fix. Deployment and remaining infrastructure facts are
recorded in the current EDUCLOUD-STATUS.md. No dedicated notebook worker has
yet been selected or provisioned.
