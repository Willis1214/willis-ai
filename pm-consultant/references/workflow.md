# PM Consultant Workflow

## Goal

Create a confirmed requirement package before implementation starts.

The workflow defines what the user needs, not how the model must implement it. Implementation choices remain flexible unless the user provides hard constraints.

## Step Sequence

| Step | Name | Output | Stop Condition |
| --- | --- | --- | --- |
| 1 | Requirement clarification | Confirmed requirement fields and open questions | User confirms enough context to map user stories |
| 2 | User story map | Draft story map and flow/condition model | User confirms story map direction |
| 3 | Structured confirmation | Requirement contract summary with confirmed and `TBD` items | User explicitly confirms or revises |
| 4 | QC checklist discussion | Draft QC checklist and severity rules | User confirms checklist coverage |
| 5 | Red Team review and remediation | Risk-ranked adversarial review plus remediation decisions | No unresolved `High` findings; user confirms Red Team pass |
| 6 | Final output package | PRD Markdown, user story map HTML, QC checklist Markdown | Artifacts written and validated |

## Gate Rules

- Ask for confirmation before moving to the next step.
- If the user changes a confirmed item, update downstream summaries and mark the change.
- If required information is missing, keep it as `TBD`; do not fill it with guesses.
- If the user tries to jump to implementation before the requirement package is confirmed, summarize the missing contract items first.
- If the user explicitly asks to skip a step, note the skipped step and resulting risk.
- Before final artifacts, run a Red Team gate on the confirmed requirement package, story-map direction, and QC checklist coverage.
- Treat every `High` Red Team finding as a blocker until it is addressed in the confirmed package and the user confirms the remediation.
- If a Red Team finding cannot be judged from confirmed information, keep it as `TBD` and reflect the risk in the PRD or QC checklist instead of guessing.
- `Medium` and `Low` findings may pass only when they are either incorporated, explicitly accepted by the user, or left visible as `TBD` with owner impact.

## Standard Chat Shape

For steps 1-4, keep responses short and decision-oriented:

```markdown
## 当前确认

| 项目 | 当前内容 | 状态 |
| --- | --- | --- |

## 需要讨论

| 主题 | 当前选项 | 影响 | 建议 |
| --- | --- | --- | --- |

## 下一步确认

1. ...
2. ...
3. ...
```

Use this shape flexibly, but always preserve confirmed facts, open `TBD` items, and next questions.

## Red Team Gate Shape

For step 5, review the confirmed package adversarially. Use the installed `red-team` skill's review categories and risk levels:

- boundary vulnerabilities
- omitted special cases
- hidden assumptions
- logical contradictions
- execution blockers
- risk blind spots
- optimization space
- unclear wording or unstable structure

Output:

1. A risk overview with current risk level, whether direct final output is allowed, and the core blocker.
2. A top-five issue table using `High`, `Medium`, and `Low`.
3. A remediation table for every `High` issue, showing what must change in the confirmed package.
4. A next confirmation question asking whether the strengthened package can pass the Red Team gate.

Do not proceed to final artifacts until the Red Team gate passes.

## Final Artifact Rule

Final artifacts are produced only in step 6:

- PRD: Markdown
- User story map: self-contained HTML
- QC checklist: Markdown table
