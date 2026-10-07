# Code Reviewer

## English

Code Reviewer is a Codex skill for static-text release review of source code, diffs, version comparisons, and Codex skill files.

It reviews only the supplied source text or explicitly referenced files. It does not run linters, interpreters, formatters, compilers, shell commands, or local environment probes. The report focuses on release risk, contract stability, semantic correctness, engineering quality, and a clear approval decision.

### What It Does

- Reviews source code, unified diffs, version comparisons, and `SKILL.md` files.
- Supports Python, Perl, Tcl, Shell, mixed-language snippets, and Codex skill instructions.
- Uses severity levels: `Critical`, `Warning`, and `Nitpick`.
- Produces a fixed `Source Code Release Review` report.
- Scores the review from 0 to 100.
- Issues one release decision: `通过`, `需备注说明后通过`, `需修改后再审`, or `拒绝`.

### When To Use It

Use this skill when you need:

- release approval review for source code
- static source-code review without executing the code
- review of a patch, diff, or version comparison
- review of a Codex skill file or skill workflow
- risk-ranked findings before accepting code for production

### When Not To Use It

Do not use this skill for:

- runnable QC/UAT against real code paths
- linting, formatting, compiling, or local test execution
- environment diagnosis
- PRD or requirement review
- automatic code modification

### Installation

Open the `Code-Reviewer-Skill` branch in `Willis1214/Skills`, then copy `code-reviewer/` into your Codex skills directory.

Recommended local path:

```text
$CODEX_HOME/skills/code-reviewer
```

### Usage Prompt

```text
Use $code-reviewer to perform a static-text release code review.
```

### Repository Contents

- `code-reviewer/SKILL.md`: skill instructions, trigger boundaries, review modes, severity rules, scoring, and output constraints.
- `code-reviewer/agents/openai.yaml`: Codex app display metadata.
- `code-reviewer/references/report-template.md`: mandatory report template.
- `code-reviewer/references/static-review-rubric.md`: scoring, modes, and language-specific review details.
- `manifest.json`: release metadata for this public skill branch.
- `REVISION_HISTORY.md`: version history.

### Release Notes

#### v1.0.0 - 2026-05-18

- Initial public release in the central `Willis1214/Skills` repository.
- Defines the `Code Reviewer` display name and `code-reviewer` installable skill name.
- Fixes the scope as static-text release review only.
- Adds the mandatory `Source Code Release Review` output template.
- Supports Python, Perl, Tcl, Shell, mixed-language snippets, and Codex skill files.
- Requires no scripts, local tools, runtime execution, network calls, or environment probes.

### Safety and Boundaries

- This skill does not modify source code.
- This skill does not run local tools or infer correctness from the current machine.
- If language/tool versions are not declared in the submitted text, the report must mark them as `未声明`.
- Findings must be evidence-backed and must not invent requirements that are not present in the source or user context.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Code Reviewer 是一个 Codex skill，用于对源码、diff、版本对比和 Codex skill 文件进行静态文本上线审查。

它只审查用户提供或明确引用的源码文本，不运行 lint、解释器、formatter、compiler、shell 命令或本机环境探测。报告重点关注上线风险、契约稳定性、语义正确性、工程质量和明确的上线结论。

### 它做什么

- 审查源码、unified diff、版本对比和 `SKILL.md` 文件。
- 支持 Python、Perl、Tcl、Shell、混合语言片段和 Codex skill 指令。
- 使用 `Critical`、`Warning`、`Nitpick` 风险等级。
- 输出固定 `Source Code Release Review` 报告。
- 给出 0 到 100 分评分。
- 给出一个上线结论：`通过`、`需备注说明后通过`、`需修改后再审` 或 `拒绝`。

### 什么时候使用

适用于：

- 源码上线前审查
- 不执行代码的静态源码审查
- patch、diff 或版本对比审查
- Codex skill 文件或 skill workflow 审查
- 接受代码前需要风险分级 findings

### 什么时候不使用

不适用于：

- 针对真实代码路径的可运行 QC/UAT
- lint、format、compile 或本地测试执行
- 环境诊断
- PRD 或需求审查
- 自动修改代码

### 安装

打开 `Willis1214/Skills` 仓库的 `Code-Reviewer-Skill` 分支，然后把 `code-reviewer/` 复制到本地 Codex skills 目录。

推荐本地路径：

```text
$CODEX_HOME/skills/code-reviewer
```

### 使用 Prompt

```text
Use $code-reviewer to perform a static-text release code review.
```

### 仓库内容

- `code-reviewer/SKILL.md`: skill 指令、触发边界、审查模式、风险等级、评分规则和输出约束。
- `code-reviewer/agents/openai.yaml`: Codex app 展示 metadata。
- `code-reviewer/references/report-template.md`: 强制报告模板。
- `code-reviewer/references/static-review-rubric.md`: 评分、模式和语言特定审查细则。
- `manifest.json`: 公开 skill 分支 release metadata。
- `REVISION_HISTORY.md`: 版本历史。

### Release Notes

#### v1.0.0 - 2026-05-18

- 首次发布到中央 `Willis1214/Skills` 仓库。
- 定义 `Code Reviewer` 展示名和 `code-reviewer` 安装名。
- 固定边界为纯静态文本上线审查。
- 增加强制 `Source Code Release Review` 输出模板。
- 支持 Python、Perl、Tcl、Shell、混合语言片段和 Codex skill 文件。
- 不需要脚本、本地工具、运行时执行、网络调用或环境探测。

### 安全与边界

- 该 skill 不修改源码。
- 该 skill 不运行本地工具，也不根据当前机器环境推断正确性。
- 如果提交文本中没有声明语言/工具版本，报告必须标记为 `未声明`。
- findings 必须有证据支撑，不得编造源码或用户上下文中不存在的需求。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
