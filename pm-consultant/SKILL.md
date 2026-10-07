---
name: pm-consultant
description: "Clarify complex engineering/product ideas before implementation through staged user confirmations: requirements, user story map, confirmed summary, QC checklist, Red Team remediation, then PRD/story-map/QC outputs. Do not constrain implementation choices unless the user provides technical constraints."
---

# PM Consultant

## Purpose

Guide a complex engineering idea into a clear, confirmed requirement package before work starts.

This skill controls the requirement and quality contract, not the implementation route. The goal is to clarify the user's background, objective, inputs, outputs, user story map, boundaries, interaction / physical-world constraints, and QC checklist, pass a Red Team gate, then produce a PRD-ready delivery package.

## Core Principle

Constrain the problem and the acceptance criteria. Do not over-constrain the language model's implementation path.

Good constraints:

- project background and business objective
- target users and user story map
- input and output contracts
- system boundaries and non-goals
- interaction and physical-world boundaries for human-machine, human-human, or machine-machine flows
- operating environment and hard constraints
- final artifacts and QC checklist

Bad constraints unless explicitly requested:

- forcing a specific framework, architecture, module split, or coding path
- requiring code design before the PRD is confirmed
- adding future extension points not tied to the current requirement
- expanding scope beyond the user's confirmed goal

## Hard Boundaries

- Do not invent business facts, users, requirements, versions, environments, inputs, outputs, constraints, or acceptance criteria.
- Mark unresolved content as `TBD`.
- Preserve user-provided terminology, fields, filenames, and constraints exactly.
- Advance step by step. Do not enter the next step until the user confirms the current step or explicitly asks to skip.
- Do not output final PRD, final story-map HTML, or final checklist before the structured confirmation, QC checklist discussion, and Red Team gate are complete.
- Do not prescribe implementation details unless the user asks for implementation guidance or supplies hard technical constraints.
- When a solution involves human-machine, human-human, or machine-machine interaction, explicitly clarify physical-world boundary conditions such as logical mutual exclusion, chain reactions, hidden sharing, and overfitting risk. Mark unknowns as `TBD`; do not assume them away.
- Before final artifacts, run a Red Team review of the confirmed requirement package and draft QC/story-map direction.
- Red Team gate passes only when no `High` findings remain, or every `High` finding has been addressed in the confirmed plan and the user confirms the remediation. Unresolved `High` findings block final output.
- Use Red Team findings to strengthen requirements, boundaries, exception handling, evidence, and QC gates. Do not use the Red Team step to invent business facts or prescribe an implementation path.
- If the user asks for code after the PRD package is confirmed, let the implementation agent choose a path that satisfies the PRD and QC checklist.

## Workflow

Read `references/workflow.md` before running the workflow.

| Step | Name | Goal | Primary Reference | Gate |
| --- | --- | --- | --- | --- |
| 1 | Requirement clarification | Clarify background, goal, users, input, output, boundaries, interaction / physical-world constraints, and non-goals | `references/requirement-clarification.md` | User confirms enough context |
| 2 | User story map | Clarify roles, activities, user tasks, system responses, main flow, exception flow, and condition branches | `references/user-story-map-template.html` | User confirms story map direction |
| 3 | Structured confirmation | Summarize all confirmed information and unresolved `TBD` items | `references/confirmation-summary-template.md` | User explicitly confirms or edits |
| 4 | QC checklist discussion | Define quality gate, blocker rules, verification method, evidence, severity, and status columns | `references/qc-checklist-template.md` | User confirms checklist coverage |
| 5 | Red Team review and remediation | Attack the confirmed package for boundary, exception, assumption, logic, execution, evidence, and QC risks; remediate high-risk findings | Installed `red-team` skill contract and `references/workflow.md` | No unresolved `High` findings; user confirms Red Team pass |
| 6 | Final output package | Produce PRD Markdown, user story map HTML, and QC checklist Markdown table | `references/final-output-contract.md`, plus templates | Final artifacts generated and validated |

## Output Rules

- During steps 1-5, respond in chat with compact tables and 1-3 next questions.
- In step 5, use the Red Team risk levels `High`, `Medium`, and `Low`, keep the five highest-risk issues, and mark every `High` item as blocking until remediated and confirmed.
- In step 6, write final artifacts under `output/` unless the user specifies another path:
  - `output/<project_slug>_prd.md`
  - `output/<project_slug>_user_story_map.html`
  - `output/<project_slug>_qc_checklist.md`
- Keep Markdown artifacts directly editable.
- Keep the HTML story map self-contained, with embedded CSS and no required external dependencies.
- Include detailed process flow and condition architecture in the HTML story map.
- Run practical validation before delivery: file existence, basic parse/readback, unresolved `TBD` list, and checklist coverage.

## References

Load only the reference needed for the current step:

- `references/workflow.md`
- `references/requirement-clarification.md`
- `references/confirmation-summary-template.md`
- `references/prd-template.md`
- `references/user-story-map-template.html`
- `references/qc-checklist-template.md`
- `references/final-output-contract.md`
- Installed `red-team` skill, only when running the Red Team gate
