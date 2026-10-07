# Artifact Contract

## Run Directory

```text
output/domain_knowledge/<domain_id>/<run_id>/
  domain_onboarding.md
  public_research_notes.md
  draft_cognition.md
  prior_contamination_audit.md
  domain_profile.yaml
  corpus_manifest.jsonl
  file_profiles.jsonl
  strata_candidates.csv
  cluster_map.json
  sampling_plan.csv
  deep_read_queue.csv
  coverage_matrix.csv
  observations.jsonl
  candidate_knowledge.jsonl
  evidence_index.jsonl
  claim_search_results.jsonl
  blind_validation.jsonl
  universality_matrix.csv
  promotion_gate_matrix.csv
  overlay_scope_map.md
  counterexample_ledger.md
  question_ledger.md
  user_feedback_casebook.jsonl
  regression_eval.jsonl
  iteration_report.md
  domain_intelligence.md
```

## Rule

Do not promote knowledge unless its supporting artifacts can be read back from the run directory.

## Domain Intelligence File

`domain_intelligence.md` is the primary final artifact.

Required sections:

- `Purpose and audience`
- `Source boundaries`
- `Domain core`
- `Subtype or project overlays`
- `File architecture`
- `Reusable constraints`
- `Contextual rules`
- `Special cases`
- `Rejected or deprecated assumptions`
- `Open questions`
- `Cannot infer`
- `Evidence map`
- `Regression hooks`
- `Promotion gate record`
- `Sampling and uncovered strata`

Rules:

- Keep public prior separate from file-observed facts.
- Each reusable constraint must point to claim ids and evidence ids.
- Each special case needs scope and preservation reason.
- Each unresolved issue must say whether it blocks reuse, narrows scope, or is acceptable debt.
- If the final state is `partial`, `blocked`, or `unsafe_to_reuse`, write that state at the top of the file.
- The file must not hide useful non-core knowledge. Preserve overlays, contextual rules, and special cases with clear boundaries.
