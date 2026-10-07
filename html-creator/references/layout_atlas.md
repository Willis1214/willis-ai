# Layout Atlas

Use this reference after the content model and before HTML implementation. Select one primary layout; add supporting components only when they clarify the same reading path.

The atlas is a canonical HTML subset of a larger visual inspiration library. It does not attempt to reproduce every image-composition variation. Translate image composition into HTML structure, focal point, whitespace, reading order, and responsive behavior.

## Selection Rules

- Select one primary layout and at most two secondary patterns.
- Prefer the layout that matches the content relationship, not the most decorative option.
- Use cards for repeated items or bounded tools, never as the default wrapper for every paragraph.
- If the content has one claim and one visual center, consider `canvas-focal`.
- If the content has evidence, comparison, or long prose, prefer a `document` layout.
- If no layout improves comprehension, keep a simple semantic flow and record why.

## Canonical Layouts

### 1. `editorial-split`

- Profile: `document`
- Use for: decision briefs, research reports, evidence-led reviews.
- Structure: lead and conclusion on the left; evidence, risk, or action rail on the right; stack on narrow screens.
- Avoid when: the material has no clear primary conclusion or side evidence.

### 2. `narrative-longform`

- Profile: `document`
- Use for: explanatory essays, method notes, long-form analysis.
- Structure: wide reading column, section rules, pull quotes, figures, and expandable source notes.
- Avoid when: the reader must compare many options side by side.

### 3. `evidence-rail`

- Profile: `document`
- Use for: source synthesis, QC, review, due diligence.
- Structure: conclusion first, then a visible retained/downgraded/eliminated evidence rail.
- Avoid when: evidence has no meaningful strength or status distinction.

### 4. `comparison-runway`

- Profile: `document`
- Use for: vendor, option, strategy, or before/after comparison.
- Structure: one comparison spine with criteria, trade-offs, and decision implication; use a mobile summary before a wide table.
- Avoid when: the options are not evaluated against shared criteria.

### 5. `vertical-sequence`

- Profile: `document`
- Use for: timeline, process, lifecycle, incident, or user journey.
- Structure: vertical axis with stages, owners, status, and exceptions.
- Avoid when: there is no sequence or state transition.

### 6. `asymmetric-feature`

- Profile: `document` or `canvas`
- Use for: one dominant idea supported by one proof object.
- Structure: large focal region plus a smaller annotation or evidence region.
- Avoid when: all content items have equal weight.

### 7. `structured-grid`

- Profile: `document` or `canvas`
- Use for: repeated items, feature inventory, checklist, or comparable modules.
- Structure: measured grid with clear grouping and one non-card anchor such as a title band or timeline.
- Avoid when: the grid is only being used to avoid deciding the information hierarchy.

### 8. `quadrant-matrix`

- Profile: `document` or `canvas`
- Use for: two-axis assessment, prioritization, portfolio, or risk positioning.
- Structure: explicit x/y axes, labels, thresholds, and text fallback.
- Avoid when: the axes are subjective but not defined, or points have no comparable scale.

### 9. `concentric-hierarchy`

- Profile: `canvas` or compact `document`
- Use for: nested priorities, layers, scope, or system rings.
- Structure: center-to-edge hierarchy with labels outside dense geometry.
- Avoid when: the relationship is sequential, not nested.

### 10. `relationship-overlap`

- Profile: `canvas` or compact `document`
- Use for: explicit set overlap, shared ownership, or intersecting concerns.
- Structure: limited number of labeled regions with a text summary.
- Avoid when: relationships are hierarchical or directional; use a tree or flow instead.

### 11. `pyramid-hierarchy`

- Profile: `canvas` or `document`
- Use for: priority, maturity, funnel, or layered argument.
- Structure: levels must represent a real order, not merely decorative stacking.
- Avoid when: items are peers or the hierarchy is unknown.

### 12. `canvas-focal`

- Profile: `canvas`
- Use for: one claim, one visual center, one proof object.
- Structure: bounded 16:9 frame, focal headline, one dominant diagram/figure, sparse annotation.
- Avoid when: the page needs paragraphs, dense tables, or multiple independent decisions.

## Responsive and Print Fallback

- `document` layouts reflow into a single readable column and provide text summaries for wide structures.
- `canvas` layouts preserve the visual frame on desktop; below the mobile threshold, provide a summary-first stacked fallback or an explicitly labeled zoomable frame.
- Every diagram keeps its semantic labels in HTML or a nearby text summary.
- Print output removes controls and preserves the claim, proof object, labels, and source notes.
