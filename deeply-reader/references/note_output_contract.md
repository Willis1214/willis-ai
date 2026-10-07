# Deeply Reader HTML Output Contract

Use this contract unless the user provides a different template.

## Default Artifact

- Final deliverable: one standalone `.html` file per book under the current workspace's `output/` directory.
- Intermediate materials: extracted text, inventories, evidence pools, draft notes, and QC materials under `temp/`.
- Do not make Markdown the final output unless the user explicitly asks for Markdown.
- The HTML must be readable offline: inline CSS, no external CDN, no remote images, no external fonts.
- The final HTML must pass `$front-taste` before delivery. Deeply Reader supplies the evidence-backed reading content; the HTML implementation supplies the final visual structure, browser zoom/reflow behavior, PDF source packaging, and HTML validation discipline.
- For PDF source reports, the source PDF should be embedded inside the final HTML as a local evidence package when feasible. Every visible page evidence reference must link back to the corresponding PDF page through a machine-readable link.

## Required HTML Structure

The final report must contain these sections, using equivalent Chinese headings when the user writes in Chinese:

1. **Reading Scope And Confidence**
   - source path;
   - identified title, author, publisher/date when available;
   - input format and extraction route;
   - coverage level: full, high, partial, or weak;
   - extraction limitations such as missing OCR, flattened diagrams, or unreadable tables;
   - confidence labels for major conclusions.

2. **Executive Thesis**
   - 1-3 sentence answer: what is the book's most valuable wisdom?
   - show the book's central problem and central answer.

3. **Layer 1: Core Summary**
   - central thesis;
   - major claims;
   - reconstructed logic map using `problem -> diagnosis -> method -> evidence -> conclusion`;
   - argument table with `claim / author reasoning / evidence anchor / confidence / possible weakness`.

4. **Evidence-Rich Reading Notes**
   - not a quote dump and not a chapter-by-chapter paraphrase;
   - preserve how the author argues: concept, example/case, reasoning step, and implication;
   - cite page, chapter, section, or structural anchor when available;
   - for PDF sources, render concrete page anchors such as `PDF 页 2`, `页 17-35`, or `抽取页 35` as PDF page hyperlinks with `data-pdf-page` metadata, with no visible concrete page evidence left as plain text;
   - use paraphrase for source evidence and quote only very short phrases when necessary.

5. **Layer 2: Method Extraction**
   - reusable methods, workflows, models, heuristics, diagnostic questions, or decision rules;
   - each method should include `solves what / steps / usable condition / failure boundary / source anchor`;
   - include a compact method map or framework grid.

6. **Layer 3: Deep Reflection**
   - must include more than current work or Codex/project implications;
   - include thinking directions for real life, long-term personal development, relationships, health or risk, learning, identity, and broader society when relevant;
   - frame this as thinking guidance, not forced personal advice;
   - distinguish book-supported ideas from reader-side reflection.

7. **How To Use This Book**
   - what to retain;
   - what to test carefully;
   - what to ignore or downgrade;
   - what chapters/pages/sections deserve rereading;
   - no checklist-style task list unless requested.

8. **Reverse Review**
   - where the author may have simplified too much;
   - assumptions that may not hold;
   - the strongest counterargument;
   - situations where the book's method may fail.

9. **Evidence Appendix**
   - table of key claims with page/chapter/section anchors;
   - PDF page/chapter anchors must be clickable when the source is PDF;
   - label evidence source as `direct support`, `structure inference`, or `reader-side reflection`;
   - record extraction limitations.

## Explicitly Removed Default Sections

Do not include these sections unless the user explicitly asks to restore them:

- `4.2 对当前判断方式的挑战`
- `4.3 最小行动实验`
- `## 7. 行动清单`
- any forced 24-hour / 7-day action checklist

## Visual Requirements

- Use a restrained report layout with a sticky or anchored table of contents for long reports.
- Avoid duplicated numeric prefixes between the table of contents and body headings. If the table of contents uses visible ordinal markers, body `h2` headings and TOC labels should not repeat leading numbers such as `0.`, `1.`, or `2.`.
- Use semantic color for evidence strength, confidence, method type, and reflection level.
- Use tables, framework grids, timelines, or compact diagrams only when they improve comprehension.
- Use `<details>` for secondary evidence and source notes.
- Avoid decorative gradients, floating ornaments, and marketing-style hero pages.
- Keep mobile readable; tables must scroll or collapse without text overlap.
- Do not include generic support controls, design-system labels, implementation metadata, or informational side cards that explain the page itself. Keep only reading controls that directly help scan, navigate, filter, compare, or understand the book report.
- For PDF sources, provide source-page evidence links that open or reuse a named browser PDF viewer window and jump with `#page=N`. The open-state check must target the same viewer that is launched. Do not claim standalone HTML can detect arbitrary external PDF reader processes.

## Mandatory Checks

Before finalizing, confirm:

- The final output is HTML and stored under `output/`.
- The report has the three layers: core summary, method extraction, deep reflection.
- The evidence layer explains how the book argues, not just the assistant's conclusions.
- Removed sections are absent.
- The reflection layer includes life and society-level thinking directions, not only work/project implications.
- Claims are grounded in extracted text, source structure, or explicitly labeled reader-side reflection.
- Coverage and confidence are stated.
- The report identifies the input format and reading method.
- The HTML parses with a local parser and has no placeholder text.
- `$front-taste` has been used as the visual quality gate for the final HTML presentation layer, unless the user explicitly required a fixed template/style with no beautification.
- Body headings and TOC labels do not duplicate numeric section prefixes.
- No generic support controls or implementation-info cards remain unless explicitly requested.
- For PDF sources, all visible concrete page evidence references are hyperlinks with `data-pdf-page`.
- For PDF sources, the HTML contains a local embedded source package or explicitly reports why the PDF could not be embedded.
- For PDF sources, the click handler opens the PDF viewer if missing or closed and reuses/navigates the same viewer when it is already open.

## Language

Use Chinese when the user's request is primarily Chinese. Keep proper nouns, book titles, model names, and original framework names in their original language when that preserves meaning.
