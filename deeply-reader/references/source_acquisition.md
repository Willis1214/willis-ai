# Deeply Reader Source Acquisition

Use the lightest reliable route. The objective is enough grounded source coverage for a deep reading note, not perfect archival conversion.

## Supported Inputs

Primary supported book-like formats:

- `.pdf`
- `.doc`
- `.docx`
- `.md` / `.markdown`
- `.epub` (use this for the user's likely `pueb` typo)
- `.txt`

Other formats are acceptable only when local tools can extract readable text without changing the user's source file.

## General Rules

- Never overwrite the source file.
- Put intermediate extracted text, inventories, and samples under `temp/`.
- Preserve headings, chapter boundaries, lists, tables, captions, and page/section hints when available.
- If extraction loses layout or figures, state that limitation in the final coverage section.
- Do not install third-party tools unless the user approves. Use available system tools or Python standard library first; use common libraries only when already available or clearly justified.

## Format Routes

### PDF

Use when the file is `.pdf`.

Preferred routes:

- `pdfinfo` for metadata/page count when available.
- `pdftotext -layout` for layout-aware text extraction when available.
- `pdfplumber` for page-level text, tables, and selected visual-aware extraction when available.
- Render selected pages only for diagrams, scanned pages, or extraction failures.

Watch for:

- scanned pages;
- multi-column layout;
- missing text layer;
- charts, diagrams, marginal notes, or tables that text extraction flattens.

### DOCX

Use when the file is `.docx`.

Preferred routes:

- `python-docx` when available for paragraphs, headings, and tables.
- unzip OOXML and read `word/document.xml` only when a lightweight fallback is enough.
- `textutil` or `soffice` conversion to text only when available and non-destructive.

Watch for:

- tables;
- footnotes/endnotes;
- comments;
- embedded images or diagrams;
- heading styles that define structure.

### DOC

Use when the file is legacy `.doc`.

Preferred routes:

- macOS `textutil -convert txt -stdout <file>` when available.
- LibreOffice `soffice --headless --convert-to txt` when available.
- If neither works, report the blocker and ask for DOCX/PDF/TXT export.

Watch for:

- conversion loss;
- garbled encoding;
- missing figures/tables.

### Markdown

Use when the file is `.md` or `.markdown`.

Preferred route:

- Read directly as UTF-8 text.
- Preserve heading hierarchy, fenced code blocks, tables, links, and blockquotes.

Watch for:

- multi-file books split across folders;
- images referenced by relative paths;
- generated table of contents that may duplicate headings.

### EPUB

Use when the file is `.epub`.

Preferred routes:

- Treat EPUB as a ZIP archive.
- Read `META-INF/container.xml`, then the OPF package, spine order, and XHTML/HTML chapter files.
- Strip HTML tags while preserving headings, paragraph order, lists, table captions, footnotes, and image alt text when available.
- Use `ebook-convert` or similar only if already installed and useful.

Watch for:

- DRM or encrypted content;
- chapters out of order if spine is ignored;
- footnotes and endnotes;
- images or diagrams not represented in text.

### TXT

Use when the file is `.txt`.

Preferred route:

- Read directly.
- Detect obvious encoding issues and line-break artifacts.
- Infer chapters from repeated headings, numbered sections, or all-caps title lines.

Watch for:

- broken paragraphs;
- missing table of contents;
- page headers/footers repeated in plain text.

## Coverage Report Fields

For every run, record:

- source path and format;
- extraction route;
- coverage: full, high, partial, or weak;
- major sections read;
- skipped or unreadable sections;
- layout/figure/table limitations;
- confidence impact.
