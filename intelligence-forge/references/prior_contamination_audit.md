# Prior Contamination Audit

## Purpose

Public research and draft cognition improve reading, but they can also bias extraction. Audit how public prior influenced each claim before promotion.

## Required Audit Questions

For every promotable claim:

- Did the claim originate from public prior, user brief, file observation, or user confirmation?
- Which terms, architecture labels, or categories came from public research?
- Can the claim be restated using only file-observed facts and user-confirmed rules?
- Would the claim still be proposed if the public prior were hidden?
- Are there corpus files that use different vocabulary or structure from the public prior?

## Audit Outcomes

Use one of:

- `clean`: supported by file evidence/user confirmation without public prior dependence.
- `label_only`: public prior supplied naming only; evidence supports the underlying pattern.
- `biased_hypothesis`: public prior shaped the claim and evidence is not sufficient.
- `unsupported_prior`: public prior not supported by corpus.
- `needs_user_boundary`: user must decide whether the prior applies locally.

## Promotion Rule

`domain_core` and `validated_general` require `clean` or `label_only`.

`biased_hypothesis` and `unsupported_prior` must remain `candidate`, `unknown`, or `rejected_assumption`.

## Artifact

Record `prior_contamination_audit.md` or equivalent rows with:

- claim id;
- public prior ids or notes;
- affected wording/categories;
- file evidence ids;
- audit outcome;
- required user question if any.
