# 调查方法论

这些方法用于客户 issue support 场景下的问题提出质疑、现场还原、合同 / 证据审查、交付问题判断、破局策略选择和归因沟通。只在相关场景读取，不要把所有方法机械套用到每个问题。

## Customer Support Outcome

使用场景:
- 来自客户或 stakeholder 的 issue 需要被认真支持，但现有证据不足以让使用者承担责任。
- 用户需要对外输出解决办法，同时保留责任边界。
- 目标不是“证明客户错”，而是把争议转成可验证、可执行、可共赢的 support path。

核心原则:
- Support action 不等于 root-cause ownership。
- 对外解决方案必须和证据强度匹配：证据不足时输出补证据、复现、workaround、review；证据充分时输出修复、Owner、预防。
- 如果 POR、SOP、Email、QC、Policy、handoff、release checklist 或 waiver 没有定义责任，不能为了安抚客户而承认交付责任。
- 如果证据证明我方确有责任，不隐藏；直接转成修复计划、客户支持和防复发动作。

默认输出:
- `客户支持目标`: 当前要帮助客户完成什么。
- `责任边界`: 哪些责任已被证据支持，哪些尚未被支持。
- `对外解决方案`: 复现、补证、workaround、修复、review、流程修补或正式回复。
- `双赢路径`: 客户问题被推进，使用者不承担不该承认的责任。

## Complaint Validity Challenge

使用场景:
- 客户、Requester、上游、下游或内部 reviewer 提出“这里有问题”。
- 看到差异不一定等于合同意义上的 defect。
- 需要先确认“问题是否真实成立”，再进入责任讨论。

核心问题:
- 谁提出问题？原话是什么？有没有截图、样例、复现步骤或交付包对比？
- 提出方拿什么做基准：合同、spec、旧版本、当前 upstream、相关 project、行业惯例，还是主观期待？
- 过去有没有同样现象：旧版本、旧 release package、旧 upstream、旧模板是否已经存在？
- 现在有没有同样现象：当前 release、当前 upstream、当前环境是否仍可复现？
- 相关 project 有没有同样现象：fully copy 来源项目、兄弟项目、同客户项目、同版本分支是否也存在？
- 差异是否有实质影响：是否影响已承诺交付、客户使用、验收标准或安全/合规边界？

待补证据:
- 客户原话、截图、复现方式、合同条款、验收标准、影响范围。
- 旧 release package、旧 upstream、历史验收记录、相关 project diff。
- 当前 release package、当前 upstream、当前环境复现结果。

可能结论:
- 观察真实，但问题尚未成立。
- 只能证明存在差异，还不能证明是 defect。
- 问题成立，但归因仍未明确。
- complaint 实际是 change request、preference 或 scope drift。

高风险说法:
- “客户抱怨不真实。”
- “这不算 issue。”但没有说明 expected behavior 和影响。
- “过去没人报，所以现在也不是问题。”

稳妥表达:
- “先把客户观察拆成事实层和合同缺陷层：当前只能证明存在 <difference>，是否构成 issue 还要看基准、历史、相关 project 和影响。”

## Breakthrough Operating Loop

使用场景:
- 用户被要求马上 `改代码`、`查 Bug`、`认领问题`，但问题是否成立、基准是否正确、归因是否清楚还没有被证明。
- 客户 support 需要继续推进，但不能在证据不足时先承认我方交付责任。
- 排查陷入僵局，继续单人低层 debugging 不能形成对外解决办法。
- 争议已经超出单点执行动作，需要把问题重新放回系统、合同、上下游、客户影响和流程边界中判断。

默认顺序:
1. 先质疑问题是否成立: 不把 complaint、alarm、review comment 直接等同于 defect。
2. 再还原现场: 已知事实、时间线、缺口、暂定假设。
3. 再审合同和证据: POR、SOP、Email、QC、Policy、handoff、release checklist、waiver、proof strength。
4. 再判断是否构成交付问题: expected behavior、actual behavior、material impact。
5. 再选择破局 / 支持策略: `冲突扩大法`、`底层溯源法`、`归因防御策略`、`困境转化法`。
6. 最后做归因和沟通: attribution matrix、Owner / RACI、`结论把握度`、对外解决方案、双赢路径。

工作流改进:
- 面对他人提出 issue 时，第一动作不是接 bug，而是提出最小证据问题。
- 面向客户 support 时，第一输出不是责任结论，而是当前可以支持客户推进的下一步。
- 面对复杂僵局时，停止围绕报错本身打转，改查“判断该报错的基准是否有效”，再给对外方案。
- 面对成熟系统突发异常时，把新输入、新上游、新环境、新发布控制作为一线假设，同时列出我方稳定性证据。
- 面对 corner / edge / special case 时，不把全部压力留在一个执行者身上，而是拆成 root-cause owner、fix owner、prevention owner、customer-support owner。

## 冲突扩大法

使用场景:
- 提出方基于一个 single issue 推导出“这里一定是你的错”。
- 用户陷入局部自证，只能解释当前点，无法检验对方逻辑本身是否成立。
- 同类系统、复制来源、兄弟 project、上下游链路按对方逻辑应当一起受影响。

核心动作:
- 先暂时接受提出方前提: “如果这个判断逻辑成立...”
- 沿系统边界推演: 哪些模块、release、客户、baseline、上游输入、下游输出也应当出现同类异常？
- 反问缺口: 为什么这些地方没有出问题、没有报警、没有投诉，或历史上已经被接受？
- 把讨论从“单点背锅”拉回“系统性一致性检验”，让客户 support 基于共同证据推进。

待补证据:
- 系统架构、模块依赖、复制来源、相关 project、历史 release、当前 release、上下游接口记录。
- 提出方判断逻辑的明确表述，而不是转述后的情绪化结论。

可能结论:
- 提出方逻辑只能解释单点观察，不能解释系统事实，问题尚未成立。
- 如果提出方逻辑成立，应当触发更大范围 review，不能只由单一 Owner 承担。
- 单点确实异常，但属于局部差异，需要继续查合同、baseline 或输入条件。

风险边界:
- 没有系统视野时不要做大范围推演。
- 不要把“没有其他投诉”当成决定性证据；它只能作为反问线索。
- 不要编造其他模块影响，只能推导对方前提必然牵连的范围。

稳妥表达:
- “如果按这个判断逻辑成立，同一 baseline / 同一上游输入 / 同类 project 理论上也应该出现相同影响。我们建议先对比这些位置，再给客户一个基于证据的 support 结论和下一步。”

## 底层溯源法

使用场景:
- 排查停留在表层报错、单一观察、习惯性判断或 reviewer 的判错结论。
- 当前争议的关键不是“有没有现象”，而是“判断它错的基准是否成立”。
- 需要追到行业规则、接口契约、物理约束、SOP、验收标准或系统 invariant。

核心动作:
- 连续追问 `为什么`: 为什么这是错？为什么这个基准适用？为什么当前场景必须遵守它？为什么替代基准不适用？
- 区分事实和评价: 发生了什么，不等于它在合同意义上错误。
- 追到可判定底层: spec、SOP、API contract、acceptance criteria、release gate、baseline、行业/物理约束。
- 如果底层基准不存在或不适用，转入 `约定缺口`、`证据缺口` 或 `范围漂移`，不要继续假装已有定论。

待补证据:
- 原始判断依据、规范条款、验收标准、接口定义、历史 accepted behavior、行业规则或系统 invariant。

可能结论:
- 表层现象真实，但判错基准不成立。
- 判错基准成立，但适用范围不覆盖当前场景。
- 判错基准成立且覆盖当前场景，继续进入合同履约和归因。

风险边界:
- 不要把 `问到底` 变成无限争辩；当下一层没有可验证证据时必须停止。
- 不要用抽象原则覆盖已经明确写下的合同或验收标准。

稳妥表达:
- “现在先确认判定这个现象为 issue 的底层基准是什么；如果基准不适用，我们仍可以支持客户做复现、说明边界或提出变更路径，但不能直接承认交付责任。”

## 归因防御策略

使用场景:
- 一个长期稳定、边界清楚、监控或回归记录充分的系统突然被归因为问题源头。
- 突发异常发生前后存在上游输入、环境、配置、权限、release control、外部系统或数据变化。
- 用户需要先快速排除自身成熟底座的嫌疑，同时继续给客户可行动的 support 路径。

核心动作:
- 明确我方系统稳定性证据: 运行历史、最近变更、监控、回归、同版本表现、输入输出 contract。
- 优先列出新变量: 上游数据、外部接口、环境策略、权限、配置、release 包、调用方式、时间窗口。
- 先验证外部假设: 要求原始输入、日志、diff、变更记录、复现条件。
- 同时保留自证条件: 如果我方最近变更、监控异常或回归失败，必须把我方责任重新拉回假设地图。

待补证据:
- 我方最近变更记录、监控/报警、回归结果、接口输入日志、上游变更、环境变更、同类场景对比。

可能结论:
- 外部新变量更可能触发异常。
- 我方成熟系统仍需补监控或回归证据才能防御归因。
- 我方确有变更或异常，不能继续使用成熟系统假设。

风险边界:
- 只适用于用户确实熟悉且有证据支持的成熟系统。
- 不能把“十几年没出问题”当成唯一证据。
- 不能用来无脑甩锅；每个外部假设都要配待补证据。

稳妥表达:
- “这个系统长期稳定只能说明我方底座不是默认第一嫌疑，但还需要用最近变更、监控和输入日志证明。我们可以先支持客户核对新增上游/环境变量和复现条件，再决定责任和修复 Owner。”

## 困境转化法

使用场景:
- 问题被定位为 corner case、edge case、special case，继续由单人处理会陷入低效死磕。
- 现有合同、流程、架构或 Owner 边界没有覆盖新场景。
- 修复动作、根因责任和防复发责任属于不同 Owner。

核心动作:
- 升维定性: 把它从“某个人的 bug”改写为“系统演进暴露的新边界 / 流程缺口 / 架构适配问题”。
- 拆 Owner: root-cause owner、fix owner、prevention owner、release/acceptance owner 分开列。
- 拉通上下游: 提出最小 review 议题、需要谁参加、需要哪些证据、要产出什么决策。
- 输出 win-win 路径: 先支持客户止血、再厘清 Owner、再修 contract/gate、最后沉淀防复发规则。

待补证据:
- 触发条件、复现样例、现有 contract 覆盖范围、上下游责任矩阵、修复可行性、预防 gate 位置。

可能结论:
- 单点修复可做，但根因属于系统设计或流程缺口。
- 本地没有足够权限关闭风险，需要跨 Owner 决策。
- 当前 case 应转成 review / change-control / architecture decision。

风险边界:
- 不要把普通本地 bug 包装成系统问题。
- 升级前要说明为什么单点行动无法完全关闭风险。
- 拉通 review 要给明确议题，不要只制造会议。

稳妥表达:
- “这个 case 已经超出单点修复边界，更像系统演进带来的新边界问题。建议先给客户明确 support 动作，再把修复 Owner、根因 Owner、防复发 Owner 和 customer-support Owner 拆开，拉上下游做一次最小 review。”

## Legacy Issue Analysis

使用场景:
- 问题来自长期存在的模板、旧系统、旧流程、历史产品或多年未改的交付物。
- 有人用“过去一直这样”或“以前没人投诉”作为判断依据。

核心问题:
- 旧版本是否也存在同一差异？
- 过去无人投诉，是没人发现、未触发场景，还是已有共识？
- 是否存在 waiver、accepted deviation、known limitation 或 special handle？
- 当前客户、场景、合同、验收标准是否不同？

待补证据:
- 旧 release package、旧 upstream、旧验收记录、release notes。
- 老邮件、ticket、waiver、deviation list、known issue list。
- 历史客户 complaint / no complaint 记录。

可能结论:
- latent legacy issue 被新产品暴露。
- 历史 accepted deviation 在当前项目未被继承或未被确认。
- 当前投诉属于新场景触发，不是当前开发首次引入。
- 缺少历史证据时，只能作为背景证据。

高风险说法:
- “十几年没人投诉，所以客户错了。”
- “这是前人的问题，和当前 release 无关。”

稳妥表达:
- “长期无投诉不能直接证明没有问题，但它提示需要追溯历史 acceptance、waiver 或 special handle，再判断当前 complaint 是否构成 defect。”

## Baseline / Delta Analysis

使用场景:
- 项目要求 fully copy、clone、migration、版本继承或按某个 baseline 发布。
- 当前结果与原始模板、上游文件或 release package 不一致。

核心问题:
- 原始 baseline 是什么？
- 后续是否发生过 baseline change？
- change 是否进入 change control？
- release 时 frozen baseline 是哪个版本？
- 当前 complaint 是对比哪个 baseline 提出的？

待补证据:
- baseline 定义、copy 指令、版本号、commit、变更记录。
- release checklist、approval、frozen package、diff 报告。

可能结论:
- 当前执行符合原 baseline，但 baseline 后续漂移。
- release gate 未捕捉 upstream 与 final product 的差异。
- fully copy 本身复制的是 legacy package，而不是干净规格。

高风险说法:
- “我 fully copy 了，所以后续都不归我管。”

稳妥表达:
- “需要先确认 release 时采用的 frozen baseline，再判断当前差异是执行偏差、baseline drift，还是 change-control gap。”

## Waiver / Special Handle Search

使用场景:
- 历史上有偏离标准但长期保留的行为。
- 有人怀疑这是 deliberate exception，而不是漏检。

核心问题:
- 是否有人正式接受过该偏差？
- special handle 的适用范围是谁、哪个客户、哪个版本、哪个场景？
- 当前项目是否继承该 exception？
- exception 是否有到期、条件或替代方案？

待补证据:
- waiver、deviation approval、meeting minutes、customer sign-off、exception list。

可能结论:
- 当前行为受历史 waiver 支持。
- waiver 不适用于当前客户或新版本。
- 没有证据，不能把历史沉默当成批准。

高风险说法:
- “以前都这样，所以这是默认同意。”

稳妥表达:
- “除非找到 waiver 或 special handle 记录，否则历史沉默只能算背景证据，不能直接作为 approval。”

## Change Control Drift

使用场景:
- 有人修改 upstream、配置、scope、requirement 或 handoff input，但最终交付没有同步。

核心问题:
- 谁提出 change？
- 谁批准 change？
- 谁负责 downstream sync？
- 是否通知 release Owner 和 QA？
- checklist 是否覆盖 change impact？

待补证据:
- change request、commit、review、approval、notification、release checklist。

可能结论:
- change 本身合理，但没有进入 release control。
- upstream Owner 未完成 impact handoff。
- downstream release gate 未发现 mismatch。

高风险说法:
- “我只是好心提醒，所以没有责任。”

稳妥表达:
- “需要区分 change 的正确性、change handoff、release consistency check 三层责任。”

## RACI / Handoff Boundary

使用场景:
- 多个 team、Owner、上游、下游、客户或 release gate 共同参与。

核心问题:
- 谁 Responsible 执行？
- 谁 Accountable 签核？
- 谁 Consulted 提供必要输入？
- 谁 Informed 只需要被通知？
- handoff contract 是否写清输入、输出、时间和验收方式？

待补证据:
- RACI、SOP、handoff checklist、邮件确认、ticket Owner、approval chain。

可能结论:
- 执行 Owner 与签核 Owner 不同。
- 修复 Owner 与根因 Owner 不同。
- 没有定义 Owner，属于流程 / 约定缺口。

高风险说法:
- “谁最后碰过就是谁负责。”

稳妥表达:
- “需要把 Responsible、Accountable、Consulted、Informed 拆开，否则会把执行责任、签核责任和修复责任混在一起。”

## Fix Owner vs Root Cause Owner

使用场景:
- 用户需要推进修复，但责任归因还没有定论。

核心问题:
- 谁最适合修复？
- 谁导致问题？
- 谁拥有防复发流程？
- 哪些 action 是止血，哪些 action 是预防？

待补证据:
- ownership map、代码/文件 Owner、流程 Owner、approval Owner、SOP Owner。

可能结论:
- 我方负责修复，不等于我方是根因。
- 上游是根因 Owner，但下游需要增加 resilience 或 release check。
- 流程 Owner 需要更新 gate。

高风险说法:
- “谁修就是谁的锅。”

稳妥表达:
- “修复 Owner 和 root cause Owner 要分开；当前先明确谁能关闭风险，再基于证据讨论根因归属。”
