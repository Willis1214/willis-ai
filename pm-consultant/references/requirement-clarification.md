# Requirement Clarification

## Objective

Clarify the requirement contract before any PRD or implementation work.

## Required Fields

| Field | Meaning | Status Rule |
| --- | --- | --- |
| Project background | Why this project exists and what current pain it addresses | Confirmed / TBD |
| Business objective | What outcome the user wants | Confirmed / TBD |
| Project type | New system, existing-system iteration, tool, workflow, platform, or feature | Confirmed / TBD |
| Target users | Who uses the output or system | Confirmed / TBD |
| User jobs | What users need to accomplish | Confirmed / TBD |
| Input | Files, data, user actions, APIs, prompts, or manual context entering the system | Confirmed / TBD |
| Output | Final artifacts, UI states, files, reports, messages, or system actions | Confirmed / TBD |
| Boundary | What the system must include, including logical, interaction, and physical-world boundaries when applicable | Confirmed / TBD |
| Non-goals | What the system must not do | Confirmed / TBD |
| Runtime environment | OS, local/remote context, permissions, network, enterprise restrictions | Confirmed / TBD |
| Constraints | Required formats, tool limits, compliance, security, deadlines, compatibility | Confirmed / TBD |
| Success criteria | Observable outcome that proves the work is useful | Confirmed / TBD |

## Clarification Questions

Ask only the questions needed to advance the current decision. Prefer 1-3 questions per turn.

Recommended first questions:

1. Is this a new system/tool/workflow, or an iteration of an existing one?
2. What are the required inputs and final outputs?
3. Who is the primary user, and what job do they need to complete?

If the solution involves human-machine, human-human, or machine-machine interaction, also confirm physical-world boundary conditions such as logical mutual exclusion, chain reactions, hidden sharing, and overfitting risk. Keep unknown boundary items as `TBD`.

## Output Pattern

```markdown
## 当前确认

| 项目 | 当前内容 | 状态 |
| --- | --- | --- |
| 背景 | TBD | 待确认 |
| 目标 | TBD | 待确认 |
| Input | TBD | 待确认 |
| Output | TBD | 待确认 |
| 用户 | TBD | 待确认 |
| 边界 | TBD | 待确认 |

## 关键缺口

| 缺口 | 为什么重要 | 建议确认方式 |
| --- | --- | --- |

## 下一步确认

1. ...
```

## Rules

- Do not ask everything at once.
- Do not recommend technology before input/output and user jobs are clear.
- Do not convert assumptions into confirmed requirements.
- Do not treat edge cases as only code-path exceptions; include interaction and physical-world boundary conditions when the workflow crosses people, devices, organizations, or automated agents.
