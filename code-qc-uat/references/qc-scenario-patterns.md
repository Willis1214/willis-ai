# QC/UAT Scenario Pattern Catalog

Use this catalog to design executable QC/UAT cases for code programs. Select only cases that match the target program contract.

## 1. Functional Golden Paths

- Minimal valid input that should complete successfully.
- Typical valid input that represents real usage.
- Valid input with multiple rows/items/files.
- Valid unicode content when the program claims text support.
- Re-run with the same valid input to check deterministic output.

## 2. Workflow Scenarios

- CLI invocation with documented required arguments.
- Input file to output file conversion.
- Multiple input files or batch mode.
- Existing output path handling.
- User-facing stdout/stderr and exit-code behavior.

## 3. I/O Contract Checks

- Output file exists at the documented path.
- Output format is parseable: JSON, CSV, text, GDS-like text, config, report.
- Required columns, keys, sections, or markers are present.
- No silent truncation, dropped records, or unexpected encoding changes.
- Failure cases return non-zero or explicit error text when the contract requires it.

## 4. Boundary Inputs

- Empty file or empty stdin.
- Missing required argument or field.
- Wrong primitive type or malformed record.
- Min/max numeric values.
- Very long string, large row count, or large file within reasonable local limits.
- Deeply nested JSON/list structures when the parser accepts structured input.

## 5. Path And Encoding Cases

- Missing input file.
- Output directory missing or unwritable when safe to simulate.
- Relative path, absolute path, and path containing spaces.
- Unicode filename and unicode content.
- Invalid or mixed encoding when the program claims robust text handling.

## 6. Regression Probes

- Reproduce the user-reported bug before judging the fix.
- Exercise recently changed modules or branches.
- Keep failing payloads unchanged unless the case itself is invalid.
- Add the exact command and payload to `qc_uat/logs/`.

## 7. Language-Specific Risk Probes

- Python: import side effects, broad exception swallowing, JSON/CSV parse edge cases, path handling, subprocess command construction.
- Perl: two-arg `open`, backticks/system, implicit globals, regex overmatching, context-dependent return values.
- Tcl: quoting/substitution, list-vs-string, `eval`/`exec`, global state, return code handling.
- Shell: unquoted variables, glob expansion, pipeline failures, unsafe temp files, bashism under `/bin/sh`.

## 8. Reporting Rules

- Record exact command, payload path, expected result, observed result, and evidence path for every blocker.
- Separate observed evidence from inferred risk.
- Mark final decision only as `Pass`, `Fail`, or `Reject`.
- The final report and every artifact must stay under `qc_uat/`.
