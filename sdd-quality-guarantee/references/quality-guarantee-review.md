# Quality Guarantee Review Rubric

## Requirement Completeness

检查 Spec 是否覆盖：

- goal、scope、non-goals；
- input、output、data、workflow、state；
- exception、edge、regression、side-effect；
- target、runtime、dependency、delivery 和 readback；
- 每条需求的来源、优先级和可验收标准。

## Traceability

每条 `SDD-REQ-*` 应能追踪到：

`SDD-REQ-* → SDD-ACC-* → TDD-CASE-* → EVID-* → Result`

没有 TDD 时，可以使用直接证据，但必须明确 `TDD not provided`。

## Acceptance Decision

- `Pass`：关键 Spec、验收、回归和副作用证据完整，没有 release blocker。
- `Fail`：实际检查证明存在 Spec 违反、错误输出、崩溃、数据损坏或交付失败。
- `Reject`：缺少目标、Spec、运行条件、数据或验收标准，无法可信判断。

## Review Questions

1. 这份 SDD 是否说明了“必须满足什么”，而不是只复述实现步骤？
2. 每条结论是否有证据，而不是只有模型判断？
3. 图是否来自已确认内容，是否隐藏了未声明的架构假设？
4. TDD 结果是否被正确引用，是否把 Planned 误写为 Passed？
5. 非目标、失败、阻塞、未执行项是否被保留？
6. 是否存在修改原始资源、错误目标、重复交付或缺少 readback 的风险？
