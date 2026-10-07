# Code-QC-UAT

为可执行程序设计并运行功能、边界和回归检查。

## 版本与状态

源版本：`1.1.0`。2026-10-07 从旧 `Code-QC-UAT-Skill` 分支迁入 Willis AI 集合；方法保持原分支版本，迁移侧路径适配见来源索引。历史前身与衍生包分别保留，不用迁移日期冒充新业务版本。

## 安装

下载本仓库并复制本目录到宿主的 Skill 目录，例如 Codex 的 `~/.codex/skills/code-qc-uat/`（自定义 CODEX_HOME 时使用对应目录）。复制整个目录，入口为 `SKILL.md`。已有同名包时先保存现有版本，再替换目录，避免新旧文件混用。

```bash
(
  set -e
  task_checkout=$(mktemp -d "${TMPDIR:-/tmp}/willis-ai-install.XXXXXX")
  git clone --depth 1 https://github.com/Willis1214/willis-ai.git "$task_checkout/repo"
  task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
  task_destination="$task_skill_root/code-qc-uat"
  mkdir -p "$task_skill_root"
  if [ -e "$task_destination" ]; then
    task_backup_root="${CODEX_HOME:-$HOME/.codex}/skill-backups"
    mkdir -p "$task_backup_root"
    task_backup=$(mktemp -d "$task_backup_root/code-qc-uat.XXXXXX")
    mv "$task_destination" "$task_backup/code-qc-uat"
    printf '已有版本保存到：%s\n' "$task_backup/code-qc-uat"
  fi
  cp -R "$task_checkout/repo/code-qc-uat" "$task_destination"
  test -f "$task_destination/SKILL.md"
  printf '已安装到：%s\n' "$task_destination"
)
```

安装后让宿主重新加载 Skill。运行前阅读 [完整方法与边界](SKILL.md)；环境和其他 Skill 依赖以原方法说明为准。

## 使用入口

```text
Use $code-qc-uat to run executable code QC/UAT. Create all QC artifacts under qc_uat/, execute the target program with functional and boundary cases, and report a strict Pass/Fail/Reject gate.
```

## 版本沿革与来源

- [原分支说明](../archive/skills-branches/Code-QC-UAT-Skill/README.md)
- [原版本元数据](../archive/skills-branches/Code-QC-UAT-Skill/manifest.json)
- [集合迁移说明](../MIGRATION.md)
- [原文件与历史映射](../migration/skills-branches-2026-10-07.json)

来源：`Willis1214/Skills` / `Code-QC-UAT-Skill` / `e6c21aac914c8c5cf16427caf0a0769f1a63a482`。完整旧 Git 历史保留在 `archive/skills-branches/Code-QC-UAT-Skill/2026-10-07` 标签下。历史原件中的旧仓库安装命令仅供追溯，当前安装使用上面的集合地址。

## 许可

原分支未指定开源许可；迁移未新增授权。其他包的许可不适用于本包。
