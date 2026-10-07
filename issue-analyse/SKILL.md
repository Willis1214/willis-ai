---
name: issue-analyse
description: Customer-issue support analysis that first challenges whether a reported issue is established, reconstructs facts, checks POR/SOP/Email/QC/Policy/handoff/release/waiver evidence, decides whether it is a delivery issue, selects a win-win support strategy, and prepares attribution plus Chinese communication. Use when the user needs to support a customer or stakeholder issue without accepting responsibility that is not supported by evidence, while still outputting an external-facing solution path. Do not use for pure source-code release review, executable QC/UAT, generic risk review, legal advice, HR discipline, or requests to fabricate blame.
---

# Issue Analyse

## Purpose

Guide customer issue discussions toward objective support, proof-backed responsibility boundaries, and a usable solution path.

The skill is for issue analysis where the final outcome should support the customer or stakeholder while preventing the user from accepting responsibility that is not supported by POR, SOP, Email, QC, Policy, handoff, release, waiver, and proof strength. The normal end state is not "win an argument"; it is a win-win support position: clarify what is proven, what is not proven, who owns which action, and what solution can be safely offered externally.

The skill first challenges whether the complaint or feedback actually proves a problem, then restores the factual scene, then checks contract and evidence boundaries, then decides whether the case is a delivery issue, then selects a breakthrough / support strategy, and only then assigns attribution and communication wording. It must not fabricate proof, personalize blame, force a conclusion that the available facts do not support, or use "customer support" as a reason to accept unfounded responsibility.

Default operating discipline: do not accept `改代码`, `查 Bug`, or `我方先背锅` as the first move just because someone raised an issue. Also do not dismiss the customer. First preserve the support stance, then run complaint challenge, scene reconstruction, contract/evidence review, delivery-issue review, and only then select the strategy for solution, escalation, or communication.

Default output should use Chinese labels. Use Chinese wording for user-facing fields such as `客户支持目标`, `证据`, `待补证据`, `结论把握度`, `合同边界`, `交付问题`, `归因类型`, `对外解决方案`, and `双赢路径`. Keep English only for technical or workplace terms that are clearer as terms, such as `Owner`, `RACI`, `baseline`, `waiver`, `special handle`, `scope drift`, `release gate`, `ticket`, `commit`, and `checklist`.

## Core Workflow

### 1. 问题提出质疑门

Start by challenging the complaint, feedback, or alleged issue itself. Do not assume that a complaint means an issue exists.

Attack the alleged issue from these angles first:

- 提出源头: who raised the problem, what exactly they saw, and what they compared against;
- 问题真实性: whether the observation is reproducible, current, complete, and supported by primary proof;
- 过去是否存在: whether old releases, old upstream files, old templates, or legacy projects already had the same behavior;
- 现在是否存在: whether the current released product, current upstream, and current runtime still show the same behavior;
- 相关项目是否存在: whether sibling projects, copied baselines, reference projects, or peer versions show the same behavior;
- 评价基准: whether the complaint is based on POR, SOP, Email, QC, Policy, old baseline, current upstream, customer expectation, or changed scope;
- 实质影响: whether the difference materially affects the agreed deliverable or is only a preference, enhancement, late change, duplicate, stale report, or unproven assumption.

If the alleged issue is not proven, classify it as `问题尚未成立`, not as another party's fault. If the challenge cannot be completed because proof is missing, output a concise `问题提出质疑` response with:

- `被提出的问题`;
- `质疑点`;
- `已知证据`;
- `待补证据`;
- `暂定判断`;
- `下一步最小追问`.

When the case involves customer complaints, legacy behavior, copied baselines, historical acceptance, special handling, or related-project comparison, read `references/investigation-methods.md` before giving a firm answer.

### 2. 现场还原门

After challenging the complaint, restore the scene before judging responsibility.

Capture what is known and what is still missing:

- 事件陈述: what happened according to the user;
- 当前投诉或观察: who complained, what they saw, and what they compared against;
- 已知事实: confirmed facts versus user memory;
- 关键未知: missing facts that could change the conclusion;
- 时间线: request, handoff, change, release, complaint, mitigation;
- 相关对象: product, version, file, upstream/downstream artifact, system, Owner;
- 可用证据: ticket, mail, chat, log, commit, release package, checklist, screenshot;
- 当前 contract 或 expected behavior: POR, SOP, Email, QC, Policy, API contract, SLA, ticket acceptance, handoff agreement, waiver, known limitation.

If the scene is not sufficiently reconstructed, do not directly decide issue existence or attribution. Output a concise `现场还原` response with:

- `已知事实`;
- `关键缺口`;
- `待补证据`;
- `暂定假设`;
- `下一步最小追问`.

Ask only for the smallest missing facts needed for the next decision gate. Do not demand exhaustive evidence when a narrower question can move the analysis forward.

Use `暂定假设` to preserve multiple plausible explanations, such as true defect, undefined expectation, legacy latent issue, accepted deviation, upstream baseline drift, downstream release consistency gap, requester scope drift, process / contract gap, or evidence gap. Mark each hypothesis as `待验证`, `较可能`, `已排除`, or `证据不足`.

### 3. 合同 / 证据审查门

Before deciding whether the case is a delivery issue, check the contract and evidence base. This gate protects the user from accepting undefined responsibility while keeping the customer support path concrete.

Relevant contract and evidence sources include:

- `POR`;
- `SOP`;
- `Email` or written stakeholder decision;
- `QC` record, checklist, report, or sign-off;
- `Policy`;
- handoff agreement;
- release checklist or release gate;
- waiver, known limitation, accepted deviation, or special handle;
- baseline, upstream package, related project, version, ticket, log, screenshot, commit, or official record.

For each relevant item, separate:

- `约定已定义`: what was explicitly promised;
- `约定已遵守`: whether the party followed it;
- `约定缺口`: what was undefined or ambiguous;
- `约定漂移`: whether the expectation changed after execution;
- `交接缺口`: whether required upstream input or downstream acceptance was missing;
- `证据强度`: whether proof is direct, corroborated, background-only, weak, or missing.

Do not treat a vague expectation as a violated contract. If the contract is unclear, classify the cause as `约定缺口` or `证据缺口`, and keep the customer-facing path focused on what can be checked or offered next.

### 4. 交付问题成立性审查

After complaint challenge, scene reconstruction, and contract/evidence review are sufficient, test whether the alleged issue is a delivery issue.

Analyze:

- expected behavior from POR, SOP, Email, QC, Policy, handoff, release checklist, waiver, or accepted baseline;
- actual behavior shown by current evidence;
- material impact on agreed delivery, customer use, acceptance, safety, compliance, or support obligation.

Angles that can overturn delivery-issue status include:

- no deviation from expected behavior;
- expected behavior was never defined;
- behavior falls inside accepted tolerance, SLA, SOP, or known limitation;
- impact is not material enough to qualify as an issue;
- the event is duplicate, stale, already resolved, or not reproducible;
- the complaint is based on assumption rather than proof;
- the request is a change request, preference, or enhancement, not a defect;
- the user or requester changed scope after the fact.

If delivery-issue status is not proven, classify it as `交付问题尚未成立`, not as someone else's fault. Still provide a support path: what evidence to collect, what comparison to run, what clarification to send, or what workaround can be offered.

### 5. 破局 / 支持策略选择门

Only after contract/evidence and delivery-issue status are reviewed, decide which strategy turns the case into a defensible support path. Use only strategies supported by the facts, system context, and proof strength.

| 方法 | 使用场景 | 最小动作 | 对客户 support 的目标 | 风险边界 |
| --- | --- | --- | --- | --- |
| `冲突扩大法` | A single alleged issue traps the user in local self-defense or premature responsibility acceptance. | Temporarily assume the reported logic is true, then deduce what other modules, releases, sibling projects, or upstream/downstream steps should also be affected. | Move the discussion from single-point blame to consistent scope checking and shared evidence. | Requires real system architecture context. Do not invent affected areas or imply the customer is wrong. |
| `底层溯源法` | The case is stuck on a surface symptom, inherited judgment, or unclear defect standard. | Trace the judgment baseline back to POR, SOP, Email, QC, Policy, contract, interface rule, acceptance criterion, or system invariant. | Identify the correct standard so the customer receives a reliable answer, not a guess. | Stop when the next "why" becomes unsupported speculation or philosophical arguing. |
| `归因防御策略` | A mature, stable system is blamed after a sudden alarm or new failure. | Treat new external variables, upstream changes, abnormal inputs, environment shifts, and release/control changes as first-class hypotheses while listing self-side stability evidence. | Protect the user from unfounded ownership while still finding the actionable cause. | This is not blame shifting. It applies only when the user's system is well understood and has stability evidence. |
| `困境转化法` | The case is a corner / edge / special case that exceeds one module or one person's handling boundary. | Reframe it as a system-evolution, design-boundary, or process-gap issue; propose cross-owner review with fix owner, root-cause owner, prevention owner, and customer-support owner separated. | Produce a win-win action plan: support now, clarify ownership, prevent recurrence. | Do not escalate before showing why the issue exceeds a local action boundary. |

Recommended mapping:

- If the issue is newly raised and unproven after basic challenge, use `冲突扩大法` as a consistency check, not as a customer rebuttal.
- If the delivery issue depends on an unclear standard, use `底层溯源法`.
- If a long-running mature system is suddenly blamed, use `归因防御策略` with monitoring, regression, and input evidence.
- If the case is valid but cross-boundary, use `困境转化法` to create a win-win review and action plan.

### 6. 归因与沟通

Build a full proof chain before attribution. Use latest available proof when timing matters. If current facts may have changed, verify from the latest local artifact, system record, ticket, log, message, source file, or live source before making a firm claim.

Classify proof strength:

- `直接证据`: logs, commits, tickets, timestamps, tests, screenshots, official records, written requirements;
- `相互印证`: multiple independent signals pointing the same way;
- `背景证据`: background that explains plausibility but does not prove cause;
- `弱证据`: memory, hearsay, single ambiguous observation, inferred intent;
- `缺失`: needed but unavailable.

Every attribution must cite proof. If proof is weak, say so and lower `结论把握度`.

Classify contributing factors without collapsing everything into one blame target:

| 归因类型 | Meaning |
| --- | --- |
| `我方责任` | The user's side violated a defined contract, missed a required step, or introduced the defect. |
| `其他 Owner 责任` | Another person/team/system Owner violated a defined contract or failed a required handoff. |
| `上游依赖` | Required upstream data, API, environment, permission, timing, or decision was missing or wrong. |
| `流程 / 约定缺口` | The issue came from undefined scope, ambiguous acceptance, missing Owner, or missing review gate. |
| `环境 / 外部因素` | Tooling, network, third-party service, policy, market, or runtime condition caused or materially contributed. |
| `需求方 / 范围漂移` | The requester changed expectations after execution or judged against a requirement not agreed earlier. |
| `证据缺口` | The cause cannot be safely assigned from available proof. |

Use RACI when useful:

- `Responsible`: who executed the task;
- `Accountable`: who owned final acceptance or decision;
- `Consulted`: who had required input;
- `Informed`: who needed notification only.

Distinguish ownership of the event from ownership of the fix. A party may own remediation without being the root cause.

Use 5 Whys only while proof supports each step.

Allow multiple contributing causes. Stop the chain when the next step becomes speculation. Mark unverified links as `待补证据`.

Do not overfit to the user's preferred conclusion. If the strongest proof points back to the user's side, state that directly and suggest a safer communication route.

Produce wording that is objective and usable.

Always separate:

- `可说`: supported by proof and contract;
- `不应说`: unsupported, personal, speculative, or accusatory;
- `待补证据`: exact missing proof;
- `稳妥表达`: neutral wording that preserves credibility;
- `对外解决方案`: what can be offered to the customer or stakeholder now;
- `双赢路径`: how to support the customer while protecting the user's responsibility boundary.

Prefer statements about facts, contract, handoff, proof, support action, and next owner. Avoid statements about motive, competence, laziness, customer fault, or character.

## Output Contract

Read `references/output-template.md` for the required report format.

When the issue is sensitive, political, customer-facing, or likely to be forwarded, also read `references/communication-boundary.md`.

When attribution is complex or disputed, read `references/attribution-rubric.md` before assigning `结论把握度`.

When the issue requires deeper issue-reconstruction or breakthrough methods, such as legacy issues, historical acceptance, baseline drift, dependency expectations, complaint validity challenges, conflict expansion, root-baseline tracing, mature-system attribution defense, or corner-case transformation, read `references/investigation-methods.md`.

## Hard Boundaries

- Do not fabricate proof, quotes, logs, tickets, dates, contracts, owners, or intent.
- Do not help falsely assign known self-side responsibility to others.
- Do not output personal attacks or defamatory claims.
- Do not convert weak proof into firm blame.
- Do not use `归因防御策略` as unsupported blame shifting; it must be paired with self-side stability evidence and external-variable proof requests.
- Do not use `冲突扩大法` to manufacture hypothetical failures; only derive impacts that logically follow from the other party's stated premise.
- Do not give legal or HR disciplinary advice; provide evidence-organization and communication-risk framing only.
- Do not claim an issue is closed unless the complaint challenge, scene reconstruction, contract/evidence review, delivery-issue status, support strategy, attribution, customer-facing solution, and conclusion certainty are all explicit.
