# Quality Guarantee Review Rubric

## Required Case Coverage

默认每条 `SDD-REQ-*` 或 `SDD-ACC-*` 需要：

1. 一个正向案例，证明正常输入和正常路径成立。
2. 一个反向或异常案例，证明错误输入、异常状态或拒绝条件被正确处理。

然后按任务适用性补充：

- `Edge`：空值、边界值、重复执行、编码、缺文件、时区或资源缺失；
- `Regression`：旧行为、旧接口、旧文件或未请求修改的资源仍保持；
- `Integration`：两个以上 Spec 条款或多个 function/workflow 组合后的真实路径；
- `Side-effect`：文件写入、远端写入、发送、readback、重复发送和目标确认。

## Case Quality

案例必须回答：

- 它验证哪个 Spec anchor？
- 它验证哪个 function、接口、工作流或用户可见行为？
- 前置条件和输入是什么？
- 预期输出、状态或错误是什么？
- 观察到了什么？
- 哪个证据支持结果？
- 失败会影响最终验收还是只影响非阻塞项？

## Evidence Strength

- `Strong`：实际命令输出、解析结果、readback、渲染、截图或用户确认。
- `Medium`：静态结构检查，且绑定明确的 Spec 条款。
- `Weak`：仅凭推断、命名或模型判断。

不能只用 `Weak` 证据声明关键案例通过。

## Final Review

检查是否存在：

- 需求没有案例；
- 案例没有实际结果；
- 计划被误写成通过；
- 只测正向、不测拒绝和异常；
- 案例只测单个 function，遗漏融合后的真实 workflow；
- TDD 暗中新增 Spec；
- 失败、阻塞或未执行项被删除；
- 副作用或远端 readback 未验证。
