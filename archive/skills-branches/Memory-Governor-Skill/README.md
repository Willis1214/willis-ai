# Memory Governor Skill

## English

Memory Governor is a Codex skill for long-term command memory governance.

The public branch name is `Memory-Governor-Skill`. The installable Codex skill name is `memory-governor`.

It detects durable user preferences, prohibitions, shortcuts, and workflow rules during normal work, asks the user for explicit approval, and writes approved rules into the long-term command memory file.

### What It Does

- Detects reusable long-term rule candidates from user wording.
- Classifies candidates as `preference`, `prohibition`, `shortcut`, or `workflow`.
- Uses a fixed approval prompt before any memory write.
- Writes approved entries into `~/.codex/memories/long-term-commands.md`.
- Initializes the long-term memory file when needed.
- Avoids duplicate entries by checking equivalent stored rules.

### Recommended Use

Install Memory Governor globally when Codex should preserve durable work rules across projects, but only after user approval.

Use it when the user says things like:

- `记住`
- `以后默认这样`
- `不要再这样`
- `以后别这么做`
- `写进长期记忆`

It is also useful when the same correction repeats and clearly applies beyond the current task.

### Not Recommended

Do not use Memory Governor for one-off task details, temporary complaints, transient debugging state, or project-local notes that should stay in the current task log.

Do not write to long-term memory without explicit user approval.

### Installation

Copy the `memory-governor` directory into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R memory-governor "$CODEX_HOME/skills/memory-governor"
```

If `CODEX_HOME` is not set, use your local Codex home path, commonly `~/.codex`.

### Files

- `memory-governor/SKILL.md`: the skill instructions and approval workflow.
- `memory-governor/agents/openai.yaml`: UI metadata for the skill.
- `memory-governor/scripts/append_memory_entry.py`: standard-library helper for initializing and appending approved memory entries.

### License

No open-source license has been selected in this release. Treat the contents as all rights reserved unless the repository owner adds a license.

---

## 中文

Memory Governor 是一个用于长期命令记忆治理的 Codex skill。

公开分支名为 `Memory-Governor-Skill`。可安装的 Codex skill 名称仍为 `memory-governor`。

它会在日常任务中识别可长期复用的用户偏好、禁令、捷径和工作流规则，先向用户请求明确批准，再把已批准规则写入长期命令记忆文件。

### 功能

- 识别可复用的长期规则候选。
- 将候选归类为 `preference`、`prohibition`、`shortcut` 或 `workflow`。
- 在任何写入前使用固定审批文案。
- 将已批准条目写入 `~/.codex/memories/long-term-commands.md`。
- 必要时初始化长期记忆文件。
- 通过等价规则检查避免重复写入。

### 推荐使用

当希望 Codex 在跨项目范围内保留稳定工作规则、但必须先经过用户批准时，建议全局安装 Memory Governor。

适合在用户表达以下意图时使用：

- `记住`
- `以后默认这样`
- `不要再这样`
- `以后别这么做`
- `写进长期记忆`

当同一纠正重复出现，并且明显超出当前任务范围时，也适合触发。

### 不推荐使用

不要把一次性任务细节、临时抱怨、调试状态或项目局部笔记写入长期记忆。

没有用户明确批准时，不得写入长期记忆。

### 安装

将 `memory-governor` 目录复制到 Codex skills 目录：

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R memory-governor "$CODEX_HOME/skills/memory-governor"
```

如果没有设置 `CODEX_HOME`，使用本地 Codex home 路径，通常是 `~/.codex`。

### 文件

- `memory-governor/SKILL.md`：skill 指令和审批流程。
- `memory-governor/agents/openai.yaml`：skill 的 UI metadata。
- `memory-governor/scripts/append_memory_entry.py`：用于初始化和追加已批准记忆条目的 Python 标准库 helper。

### License

当前 release 尚未选择开源许可证。除非仓库 owner 后续添加 license，否则按 all rights reserved 处理。
