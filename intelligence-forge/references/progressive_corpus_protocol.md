# Progressive Corpus Protocol

## Principle

All files must be visible; not all files must be deeply read in every iteration.

Visibility is not a flat file list. Every corpus must be stratified before claims are generalized.

## Corpus Size Routing

| Corpus size | Required approach |
| --- | --- |
| 5-10 files | Full manifest, full shallow profile, likely full deep read, leave-one-out validation. |
| 11-30 files | Full manifest, full shallow profile, deep read rare/outlier strata, rotate holdout. |
| 31-100 files | Full manifest, full shallow profile, stratified deep waves, counterexample search across all files. |
| 100+ files | Same protocol plus batch queue, novelty threshold, and stale-stratum revisit schedule. |

## Input Stratification

Build strata from multiple layers:

| Layer | Purpose |
| --- | --- |
| `metadata` | project, version, date, author, path, tool, extension, file size, source family. |
| `content` | sections, keywords, declarations, repeated blocks, commands, field names, comments. |
| `behavior` | what the file appears to configure, validate, transform, decide, or output. |
| `exception` | unusual syntax, contradictions, deprecated patterns, project-only logic, overrides. |
| `feedback` | user-marked important files, known traps, prior corrections, regression cases. |

The first shallow pass must produce a subtype or schema-drift hypothesis before deep reading is treated as representative.

Deep reading should follow `deep_read_sampling_protocol.md`. Sampling must preserve rare subtype and exception signals, not only majority templates.

## Subtype And Schema Drift

Do not assume the corpus is one homogeneous file type.

Detect and preserve drift such as:

- project family differences;
- tool or syntax version differences;
- template changes over time;
- stage differences such as setup, checker, report, waiver, or override files;
- author or team conventions;
- legacy, deprecated, or migration-only files.

If drift is present, claims must declare their scope as `domain core`, `subtype overlay`, `project overlay`, `local exception`, or `unknown`.

Default new drift-sensitive claims to overlay lanes. Upgrade to `domain core` only through `core_overlay_separation.md`.

## File States

Each included file must have one visible state:

- `deep_read`
- `shallow_profiled`
- `cluster_represented`
- `holdout`
- `queued`
- `excluded_with_reason`

## Coverage Denominator

Every candidate claim must name the denominator it claims over:

- all included files;
- a subtype;
- a project family;
- a version range;
- a section or object class;
- user-confirmed scope.

Promotion is blocked when the denominator is wider than the evidence.

Lack of full coverage should not delete the claim. Route it to a narrower lane or leave it as an exploratory candidate.

## Blocking Conditions

Block promotion when:

- a relevant major stratum is unprofiled;
- a claim says "all" but corpus coverage is partial;
- counterexample search has not touched relevant strata;
- a high-impact outlier is queued but unresolved;
- subtype/schema drift is detected but not represented in claim scope;
- file-observed facts are mixed with public prior without source labels;
- no sampling record exists for high-impact promoted claims;
- domain-core promotion skips overlay separation.
