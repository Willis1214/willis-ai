# Visual Quality Control

Run this review after rendering the HTML. Structural parsing alone cannot prove that a page has hierarchy or visual meaning.

## Quality Dimensions

Score each as `Pass`, `Weak`, or `Fail`:

- `identity`: page purpose and selected mode are obvious in the first viewport.
- `hierarchy`: title, conclusion, evidence, and next action can be scanned in order.
- `composition`: sections have distinct roles; the page is not a wall of equal cards.
- `typography`: headings, labels, body, values, captions, and warnings are distinct.
- `density`: information density matches document reading or canvas viewing.
- `semantic_color`: color consistently encodes status, risk, confidence, category, or evidence.
- `proof_object`: charts, diagrams, tables, and figures explain a claim rather than decorate it.
- `responsive`: desktop, mobile, and print states preserve the intended meaning.
- `accessibility`: reading order, labels, contrast, focus, and text alternatives are present.

## Hard Fail Conditions

- Every paragraph is framed as a card without a semantic reason.
- A chart or diagram is used without the data/relationship that justifies it.
- A data figure lacks the applicable axis, scale, legend, labels, source, or text takeaway.
- The first viewport hides the conclusion or primary visual claim.
- Canvas text is unreadable at desktop or the mobile fallback clips key information.
- A wide table or diagram has no mobile summary or text fallback.
- Color is the only carrier of status, evidence strength, or risk.
- External fonts, scripts, images, or CDNs are introduced without approval.
- Placeholder, invented, or unsupported claims remain in the final page.

## Minimal Evidence

- HTML parser or lint result.
- Desktop render at a normal report width or full canvas size.
- Mobile render or responsive inspection.
- Console check when JavaScript exists.
- External dependency and placeholder scan.
- A short visual review record naming the selected profile, layout, and any remaining `Weak` items.
