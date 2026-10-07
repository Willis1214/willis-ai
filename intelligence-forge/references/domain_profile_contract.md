# Domain Profile Contract

## Example

```yaml
domain_id: drc_runset
domain_name: DRC Runset
field_brief:
  user_summary: ""
  public_research_allowed: false
  draft_cognition_reviewed: false
  intended_intelligence_audience: "AI domain constraint"
corpus_roots: []
allowed_extensions: []
exclude_patterns: []
artifact_sensitivity: proprietary
source_classes:
  - public_prior
  - user_brief
  - file_observed_fact
  - user_confirmed_rule
  - unresolved_hypothesis
  - rejected_assumption
claim_types:
  - architecture
  - invariant
  - workflow
  - naming
  - dependency
  - exception
  - anti-pattern
strata_hints:
  metadata: []
  content: []
  behavior: []
  exception: []
  feedback: []
subtype_hypotheses: []
evidence_policy:
  raw_excerpt_allowed: false
  max_excerpt_chars: 240
promotion_policy:
  min_iterations: 1
  dynamic_stop_required: true
  require_regression_pass: true
  require_blind_validation: true
  require_prior_contamination_audit: true
  require_overlay_before_domain_core: true
  default_validated_general_min_support_files: 2
  default_domain_core_min_major_strata: 2
  allow_exploratory_candidates: true
  default_exit_states:
    - usable
    - partial
    - blocked
    - unsafe_to_reuse
intelligence_policy:
  final_artifact: domain_intelligence.md
  split_core_and_overlays: true
  require_cannot_infer_section: true
  preserve_non_core_knowledge: true
sampling_policy:
  require_sampling_plan: true
  prioritize_counterexamples: true
  preserve_rare_subtypes: true
  keep_holdout_for_promotion: true
cannot_infer:
  - "Do not infer real-world execution responsibility from files alone."
  - "Do not infer external policy or legal validity from corpus text alone."
  - "Do not infer runtime behavior unless execution evidence is present."
```

## Rule

Keep domain profile data project-local. The global skill owns the workflow, not the domain facts.

Public prior, user brief, file observations, and user-confirmed rules must remain separately labeled. Do not merge them into one evidence class.
