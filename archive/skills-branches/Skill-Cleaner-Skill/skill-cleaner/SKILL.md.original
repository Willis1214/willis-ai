---
name: skill-cleaner
description: "审计 Codex/OpenClaw skills：全局 skill 根目录、重复 skill、疑似未使用 skill、prompt budget 成本、长描述压缩候选；默认只输出中文建议，不自动删除或改写。"
---

# Skill Cleaner

Use this when trimming skill prompt budget, finding duplicate skills, auditing enabled/disabled skill roots, or deciding which skills/plugins to remove.

本地适配规则：

- 最终面向用户的结论、风险、建议和报告必须使用中文。
- 默认只读扫描和建议；不得自动删除、禁用、重命名或改写任何现有 skill。
- 如果需要执行清理动作，必须先列出目标路径、保留副本、影响范围和回滚方式，并等待用户单独确认。
- 原始英文输出可保存在 `temp/` 作为证据；最终交付报告写入当前工作区 `output/`。

## Low-Cost Worker Routing

- When the task is low-risk, bounded, parallelizable, and verifiable, the main agent may delegate a sidecar subtask to the built-in `default` subagent and must request `model = "gpt-5.4-mini"` plus a self-contained task card when spawning it.
- The delegated task card must include task ID, allowed paths, forbidden actions, expected output, and verification method.
- The main agent keeps final responsibility for user-facing conclusions, file writes, external side effects, and pass/fail decisions.
- Do not use low-cost sidecar routing for finance, legal, medical, security, irreversible external actions, credential handling, publishing, or final high-stakes judgment.
- For this skill, Low-Cost Worker may inspect generated audit reports, classify duplicates, and draft deletion/compaction candidates; it must never delete, disable, rename, or edit skills.


## Workflow

1. 运行中文报告 wrapper，输出本机 skills 状态审计：

```bash
node /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner-cn.mjs \
  --months 3 \
  --out "$PWD/output/skill_cleaner_local_audit.md"
```

2. 如需保留上游原始报告，运行只读 analyzer：

```bash
node --experimental-strip-types /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner.ts --months 3
```

Useful variants:

```bash
node /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner-cn.mjs --no-logs --out "$PWD/output/skill_cleaner_no_logs.md"
node /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner-cn.mjs --months 6 --max-log-mb 800 --deep-logs --out "$PWD/output/skill_cleaner_deep_logs.md"
node /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner-cn.mjs --context-tokens 272000 --budget-percent 2 --no-logs --out "$PWD/output/skill_cleaner_budget_only.md"
node /Users/lizhendong/.codex/skills/skill-cleaner/scripts/skill-cleaner-cn.mjs --root ~/Dropbox/boxd/skills --no-logs --out "$PWD/output/skill_cleaner_extra_root.md"
```

3. Read the report in this order:
- `Skill Budget`: GPT-5.5 context size, 2% skills budget, Codex-budgeted usage, and pre-budget full-list pressure.
- `Description candidates`: long descriptions where relaxed grammar saves prompt budget.
- `Duplicates`: same skill name or near-identical description/body across Codex, plugin cache, repo siblings, and personal skill roots.
- `Unused candidates`: no recent `$skill` mention, `SKILL.md` read, or explicit skill-use trace in recent Codex/OpenClaw logs.
- `Root summary`: where skills came from and whether config marks them disabled.

4. Before deleting or editing:
- Verify the kept copy exists and is loaded.
- Prefer deleting repo-local or `agent-scripts` duplicates when Codex built-ins cover them.
- Keep repo-local OpenClaw maintainer skills when they encode repo policy or live operations.
- Preserve trigger nouns in descriptions: product, tool, action, object.

## Analyzer Notes

- The script mirrors Codex's model-visible line shape: `- name: description (file: path)`.
- It applies Codex-like frontmatter rules: YAML frontmatter only, default name from parent dir, single-line sanitized `name` and `description`.
- It follows Codex `core-skills/src/render.rs`: 2% of raw `context_window`, token cost `ceil(utf8_bytes / 4)`, then full descriptions -> equal description truncation -> omitted minimum lines.
- It reads `~/.codex/models_cache.json` for GPT-5.5 `context_window`; fallback is 272,000 tokens and 2%.
- It scans only normal Codex/plugin/repo skill roots by default. Extra folders such as Dropbox archives are included only with `--root <path>`.
- It realpath-dedupes roots, so symlinked roots such as `~/.codex/skills/agent-scripts -> ~/Projects/agent-scripts/skills` do not create false duplicates.
- For duplicate names, it reports description/body similarity and suggests deletion candidates only when bodies are near copies. Keep priority defaults to direct Codex system skills, then direct Codex skills, then plugin skills, then personal/repo copies.
- It scans `~/.codex/history.jsonl` and recent `~/.codex/sessions/**/*.jsonl` by default. Add `--deep-logs` for archived sessions and common OpenClaw/Clawd log folders.
- Usage evidence is heuristic: `$skill`, `Use $skill`, and paths like `skills/<name>/SKILL.md`.

## Output Policy

- Suggest first; edit only when the user asks.
- If asked to apply cleanup, make small grouped commits: descriptions, deletes, config disables.
- Do not delete ignored/untracked skill dirs without naming the destination or confirming they are disposable.
