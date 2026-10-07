# Revision History

## v1.1.0 - 2026-05-18

- Renamed the installable skill from the local QC/UAT lineage to `code-qc-uat`.
- Renamed the display name to `Code-QC-UAT`.
- Refocused the workflow on executable code QC/UAT for Python, Perl, Tcl, Shell, CLI tools, parsers, converters, and data-processing programs.
- Preserved lightweight robustness probes, but made functional scenarios, boundary conditions, I/O contracts, and regression checks the primary QC path.
- Allowed generated temporary QC runners to execute the real target program.
- Required every QC artifact to stay under the target workspace `qc_uat/`.
- Simplified the final report path to `qc_uat/qc_uat_result.md`.

## v1.0.0 - Local Baseline

- Original local QC/UAT workflow.
- Focused on adversarial QC/UAT, synthetic dirty/golden cases, and strict pass/fail blocker evidence.
