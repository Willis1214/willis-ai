# TDD Quality Guarantee Output Contract

所有运行时最终文件均为 Markdown。默认输出根目录为 `output/<task-slug>/tdd-quality-guarantee/TDD/`。

## 1. `spec_inventory.md`

```markdown
# Spec Inventory

## Source Documents
| Source | Type | Authority | Readback | Status |
| --- | --- | --- | --- | --- |

## SDD Requirements
| Spec ID | Requirement | Workflow/Function | Acceptance Anchor | TDD Coverage |
| --- | --- | --- | --- | --- |

## Unclear Or Unmapped Requirements
| ID | Description | Why It Matters | Owner/Next Action |
| --- | --- | --- | --- |
```

## 2. `test_cases.md`

每个案例必须有唯一 `TDD-CASE-001` ID，且不能使用泛化名称。

```markdown
# Test Cases

## Coverage Gate
- Positive cases:
- Negative/exception cases:
- Edge cases:
- Regression cases:
- Integration/fusion cases:
- Side-effect/readback cases:

## Case Matrix
| Case ID | Type | Spec Anchor | Function/Workflow | Preconditions | Input | Action | Expected | Evidence Method | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Case Design Rationale
## Waivers And Non-Applicable Cases
```

适用的 `Type`：`Acceptance`、`Workflow`、`Edge`、`Regression`、`Integration`、`Side-effect`。

## 3. `test_results.md`

```markdown
# Test Results

## Execution Summary
- Planned:
- Passed:
- Failed:
- Blocked:
- Not Executed:

## Result Matrix
| Case ID | Spec Anchor | Expected | Observed | Evidence | Result | Failure/Gap |
| --- | --- | --- | --- | --- | --- | --- |

## Red-Green-Refactor Evidence
## Failed And Blocked Cases
## Unmapped Findings
```

案例状态只能使用：`Planned`、`Passed`、`Failed`、`Blocked`、`Not Executed`。

## 4. `TDD.md`

```markdown
# TDD Quality Guarantee

## Review Summary
## SDD Content Covered
## Case Design Summary
## Execution Result Summary
## Spec-to-Test-to-Evidence Traceability
| Spec ID | Case IDs | Expected | Observed | Evidence | Result |
| --- | --- | --- | --- | --- | --- |
## Positive/Negative/Edge/Regression/Integration Coverage
## Failures, Blockers And Unmapped Requirements
## Final TDD Conclusion
## Reviewer Checklist
## Linked Markdown Artifacts
```

最终 TDD 结论建议使用：`Complete`、`Failed`、`Incomplete`。它不是 SDD 的 `Pass / Fail / Reject` 替代品。

## Case Detail Standard

每个关键案例至少解释：为什么选这个案例、它验证哪条 Spec、如果失败意味着什么、证据在哪里、是否会阻塞最终验收。
