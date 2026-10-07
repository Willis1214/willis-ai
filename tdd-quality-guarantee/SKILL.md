---
name: tdd-quality-guarantee
description: "Create review-ready TDD Quality Guarantee documents for a task. Must trigger when the user explicitly names TDD, Test-Driven Development, or $tdd-quality-guarantee and asks for test cases, coverage, execution results, or quality control. Produces Markdown-only Spec inventory, test cases, test results, and TDD documents. Do not use for ordinary testing advice, static code review, or SDD-only acceptance."
---

# TDD Quality Guarantee

## Purpose

把 SDD 需求拆成可审查、可执行、可追踪的测试案例，并把实际结果、证据、失败原因和最终结论沉淀为 TDD Quality & Control 文档。TDD 是案例与证据档案，不单独取代 SDD 的需求权威和最终验收责任。

## Hard Boundaries

- 只有用户明确点名 TDD、Test-Driven Development 或 `$tdd-quality-guarantee` 时才触发。
- 运行时最终产物只能是 Markdown：`spec_inventory.md`、`test_cases.md`、`test_results.md`、`TDD.md`。
- 不把泛化的“测试成功”写成案例；每个案例必须有 Spec 锚点、前置条件、输入、动作、预期、实际、证据和结果。
- 不修改目标源码、业务文件或 SDD，除非用户明确要求修复或更新。
- 不把测试计划误报为测试结果；`Planned`、`Passed`、`Failed`、`Blocked`、`Not Executed` 必须区分。
- 发现未映射需求时使用 `TDD-UNMAPPED`，不要静默扩展 Spec。
- 代码任务可以执行 Red-Green-Refactor；文档、配置、自动化和其他非代码任务使用适配的验收/流程/边界/回归/副作用案例。

## Coverage Gate

每次 TDD 至少完成以下覆盖，除非在文档中明确记录不适用理由：

- 每个 `SDD-REQ-*` 或 `SDD-ACC-*` 至少一个正向案例和一个反向/异常案例。
- 每个公开 function、CLI/API 行为、文档交付接口或关键业务行为至少有一个直接案例。
- 每个主要工作流至少有一个融合/集成案例，验证多个 Spec 条款组合后的真实结果。
- 每个边界、回归风险、文件写入、外部副作用或 readback 要求至少有一个对应案例。
- 总体案例必须覆盖 `Acceptance`、`Workflow`、`Edge`、`Regression`、`Integration`、`Side-effect` 六类中的适用项。
- 某类案例不适用时，写明“不适用理由”和审查影响；不得用空行或泛化描述代替。

## Workflow

1. 绑定任务标识和输出根目录：`output/<task-slug>/tdd-quality-guarantee/TDD/`；不要写入本地 Codex skill 根。
2. 读取 SDD、用户请求、PRD、目标源码/文档、现有测试和验收约束；按 `references/tdd-output-contract.md` 建立 Spec inventory。
3. 为每条 Spec 生成 `TDD-CASE-*`：说明案例类型、映射的 function/workflow、前置条件、输入、动作、预期状态和证据方式。
4. 先做案例质量 Review，再执行可执行检查、用户流程、解析、渲染、回归、边界、外部 readback 或静态证据收集。
5. 逐条记录实际结果和证据，失败或阻塞案例不得被改写成通过；发现额外需求时创建 `TDD-UNMAPPED-*`。
6. 写入四个 Markdown 文件，并在 `TDD.md` 汇总 Spec 内容、案例设计理由、执行结果、覆盖率、缺口和最终 TDD 结论。
7. 按 `references/quality-guarantee-review.md` 做覆盖、追踪、证据强度和 Review 完整性检查。

## Code And Non-Code Modes

- 代码任务：优先从最小行为开始，记录 Red、Green、Refactor 的输入和观察结果；测试必须证明公开行为，而不是只证明内部实现细节。
- 非代码任务：使用 Acceptance、Workflow、Edge、Regression、Integration 和 Side-effect 案例；不得为了满足“测试”二字而编造单元测试。
- 只有 Spec 没有目标执行对象时：可以输出 `Planned` 案例，但最终结论必须是 `Incomplete` 或明确阻塞，不得声称执行完成。

## Resources

- 读取 `references/tdd-output-contract.md`：生成四个 Markdown 文档时使用。
- 读取 `references/quality-guarantee-review.md`：案例质量、证据等级和最终结论 Review 时使用。
- 运行 `scripts/scaffold_tdd.py --output-dir output/<task-slug>/tdd-quality-guarantee`：需要创建标准 Markdown 输出骨架时使用。

## Completion Contract

最终回复必须报告：四个 Markdown 文件路径、Spec 条款数、案例总数及分类数量、Passed/Failed/Blocked/Not Executed 数量、未映射需求、最终 TDD 结论和证据缺口。不要把案例计划误报为已执行测试。
