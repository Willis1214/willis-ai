# QC Checklist Template

Use this Markdown template for `output/<project_slug>_qc_checklist.md`.

```markdown
# QC Checklist：{项目名称}

## 1. Checklist Overview

| 项目 | 内容 |
| --- | --- |
| 测试对象 | {project_name} |
| 目标版本 | {target_version_or_TBD} |
| 关联 PRD | `{project_slug}_prd.md` |
| 关联用户故事地图 | `{project_slug}_user_story_map.html` |
| Checklist 状态 | Draft / Review / Final |

## 2. Severity Rule

| Severity | Meaning | Release Impact |
| --- | --- | --- |
| Blocker | Core requirement, input/output contract, safety, or data integrity failure | Must fix before acceptance |
| Warning | Important gap or risk with workaround or explicit owner acceptance | Can pass only with owner note |
| Acceptable | Minor issue, documentation gap, or non-blocking improvement | Does not block acceptance |
| Pass | Fully satisfies the check | Accepted |

## 3. Checklist Table

| ID | Category | Check Item | Acceptance Standard | Verification Method | Evidence Required | Severity | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QC-001 | Requirement | Background and objective are explicit | PRD states why the project exists and what outcome is expected | PRD review | PRD section link / excerpt | Blocker | TBD |  |
| QC-002 | Input | Input contract is complete | All required inputs, format, source, and missing-input behavior are defined | PRD + story map review | Input table | Blocker | TBD |  |
| QC-003 | Output | Output contract is complete | Final output artifacts, fields, format, and location are defined | PRD review | Output table | Blocker | TBD |  |
| QC-004 | User Story | Main user journey is covered | Primary role, activity, task, and system response are mapped | HTML story map review | Story map section | Blocker | TBD |  |
| QC-005 | Boundary | In-scope and out-of-scope are explicit | PRD separates required behavior from non-goals and covers logical, interaction, and physical-world boundaries where applicable | PRD review | Boundary table | Blocker | TBD |  |
| QC-006 | Condition | Conditional branches are covered | Key condition triggers, behavior, feedback, QC check, logical mutual exclusion, and chain reactions are defined | HTML story map review | Condition architecture table | Warning | TBD |  |
| QC-007 | Exception | Edge cases are covered | Known failure modes, hidden sharing risk, overfitting risk, and expected handling are listed where applicable | PRD + story map review | Exception table | Warning | TBD |  |
| QC-008 | Implementation Freedom | PRD avoids unnecessary implementation prescription | Technical path is constrained only where user gave hard constraints | PRD review | Constraint table | Warning | TBD |  |
| QC-009 | Security | Permission, privacy, and data risks are covered | Sensitive data, file writes, network, and permission assumptions are stated | PRD review | Security notes | Blocker | TBD |  |
| QC-010 | Validation | Acceptance can be verified | Every key objective has a verification method and evidence requirement | Checklist review | This checklist | Blocker | TBD |  |
| QC-011 | Red Team Gate | High-risk review findings are resolved before final output | No unresolved `High` Red Team findings remain; accepted residual `Medium` / `Low` risks are visible in PRD or QC | Red Team review + remediation readback | Red Team issue table and remediation confirmation | Blocker | TBD |  |

## 4. Open QC Questions

| ID | Question | Impact | Owner Decision Needed |
| --- | --- | --- | --- |
```

## Rules

- QC should constrain outcomes, evidence, and release gates, not implementation style.
- Use `Blocker` sparingly but strictly for contract, safety, data integrity, or core user journey failures.
- Treat unresolved `High` Red Team findings as `Blocker` issues.
- Do not mark `Pass` unless evidence is available.
