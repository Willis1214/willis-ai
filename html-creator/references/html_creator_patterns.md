# HTML Creator Patterns

Use this reference when implementing a real HTML deliverable.

## Layout Patterns

### Decision Page

- Top band: title, subtitle, update timestamp, source status.
- Summary strip: recommendation, confidence, top risk, next action.
- Two-column body on desktop:
  - Left: decision narrative, criteria, risks.
  - Right: evidence, open questions, action list.
- Full-width comparison table when options are central.
- Appendix: sources, raw notes, excluded material.

### Requirements Page

- Top band: feature name, status, audience, version.
- Flow section: user journey, state sequence, or screen transition diagram when sequence matters.
- Requirements table:
  - ID
  - requirement
  - priority
  - rationale
  - acceptance signal
  - open issue
- Keep non-goals near scope so reviewers see boundaries early.

### Evidence Report

- Use three visibly separate evidence groups:
  - Retained: strong enough to support the conclusion.
  - Downgraded: useful but weak, stale, indirect, or contradicted.
  - Eliminated: excluded with reason.
- Each evidence row should carry source, date, claim, implication, and confidence.
- Do not hide weak evidence; label it.

## Component Choices

- Use tables for comparison and requirements.
- Use metric tiles only for stable numeric summaries.
- Use timelines for sequencing, not decoration.
- Use diagrams for workflows, handoffs, architecture, state transitions, data movement, and dependency maps when prose would hide structure.
- Use risk matrices when severity and likelihood both matter.
- Use `<details>` for long evidence, source notes, and alternative reasoning.
- Use filter chips only when the page has at least 8-10 repeated items.

For diagram-specific routing and QA, read `references/diagram_patterns.md`.

## CSS Baseline

Use a neutral, non-branded baseline unless the user provides a brand system:

```css
:root {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --ink: #18212f;
  --muted: #5f6b7a;
  --line: #d9dee7;
  --accent: #2563eb;
  --good: #0f7b4f;
  --warn: #9a6700;
  --bad: #b42318;
  --info: #245bdb;
  --radius: 8px;
  --shadow: 0 1px 2px rgba(24, 33, 47, 0.08);
}
```

Rules:
- Use `border: 1px solid var(--line)` before shadows.
- Keep `letter-spacing: 0`.
- Do not scale font size with viewport width.
- Keep body text around 15-17px; use compact table text around 13-14px.
- Use `overflow-x:auto` for wide tables plus a concise mobile summary when the table is central.

## Accessibility And Sharing

- One `h1`.
- Logical heading order.
- Visible focus states for interactive controls.
- No information conveyed by color alone.
- Print styles for long reports:

```css
@media print {
  body { background: #fff; }
  .no-print { display: none !important; }
  a { color: inherit; text-decoration: none; }
  section { break-inside: avoid; }
}
```

## QA Checklist

- The first viewport answers: what is this, what is recommended, how confident are we, and what is next.
- No claims without evidence, assumption label, or explicit user-provided basis.
- No mixed evidence tiers.
- No placeholder text.
- No broken local links or external dependencies unless approved.
- Tables remain readable at mobile width or have a mobile summary.
- Diagrams remain readable at mobile width and preserve source diagram text when generated from Mermaid or another DSL.
- Interactive controls work without console errors.
- The final file opens directly in a browser.
