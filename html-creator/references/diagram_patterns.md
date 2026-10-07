# HTML Creator Diagram Patterns

Use this reference only when a standalone HTML artifact needs workflow, architecture, state, sequence, data relationship, or graph-style expression.

## Diagram Decision Tree

| Need | Default diagram | When to avoid |
| --- | --- | --- |
| Business process, approval path, decision branch | Flowchart | Use a table when every row is independent and sequence is irrelevant. |
| Agent, service, API, or handoff sequence | Sequence diagram | Use a flowchart when concurrency or participants are not important. |
| Lifecycle, release status, retry policy, exception path | State diagram | Use a timeline when time order matters more than allowed transitions. |
| System, dependency, data movement, ownership boundary | Grouped flowchart or architecture map | Use a matrix when relationships are many-to-many and too dense. |
| Data schema, entities, domain object relationships | ER/class-style diagram | Use a plain table when there are fewer than three entities. |
| Research logic, evidence filtering, conclusion downgrade path | Flowchart with evidence tiers | Use bullets when there are no branches or gates. |

## Implementation Choices

Prefer this order:

1. Inline SVG or CSS-native diagram for small, custom, presentation-grade visuals.
2. Mermaid source rendered to SVG locally, then embedded inline.
3. Mermaid source shown inside `<details>` plus a simple SVG fallback when no renderer is available.
4. D3 or Cytoscape only for genuinely interactive data visualizations, dense graph exploration, or user-controlled filtering.

Do not use CDN Mermaid, D3, Cytoscape, external icon fonts, or remote images by default. A standalone HTML report should open offline unless the user explicitly approves external dependencies.

## Visual Rules

- Keep one main idea per diagram.
- Use stable labels that match the surrounding section names.
- Use solid lines for the main flow.
- Use dashed lines for dependency, reference, influence, feedback, or optional paths.
- Keep labels close to the relevant edge.
- Avoid arrowheads landing in node centers; leave visual breathing room around nodes.
- Do not use decorative gradient blobs, bokeh, or generic hero-like illustration.
- Keep text at fixed CSS sizes, not viewport-scaled sizes.
- Provide mobile behavior: wrap, scale the SVG viewBox, or provide a concise mobile summary.

## Mermaid Handling

When using Mermaid as the source DSL:

- Preserve the Mermaid text in a `<details>` block or HTML comment so the diagram is reviewable and editable.
- Use `flowchart LR` for horizontal architecture/data movement and `flowchart TB` for staged gates or vertical processes.
- Prefer specific diagram types over forcing everything into flowcharts.
- Avoid lowercase `end` as a node id or label without quoting.
- Quote labels that contain punctuation, parentheses, slashes, or mixed Chinese/English terms.
- Validate with local Mermaid CLI (`mmdc`) when available. If it is not available, state the validation gap and rely on HTML parse plus browser preview.

## Section Pairing

Every central diagram should be paired with one of these short textual companions:

- Decision implication: what this diagram changes about the recommendation.
- Failure point: which edge or node is the main risk.
- Owner/action: who must act on the next node.
- Evidence boundary: which nodes are supported, assumed, downgraded, or unknown.

## QA Checklist

- Diagram renders in the browser.
- Labels are readable at desktop and mobile widths.
- The diagram does not overlap nearby text or controls.
- Source diagram text is preserved when generated from Mermaid or another DSL.
- Semantics are not carried only by color.
- No unsupported dependency was introduced.
