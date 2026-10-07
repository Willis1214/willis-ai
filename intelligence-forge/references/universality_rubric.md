# Universality Rubric

## Claim Status

| Status | Rule |
| --- | --- |
| `hypothesis` | Extracted from evidence but not validated. |
| `candidate` | Supported by evidence but pending coverage/counterexample checks. |
| `validated_general` | Holds across relevant strata and survives counterexample, feedback, and regression checks. |
| `contextual` | True only under an explicit scope guard. |
| `special_case` | True in a narrow or isolated case; requires preservation reason or user decision. |
| `contradicted` | Counterexamples invalidate the general claim. |
| `unknown` | Evidence is insufficient or ambiguous. |
| `rejected` | User or validation rejected the claim. |

## Atomic Claim Shape

Every claim should be falsifiable and scoped:

```json
{
  "claim_id": "C-...",
  "type": "architecture|invariant|workflow|naming|dependency|exception|anti-pattern",
  "source_class": "public_prior|file_observed_fact|user_confirmed_rule|unresolved_hypothesis|rejected_assumption",
  "status": "hypothesis|candidate|validated_general|contextual|special_case|contradicted|unknown|rejected",
  "scope": "domain core|subtype overlay|project overlay|local exception|unknown",
  "coverage_denominator": "all included files|subtype:...|project:...|section:...",
  "applies_when": [],
  "does_not_apply_when": [],
  "supporting_files": [],
  "contradicting_files": [],
  "source_evidence": [],
  "counterexample_ids": [],
  "confidence": 0.0,
  "last_checked": "ISO-8601",
  "regression_cases": []
}
```

## Universality Score

The score is a promotion signal, not a truth probability.

```text
support_breadth
+ strata_coverage
+ counterexample_absence
+ scope_clarity
+ regression_stability
- contradiction_severity
- untested_relevance
- extraction_uncertainty
```

## Promotion Rules

- `validated_general` requires support across relevant strata, no unresolved high-relevance contradiction, and passing regression cases.
- `domain_core` and `validated_general` require the promotion gate matrix. If the gate fails, demote to the narrowest useful lane instead of deleting the claim.
- `contextual` requires an explicit scope guard.
- `special_case` requires a preservation reason or user confirmation.
- `unknown` is acceptable output and must not be rewritten as confident prose.
- `rejected` remains blocked by regression unless reopened explicitly.
- `public_prior` cannot become `validated_general` without file evidence or explicit user confirmation.
- A claim with unresolved subtype/schema drift cannot be wider than the drift boundary.
- A claim without `applies_when` and `does_not_apply_when` is not ready for reuse as an AI domain constraint.
- `domain_core` is not the only valuable output. `project_overlay`, `subtype_overlay`, `contextual`, and `special_case` claims should remain in the intelligence file when they help future reasoning.

## Promotion Matrix Reference

Use `promotion_gate_matrix.md` for lane-specific gates.

Key principle:

```text
block over-promotion; preserve under-proven knowledge.
```
