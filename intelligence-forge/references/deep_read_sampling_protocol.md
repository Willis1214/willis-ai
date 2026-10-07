# Deep Read Sampling Protocol

## Purpose

Deep reading is expensive. Sampling must catch real domain knowledge without letting dominant templates erase rare but important cases.

## Sampling Layers

Build sampling cells from:

- project or source family;
- version or date bucket;
- tool, syntax, or generator family;
- lifecycle stage;
- schema or section shape;
- exception density;
- user-marked importance;
- claim-specific counterexample relevance.

## Minimum Sampling Rule

For each active round:

- include at least one representative from every major stratum;
- include every high-impact outlier until resolved or explicitly deferred;
- include files with counterexample hints before more support-only files;
- include rare subtype candidates even when their file count is low;
- reserve holdout files for promotion checks;
- mark unsampled strata as `uncovered`, not absent.

## Priority Formula

Use this qualitative priority order:

```text
counterexample_hint
> high_impact_user_marked
> schema_drift_or_rare_subtype
> exception_density
> uncovered_major_stratum
> support_for_promotable_claim
> stale_stratum_revisit
> ordinary_representative
> holdout
```

## Split Thresholds

Consider `split_domain` when:

- two or more major strata have incompatible architecture;
- the same claim is repeatedly true in one stratum and false in another;
- project/version/tool/stage explains more variance than the claimed domain;
- user says the file families serve different decision purposes.

## Sampling Record

Each deep-read queue should record:

- sampling role: `representative`, `counterexample`, `rare_subtype`, `exception`, `holdout`, `user_marked`, or `stale_revisit`;
- stratum key and value;
- claim ids affected;
- reason for sampling;
- unresolved strata left after the round.

## Anti-Overfitting Rule

Do not deep-read only files that support the current theory.

Every promotion-oriented round must include at least one pressure source: counterexample search, holdout, rare subtype, or user-marked trap.
