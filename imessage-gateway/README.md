# Willis x AI iMessage Gateway

在 macOS 上做限定会话读取、明确发送及 iMessage 状态核验。

## 版本与状态

源版本：`1.0.0`。2026-10-07 从旧 `Willis-x-AI-iMessage-Gateway-Skill` 分支迁入 Willis AI 集合；方法保持原分支版本，迁移侧路径适配见来源索引。历史前身与衍生包分别保留，不用迁移日期冒充新业务版本。

## 安装

下载本仓库并复制本目录到宿主的 Skill 目录，例如 Codex 的 `~/.codex/skills/imessage-gateway/`（自定义 CODEX_HOME 时使用对应目录）。复制整个目录，入口为 `SKILL.md`。已有同名包时先保存现有版本，再替换目录，避免新旧文件混用。

```bash
(
  set -e
  task_checkout=$(mktemp -d "${TMPDIR:-/tmp}/willis-ai-install.XXXXXX")
  git clone --depth 1 https://github.com/Willis1214/willis-ai.git "$task_checkout/repo"
  task_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
  task_destination="$task_skill_root/imessage-gateway"
  mkdir -p "$task_skill_root"
  if [ -e "$task_destination" ]; then
    task_backup_root="${CODEX_HOME:-$HOME/.codex}/skill-backups"
    mkdir -p "$task_backup_root"
    task_backup=$(mktemp -d "$task_backup_root/imessage-gateway.XXXXXX")
    mv "$task_destination" "$task_backup/imessage-gateway"
    printf '已有版本保存到：%s\n' "$task_backup/imessage-gateway"
  fi
  cp -R "$task_checkout/repo/imessage-gateway" "$task_destination"
  test -f "$task_destination/SKILL.md"
  printf '已安装到：%s\n' "$task_destination"
)
```

安装后让宿主重新加载 Skill。运行前阅读 [完整方法与边界](SKILL.md)；环境和其他 Skill 依赖以原方法说明为准。

需要 macOS 及对应消息应用/权限；安装包不包含账号、联系人或登录状态。

## 使用入口

```text
Use $imessage-gateway to run a Mac-to-iPhone iMessage self-test and explain the delivery state.
```

## 版本沿革与来源

- [原分支说明](../archive/skills-branches/Willis-x-AI-iMessage-Gateway-Skill/README.md)
- [原版本元数据](../archive/skills-branches/Willis-x-AI-iMessage-Gateway-Skill/manifest.json)
- [集合迁移说明](../MIGRATION.md)
- [原文件与历史映射](../migration/skills-branches-2026-10-07.json)

来源：`Willis1214/Skills` / `Willis-x-AI-iMessage-Gateway-Skill` / `34a35e88e1d3d958c2cfd2c14efbb0ae7ca06a87`。完整旧 Git 历史保留在 `archive/skills-branches/Willis-x-AI-iMessage-Gateway-Skill/2026-10-07` 标签下。历史原件中的旧仓库安装命令仅供追溯，当前安装使用上面的集合地址。

## 许可

原 manifest 声明 MIT，但源分支没有 LICENSE 文件。其他包的许可不适用于本包。
