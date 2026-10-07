# Skill Cleaner

## English

Skill Cleaner is a Codex skill for auditing local Codex/OpenClaw skill installations.

It scans skill roots, prompt-budget pressure, long descriptions, duplicate or near-duplicate skills, and recent usage evidence, then produces Chinese-first cleanup recommendations. It is read-only by default: it reports what should be reviewed before any deletion, disabling, renaming, or rewriting happens.

### What It Does

- Audits loaded and local Codex/OpenClaw skill roots.
- Estimates prompt-budget pressure from skill descriptions.
- Finds long-description candidates that may be compacted.
- Detects duplicate skill names and near-identical skill copies.
- Identifies possibly unused skills from recent history and session evidence.
- Produces a Chinese audit report under the current workspace `output/` directory.

### When To Use It

Use this skill when you need to:

- trim skill prompt budget
- audit too many loaded skills
- find duplicate or stale skill copies
- review unused-skill candidates
- decide which skills or plugin copies may need cleanup
- prepare a human review before changing local skill folders

### When Not To Use It

Do not use this skill to automatically delete, disable, rename, or rewrite skills. Cleanup actions require a separate explicit user confirmation with target paths, backup plan, impact scope, and rollback method.

### Installation

Install from this repository branch:

```bash
npx skills add https://github.com/Willis1214/Skills/tree/Skill-Cleaner-Skill --skill skill-cleaner
```

Or copy `skill-cleaner/` into your Codex skills directory.

### Usage Prompt

```text
Use $skill-cleaner to audit my local Codex skills and produce a Chinese cleanup report.
```

### Repository Contents

- `skill-cleaner/SKILL.md`: skill instructions, workflow, boundaries, report contract, and analyzer notes.
- `skill-cleaner/agents/openai.yaml`: Codex app display metadata.
- `skill-cleaner/scripts/skill-cleaner-cn.mjs`: Chinese report wrapper.
- `skill-cleaner/scripts/skill-cleaner.ts`: read-only skill analyzer.
- `manifest.json`: public release metadata.
- `REVISION_HISTORY.md`: release history.

### Release Notes

#### v1.0.0 - 2026-06-24

- Initial central `Willis1214/Skills` release.
- Publishes the installable `skill-cleaner` folder with analyzer scripts and Codex app metadata.
- Keeps the default workflow read-only and Chinese-first.
- Requires explicit confirmation before any destructive cleanup action.

### Safety and Boundaries

- The default workflow only generates reports and suggestions.
- The skill must not delete, disable, rename, or rewrite existing skills without separate explicit confirmation.
- Raw analyzer output may be kept in `temp/`; final user-facing reports should be written to `output/`.
- No GitHub repository, external service, or credential is required for normal audit runs.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Skill Cleaner 是一个用于审计本地 Codex/OpenClaw skills 的 Codex skill。

它会扫描 skill 根目录、prompt budget 压力、长 description、重复或近似重复的 skill，以及近期使用痕迹，然后输出中文清理建议。默认只读，不会自动删除、禁用、重命名或改写任何 skill。

### 它做什么

- 审计本地 Codex/OpenClaw skill 根目录。
- 估算 skill description 带来的 prompt budget 压力。
- 找出可压缩的长 description 候选。
- 检查同名 skill 和近似重复 skill。
- 根据近期 history/session 证据识别疑似未使用 skill。
- 在当前工作区 `output/` 下生成中文审计报告。

### 什么时候使用

适用于：

- skill 数量过多，需要降低 prompt budget 压力
- 需要检查重复 skill 或旧 skill 副本
- 需要识别疑似未使用 skill
- 需要判断哪些 skill、plugin copy 或本地副本值得清理
- 清理前需要先出一份人工 review 报告

### 什么时候不使用

不要用它直接自动删除、禁用、重命名或改写 skill。任何清理动作都需要用户单独确认目标路径、备份方案、影响范围和回滚方式。

### 安装

从本仓库分支安装：

```bash
npx skills add https://github.com/Willis1214/Skills/tree/Skill-Cleaner-Skill --skill skill-cleaner
```

也可以把 `skill-cleaner/` 复制到本地 Codex skills 目录。

### 使用 Prompt

```text
Use $skill-cleaner to audit my local Codex skills and produce a Chinese cleanup report.
```

### 仓库内容

- `skill-cleaner/SKILL.md`: skill 指令、workflow、边界、报告合同和 analyzer notes。
- `skill-cleaner/agents/openai.yaml`: Codex app 展示 metadata。
- `skill-cleaner/scripts/skill-cleaner-cn.mjs`: 中文报告 wrapper。
- `skill-cleaner/scripts/skill-cleaner.ts`: 只读 analyzer。
- `manifest.json`: 公开 release metadata。
- `REVISION_HISTORY.md`: 发布历史。

### Release Notes

#### v1.0.0 - 2026-06-24

- 首次发布到中央 `Willis1214/Skills` 仓库。
- 发布可安装的 `skill-cleaner` 目录，包含 analyzer 脚本和 Codex app metadata。
- 保持默认工作流只读、中文优先。
- 任何破坏式清理动作前都必须单独获得用户确认。

### 安全与边界

- 默认工作流只生成报告和建议。
- 未经单独明确确认，不得删除、禁用、重命名或改写任何现有 skill。
- 原始 analyzer 输出可以保存在 `temp/`；最终用户报告应写入 `output/`。
- 正常审计运行不需要 GitHub 仓库、外部服务或凭证。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
