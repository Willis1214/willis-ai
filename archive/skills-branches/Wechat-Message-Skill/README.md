# Wechat Message

## English

Wechat Message is a Codex skill for sending a prepared message through the visible macOS desktop WeChat app using a fixed keyboard shortcut workflow.

### What It Does

- Activates the desktop WeChat app.
- Searches for the requested contact or group with `Cmd+F`.
- Pastes the exact contact name.
- Opens the matched conversation with `Return`.
- Pastes the exact message body.
- Appends the fixed disclosure suffix:

```text


该消息由 AI 自主发送！
```

- Presses `Return` to send.
- Reports `已执行` after the fixed shortcut chain completes through the final `Return`.

### When To Use It

Use this skill when Codex needs to send a user-approved message to a known WeChat contact or group through the local macOS WeChat desktop app.

### When Not To Use It

Do not use this skill when:

- the contact or message body is missing or ambiguous;
- WeChat is logged out or blocked by an account-security prompt;
- the task requires WeChat private APIs, bridge services, `wxauto`, browser automation, or server-side message sending;
- the user requires visual delivery confirmation after sending.

### Install

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Willis1214/Wechat-Message-Skill.git /tmp/wechat-message-skill
cp -R /tmp/wechat-message-skill/wechat-message ~/.codex/skills/wechat-message
```

### Usage Prompt

```text
Use $wechat-message to send a desktop WeChat message to <用户> with <信息>.
```

### Repository Contents

```text
README.md
manifest.json
wechat-message/SKILL.md
wechat-message/agents/openai.yaml
```

### Safety Boundaries

This skill only uses visible desktop WeChat and keyboard/clipboard actions. It does not use WeChat private APIs, session extraction, browser cookies, bridges, or raw credentials.

The result `已执行` means the required shortcut chain completed. It is not a separate visual delivery confirmation.

### Release Notes

#### v1.0.0 - 2026-05-07

- Initial public release.
- Defines the fixed macOS desktop WeChat shortcut workflow.
- Uses `已执行` once the final `Return` keypress completes.
- Avoids final Computer Use readback solely for message-bubble confirmation.

### License Status

No open-source license file is included in this release. Unless the repository owner adds a license, all rights are reserved by default.

---

## 中文

Wechat Message 是一个 Codex skill，用于通过 macOS 桌面微信的固定键盘快捷链路发送已准备好的消息。

### 功能

- 激活桌面微信应用。
- 使用 `Cmd+F` 搜索指定联系人或群聊。
- 粘贴精确联系人名称。
- 使用 `Return` 打开匹配会话。
- 粘贴精确消息正文。
- 追加固定披露后缀：

```text


该消息由 AI 自主发送！
```

- 按 `Return` 发送。
- 固定快捷链路执行到最后一次 `Return` 后报告 `已执行`。

### 适用场景

当 Codex 需要通过本机 macOS 桌面微信向明确的微信联系人或群聊发送用户已批准的消息时，使用本 skill。

### 不适用场景

以下情况不要使用本 skill：

- 联系人或消息正文缺失、歧义或只能从当前微信窗口推断；
- 微信未登录，或出现重新登录、二维码、安全验证等阻断；
- 任务要求使用微信私有 API、桥接服务、`wxauto`、浏览器自动化或服务端发信；
- 用户要求发送后必须进行可视化送达确认。

### 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Willis1214/Wechat-Message-Skill.git /tmp/wechat-message-skill
cp -R /tmp/wechat-message-skill/wechat-message ~/.codex/skills/wechat-message
```

### 使用提示词

```text
Use $wechat-message to send a desktop WeChat message to <用户> with <信息>.
```

### 仓库内容

```text
README.md
manifest.json
wechat-message/SKILL.md
wechat-message/agents/openai.yaml
```

### 安全边界

本 skill 只使用可见桌面微信和键盘/剪贴板动作。不使用微信私有 API、会话提取、浏览器 cookie、桥接服务或原始凭证。

结果 `已执行` 表示必需的快捷链路已经完成，不等于额外的可视化送达确认。

### Release Notes

#### v1.0.0 - 2026-05-07

- 首次公开发布。
- 定义 macOS 桌面微信固定快捷链路。
- 最后一次 `Return` 完成后使用 `已执行` 作为结果。
- 不再为了确认消息气泡而执行最终 Computer Use 状态回读。

### 许可证状态

本版本未包含开源许可证文件。除非仓库所有者后续添加许可证，否则默认保留所有权利。
