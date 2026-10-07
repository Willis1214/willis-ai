# Brainstorm Workflow

## Goal

Create a confirmed requirement package before implementation starts.

The workflow defines what the user needs, not how the model must implement it. Implementation choices remain flexible unless the user provides hard constraints.

## Discussion Round Loop

Brainstorm no longer advances through serial chat steps. Every chat round runs the same integrated loop and outputs the fixed role-based discussion format.

Each round must cover these seven task classes at the strongest useful depth for the current context:

1. Requirement clarification: background, objective, users, input, output, constraints, interaction / physical-world boundaries, non-goals, and unresolved `TBD`.
2. Story / flow mapping: roles, activities, user tasks, system responses, main flow, exception flow, condition branches, and process architecture.
3. Structured confirmation: confirmed decisions, changed decisions, unresolved `TBD`, terminology, filenames, fields, and constraints to preserve.
4. QC / acceptance thinking: quality gates, blocker rules, verification method, evidence, severity, status, and minimal validation path.
5. Risk attack: attacks against the stated boundary and current plan, including boundary leaks, omitted special cases, hidden assumptions, logical contradictions, execution blockers, evidence gaps, risk blind spots, and unclear wording.
6. Practice probing: safe shortest-path MVP/demo opportunities that can clarify a live uncertainty in the discussion, plus the probe result or the exact statement `没有实践案例需要跑。`.
7. Reflection clarification: critical `未知已知` and `未知未知` that could force the task, goal definition, execution route, resource allocation, boundary, or acceptance standard to be redone if wrong.

## Role and Gate Responsibility Contract

Keep the discussion roles and final gate separate:

- `🧱 边界官` defines the current boundary: in-scope, out-of-scope, forbidden assumptions, untouched terms, permission limits, and logical / interaction / physical-world constraints. It does not attack, score, or decide the final gate.
- `⚔️ 攻击者` attacks the boundary and current plan: where the stated boundary leaks, which assumptions may fail, which exception cases are missing, and which evidence gaps could make the plan unreliable. It produces risk candidates during the round; it does not replace Red Team and does not assign the final pass/fail verdict.
- `🪞 反思者` checks whether the map is wrong: map bias, missing decision variables, key unknowns, route forks, rollback points, and questions that could change the goal, route, boundary, resource allocation, or acceptance standard. It does not decide, recommend, score, block, or choose a route.
- Red Team is the final artifact gate: it reviews the confirmed requirement package, story-map direction, and QC checklist coverage after the loop has produced a coherent package. It blocks final artifacts only through unresolved `High` findings.

Handle `TBD` explicitly:

- Treat a `TBD` as blocking when it can materially change the goal, boundary, acceptance standard, evidence requirement, delivery credibility, or whether the user should proceed.
- Non-blocking `TBD` items may pass into final artifacts only when they remain visible as residual risks, owner-accepted gaps, or QC checklist items.

The loop repeats until the confirmed package is strong enough for final artifacts, or until the user redirects, pauses, or cancels the discussion.

## Gate Rules

- Ask only the next 1-3 question groups needed to strengthen the current package; do not ask everything at once.
- If the user changes a confirmed item, update downstream summaries and mark the change.
- If required information is missing, keep it as `TBD`; do not fill it with guesses.
- If the user tries to jump to implementation before the requirement package is confirmed, summarize the missing contract items first.
- If the user explicitly waives part of the discussion loop, note the waived task class and resulting risk.
- Before final artifacts, run a Red Team gate on the confirmed requirement package, story-map direction, and QC checklist coverage. This is a final gate, not another round-level `⚔️ 攻击者` block.
- Red Team is a local-skill-first module: load the installed `red-team` skill and follow its review contract. If the `red-team` skill recommends spawning the `red-team` Sub Agent, the main Agent owns the spawn call, final integration, and user-facing gate decision.
- Treat every `High` Red Team finding as a blocker until it is addressed in the confirmed package and the user confirms the remediation.
- If a Red Team finding cannot be judged from confirmed information, keep it as `TBD` and reflect the risk in the PRD or QC checklist instead of guessing.
- `Medium` and `Low` findings may pass only when they are either incorporated, explicitly accepted by the user, or left visible as `TBD` with owner impact.
- Front Taste is also a local-skill-first module. When the final package includes visual, UI, HTML, dashboard, deck, or decision-material quality concerns, load the installed `front-taste` skill during final output validation. If `front-taste` recommends a sidecar, the main Agent follows the current `$front-taste` sidecar route and owns final integration and delivery decision.

## Standard Chat Shape

For every discussion round, keep the response in the fixed role-based discussion format from `references/discussion-output-format.md`.

The process format must preserve these role labels in order. Use the same label style for every role: emoji + role name, without Markdown heading markers such as `##`.

1. `🧭 主持人`
2. `📝 记录者`
3. `💡 补充者（用户视角）`
4. `💡 补充者（交付视角）`
5. `💡 补充者（系统视角）`
6. `🧱 边界官`
7. `⚔️ 攻击者`
8. `🛠️ 实践者`
9. `🪞 反思者`
10. `📌 汇总者`

Do not replace this process format with Markdown tables. Always preserve confirmed facts, changed decisions, open `TBD` items, risks, boundaries, the minimal verification path, and the next 1-3 question groups.

Map the task classes into the role format:

1. Requirement clarification appears mainly under `🧭 主持人`, `📝 记录者`, and `🧱 边界官`.
2. Story / flow mapping appears mainly under `💡 补充者（用户视角）` and `💡 补充者（系统视角）`.
3. Structured confirmation appears mainly under `📝 记录者`.
4. QC / acceptance thinking appears mainly under `💡 补充者（交付视角）`.
5. Risk attack appears mainly under `⚔️ 攻击者`, and must attack the current stated boundary or plan instead of redefining the boundary.
6. Practice probing appears only under `🛠️ 实践者`; it identifies whether a safe shortest-path MVP/demo probe should be run, records the shortest path and conclusion when useful, or writes `没有实践案例需要跑。` when no useful safe case exists.
7. Reflection clarification appears only under `🪞 反思者`; it exposes critical `未知已知` and `未知未知` for the user to understand and does not decide, recommend, score, block, or choose a route.

Use `🧱 边界官` to state the boundary before it is attacked. The boundary role should make clear what is included, excluded, forbidden to assume, or constrained by permissions, people, tools, environment, logic, interaction, or physical-world limits.

The `🛠️ 实践者` role is evidence support for discussion, not a downstream implementation shortcut. It may run or propose only safe, low-cost, reversible, local or demo-scope probes that clarify the current requirement, feasibility, or acceptance uncertainty. It must not create final artifacts, modify production/configuration state, perform external writes, publish/send/upload, or turn the discussion round into full execution. If a useful probe would exceed that boundary, report the boundary and keep the item as a handoff or `TBD`.

Use `📌 汇总者` only as a compressed user-communication handoff. It should list which outputs exist in the current round and only the confirmation items that could affect the goal, route, boundary, or acceptance: current `TBD`, key confirmation items, and the next question to ask the user, without repeating the detailed content already written by the other roles.

## Final Red Team Gate Shape

Before final artifacts, review the confirmed package adversarially. Use the installed local `red-team` skill first. The Red Team skill may recommend a Sub Agent route, but Brainstorm must not bypass the local skill contract. This final gate is separate from the round-level `⚔️ 攻击者`: the attacker finds risk candidates during discussion, while Red Team decides whether the confirmed package is safe enough to become artifacts. Use the installed `red-team` skill's review categories and risk levels:

- boundary vulnerabilities
- omitted special cases
- hidden assumptions
- logical contradictions
- execution blockers
- risk blind spots
- optimization space
- unclear wording or unstable structure

Output:

1. A risk overview with current risk level, whether direct final output is allowed, and the core blocker.
2. A top-five issue table using `High`, `Medium`, and `Low`.
3. A remediation table for every `High` issue, showing what must change in the confirmed package.
4. A next confirmation question asking whether the strengthened package can pass the Red Team gate.

Do not proceed to final artifacts until the Red Team gate passes.

## Front Taste Module Shape

For the final output package, use Front Taste only when visual quality, UI clarity, HTML report readability, dashboard composition, deck quality, or decision-material taste matters.

1. Load the installed local `front-taste` skill.
2. Ask it to review the relevant artifact direction or final draft.
3. If `front-taste` recommends a sidecar, the main Agent may spawn it through the current `$front-taste` route and then integrate the findings.
4. Treat must-fix taste findings as blockers for visual delivery only when they affect task clarity, trust, usability, readability, or artifact acceptance.

Do not add a new numbered discussion step for Front Taste. It is a final output validation module.

## Final Artifact Rule

Final artifacts are produced only after the discussion round loop has yielded a confirmed package and the required final gates have passed:

- PRD: Markdown
- User story map: self-contained HTML
- QC checklist: Markdown table
