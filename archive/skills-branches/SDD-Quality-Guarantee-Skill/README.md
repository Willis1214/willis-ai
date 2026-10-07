# SDD Quality Guarantee

## English

SDD Quality Guarantee turns a task's requirements into a review-ready Specification and Quality & Control record. It captures scope, non-goals, inputs, outputs, workflows, architecture, acceptance criteria, evidence, gaps, and a final `Pass`, `Fail`, or `Reject` decision.

The runtime deliverables are Markdown-only:

- `spec.md`: source-backed requirements and constraints.
- `acceptance.md`: acceptance matrix, UAT, side effects, and evidence.
- `diagram.md`: Mermaid architecture, workflow, state, or traceability diagram.
- `SDD.md`: the compact Review entry point linking the complete record.

Use it when the user explicitly asks for SDD, Spec-Driven Development, or SDD Quality Guarantee. It is not a replacement for executable code QC/UAT, static code review, or TDD case execution.

The package is published for GitHub distribution. This release does not install the skill into a local Codex environment or project.

### Package contents

- `sdd-quality-guarantee/SKILL.md`
- `sdd-quality-guarantee/agents/openai.yaml`
- `sdd-quality-guarantee/references/sdd-output-contract.md`
- `sdd-quality-guarantee/references/quality-guarantee-review.md`
- `sdd-quality-guarantee/scripts/scaffold_sdd.py`
- `sdd-quality-guarantee/scripts/validate_sdd_report.py`

## 中文

SDD Quality Guarantee 把任务需求沉淀成可供他人 Review 的 Spec 与 Quality & Control 文档。它记录范围、非目标、输入、输出、工作流、架构、验收标准、证据、缺口以及最终 `Pass`、`Fail` 或 `Reject` 结论。

运行时最终产物全部为 Markdown：

- `spec.md`：基于来源的需求和约束；
- `acceptance.md`：验收矩阵、UAT、副作用和证据；
- `diagram.md`：Mermaid 架构图、流程图、状态图或追踪图；
- `SDD.md`：供 Review 使用的总入口文件。

只有用户明确点名 SDD、Spec-Driven Development 或 SDD Quality Guarantee 时使用。它不替代可执行代码 QC/UAT、静态代码审查或 TDD 案例执行。

本分支用于 GitHub 分发；本次发布不会把 skill 安装到本地 Codex 环境或项目中。

### 版本

`1.0.0` — 首次发布，建立 Markdown-only SDD Quality & Control 文档合同。

### License

No open-source license has been selected for this release. Treat the contents as all rights reserved unless the repository owner adds a license.
