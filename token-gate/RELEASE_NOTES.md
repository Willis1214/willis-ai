# Collection migration — 2026-10-07

源业务版本保持 `0.1.0`；本次迁移只改变仓库位置、安装说明和必要路径。

---

# token-gate v0.1.0

Initial public release candidate for Token Gate.

## Highlights

- Adds a silent pre-execution decision gate for avoidable token waste.
- Preserves the user's final goal, deliverable, quality bar, and acceptance criteria.
- Distinguishes justified high-token work from meaningless token consumption.
- Provides a four-level interruption gate and concrete preferred alternative patterns.
- Documents innovation points and recommended use cases for public evaluation.

## Validation

- Skill structure validation passes with the Codex skill creator validator.
- Staging package contains `SKILL.md` and `agents/openai.yaml`.
- Release package is generated from staging rather than directly from the source skill directory.
