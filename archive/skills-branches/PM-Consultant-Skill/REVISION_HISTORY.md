# Revision History

## English

### v1.2.0 - 2026-06-03

| Field | Value |
| --- | --- |
| Version | v1.2.0 |
| Date | 2026-06-03 |
| Change Type | Minor update |
| Repository | Willis1214/Skills |
| Branch | PM-Consultant-Skill |

#### Summary

Added a Red Team review and remediation gate before final PRD, user story map, and QC checklist output.

#### Source Skill Changes

- Updated `SKILL.md` so the workflow now has six steps: requirement clarification, user story map, structured confirmation, QC checklist discussion, Red Team review and remediation, and final output package.
- Added rules that unresolved `High` Red Team findings block final output until remediated and confirmed by the user.
- Updated `references/workflow.md` with Red Team gate shape, top-five issue review, and remediation confirmation.
- Updated `references/final-output-contract.md` so final artifacts require Red Team gate evidence.
- Added `QC-011` to `references/qc-checklist-template.md`.
- Added Red Team Gate Summary to `references/prd-template.md`.
- Updated `references/confirmation-summary-template.md` and `agents/openai.yaml` to reflect the new gate.

#### Repository Documentation Changes

- Updated README to describe the Red Team gate, six-step workflow, usage prompt, and v1.2.0 release notes.
- Updated `manifest.json` to version `1.2.0` and release date `2026-06-03`.

#### Compatibility and Migration

- The installable skill name remains `pm-consultant`.
- Existing prompts for PM-style requirement clarification remain compatible.
- Users expecting final artifacts immediately after QC checklist discussion now need to pass the Red Team gate first.

#### Validation

- Branch package validation: pass
- Manifest JSON parse: pass
- Red Team gate keyword and contract check: pass

#### Known Gaps

- No open-source license has been selected.
- The legacy standalone repository `Willis1214/PM-Consultant-Skill` remains online; it was not deleted or archived.

### v1.1.0 - 2026-05-18

| Field | Value |
| --- | --- |
| Version | v1.1.0 |
| Date | 2026-05-18 |
| Change Type | Minor update |
| Repository | Willis1214/Skills |
| Branch | PM-Consultant-Skill |

#### Summary

Reworked PM Consultant from a fixed five-stage product and architecture consulting workflow into a PRD-first, QC-gated requirement workflow.

#### Source Skill Changes

- Updated `SKILL.md` to focus on requirement clarification, user story map, structured confirmation, QC checklist discussion, and final three-artifact output.
- Removed the default code-design and retrospective stages.
- Replaced old `stage-*.md` references with workflow, requirement, PRD, HTML story map, QC checklist, and final output contract templates.

#### Repository Documentation Changes

- Updated README to describe the new PRD-first and QC-gated workflow.
- Updated `manifest.json` to version `1.1.0` and the central `Skills` branch layout.

#### Compatibility and Migration

- The installable skill name remains `pm-consultant`.
- Existing prompts that ask for PM-style requirement clarification still apply.
- Prompts relying on the old default code-design or retrospective stages should now ask for implementation or retrospective explicitly outside this skill's default requirement workflow.

#### Validation

- Local source skill validation: pass
- Branch package validation: pass
- HTML story map template parse/readback: pass
- Manifest JSON parse: pass

#### Known Gaps

- No open-source license has been selected.
- The legacy standalone repository `Willis1214/PM-Consultant-Skill` remains online; it was not deleted or archived.

### v1.0.0 - 2026-05-18

Initial public release of `pm-consultant` as a staged product and architecture consulting skill.

---

## 中文

### v1.2.0 - 2026-06-03

| 字段 | 值 |
| --- | --- |
| 版本 | v1.2.0 |
| 日期 | 2026-06-03 |
| 变更类型 | Minor update |
| 仓库 | Willis1214/Skills |
| 分支 | PM-Consultant-Skill |

#### 摘要

在最终 PRD、用户故事地图和 QC Checklist 输出前，增加 Red Team review and remediation gate。

#### Source Skill 变更

- 更新 `SKILL.md`，将工作流改为六步：需求澄清、用户故事地图、结构化确认、QC Checklist 讨论、Red Team review and remediation、最终输出包。
- 增加规则：未解决的 `High` Red Team findings 会阻止最终输出，直到被修复并由用户确认。
- 更新 `references/workflow.md`，增加 Red Team gate shape、top-five issue review 和 remediation confirmation。
- 更新 `references/final-output-contract.md`，要求最终产物包含 Red Team gate evidence。
- 在 `references/qc-checklist-template.md` 增加 `QC-011`。
- 在 `references/prd-template.md` 增加 Red Team Gate Summary。
- 更新 `references/confirmation-summary-template.md` 和 `agents/openai.yaml`，同步新 gate。

#### 仓库文档变更

- 更新 README，说明 Red Team gate、六步工作流、使用 prompt 和 v1.2.0 release notes。
- 更新 `manifest.json` 到版本 `1.2.0`，发布日期为 `2026-06-03`。

#### 兼容性与迁移

- installable skill name 保持 `pm-consultant`。
- 现有 PM-style 需求澄清类 prompt 仍兼容。
- 期望在 QC Checklist 讨论后立即输出最终文件的用户，现在需要先通过 Red Team gate。

#### 验证

- Branch package validation: pass
- Manifest JSON parse: pass
- Red Team gate keyword and contract check: pass

#### 已知缺口

- 尚未选择开源 License。
- 旧 standalone 仓库 `Willis1214/PM-Consultant-Skill` 仍保留；本次未删除或归档。

### v1.1.0 - 2026-05-18

| 字段 | 值 |
| --- | --- |
| 版本 | v1.1.0 |
| 日期 | 2026-05-18 |
| 变更类型 | Minor update |
| 仓库 | Willis1214/Skills |
| 分支 | PM-Consultant-Skill |

#### 摘要

将 PM Consultant 从固定五阶段产品/架构咨询流程，改造为 PRD-first、QC-gated 的需求工作流。

#### Source Skill 变更

- 更新 `SKILL.md`，聚焦需求澄清、用户故事地图、结构化确认、QC Checklist 讨论和最终三件套输出。
- 移除默认代码设计和复盘阶段。
- 将旧 `stage-*.md` references 替换为 workflow、需求、PRD、HTML 用户故事地图、QC Checklist 和最终输出契约模板。

#### 仓库文档变更

- 更新 README，说明新的 PRD-first 和 QC-gated 工作流。
- 更新 `manifest.json` 到 `1.1.0`，并记录中央 `Skills` 分支布局。

#### 兼容性与迁移

- installable skill name 保持 `pm-consultant`。
- 现有 PM-style 需求澄清类 prompt 仍适用。
- 依赖旧默认代码设计或复盘阶段的 prompt，应在本 skill 的默认需求流程之外明确请求实现或复盘。

#### 验证

- 本地 source skill validation: pass
- 分支包 validation: pass
- HTML 用户故事地图模板 parse/readback: pass
- Manifest JSON parse: pass

#### 已知缺口

- 尚未选择开源 License。
- 旧 standalone 仓库 `Willis1214/PM-Consultant-Skill` 仍保留；本次未删除或归档。

### v1.0.0 - 2026-05-18

`pm-consultant` 作为阶段式产品与架构咨询 skill 首次公开发布。
