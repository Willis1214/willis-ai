# Final Output Contract

## Entry Gate

Do not generate final artifacts until the Red Team gate has passed.

If the final package includes visual, UI, HTML, dashboard, deck, or decision-material quality concerns, do not deliver it until the Front Taste module has been run or explicitly waived.

The gate passes only when:

1. The confirmed requirement package, story-map direction, and QC checklist coverage have been reviewed for boundary, exception, hidden-assumption, logic, execution, evidence, and QC risks.
2. No unresolved `High` Red Team finding remains.
3. Every original `High` finding is remediated in the confirmed package and the user confirms the remediation is complete.
4. Any unresolved `Medium` or `Low` finding remains visible as `TBD`, owner-accepted risk, or a QC checklist item.

`TBD` is allowed only when it is not blocking. A `TBD` is blocking when it can materially change the goal, boundary, acceptance standard, evidence requirement, delivery credibility, or whether the user should proceed. Blocking `TBD` items must be resolved or explicitly carried as Red Team `High` blockers before final artifacts are generated.

The Red Team module must start from the installed local `red-team` skill. If that skill recommends spawning the `red-team` Sub Agent, the main Agent owns the spawn call and final gate decision.

The Front Taste module must start from the installed local `front-taste` skill. If that skill recommends spawning the `front-taste` Sub Agent, the main Agent owns the spawn call and final delivery decision.

## Final Artifacts

Write final artifacts under `output/` unless the user gives a different directory.

| Artifact | Format | Default Filename | Required Template |
| --- | --- | --- | --- |
| PRD | Markdown | `output/<project_slug>_prd.md` | `references/prd-template.md` |
| User story map | HTML | `output/<project_slug>_user_story_map.html` | `references/user-story-map-template.html` |
| QC checklist | Markdown | `output/<project_slug>_qc_checklist.md` | `references/qc-checklist-template.md` |

## Generation Rules

1. Use the Red-Team-cleared confirmed structured summary as source of truth.
2. Preserve unresolved items as `TBD`.
3. Do not add implementation details unless confirmed by the user.
4. Keep PRD and checklist editable Markdown.
5. Keep HTML self-contained with embedded CSS and no required external dependencies.
6. Include detailed process flow and condition architecture in the HTML story map.
7. Carry accepted Red Team residual risks into the PRD Red Team Gate Summary or QC checklist.
8. Carry Front Taste must-fix findings or waivers into the PRD review summary or QC checklist when visual quality matters.

## Validation Checklist Before Delivery

| Check | Required Result |
| --- | --- |
| Files exist | All three artifacts are written to the agreed output path |
| PRD parse/readback | File can be read and contains project overview, input/output, user stories, boundary, constraints, and acceptance summary |
| HTML parse/readback | File contains valid basic HTML structure, process flow, condition architecture, and story table |
| Checklist readback | File contains severity rules and checklist table |
| TBD visibility | Any unresolved content remains visible as `TBD` |
| Cross-artifact consistency | Project name, users, input/output, boundaries, and QC items do not contradict each other |
| Red Team gate evidence | Final response states the gate passed or lists any blocked gate |
| Front Taste evidence | For visual / UI / HTML / deck / dashboard outputs, final response states the local `front-taste` skill was run or explicitly waived |

## Final Response

Return only:

- artifact paths
- validation performed
- unresolved `TBD` items
- any blocked gates
- Front Taste status when applicable
