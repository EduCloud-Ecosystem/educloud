# INFO 511 pilot without generative AI

The first classroom pilot uses Waypoint/JupyterHub, the EduCloud IDE's authored Math Inspector and Cairn submission to GitHub. CACAO describes the AWS host. Belay Classroom, Portage, model devices, model credentials and inference leases are optional future additions. Outfitter becomes relevant if a course requests scarce compute. The host still needs real sign-in, capacity, recovery, privacy/accessibility review and instructor acceptance. The existing readiness record remains the reviewed evidence for its dated configuration.

## What the learner sees

In the NHANES notebook the Math inspector opens when the notebook loads. Selecting a join, reshape or missingness operation brings up a question written by the instructor. Typing the standalone answer “one row per reading” in the unit-prediction cell prompts the learner to explain what ties two readings to the same person. Other wording receives an open conceptual question. The panel recognizes a small set of patterns and offers no verdict on correctness or authorship. No model runs. Learners can close the panel and continue in ordinary Python. [Build and rehearsal](../../experiments/cacaoutfitter/ai-free/README.md)

## Assignment design and private reminders

Before opening an assignment, publish its AI rule, permitted resources, disclosure route, explanation rubric and available accommodations. A recommended first rule is independent predictions, code and reasoning using course materials, ordinary documentation, approved accessibility tools and the authored panel. Ask learners to predict an output before running code, check one row by hand and explain a changed case. These steps work when a learner also has a phone or an external browser.

For a later lightweight checker, distinguish a directly observed action from an inference about who wrote an answer. A request to a disabled **first-party** tutoring action could display a local, private reminder before dispatch. The message should say what happened: “AI tutoring is off for this assignment. You can use the Math inspector or continue in your notebook.” A blocked attempt sends no prompt and assigns no work. The current pilot omits the tutor action altogether. A student can also declare outside assistance in the existing submission declaration. EduCloud cannot observe AI use on another device. Keep the checker out of clipboard contents, typing cadence, browser history and writing-style classification. Do not treat Math Inspector activity, paste, accessibility tools or correct answers as AI-use evidence. Arizona's teaching guidance explains the false positives and limits of detector scores. [University of Arizona instructor guidance](https://libguides.library.arizona.edu/ai-literacy-instructors/policies)

## Proposed explanation assignment

Publish this option prospectively. When a student discloses relevant AI assistance, or an instructor confirms a specific use with the student, the instructor assigns the explanation route. A student may clarify a mistaken concern privately before reassignment. An unresolved flag leaves the original grading route in place. Scheduling a checkpoint uniformly or offering the same route voluntarily can also give instructors comparable evidence. The pilot software does not activate this proposal, assign a penalty or send grades.

Give the learner a short, private Panopto assignment, with a suggested length of 3–5 minutes. Ask them to show one cell from their own submission and address four things:

1. State the assignment question in your own words. If you used an AI prompt, paraphrase what you asked, why, and what you accepted or changed. Omit personal information and private chat logs.
2. Explain why the operation fits the question. Trace one participant and one reading from input to output.
3. Change one assumption, predict what will happen, then run or check it. Explain any difference.
4. Identify one limitation or uncertainty and the evidence you used to check the result.

For the existing 10-point rubric, first score the submitted work on its usual 10-point scale. On the explanation route award **0.5 × ordinary score + explanation score (0–5)**. Award up to 1 point for question/prompt and purpose, 2 for the logical walkthrough, 1 for prediction and verification, and 1 for interpreting the result and its limits. For example, 8/10 on the ordinary rubric and 4/5 on the explanation yields 8/10 overall. A 10/10 remains available. Grade conceptual reasoning. Completing the ordinary assistance declaration earns the same credit whichever route the student takes. Delivery polish, accent, camera presence, declared use and a checker signal carry no separate deductions. Never count the explanation twice. Communicate the deadline, ordinary extension/resubmission process and equivalent accessible options in advance.

Use the university course's Panopto assignment folder with peer viewing disabled. Record the screen and narration or accept an equivalent accessible demonstration such as a captioned screen recording or instructor conversation assessed against the same rubric. Confirm who can view a test recording before assigning it. Use the institution's approved retention and access settings. Keep videos and transcripts in the institutional system. Instructors can run the first trial manually in Brightspace, record rubric points once and keep video links out of GitHub, tutor prompts and learner telemetry. [Instructor folder setup](https://help.intech.arizona.edu/article/643-create-assignment-folder) · [Student recording or upload](https://studenthelp.intech.arizona.edu/article/577-create-and-post-video-to-panopto-assignment-folder)

## Before teaching

1. Have an instructor review the authored cues and scoring examples against the actual assignment, and rehearse the alternate submission with a test student account. Confirm the institutional recording/accessibility arrangements and the course's assessment policy.
2. On the selected host, verify a rostered learner can open the assignment, inspect a concept, run, save, preview, submit to the intended private GitHub repository and recover the receipt while inference services are absent. Repeat with the panel closed. Test keyboard navigation, zoom and a screen reader with the intended course workflow.
3. Rehearse the largest staggered group (nine learners plus an instructor), restore saved work on a replacement host and test access revocation. If AI is enabled in a later course profile, review its independent data-flow, placement, endpoint and instructional gates before activation.
