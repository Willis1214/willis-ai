# Token-Gate_Skill

## English

Token Gate is a silent pre-execution skill for Codex-style coding agents.

The public repository name is `Token-Gate_Skill`. The installable Codex skill name remains `token-gate`.

It prevents avoidable model-context waste before expensive work starts, while preserving the user's original goal, deliverable, quality standard, and acceptance criteria.

### Why It Matters

Large token usage is sometimes necessary. Full audits, complete artifact generation, compliance work, and exhaustive reviews may legitimately need a large context budget.

Token Gate focuses only on meaningless token consumption: full-repository reads when an index is enough, full-log ingestion when filtered traces are enough, raw CSV/JSON/PDF loading when schema and samples are enough, or large chat output when a file artifact is the right delivery surface.

### Innovation Points

- Goal-preserving interruption: the skill only pauses when the same final outcome can be reached through a better path.
- Meaningless-cost distinction: it separates justified high token use from avoidable waste.
- Four-level gate: high-risk detection, avoidability, equivalent path, and interruption value must all pass.
- Path-constraint awareness: suggested paths, default paths, and hard constraints are handled differently.
- Deterministic preprocessing bias: indexing, filtering, sampling, diffing, and extraction happen before model-context spending.
- Silent default: normal tasks proceed without token-cost commentary.
- Acceptance-criteria firewall: cheaper paths are rejected if they weaken correctness, completeness, auditability, or output quality.

### Recommended Use

Install Token Gate globally when agents frequently handle:

- repository or multi-file analysis
- large logs and stack traces
- CSV, JSON, XML, PDF, or OCR workflows
- large generated artifacts
- repeated context across turns
- subagent-heavy planning or review
- debugging based on diffs, changed files, entrypoints, or failing traces

### Not Recommended

Do not use Token Gate to shrink the user's goal or avoid necessary work.

Do not interrupt when the user explicitly requests exhaustive review, complete documentation, line-by-line analysis, compliance-grade audit, or full artifact generation.

Do not use it when the alternative path is speculative, marginally cheaper, or less auditable.

### Installation

Copy the `token-gate` directory into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R token-gate "$CODEX_HOME/skills/token-gate"
```

If `CODEX_HOME` is not set, use your local Codex home path, commonly `~/.codex`.

### Files

- `token-gate/SKILL.md`: the skill instructions and decision gate.
- `token-gate/agents/openai.yaml`: UI metadata for the skill.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Token Gate 是一个面向 Codex 风格编码代理的静默执行前 skill。

公开仓库名为 `Token-Gate_Skill`。可安装的 Codex skill 名称仍为 `token-gate`。

它会在高成本任务开始前拦截可避免的模型上下文浪费，同时保持用户原始目标、交付物、质量标准和验收条件不变。

### 为什么重要

大 token 消耗并不天然错误。完整审计、完整交付物生成、合规任务和穷尽式 review 可能确实需要较大的上下文预算。

Token Gate 只治理无意义的 token 消耗：例如索引足够时仍全文读取仓库、过滤 trace 足够时仍整段吞日志、schema 和样例足够时仍直接加载原始 CSV/JSON/PDF，或应该写文件却把大产物直接贴进对话。

### 创新点

- 目标保持型打断：只有同一个最终结果可以通过更优路径达成时，才允许暂停。
- 无意义成本区分：区分必要的高 token 使用和可避免浪费。
- 四层门禁：高风险识别、可避免性、等价路径、打断价值都必须成立。
- 路径约束感知：区分用户建议路径、默认路径和硬约束。
- 确定性预处理优先：先用索引、过滤、采样、diff、抽取缩小范围，再消耗模型上下文。
- 默认静默：普通任务不会被 token 成本说明打断。
- 验收标准防火墙：如果更便宜路径削弱正确性、完整性、可审计性或输出质量，就拒绝替代。

### 推荐使用

当代理经常处理以下任务时，建议全局安装 Token Gate：

- 仓库或多文件分析
- 大日志和 stack trace
- CSV、JSON、XML、PDF 或 OCR 工作流
- 大型生成产物
- 多轮重复上下文
- 大量 subagent 规划或 review
- 基于 diff、变更文件、入口文件或失败 trace 的调试

### 不推荐使用

不要用 Token Gate 缩小用户目标或逃避必要工作。

当用户明确要求穷尽式 review、完整文档、逐行分析、合规级审计或完整产物生成时，不要因节省 token 而打断。

当替代路径只是推测性、更省一点点、或可审计性更差时，不要使用。

### 安装

将 `token-gate` 目录复制到 Codex skills 目录：

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R token-gate "$CODEX_HOME/skills/token-gate"
```

如果没有设置 `CODEX_HOME`，使用本地 Codex home 路径，通常是 `~/.codex`。

### 文件

- `token-gate/SKILL.md`：skill 指令和决策门禁。
- `token-gate/agents/openai.yaml`：skill 的 UI metadata。

### License

当前 release 尚未选择开源许可证。除非仓库 owner 后续添加 license，否则按 all rights reserved 处理。
