# TDD Quality Guarantee

## English

TDD Quality Guarantee turns SDD requirements into reviewable test cases, execution results, evidence mappings, and a final Test-Driven Development quality record. It makes positive, negative, edge, regression, integration, and side-effect coverage explicit instead of treating a generic “tests passed” statement as proof.

The runtime deliverables are Markdown-only:

- `spec_inventory.md`: the SDD/Spec requirements used as the test basis.
- `test_cases.md`: detailed cases with function/workflow mapping and rationale.
- `test_results.md`: observed results, evidence, failures, blockers, and unmapped findings.
- `TDD.md`: the Review entry point with Spec-to-Test-to-Evidence traceability and final TDD conclusion.

Use it when the user explicitly asks for TDD, Test-Driven Development, or TDD Quality Guarantee. It is not ordinary testing advice, static code review, SDD-only acceptance, or a license to silently change the Spec.

The package is published for GitHub distribution. This release does not install the skill into a local Codex environment or project.

### Package contents

- `tdd-quality-guarantee/SKILL.md`
- `tdd-quality-guarantee/agents/openai.yaml`
- `tdd-quality-guarantee/references/tdd-output-contract.md`
- `tdd-quality-guarantee/references/quality-guarantee-review.md`
- `tdd-quality-guarantee/scripts/scaffold_tdd.py`
- `tdd-quality-guarantee/scripts/validate_tdd_report.py`

## 中文

TDD Quality Guarantee 把 SDD 需求转成可 Review 的测试案例、执行结果、证据映射和最终 TDD 质量文档。它明确记录正向、反向、边界、回归、融合/集成和副作用覆盖，不把“测试通过”这种泛化描述当成完整证据。

运行时最终产物全部为 Markdown：

- `spec_inventory.md`：作为测试依据的 SDD/Spec 需求清单；
- `test_cases.md`：含 function/workflow 映射和案例理由的详细案例；
- `test_results.md`：实际结果、证据、失败、阻塞和未映射发现；
- `TDD.md`：含 Spec-to-Test-to-Evidence 追踪和最终 TDD 结论的 Review 入口。

只有用户明确点名 TDD、Test-Driven Development 或 TDD Quality Guarantee 时使用。它不替代普通测试建议、静态代码审查或 SDD-only 验收，也不能静默修改 Spec。

本分支用于 GitHub 分发；本次发布不会把 skill 安装到本地 Codex 环境或项目中。

### 版本

`1.0.0` — 首次发布，建立 Markdown-only TDD Quality & Control 文档合同。

### License

No open-source license has been selected for this release. Treat the contents as all rights reserved unless the repository owner adds a license.
