# Final Output Contract

## Entry Gate

Do not generate final artifacts until the Red Team gate has passed.

The gate passes only when:

1. The confirmed requirement package, story-map direction, and QC checklist coverage have been reviewed for boundary, exception, hidden-assumption, logic, execution, evidence, and QC risks.
2. No unresolved `High` Red Team finding remains.
3. Every original `High` finding is remediated in the confirmed package and the user confirms the remediation is complete.
4. Any unresolved `Medium` or `Low` finding remains visible as `TBD`, owner-accepted risk, or a QC checklist item.

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

## Final Response

Return only:

- artifact paths
- validation performed
- unresolved `TBD` items
- any blocked gates
