#!/usr/bin/env python3
"""Local, evidence-oriented Messages.app helper. No network calls or credentials."""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CHAT_DB = Path.home() / "Library" / "Messages" / "chat.db"
MAX_FILE_BYTES = 100 * 1024 * 1024


def emit(value: dict) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True))


def normalize_phone(value: str) -> str:
    raw = re.sub(r"[\s()-]", "", value or "")
    if not re.fullmatch(r"\+\d{6,15}", raw):
        raise ValueError("phone number must be E.164, for example +8613812345678")
    return raw


def db_connection() -> sqlite3.Connection:
    if not CHAT_DB.is_file():
        raise RuntimeError(f"Messages database not found: {CHAT_DB}")
    try:
        return sqlite3.connect(f"file:{CHAT_DB}?mode=ro", uri=True)
    except sqlite3.Error as error:
        raise RuntimeError("cannot read chat.db; grant Full Disk Access to the host app or terminal") from error


def verify_db() -> None:
    try:
        with db_connection() as conn:
            conn.execute("SELECT ROWID FROM message LIMIT 1").fetchone()
    except sqlite3.Error as error:
        raise RuntimeError("cannot read chat.db; grant Full Disk Access to the host app or terminal") from error


def self_handle() -> str:
    sql = """
    SELECT lower(h.id)
    FROM message AS m
    JOIN handle AS h ON h.ROWID = m.handle_id
    WHERE m.is_from_me = 1
      AND m.account IS NOT NULL
      AND m.account <> ''
      AND lower(h.id) = lower(
        CASE WHEN m.account GLOB '[A-Za-z]:*' THEN substr(m.account, 3) ELSE m.account END
      )
    ORDER BY m.date DESC
    LIMIT 1
    """
    with db_connection() as conn:
        row = conn.execute(sql).fetchone()
    if not row:
        raise RuntimeError("no local iMessage address found; send yourself one iMessage in Messages.app first")
    return str(row[0])


def run_osascript(script: str, args: list[str]) -> None:
    result = subprocess.run(["osascript", "-", *args], input=script, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"osascript exited {result.returncode}")


def send_to_chat(chat_guid: str, text: str) -> None:
    run_osascript(
        "on run argv\n  tell application \"Messages\" to send (item 1 of argv) to chat id (item 2 of argv)\nend run",
        [text, chat_guid],
    )


def send_to_handle(handle: str, text: str) -> None:
    run_osascript(
        "on run argv\n  tell application \"Messages\"\n    set targetService to first service whose service type is iMessage\n    set targetBuddy to buddy (item 1 of argv) of targetService\n    send (item 2 of argv) to targetBuddy\n  end tell\nend run",
        [handle, text],
    )


def send_file_to_handle(handle: str, file_path: Path) -> None:
    run_osascript(
        "on run argv\n  tell application \"Messages\"\n    set targetService to first service whose service type is iMessage\n    set targetBuddy to buddy (item 1 of argv) of targetService\n    send (POSIX file (item 2 of argv)) to targetBuddy\n  end tell\nend run",
        [handle, str(file_path)],
    )


def matching_message(text: str, handle: str | None = None) -> dict | None:
    clauses = ["m.is_from_me = 1", "(m.text = ? OR instr(m.attributedBody, CAST(? AS BLOB)) > 0)"]
    params: list[object] = [text, text]
    if handle:
        clauses.append("replace(replace(replace(h.id, '+', ''), ' ', ''), '-', '') = ?")
        params.append(handle.lstrip("+"))
    sql = f"""
    SELECT m.service, m.is_sent, m.is_delivered, m.error,
           CASE WHEN m.date_delivered > 0 THEN 1 ELSE 0 END AS has_delivery_time
    FROM message AS m
    LEFT JOIN handle AS h ON h.ROWID = m.handle_id
    WHERE {' AND '.join(clauses)}
    ORDER BY m.ROWID DESC LIMIT 1
    """
    with db_connection() as conn:
        row = conn.execute(sql, params).fetchone()
    if not row:
        return None
    service, sent, delivered, error, has_delivery_time = row
    if error:
        state = "failed"
    elif delivered:
        state = "delivered"
    elif sent:
        state = "sent"
    else:
        state = "pending"
    return {"state": state, "service": service, "is_sent": bool(sent), "is_delivered": bool(delivered), "error": int(error or 0), "has_delivery_time": bool(has_delivery_time)}


def wait_for_status(text: str, handle: str | None, timeout: int) -> dict:
    deadline = time.monotonic() + timeout
    latest = None
    while time.monotonic() <= deadline:
        latest = matching_message(text, handle)
        # "sent" is only local transport acceptance.  Keep polling within the
        # requested window so a later delivery receipt is not lost.
        if latest and latest["state"] in {"failed", "delivered"}:
            return latest
        time.sleep(1)
    return latest or {"state": "not_recorded", "service": None, "is_sent": False, "is_delivered": False, "error": 0, "has_delivery_time": False}


def command_status(_: argparse.Namespace) -> int:
    verify_db()
    handle = self_handle()
    emit({"ok": True, "chat_db_readable": True, "self_chat_found": True, "self_handle": handle})
    return 0


def command_self_test(args: argparse.Namespace) -> int:
    verify_db()
    message = f"Willis x AI self-test {datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    handle = self_handle()
    send_to_handle(handle, message)
    status = wait_for_status(message, handle, args.timeout)
    emit({"ok": status["state"] in {"sent", "delivered"}, "kind": "self_test", "message_id": message.rsplit(" ", 1)[-1], "status": status})
    return 0 if status["state"] in {"sent", "delivered"} else 2


def command_send(args: argparse.Namespace) -> int:
    verify_db()
    handle = normalize_phone(args.to)
    send_to_handle(handle, args.text)
    status = wait_for_status(args.text, handle, args.timeout)
    emit({"ok": status["state"] in {"sent", "delivered"}, "kind": "send", "to": handle, "status": status})
    return 0 if status["state"] in {"sent", "delivered"} else 2


def command_send_file(args: argparse.Namespace) -> int:
    verify_db()
    handle = normalize_phone(args.to)
    file_path = Path(args.file).expanduser().resolve()
    if not file_path.is_file():
        raise RuntimeError("file must be an existing regular file")
    if file_path.stat().st_size > MAX_FILE_BYTES:
        raise RuntimeError("file exceeds 100 MiB limit")
    send_file_to_handle(handle, file_path)
    emit({"ok": True, "kind": "send_file", "to": handle, "file_name": file_path.name, "bytes": file_path.stat().st_size, "status": "accepted_by_messages_app"})
    return 0


def command_read(args: argparse.Namespace) -> int:
    verify_db()
    limit = max(1, min(args.limit, 100))
    sql = """
    SELECT m.is_from_me, m.service, m.text
    FROM message AS m
    JOIN chat_message_join AS cmj ON cmj.message_id = m.ROWID
    JOIN chat AS c ON c.ROWID = cmj.chat_id
    WHERE c.guid = ? ORDER BY m.date DESC LIMIT ?
    """
    with db_connection() as conn:
        rows = conn.execute(sql, (args.chat_guid, limit)).fetchall()
    emit({"ok": True, "chat_guid": args.chat_guid, "messages": [{"from_me": bool(row[0]), "service": row[1], "text": row[2] or ""} for row in reversed(rows)]})
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local macOS iMessage gateway")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status").set_defaults(func=command_status)
    self_test = sub.add_parser("self-test")
    self_test.add_argument("--timeout", type=int, default=15)
    self_test.set_defaults(func=command_self_test)
    send = sub.add_parser("send")
    send.add_argument("--to", required=True)
    send.add_argument("--text", required=True)
    send.add_argument("--timeout", type=int, default=15)
    send.set_defaults(func=command_send)
    send_file = sub.add_parser("send-file")
    send_file.add_argument("--to", required=True)
    send_file.add_argument("--file", required=True)
    send_file.set_defaults(func=command_send_file)
    read = sub.add_parser("read")
    read.add_argument("--chat-guid", required=True)
    read.add_argument("--limit", type=int, default=20)
    read.set_defaults(func=command_read)
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (RuntimeError, ValueError) as error:
        emit({"ok": False, "error": str(error)})
        return 2


if __name__ == "__main__":
    sys.exit(main())
