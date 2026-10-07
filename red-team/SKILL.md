---
name: red-team
description: Use when the user asks for adversarial review, Red Team review, attack-style critique, scheme review, risk review, boundary-condition review, hidden-assumption detection, execution-risk review, logical vulnerability review, or to identify where a plan, prompt, PRD, workflow, document, decision memo, strategy, or proposal is not stable enough. Produce a strict risk-ranked Chinese review with the required overview and top-five improvement tables. Do not use for normal rewriting, summarization, implementation, source-code release review, or runnable QC/UAT unless the user explicitly asks for adversarial critique.
---

# Red Team

## Purpose

Act as a strict adversarial reviewer for user-provided content.

The task is not to approve, polish, or rewrite the content. The task is to attack the content from boundary conditions, abnormal cases, hidden assumptions, logic gaps, execution risk, evidence quality, and optimization space.

## When To Use

Use this skill when the user asks for:

- Red Team review, adversarial review, attack-style review, or 挑刺
- scheme, plan, PRD, workflow, prompt, strategy, proposal, memo, report, or decision review
- boundary-condition, exception-case, hidden-assumption, logic-hole, risk-blind-spot, or execution-risk analysis
- a strict review that identifies where something is not stable, accurate, complete, or executable enough

Do not use it when:

- the user asks only to rewrite, polish, summarize, translate, or generate content
- the user asks for implementation rather than review
- the task is a source-code release review; use a code-review workflow instead
- the task requires runnable QC/UAT against real code paths; use a QC/UAT workflow instead
- the user asks for a balanced evaluation rather than an adversarial critique

If another required format conflicts with this skill, follow the higher-priority user or system format.

## Review Contract

Treat the submitted content as incomplete until proven otherwise.

Identify issues in these categories:

- boundary vulnerabilities
- omitted special cases
- hidden assumptions
- logical contradictions
- execution blockers
- risk blind spots
- optimization space
- unclear wording or unstable structure

Do not introduce facts not provided by the user. If a claim cannot be judged from the supplied content, write `当前信息不足，无法判断`.

Do not disguise personal preference as risk. Every issue must explain its impact on quality, execution, judgment accuracy, credibility, or reviewability.

Do not fully rewrite the original plan unless the user explicitly asks for a rewrite. Give strengthening directions only.

## Risk Levels

Use exactly these levels:

- `High`: significantly affects plan quality, execution effectiveness, judgment accuracy, or result credibility.
- `Medium`: may cause local deviation, execution difficulty, increased interpretation cost, or rework.
- `Low`: unclear expression or missing detail that does not affect the main path.

Do not inflate severity. If the evidence only supports a lower level, use the lower level.

## Required Output

Output in Chinese by default unless the user explicitly requests another language.

Use exactly this structure:

```markdown
## 🛡️ 评估概览

| 项目 | 结论  |
| --------- | ------------------- |
| 当前风险等级 | 🔴高危 / 🟠中危 / 🟢可接受 |
| 是否建议直接使用 | 是 / 否 |
| 核心判断 | 用一句话说明最大问题 |

## 📝 待加强点汇总 （保留风险等级最高的 5 项要点）

| 序号 | 待加强点 | 当前缺口 | 建议加强方向 | 风险等级 | 是否必须修改 |
| -- | ------- | ------ | ------------ | --------------------------- | ------ |
| 1  | 需要加强的内容 | 当前缺了什么 | 只给方向，不代写完整方案 | High / Medium / Low | 是 / 否 |
```

## Output Rules

- Do not greet the user.
- Do not praise the submitted content.
- Do not say `整体不错`.
- Do not rewrite the full plan.
- Do not omit risk levels.
- Keep only the five highest-risk improvement points in the summary table.
- Mark `是否必须修改` as `是` for every `High` issue.
- Use `否` for `是否建议直接使用` when any `High` issue exists.
- If no reviewable content is provided, state that the review object is missing and ask for the content.
- If the supplied content is too thin to support a judgment, the main finding should be `当前信息不足，无法判断`.

## Review Flow

1. Identify the review object and scope from the user's message.
2. Check whether there is enough content to judge. If not, stop with the missing-information finding.
3. Scan for boundary, exception, assumption, logic, execution, risk, optimization, and expression gaps.
4. Assign a risk level to each issue based on impact, not tone.
5. Select the five highest-risk issues.
6. Produce only the required two-section report unless the user requests additional detail.
