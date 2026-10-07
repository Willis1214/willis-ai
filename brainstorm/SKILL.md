---
name: brainstorm
description: "Clarify complex engineering/product ideas before implementation through a repeatable role-based round loop: clarify requirements, map story/flow, confirm decisions, define boundaries, attack boundary risks, check QC, test safe shortest-path MVP/demo cases when useful, expose map-changing unknowns, then produce PRD/story-map/QC outputs after the Red Team final gate and optional Front Taste gate. Do not constrain implementation choices unless the user provides technical constraints."
---

# Brainstorm

## Purpose

Guide a complex engineering idea into a clear, confirmed requirement package before work starts.

This skill controls the requirement and quality contract, not the implementation route. The goal is to run repeated, full-strength discussion rounds that clarify the user's background, objective, inputs, outputs, user story map, boundaries, interaction / physical-world constraints, QC criteria, risks, and critical unknowns, then produce a PRD-ready delivery package after the required review gates.

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
- Do not run the old requirement / story-map / confirmation / QC / risk work as separate serial chat steps. Each discussion round must cover all seven task classes at the strongest useful depth for the current context.
- The unified workflow and fixed role format simplify orchestration and output only; they do not reduce the thinking depth, evidence discipline, boundary checks, QC rigor, or risk review expected from the old task classes.
- Do not output final PRD, final story-map HTML, or final checklist before the round loop has produced a confirmed requirement package, story / flow direction, QC coverage, and Red Team gate result.
- Do not prescribe implementation details unless the user asks for implementation guidance or supplies hard technical constraints.
- The `🛠️ 实践者` role may only run or propose a shortest-path MVP/demo probe when it is safe, low-cost, reversible, and useful for clarifying a live uncertainty in the discussion. It must not create final deliverables, perform external writes, publish/send/upload, make irreversible changes, or replace the downstream implementation workflow.
- If the current round has no useful safe MVP/demo probe, `🛠️ 实践者` must explicitly write `没有实践案例需要跑。`.
- When a solution involves human-machine, human-human, or machine-machine interaction, explicitly clarify physical-world boundary conditions such as logical mutual exclusion, chain reactions, hidden sharing, and overfitting risk. Mark unknowns as `TBD`; do not assume them away.
- Before final artifacts, run a Red Team review of the confirmed requirement package and draft QC/story-map direction.
- The Red Team review must use the installed local `red-team` skill first. If that skill recommends Sub Agent execution, the main Agent may spawn the matching `red-team` Sub Agent and then integrate its findings back into this workflow.
- Red Team gate passes only when no `High` findings remain, or every `High` finding has been addressed in the confirmed plan and the user confirms the remediation. Unresolved `High` findings block final output.
- Use Red Team findings to strengthen requirements, boundaries, exception handling, evidence, and QC gates. Do not use the Red Team step to invent business facts or prescribe an implementation path.
- When the final package includes visual, UI, HTML, dashboard, deck, or decision-material quality concerns, run the installed local `front-taste` skill as the Front Taste module before final delivery. If that skill recommends Sub Agent execution, the main Agent follows the current `$front-taste` sidecar route and then integrates its findings back into this workflow.
- Red Team and Front Taste are local-skill-first modules. Brainstorm does not bypass those skills by directly inventing a Sub Agent task card.
- Keep role responsibilities separated: `🧱 边界官` defines the current boundary, `⚔️ 攻击者` attacks the stated boundary and current plan, `🪞 反思者` exposes map-changing unknowns, and Red Team is the final gate before artifacts.
- The round-level `⚔️ 攻击者` produces risk candidates during discussion; it does not replace the final Red Team gate, assign the final pass/fail verdict, or block final artifacts by itself.
- The final Red Team gate reviews the confirmed requirement package, story-map direction, and QC coverage after the discussion loop. It blocks only through unresolved `High` findings.
- A `TBD` item becomes blocking when it can materially change the goal, boundary, acceptance standard, evidence requirement, or delivery credibility. Non-blocking `TBD` items may remain visible as residual risks, owner-accepted gaps, or QC checklist items.
- If the user asks for code after the PRD package is confirmed, let the implementation agent choose a path that satisfies the PRD and QC checklist.

## Workflow

Read `references/workflow.md` before running the workflow.

| Phase | Name | Goal | Primary Reference | Gate |
| --- | --- | --- | --- | --- |
| 1 | Discussion round loop | Every chat round clarifies requirements, maps story / flow, confirms decisions, strengthens QC, attacks risks, checks safe shortest-path MVP/demo opportunities, and exposes critical unknowns in the fixed role-based format | `references/workflow.md`, `references/discussion-output-format.md`, plus the relevant requirement / story / confirmation / QC references | Continue until the confirmed package is ready for final output or the user redirects |
| 2 | Final output package | Produce PRD Markdown, user story map HTML, and QC checklist Markdown table; run the installed local `red-team` gate first and the installed local `front-taste` skill when visual / UI / HTML quality matters | `references/final-output-contract.md`, plus templates and optional installed `front-taste` skill contract | Final artifacts generated and validated |

## Output Rules

- During every discussion round, respond in chat with the fixed role-based discussion format in `references/discussion-output-format.md`; do not use Markdown table headers for the process format.
- Every discussion round must cover all seven task classes: requirement clarification, story / flow mapping, structured confirmation, QC / acceptance thinking, risk attack, practice probing, and reflection clarification. If a task class has no new material in that round, state `无` rather than omitting it; for practice probing with no useful safe case, write `没有实践案例需要跑。`.
- Before final artifacts, call the local `red-team` skill before any Red Team Sub Agent path. Follow that skill's recommendation if it asks the main Agent to spawn a Sub Agent.
- In the final Red Team gate, use the risk levels `High`, `Medium`, and `Low`, keep the five highest-risk issues, and mark every `High` item as blocking until remediated and confirmed.
- In the final output package phase, call the local `front-taste` skill before delivering visual, UI, HTML, dashboard, deck, or decision-material artifacts. Follow that skill's recommendation if it asks the main Agent to spawn a Sub Agent.
- In the final output package phase, write final artifacts under `output/` unless the user specifies another path:
  - `output/<project_slug>_prd.md`
  - `output/<project_slug>_user_story_map.html`
  - `output/<project_slug>_qc_checklist.md`
- Keep Markdown artifacts directly editable.
- Keep the HTML story map self-contained, with embedded CSS and no required external dependencies.
- Include detailed process flow and condition architecture in the HTML story map.
- Run practical validation before delivery: file existence, basic parse/readback, unresolved `TBD` list, and checklist coverage.

## References

Load only the reference needed for the current round or final output:

- `references/workflow.md`
- `references/discussion-output-format.md`
- `references/requirement-clarification.md`
- `references/confirmation-summary-template.md`
- `references/prd-template.md`
- `references/user-story-map-template.html`
- `references/qc-checklist-template.md`
- `references/final-output-contract.md`
- Installed `red-team` skill, only when running the Red Team gate
- Installed `front-taste` skill, only when visual, UI, HTML, dashboard, deck, or decision-material quality matters
