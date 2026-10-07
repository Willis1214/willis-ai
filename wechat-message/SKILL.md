---
name: wechat-message
description: Send a message through the macOS desktop WeChat app using a fixed Computer Use / keyboard shortcut workflow. Use when the user asks Codex to send WeChat messages to a named contact without a bridge, API, wxauto, or private WeChat interface.
---

# Wechat Message

Use this skill only for desktop WeChat message sending through the visible macOS WeChat app. Do not use bridge services, WeChat private APIs, wxauto, or MCP message-sending servers.

## Required Inputs

Before touching WeChat, confirm both values are already known from the user's request or current task context:

- `<用户>`: the exact WeChat contact or group name to search.
- `<信息>`: the exact user-provided message body.

If either value is missing, ambiguous, or only inferable from the current WeChat window, abort before activating WeChat.

## Fixed Workflow

Use this exact path unless the user explicitly changes it:

1. Activate the desktop WeChat app.
2. Press `Cmd+F`.
3. Put `<用户>` on the clipboard.
4. Paste `<用户>`.
5. Press `Return`.
6. Put `<信息>` on the clipboard.
7. Paste `<信息>`.
8. Put this suffix on the clipboard:

```text


该消息由 AI 自主发送！
```

9. Paste the suffix.
10. Press `Return` to send.

## Abort Rules

Abort without sending when any of these happen:

- `<用户>` or `<信息>` is not available before the workflow starts.
- WeChat is not running and cannot be activated.
- WeChat shows an explicit logged-out, relogin, QR login, or account-security prompt.
- The workflow cannot complete due to a system permission, Computer Use, or Apple Events error.

If the user has requested a blind shortcut flow, do not add extra UI validation gates. Execute the fixed workflow and report workflow completion directly.

## Reporting

After execution, report one of:

- `已执行`: when the fixed workflow completed through the final `Return` keypress.
- `已中止`: when an abort rule was hit before the final `Return` keypress.

Do not perform a final Computer Use state readback solely to confirm the WeChat window, intended chat, or message bubble after the final `Return`. `已执行` means the required desktop shortcut chain completed; it is not a separate visual delivery confirmation.
