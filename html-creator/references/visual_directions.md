# Visual Directions

Choose one visual direction before writing CSS. Directions are art-direction constraints, not themes to mix freely.

## `editorial-evidence`

- Best for: decision briefs, research, review, and evidence reports.
- Thesis: restrained editorial hierarchy, strong reading column, semantic accents, and drill-down evidence.
- Density: medium-high; text and proof objects share priority.
- Shape: low radius, visible rules, asymmetric split, quiet surface.
- Avoid: marketing hero treatment, excessive metrics, decorative gradients.

## `technical-blueprint`

- Best for: architecture, workflow, system map, lifecycle, and canvas pages.
- Thesis: bounded geometry, explicit relationships, disciplined labels, and one dominant diagram.
- Density: medium; diagram is primary, prose is annotation.
- Shape: grid, thin lines, mono labels, controlled accent color.
- Avoid: unlabelled geometry, ornamental nodes, diagram-only meaning.

## `data-newsroom`

- Best for: comparison, market, operational, or metric-heavy pages.
- Thesis: evidence-first rhythm with strong numbers, restrained chart color, and source-aware captions.
- Density: high but scannable; charts must have text takeaways.
- Shape: compact rails, tables, axis labels, clear status colors.
- Avoid: chart variety without a question, unsupported precision, one-hue dashboards.

## `quiet-minimal`

- Best for: long-form explanation, reflective analysis, and sparse executive notes.
- Thesis: generous whitespace, narrow reading measure, one accent, and carefully placed proof.
- Density: low-medium; emphasis comes from spacing and type scale.
- Shape: flat surfaces, minimal framing, large section rhythm.
- Avoid: empty filler, oversized headings, or hiding important evidence in whitespace.

## Shared Token Rules

- Define background, surface, ink, muted, line, primary, success, warning, error, radius, and spacing before implementation.
- Use color semantically for status, risk, confidence, category, and evidence strength.
- Keep body text readable at fixed CSS sizes; do not use viewport-scaled type.
- Use the smallest visual system that creates a clear hierarchy for the selected page.
