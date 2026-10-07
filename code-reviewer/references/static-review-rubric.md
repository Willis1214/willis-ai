# Static Review Rubric

## Input Handling

Review only the source text and context supplied by the user or explicitly referenced by path. If a referenced file is available locally, read only the needed files or diffs. Avoid full-repository scans unless the user asks for repository-level review.

Do not require a PRD. When no PRD is supplied, evaluate visible intent, contracts, release risk, and engineering quality only.

## Version and Tool Context

The report field `语言与工具版本` means the static target version declared by the user or visible in source text, such as shebangs, comments, `.tool-versions`, `pyproject.toml`, `package` metadata, or user-provided target runtime.

Never populate that field from the reviewing machine. If the source does not declare a version, write `未声明`.

Examples:

- `Python 3.11 declared in pyproject; ruff target-version py311`.
- `Shell: bash shebang; Bash version 未声明`.
- `Perl: version 未声明`.
- `SKILL.md: Codex skill format; tool version 未声明`.

## Findings Standard

Every finding should include:

- location: file and line when available;
- problem: what is wrong;
- impact: why it matters for release;
- fix direction: the smallest reasonable correction.

Avoid generic style comments unless they materially improve readability or maintainability.

## Contract Review Checklist

Inspect:

- function signatures and positional/keyword parameter compatibility;
- return data shape, required keys, optional keys, nullability, and type drift;
- exception behavior and swallowed failures;
- file paths, output filenames, generated artifacts, and overwrite behavior;
- CLI flags, environment variables, exit codes, stdout/stderr contracts;
- network, database, filesystem, process, or UI side effects;
- parser and data-fetching functions whose downstream consumers likely depend on stable structures.

For version comparison, explicitly say whether the contract is stable, changed safely, changed with risk, or broken.

## Release Decision Guide

Use `拒绝` only for release-blocking Critical findings.

Use `需修改后再审` when the code has no obvious catastrophic issue but the remaining risks are too concrete for release approval.

Use `需备注说明后通过` when the code can ship but known warnings should be documented by the owner.

Use `通过` when only low-risk warnings or nitpicks remain.

## Language-Specific Static Signals

### Python

- mutable default arguments;
- broad `except` or swallowed exceptions;
- unstable dict/list return structures;
- implicit encoding and timezone assumptions;
- subprocess without argument lists or input sanitization;
- unchecked file overwrite/delete;
- type hints missing on public interfaces when the codebase style expects them.

### Perl

- missing `use strict` or `use warnings`;
- unscoped globals and context-sensitive returns;
- fragile regex parsing;
- unsafe `system`, backticks, or open-pipe usage;
- unchecked filehandles and silent failures.

### Tcl

- unsafe `eval` or `exec`;
- list/string confusion;
- brittle quoting and substitution;
- global state mutation without clear ownership;
- missing return-code checks.

### Shell

- unquoted variables and word splitting;
- unsafe globbing;
- command injection;
- fragile `set -e` assumptions;
- destructive operations without guardrails;
- bash/zsh/POSIX assumptions not reflected in the shebang.

### SKILL.md

- vague trigger description;
- hidden side effects or unapproved installs;
- missing hard boundaries;
- conflict with current workspace or global governance rules;
- output template not enforced;
- excessive references or scripts for a simple instruction-only skill.
