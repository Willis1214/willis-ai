# PM Consultant

## English

PM Consultant is a Codex skill for PRD-first requirement clarification, QC-gated delivery, and Red Team review before final specification output.

It helps complex engineering ideas move from unclear intent to a confirmed requirement package before implementation starts. The skill constrains the problem, user story map, input/output contract, boundaries, risk handling, and acceptance checks. It does not prescribe or restrict the implementation path unless the user explicitly provides hard technical constraints.

### What It Does

- Clarifies project background, business objective, users, inputs, outputs, boundaries, non-goals, runtime environment, constraints, and success criteria.
- Builds a user story map with roles, activities, tasks, system responses, process flow, condition architecture, exceptions, and edge cases.
- Summarizes all confirmed information and unresolved `TBD` items for explicit user confirmation.
- Discusses a QC checklist before final output so acceptance criteria become part of the requirement contract.
- Runs a Red Team gate before final artifacts, using risk levels `High`, `Medium`, and `Low`.
- Blocks final output until every `High` Red Team finding is remediated and the user confirms the remediation.
- Produces a final three-artifact package:
  - PRD Markdown
  - user story map HTML
  - QC checklist Markdown table

### When To Use It

Use this skill when:

- you have a new system, tool, workflow, platform, or feature idea
- requirements are still ambiguous
- users, inputs, outputs, boundaries, and non-goals need to be clarified
- you want a PRD-ready package before implementation
- you need a user story map with flow and condition architecture
- you need a QC checklist that constrains acceptance without over-constraining implementation
- you want adversarial review before final specification files are generated

### When Not To Use It

Do not use this skill for:

- simple factual answers
- narrow bug fixes with already confirmed requirements
- formal code review findings
- ordinary repository publishing workflows
- cases where the user has already provided a complete PRD and only wants implementation

### Workflow

| Step | Name | Output | Gate |
| --- | --- | --- | --- |
| 1 | Requirement clarification | Confirmed fields and open questions | User confirms enough context |
| 2 | User story map | Draft story map and flow/condition model | User confirms story map direction |
| 3 | Structured confirmation | Requirement contract summary with confirmed and `TBD` items | User explicitly confirms or edits |
| 4 | QC checklist discussion | Draft QC checklist and severity rules | User confirms checklist coverage |
| 5 | Red Team review and remediation | Risk-ranked adversarial review plus remediation decisions | No unresolved `High` findings; user confirms Red Team pass |
| 6 | Final output package | PRD Markdown, user story map HTML, QC checklist Markdown | Artifacts generated and validated |

### Installation

Install from the central Skills repository branch:

```bash
npx skills add https://github.com/Willis1214/Skills/tree/PM-Consultant-Skill --skill pm-consultant
```

Or copy `pm-consultant/` from this branch into your Codex skills directory.

### Usage Prompt

```text
Use $pm-consultant to clarify requirements, build a user story map, confirm structured requirements, discuss QC checklist coverage, run a Red Team review and remediate high-risk findings, then output PRD Markdown, user-story-map HTML, and QC checklist Markdown without prescribing the implementation path.
```

### Repository Contents

- `pm-consultant/SKILL.md`: core skill instructions and workflow gate.
- `pm-consultant/agents/openai.yaml`: Codex app display metadata.
- `pm-consultant/references/workflow.md`: workflow sequence, Red Team gate shape, and gate rules.
- `pm-consultant/references/requirement-clarification.md`: requirement contract fields and clarification prompts.
- `pm-consultant/references/confirmation-summary-template.md`: structured confirmation gate template.
- `pm-consultant/references/prd-template.md`: final PRD Markdown template, including Red Team Gate Summary.
- `pm-consultant/references/user-story-map-template.html`: self-contained HTML story map template.
- `pm-consultant/references/qc-checklist-template.md`: final QC checklist Markdown template with Red Team gate item.
- `pm-consultant/references/final-output-contract.md`: final artifact contract and validation checklist.
- `manifest.json`: release metadata for this skill branch.
- `REVISION_HISTORY.md`: version history.

### Release Notes

#### v1.2.0 - 2026-06-03

- Added a Red Team review and remediation gate before final specification output.
- Moved final artifact generation from Step 5 to Step 6.
- Added `QC-011` to require Red Team high-risk closure before final output.
- Added a PRD Red Team Gate Summary so final artifacts can carry review evidence.
- Updated the default prompt and final output contract to block unresolved `High` findings.

#### v1.1.0 - 2026-05-18

- Reworked the skill from a fixed five-stage consulting/code/UAT/retrospective flow into a PRD-first, QC-gated requirement workflow.
- Removed default code-design and retrospective stages.
- Added final output contract for PRD Markdown, user-story-map HTML, and QC checklist Markdown.
- Added a self-contained user story map HTML template with process flow and condition architecture.
- Updated guidance to avoid over-constraining the language model's implementation path.

#### v1.0.0 - 2026-05-18

- Initial public release.
- Added the `pm-consultant` installable skill with display name `PM Consultant`.
- Defined five explicit stages: consultation, PRD, code design, UAT/QC, and retrospective.
- Added stage-specific reference templates.

### Safety and Boundaries

- The skill does not request or use credentials.
- The skill does not run commands or access external services by itself.
- It marks unresolved content as `TBD`.
- It constrains requirements and acceptance criteria, not implementation style.
- It does not generate final PRD, story-map HTML, or QC checklist files until the Red Team gate passes.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

PM Consultant 是一个 Codex skill，用于 PRD-first 的需求澄清、QC-gated 的交付准备，以及最终规格文件输出前的 Red Team 审核。

它帮助复杂工程想法在开始实现前，先形成确认过的需求包。该 skill 约束问题、用户故事地图、输入输出契约、边界、风险处理和验收检查，不规定或限制具体实现路径，除非用户明确提供硬性技术约束。

### 它做什么

- 澄清项目背景、业务目标、用户、输入、输出、边界、非目标、运行环境、约束和成功标准。
- 建立用户故事地图，包括角色、活动、任务、系统响应、流程、条件架构、异常和边界场景。
- 汇总所有已确认信息和未解决的 `TBD` 项，要求用户二次确认。
- 在最终输出前先讨论 QC Checklist，让验收标准成为需求合同的一部分。
- 在最终文件输出前运行 Red Team gate，使用 `High`、`Medium`、`Low` 风险等级。
- 在所有 `High` Red Team findings 修复并由用户确认前，阻止最终输出。
- 最终输出三件套：
  - PRD Markdown
  - 用户故事地图 HTML
  - QC Checklist Markdown table

### 什么时候使用

适用于：

- 新系统、新工具、新流程、新平台或新功能想法
- 需求仍然模糊
- 需要澄清用户、输入、输出、边界和非目标
- 需要在实现前形成 PRD-ready package
- 需要带流程和条件架构的用户故事地图
- 需要用 QC Checklist 限制验收，而不是限制实现路径
- 需要在最终规格文件生成前做对抗式风险审查

### 什么时候不使用

不适用于：

- 简单事实问答
- 需求已确认的窄范围 bug 修复
- 正式代码审查 findings
- 普通 GitHub 仓库发布流程
- 用户已经提供完整 PRD 且只需要实现的场景

### 工作流

| Step | 名称 | 输出 | Gate |
| --- | --- | --- | --- |
| 1 | 需求澄清 | 已确认字段和开放问题 | 用户确认上下文足够进入故事地图 |
| 2 | 用户故事地图 | Draft story map 和流程/条件模型 | 用户确认故事地图方向 |
| 3 | 结构化确认 | 含已确认项和 `TBD` 的需求合同摘要 | 用户明确确认或修改 |
| 4 | QC Checklist 讨论 | Draft QC checklist 和严重等级规则 | 用户确认 checklist 覆盖范围 |
| 5 | Red Team review and remediation | 风险排序后的对抗式审查与修复决策 | 无未解决 `High` findings，且用户确认 Red Team pass |
| 6 | 最终三件套输出 | PRD Markdown、用户故事地图 HTML、QC Checklist Markdown | 文件生成并验证 |

### 安装

从中央 Skills 仓库分支安装：

```bash
npx skills add https://github.com/Willis1214/Skills/tree/PM-Consultant-Skill --skill pm-consultant
```

也可以把本分支的 `pm-consultant/` 复制到本地 Codex skills 目录。

### 使用 Prompt

```text
Use $pm-consultant to clarify requirements, build a user story map, confirm structured requirements, discuss QC checklist coverage, run a Red Team review and remediate high-risk findings, then output PRD Markdown, user-story-map HTML, and QC checklist Markdown without prescribing the implementation path.
```

### 仓库内容

- `pm-consultant/SKILL.md`: 核心 skill 指令与 workflow gate。
- `pm-consultant/agents/openai.yaml`: Codex app 展示 metadata。
- `pm-consultant/references/workflow.md`: 工作流顺序、Red Team gate 形态与 gate 规则。
- `pm-consultant/references/requirement-clarification.md`: 需求合同字段与澄清问题。
- `pm-consultant/references/confirmation-summary-template.md`: 结构化确认 gate 模板。
- `pm-consultant/references/prd-template.md`: 最终 PRD Markdown 模板，包含 Red Team Gate Summary。
- `pm-consultant/references/user-story-map-template.html`: 自包含 HTML 用户故事地图模板。
- `pm-consultant/references/qc-checklist-template.md`: 包含 Red Team gate 检查项的 QC Checklist Markdown 模板。
- `pm-consultant/references/final-output-contract.md`: 最终产物合同与验证清单。
- `manifest.json`: 当前 skill 分支的 release metadata。
- `REVISION_HISTORY.md`: 版本历史。

### Release Notes

#### v1.2.0 - 2026-06-03

- 在最终规格文件输出前增加 Red Team review and remediation gate。
- 将最终文件生成从 Step 5 顺延到 Step 6。
- 增加 `QC-011`，要求 Red Team high-risk closure 后才能最终输出。
- 在 PRD 模板中增加 Red Team Gate Summary，确保最终产物保留审核证据。
- 更新默认 prompt 和 final output contract，阻止存在未解决 `High` findings 时输出最终文件。

#### v1.1.0 - 2026-05-18

- 将 skill 从固定五阶段咨询/代码/UAT/复盘流程改为 PRD-first、QC-gated 的需求工作流。
- 移除默认代码设计和复盘阶段。
- 增加 PRD Markdown、用户故事地图 HTML、QC Checklist Markdown 的最终输出合同。
- 增加自包含用户故事地图 HTML 模板，覆盖流程和条件架构。
- 更新规则，避免过度限制语言模型的具体实现路径。

#### v1.0.0 - 2026-05-18

- 首次公开发布。
- 增加 installable skill `pm-consultant`，展示名为 `PM Consultant`。
- 定义五个显式阶段：consultation、PRD、code design、UAT/QC、retrospective。
- 增加阶段化 reference templates。

### 安全与边界

- 该 skill 不请求或使用凭证。
- 该 skill 本身不运行命令或访问外部服务。
- 未解决内容标为 `TBD`。
- 它约束需求和验收标准，不约束实现风格。
- Red Team gate 未通过前，不生成最终 PRD、用户故事地图 HTML 或 QC Checklist 文件。

### License

当前版本尚未选择开源 License。在仓库所有者添加 License 前，请按 all rights reserved 处理。
