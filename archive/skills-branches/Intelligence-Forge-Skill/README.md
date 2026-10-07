# Intelligence Forge

## English

Intelligence Forge is a Codex skill for turning many same-domain professional files into a reusable `domain_intelligence.md`.

It is designed for domains where historical experience is scattered across runsets, configs, specs, reports, logs, cases, or similar file families. The skill first builds a draft understanding of the field and file type, then extracts and validates domain claims with evidence, counterexamples, user feedback, promotion gates, and explicit extraction boundaries.

### What It Does

- Starts with domain onboarding before reading private corpus files.
- Separates public prior, user brief, file-observed facts, user-confirmed rules, unresolved hypotheses, and rejected assumptions.
- Builds full manifests and shallow profiles so no file is invisible.
- Uses stratified deep-read planning to preserve rare subtypes, exceptions, and counterexamples.
- Routes claims through promotion gates instead of promoting plausible text too early.
- Preserves useful non-core knowledge as contextual rules, project overlays, subtype overlays, special cases, unknowns, or `Cannot infer` boundaries.
- Produces evidence-backed intelligence suitable as domain constraints for downstream AI work.

### When To Use It

Use this skill when you need to:

- learn a professional file domain from many related files;
- build a reusable `domain_intelligence.md`;
- extract architecture, workflow, dependency, naming, exception, or anti-pattern knowledge;
- decide which claims are general, contextual, special cases, contradicted, unknown, or cannot be inferred;
- incorporate user answers as supervised feedback and regression cases;
- avoid false generalization across projects, versions, tools, or lifecycle stages.

### When Not To Use It

Do not use this skill for:

- one-file summaries;
- ordinary RAG answers;
- generic knowledge notes without corpus-level validation;
- quick translations or rewrites;
- publishing private corpus excerpts without explicit permission.

### Installation

Open the `Intelligence-Forge-Skill` branch in this repository and copy the `intelligence-forge/` folder into your Codex skills directory:

```text
~/.codex/skills/intelligence-forge
```

### Usage Prompt

```text
Use $intelligence-forge to build a domain_intelligence.md from this professional corpus.
```

### Repository Contents

- `intelligence-forge/SKILL.md`: skill trigger, workflow, hard rules, output contract, and red-team review requirement.
- `intelligence-forge/agents/openai.yaml`: Codex app display metadata.
- `intelligence-forge/references/`: detailed contracts for onboarding, corpus stratification, promotion gates, sampling, prior audit, overlays, questions, anti-hallucination, and final artifacts.
- `intelligence-forge/scripts/`: deterministic helpers for manifesting, profiling, extracting candidate claims, scoring coverage, searching counterexamples, planning deep reads, blind validation, claim validation, question ledger rendering, feedback capture, and iteration reports.
- `manifest.json`: release metadata.
- `REVISION_HISTORY.md`: release history.

### Release Notes

#### v1.0.0 - 2026-06-11

- Initial public release.
- Adds Stage 0 domain onboarding and draft cognition before private corpus induction.
- Adds promotion gates, prior-contamination audit, stratified deep-read sampling, and core/overlay separation.
- Preserves under-proven knowledge instead of discarding it, while blocking unsafe `domain_core` and `validated_general` promotion.
- Adds local helper scripts for corpus inventory, candidate extraction, counterexample search, validation, question ledgers, and iteration reporting.

### Safety and Boundaries

- Public research is prior context, not corpus evidence.
- Model prose is not evidence.
- Special cases must not be silently promoted to general rules.
- Claims that fail high promotion lanes should be scoped or preserved, not deleted.
- Raw proprietary excerpts should be minimized and only used when explicitly allowed.
- Real-domain accuracy requires a pilot on real or sanitized corpus with user domain briefing.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Intelligence Forge 是一个 Codex skill，用于从大量同领域专业文件中沉淀可复用的 `domain_intelligence.md`。

它适合处理历史经验分散在 runset、配置、规格、报告、日志、案例或类似文件族中的场景。skill 会先建立领域和文件类型的 draft cognition，再用证据、反例、用户反馈、promotion gate 和抽取边界来验证领域知识。

### 它做什么

- 在读取私有 corpus 前先做领域进入。
- 区分 public prior、user brief、file-observed fact、user-confirmed rule、unresolved hypothesis 和 rejected assumption。
- 通过 manifest 和 shallow profile 保证没有文件隐形。
- 用分层 deep-read 规划保留稀有 subtype、例外和反例。
- 通过 promotion gate 控制 claim 升级，避免过早泛化。
- 将未充分证明但有价值的内容保留为 contextual rule、project overlay、subtype overlay、special case、unknown 或 `Cannot infer`。
- 输出可作为下游 AI domain constraint 的证据化 intelligence。

### 什么时候使用

适用于：

- 从大量相关文件中学习专业文件领域；
- 生成可复用 `domain_intelligence.md`；
- 抽取架构、流程、依赖、命名、例外和反模式；
- 判断 claim 是 general、contextual、special case、contradicted、unknown 还是 cannot infer；
- 把用户回答沉淀为监督反馈和 regression case；
- 避免跨项目、版本、工具或生命周期阶段的错误泛化。

### 什么时候不使用

不适用于：

- 单文件总结；
- 普通 RAG 问答；
- 不需要 corpus-level validation 的普通知识笔记；
- 快速翻译或改写；
- 未经明确授权发布私有 corpus 原文片段。

### 安装

打开本仓库的 `Intelligence-Forge-Skill` 分支，将 `intelligence-forge/` 文件夹复制到本地 Codex skills 目录：

```text
~/.codex/skills/intelligence-forge
```

### 使用 Prompt

```text
Use $intelligence-forge to build a domain_intelligence.md from this professional corpus.
```

### 仓库内容

- `intelligence-forge/SKILL.md`: skill 触发条件、工作流、硬规则、输出契约和红队审查要求。
- `intelligence-forge/agents/openai.yaml`: Codex app 展示 metadata。
- `intelligence-forge/references/`: onboarding、corpus 分层、promotion gate、sampling、prior audit、overlay、question ledger、反幻觉和最终产物契约。
- `intelligence-forge/scripts/`: manifest、profile、candidate claim 抽取、coverage、反例搜索、deep-read 规划、blind validation、claim validation、question ledger、feedback 和 iteration report 工具。
- `manifest.json`: release metadata。
- `REVISION_HISTORY.md`: 版本历史。

### Release Notes

#### v1.0.0 - 2026-06-11

- 首次公开发布。
- 增加 Stage 0 领域进入和 draft cognition。
- 增加 promotion gate、prior-contamination audit、分层 deep-read sampling 和 core/overlay 隔离。
- 对未充分证明的知识保留探索通道，同时阻止不安全的 `domain_core` 和 `validated_general` 升级。
- 增加本地 helper scripts，覆盖 corpus 盘点、候选知识抽取、反例搜索、验证、问题账本和迭代报告。

### 安全与边界

- 公开资料只是 prior context，不是 corpus evidence。
- 模型生成文字不是证据。
- special case 不能静默升级为 general rule。
- 高 promotion lane 失败的 claim 应被缩小范围或保留，而不是直接删除。
- proprietary raw excerpt 应最小化，并且只能在明确授权后使用。
- 真实领域准确性需要在真实或脱敏 corpus 上做 pilot，并结合用户领域 briefing。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
