# Skill Cleaner

只读审计 Skill 根目录、重复包、使用情况和清理候选。

## 版本与状态

源版本：`1.0.0`。2026-10-07 从旧 `Skill-Cleaner-Skill` 分支迁入 Willis AI 集合；方法保持原分支版本，迁移侧路径适配见来源索引。历史前身与衍生包分别保留，不用迁移日期冒充新业务版本。

## 安装

下载本仓库并复制本目录到宿主的 Skill 目录，例如 Codex 的 `~/.codex/skills/skill-cleaner/`（自定义 CODEX_HOME 时使用对应目录）。复制整个目录，入口为 `SKILL.md`。已有同名包时先保存现有版本，再替换目录，避免新旧文件混用。

```bash
(
  set -e
  task_checkout=$(mktemp -d "${TMPDIR:-/tmp}/willis-ai-install.XXXXXX")
  git clone --depth 1 https://github.com/Willis1214/willis-ai.git "$task_checkout/repo"
  task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
  task_destination="$task_skill_root/skill-cleaner"
  mkdir -p "$task_skill_root"
  if [ -e "$task_destination" ]; then
    task_backup_root="${CODEX_HOME:-$HOME/.codex}/skill-backups"
    mkdir -p "$task_backup_root"
    task_backup=$(mktemp -d "$task_backup_root/skill-cleaner.XXXXXX")
    mv "$task_destination" "$task_backup/skill-cleaner"
    printf '已有版本保存到：%s\n' "$task_backup/skill-cleaner"
  fi
  cp -R "$task_checkout/repo/skill-cleaner" "$task_destination"
  test -f "$task_destination/SKILL.md"
  printf '已安装到：%s\n' "$task_destination"
)
```

安装后让宿主重新加载 Skill。运行前阅读 [完整方法与边界](SKILL.md)；环境和其他 Skill 依赖以原方法说明为准。

## 使用入口

```text
Use $skill-cleaner to audit loaded Codex/OpenClaw skills, duplicate skill copies, unused skills from recent logs, and compact description candidates. 输出给用户的结论、风险和建议必须使用中文；默认只生成报告，不自动删除、禁用或改写任何 skill。 For low-risk report triage, delegate a bounded sidecar task to default subagent with model gpt-5.4-mini.
```

## 版本沿革与来源

- [原分支说明](../archive/skills-branches/Skill-Cleaner-Skill/README.md)
- [原版本元数据](../archive/skills-branches/Skill-Cleaner-Skill/manifest.json)
- [集合迁移说明](../MIGRATION.md)
- [原文件与历史映射](../migration/skills-branches-2026-10-07.json)

来源：`Willis1214/Skills` / `Skill-Cleaner-Skill` / `066b1f10218b4a801e77715d69b4f6e16eada455`。完整旧 Git 历史保留在 `skills-archive-Skill-Cleaner-Skill-2026-10-07` 标签下。历史原件中的旧仓库安装命令仅供追溯，当前安装使用上面的集合地址。

## 许可

原分支未指定开源许可；迁移未新增授权。其他包的许可不适用于本包。
