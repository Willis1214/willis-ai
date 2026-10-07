# Blind Validation Contract

## Purpose

Prevent the extractor from certifying its own claims.

## Roles

- Extractor: proposes observations, candidate claims, and evidence links.
- Blind validator: receives claim records, evidence records, manifest, profiles, and coverage only.
- Main agent: resolves conflicts, asks the user, and controls promotion.

## Validator Inputs

The validator may see:

- claim id;
- claim text;
- scope guard;
- evidence records;
- support files and strata;
- counterexample records;
- regression cases.

The validator must not see:

- extractor rationale;
- broad prose conclusions;
- final report language that may bias the verdict.

## Verdicts

- `supported`
- `unsupported`
- `contradicted`
- `scope_needed`
- `insufficient_evidence`

Promotion requires a validator pass plus deterministic script validation.

## Script Contract

`scripts/blind_validate_claims.py` produces:

```text
blind_validation.jsonl
```

Each row must contain:

- `claim_id`
- `blind_verdict`
- `reasons`
- `support_files`
- `counter_files`
- `untested_files`
- `limiting_feedback`

The main validation step must block `validated_general` when the blind verdict is `unsupported`, `contradicted`, `scope_needed`, or `insufficient_evidence`.
