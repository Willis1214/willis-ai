# Domain Core And Overlay Separation

## Purpose

Most early knowledge should not enter `domain core`. Project, subtype, version, tool, lifecycle, and author patterns are valuable intelligence, but they must be isolated until proven reusable.

## Default Routing

Route new claims conservatively:

| Observation pattern | Default route |
| --- | --- |
| Seen in one project or source family | `project_overlay` |
| Seen in one syntax/schema/tool family | `subtype_overlay` |
| Seen in repeated sections but not checked against exceptions | `candidate` |
| Seen across major strata and pressure-tested | `domain_core` candidate |
| Rare but high-impact | `special_case` |
| Asked by user but not evidenced | `open_question` |

## Domain Core Upgrade Gate

A claim can move from overlay to `domain_core` only when:

- the coverage denominator is explicit;
- support spans relevant major strata;
- holdout files do not contradict it;
- counterexamples are absent, scoped, or downgraded with reason;
- user-confirmed project/version/stage boundaries do not exclude it;
- future regressions can detect accidental overgeneralization.

## Overlay Merge Rule

Do not merge overlays merely because wording is similar.

Merge only when:

- the same underlying behavior or architecture is evidenced;
- vocabulary differences are mapped;
- exceptions are preserved;
- downstream reuse would not change meaning.

## Useful Non-Core Knowledge

An overlay can still be valuable intelligence.

`domain_intelligence.md` should preserve:

- local project practices;
- version-specific migrations;
- legacy patterns;
- tool-specific syntax;
- lifecycle-stage files;
- known anti-patterns;
- one-off traps.

The failure to become `domain_core` is not a failure to become useful intelligence.
