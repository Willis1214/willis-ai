---
name: html-creator
description: Create or revise standalone decision-ready HTML pages from requirements, Markdown drafts, research notes, reports, comparisons, PRDs, code-review findings, market briefs, project updates, or evidence-heavy material. Use when the user needs a visual report, decision page, interactive artifact, visual PRD, HTML-PPT-like canvas, or richer layout/component composition because Markdown is too flat. Do not use for production web-app implementation, PPTX/Word/PDF/Figma delivery, generic landing pages, short linear notes, or source documents that should remain Markdown-first.
---

# HTML Creator

Create self-contained HTML pages that help a human scan, understand, compare, and act faster. Treat HTML as the presentation and decision layer; keep Markdown, JSON, CSV, or notes as the editable evidence layer when those sources already exist.

## Fit Gate

Use HTML when the material needs one or more of: multi-dimensional comparison, evidence tiers, risks, timelines, owners, next actions, visual hierarchy, drill-down, tables, diagrams, or a browser-openable review artifact.

Prefer Markdown when the material is short, linear, still being heavily edited, intended as a README/source spec/prompt, or gains no decision value from styling or interaction.

Do not take over production frontend work. Route React/Next.js/app integration, design-system implementation, PPTX/Word/PDF/Figma output, and generic marketing pages to the appropriate workflow.

## Output Contract

- Produce a real `.html` file unless the user explicitly asks for inline code.
- Default to one self-contained file with inline CSS and only minimal JavaScript.
- Keep source claims, evidence, assumptions, unknowns, and decisions distinct; never invent metrics, citations, or relationships.
- Prefer offline-safe output. Avoid external fonts, CDNs, images, and scripts unless approved.
- Preserve diagrams as inspectable inline SVG/CSS or locally rendered SVG; keep source DSL text when applicable.
- Follow the active workspace rule: final HTML under `output/`, temporary checks under `temp/`.

## Page Routing

Choose exactly one primary archetype, then adapt lightly:

- `decision-brief`: recommendation, comparison, evidence, risk, next action.
- `requirements-prd`: objective, scope, flow, requirements, acceptance, open questions.
- `research-report`: conclusion, source quality, findings, contradictions, evidence implications.
- `status-report`: state, progress, timeline, metrics, blockers, next checkpoint.
- `review-risk`: release decision, findings, coverage, required fixes, residual risk.

Read `references/html_creator_patterns.md` for archetype details and base layout choices. Read `references/diagram_patterns.md` when process, state, sequence, architecture, dependency, data movement, or screen journey structure is central.

## Design Layer

Build a design plan before writing HTML. This is a semantic choice layer, not a random template selector:

1. Choose `mode`: `document` or `canvas`.
2. Choose one `visual_direction`.
3. Write the `Design Plan`: reading path, focal point, primary layout, components, data rules, responsive/print fallback, and anti-patterns.
4. Select one primary canonical layout and at most two supporting patterns.
5. Select components only when their reading job and required data exist.

Read `references/layout_atlas.md`, `references/component_catalog.md`, `references/design_plan_schema.md`, and `references/visual_directions.md` for this step. The first release is intentionally curated to 10–12 canonical layouts and 20–25 semantic components; do not reproduce every external library.

## Renderer Profiles

### `document`

Use for long-form, evidence-led, printable pages. Allow variable height, vertical reading, tables, expandable evidence, mobile reflow, and text fallbacks for wide structures.

### `canvas`

Use for HTML-PPT-like pages, posters, single-screen infographics, and one-claim visual narratives. Use a bounded 16:9 frame by default, one visual center, short prose, and one primary proof object. Read `references/canvas_profile.md`; this profile is not a PPTX generator.

## Content and Visual Rules

- Show why the page matters and what the reader should do next; do not merely beautify source text.
- Keep facts, interpretations, assumptions, decisions, open questions, and actions visually distinct.
- Do not use a card wall as the default page grammar; cards are for repeated items, metric tiles, or framed tools.
- Use color semantically for status, risk, confidence, category, or evidence strength; never rely on color alone.
- Do not use decorative gradients, bokeh, floating orbs, filler icons, or unsupported charts.
- Use fixed readable CSS type sizes, logical headings, visible focus states, and accessible text fallbacks.

## Build and Validate

1. Confirm HTML fit, audience, source facts, assumptions, unresolved questions, and desired outcome.
2. Normalize the content model and attach source/date context to claims.
3. Build and record the design plan.
4. Implement semantic HTML with CSS variables; use inline SVG/CSS or local diagram output when diagrams are needed.
5. Validate structure, browser rendering, desktop/mobile behavior, print behavior, console state, dependencies, placeholders, and claim support.
6. Run `references/visual_qc.md`; for `canvas`, inspect desktop, thumbnail, and mobile fallback states.
7. Report the actual HTML path, overwrite status, checks performed, and remaining risks.

## Negative Triggers

Do not use this skill for production app pages, generic landing pages, PPTX/Word/PDF/Figma artifacts, short answers, simple one-screen notes, raw data extraction, or pages where HTML adds no decision value. When a neighboring workflow is better, route there and keep HTML Creator out of the way.
