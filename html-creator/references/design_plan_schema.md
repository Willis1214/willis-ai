# Design Plan Schema

Build this plan after the content model and before HTML implementation. It is the bridge between evidence and visual output.

```yaml
mode: document | canvas
archetype: decision-brief | requirements-prd | research-report | status-report | review-risk
visual_direction: editorial-evidence | technical-blueprint | data-newsroom | quiet-minimal
visual_thesis: "mood + density + dominant composition"
reading_path: [conclusion, evidence, risk, action]
focal_point: "the first thing the reader should see"
layout_pattern: "one canonical layout from layout_atlas.md"
supporting_patterns: []
components:
  - name: decision-banner
    purpose: "why this component exists"
    required_data: [recommendation, confidence, next_action]
data_rules:
  - "quadrant requires defined x and y axes"
responsive_strategy: "document reflow or canvas summary-first fallback"
print_strategy: "preserve claim, proof, labels, and sources"
anti_patterns: [card-wall, decorative-chart, unsupported-metric]
```

## Planning Rules

1. `mode` is chosen from the reader's job, not from visual novelty.
2. `archetype` remains the content contract; `layout_pattern` is the presentation choice.
3. The first component should expose the main conclusion, question, or visual claim.
4. `supporting_patterns` contains zero to two patterns; do not let secondary patterns compete with the primary layout.
5. Every analytical component must name the data or relationship that justifies it.
6. `canvas` keeps one dominant claim and one primary proof object.
7. Missing or weak evidence is shown as `assumption`, `TBD`, or `unknown`; it is never filled by decorative numbers.
8. The plan may be kept as a temporary implementation note, but the final HTML must remain self-contained.
