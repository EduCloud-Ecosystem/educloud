# INFO 511 instructor and volunteer rehearsal

Use a disposable copy of the AI-free NHANES assignment and synthetic course accounts. The volunteer takes the learner's role and describes what they understand. The instructor observes, then asks, “What would you do next?” before offering help. Record the first obstacle even if a workaround succeeds.

**Session** ______  **Date** ______  **Instructor / volunteer roles or aliases** ______
**Course image digest** ______  **Host** ______  **Browser, zoom, input and assistive technology** ______

For each case enter **pass**, **fail**, or **not run** and a brief observation. Keep names, course records, links to recordings and private conversations off this sheet. These are expected outcomes for a future human review. [Course profile and proposed assessment](AI_FREE_FIRST_PILOT.md)

## Notebook and accessibility

| Case | What to try and what to observe | Result / observation |
|---|---|---|
| 1. Selected function | In the learner-work cell, type `joined = demographics.merge(bp_readings)`. Select the line, then replace it with `long = joined.melt()`. The first cue asks about matching keys and row counts. The second asks what identifies a row after reshaping. Ask the learner to explain that difference. | ______ |
| 2. Equivalent answer | In the unit-prediction cell enter “One row per reading.” Then try “Every record pairs a person with a measurement occasion.” The first gets the reading-level cue. The second gets the open unit-of-observation question. Both answers remain editable and neither receives a grade or authorship label. | ______ |
| 3. Misleading text | Enter `# data.merge()` as the only line of the learner-work cell. The panel gives general assignment guidance. The comment generates no join-specific cue, allegation or follow-up assignment. | ______ |
| 4. Keyboard and screen reader | Without a pointer, select a prediction, read its cue, close the panel, return to the notebook, run `print(6 * 7)`, save, then reopen the panel. Check visible focus, intelligible spoken status after the cue changes and saved output of 42. Record any action requiring a pointer or sight. | ______ |
| 5. Zoom and submission | At 200% zoom, find and read a cue, dismiss the panel and use a **prepared synthetic submission** to preview all four filenames, confirm once and locate the receipt. Check that controls, focus and receipt text remain reachable. Identify the actual destination or mark the submission portion not run. | ______ |

## Explanation assignment tabletop

Use a paper storyboard for this rehearsal. No recording, upload, student contact or gradebook entry is needed. The course currently omits the tutor action. The reminder and alternate assessment are proposals.

| Situation to present | Expected instructor action | Result / observation |
|---|---|---|
| The learner pastes their own notes, uses assistive software, or disputes an ambiguous flag and declines a voluntary recording. | Offer private clarification. Retain the ordinary rubric while use is unconfirmed. The flag, paste, declined recording and accessibility tool produce no deduction. | ______ |
| The learner discloses using AI to explain a join. The instructor has published the alternate route before the assignment. | Identify the relevant decision with the learner. Manually assign the explanation and give its deadline, rubric and alternative. A brief paraphrase of the prompt and what the learner kept or changed suffices. | ______ |
| The learner can explain their reasoning but cannot use the recorder or declines the recording format for the assigned explanation. | Offer an accessible equivalent, such as a private instructor conversation. Apply the same criteria and maximum score. For a missed assessment, use the announced ordinary extension or resubmission process. | ______ |
| A peer can view the mock folder, or the volunteer cannot use it with their normal access tools. | Mark access failed or not run and name the owner of the fix. Use a new test account and an institutionally approved synthetic test asset to verify instructor/submitter access and peer exclusion before enabling video. | ______ |

### Score the same synthetic work

Supply two fictitious participant keys. A has a matching record with readings 110, blank and 114. B has no matching record. Six long rows should remain. A's second reading and B's three readings are missing for different documented reasons. These rows illustrate the explanation exercise only.

- **Ordinary route.** Give both reviewers a packet with a correct CSV, no independent notebook checks, reproducible code and a satisfactory short explanation, and a complete assistance declaration. The published categories yield **4 + 0 + 2 + 1 = 7/10**.
- **Explanation route.** Use that same 7/10 packet. The storyboard paraphrases the task and purpose (1/1), traces A's second reading from input to output (1/1) and explains why B still needs rows (1/1). It predicts that dropping missing readings leaves two rows and verifies this by counting the six-row example (1/1). It gives no limitation or supporting evidence for what the missingness means (0/1). Expect **0.5 × 7 + 4 = 7.5/10**. A private conversation demonstrating the same reasoning earns the same score.
- **Ceiling check.** A 10/10 ordinary submission and a 5/5 explanation yield **10/10**. Record one assignment score. A flag has no score of its own.

**Independent scores before discussion** Ordinary ______ / ______  Explanation route ______ / ______
**Difference and resolution** ______

## Human decision

**Instructor** ______  **Volunteer** ______  **Date** ______
**Concept cues** ______  **Accessibility and submission** ______  **Rubric calibration** ______
**Institutional Panopto access actually verified** yes / no / not run
**Decision for the tested activity** accept / revise and repeat / incomplete
**Failed or unrun case, owner, next action and retest date** ______

The lead instructor keeps the completed worksheet in the approved course location. A tabletop result covers the assessment design only. Hosted access, private-folder settings and classroom capacity have their own verification.
