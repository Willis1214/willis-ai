---
name: intelligence-forge
description: "Use when Codex needs to forge a reusable domain intelligence file from many same-domain professional files: first learn the field and file type, then extract, validate, red-team, and iteratively refine claims with evidence, coverage, counterexamples, user feedback, promotion gates, overlays, and Cannot infer boundaries. Do not use for one-file summaries, ordinary RAG answers, or notes that do not require corpus-level validation."
---

# Intelligence Forge

## Purpose

Induce reusable domain intelligence from a professional same-domain corpus with domain onboarding, evidence, coverage, user confirmation, counterexample pressure, and regression.

This skill is not a summarizer. It first builds a draft cognition of the domain and file type, then turns corpus observations into candidate claims, tests whether those claims are general, contextual, special-case, contradicted, or unknown, and only promotes stable claims after dynamic validation gates pass.

The final target is an intelligence file, not a pile of notes. The intelligence file must say what is reusable, where it applies, where it does not apply, what remains unresolved, and what the extractor cannot infer.

## Hard Rules

- Stage 0 domain onboarding comes before private corpus induction: the user explains the field and file type, then Codex researches/studies public or general domain context and drafts initial cognition for user correction.
- Public research is only prior knowledge and question-generation context; it cannot become promoted domain intelligence unless private corpus evidence or user confirmation supports it.
- Every claim must identify its source class: `public_prior`, `file_observed_fact`, `user_confirmed_rule`, `unresolved_hypothesis`, or `rejected_assumption`.
- Extraction produces hypotheses, not truth.
- No corpus file is invisible: it must be indexed, shallow-profiled, cluster-represented, queued, holdout, excluded with reason, or explicitly out of scope.
- All files must be visible; not all files must be deeply read in every iteration.
- No universality claim without coverage evidence.
- No `domain core` or `validated_general` promotion without passing the promotion gate matrix.
- No special case may be silently promoted to general.
- Do not discard weak but plausible signals. Preserve them as `candidate`, `contextual`, `special_case`, `project overlay`, `subtype overlay`, or `unknown` until evidence resolves them.
- User feedback is supervised data and must enter feedback casebook plus regression eval.
- Iteration count is dynamic. A configured minimum may exist, but no fixed count proves quality by itself; continue/stop decisions depend on coverage, contradictions, novelty, unresolved questions, regression, and budget-to-signal ratio.
- The extractor cannot certify its own claims; promotion validation needs a separate checking pass.
- Model-generated prose is not evidence.
- Cross-project differences must be represented as scope, subtype, overlay, exception, or unresolved drift; never flatten them into one general rule.
- The final intelligence must include a `Cannot infer` boundary so downstream AI models know what this corpus does not prove.
- Public-prior contamination must be audited before any claim is promoted beyond candidate/contextual status.

## Workflow

0. Run domain onboarding:
   - ask the user to explain the professional field, file type, intended intelligence target, known subtypes, and known traps;
   - research/study public or general domain context when allowed or needed;
   - draft `draft_cognition.md` with assumptions, vocabulary, likely architecture, likely file concerns, and open questions;
   - get user correction before treating the cognition as the local working frame.
1. Resolve domain profile, corpus root, sensitivity policy, extraction boundary, and final intelligence target.
2. Build a full manifest with `scripts/build_manifest.py`.
3. Build shallow profiles for every included file with `scripts/build_file_profiles.py`.
4. Detect subtype/schema drift and build strata by metadata, content, behavior, exception signals, and feedback signals.
5. Plan stratified deep-read sampling so each project/version/tool/stage/schema-drift/exception cluster is either sampled, held out, or explicitly unresolved.
6. Build/inspect strata coverage with `scripts/score_coverage.py`.
7. Extract observations and candidate claims with `scripts/extract_candidate_claims.py`.
8. Search counterexamples with `scripts/search_counterexamples.py`.
9. Plan the next deep-read wave with `scripts/plan_deep_read_queue.py`.
10. Audit public-prior influence on generated hypotheses.
11. Run blind claim checking with `scripts/blind_validate_claims.py`.
12. Validate claims with `scripts/validate_claims.py`.
13. Render high-value user questions with `scripts/render_question_ledger.py`.
14. Append user feedback with `scripts/append_feedback_case.py`.
15. Render iteration report with `scripts/render_iteration_report.py`.
16. Route each claim through the promotion gate matrix: preserve signals when evidence is promising but insufficient; promote only when the target lane passes.
17. Repeat, split, or stop by dynamic gates. More rounds are required when contradictions, schema drift, high-impact unknowns, or regression failures remain.
18. Promote into `domain_intelligence.md` only after the intelligence boundary, evidence coverage, and unresolved issues are explicit.

## When To Ask The User

Ask only if the answer changes promotion, scope, exception handling, or regression behavior.

Ask more when user answers can remove high-impact uncertainty. User confirmation load is acceptable for high-value domain boundaries, subtype decisions, and extraction capability limits.

Do not ask about low-impact ambiguity. Keep it unresolved, scoped, or deferred with reason.

## Output Contract

Each run writes artifacts under:

```text
output/domain_knowledge/<domain_id>/<run_id>/
```

The final intelligence version must distinguish:

- candidate knowledge;
- domain core;
- project or subtype overlays;
- contextual knowledge;
- special cases;
- rejected claims;
- promoted constraints;
- open questions;
- deprecated assumptions;
- extraction capability boundaries;
- `Cannot infer` limits.

The main final artifact should be:

```text
domain_intelligence.md
```

It must be backed by machine-readable artifacts and should be suitable as a domain-constraint input for another AI model.

## Red-Team Review

When using a `red-team` subagent, pass an explicit review contract. Do not rely on implicit inheritance from the installed `red-team` skill.

The prompt must include:

- review object and scope;
- output format;
- High/Medium/Low risk rules;
- evidence discipline;
- no full rewrite;
- no file modification;
- top-risk limit;
- upgrade conditions for high-stakes decisions.

## References

Read only the reference files needed for the current pass:

- `references/domain_onboarding_protocol.md`
- `references/progressive_corpus_protocol.md`
- `references/deep_read_sampling_protocol.md`
- `references/iteration_protocol.md`
- `references/universality_rubric.md`
- `references/promotion_gate_matrix.md`
- `references/prior_contamination_audit.md`
- `references/core_overlay_separation.md`
- `references/question_ledger_contract.md`
- `references/anti_hallucination_contract.md`
- `references/blind_validation_contract.md`
- `references/domain_profile_contract.md`
- `references/artifact_contract.md`
