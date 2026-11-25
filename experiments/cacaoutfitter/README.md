# Cacaoutfitter classroom pilot

Use CACAO to describe the AWS course host, Waypoint to divide its notebook capacity among learners, and Outfitter to reserve scarce resources for finite periods. A learner's normal workspace lasts across group sessions. Ending a model or worker reservation must leave that workspace usable.

## Division of responsibility

| Component | Operation | Lifetime |
| --- | --- | --- |
| CACAO AWS recipe | Select the AWS account, region, one prepared host image, instance size, subnet and security group. Attach an existing encrypted course disk. | Operator-managed course deployment |
| Waypoint and JupyterHub | Admit the current roster, start a container on login, mount its learner's home and apply CPU, RAM and active-server limits. | Notebook process per session, home across sessions |
| Outfitter | Admit an eligible request against course compute allowance, reserve a named scarce device or worker until a deadline, account for occupancy and verify release. | One bounded reservation |
| Portage and model runtime | Route approved model aliases to eligible endpoints, enforce request concurrency and token budgets, and keep uncertain usage outstanding. | One inference request within the resource window |
| Belay Classroom and Cairn | Provide optional help and allow normal notebook submission to GitHub through Cairn's independent workflow. | Course activity and retained submission |

The Outfitter row is the intended scope. Its local Docker broker can already time and clean up a pinned CPU job. Binding a model reservation to the actual Ollama process and device remains implementation work. For model outfitting, match an approved model revision to a registered device with sufficient memory, a compatible runtime and a free slot. Bind the reservation to that device and model, the course and the original deadline. For CPU or accelerator jobs, match the job’s resource requirements to the remaining course allowance and available capacity. If no eligible device is available, surface that result before dispatch. Portage remains authoritative for model requests and tokens. A busy device should return an explicit busy status with a retry path. An expired reservation should disable the model option while ordinary notebook work and submission continue. A waiting queue and per-learner fairness remain design choices.

## CACAO reuse on AWS

CyVerse publishes both a JupyterHub reference on OpenStack and an AWS single-image template. The latter's source revision in the catalog is `8d5d37c083c08a20ce3508b05566f61b3e96f63b`. Its optional AWS Budgets notifications address cloud spending. The course also needs decisions at the time a learner requests scarce compute. The AWS template here adopts the upstream CACAO metadata structure, AWS image, flavor and region parameter types, and instance-list output names. Its infrastructure code is specific to an existing course network and independently retained storage. It does not require a Jetstream2 account. [CACAO AWS catalog entry](https://cacao.jetstream-cloud.org/templates/template-cu3vj3v3clcc73fvrqpg) · [AWS recipe source](https://gitlab.com/cyverse/cacao-tf-aws-ops/-/tree/8d5d37c083c08a20ce3508b05566f61b3e96f63b/single-image) · [JupyterHub reference](https://docs.jetstream-cloud.org/ui/cacao/deployment_jupyterhub/)

The template root for a future CACAO import is [aws-host](aws-host). It creates one private EC2 instance and one attachment. The course home volume, subnet and security group already exist and remain independently owned. The volume must carry the matching `EduCloudCourse` tag. Deleting the deployment stops the host before detaching the volume. The disposable root disk is deleted with the host. Before a planned replacement, stop the course, confirm a recoverable backup and unmount learner storage. Review the plan for the intended account. A matching volume and a successful attachment establish neither a mounted filesystem nor a working backup.

This recipe provisions the host layer. The prepared AMI, private HTTPS route, wildcard TLS, institutional identity and approved Waypoint manifest are operator inputs. Configure the AMI to leave course services stopped until the intended filesystem is mounted and verified by volume identity and filesystem UUID. Follow Waypoint's course manifest and recovery workflow for images, home paths, quotas, identity and activation. Keep credentials out of CACAO metadata, Terraform variables and state. [Waypoint course setup](https://github.com/EduCloud-Ecosystem/waypoint/blob/af44909f8a0757b1f15c35d74414a7d47f559a39/course-workspace/COURSE-MANIFEST.md)

For 20–25 learners, test three groups first. The largest group has nine learners and one instructor. Configure the intended ten simultaneous notebook seats in Waypoint and start with one shared model slot on a managed device. Cairn owns the academic roster. Waypoint enforces current workspace membership, the operator holds cloud credentials, and Portage mediates model access. The rehearsal below uses two synthetic accounts. Its small RAM limit exercises enforcement and supplies no course sizing benchmark.

## Reproduce the local checks

From the template directory, initialize the pinned provider and run:

```sh
tofu init -backend=false
tofu fmt -recursive -check
tofu validate
tofu test
```

Terraform 1.12.2 and OpenTofu 1.12.0 both validated the recipe and passed the four cases with AWS provider 6.74.0. All infrastructure tests use a mock AWS provider and plan operations. Test cases cover a private host with a retained disk, an incompatible network, a cross-zone disk and an unencrypted disk. Validate [.cacao/metadata.json](aws-host/.cacao/metadata.json) against CyVerse's [v3 import schema](https://gitlab.com/cyverse/cacao-common/-/raw/50d750fd90d692b71c4cf8ebe46d5521cf4dc6ec/template/metadata-schemas/v3/schema.json). Schema and plan checks precede a real CACAO import and an authorized AWS trial.

For the independent classroom check use Waypoint `af44909f8a0757b1f15c35d74414a7d47f559a39`, Outfitter `bfc3ac48acbae7fafb7893ee35a9332f848d5c15`, a local Docker engine and a Python environment with Waypoint's `requests` and `websocket-client` test dependencies. Build the Hub and course images from the two Dockerfiles at that Waypoint revision. Build Outfitter's `./cmd/outfitter` binary. Supply local immutable Docker image IDs. The job image must contain Python and support a non-root, network-disabled process. The script uses Waypoint's own login, save and kernel probes.

```sh
python rehearse.py --waypoint "$WAYPOINT_SOURCE" --outfitter "$OUTFITTER_BINARY" \
    --hub-image "$HUB_IMAGE_ID" --course-image "$COURSE_IMAGE_ID" --job-image "$PYTHON_IMAGE_ID"
```

The runner creates a disposable Hub bound to loopback, two learner containers, two home volumes and per-user networks. It saves separate markers while the Outfitter job is active, verifies release at the original deadline, saves and executes Python again, restarts the Hub and reads both markers from freshly spawned notebooks. It removes its disposable classroom resources on exit. A failed check exits nonzero. The test exercises a timed CPU job. Real model serving, cross-host recovery, GitHub submission and ten concurrent notebooks each need separate evidence.

## Verification checkpoint

The [two-learner receipt](local-result.json) records the image IDs, component revisions, original deadline, observed finish, accounting method and cleanup. The November 24 local run passed on an ARM Mac with a Docker 29.8.2 engine. Outfitter's watchdog closed the 20-second job and verified cleanup. Both users wrote to separate homes during the job, executed code after expiry and recovered their own work after the Hub restarted. The 20 CPU-seconds charged are the reserved upper bound.

Development exposed three issues in the rehearsal itself. The Hub needed Docker name resolution on its initial network. The broker and watchdog can record different terminal states at the original deadline. Docker can assign a new loopback port on restart. The successful run joined a named network, checked both deadline and cleanup evidence, and rediscovered the bound port after restart.

The umbrella change is on `codex/cacaoutfitter-pilot`, based on `1b4c103df7a0860eb28753cd73465b858d1fb9b9`. The integration guide links this experiment. The CACAO schema check, Terraform and OpenTofu plan tests, and standard umbrella checks passed locally. Live CACAO import, the AWS image and storage recovery, the real model-device lease and full-group capacity remain open. The next device test should hold two notebooks open, grant one reviewed device/model pair, verify a second request sees a busy slot, and confirm that expiry releases the actual runtime before the next group can acquire it.
