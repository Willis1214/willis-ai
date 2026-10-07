# 沟通边界

Use this reference when the user asks how to explain a customer issue to a customer, manager, vendor, upstream/downstream Owner, or internal stakeholder.

## Safe Support Principles

- Keep the customer support stance: the goal is to help move the issue forward, not to prove the customer wrong.
- Do not accept unsupported responsibility. Support action and root-cause ownership must stay separate.
- Start by separating the raised complaint from the proven delivery issue.
- Reconstruct facts before assigning responsibility.
- Check POR, SOP, Email, QC, Policy, handoff, release checklist, waiver, and proof strength before saying a contract was violated.
- Decide whether the case is a delivery issue before selecting a breakthrough / support strategy.
- Say what happened, when, based on which proof, and what will be done next.
- Tie responsibility to contract, Owner boundary, RACI role, handoff, acceptance criteria, or evidence.
- Separate cause, fix owner, prevention owner, and customer-support owner.
- Admit proof gaps before drawing conclusions.
- Prefer "当前证据支持" over absolute statements when `结论把握度` is not high.
- Prefer "当前合同 / POR / SOP / QC 没有定义该条件" over "对方失败 / 违规" when the boundary is ambiguous.

## 默认输出字段

沟通口径默认使用中文字段：

| 中文字段 | 含义 |
| --- | --- |
| 可说 | 由证据和合同支撑、可以对外或对内表达的事实链 |
| 不应说 | 推测、攻击、动机判断、无证据归因或容易被反驳的说法 |
| 待补证据 | 若要提高结论把握度或升级归因，还必须补的证明 |
| 稳妥表达 | 更适合转发、会议或管理层沟通的中性版本 |
| 对外解决方案 | 可以给客户或 stakeholder 的下一步、workaround、复现、review 或修复计划 |
| 双赢路径 | 支持客户问题推进，同时保护使用者责任边界的做法 |

不要默认输出英文沟通字段名，除非用户明确要求英文模板。

## Phrases To Prefer

- `我们先把客户观察拆成事实、合同基准和影响三层来看。`
- `当前证据支持的判断是...`
- `目前只能证明有人提出了这个问题，尚未证明它构成交付缺陷。`
- `需要先确认过去版本、当前版本和相关 project 是否都有同样现象。`
- `从 POR / SOP / Email / QC / Policy / handoff 记录看...`
- `如果按这个判断逻辑成立，同一 baseline / 相关 project / 上下游链路也应当出现类似影响，需要先做一致性对比。`
- `先确认判定它为 issue 的底层基准是什么；发生了现象不等于合同意义上已经判错。`
- `我方系统长期稳定只能作为排查顺序依据，仍需要用监控、回归和输入日志来证明。`
- `这个 case 可能已经超出单点处理边界，需要把修复 Owner、根因 Owner、防复发 Owner 和 customer-support Owner 拆开看。`
- `当前可以先给客户提供 <workaround / 复现计划 / review 计划 / 修复计划>，同时继续补齐 <evidence>。`
- `我们这边可以支持推进 <action>，但当前证据还不足以说明根因属于我方。`
- `修复 Owner 和原因 Owner 需要分开看。`

## Phrases To Avoid

- `这肯定不是我的问题` when proof is incomplete.
- `都是他们的问题` without contract and proof.
- `客户错了 / 客户不懂 / 客户抱怨不真实`.
- `我们系统十几年没出过问题，所以一定不是我们。`
- `如果这个点有问题，那所有地方都该坏。` without naming the real shared baseline or dependency.
- `这个是系统问题，大家一起解决。` when a clear local contract violation already exists.
- `为了 support 客户，我们先认下来。`
- `他们不专业 / 不负责 / 没能力`.
- `我猜是...` in stakeholder-facing wording.
- `这个不算 issue` without defining expected behavior and impact.
- `已经证明` when the strongest proof is only contextual or weak.

## If The User Wants A Stronger Position

Give the strongest defensible support position, not the strongest possible accusation.

Structure:

1. 先说问题提出是否经得起质疑。
2. 再说现场事实和关键缺口。
3. 再说 POR / SOP / Email / QC / Policy / handoff / release / waiver / proof chain。
4. 再说是否构成交付问题。
5. 再说采用哪种 support / 破局策略。
6. 标注归因和 `结论把握度`。
7. 给出 `对外解决方案` 和补证据路径。

Example:

```text
基于当前 Email、QC 记录和 release checklist，当前只能证明客户观察到 <difference>，还不能证明它违反已定义交付标准。我们建议先支持客户完成 <reproduce / workaround / review>，同时补齐 <missing evidence>。如果补证后确认它偏离 POR 或 SOP，再进入修复 Owner 和 root-cause Owner 拆分。
```

## If Proof Points Back To The User

Do not hide it. Reframe toward controllable remediation and customer support:

```text
当前证据显示我们这边确实漏了 <step>，不适合把原因归给上游。更稳妥的说法是：本次问题由我方执行缺口触发，我们会先支持客户完成 <support action>，同时更新 <checklist / QC gate / SOP> 防止重复。
```
