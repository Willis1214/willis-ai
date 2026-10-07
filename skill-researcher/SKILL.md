---
name: skill-researcher
description: Pre-creation research gate for Codex skills. Use $skill-researcher / Skill Researcher before creating, designing, installing, publishing, or substantially updating any Codex skill, global skill, reusable skill workflow, or AGENTS rule about skill creation. This skill must interrupt before skill file edits, research existing open skills and methodology from skills.sh, GitHub, local skills, and relevant docs, summarize candidate options, risks, QC strategy, and the recommended build plan in the Chinese output template, then ask for explicit user confirmation before invoking skill-creator, installing third-party skills, or editing skill files.
---

# Skill Researcher

## Purpose

Act as the mandatory research gate before Codex creates or substantially changes a skill. The output is a decision brief, not code. Do not create, edit, install, or execute skill artifacts until the user confirms the brief.

Use this skill before `skill-creator` unless the user explicitly says to skip the research gate.

## Hard Gate

When the user asks to create a new skill or make a substantial skill update:

1. Stop before file edits.
2. Research comparable open skills and local precedents.
3. Summarize the evidence, design options, risks, and recommended path.
4. Ask for explicit confirmation.
5. Proceed to `skill-creator` only after confirmation.

Do not run `npx skills add`, install third-party skills, or execute downloaded skill code during the research gate. If `npx skills find` would materially improve discovery, explain that it runs a package-manager command and ask before using it. Prefer web/GitHub search first.

Skip this gate only for narrow non-behavioral changes such as a display-name-only metadata fix, unless the user asks for research anyway.

## Research Workflow

### 1. Clarify the requested skill

Identify:

- skill objective
- expected user prompts that should trigger it
- prompts that should not trigger it
- install scope: global `~/.codex/skills/<skill-name>` or project-local
- required resources: `scripts/`, `references/`, `assets/`
- whether AGENTS entry rules are needed for reliable preflight behavior
- validation target and minimal acceptance criteria

If these are ambiguous enough to change the design, ask before proceeding.

### 2. Search candidate sources

Use targeted, low-noise discovery:

- local installed skills under `~/.codex/skills`
- current workspace notes or prior research reports when relevant
- `skills.sh` pages and leaderboard
- GitHub searches for `SKILL.md`, skill names, and domain keywords
- official or high-reputation sources first, such as `vercel-labs`, `anthropics`, `microsoft`, or project owners tied to the domain

Avoid broad repository dumps. Read only candidate summaries, `SKILL.md`, README, security/audit metadata, and minimal source files needed to judge methodology.

### 3. Verify candidate quality

Do not recommend based only on name similarity. Check:

- task fit and trigger fit
- install count or ecosystem signal
- source reputation
- GitHub stars, activity, and issue quality when available
- security audits or warnings
- whether the skill contains scripts, network calls, credential access, shell commands, or hidden install steps
- license and maintenance state when publication or reuse is likely
- whether its method can be adapted without copying unnecessary structure

Treat unknown authors, low installs, low stars, missing audits, or opaque scripts as caution signals.

### 4. Extract reusable methodology

From each useful candidate, extract only what improves the requested skill:

- trigger wording and negative triggers
- workflow sequence
- decision gates and confirmation points
- progressive-disclosure structure
- reusable scripts or references worth bundling
- QC/eval examples
- safety boundaries

Prefer borrowing method, not blindly installing or copying.

### 5. Present the interruption brief

Use this exact Chinese structure before implementation:

```text
<skill-research-gate>
目标 Skill: <name or working name>
用户目标: <one sentence>
假设: <short list>
待确认问题: <short list or none>

已检查来源:
- <source>: <why it matters>

候选对比:
| 候选 | 匹配度 | 可复用方法 | 风险 / 限制 | 采用决策 |
| --- | --- | --- | --- | --- |

推荐设计:
- 名称:
- 安装范围:
- 触发策略:
- 资源:
- 是否需要 AGENTS 规则:
- QC 策略:

实施边界:
- 要创建/更新的文件:
- 不触碰的文件:
- 第三方安装/执行: 除非单独批准，否则无

请确认: 回复 "Continue" 按推荐方案创建/更新 Skill，或提供修改意见。确认前我不会编辑 Skill 文件。
</skill-research-gate>
```

Keep the brief concise and use the Chinese field labels exactly. Put detailed notes in `output/` only if the user requested an artifact or the research is non-trivial enough to preserve.

### 6. Continue with skill creation

After confirmation:

1. Use `skill-creator`.
2. Initialize or edit the skill in the confirmed location.
3. Keep `SKILL.md` concise and put deeper methodology in `references/`.
4. Add scripts only when deterministic checks or repeated operations justify them.
5. Validate with `skill-creator/scripts/quick_validate.py`.
6. Run targeted scenario checks for trigger fit and interruption behavior.
7. If AGENTS rules changed, scan for contradictions.
8. Write final QC results to `output/`.

## Reference

For the full reproducible rubric and command patterns, read `references/skill_research_methodology.md` when designing a new skill or when candidate comparison is non-trivial.
