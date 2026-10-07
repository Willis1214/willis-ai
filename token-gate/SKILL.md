---
name: token-gate
description: Silent pre-execution gate for detecting large avoidable token waste. Use when a user task may involve large files, many files, full-repository scans, raw logs, PDFs, CSV/JSON dumps, repeated context, large generated outputs, exhaustive documentation, OCR, or subagent-heavy workflows. Interrupt only when there is a clearly better path that preserves the user's final goal, deliverable, quality standard, and acceptance criteria.
---

# Token Gate

## Purpose

Token Gate prevents large meaningless token consumption while preserving the user's original intent.

It must remain silent by default.

It must interrupt only when the requested path is likely to waste a large amount of tokens and a better path exists that still satisfies the same final objective.

This skill must never simplify, weaken, or reinterpret the user's intent for the sake of saving tokens.

## Core Principle

High token usage is not automatically a problem.

Only avoidable, meaningless token usage is a problem.

A task may be large and expensive but still valid if the user's final goal requires completeness, auditability, full review, or full artifact generation.

## Published Positioning

Token Gate is a pre-execution decision gate for coding agents and automation agents.

It is not a summarization prompt, a compression shortcut, or a general instruction to do less work.

Its job is to prevent avoidable model-context waste before expensive work starts, while keeping the user's final goal, deliverable, quality bar, and acceptance criteria intact.

The skill is designed for global installation in agent entry rules, where it can run silently before repository scans, large-file analysis, generated-artifact delivery, OCR/PDF work, log review, or subagent-heavy execution.

## Innovation Points

- Goal-preserving interruption: the skill may pause only when the same final outcome can be reached through a better path.
- Meaningless-cost distinction: it separates necessary high token usage from avoidable token waste instead of treating all large tasks as bad.
- Four-level decision gate: high-risk detection, avoidability, equivalent alternative path, and interruption value must all pass before the user is interrupted.
- Path-constraint awareness: suggested paths, default paths, and hard constraints are treated differently, preventing silent changes to user intent.
- Deterministic preprocessing bias: mechanical extraction, indexing, filtering, sampling, and diffing are routed to tools before model context is spent.
- Silent-by-default behavior: normal tasks proceed without token-cost commentary unless a concrete intervention is justified.
- Acceptance-criteria firewall: cheaper alternatives are rejected when they weaken correctness, completeness, auditability, or requested output quality.

## Recommended Use

Use Token Gate as a global preflight skill when an agent may otherwise spend large context on work that deterministic tools can narrow first.

Recommended situations:

- Repository or multi-file analysis where indexing and targeted reads are enough.
- Large logs where error filtering, stack traces, timestamps, or tail sections can identify the relevant region.
- CSV, JSON, XML, PDF, or OCR tasks where schema, metadata, samples, or deterministic extraction should precede model review.
- Large generated outputs where writing files is better than pasting artifacts into chat.
- Repeated context, repeated analysis, or subagent-heavy workflows that need decomposition before execution.
- Review or debugging tasks where changed files, diffs, entrypoints, or failing traces should be inspected before broad reading.

## Not Recommended

Do not use Token Gate to shrink the user's goal.

Do not use it to avoid necessary work when the user explicitly requests exhaustive review, line-by-line analysis, complete documentation, compliance-grade audit, or full artifact generation.

Do not use it when the alternative path is only marginally cheaper, speculative, or less auditable.

Do not mention token cost for small tasks that can be completed directly.

## Default Behavior

Execute the user's instruction normally without mentioning token cost unless all conditions are true:

1. The final user goal can remain unchanged.
2. The requested task or path has large avoidable token waste.
3. The expensive part is unnecessary for the final goal.
4. A concrete alternative path exists.
5. The alternative path preserves output quality, completeness, and auditability.
6. The user has not explicitly forbidden path changes.
7. Interrupting the user is likely to save more cost and confusion than it creates.

If any condition is false, do not interrupt.

## Goal Preservation Rule

Before considering any interruption, identify the following internally:

- Final goal
- Required deliverable
- Required output format
- Quality standard
- Acceptance criteria
- Explicit constraints
- User-specified implementation path, if any

Do not interrupt if the alternative path changes any of these.

Do not replace the user's goal with a smaller or easier goal.

Do not reduce completeness unless the user confirms.

## Path Constraint Classification

User-specified paths are not all equal.

Classify the user's path before deciding whether to interrupt.

### 1. Suggested Path

Examples:

- "可以用 Python 做"
- "你可以先扫一下仓库"
- "大概可以全文读一下"
- "Maybe use grep or scripts"

Meaning:

The user is offering a possible method, not a hard constraint.

Behavior:

- You may choose a better path silently.
- Interrupt only if the suggested path is clearly wasteful and user confirmation is useful.

### 2. Default Path

Examples:

- "按这个方法实现"
- "先读所有文件再总结"
- "把这些文件全部分析一下"
- "把完整日志交给模型找问题"

Meaning:

The user gave an implementation path, but did not explicitly forbid alternatives.

Behavior:

- If the path has large avoidable token waste and a better path exists, interrupt and propose the better solution.
- Do not silently change major implementation paths without confirmation.

### 3. Hard Constraint

Examples:

- "必须严格按这个路径做"
- "不要换方法"
- "不要优化流程"
- "即使耗 token 也要这样做"
- "我就是要你全文逐行审阅"

Meaning:

The user explicitly requires the path.

Behavior:

- Do not interrupt for token-saving reasons.
- Follow the path unless it is unsafe, impossible, or conflicts with higher-priority instructions.
- You may still use efficient internal execution if it does not violate the required path.

## Waste Detection

Token waste may exist when the task involves one or more of the following:

### Large Input Risk

- Reading an entire repository before the real target is known.
- Reading many files when only entrypoints, changed files, or selected modules matter.
- Reading large logs when filtered errors, stack traces, tail sections, or timestamps are enough.
- Reading full CSV/JSON/XML files when schema, samples, or aggregated statistics are enough.
- OCR-processing entire PDFs when text extraction, selected pages, or metadata are enough.
- Passing large raw data directly into the model instead of preprocessing it with scripts.

### Large Output Risk

- Printing long generated files directly in chat when writing files is better.
- Rewriting an entire large file when a patch or targeted replacement is enough.
- Generating exhaustive documentation when the user only needs onboarding, review, or architecture understanding.
- Producing repeated summaries for many files with identical structure.

### Workflow Risk

- Using multiple subagents without clear decomposition.
- Re-running analysis already completed in the same task.
- Re-reading unchanged context across turns.
- Asking the model to do mechanical extraction that deterministic tools can do better.
- Using model reasoning for tasks better handled by grep, ripgrep, AST parsing, SQL, Python scripts, checksums, or metadata inspection.

## Meaningless Token Consumption

Token consumption is meaningless when it does not materially improve:

- final answer quality
- artifact correctness
- implementation reliability
- auditability
- user decision quality
- acceptance criteria satisfaction

Examples:

- Full-repository reading when file indexing is enough.
- Full-log reading when error extraction is enough.
- Full-data loading when schema and sampled rows are enough.
- Full-file rewrite when minimal diff is enough.
- Full PDF OCR when selectable text or page-level extraction is enough.
- Repeatedly pasting the same context.
- Asking multiple agents to inspect the same files without independent responsibilities.

## Not Meaningless

Do not interrupt when high token usage is necessary or justified.

Examples:

- The user explicitly requests exhaustive documentation.
- The user asks for line-by-line review.
- The task is a safety, compliance, financial, legal, or production-quality audit requiring completeness.
- The user requires all details to be preserved.
- The alternative path may miss important edge cases.
- The alternative path reduces correctness or auditability.
- The task scope is small enough to execute directly.
- There is no reliable better path.
- The token saving is speculative or marginal.
- The interruption itself would be more disruptive than helpful.

## Four-Level Gate

Use this internal gate before interrupting.

### Level 1: Is There High Token Risk?

Check whether the task includes large input, large output, or workflow risk.

If no, execute silently.

### Level 2: Is the Cost Avoidable and Meaningless?

Check whether the expensive part is unnecessary for the final goal.

If the cost is necessary, execute silently.

### Level 3: Is There a Better Equivalent Path?

Check whether there is a concrete path that:

- preserves the goal
- preserves the deliverable
- preserves output format
- preserves quality requirements
- preserves acceptance criteria
- reduces unnecessary model context
- improves or maintains reliability

If no, execute silently.

### Level 4: Is Interruption Worth It?

Check whether the benefit is meaningful enough to justify interrupting the user.

If the benefit is unclear, execute silently.

## Anti-Interruption Rules

Do not interrupt when:

1. The user did not specify an inefficient path and the task can be completed normally.
2. The task is naturally large and must be exhaustive.
3. The alternative path is only slightly cheaper.
4. The alternative path may reduce correctness, completeness, or auditability.
5. You are uncertain whether the current path is actually wasteful.
6. The task can be completed quickly without special routing.
7. The user explicitly forbids path changes.
8. The explanation required to justify the interruption would cost more attention than the saved tokens.
9. The user asked for a direct artifact and the artifact itself is the required output.
10. The current path is expensive but aligned with the user's stated acceptance criteria.

When in doubt, do not interrupt.

## Preferred Alternative Patterns

Use these patterns when they preserve the user's goal.

### Pattern 1: Index First

Use when the user asks to analyze many files or a whole repository.

Better path:

1. Build file inventory.
2. Classify files by path, extension, size, and likely relevance.
3. Identify candidate entrypoints or changed files.
4. Read only relevant files.
5. Expand scope only when evidence requires it.

Use this instead of reading every file immediately.

### Pattern 2: Metadata Before Content

Use when processing large files, PDFs, logs, CSVs, JSON files, or generated outputs.

Better path:

1. Inspect file size, type, schema, headings, timestamps, and samples.
2. Extract only relevant sections.
3. Feed summaries or snippets to the model.
4. Use deterministic tools for full extraction.

Use this instead of passing full raw content into the model.

### Pattern 3: Patch Instead of Rewrite

Use when editing large files.

Better path:

1. Locate the target region.
2. Produce a minimal patch.
3. Validate syntax or tests if available.
4. Report changed locations.

Use this instead of regenerating the full file.

### Pattern 4: Script Before Model

Use when the task is mechanical or repetitive.

Prefer deterministic tools for:

- file listing
- grep/ripgrep search
- AST parsing
- JSON/CSV/XML processing
- log filtering
- schema extraction
- checksum comparison
- copying/moving files
- repetitive formatting
- counting lines or fields

Use the model for:

- interpreting results
- designing logic
- judging tradeoffs
- writing documentation
- reviewing edge cases
- explaining conclusions

### Pattern 5: Sample Then Generalize

Use when full data review is unnecessary at the reasoning stage.

Better path:

1. Inspect representative samples.
2. Infer structure and edge cases.
3. Write deterministic full-run logic.
4. Run the logic on all data.
5. Summarize results and exceptions.

### Pattern 6: Diff First

Use when the task concerns changes, upgrades, regressions, or revisions.

Better path:

1. Inspect changed files or diffs first.
2. Identify impacted modules.
3. Expand only to dependencies.
4. Avoid full baseline re-reading unless needed.

### Pattern 7: Output to File

Use when the user needs a large artifact.

Better path:

1. Write the artifact to a file.
2. Provide a short summary in chat.
3. Avoid pasting large generated content directly into the conversation unless requested.

## Confirmation Format

If interruption is required, use this format exactly.

```markdown
当前路径可能产生明显无意义 token 消耗，建议改用更高效路径；目标不变。

| 项目 | 判断 |
|---|---|
| 原目标 | ... |
| 浪费点 | ... |
| 更优路径 | ... |
| 保持不变 | 输出目标 / 格式 / 质量要求 / 验收标准不变 |
| 可能影响 | ... |

请选择：

1. 继续原路径
2. 采用更优路径
```

Rules:

- Keep the interruption short.
- Offer only one best alternative path.
- Do not list many theoretical options.
- Do not over-explain token mechanics.
- Do not imply the user's instruction is wrong.
- Do not execute the alternative path until the user confirms.
- If the user chooses the original path, follow it.

## Examples

### Example 1: Do Not Interrupt

User:

> Fix the bug in `parser.py`.

Reason:

Small scope. No obvious token waste.

Behavior:

Execute normally.

### Example 2: Interrupt

User:

> Read every file in this repository and tell me where the CLI entrypoint is.

Reason:

The goal is to find the CLI entrypoint. Full-repository reading is unnecessary.

Better path:

Index files, inspect package metadata, search for CLI declarations, then read candidate files.

Behavior:

Interrupt and propose index-first path.

### Example 3: Do Not Interrupt

User:

> Generate a complete Markdown manual for every function in this utility library.

Reason:

Large output may be necessary because the user explicitly requested complete documentation.

Behavior:

Proceed efficiently, but do not interrupt for token-saving reasons.

### Example 4: Interrupt

User:

> Paste the entire 50,000-line log into the model and find the error.

Reason:

Full-log model reading is likely wasteful.

Better path:

Filter errors, stack traces, timestamps, and tail sections first.

Behavior:

Interrupt and propose filtered-log workflow.
