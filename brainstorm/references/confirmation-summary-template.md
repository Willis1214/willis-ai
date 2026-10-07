# Structured Confirmation Summary Template

## Purpose

Before entering QC checklist discussion, Red Team review, and final artifact generation, summarize all confirmed information and ask the user for explicit confirmation.

## Required Output

```markdown
## 结构化需求确认

### 1. 项目概览

| 项目 | 内容 | 状态 |
| --- | --- | --- |
| 项目名称 | TBD | 待确认 |
| 背景 | TBD | 待确认 |
| 核心目标 | TBD | 待确认 |
| 项目类型 | TBD | 待确认 |
| 运行环境 | TBD | 待确认 |

### 2. Input / Output Contract

| 类型 | 内容 | 格式 / 来源 | 状态 |
| --- | --- | --- | --- |
| Input | TBD | TBD | 待确认 |
| Output | TBD | TBD | 待确认 |

### 3. 用户故事地图摘要

| 用户角色 | 活动 | 用户任务 | 系统响应 | 状态 |
| --- | --- | --- | --- | --- |

### 4. 边界与非目标

| 类型 | 内容 | 状态 |
| --- | --- | --- |
| In Scope | TBD | 待确认 |
| Out of Scope | TBD | 待确认 |

### 5. 约束与风险

| 类型 | 内容 | 影响 | 状态 |
| --- | --- | --- | --- |

### 6. 待确认项

| 编号 | 问题 | 影响范围 | 优先级 |
| --- | --- | --- | --- |
| TBD-001 | TBD | TBD | High |

### 7. 外部评审模块

| 模块 | 触发条件 | 本地 Skill 路径 | Sub Agent 路径 | 状态 |
| --- | --- | --- | --- | --- |
| Red Team | 最终输出前必须运行 | Installed `red-team` skill | 由 `red-team` skill 建议，主 Agent 决定是否 spawn | 待运行 |
| Front Taste | 视觉 / UI / HTML / dashboard / deck / decision-material 质量相关时运行 | Installed `front-taste` skill | 由 `front-taste` skill 建议，主 Agent 决定是否 spawn | TBD |

## 请确认

请确认以上内容是否可以作为 QC Checklist 讨论、Red Team 审核和最终 PRD / 用户故事地图 / QC Checklist 的生成依据。确认后进入 QC Checklist 讨论；如有修改，请直接指出需要变更的字段。
```

## Rules

- The summary is a gate, not a final PRD.
- Explicitly separate confirmed facts from `TBD`.
- Do not proceed to QC checklist discussion, Red Team review, or final output until the user confirms or edits this summary.
