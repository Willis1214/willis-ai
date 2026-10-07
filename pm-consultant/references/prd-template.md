# PRD Template

Use this Markdown template for `output/<project_slug>_prd.md`.

```markdown
# PRD：{项目名称}

## 1. 文档概览

| 项目 | 内容 |
| --- | --- |
| 项目名称 | {project_name} |
| 文档版本 | {doc_version} |
| 目标版本 | {target_version_or_TBD} |
| 文档状态 | Draft / Review / Final |
| 目标用户 | {target_users} |
| 运行环境 | {runtime_environment} |

## 2. 背景与问题

{project_background}

## 3. 核心目标

| 目标 | 说明 | 成功标准 |
| --- | --- | --- |

## 4. Input / Output Contract

| 类型 | 内容 | 格式 / 来源 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| Input |  |  |  |  |
| Output |  |  |  |  |

## 5. 用户与场景

| 用户角色 | 使用场景 | 用户目标 | 关键痛点 |
| --- | --- | --- | --- |

## 6. 用户故事地图摘要

| 用户活动 | 用户任务 | 系统响应 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |

## 7. 功能需求

| 功能模块 | 功能说明 | 输入 | 输出 | 业务规则 | 异常处理 |
| --- | --- | --- | --- | --- | --- |

## 8. 边界与非目标

| 类型 | 内容 | 理由 |
| --- | --- | --- |
| In Scope |  |  |
| Out of Scope |  |  |

## 9. 约束条件

| 约束类型 | 内容 | 影响 |
| --- | --- | --- |

## 10. 验收标准摘要

| 验收项 | 标准 | 验证方式 |
| --- | --- | --- |

## 11. Red Team Gate Summary

| 项目 | 内容 |
| --- | --- |
| Red Team 状态 | Passed / Blocked / TBD |
| High 风险处理结果 | None / Remediated / Blocked |
| Medium / Low 残余风险 | TBD |
| 用户确认 | Confirmed / TBD |

## 12. 待确认问题

| 编号 | 问题 | 影响范围 | 优先级 |
| --- | --- | --- | --- |
```

## Rules

- Use only confirmed content plus explicit `TBD`.
- Do not include implementation path unless it is a confirmed requirement.
- Do not mark Red Team 状态 as `Passed` unless the step 5 Red Team gate passed.
- Keep identifiers, filenames, CLI flags, API names, and technical labels exactly as provided.
