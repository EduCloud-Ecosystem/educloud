# EduCloud interface assessment and Arizona design alternatives

Prepared 2026-11-14 (America/Los_Angeles). Status: two interactive design proposals, not deployed application changes. The working classroom pilot is preserved.

## Recommendation

Use **Studio Classic** as the classroom pilot direction. Retain Jupyter's familiar file tree, notebook tabs, code cells, run/save controls and explicit submission. Apply a unified Arizona palette and simplify the tutoring and submission handoffs. **Studio Focus** offers the same workflow with a collapsed file tree, quieter tool rail, wider reading area and navy course masthead. It is an alternative default, not a separate student product.

The existing IDE is the strongest foundation. EduCloud's main design weakness is fragmentation between components, not lack of features. Replacing it with a dashboard would add navigation before the learner can work. The highest-value improvements are fewer competing instructions, predictable action placement, readable status and a clear receipt.

## Coverage and evidence boundaries

| Surface | Inspection | Assessment and proposed treatment |
| --- | --- | --- |
| Waypoint Learning Studio, native notebook and integrated tutor | Actual local live browser interaction, screenshots and bounded automated end-to-end acceptance | Familiar IDE works. Keep native editing/run/save. Make the tutor question prominent; reveal prediction and sharing confirmation when needed. Move provider details out of the main reading path. |
| Saved-file picker and Cairn submission/receipt | Source, prior screenshots and successful live end-to-end acceptance | Preserve explicit selection, preview and confirmation. Make saved versus unsaved work unmistakable. Put the receipt above completed controls; show received, checked and reviewed as different states. |
| Cairn instructor console, assessment, roster, calibration and grade delivery | App/sidebar/style source plus targeted component headings/actions; not every admin route rendered | Warm paper/vermilion identity conflicts with classroom branding. Use Arizona tokens, task-oriented headings and ordinary tables. Keep calibration, publication and grade delivery explicit instructor actions. |
| Cairn student work/results | Student-page source; not a complete live route audit | Unify typography and color with Learning Studio. Retain receipt identity and result details. A successful checker is not a published grade. |
| Belay-classroom reference workbench/widget/demo | HTML/CSS source; not all reference demos rendered | Electric-blue/teal identity and developer controls are unsuitable as the classroom shell. Borrow behavior, not the full development workbench UI. Keep the integrated tutor compact and optional. |
| Portage instructor walkthrough | Full small HTML source read | Teal/gold palette is inconsistent. Keep it an operator diagnostic, adopt shared tokens, and retain request/accounting/stop controls. Do not expose it as another student navigation destination. |
| Outfitter native-SU implementation | Tracked-file inventory at the pin below | No standalone HTML/CSS/TSX/Vue surface found in this inspected implementation. Represent verified lifecycle status in operator views; do not invent a learner-facing Outfitter dashboard. |
| Waypoint research workspace | Static page and stylesheet source | Teal/mint cards form a separate product language. Shared brand tokens can apply later; research project navigation should remain separate from Learning Studio. |
| EduCloud umbrella | Repository guidance and shared coordination | Own the cross-component design contract here; component code changes belong in the component repositories. |
| Wayfare/mobile, every historical prototype, every instructor dialog | Not comprehensively inspected | Physical-device, full admin-route and human accessibility acceptance remain unexecuted. Do not describe this as an exhaustive live audit of every EduCloud screen. |

## Design findings

1. **Intuitiveness:** the notebook is recognizable; transitions into tutoring and submission ask the learner to understand too much infrastructure vocabulary. Use “Ask tutor,” “Review & submit,” “Files received,” and “Instructor review” for tasks. Preserve component names in operational details.
2. **Comfort:** reduce repeated explanatory paragraphs, uppercase micro-labels and competing cards. Offer help at the point of uncertainty. Use concise, non-punitive recovery copy and leave the work visible whenever authority permits.
3. **Elegance:** one spacing rhythm, one neutral UI type system, consistent line weights and restrained corners will do more than decorative backgrounds or large metrics. Avoid heavy dashboard styling around code.
4. **Brand coherence:** replace vermilion, electric blue, teal and gold as primary UI identities with Arizona Blue and Red. Keep semantic states distinct and labeled; red is not the only indication of an error.
5. **Trust:** sharing, saving, transferring, submitting, checking and grading are separate actions. Never silently rewrite the learner's assistance declaration. Receipt hashes remain inspectable details, not the main success message.
6. **Continuity:** the live review window expired during the first manual attempt. A future design should separate tutor expiry from a separately authorized save/submission window. This must not extend a reservation, alter original deadlines or infer new admission authority. The recovery view in these proposals is illustrative, not an implemented fix.

## Brand contract

Primary sources consulted:

- [University of Arizona colors](https://marcom.arizona.edu/brand-guidelines/colors): Arizona Blue `#0C234B`, Arizona Red `#AB0520`, Cloud `#E5EFF7`, Caliche `#F2EFEA`, White `#FFFFFF`.
- [University of Arizona typography](https://marcom.arizona.edu/brand-guidelines/typography): Proxima Nova is the primary digital sans serif. The prototypes use a system UI stack; they do not bundle or claim to license Proxima Nova.
- [Arizona Bootstrap color contrast](https://digital.arizona.edu/arizona-bootstrap/v5/docs/5.1/getting-started/color-contrast/): check actual combinations rather than assuming a brand color makes a UI accessible.

Use Blue for navigation and structural identity; Red for the principal next action and a restrained identifying rule. Use Cloud sparingly for selected rows and context. Keep code/output surfaces neutral. Avoid coloring every component differently. Do not construct an unofficial university logo or imply institutional certification from the palette.

`brand-tokens.css` is a proposed, namespaced shared contract. It is not imported into any production app. Its names are design proposals, not newly accepted API contracts.

## Two proposals

`studio-proposals.html` is the canonical interactive fragment. A byte-identical copy is presented in this chat's durable visualization directory. The renderable preview is a convenience wrapper, not a second source of truth.

- **Studio Classic:** visible file tree, familiar notebook chrome, white masthead with a thin red line, compact controls and an optional right-hand tutor. Recommended for INFO 511 because it changes the fewest learned conventions.
- **Studio Focus:** collapsed files, slim workspace rail, navy course masthead, larger notebook reading area and more breathing room. Files and help remain one action away. It offers focus without adding a new dashboard or workflow.

Both include editable synthetic notebook/file text, illustrative cell output, explicit tutor-sharing consent and a prediction checkpoint, assistance-declaration review, unsaved-work recovery, four-file submission confirmation, a receipt, a small instructor view, and a proposed help-expiry state. Neither executes notebook code, sends model requests, saves learner files, publishes a submission, grades a student or changes access.

The required file names match the selected task: `nhanes-wrangling.ipynb`, `tidy-nhanes.csv`, `explanation.md`, `assistance.md`. Demo row identifiers and receipt contents are explicitly synthetic. These examples do not replace actual NHANES data or acceptance fixtures.

## Validation and failures retained

- JavaScript syntax check: passed with Node `--check`.
- Fragment structure, two named variants, no external URLs or transport APIs: passed source checks.
- Calculated WCAG contrast: white on Arizona Red **7.57:1**; white on Arizona Blue **15.47:1**; secondary text `#506075` on white **6.42:1**, on Cloud **5.51:1**; main text `#172B48` on white **14.23:1**; dark-mode secondary `#AFBDD0` on `#111D30` **8.87:1**. These are selected-pair calculations, not a complete accessibility audit.
- Source includes labeled native controls, visible focus, modal focus containment/return, Escape dismissal, local state, 320px responsive rules and coarse-pointer target rules. Rendered keyboard, narrow-layout, theme and human accessibility checks remain **unexecuted** for these new proposals.
- Preview wrapper generated successfully. Its generic host-API warning was inspected: fragment uses only optional widgetState/setWidgetState, with no model or network action.
- **Blocked check:** the preview browser rejected the `file:` URL under its protocol security policy. No alternate browser, local server workaround or bypass was attempted. No screenshot or rendered-pass claim is made for the new mockups.
- Source review caught and corrected a draft interaction that automatically rewrote the assistance declaration after a hint. The final proposal prompts explicit review instead. Also corrected dialog focus return and unsaved-status continuity across role previews.

The existing live pilot has a separate successful eight-stage run at Waypoint source `d19cda90ab41d5306b78b47acd7b8e200238c685`, documented in `docs/learning-studio-live-test-v1.md` at `e29c373ff8f3420371180d63eb3b8238d70750d4`. Six transport requests across the incomplete first review and completed rerun cost $0.0053728, with no new unresolved usage. This supports the live workflow, **not these newly authored design alternatives**. The historical unknown liability remains separate.

## Pinned inspection map

All six selected trees were clean before this design record. Existing dirty primary checkouts, historical worktrees, private evidence and original prototypes were preserved.

| Repository | Branch | Exact inspection revision | Worktree |
| --- | --- | --- | --- |
| educloud | codex/nhanes-live-readiness | 9df06110d83f2235de1491a3e829d342ccb32295 | /Users/gregchism/dev/.educloud-worktrees/educloud-classroom-full-stack-v1 |
| Waypoint | codex/nhanes-live-tutoring | e29c373ff8f3420371180d63eb3b8238d70750d4 | /Users/gregchism/.codex/worktrees/waypoint-runtime-release/waypoint |
| Cairn | codex/cairn-nhanes-handoff | 2eb0a0415f791f7d53734d5909a3a3d7454e34f0 | /Users/gregchism/.codex/worktrees/cairn-nhanes-handoff/cairn |
| Belay-classroom | codex/system-one-classroom-consumer-v1 | c5a27073e74b9eeb7ab697190915378b50132883 | /Users/gregchism/dev/.educloud-worktrees/belay-classroom-system-one-consumer-v1 |
| Portage | codex/nhanes-live-tutoring-v1 | b72881f009e61e1311b6e46b92b42841991fd163 | /Users/gregchism/.codex/worktrees/classroom-live-tutoring/portage |
| Outfitter | codex/native-su-cleanup | 07e8e5001b3db5569678b3c552d624d7348ff3d6 | /Users/gregchism/dev/.educloud-worktrees/outfitter-native-su |

These are inspected implementation revisions, not claims of merge or deployment. This change adds only a local design record, tokens and proposals to the umbrella branch. No application source, cloud resource or production state changed.

## Next implementation gate

1. Review the two interactive proposals; default recommendation is Classic.
2. Apply its tokens and hierarchy to Waypoint's tutor/picker and Cairn's submission/receipt first, preserving native notebook behavior and all existing acceptance controls.
3. Qualify rendered desktop/narrow, keyboard/focus, light/dark and actual save/hint/submission/error paths against the selected implementation. Retain failures; do not use this preview's simulated outcomes as test evidence.
4. Align Cairn instructor/student styles and operator-facing Portage styles. Keep Outfitter authority and research-product navigation separate.
5. Implement separately authorized recovery timing as behavior work with explicit admission, expiry, retention and cleanup tests, not as a cosmetic patch.
