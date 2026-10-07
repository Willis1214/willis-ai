# Skill Researcher

## English

Skill Researcher is a Codex skill that acts as a research gate before creating, updating, installing, or publishing Codex skills. It checks local skills, public skill examples, GitHub candidates, and relevant methodology before any skill file is edited or any third-party skill is trusted.

## What It Does

- Interrupts substantial skill creation or update work before implementation.
- Compares local and public candidates instead of starting from a blank design.
- Summarizes reusable methods, risks, quality checks, and recommended implementation boundaries.
- Uses a fixed Chinese research-gate template so the user can confirm before edits begin.
- Keeps `skill-creator` as the implementation skill, not the research gate itself.

## When To Use

Use this skill when you need to create a new Codex skill, substantially update an existing skill, install or evaluate a third-party skill, publish a skill, or add AGENTS rules related to skill creation. It is intentionally not required for narrow metadata-only edits.

## Install

Copy the `skill-researcher/` folder from this branch into your Codex skills directory, for example `~/.codex/skills/skill-researcher/`.

## Quality Checks

This release was validated with the Codex skill quick validator, the bundled Skill Researcher structure validator, and a prompt-input visibility check for `$skill-researcher`.

## 中文

Skill Researcher 是一个 Codex Skill 创建前置研究门。它在创建、重大更新、安装、发布 Skill 或新增 Skill 创建相关 AGENTS 规则之前，先检查本地 Skill、公开 Skill、GitHub 候选和相关方法论，再输出中文研究简报并等待用户确认。

## 适用场景

- 创建新的 Codex Skill。
- 对已有 Skill 做行为级重大更新。
- 评估或安装第三方 Skill。
- 发布 Skill 到 GitHub。
- 新增与 Skill 创建流程相关的 AGENTS 规则。

## 不适用场景

- 仅修改展示名、拼写、窄范围 metadata。
- 用户明确要求跳过研究门。
- 普通代码实现、文档修订或一次性分析任务。

## 发布说明

v1.1.0 修复了 frontmatter YAML 可解析性，加入明确 `$skill-researcher` 触发措辞，并保留中文二次确认门。
