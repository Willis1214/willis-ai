# Delivery diagnosis

## Status meanings

| State | Evidence | Meaning |
| --- | --- | --- |
| `failed` | `error != 0` | Messages could not submit the message to the selected iMessage route. Check the recipient address and iMessage registration. |
| `pending` | No error, `is_sent = 0` | The Mac recorded the message but has not sent it yet. Check network and Messages sign-in. |
| `sent` | `is_sent = 1`, `is_delivered = 0` | The Mac submitted the message; recipient-side arrival is not yet confirmed. |
| `delivered` | `is_delivered = 1` | The iMessage service recorded delivery. This is not the same as a user reading the message. |

## Self-test does not appear on iPhone

1. Run `status` and confirm the Messages database is readable.
2. In Messages on both Mac and iPhone, confirm the same Apple Account is signed in and Messages in iCloud is enabled or syncing.
3. Check `self-test` output. An AppleScript success alone is insufficient; use `sent`, `delivered`, and `error`.
4. If the message is `delivered` but not visibly surfaced on the iPhone, open the self conversation on the iPhone and allow sync time. Do not repeatedly resend a test message.

## Recipient failure

- A contact card is not required. Use the exact E.164 phone number or registered Apple Account email.
- If Messages marks the number as not registered for iMessage, the receiver must enable iMessage and activate that number or email under Send & Receive.
- An Android phone cannot receive iMessage. This Skill does not automatically downgrade to SMS/RCS.

## SMS/RCS boundary

SMS, MMS, and RCS are carrier services. A Mac can use them only after the owner configures iPhone Text Message Forwarding and the carrier/region supports the route. Any such send may consume the iPhone plan or incur carrier charges. Treat it as a separate, explicit user-approved transport.
