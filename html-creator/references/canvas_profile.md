# Canvas Profile

Use `canvas` for HTML-PPT-like pages, posters, single-screen infographics, and visual narratives. It is not a PPTX generator and it does not replace the `document` profile.

## Core Contract

- Use a bounded 16:9 canvas by default.
- Express one main claim and one dominant visual center per canvas.
- Keep prose short; move detail to captions, notes, or a paired document page.
- Use CSS Grid/Flexbox for macro layout and inline SVG/CSS for geometry.
- Avoid coordinate-heavy absolute positioning except for small decorative or diagram primitives.
- Keep labels in semantic HTML or provide an adjacent text summary.
- Do not add animation, keyboard paging, export, or external chart libraries unless explicitly requested.

## Recommended Composition

1. Kicker or section number.
2. Large claim headline.
3. One proof object: diagram, comparison, chart, or figure.
4. Minimal annotations and source note.
5. Optional status or next-action strip.

## Mobile Fallback

At narrow widths, do not merely shrink all canvas text. Use one of these explicit strategies:

- `summary-first`: show the claim, takeaway, and simplified proof object in a readable stacked view.
- `zoomable-frame`: retain the 16:9 frame with an explicit zoom/scroll affordance and a text summary outside it.

Default to `summary-first` when the canvas contains more than one label cluster or any text smaller than normal body text.

## Validation

- Desktop: inspect the full canvas and a thumbnail-sized view.
- Mobile: verify the fallback is readable and does not clip the claim or proof labels.
- Print: preserve the canvas boundary, claim, proof object, labels, and source note.
- Accessibility: expose a heading and a text equivalent for the primary visual relationship.
