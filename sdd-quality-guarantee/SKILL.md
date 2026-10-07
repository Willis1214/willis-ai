---
name: sdd-quality-guarantee
description: "Create review-ready SDD Quality Guarantee documents for a task. Must trigger when the user explicitly names SDD, Spec-Driven Development, or $sdd-quality-guarantee and asks to capture requirements, architecture, acceptance, or final quality control. Produces Markdown-only spec, acceptance, Mermaid diagram, and SDD documents. Do not use for ordinary planning, code-only review, or TDD-only case execution."
---

# SDD Quality Guarantee

## Purpose

把用户需求、Spec、架构关系、验收标准和最终证据沉淀为可供他人 Review 的 SDD Quality & Control 文档。SDD 是需求与最终验收的权威档案；它不能用没有证据的推断替代实际验收。

## Hard Boundaries

- 只有用户明确点名 SDD、Spec-Driven Development 或 `$sdd-quality-guarantee` 时才触发。
- 运行时最终产物只能是 Markdown：`spec.md`、`acceptance.md`、`diagram.md`、`SDD.md`。
- `diagram.md` 使用 Mermaid fenced block 表达图；不把 `.svg`、截图或代码文件当作最终 SDD 文档。
- 不修改目标源码、业务文件或原始 Spec，除非用户明确要求修复或更新。
- 不把 TDD 案例表直接冒充 SDD 验收；可以读取 TDD 结果，但必须保留 Spec-to-Evidence 对齐。
- 如果目标、输入、输出、验收标准或关键运行条件不足以作出可信判断，输出 `Reject` 或明确阻塞项。
- `Pass` 只能建立在实际执行、解析、读取、渲染、回归或用户提供的可核验证据上。

## Workflow

1. 绑定任务标识和输出根目录：`output/<task-slug>/sdd-quality-guarantee/SDD/`；不要写入本地 Codex skill 根。
2. 读取用户请求、PRD、现有 Spec、目标产物、TDD 文档和证据索引；按 `references/sdd-output-contract.md` 建立来源清单。
3. 冻结 Spec：记录目标、范围、非目标、输入、输出、数据结构、工作流、异常分支、约束、依赖和 `SDD-REQ-*` / `SDD-ACC-*` ID。
4. 建立架构图：只表达已知的组件、状态、数据流、责任边界和验收关系；未知内容标记 `TBD`，不得为了图完整而编造节点。
5. 建立最终验收：逐条把 Spec 映射到交付证据、TDD 结果、UAT、回归、渲染、readback 或阻塞项。
6. 写入四个 Markdown 文件，并在 `SDD.md` 中汇总 Spec、图、验收结论、证据和 Review 指引。
7. 按 `references/quality-guarantee-review.md` 做静态一致性检查；最终报告明确 `Pass / Fail / Reject`、已验证项和未验证缺口。

## Inputs And Companion TDD

- 有 TDD 时：读取 `TDD.md`、案例结果和证据 ID，但不改变 TDD 原始结果。
- 没有 TDD 时：SDD 可以独立工作；必须在 `acceptance.md` 里说明“未提供 TDD”，并使用可用的直接证据完成或拒绝验收。
- TDD 发现的 `TDD-UNMAPPED` 需求只能作为 SDD 的待确认项，不能静默进入已确认 Spec。

## Resources

- 读取 `references/sdd-output-contract.md`：生成四个 Markdown 文档时使用。
- 读取 `references/quality-guarantee-review.md`：最终 Review、证据等级和 Pass/Fail/Reject 判定时使用。
- 运行 `scripts/scaffold_sdd.py --output-dir output/<task-slug>/sdd-quality-guarantee`：需要创建标准 Markdown 输出骨架时使用。

## Completion Contract

最终回复必须报告：四个 Markdown 文件路径、Spec 条款数、验收条款数、架构图是否生成、Pass/Fail/Reject 结论、证据缺口，以及未执行的检查。不要把本地生成误报为外部发布或远端 readback。
