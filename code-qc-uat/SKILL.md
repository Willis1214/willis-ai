---
name: code-qc-uat
description: Run executable code QC/UAT for Python, Perl, Tcl, Shell, and similar scripts or repositories by discovering the entrypoint and I/O contract, building functional scenarios plus boundary and regression cases, creating temporary test runners under qc_uat/, executing the target program, and issuing an evidence-backed Pass/Fail/Reject gate. Use when users ask for QC, UAT, functional validation, boundary testing, regression checks, crash hunting, or release gating of runnable code. Do not use for pure static code review, document review, or non-code artifacts.
---

# Code-QC-UAT

## Mission

Validate runnable code against its intended behavior before release.

Focus first on functional correctness, common usage scenarios, input/output contract stability, and boundary conditions. Keep adversarial inputs as robustness probes, not as the main purpose.

## Hard Boundaries

- Target code is Python, Perl, Tcl, Shell, or similar runnable source code, scripts, CLI tools, parsers, converters, data processors, or repositories.
- Do not modify source code during QC unless the user explicitly asks for fixes.
- Temporary test scripts, generated cases, logs, reports, manifests, and all other QC/UAT artifacts must live under the target workspace `qc_uat/` directory.
- Do not write QC artifacts to root, `temp/`, `output/`, or scattered side paths unless the user explicitly overrides this skill.
- Prefer deterministic executable runners over one-off terminal checks.
- Do not claim `Pass` unless the core functional and boundary checks were actually executed against the real target path.

## Execution Contract

1. Run `scripts/scaffold_qc_uat.py` from this skill to create or refresh `qc_uat/`.
2. Resolve the target entrypoint, language, runtime command, required inputs, expected outputs, and existing tests.
3. Build or update `qc_uat/plan/check_list.md` with:
   - functional golden-path scenarios
   - common user/workflow scenarios
   - boundary and malformed input cases
   - regression probes for changed modules or known defects
   - execution commands, expected signals, and timeouts
4. Run `scripts/generate_synthetic_cases.py` to create reusable case files under `qc_uat/testcases/`.
5. Create runnable QC scripts only under `qc_uat/engineer/` and execute them against the real target program.
6. Save command output, failures, payloads, and manifests under `qc_uat/logs/`.
7. Write the final report to `qc_uat/qc_uat_result.md`.

## Workflow

### 1) Target Discovery

- Detect language from files and shebangs: `.py`, `.pl`, `.pm`, `.tcl`, `.sh`, or project config.
- Identify the executable entrypoint: CLI script, module command, main function, test command, or documented run command.
- If the entrypoint or expected behavior is ambiguous enough to change the test design, ask the user before running QC.
- Reuse existing test commands when they are relevant, but add focused QC runners when existing tests do not cover the requested validation.

### 2) Functional Scenario QC

Build at least one case in each applicable class:

- Golden path: valid minimal input, valid typical input, valid larger input.
- Workflow path: realistic sequence of actions or files a user would run.
- I/O contract: output file presence, schema/columns/keys, exit code, stdout/stderr expectations.
- Error handling: missing file, empty input, invalid option, unsupported format.
- Regression: previously failing input, recently changed function, or user-reported risk.

### 3) Boundary And Robustness QC

Add cases only when relevant to the program contract:

- Empty, null, missing field, wrong type, invalid enum.
- Min/max numeric, oversized string/list/file, deeply nested data.
- Invalid path, missing permissions, unicode filename/content, invalid encoding.
- Repeated execution, same output path reused, simple burst loop for state leakage.
- Injection-style probes only for programs that consume commands, SQL, file paths, templates, or external input.

### 4) Language Focus

- Python: CLI args, import side effects, path handling, encoding, JSON/CSV parsing, exception handling, dependency availability, mutable defaults when behavior-visible.
- Perl: `use strict` / `use warnings`, lexical scoping, filehandle handling, regex brittleness, two-arg `open`, backticks/system use, context-sensitive return behavior.
- Tcl: quoting/substitution, list vs string confusion, `eval`/`exec`, global mutation, return-code handling, path normalization, brace usage.
- Shell: quoting, word splitting, globbing, pipeline status, temp file races, unsafe `rm`/`mv`, POSIX vs bash/zsh assumptions.

### 5) Gate Decision

- `Pass`: all executed core functional, boundary, and regression checks pass; no release-blocking evidence remains.
- `Fail`: QC executed and found functional, contract, crash, data-loss, or security-smoke blockers.
- `Reject`: QC cannot produce a reliable result because entrypoint, expected behavior, required data, or runtime prerequisites are insufficient.

If critical failures exist, stop optimization and report blocker evidence first. Post-fix cleanup ideas are secondary and must not dilute the gate result.

## Final Report Format

Write `qc_uat/qc_uat_result.md` with this structure:

```markdown
# QC/UAT Result

## Status
**[Pass / Fail / Reject]**

## Executive Summary
* **Target**: [path / entrypoint]
* **Language**: [Python / Perl / Tcl / Shell / Mixed]
* **Tests Executed**: [Count]
* **Tests Passed**: [Count]
* **Coverage**: [High / Medium / Low]

## Command Matrix
| Command | Purpose | Result | Evidence |
| --- | --- | --- | --- |

## Functional Scenarios
| Scenario | Input | Expected | Observed | Result |
| --- | --- | --- | --- | --- |

## Boundary And Regression Cases
| Case | Payload / File | Expected | Observed | Result |
| --- | --- | --- | --- | --- |

## Blockers
1. [Failure] - [Exact command and evidence path]

## Non-Blocking Findings
* [Finding] - [Risk / suggested follow-up]

## Artifact Index
* Plan: `qc_uat/plan/check_list.md`
* Testcases: `qc_uat/testcases/`
* Runners: `qc_uat/engineer/`
* Logs: `qc_uat/logs/`
```

## Bundled Resources

- `scripts/scaffold_qc_uat.py`: create the `qc_uat/` workspace and checklist template.
- `scripts/generate_synthetic_cases.py`: generate reusable functional, boundary, dirty, and regression seed cases under `qc_uat/testcases/`.
- `references/qc-scenario-patterns.md`: scenario catalog for code functional QC/UAT.
