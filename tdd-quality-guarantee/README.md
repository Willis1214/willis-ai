# TDD Quality Guarantee

整理详细测试场景、执行证据及 Spec 对应关系。

## 版本与状态

源版本：`1.0.0`。2026-10-07 从旧 `TDD-Quality-Guarantee-Skill` 分支迁入 Willis AI 集合；方法保持原分支版本，迁移侧路径适配见来源索引。历史前身与衍生包分别保留，不用迁移日期冒充新业务版本。

## 安装

下载本仓库并复制本目录到宿主的 Skill 目录，例如 Codex 的 `~/.codex/skills/tdd-quality-guarantee/`（自定义 CODEX_HOME 时使用对应目录）。复制整个目录，入口为 `SKILL.md`。已有同名包时先保存现有版本，再替换目录，避免新旧文件混用。

```bash
(
  set -e
  task_checkout=$(mktemp -d "${TMPDIR:-/tmp}/willis-ai-install.XXXXXX")
  git clone --depth 1 https://github.com/Willis1214/willis-ai.git "$task_checkout/repo"
  task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
  task_destination="$task_skill_root/tdd-quality-guarantee"
  mkdir -p "$task_skill_root"
  if [ -e "$task_destination" ]; then
    task_backup_root="${CODEX_HOME:-$HOME/.codex}/skill-backups"
    mkdir -p "$task_backup_root"
    task_backup=$(mktemp -d "$task_backup_root/tdd-quality-guarantee.XXXXXX")
    mv "$task_destination" "$task_backup/tdd-quality-guarantee"
    printf '已有版本保存到：%s\n' "$task_backup/tdd-quality-guarantee"
  fi
  cp -R "$task_checkout/repo/tdd-quality-guarantee" "$task_destination"
  test -f "$task_destination/SKILL.md"
  printf '已安装到：%s\n' "$task_destination"
)
```

安装后让宿主重新加载 Skill。运行前阅读 [完整方法与边界](SKILL.md)；环境和其他 Skill 依赖以原方法说明为准。

## 使用入口

```text
Use $tdd-quality-guarantee when the user explicitly requests TDD Quality Guarantee for a task.
```

## 版本沿革与来源

- [原分支说明](../archive/skills-branches/TDD-Quality-Guarantee-Skill/README.md)
- [原版本元数据](../archive/skills-branches/TDD-Quality-Guarantee-Skill/manifest.json)
- [集合迁移说明](../MIGRATION.md)
- [原文件与历史映射](../migration/skills-branches-2026-10-07.json)

来源：`Willis1214/Skills` / `TDD-Quality-Guarantee-Skill` / `4b490dba9362942a01c8907c2a6d08135ba8ff52`。完整旧 Git 历史保留在 `skills-archive-TDD-Quality-Guarantee-Skill-2026-10-07` 标签下。历史原件中的旧仓库安装命令仅供追溯，当前安装使用上面的集合地址。

## 许可

原分支未指定开源许可；迁移未新增授权。其他包的许可不适用于本包。
