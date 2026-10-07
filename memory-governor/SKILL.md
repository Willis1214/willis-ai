---
name: memory-governor
description: Use when the conversation reveals a durable user preference, prohibition, shortcut, or workflow rule that should be proposed for long-term memory, approved by the user, and then written into ~/.codex/memories/long-term-commands.md.
---

# Memory Governor

Use this skill to govern long-term command memory. Its job is to detect high-confidence reusable rules during normal work, propose them in a fixed approval format, and write them into the long-term memory file only after explicit user approval.

## When to trigger

Trigger this skill when at least one of these conditions is true:

- The user explicitly says `记住`, `以后`, `默认按这个来`, `不要再这样`, `以后别这么做`.
- The user repeats the same correction on the same execution path at least twice in the current thread.
- A shorter path has already been validated in the current task and the user frames it as a preferred default.
- The experience is clearly reusable beyond the current single message or single artifact.

Do not trigger for one-off complaints, temporary frustrations, or task-specific details that do not generalize.

## Candidate types

- `preference`: stable user preference about how work should be done
- `prohibition`: things the user does not want done
- `shortcut`: preferred shortest-path handling for routine work
- `workflow`: reusable multi-step operating rule

## Approval gate

When a high-confidence candidate is detected, pause and present this exact structure:

```text
检测到一条可复用长期命令候选：{candidate_summary}
类型：{preference|prohibition|shortcut|workflow}
建议沉淀内容：{normalized_rule}
是否加入长期命令库？
```

Do not write anything into long-term memory until the user gives explicit approval.

Explicit approval includes clear confirmations such as:

- `加入`
- `记住这个`
- `写进去`
- `可以`
- `同意`

If the user revises the wording, use the revised wording instead of the original candidate.

## Write path

The canonical long-term memory file is:

- `~/.codex/memories/long-term-commands.md`

Use the bundled script to initialize or append entries:

```bash
python3 ~/.codex/skills/memory-governor/scripts/append_memory_entry.py --init-only
python3 ~/.codex/skills/memory-governor/scripts/append_memory_entry.py \
  --type preference \
  --source "用户明确要求以后默认走最短路径，不要为平凡任务过度封装" \
  --rule "对于平凡且低风险任务，默认优先选择最短可验证路径，避免先行过度封装。" \
  --rationale "用户将该偏好表述为长期默认做法。"
```

## Required behavior

1. Read `~/.codex/memories/long-term-commands.md` before proposing a new candidate when possible.
2. Avoid writing duplicates when an equivalent rule already exists.
3. Normalize emotional or conversational wording into a stable instruction sentence.
4. Keep the stored rule short, actionable, and reusable.
5. Preserve the original user wording in the `source` field when writing.

## Storage format

The memory file is organized into these sections:

- `preference`
- `prohibition`
- `shortcut`
- `workflow`

Each entry stores:

- `id`
- `created_at`
- `rule`
- `rationale`
- `source`

## Non-goals

- Do not silently rewrite or delete existing memory entries.
- Do not auto-promote memory entries into other skills.
- Do not treat every user correction as long-term policy.
