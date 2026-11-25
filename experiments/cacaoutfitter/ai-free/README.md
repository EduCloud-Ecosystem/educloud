# AI-free course image

Use this profile for the first INFO 511 NHANES classroom rehearsal. It layers the Math Inspector and the learner-only assignment onto Waypoint's ordinary course image. The course image contains Jupyter, its kernels and the Cairn handoff. Building or running it requires no Belay Classroom checkout, inference gateway, model weights, model key or Outfitter lease. The legacy wheel name `belay-math` identifies the standalone IDE extension. The NHANES panel reads the active cell through the notebook server and selects an authored response. It has no grade or monitoring channel.

From this directory, supply local clones of the [IDE](https://github.com/EduCloud-Ecosystem/educloud-ide) and [Waypoint](https://github.com/EduCloud-Ecosystem/waypoint). The builder exports only the pinned revisions specified in `build.py`. Use Python 3.12+ and a local Docker engine. The base build needs standard package repositories on a cold build. Panel installation runs offline.

```sh
python3 build.py --waypoint "$WAYPOINT_SOURCE" --ide "$IDE_SOURCE"
python3 check_panel.py --ide "$IDE_SOURCE"
```

The browser check uses the IDE checkout's Waypoint relay and the Python Playwright package with its Chromium browser installed. It starts the actual course image on an internal Docker network. It opens the assignment in JupyterLab, checks code and prediction cues, checks narrow layout, closes the panel, runs Python and verifies the saved notebook output. It then shuts down the kernel, reopens the panel and verifies static recognition in the same assignment. This check originally exposed a detached sidebar tab that could not be reopened. The pinned IDE revision fixes tab disposal. [Local test receipt](local-result.json)

Run the [saved submission rehearsal](journey.md) against a disposable Cairn classroom and the [capacity rehearsal](capacity.md) against separate JupyterHub sessions. The recorded local image is Linux arm64. For a host trial, build and rerun on the intended architecture, publish the tested course image to the approved registry and select its immutable digest in Waypoint's course manifest. Start JupyterHub and Cairn using the normal identity and submission configuration. Omit the tutoring overlay, its launchers and credentials. In a new learner home, open `nhanes-wrangling.ipynb` in the top-level file browser. Waypoint preserves the selected paths when sending files to Cairn, and the grading template expects the four deliverables at this level. For an existing home, back it up and deliver the starter at the same level after checking for filename conflicts. Replacing an image alone does not populate an existing home. Hosted submission, recovery, capacity and human accessibility acceptance remain open.

The [pilot testing guide](../../../docs/pilot/AI_FREE_TESTING.md) assigns work for the learner journey, class capacity, instructor review and hosted acceptance.
