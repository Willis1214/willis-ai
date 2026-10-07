# Promotion Gate Matrix

## Purpose

Promotion gates prevent false generalization while preserving early domain signals.

Failing a high lane does not delete a claim. It routes the claim to a narrower or exploratory lane.

## Promotion Lanes

| Target lane | Minimum evidence | Counterexample rule | User role | Holdout / regression | If gate fails |
| --- | --- | --- | --- | --- | --- |
| `domain_core` | File-observed or user-confirmed support across all relevant major strata, with an explicit coverage denominator. | No unresolved high-relevance counterexample. Low-relevance counterexamples must be scoped. | User confirms any ambiguous scope or domain meaning. | Must pass holdout and regression. | Demote to `subtype_overlay`, `project_overlay`, or `candidate`. |
| `validated_general` | Support across the declared denominator, not just repeated text. | No unresolved contradiction inside the denominator. | User confirmation required if claim changes downstream behavior. | Must pass blind validation and regression. | Demote to `contextual` or `candidate`. |
| `subtype_overlay` | Support inside one subtype or schema family. | Counterexamples outside subtype do not block if boundary is explicit. | User confirms subtype boundary when high impact. | Regression should protect boundary. | Keep as `candidate` or `unknown`. |
| `project_overlay` | Support inside one project, source family, version, or lifecycle stage. | Cross-project contradiction is expected and must be listed. | User confirms whether project-local behavior is valuable. | Regression should prevent accidental domain-core promotion. | Keep as `candidate` or `special_case`. |
| `contextual_rule` | Evidence supports a rule under explicit `applies_when` and `does_not_apply_when`. | Counterexamples become scope guards. | User confirmation required if scope affects final reuse. | Regression covers scope guard. | Keep as `candidate`. |
| `special_case` | Narrow evidence exists and preservation value is clear. | Counterexamples do not matter if case is explicitly isolated. | User decides preserve/reject when impact is high. | Regression prevents silent generalization. | Keep as `unknown` or `rejected_assumption`. |
| `cannot_infer` | Evidence shows the corpus does not contain the needed signal, or user confirms the inference is outside scope. | Not applicable. | User confirmation preferred for high-impact boundaries. | Regression checks future claims do not violate it. | Keep as `open_question`. |

## Hard Blockers

Block `domain_core` and `validated_general` promotion when any is true:

- source class is only `public_prior`, `unresolved_hypothesis`, or `rejected_assumption`;
- coverage denominator is missing or wider than evidence;
- unresolved high-relevance counterexample exists;
- relevant files are still marked `needs_deep_read`;
- holdout validation is missing for a high-impact claim;
- user feedback scoped, rejected, or marked the claim as special case;
- `applies_when` or `does_not_apply_when` is missing for a reusable constraint;
- subtype/schema drift is detected but the claim lacks an overlay boundary.

## Exploration Preservation

Do not collapse every blocker into rejection.

Use these fallback routes:

- contradiction across projects -> `project_overlay` or `contextual_rule`;
- weak support but no contradiction -> `candidate`;
- strong support in one subtype -> `subtype_overlay`;
- rare but important pattern -> `special_case`;
- no evidence for an inference -> `cannot_infer` or `open_question`;
- user says "sometimes" -> scoped `contextual_rule`, not rejected.

## Promotion Record

Every promoted claim must record:

- target lane;
- evidence ids;
- covered strata;
- uncovered strata;
- counterexample disposition;
- user-confirmation state;
- holdout state;
- regression cases.
