# Notifications

Notifications keep users informed about events and changes — both in the moment (toasts) and over time (notification center). The goal is to surface relevant information without overwhelming.

---

## Toast notifications

Toasts are brief, non-blocking messages that appear temporarily at the edge of the screen to confirm an action or communicate a low-priority event.

### When to use toasts

- Confirming a successful action: "Connector saved."
- Notifying about a background event: "Import complete — 1,234 contacts added."
- Communicating a non-critical failure: "Couldn't save draft. Check your connection."

**Do not use toasts for:**

- Critical errors that block the user — use an [alert](../components/alerts.md) or [banner](../components/banners.md).
- Information the user explicitly requested — put it on the page.
- Actions that require the user to act on the notification.

---

### Toast variants

| Type | Usage | Color |
|------|-------|-------|
| **Success** | Action completed | Green `#2E7D32` |
| **Info** | Neutral update | `--ac-navy-mid` |
| **Warning** | Non-blocking issue | Amber `#F57C00` |
| **Error** | Non-blocking failure | Red `#D32F2F` |

```html
<div class="rc-toast-container" aria-live="polite" aria-atomic="false">

  <div class="rc-toast rc-toast--success" role="status">
    <span class="rc-toast__icon" aria-hidden="true">✓</span>
    <span class="rc-toast__message">Connector saved successfully.</span>
    <button class="rc-toast__dismiss" aria-label="Dismiss">✕</button>
  </div>

</div>
```

---

### Toast placement

| Position | Use case |
|----------|----------|
| **Bottom-right (default)** | General product notifications |
| **Bottom-center** | Mobile / narrow viewports |
| **Top-center** | System-level alerts (rare) |

Toasts should appear above dialogs and drawers (`z-index: var(--z-toast)`).

---

### Toast timing

| Type | Default duration |
|------|-----------------|
| Success | 4 seconds |
| Info | 5 seconds |
| Warning | 6 seconds |
| Error | Persistent (user must dismiss) |

Always provide a manual dismiss button regardless of auto-dismiss duration.

---

### Stacking

When multiple toasts appear in quick succession, stack them vertically with 8px gaps. Limit to 3 visible at a time — new toasts push out the oldest.

---

## Notification center

An in-app panel (often a drawer or dropdown) that collects notifications over time, allowing users to review them asynchronously.

### When to use a notification center

- Events happen frequently enough to need a history.
- Users miss toasts and need a way to catch up.
- Notifications require an action that may not be taken immediately.

### Notification item anatomy

```html
<li class="rc-notification rc-notification--unread">
  <div class="rc-notification__icon-wrap" aria-hidden="true">
    <span class="rc-avatar rc-avatar--sm">SF</span>
  </div>
  <div class="rc-notification__content">
    <p class="rc-notification__message">
      <strong>Salesforce sync paused.</strong>
      Your authentication token expired. Re-authenticate to resume.
    </p>
    <time class="rc-notification__time" datetime="2026-05-11T14:30:00Z">
      Today at 2:30 PM
    </time>
  </div>
  <a class="md-button md-button--sm" href="/connectors/salesforce/auth">
    Re-authenticate
  </a>
</li>
```

### Unread indicators

- Use a badge on the notification bell icon with the unread count.
- Mark individual items visually distinct (bold, colored left border, or dot indicator).
- "Mark all as read" appears when unread items are present.

---

## Notification content guidelines

| Principle | Guidance |
|-----------|----------|
| **Be specific** | "Salesforce sync paused" not "Sync issue" |
| **Include an action** | What should the user do? Link to it. |
| **Use relative time** | "2 minutes ago" for recent; absolute for older than 24h |
| **Group similar events** | "3 connectors have expired tokens" not 3 separate notifications |

---

## Email and external notifications

Out-of-app notifications (email, SMS, push) follow the same content guidelines:

- Subject / headline: specific, outcome-focused
- Body: what happened, what to do
- CTA: deep link to the relevant product page
- Footer: notification settings link + unsubscribe

!!! tip "Deep link everything"
    Every notification — toast, in-app, or email — should link directly to the specific record or action that triggered it. "Salesforce sync paused" should link to the Salesforce connector settings, not the dashboard.
