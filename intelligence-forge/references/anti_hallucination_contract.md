# Anti-Hallucination Contract

## Rules

1. A claim is not knowledge until evidence and scope are attached.
2. Model intuition is not evidence.
3. A generated summary cannot be used as support for another generated summary.
4. Claim verification must operate at atomic claim level.
5. The validator should be separated from the extractor for promotion decisions.
6. A claim cannot say "all" unless corpus coverage proves all relevant strata were considered.
7. A contradiction cannot be deleted; it can only be resolved, scoped, or rejected with reason.
8. User feedback does not automatically make a rule universal; it becomes supervised evidence that must be revalidated.
9. Proprietary raw excerpts should be minimized; use file ids, line pointers, hashes, and short summaries when needed.
10. Every promoted rule needs a regression case or deterministic validation hook.
11. Public prior is not file evidence. It can seed questions but cannot certify local truth.
12. Cross-project differences must be scoped, not averaged away.
13. If a file does not record intent, runtime outcome, organizational responsibility, or external validity, do not infer those facts from structure alone.

## Cannot Infer Boundary

The final intelligence must include a `Cannot infer` section.

Default boundaries:

- Do not infer real-world execution ownership from files alone.
- Do not infer business priority from file frequency alone.
- Do not infer current validity of external policy, law, standard, foundry rule, or tool behavior without current source evidence.
- Do not infer runtime behavior unless execution logs, tests, or tool output are present.
- Do not infer author intent when only syntax or comments are available.
- Do not infer that a repeated pattern is preferred; it may be legacy, copied, or deprecated.

When a user confirms a boundary, record it as `user_confirmed_rule` and add a regression case.
