# Willis x AI iMessage Gateway

## English

Willis x AI iMessage Gateway is a local macOS Codex Skill for using Messages.app with delivery evidence. It can run a Mac-to-iPhone self-test, send an explicitly approved iMessage, send a bounded file, and read only a specified conversation.

### What It Does

- Reads the local Messages database in read-only mode.
- Sends through the public AppleScript interface of Messages.app.
- Distinguishes `failed`, `pending`, `sent`, and `delivered` instead of treating a script exit code as delivery.
- Keeps SMS/MMS/RCS off by default and explains the Android/carrier boundary.

### Install

```bash
git clone --branch Willis-x-AI-iMessage-Gateway-Skill --single-branch https://github.com/Willis1214/Skills.git /tmp/willis-x-ai-imessage
mkdir -p ~/.codex/skills
cp -R /tmp/willis-x-ai-imessage/imessage-gateway ~/.codex/skills/imessage-gateway
```

Restart Codex after installation.

### Quick Start

```text
Use $imessage-gateway to run a Mac-to-iPhone iMessage self-test and explain the delivery state.
```

### Requirements

- macOS with Messages.app signed in to iMessage.
- Full Disk Access for the process that reads `~/Library/Messages/chat.db`.
- Automation permission when macOS asks to let the host control Messages.

### Safety

- Sends require a user-specified destination and exact content.
- Conversation reads require an explicit chat GUID; no bulk contact discovery or history export.
- Android phones do not receive iMessage. SMS/RCS needs a separately configured carrier route and explicit approval.

See `imessage-gateway/references/delivery-diagnosis.md` for delivery and Android troubleshooting.

## 中文

Willis x AI iMessage Gateway 是一个本地 macOS Codex Skill：通过 Messages.app 做有证据的 iMessage 操作。它支持 Mac 到 iPhone 自测、向明确收件人发送 iMessage、发送受限附件，以及按指定会话读取消息。

### 能做什么

- 只读访问本机 Messages 数据库。
- 通过 macOS 的公开 AppleScript 接口发送消息。
- 区分 `failed`、`pending`、`sent`、`delivered`，不把脚本无报错误当作送达。
- 默认关闭 SMS/MMS/RCS，明确安卓与运营商的边界。

### 安装

```bash
git clone --branch Willis-x-AI-iMessage-Gateway-Skill --single-branch https://github.com/Willis1214/Skills.git /tmp/willis-x-ai-imessage
mkdir -p ~/.codex/skills
cp -R /tmp/willis-x-ai-imessage/imessage-gateway ~/.codex/skills/imessage-gateway
```

安装后重启 Codex。

### 快速使用

```text
Use $imessage-gateway to run a Mac-to-iPhone iMessage self-test and explain the delivery state.
```

### 前提

- macOS，并在 Messages.app 登录 iMessage。
- 读取 `~/Library/Messages/chat.db` 的宿主程序已获“完全磁盘访问权限”。
- 首次发送时，按 macOS 提示允许宿主程序控制 Messages。

### 安全边界

- 发送必须由用户明确给出收件地址和内容。
- 读取必须指定 chat GUID；不批量扫描联系人或导出聊天记录。
- 安卓不支持 iMessage。SMS/RCS 需要独立的运营商路径和明确授权。

详见 `imessage-gateway/references/delivery-diagnosis.md`。

## License

MIT
