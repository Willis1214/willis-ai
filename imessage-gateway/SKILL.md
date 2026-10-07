---
name: imessage-gateway
description: "Use when Codex needs to diagnose, read from, or send a user-approved iMessage through the local macOS Messages app. Trigger on Mac-to-iPhone iMessage self-tests, verified iMessage delivery status, or a clearly specified iMessage recipient and text/file. Do not use for Android SMS/RCS by default, bulk chat export, arbitrary contact discovery, or unapproved external sends."
---

# iMessage Gateway

Use this Skill to operate the local macOS Messages path with evidence, rather than treating a successful AppleScript call as delivery proof.

## Boundaries

- macOS and Messages.app are required. The terminal or host process needs Full Disk Access only for `chat.db` reads; the first send may require macOS Automation permission.
- Send only when the user has explicitly supplied the destination and exact text or file. Normalize phone numbers to E.164 format such as `+8613812345678`.
- Default transport is iMessage only. Do not silently fall back to SMS, MMS, or RCS. Android delivery is out of scope unless the user explicitly requests a separately configured carrier route.
- Read only a user-specified chat GUID. Do not enumerate or export the owner's private conversations merely to find a contact.
- A local `sent` or `delivered` record is evidence about the Mac/iMessage path, not a visual receipt from the recipient's device.

## Workflow

1. Run `python3 scripts/imessage_gateway.py status`. If database access fails, stop and explain the Full Disk Access fix.
2. For a Mac-to-iPhone check, run `self-test` and report `sent`, `delivered`, or `failed` from the returned JSON.
3. For an outgoing message, require a destination and exact content, then run `send --to <E164> --text <text>`. Confirm the resulting state before reporting success.
4. For a file, require an explicit absolute path and use `send-file`; the script rejects files above 100 MiB. Report only that Messages.app accepted the attachment unless a separate delivery record is available.
5. For history, use `read --chat-guid <GUID> --limit <N>` only after the user identifies the conversation scope.

## Commands

```bash
python3 scripts/imessage_gateway.py status
python3 scripts/imessage_gateway.py self-test --timeout 15
python3 scripts/imessage_gateway.py send --to +8613812345678 --text "你好"
python3 scripts/imessage_gateway.py send-file --to +8613812345678 --file /absolute/path/report.pdf
python3 scripts/imessage_gateway.py read --chat-guid 'iMessage;+;chat...' --limit 20
```

Read `references/delivery-diagnosis.md` when delivery is pending or failed, a self-test does not appear on iPhone, or the recipient uses Android.

## Verification

Run `python3 -m unittest discover -s test` from the package root for deterministic checks. A real send must be reported as `failed`, `pending`, `sent`, or `delivered`; never upgrade it to recipient confirmation without an authoritative receipt.
