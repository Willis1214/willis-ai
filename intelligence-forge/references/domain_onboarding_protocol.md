# Domain Onboarding Protocol

## Purpose

Before reading a private corpus, build a draft understanding of the professional field and file type. This prevents the induction loop from treating raw files as context-free text and makes later user questions more precise.

## Stage 0 Inputs

Ask the user for a compact domain briefing:

- field and file type;
- what the files control, configure, describe, or decide;
- intended final intelligence target;
- known project families, versions, tools, authors, or lifecycle stages;
- known traps, exceptions, deprecated patterns, and terms of art;
- sensitivity rules for raw text, paths, excerpts, and external research.

## Research And Study Pass

When allowed, study public or general material about the field before corpus induction.

The output is not promoted knowledge. It is a prior used to generate better questions and an initial reading frame.

Required sections in `draft_cognition.md`:

- `Domain summary`: what the field appears to be about.
- `File role hypothesis`: what this file type likely does.
- `Likely architecture`: expected sections, objects, dependencies, or workflows.
- `Key vocabulary`: terms that may need local meaning.
- `Likely variation axes`: project, version, tool, stage, author, template, or policy differences.
- `Known unknowns`: questions that need user confirmation before private induction.
- `Assumption ledger`: each assumption marked as `public_prior`, `user_brief`, or `unverified`.

## Prior Contamination Guard

Public research and user briefing must be kept separate from file evidence.

Use these source classes:

- `public_prior`: useful for orientation, never sufficient for promotion.
- `user_brief`: trusted as task framing, still scoped to the user's stated context.
- `file_observed_fact`: observed in corpus artifacts.
- `user_confirmed_rule`: user answer accepted as supervised evidence.
- `unresolved_hypothesis`: plausible but not yet supported enough.
- `rejected_assumption`: disproven or user-rejected prior.

## Entry Gate To Corpus Induction

Do not begin promotion-oriented corpus induction until these are explicit:

- corpus scope and sensitivity policy;
- draft cognition reviewed or accepted by the user;
- expected final intelligence file audience;
- extraction capability boundary;
- initial subtype or schema-drift hypotheses;
- open questions that would change reading strategy.

If the user chooses to skip public research, record the waiver and proceed with a user-brief-only draft cognition.
