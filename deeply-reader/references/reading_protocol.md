# Deeply Reader Reading Protocol

## Source Acquisition

Start with a source inventory:

- File path, format, file size, length/page count when available, and title/author if available.
- Whether text extraction works.
- Table of contents or inferred chapter boundaries.
- Pages with diagrams, tables, named frameworks, chapter summaries, or dense cases.

Use `source_acquisition.md` for format-specific routes before doing deep analysis.

Preferred extraction order:

1. Metadata and table of contents.
2. Preface, introduction, conclusion, afterword.
3. Chapter openings and endings.
4. Sections with named models, numbered steps, frameworks, examples, diagrams, and tables.
5. Full text when feasible; otherwise stratified chapter samples.

For very long books, do not spend the entire budget on raw extraction. Build a coverage map first, then allocate reading depth to thesis-bearing and method-bearing sections.

## Three-Pass Reading

### Pass 1: Orientation

Answer:

- What kind of book is this?
- What problem is the book trying to solve?
- Who is the intended reader?
- What is the central thesis candidate?
- What would count as the book's practical value?

Output: one-paragraph orientation and a provisional logic map.

### Pass 2: Argument Reconstruction

Build the core chain:

`problem -> central thesis -> major claims -> reasoning -> evidence/cases -> conclusion`

For each major claim, capture:

- claim text;
- supporting chapter/section/page hint when available;
- evidence type: data, case, anecdote, theory, practitioner experience, historical example, analogy;
- confidence: high, medium, low;
- weakness, missing assumption, or likely overreach.

Output: concise argument table plus a narrative explanation of how the book's logic works.

### Pass 3: Method And Transfer

Extract the author's operating system:

- named frameworks;
- step-by-step processes;
- heuristics and decision rules;
- diagnostic questions;
- sequencing logic;
- tradeoff rules;
- constraints or contexts where the method works.

Then translate it into the user's environment:

- user-context anchor: what current work or decision this connects to;
- transferable principle;
- concrete adaptation;
- smallest useful action;
- risk or failure mode;
- evidence needed to know if it works.

Output: method table and application matrix.

## Evidence Discipline

Use these labels:

- `directly supported`: visible in extracted text, page sample, diagram, or table.
- `structure-based inference`: inferred from chapter structure, repeated concepts, or argument sequence.
- `reader-side application`: the assistant's adaptation to the user's work context.

If source coverage is incomplete, do not hide it. State:

- what was extracted;
- what was sampled;
- what could not be read;
- which conclusions have lower confidence.

## Quality Bar

A strong note:

- states the book's central claim in specific, testable language;
- explains the author's logic instead of listing chapters;
- extracts reusable methods in operational form;
- includes practical actions and boundary conditions;
- distinguishes the book's wisdom from the assistant's application ideas;
- says what the user can ignore, disagree with, or test.

A weak note:

- paraphrases the table of contents;
- creates a decorative mind map without decisions or actions;
- gives generic inspiration that could apply to any book;
- fails to say what was actually read;
- invents facts, examples, or page references.
