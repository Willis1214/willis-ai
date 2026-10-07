---
name: deeply-reader
description: Create evidence-grounded deep reading HTML reports from whole-book files (PDF/DOCX/EPUB/MD/TXT). Use for book intelligence, cognitive maps, method extraction, actionable notes, and work/life reflection; not document editing, OCR, conversion, slides, or shallow mind maps.
---

# Deeply Reader

## Purpose

Turn a full book file into a deep, evidence-aware, visually readable HTML report. The input may be PDF, DOC, DOCX, Markdown, EPUB, TXT, or another text-extractable book format. The goal is not to summarize every chapter evenly; it is to extract the book's useful intelligence: what it argues, how the author thinks and works, what evidence supports those ideas, and what directions the reader can reflect on for real life, work, long-term personal development, and society.

## Trigger Boundary

Use this skill when:

- the input is a whole-book file or a long book-like document in PDF, DOC, DOCX, Markdown, EPUB, TXT, or a similar locally readable format;
- the user asks for reading notes, deep summary, key ideas, wisdom extraction, methodology extraction, action guidance, cognitive map, or "what should I do with this book";
- the user wants more than a brief synopsis or table of contents.

Do not use this skill for:

- document creation, editing, merging, splitting, watermarking, form filling, or format conversion;
- one article, one academic paper, or a small paper batch unless the user explicitly wants book-style reading notes;
- pure text extraction without analysis;
- a shallow mind map, quote dump, or chapter-by-chapter paraphrase.

## Required Output

The final note must contain three layers:

1. **Core Summary**: the book's central thesis, major claims, argument structure, and logic map.
2. **Method Extraction**: the author's concrete methods, workflows, models, heuristics, decision rules, or reusable frameworks.
3. **Reflection Thinking**: deep reflection that connects the book to the user's real life, long-term choices, current work, decisions, constraints, and social environment. This layer should open high-quality thinking directions rather than force a narrow action checklist.

Default final artifact: a standalone HTML file under the current workspace's `output/` directory, unless the user explicitly asks for chat-only output or another format. Use `temp/` for extracted text, page samples, inventories, and other intermediate files. Markdown can be used only as an intermediate evidence draft, not as the final deliverable unless requested.

For final HTML generation, explicitly use `$front-taste` as the visual quality gate. Deeply Reader owns source acquisition, evidence quality, reading analysis, and the three-layer content model; the HTML implementation owns the final standalone presentation, scan-first layout, useful interaction, browser zoom/reflow behavior, PDF source packaging, and validation.

For PDF source reports, every visible page evidence anchor must be linkable back to the source PDF page. The final HTML should embed the source PDF as a local evidence package inside the HTML file when file size and user authorization allow it, so the report remains auditable offline. Use `references/pdf_evidence_links.md` for the page-evidence data model, click behavior, and limits.

## Workflow

1. **Scope the source**
   - Identify the file path, format, title, author, length, language, table of contents, and whether text extraction is reliable.
   - Use `references/source_acquisition.md` to choose the lightest reliable extraction route for PDF, DOC/DOCX, Markdown, EPUB, TXT, or other book-like files.
   - If extraction is weak, try a proportionate fallback only when available. Otherwise continue with an explicit coverage warning.
   - Record what was read directly, sampled, inferred from structure, or unavailable.

2. **Build a book map before analysis**
   - Extract or reconstruct the table of contents.
   - Identify chapter roles: problem framing, thesis setup, conceptual model, method, evidence/cases, objections, conclusion.
   - Prefer thesis-bearing sections first: preface, introduction, conclusion, chapter openings/endings, summaries, diagrams, named models, examples, and repeated terms.

3. **Read in passes**
   - Pass 1: orientation. Determine genre, target reader, central problem, thesis candidate, and likely practical value.
   - Pass 2: argument reconstruction. Map `problem -> claim -> reasoning -> evidence/case -> conclusion`.
   - Pass 3: method and transfer. Extract the author's operating system and test how it applies to the user's actual work context.

4. **Separate evidence from inference**
   - Label claims as `directly supported`, `structure-based inference`, or `reader-side application`.
   - Do not invent facts, page references, author background, or case details.
   - When coverage is partial, state the coverage and confidence instead of pretending full comprehension.
   - Provide enough evidence context for the reader to understand how the author argued, not only what conclusion the assistant drew.
   - Avoid long verbatim quotations. Prefer paraphrased evidence with page, chapter, or section anchors; use only short source phrases when they carry conceptual force.
   - For PDF sources, normalize every concrete page reference into a page evidence anchor with source id, page start, optional page end, visible label, and confidence. Page ranges link to the first page in the range and preserve the range metadata. Do not leave any visible concrete page evidence reference as plain text.

5. **Draft the note**
   - Use `references/note_output_contract.md` for the report structure.
   - Use `references/pdf_evidence_links.md` when the report source is PDF or when extracted evidence has page numbers.
   - Use `references/reading_protocol.md` when the book is long, extraction is imperfect, or the application layer needs more rigor.
   - Keep the report useful to a busy reader: conclusion first, then logic, evidence, method, reflection, and reading-use guidance.
   - Build a clean content model first, then use `$front-taste` to set the visual direction and quality gate before rendering the final HTML.
   - For PDF sources, pass the HTML implementation the source PDF package data and require one unified click path: user clicks a `.pdf-page-link`, the HTML checks the named PDF viewer context for that launch target, opens it if missing or closed, and navigates it to `#page=N`.

6. **Quality gate**
   - Verify the note includes all three required layers.
   - Verify the evidence layer is not just pure opinion: each major claim should have chapter/page/section support where available.
   - Verify the reflection layer includes life and society-level thinking directions, not only Codex/project/workflow implications.
   - Remove generic statements that could apply to any book.
   - Include a brief "coverage and confidence" section so the user knows how much of the source supports the note.
   - Confirm the final artifact is HTML, not Markdown, unless the user explicitly requested Markdown.
   - Confirm the final HTML also satisfies `$front-taste` visual checks: responsive layout, browser zoom/reflow support, no accidental external dependency, and interaction only when it helps reading.
   - For PDF sources, confirm all visible page evidence anchors are clickable, the embedded PDF source package is present, and the click path opens or reuses the configured PDF viewer target, or explicitly report the reason for any fallback.

## Reflection Layer Rules

Use the best available user context: the current request, visible workspace, current project goal, explicit user role, prior context already available in the thread, and any files the user provides. Do not fabricate private context.

If the user's current life or work context is unclear, still produce the reflection layer, but mark it as based on limited context and frame it as thinking directions rather than personal facts. Ask follow-up questions only when the missing context would materially change the report.

The reflection layer must answer:

- What idea from the book changes how the user should think?
- What method can be transplanted into the user's work?
- What question does the book raise about the user's life, identity, relationships, learning, health, risk, or long-term development?
- What social pattern, institutional incentive, or era-level pressure does the book help the user notice?
- Where would the book's advice fail in the user's environment?

Do not include sections named `4.2 对当前判断方式的挑战`, `4.3 最小行动实验`, or `行动清单` unless the user explicitly asks to restore them.

## Output Style

- Write in the user's current language by default.
- Prefer concise analytical prose, tables, and decision/action matrices over decorative mind maps.
- Quote sparingly. Use short quotes only when they carry conceptual force.
- Preserve important original terms, model names, and proper nouns.
- The note should read like a senior advisor's working memo, not a generic book report.
- Use HTML visual hierarchy when it improves reading: anchored navigation, evidence tables, framework grids, expandable source notes, and confidence labels.
- For PDF reports, render page evidence as hyperlinks, not plain text. Examples: `PDF 页 2`, `页 17-35`, and `抽取页 35` should become source-page links with machine-readable `data-pdf-page` attributes in the final HTML. The default target is the browser-managed `DeeplyReaderSourcePDF` PDF viewer context; if a report explicitly uses a system PDF reader instead, the open-state check must target that same system reader/app document state rather than an unrelated HTML/browser state.
- Avoid duplicated numbering between the navigation and body headings. If the navigation already provides an ordinal index, remove leading numeric prefixes from the visible section heading text and navigation label.
- Do not add generic support/tooling controls, design metadata cards, or implementation-explanation info cards unless the user explicitly asks for them. Reading controls should be limited to what directly improves understanding of the report.

## References

- `references/reading_protocol.md`: detailed acquisition and analysis protocol.
- `references/source_acquisition.md`: format-specific source reading routes.
- `references/note_output_contract.md`: required HTML report skeleton and QC checklist.
- `references/pdf_evidence_links.md`: PDF page evidence anchor contract and source-package expectations.
- `$front-taste` (`/Users/lizhendong/.codex/skills/front-taste/SKILL.md`): visual direction and quality gate for the final standalone HTML.
