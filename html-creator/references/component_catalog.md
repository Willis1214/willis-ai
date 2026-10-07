# Semantic Component Catalog

Use components to express meaning, not to decorate empty space. Each component must pass the `use_when`, `avoid_when`, and `fallback` rules before implementation.

## Framing and Narrative

1. `decision-banner` — recommendation, confidence, risk, and next action; avoid for neutral summaries.
2. `lead-block` — title, subtitle, audience, and context; avoid repeating it for every section.
3. `metric-rail` — a small set of stable numeric summaries; avoid for speculative or incomparable values.
4. `status-rail` — current state, owner, severity, or readiness; avoid when status is not actionable.
5. `section-rule` — a light structural break with a clear label; avoid decorative section dividers.

## Comparison and Assessment

6. `comparison-table` — shared criteria across options; always provide a narrow-screen summary.
7. `comparison-rail` — visual before/after or option-to-option contrast; avoid when criteria are unrelated.
8. `scorecard` — explicit dimensions with a stated scoring basis; never imply unsupported precision.
9. `quadrant-matrix` — two defined axes and comparable points; do not use as a generic scatter decoration.
10. `criteria-matrix` — many-to-many mapping between requirements, options, risks, or owners.

## Flow and Time

11. `timeline` — ordered events, milestones, or evidence dates.
12. `stepper` — finite procedure with current/next/completed state.
13. `swimlane` — sequence across owners, systems, or roles.
14. `lifecycle-rail` — allowed states, transitions, retry, or release gates.
15. `journey-map` — user or reader stages with needs, friction, and actions.

## Structure, Relationship, and Data

16. `concentric-hierarchy` — nested layers, scope, or priorities; use only when nesting is real.
17. `relationship-overlap` — explicit set intersection or shared concerns.
18. `pyramid-hierarchy` — ordered levels, maturity, funnel, or argument structure.
19. `architecture-map` — grouped nodes, ownership boundaries, and dependencies.
20. `data-figure` — bar, trend, heatmap, radar, or other chart with labeled data and a text takeaway.

## Evidence and Detail

21. `evidence-strip` — one claim, source/status, and confidence at scan speed.
22. `quote-callout` — a supported key sentence or user-provided quote; never use as filler.
23. `figure-annotation` — image, diagram, or screenshot with labels explaining why it matters.
24. `details-source-note` — secondary evidence, source notes, caveats, or alternate reasoning.
25. `code-terminal-block` — code, command, prompt, or configuration that must preserve exact text.

## Component Contract

For each selected component, record:

- `purpose`: the decision or reading job it serves.
- `use_when`: content conditions that justify it.
- `avoid_when`: semantic or density conditions that disqualify it.
- `required_data`: minimum fields; missing fields become `TBD`, not invented values.
- `visual_anatomy`: title, body, label, edge, axis, legend, or source treatment.
- `semantic_color_roles`: what colors mean and what must remain legible without color.
- `responsive_fallback`: stack, summarize, reflow, or provide a text equivalent.
- `print_fallback`: what remains when controls and interactive affordances disappear.
- `accessibility_notes`: heading order, labels, focus, contrast, and reading order.

## Required Data and Fallback Map

The following minimum contracts make the 25 components executable rather than decorative:

- `decision-banner`: recommendation + confidence + next action; fallback is a labeled text summary.
- `lead-block`: title + context + audience; fallback is the document heading and subtitle.
- `metric-rail`: stable values + labels + units; fallback is a short list without tiles.
- `status-rail`: state + owner/severity when relevant; fallback is labeled status text.
- `section-rule`: section label; fallback is a semantic heading with no ornament.
- `comparison-table`: shared criteria + option values; fallback is one stacked option summary per row.
- `comparison-rail`: two or more explicitly comparable sides; fallback is a before/after text pair.
- `scorecard`: dimensions + scoring basis + values; fallback is a ranked list with the scoring caveat.
- `quadrant-matrix`: defined x/y axes + comparable points; fallback is a two-column priority list.
- `criteria-matrix`: row/column entities + relationship values; fallback is grouped relationship text.
- `timeline`: ordered dates/stages + labels; fallback is an ordered list.
- `stepper`: finite steps + current state; fallback is a numbered procedure.
- `swimlane`: participants + ordered events; fallback is grouped participant timelines.
- `lifecycle-rail`: states + allowed transitions; fallback is a state table with transition notes.
- `journey-map`: stages + user need/friction/action; fallback is a staged list.
- `concentric-hierarchy`: explicit nesting levels; fallback is an indented hierarchy.
- `relationship-overlap`: explicit sets + overlap labels; fallback is a relationship table.
- `pyramid-hierarchy`: ordered levels + level rationale; fallback is a ranked hierarchy.
- `architecture-map`: nodes + ownership/dependency edges; fallback is a grouped dependency list.
- `data-figure`: series/points + axes/scale/legend/source + text takeaway; fallback is a data table.
- `evidence-strip`: claim + source/status + confidence; fallback is a labeled evidence sentence.
- `quote-callout`: supported quote or key sentence + source when external; fallback is normal prose.
- `figure-annotation`: figure + annotation labels + why-it-matters caption; fallback is caption plus text description.
- `details-source-note`: secondary evidence + caveat/source; fallback is an appendix section.
- `code-terminal-block`: exact code/command text + optional language; fallback is a preformatted text block.

## Composition Limits

- Select 2–6 components for a normal page section.
- Do not repeat the same framed component more than three times without a clear grouping reason.
- Do not place a card inside a card unless the inner unit is a genuinely repeated item or tool.
- Prefer one dominant proof object over several decorative mini-graphics.
