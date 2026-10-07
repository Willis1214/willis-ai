# Brainstorm Discussion Output Format

Use this format for every discussion-round chat response. Keep the role labels, role order, and field labels stable. Do not use Markdown tables or table headers in this process format.

## Fixed Round Template

```markdown
🧭 主持人
当前环节：
本轮问题：
推进规则：

📝 记录者
已确认：
   1. ……
   2. ……
已变更：
   1. ……
   2. ……
TBD：
   1. ……
   2. ……

💡 补充者（用户视角）
补充内容：
   1. ……
   2. ……

💡 补充者（交付视角）
补充内容：
   1. ……
   2. ……

💡 补充者（系统视角）
补充内容：
   1. ……
   2. ……

🧱 边界官
边界声明：
   1. ……
   2. ……
明确不做：
   1. ……
   2. ……

⚔️ 攻击者
风险：
   1. ……
   2. ……

🛠️ 实践者
MVP/demo 判断：
   1. ……
最短路径：
   1. ……
实践结论：
   1. …… / 没有实践案例需要跑。

🪞 反思者
未知已知：
   1. 用户可能一看就能判断、但当前没有写出的标准是什么？
未知未知：
   1. 当前讨论没有覆盖、但可能改变目标、路线、边界或验收的问题是什么？

📌 汇总者
本轮产出：
   1. ……
   2. ……
待用户确认：
   1. TBD 汇总：……
   2. 关键确认项：……
   3. 下一问：……
```

## Use Rules

- Keep every section even when content is sparse.
- Use `无` when a section has no material content for the current round.
- Use `TBD` exactly for unresolved requirement, boundary, evidence, or acceptance content.
- Every round must cover all seven task classes at the strongest useful depth for the current context: requirement clarification, story / flow mapping, structured confirmation, QC / acceptance thinking, risk attack, practice probing, and reflection clarification.
- Ask only the next 1-3 question groups needed to strengthen the current package, and place them under `📌 汇总者 / 待用户确认`.
- Record changed decisions under `📝 记录者 / 已变更` instead of silently replacing earlier conclusions.
- Split every user-provided perspective into a separate `💡 补充者（...视角）` role. Do not merge multiple perspectives under one `补充者` block.
- Use the same role-label style for every role: emoji + role name, without Markdown heading markers such as `##`.
- Put QC gates, acceptance details, evidence needs, and minimal validation detail under `💡 补充者（交付视角）`, not under `📌 汇总者`.
- Put current boundary declarations under `🧱 边界官 / 边界声明`: in-scope, out-of-scope, forbidden assumptions, untouched terms, permission limits, and logical / interaction / physical-world constraints. Use `🧱 边界官 / 明确不做` only for non-goals and prohibited actions.
- Put adversarial concerns under `⚔️ 攻击者`; attack the stated boundary and current plan, but do not redefine the boundary, score the package, or replace the final Red Team gate. Before final artifacts, still follow the Red Team gate and local `red-team` skill contract.
- Put safe shortest-path MVP/demo checks under `🛠️ 实践者`. This role may run or propose only low-risk, reversible, demo-scope probes that clarify the current discussion; it must not create final deliverables, perform external writes, or replace downstream implementation. If no useful safe probe exists, write `没有实践案例需要跑。` under `实践结论`.
- Put only critical map-check notes under `🪞 反思者`: `未知已知` that the user can likely judge on sight but has not written down, and `未知未知` that the discussion has not covered but could change the goal, route, boundary, resource allocation, or acceptance. The reflector is a standing role and does not decide, recommend, score, block, or choose a route.
- Treat a `TBD` as blocking when it can materially change the goal, boundary, acceptance standard, evidence requirement, delivery credibility, or whether the user should proceed. Non-blocking `TBD` items may remain visible as residual risks, accepted gaps, or QC checklist items.
- Keep `📌 汇总者` compressed as the user-communication handoff. It must list the current round's outputs and only the confirmation items that could affect the goal, route, boundary, or acceptance: current `TBD`, key confirmation items, and the next question to ask the user. It must not repeat detailed content, evidence, reasoning, or risk explanations already covered by earlier roles.

## Final Packaging Prompt

When the repeated discussion rounds have produced a confirmed package that is ready for final output, actively ask whether to organize the discussion into final artifacts:

```markdown
## 📦 产出整理建议
当前讨论已经足够收拾成正式产物。建议生成：

1. PRD Markdown
2. User Story Map HTML
3. QC Checklist Markdown
4. 未决事项 TBD 清单

是否现在整理成文件？
```
