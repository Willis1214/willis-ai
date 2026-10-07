# PDF Evidence Links

Use this reference when a Deeply Reader source is a PDF and the final output is HTML.

## Contract

Every visible concrete page evidence reference in the final report must be clickable. Do not leave a concrete page evidence label visible as plain text if the source PDF and page number are known.

Examples that must become links:

- `PDF 页 2`
- `页 17`
- `页 17-35`
- `抽取页 35`

Do not link vague page-related text without a concrete number, such as `页码以抽取页为准`.

## Evidence Data Model

Represent each PDF page evidence link with machine-readable attributes:

```html
<a
  class="pdf-page-link"
  href="#pdf-page-17"
  data-pdf-source-id="source-pdf"
  data-pdf-page="17"
  data-pdf-page-end="35"
  title="打开源 PDF 第 17 页"
>页 17-35</a>
```

Rules:

- `data-pdf-page` is required and must be a positive integer.
- `data-pdf-page-end` is optional and used for ranges.
- Ranges link to the first page in the range while preserving the ending page as metadata.
- The visible label must preserve the original evidence wording.
- Page numbers should be the extracted PDF page numbers used during source acquisition. If paper-book page numbers differ, label the basis clearly.

## Source Package Expectation

For PDF source reports, provide the source PDF to the final HTML implementation as a local evidence package:

- source file path;
- source file name;
- MIME type `application/pdf`;
- byte size;
- base64 payload or a generated package path for embedding;
- extraction-page basis and known page-offset caveats.

The final HTML should embed the PDF package when feasible so the report remains auditable offline. Treat this as an HTML-embedded local source package, not browser `localStorage`. If the PDF is too large, confidential, missing, or not user-authorized for embedding, the report must state the fallback and keep page evidence labels visible.

## Click Behavior And Open-State Check

The open-state check must match the actual launch target.

Default supported path: browser-managed reuse of one named PDF viewer context:

1. user clicks a page evidence link;
2. the HTML creates a Blob URL from the embedded PDF package if needed;
3. the HTML checks its `DeeplyReaderSourcePDF` window reference;
4. if the named viewer is missing or closed, the HTML opens it;
5. if it is already open, the HTML reuses/navigates that same named viewer;
6. the PDF viewer navigates to the requested page with `#page=N` when supported.

Ordinary browser JavaScript cannot reliably inspect whether the same PDF is already open in an external system PDF reader such as Preview or Acrobat. If a report explicitly chooses a system PDF reader launch path, do not check whether the HTML page or browser tab is open as a substitute. That path must use an external native helper or automation that checks the corresponding system reader/app document state, opens the PDF if needed, and then jumps to the requested page if the reader supports page-targeted automation.

Do not promise OS-level PDF-process detection from standalone HTML.

## QA

Before final delivery:

- Check every visible concrete PDF page reference is wrapped in `.pdf-page-link`.
- Check every `.pdf-page-link` has `data-pdf-page`.
- Check the final HTML contains an embedded PDF package or an explicit fallback notice.
- Browser-test at least one page link from the report. The opened URL should contain `#page=<number>`.
- Browser-test two different page links. The second click should reuse the same named PDF viewer context where the browser permits it.
- Check the open-state logic is not mixed across targets: browser viewer paths check/reuse the browser viewer; system-reader paths require a matching native helper and must not claim standalone HTML can inspect the reader.
