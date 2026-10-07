# PM Consultant

需求咨询与 PRD 工作流的历史版本；后续演进见 Brainstorm。

## 版本与状态

源版本：`1.2.0`。2026-10-07 从旧 `PM-Consultant-Skill` 分支迁入 Willis AI 集合；方法保持原分支版本，迁移侧路径适配见来源索引。历史前身与衍生包分别保留，不用迁移日期冒充新业务版本。

## 安装

下载本仓库并复制本目录到宿主的 Skill 目录，例如 Codex 的 `~/.codex/skills/pm-consultant/`（自定义 CODEX_HOME 时使用对应目录）。复制整个目录，入口为 `SKILL.md`。已有同名包时先保存现有版本，再替换目录，避免新旧文件混用。

```bash
(
  set -e
  task_checkout=$(mktemp -d "${TMPDIR:-/tmp}/willis-ai-install.XXXXXX")
  git clone --depth 1 https://github.com/Willis1214/willis-ai.git "$task_checkout/repo"
  task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
  task_destination="$task_skill_root/pm-consultant"
  mkdir -p "$task_skill_root"
  if [ -e "$task_destination" ]; then
    task_backup_root="${CODEX_HOME:-$HOME/.codex}/skill-backups"
    mkdir -p "$task_backup_root"
    task_backup=$(mktemp -d "$task_backup_root/pm-consultant.XXXXXX")
    mv "$task_destination" "$task_backup/pm-consultant"
    printf '已有版本保存到：%s\n' "$task_backup/pm-consultant"
  fi
  cp -R "$task_checkout/repo/pm-consultant" "$task_destination"
  test -f "$task_destination/SKILL.md"
  printf '已安装到：%s\n' "$task_destination"
)
```

安装后让宿主重新加载 Skill。运行前阅读 [完整方法与边界](SKILL.md)；环境和其他 Skill 依赖以原方法说明为准。

涉及视觉质量时，原方法调用 `$front-taste`；该外部依赖未包含在本集合。

## 使用入口

```text
Use $pm-consultant to clarify requirements, including interaction and physical-world boundaries, build a user story map, confirm structured requirements, discuss QC checklist coverage, run a Red Team review and remediate high-risk findings, then output PRD Markdown, user-story-map HTML, and QC checklist Markdown without prescribing the implementation path.
```

## 版本沿革与来源

- [原分支说明](../archive/skills-branches/PM-Consultant-Skill/README.md)
- [原版本元数据](../archive/skills-branches/PM-Consultant-Skill/manifest.json)
- [集合迁移说明](../MIGRATION.md)
- [原文件与历史映射](../migration/skills-branches-2026-10-07.json)

来源：`Willis1214/Skills` / `PM-Consultant-Skill` / `ef29d53d833143cd6d76cb130120966093861586`。完整旧 Git 历史保留在 `archive/skills-branches/PM-Consultant-Skill/2026-10-07` 标签下。历史原件中的旧仓库安装命令仅供追溯，当前安装使用上面的集合地址。

## 许可

原分支未指定开源许可；迁移未新增授权。其他包的许可不适用于本包。
