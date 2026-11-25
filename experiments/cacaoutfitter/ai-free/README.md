# AI-free course image

Use this profile for the first INFO 511 NHANES classroom rehearsal. It layers the Math Inspector and the learner-only assignment onto Waypoint's ordinary course image. The course image contains Jupyter, its kernels and the Cairn handoff. Building or running it requires no Belay Classroom checkout, inference gateway, model weights, model key or Outfitter lease. The legacy wheel name `belay-math` identifies the standalone IDE extension. The NHANES panel reads the active cell through the notebook server and selects an authored response. It has no grade or monitoring channel.

From this directory, supply local clones of the [IDE](https://github.com/EduCloud-Ecosystem/educloud-ide) and [Waypoint](https://github.com/EduCloud-Ecosystem/waypoint). The builder exports only the pinned revisions specified in `build.py`. Use Python 3.12+ and a local Docker engine. The base build needs standard package repositories on a cold build. Panel installation runs offline.

```sh
python3 build.py --waypoint "$WAYPOINT_SOURCE" --ide "$IDE_SOURCE"
python3 check_panel.py --ide "$IDE_SOURCE"
```

The browser check uses the IDE checkout's Waypoint relay and the Python Playwright package with its Chromium browser installed. It starts the actual course image on an internal Docker network. It opens the assignment in JupyterLab, checks code and prediction cues, checks narrow layout, closes the panel, runs Python and verifies the saved notebook output. It then shuts down the kernel, reopens the panel and verifies static recognition in the same assignment. This check originally exposed a detached sidebar tab that could not be reopened. The pinned IDE revision fixes tab disposal. [Local test receipt](local-result.json)

For a host trial, publish the tested course image to the approved registry and select its immutable digest in Waypoint's course manifest. Start JupyterHub and Cairn using the normal identity and submission configuration. Omit the tutoring overlay, its launchers and credentials. New learner homes receive `INFO-511-NHANES/nhanes-wrangling.ipynb` when created. Existing homes retain their contents; distribute a fresh assignment directory through the course's normal delivery process. An image replacement alone does not update a nonempty home volume. The local check covers the notebook and panel. Hosted submission, recovery, capacity and human accessibility acceptance remain open.
