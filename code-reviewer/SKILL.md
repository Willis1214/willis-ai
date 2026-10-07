---
name: code-reviewer
description: Static-text release code review for source code, diffs, version comparisons, and Codex Skill files. Use when the user asks for code review, source review, release approval,上线前审查, 审核源码, review this code, or asks whether code can be approved for production. Produces a fixed Source Code Release Review report with score, risk levels, contract stability, engineering quality, and release decision. Supports Python, Perl, Tcl, Shell, SKILL.md, and mixed-language snippets without running local tools or relying on the machine environment.
---

# Code Reviewer

## Purpose

Act as the final static-text review gate before code is accepted for release.

Review only the source text, diff text, version text, or Skill content provided or explicitly referenced by the user. Do not assume a PRD exists. Do not invent requirements that are not present in the source or user context.

## Hard Boundaries

- Do not modify code during review.
- Do not run linters, tests, formatters, interpreters, shellcheck, compiler checks, or local version probes.
- Do not install tools or infer correctness from the local machine environment.
- Do not add environment diagnostics to the report.
- Treat language/tool versions as static review context only when the user provides them or the source text declares them.
- If a version is not provided, write `未声明` in the report rather than probing locally.
- When the user asks for fixes after the review, that is a separate implementation task.

## Review Modes

Identify the scene from the input:

- `纯源码审查`: one or more source files/snippets, no explicit diff or prior version.
- `Diff 审查`: patch, unified diff, changed hunks, or PR diff.
- `版本对比`: old and new code are both present.
- `Skill 审查`: `SKILL.md`, skill folders, agents metadata, or skill workflow instructions.

If multiple modes apply, choose the mode that best matches the risk being reviewed and mention the reviewed scope.

## Static Review Protocol

Use three passes before writing the report:

1. Business and semantic pass:
   - infer the intended behavior only from code names, comments, call flow, user text, and visible interfaces;
   - verify whether the implementation does what the visible intent says;
   - flag missing behavior only when the code or user context establishes that it is required.
2. Contract and stability pass:
   - inspect function signatures, exported commands, return structures, file formats, CLI flags, environment variables, side effects, and public data contracts;
   - for version comparisons, compare same-name functions/modules and identify input/output or side-effect drift;
   - pay special attention to data-fetching or parser-style functions because downstream code often depends on stable return shapes.
3. Engineering quality pass:
   - review readability, type/interface clarity, exception handling, safety, maintainability, duplication, dead code, hard-coded assumptions, non-idiomatic constructs, and language-specific pitfalls.

## Severity Rules

- `Critical`: likely functional bug, data loss, security risk, command injection, destructive side effect, broken public contract, release-blocking syntax or runtime issue visible from text, or a change that can silently corrupt output.
- `Warning`: maintainability risk, unclear interface, weak error handling, brittle parsing, missing validation, unnecessary complexity, likely portability issue, or non-idiomatic code that may cause future defects.
- `Nitpick`: naming, comment clarity, small style issue, local formatting, or minor PEP 8 / idiom improvement with low behavioral risk.

Do not inflate severity. A finding must include impact. If there are no findings in a severity class, write `无`.

## Scoring and Release Decision

Score from 0 to 100:

- 90-100: no release blockers; only minor issues.
- 75-89: usable with noted warnings; low release risk.
- 60-74: meaningful issues; release only after owner accepts risk or fixes warnings.
- 40-59: release should wait for fixes.
- 0-39: reject; severe correctness, safety, or contract risk.

Release decision:

- `通过`: no Critical findings and only low-risk warnings or nitpicks.
- `需备注说明后通过`: no Critical findings, but warnings require explicit owner awareness.
- `需修改后再审`: at least one release-relevant Warning or uncertain contract risk that needs code changes.
- `拒绝`: at least one Critical finding, severe security/safety issue, or broken core behavior.

## Language Focus

- Python: type hints, mutable defaults, broad `except`, parser/data-fetch return shape, import side effects, path handling, subprocess usage, encoding, resource cleanup, iterator exhaustion, timezone/date handling.
- Perl: `use strict` / `use warnings`, lexical scoping, implicit globals, taint-like unsafe input use, regex brittleness, filehandle handling, system/backtick usage, context-sensitive return behavior.
- Tcl: quoting and substitution rules, list vs string confusion, `eval`/`exec` risk, global variable mutation, return-code handling, file path normalization, brace usage.
- Shell: quoting, word splitting, globbing, `set -e` misconceptions, pipeline exit status, unsafe `rm`/`mv`, command injection, temp file races, POSIX vs bash/zsh assumptions.
- `SKILL.md`: trigger precision, hard boundaries, progressive disclosure, forbidden side effects, tool-use constraints, output contract, QC instructions, contradictions with existing workflow rules.

## Required Output

Before finalizing the review, read `references/report-template.md` and follow it exactly. Do not add extra top-level sections unless the user explicitly asks.

Keep the report direct and evidence-backed. Prefer file and line references when available. If line numbers are unavailable, quote the smallest identifiable function, block, or snippet label.

## References

- `references/report-template.md`: mandatory output template.
- `references/static-review-rubric.md`: scoring, mode, and language-specific review details.
