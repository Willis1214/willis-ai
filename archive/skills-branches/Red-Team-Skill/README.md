# Red Team

## English

Red Team is a Codex skill for strict adversarial review of plans, prompts, workflows, PRDs, proposals, decision memos, reports, and strategy documents.

It focuses on boundary conditions, omitted special cases, hidden assumptions, logical contradictions, execution blockers, risk blind spots, optimization space, and unstable wording.

### What It Does

- Reviews user-provided content from an adversarial perspective.
- Identifies where the content is not stable, accurate, complete, credible, or executable enough.
- Assigns each issue a `High`, `Medium`, or `Low` risk level.
- Produces a fixed Chinese review format with an evaluation overview and the top five improvement points.
- Preserves the user's original plan instead of rewriting it unless the user explicitly asks for a rewrite.

### When To Use It

Use this skill when you need:

- Red Team review
- adversarial critique
- attack-style plan review
- scheme, PRD, workflow, prompt, strategy, proposal, or decision review
- hidden-assumption detection
- boundary-condition and execution-risk analysis
- a strict review that avoids praise and only surfaces stability gaps

### When Not To Use It

Do not use this skill for:

- normal rewriting, polishing, summarization, or translation
- implementation work
- source-code release review
- runnable QC/UAT against real code paths
- balanced evaluation when the user did not request adversarial critique

### Installation

Install from this repository:

```bash
npx skills add https://github.com/Willis1214/Red-Team-Skill --skill red-team
```

Or copy `red-team/` into your Codex skills directory.

### Usage Prompt

```text
Use $red-team to perform an adversarial review of this plan or document.
```

### Repository Contents

- `red-team/SKILL.md`: skill instructions, trigger boundaries, review contract, risk levels, and required output format.
- `red-team/agents/openai.yaml`: Codex app display metadata.
- `manifest.json`: release metadata for this public skill repository.

### Release Notes

#### v1.0.0 - 2026-05-18

- Initial public release.
- Defines the `Red Team` display name and installable `red-team` skill name.
- Adds a strict adversarial review workflow for plans, prompts, workflows, proposals, and decision materials.
- Requires a fixed Chinese output structure with evaluation overview and top-five improvement table.
- Keeps the skill instruction-only; no scripts, assets, network calls, or external services are required.

### Safety and Boundaries

- This skill must not introduce facts not provided by the user.
- If evidence is insufficient, it must state `当前信息不足，无法判断`.
- This skill does not rewrite the original content unless explicitly requested.
- No credentials, tokens, network calls, or local shell actions are required by this skill.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Red Team 是一个 Codex skill，用于对方案、prompt、流程、PRD、提案、决策材料、报告和策略文档进行严格的攻击式审查。

它重点检查边界条件、特殊情况遗漏、隐藏假设、逻辑矛盾、执行障碍、风险盲区、优化空间和表达结构不稳的问题。

### 它做什么

- 从攻击式视角审查用户提供的内容。
- 识别内容哪里不够稳、不够准、不够完整、不够可信或不够可执行。
- 为每个问题标注 `High`、`Medium` 或 `Low` 风险等级。
- 输出固定中文审查格式，包括评估概览和风险最高的 5 项待加强点。
- 默认不重写用户原方案，除非用户明确要求重写。

### 什么时候使用

适用于：

- Red Team 审查
- 攻击式审查
- 挑刺式方案审查
- 方案、PRD、流程、prompt、策略、提案或决策材料审查
- 隐藏假设识别
- 边界条件和执行风险分析
- 需要避免寒暄和夸奖、只暴露稳定性缺口的严格审查

### 什么时候不使用

不适用于：

- 普通改写、润色、摘要或翻译
- 实现代码或执行任务
- 源码上线审查
- 针对真实代码路径的可运行 QC/UAT
- 用户没有要求攻击式视角时的平衡型评估

### 安装

从本仓库安装：

```bash
npx skills add https://github.com/Willis1214/Red-Team-Skill --skill red-team
```

也可以把 `red-team/` 复制到本地 Codex skills 目录。

### 使用 Prompt

```text
Use $red-team to perform an adversarial review of this plan or document.
```

### 仓库内容

- `red-team/SKILL.md`: skill 指令、触发边界、审查契约、风险等级和固定输出格式。
- `red-team/agents/openai.yaml`: Codex app 展示 metadata。
- `manifest.json`: 公开 skill 仓库的 release metadata。

### Release Notes

#### v1.0.0 - 2026-05-18

- 首次公开发布。
- 定义 `Red Team` 展示名和 `red-team` 安装名。
- 增加面向方案、prompt、流程、提案和决策材料的攻击式审查流程。
- 要求固定中文输出结构，包括评估概览和风险最高的 5 项待加强点表格。
- 保持 instruction-only，不需要脚本、资产、网络调用或外部服务。

### 安全与边界

- 该 skill 不得引入用户未提供的事实。
- 证据不足时必须写明 `当前信息不足，无法判断`。
- 除非用户明确要求，该 skill 不重写原内容。
- 该 skill 不需要凭证、token、网络调用或本地 shell 操作。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
