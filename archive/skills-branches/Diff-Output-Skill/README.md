# Diff Output

## English

Diff Output is a Codex skill that standardizes modification, update, and comparison summaries into a compact Markdown table.

It uses this required header:

```markdown
| Type | Content | As is | To be | Why |
| --- | --- | --- | --- | --- |
```

### What It Does

- Summarizes before/after changes in a fixed table format.
- Separates the changed object, previous state, target state, and reason.
- Supports code, documents, prompts, configuration, workflows, artifacts, and decision updates.
- Keeps implementation, testing, and code review responsibilities outside this skill.

### When To Use It

Use this skill when you need:

- modification summaries
- update summaries
- version comparisons
- before/after status reports
- "what changed" explanations
- diff-style delivery summaries

### When Not To Use It

Do not use this skill for:

- pure implementation steps before a summary is needed
- simple factual Q&A
- formal code review findings that require a findings-first format
- tasks without a meaningful before/after state

### Installation

Install from this repository:

```bash
npx skills add https://github.com/Willis1214/Diff-Output-Skill --skill diff-output
```

Or copy `diff-output/` into your Codex skills directory.

### Usage Prompt

```text
Use $diff-output to summarize the changes with Type | Content | As is | To be | Why.
```

### Repository Contents

- `diff-output/SKILL.md`: skill instructions and output contract.
- `diff-output/agents/openai.yaml`: Codex app display metadata.
- `manifest.json`: release metadata for this public skill repository.

### Release Notes

#### v1.0.0 - 2026-05-18

- Initial public release.
- Defines the required table header: `Type | Content | As is | To be | Why`.
- Adds normalized change types such as `added`, `changed`, `fixed`, `verified`, `risk`, and `decision`.
- Keeps the skill instruction-only; no scripts, assets, or external services are required.

### Safety and Boundaries

- No credentials, tokens, network calls, or local shell actions are required by this skill.
- The skill only controls output format; it does not replace implementation, tests, release review, or debugging workflows.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Diff Output 是一个 Codex skill，用于把修改、更新、比较、版本差异和前后状态总结统一输出为紧凑的 Markdown 表格。

固定表头如下：

```markdown
| Type | Content | As is | To be | Why |
| --- | --- | --- | --- | --- |
```

### 它做什么

- 用固定表格总结前后变化。
- 分离变化对象、原状态、目标状态和修改原因。
- 适用于代码、文档、prompt、配置、流程、交付物和方案决策更新。
- 不替代实现、测试、代码审查或调试流程。

### 什么时候使用

适用于：

- 修改总结
- 更新说明
- 版本对比
- 前后状态报告
- “改了什么”说明
- diff 风格交付总结

### 什么时候不使用

不适用于：

- 尚未需要总结的纯实现步骤
- 简单事实问答
- 需要 findings-first 格式的正式代码审查
- 没有明确前后状态的任务

### 安装

从本仓库安装：

```bash
npx skills add https://github.com/Willis1214/Diff-Output-Skill --skill diff-output
```

也可以把 `diff-output/` 复制到本地 Codex skills 目录。

### 使用 Prompt

```text
Use $diff-output to summarize the changes with Type | Content | As is | To be | Why.
```

### 仓库内容

- `diff-output/SKILL.md`: skill 指令和输出契约。
- `diff-output/agents/openai.yaml`: Codex app 展示 metadata。
- `manifest.json`: 公开 skill 仓库的 release metadata。

### Release Notes

#### v1.0.0 - 2026-05-18

- 首次公开发布。
- 定义固定表头：`Type | Content | As is | To be | Why`。
- 增加标准 Type，如 `added`、`changed`、`fixed`、`verified`、`risk`、`decision`。
- 保持 instruction-only，不需要脚本、资产或外部服务。

### 安全与边界

- 该 skill 不需要凭证、token、网络调用或本地 shell 操作。
- 该 skill 只约束输出格式，不替代实现、测试、上线审查或调试流程。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
