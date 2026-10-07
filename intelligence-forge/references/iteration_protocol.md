# Iteration Protocol

## States

Use these states:

```text
onboard -> draft_cognition -> profile -> stratify -> seed_extract -> counterexample_search -> validate -> question -> feedback -> regress -> report -> promote_candidate -> intelligence_update
```

## Dynamic Loop Controller

Iteration count is not fixed. The controller decides whether to continue, split, stop, or promote.

Each loop must declare:

- objective for this round;
- files or strata touched;
- candidate claims changed;
- new contradictions or exceptions;
- user questions opened or closed;
- regression cases added or passed;
- budget-to-signal judgment;
- next route: `continue`, `split_domain`, `ask_user`, `holdout_validate`, `promote`, `partial_stop`, or `blocked_stop`.

## Configurable Minimum

A domain profile may set `min_iterations`, but this is only a guardrail. It is not proof of quality.

Examples:

| Situation | Loop behavior |
| --- | --- |
| Small, homogeneous corpus with stable user briefing | Fewer loops may be enough if coverage and regression are explicit. |
| Large multi-project corpus | Continue until subtype drift and high-impact contradictions are scoped. |
| Many unresolved user questions | Pause as `blocked_stop` or `partial_stop` rather than hallucinating closure. |
| Strong novelty keeps appearing | Continue or split into subdomains. |
| Budget signal is low but risks remain | Produce `partial` intelligence with explicit unresolved boundary. |

## Stop Criteria

Promotion to `domain_intelligence.md` can be considered only when:

- novelty rate is low;
- high-impact contradiction queue is empty or scoped;
- prior regression cases pass;
- relevant strata are represented, excluded, or explicitly unresolved;
- no special case is being generalized silently;
- public priors have been separated from file evidence;
- subtype or project overlays are explicit;
- `Cannot infer` limits are written.

## Exit States

Use one of these final states:

| State | Meaning |
| --- | --- |
| `usable` | Sufficiently supported for the stated audience and scope. |
| `partial` | Useful intelligence exists, but unresolved areas must remain explicit. |
| `blocked` | User/domain information or evidence is missing for high-impact decisions. |
| `unsafe_to_reuse` | Corpus drift, contradictions, or evidence gaps make reuse misleading. |
