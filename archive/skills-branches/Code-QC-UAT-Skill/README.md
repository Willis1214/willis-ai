# Code-QC-UAT

## English

Code-QC-UAT is a Codex skill for executable code QC/UAT on Python, Perl, Tcl, Shell, and similar runnable scripts or repositories.

It focuses on functional scenarios, common user workflows, boundary inputs, regression probes, and evidence-backed release gating. It can create temporary test scripts and execute the real target program, but all QC artifacts must stay under the target workspace `qc_uat/` directory.

### What It Does

- Discovers the target entrypoint, language, runtime command, and input/output contract.
- Builds functional golden-path scenarios before robustness checks.
- Adds boundary, malformed-input, encoding, path, and regression cases when relevant.
- Creates executable QC runners under `qc_uat/engineer/`.
- Executes the real target program and records command output under `qc_uat/logs/`.
- Writes the final gate report to `qc_uat/qc_uat_result.md`.

### When To Use It

Use this skill when you need:

- QC or UAT for runnable source code
- functional validation for a script, CLI tool, parser, converter, or data processor
- boundary-condition testing
- regression checks after a bug fix or code change
- crash hunting against real code paths
- a strict `Pass`, `Fail`, or `Reject` release gate

### When Not To Use It

Do not use this skill for:

- pure static code review without execution
- document, PPT, image, or non-code artifact review
- general adversarial critique of plans or PRDs
- security penetration testing beyond lightweight code robustness probes
- tasks where the target entrypoint or expected behavior is unknown and cannot be clarified

### Installation

Open the `Code-QC-UAT-Skill` branch in `Willis1214/Skills`, then copy `code-qc-uat/` into your Codex skills directory.

Recommended local path:

```text
$CODEX_HOME/skills/code-qc-uat
```

### Usage Prompt

```text
Use $code-qc-uat to run executable code QC/UAT for this target program.
```

### Repository Contents

- `code-qc-uat/SKILL.md`: skill instructions, trigger boundaries, execution contract, report format, and gate rules.
- `code-qc-uat/agents/openai.yaml`: Codex app display metadata.
- `code-qc-uat/references/qc-scenario-patterns.md`: reusable functional, boundary, path, encoding, regression, and language-specific QC patterns.
- `code-qc-uat/scripts/scaffold_qc_uat.py`: creates the target workspace `qc_uat/` structure.
- `code-qc-uat/scripts/generate_synthetic_cases.py`: generates reusable seed cases under `qc_uat/testcases/`.
- `manifest.json`: release metadata for this public skill branch.
- `REVISION_HISTORY.md`: version history.

### Release Notes

#### v1.1.0 - 2026-05-18

- Renamed the installable skill to `code-qc-uat` and display name to `Code-QC-UAT`.
- Refocused the workflow from broad red-team attack testing to executable code functional QC/UAT.
- Keeps Python, Perl, Tcl, Shell, CLI tools, parsers, converters, and data processors as the primary targets.
- Allows temporary QC runners to be generated and executed against the real target program.
- Requires all intermediate files, test cases, logs, and final reports to stay under `qc_uat/`.
- Simplified the final report path to `qc_uat/qc_uat_result.md`.

### Safety and Boundaries

- The skill does not modify source code unless the user explicitly asks for fixes.
- All QC artifacts are isolated under `qc_uat/`.
- It must not claim `Pass` unless the relevant functional and boundary checks were actually executed.
- It separates observed evidence from inferred risk.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Code-QC-UAT 是一个 Codex skill，用于对 Python、Perl、Tcl、Shell 以及类似可运行脚本或仓库进行可执行代码 QC/UAT。

它重点关注功能场景、常见用户流程、边界输入、回归探针和有证据支撑的发布 gate。它允许生成临时测试脚本并真实执行目标程序，但所有 QC 产物都必须保留在目标工作区的 `qc_uat/` 目录下。

### 它做什么

- 识别目标入口、语言、运行命令和输入/输出契约。
- 先构建功能 golden-path 场景，再做鲁棒性检查。
- 按需加入边界、脏输入、编码、路径和回归用例。
- 在 `qc_uat/engineer/` 下创建可执行 QC runner。
- 真实执行目标程序，并把命令输出记录到 `qc_uat/logs/`。
- 将最终 gate 报告写入 `qc_uat/qc_uat_result.md`。

### 什么时候使用

适用于：

- 对可运行源码做 QC 或 UAT
- 验证脚本、CLI 工具、parser、converter 或数据处理程序的功能
- 边界条件测试
- bug 修复或代码变更后的回归检查
- 针对真实代码路径的崩溃排查
- 需要严格 `Pass`、`Fail` 或 `Reject` 发布结论

### 什么时候不使用

不适用于：

- 不执行代码的纯静态源码审查
- 文档、PPT、图片或非代码产物审查
- 对方案或 PRD 的通用攻击式审查
- 超出轻量代码鲁棒性探针范围的安全渗透测试
- 无法确认目标入口或预期行为的任务

### 安装

打开 `Willis1214/Skills` 仓库的 `Code-QC-UAT-Skill` 分支，然后把 `code-qc-uat/` 复制到本地 Codex skills 目录。

推荐本地路径：

```text
$CODEX_HOME/skills/code-qc-uat
```

### 使用 Prompt

```text
Use $code-qc-uat to run executable code QC/UAT for this target program.
```

### 仓库内容

- `code-qc-uat/SKILL.md`: skill 指令、触发边界、执行契约、报告格式和 gate 规则。
- `code-qc-uat/agents/openai.yaml`: Codex app 展示 metadata。
- `code-qc-uat/references/qc-scenario-patterns.md`: 可复用的功能、边界、路径、编码、回归和语言特定 QC 模式。
- `code-qc-uat/scripts/scaffold_qc_uat.py`: 创建目标工作区 `qc_uat/` 结构。
- `code-qc-uat/scripts/generate_synthetic_cases.py`: 在 `qc_uat/testcases/` 下生成可复用 seed cases。
- `manifest.json`: 公开 skill 分支 release metadata。
- `REVISION_HISTORY.md`: 版本历史。

### Release Notes

#### v1.1.0 - 2026-05-18

- 安装名改为 `code-qc-uat`，展示名改为 `Code-QC-UAT`。
- 从宽泛红队攻击测试收敛为可执行代码功能 QC/UAT。
- 主要目标限定为 Python、Perl、Tcl、Shell、CLI 工具、parser、converter 和数据处理程序。
- 允许生成临时 QC runner 并真实执行目标程序。
- 要求所有中间文件、testcase、日志和最终报告都保留在 `qc_uat/`。
- 最终报告路径简化为 `qc_uat/qc_uat_result.md`。

### 安全与边界

- 除非用户明确要求修复，否则该 skill 不修改源代码。
- 所有 QC 产物隔离在 `qc_uat/`。
- 未真实执行相关功能和边界检查时，不得声称 `Pass`。
- 必须区分已观测证据和推断风险。

### License

本版本未选择开源 License。除非仓库所有者后续添加 License，否则按 all rights reserved 处理。
