# Question Ledger Contract

## Purpose

Ask the user about decisions that change promotion, scope, special-case handling, subtype boundaries, extraction capability boundaries, or regression behavior.

## Fields

```json
{
  "question_id": "Q-YYYYMMDD-001",
  "claim_ids": ["C-..."],
  "reason": "contradiction|scope_boundary|special_case|missing_schema|subtype_drift|capability_boundary|high_impact_unknown",
  "affected_fields": ["status", "scope", "coverage_denominator", "applies_when", "does_not_apply_when", "regression_cases"],
  "user_question": "...",
  "options": ["approve_general", "scope_contextual", "mark_special_case", "project_overlay", "subtype_overlay", "cannot_infer", "reject", "answer_freeform"],
  "evidence_summary": "...",
  "answer_capture": "user_confirmed_rule|rejected_assumption|scope_guard|cannot_infer|open_question",
  "blocking_promotion": true,
  "status": "open|answered|deferred|closed",
  "created_at": "ISO-8601",
  "answered_at": null
}
```

## Priority

```text
priority =
  user_impact_if_wrong
  * contradiction_severity
  * affected_claim_count
  * represented_file_count
  / expected_user_effort
```

## Rules

- Ask high-impact questions even if there are many. User confirmation load is acceptable when it prevents false generalization.
- Do not ask low-impact uncertainty.
- Prefer grouped questions over one question per file.
- Include evidence summary, not raw bulk corpus text.
- Every answered question must point to impacted claims and regression cases.
- Questions about `Cannot infer` boundaries are first-class questions, not optional notes.
- Deduplicate questions by claim ids plus affected fields. Do not ask the same scope decision repeatedly.
- Stop asking when the answer would not change lane, scope, regression, or final intelligence wording.
- User answers must be captured as a limited-scope supervised signal, not automatically upgraded to whole-domain truth.
