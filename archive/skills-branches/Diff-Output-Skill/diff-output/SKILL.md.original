---
name: diff-output
description: Use when the user asks for modifications, updates, comparisons, version differences, before/after summaries, change logs, or "what changed" results and wants a structured table. Produce a concise Markdown table with exactly these headers: Type, Content, As is, To be, Why. Do not use for pure implementation steps, simple Q&A, or code review findings unless the user asks for a diff-style output table.
---

# Diff Output

## Purpose

Standardize change, update, and comparison results into one reviewable table.

This skill controls the output shape only. It does not replace implementation, testing, release review, debugging, or project-specific logging requirements.

## When To Use

Use this skill when the user asks to summarize or compare:

- modifications or updates
- old vs new behavior
- current state vs target state
- version differences
- implementation results
- document, prompt, config, code, workflow, or asset changes
- "what changed", "diff output", "as is/to be", or similar requests

Do not use it when:

- the user only asks for code to be implemented and no summary is needed yet
- the answer is a one-line factual response
- a code-review workflow requires findings-first output
- the task has no meaningful before/after state

If another required format conflicts with this table, follow the higher-priority user or system format and include this table only when it still fits.

## Required Table

Use exactly this Markdown table header:

```markdown
| Type | Content | As is | To be | Why |
| --- | --- | --- | --- | --- |
```

Column meanings:

- `Type`: normalized change type.
- `Content`: the changed or compared object, such as file, function, section, field, config, workflow step, output artifact, or decision.
- `As is`: old state, current state, source version, or original behavior. Use `N/A` for new items.
- `To be`: new state, target state, updated version, or final behavior. Use `N/A` for removed items.
- `Why`: the reason tied to user intent, evidence, defect cause, validation result, risk, or tradeoff. Avoid vague reasons such as "optimize" without concrete impact.

## Type Values

Prefer these values:

- `added`: new item or capability
- `changed`: changed behavior, content, logic, configuration, or structure
- `removed`: deleted item or behavior
- `renamed`: name changed while identity remains the same
- `moved`: location changed while content mostly remains the same
- `fixed`: defect or mismatch corrected
- `verified`: validation performed and passed
- `blocked`: requested result could not be completed
- `risk`: unverified gap, residual risk, or known limitation
- `decision`: explicit design, scope, or tradeoff decision

Use a new `Type` only when these values would be misleading.

## Output Rules

- Keep the table compact. Merge rows that describe the same atomic change.
- Prefer concrete paths, symbols, filenames, commands, artifact names, or section titles in `Content`.
- Do not invent old state, new state, or rationale. Use `Unknown` when evidence is missing.
- When verification matters, include `verified` or `risk` rows instead of hiding validation status in prose.
- If the table needs context, write at most one short sentence before it.
- If there are no meaningful differences, output one `verified` or `decision` row explaining that no material change was found.

## Example

```markdown
| Type | Content | As is | To be | Why |
| --- | --- | --- | --- | --- |
| changed | Output summary format | Free-form prose | Fixed table with five columns | Makes change review faster and reduces missed before/after details |
| added | Validation status | Not separated from change summary | `verified` and `risk` rows show evidence status | Prevents unverified work from being reported as complete |
| decision | Skill boundary | Could be confused with code review | Output-format skill only | Keeps review, testing, and implementation responsibilities separate |
```

