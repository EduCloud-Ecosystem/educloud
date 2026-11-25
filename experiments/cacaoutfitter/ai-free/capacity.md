# Rehearse the AI-free classroom's busiest group

For 25 learners in three groups, rehearse nine learner notebooks and one instructor notebook together. The instructor seat runs the same course workload. For two groups of 25 learners, rehearse the larger group of 13 plus an instructor with `--seats 14`.

Run this from the AI-free experiment directory on the machine being measured. Use a Linux Docker engine with cgroup v2 and a local Unix socket (including Docker on a workstation), Python 3.12+ with `requests` and `websocket-client`, a Waypoint Git clone and the AI-free image built with [the course image instructions](README.md). The runner uses preloaded images and resolves their immutable IDs. To build the matching Hub image from the pinned source:

```sh
hub_build=$(mktemp -d)
git -C "$WAYPOINT_SOURCE" archive af44909f8a0757b1f15c35d74414a7d47f559a39 course-workspace/hub |
  tar -x -C "$hub_build"
docker build -t educloud-capacity-hub:af44909 "$hub_build/course-workspace/hub"
```

For a disposable AWS test VM, run locally **on that VM**:

```sh
python3 capacity.py --waypoint "$WAYPOINT_SOURCE" \
  --hub-image educloud-capacity-hub:af44909 --course-image educloud-info511:ai-free \
  --seats 10 --memory-mib 2048 --receipt capacity-host-result.json
```

For a smaller local baseline, use `--seats 3 --memory-mib 768`. Before launch the runner checks Docker's available memory against the sum of all notebook limits, 512 MiB for JupyterHub and 1 GiB of headroom. At 2 GiB per seat, ten seats require 22,016 MiB available and fourteen require 30,208 MiB available. This threshold is a test startup guard. The actual peaks are recorded separately.

The runner verifies the Hub configuration against the pinned Waypoint source, then substitutes the synthetic roster only in a temporary copy mounted into a fresh, loopback-only Hub. Students launch through its usual sign-in and DockerSpawner path, in waves of two. Each kernel checks for the starter notebook in the course workspace root (`/home/learner/work`), reads the NHANES tables from its `data/` directory and waits until the entire cohort is ready. It runs the completed exercise from the pinned Waypoint operator fixture 30 times, including its data checks, and saves the 192-row CSV and a seat-specific result. The runner loads instructor code from the supplied operator checkout at runtime. The learner image contains the starter only. A passing run requires a common interval of computation across **all** seats, separate volumes and networks, enforced CPU and RAM limits, zero recorded notebook OOM kills, and exact output recovery after every server is stopped and respawned. One authenticated learner also attempts to read another active notebook’s saved result. A separate rostered learner must receive a full-classroom response, then enter and open the assignment after one seat is released. The other seats must keep their original notebooks and saved outputs throughout the handoff. The runner removes its uniquely labeled resources and writes the receipt after cleanup. Per-seat cgroup peaks include the notebook server, kernel and filesystem cache. Their sum is not a measurement of simultaneous host memory use.

The [local receipt](capacity-local-result.json) is a three-seat Docker measurement. To record a ten- or fourteen-seat result, run the command on the intended host with the chosen group size. Institutional sign-in, public routing, home quotas, submission, browser response time and a full class period require their own rehearsals. This capacity run uses a fresh home per synthetic account and exercises the notebook alone.
