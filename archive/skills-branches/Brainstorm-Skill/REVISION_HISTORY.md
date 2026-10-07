# Revision History

## English

### v2.2.0 - 2026-07-09

| Field | Value |
| --- | --- |
| Version | v2.2.0 |
| Date | 2026-07-09 |
| Change Type | Role and gate contract clarification |
| Repository | Willis1214/Skills |
| Branch | Brainstorm-Skill |

#### Summary

Clarified Brainstorm's internal role boundaries and final review gate. `🧱 边界官` defines the current boundary, `⚔️ 攻击者` attacks the stated boundary and current plan, `🪞 反思者` exposes map-changing unknowns, and Red Team remains the final artifact gate.

#### Source Skill Changes

- Updated `SKILL.md` description and hard boundaries to separate role-level risk discovery from final Red Team gating.
- Updated `references/workflow.md` with a role and gate responsibility contract.
- Updated `references/discussion-output-format.md` so the Boundary Officer explicitly records `边界声明` before `明确不做`.
- Updated `references/final-output-contract.md` to clarify when `TBD` becomes blocking.
- Updated `agents/openai.yaml` trigger language for boundary definition, boundary-risk attack, map-changing unknowns, and Red Team final gating.

#### Compatibility

- Installable skill name remains `brainstorm`.
- Branch remains `Brainstorm-Skill`.
- Existing final artifact paths remain unchanged.
- Discussion rounds keep the same role order, with a clearer Boundary Officer field.

#### Validation

- Local `SKILL.md` frontmatter parsed.
- `agents/openai.yaml` parsed.
- Required role/gate keywords checked.
- `manifest.json` parsed.
- Staged repository package validated with `validate_skill_repo.py --upgrade`.
- Remote branch and catalog verification are recorded in the publish report for this release.

#### Known Gaps

- No open-source license has been selected.
- Legacy `PM-Consultant-Skill` branch cleanup remains out of scope.

### v2.1.0 - 2026-07-01

Updated Brainstorm from a serial step workflow into a repeatable discussion round loop. Each round covers requirement clarification, story/flow mapping, structured confirmation, QC thinking, and risk attack in a fixed role-based format.

### v2.0.0 - 2026-06-11

Renamed the real skill identity from PM Consultant / `pm-consultant` to Brainstorm / `brainstorm`, while preserving the existing PRD-first implementation path. Added local-skill-first Red Team and Front Taste routing.

### v1.2.0 - 2026-06-03

Added a Red Team review and remediation gate before final PRD, user story map, and QC checklist output.

### v1.1.0 - 2026-05-18

Reworked PM Consultant from a fixed consulting/code/UAT/retrospective flow into a PRD-first, QC-gated requirement workflow.

### v1.0.0 - 2026-05-18

Initial public release as PM Consultant.

## 中文

### v2.2.0 - 2026-07-09

| 字段 | 内容 |
| --- | --- |
| 版本 | v2.2.0 |
| 日期 | 2026-07-09 |
| 变更类型 | 角色与门禁合同澄清 |
| 仓库 | Willis1214/Skills |
| 分支 | Brainstorm-Skill |

#### 摘要

澄清 Brainstorm 内部角色边界和最终评审门禁：`🧱 边界官` 负责定义当前边界，`⚔️ 攻击者` 负责攻击已声明边界和当前方案，`🪞 反思者` 负责暴露会重画地图的关键未知，Red Team 保持为最终产物门禁。

#### 源 Skill 变更

- 更新 `SKILL.md` description 和 hard boundaries，拆开轮内风险发现与最终 Red Team 门禁。
- 更新 `references/workflow.md`，新增角色与门禁职责合同。
- 更新 `references/discussion-output-format.md`，让边界官先记录 `边界声明`，再记录 `明确不做`。
- 更新 `references/final-output-contract.md`，澄清 `TBD` 何时成为阻塞项。
- 更新 `agents/openai.yaml` 触发文案，覆盖边界定义、边界风险攻击、地图级未知和 Red Team final gate。

#### 兼容性

- 可安装 Skill 名称仍为 `brainstorm`。
- 分支仍为 `Brainstorm-Skill`。
- 既有最终产物路径不变。
- 讨论轮次保持原角色顺序，只增强边界官字段。

#### 验证

- 本地 `SKILL.md` frontmatter 已解析。
- `agents/openai.yaml` 已解析。
- 关键角色/门禁关键词已检查。
- `manifest.json` 已解析。
- staged 仓库包通过 `validate_skill_repo.py --upgrade`。
- 远端分支和 catalog 读回记录在本次 publish report。

#### 已知缺口

- 当前未选择开源许可证。
- 旧 `PM-Consultant-Skill` 分支清理不在本次范围。

### v2.1.0 - 2026-07-01

将 Brainstorm 从串行步骤工作流更新为可重复讨论轮次。每轮用固定角色格式同时覆盖需求澄清、故事/流程映射、结构确认、QC 思考和风险攻击。

### v2.0.0 - 2026-06-11

将真实 Skill 身份从 PM Consultant / `pm-consultant` 重命名为 Brainstorm / `brainstorm`，保留原 PRD-first 实现路径，并加入 local-skill-first 的 Red Team 和 Front Taste 路由。

### v1.2.0 - 2026-06-03

在最终 PRD、用户故事地图和 QC checklist 输出前加入 Red Team 审核和整改门禁。

### v1.1.0 - 2026-05-18

将 PM Consultant 从固定咨询/code/UAT/retrospective 流程重做为 PRD-first、QC-gated 的需求工作流。

### v1.0.0 - 2026-05-18

以 PM Consultant 身份首次公开发布。
