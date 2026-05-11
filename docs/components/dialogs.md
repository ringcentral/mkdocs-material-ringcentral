# Dialogs

Dialogs interrupt the user's current task to request a decision or present focused information that cannot be deferred. Use them sparingly — each dialog is an interruption.

---

## When to use a dialog

Use a dialog when:

- The user needs to confirm a **destructive or irreversible action** (delete, disconnect, revoke).
- Completing the task requires **focused input** that would disrupt page context if done inline.
- A **critical alert** must be acknowledged before proceeding.

Do **not** use a dialog when:

- The user is just navigating — use a new page or a drawer.
- The content is informational only — use an alert or a tooltip.
- The form is complex with many steps — use a multi-step page or drawer instead.

---

## Variants

### Confirmation dialog

The most common dialog type. Presents a question and two actions: confirm and cancel.

```html
<dialog class="rc-dialog" aria-labelledby="dialog-title" aria-describedby="dialog-desc">
  <div class="rc-dialog__header">
    <h2 id="dialog-title">Delete Salesforce connector?</h2>
  </div>
  <div class="rc-dialog__body">
    <p id="dialog-desc">
      This will stop call logging and remove all sync settings.
      This cannot be undone.
    </p>
  </div>
  <div class="rc-dialog__actions">
    <button class="md-button" data-dialog-cancel>Cancel</button>
    <button class="md-button md-button--danger">Delete connector</button>
  </div>
</dialog>
```

### Form dialog

Contains a short form (2–4 fields). The primary action submits the form.

```html
<dialog class="rc-dialog rc-dialog--form" aria-labelledby="dialog-title">
  <div class="rc-dialog__header">
    <h2 id="dialog-title">Rename connector</h2>
    <button class="rc-dialog__close" aria-label="Close dialog">✕</button>
  </div>
  <div class="rc-dialog__body">
    <div class="rc-field">
      <label for="connector-name">Connector name</label>
      <input type="text" id="connector-name" value="My Salesforce" />
    </div>
  </div>
  <div class="rc-dialog__actions">
    <button class="md-button" data-dialog-cancel>Cancel</button>
    <button class="md-button md-button--primary">Save</button>
  </div>
</dialog>
```

### Alert dialog

For critical notices that require acknowledgment before continuing. No "cancel" option — only an acknowledgment action.

```html
<dialog
  class="rc-dialog rc-dialog--alert"
  role="alertdialog"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <div class="rc-dialog__body">
    <span class="rc-dialog__icon rc-dialog__icon--warning" aria-hidden="true">⚠️</span>
    <h2 id="dialog-title">Your session is about to expire</h2>
    <p id="dialog-desc">You'll be signed out in 2 minutes due to inactivity.</p>
  </div>
  <div class="rc-dialog__actions">
    <button class="md-button md-button--primary">Stay signed in</button>
  </div>
</dialog>
```

---

## Sizes

| Size | Width | Usage |
|------|-------|-------|
| Small | 400px | Simple confirmations, single-field forms |
| **Default** | 520px | **Standard dialogs** |
| Large | 680px | Multi-field forms, comparison views |
| Full-screen | 100vw / 100vh | Complex focused tasks (mobile only) |

---

## Anatomy

```
┌─────────────────────────────────┐
│ Header                    [✕]  │  ← Title + optional close button
│─────────────────────────────────│
│                                 │
│  Body content                   │  ← Description, form, or info
│                                 │
│─────────────────────────────────│
│         [Cancel]  [Confirm]     │  ← Actions (right-aligned)
└─────────────────────────────────┘
```

**Action order:** Cancel on the left, primary action on the right. For destructive actions, the primary button uses the danger variant.

---

## Backdrop and animation

Dialogs appear over a `rgba(0,0,0,0.4)` backdrop. They animate in with:

- Enter: `translateY(8px) → translateY(0)` + `opacity: 0 → 1`, 300ms `ease-decelerate`
- Exit: `translateY(0) → translateY(8px)` + `opacity: 1 → 0`, 200ms `ease-accelerate`

---

## Accessibility

Dialogs must trap focus while open and restore focus to the trigger element on close.

```javascript
// Minimal focus trap
dialog.addEventListener('keydown', (e) => {
  if (e.key !== 'Tab') return;
  const focusable = dialog.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last  = focusable[focusable.length - 1];

  if (e.shiftKey && document.activeElement === first) {
    e.preventDefault();
    last.focus();
  } else if (!e.shiftKey && document.activeElement === last) {
    e.preventDefault();
    first.focus();
  }
});
```

Key requirements:

- Use `<dialog>` element or `role="dialog"` with `aria-modal="true"`.
- Set `aria-labelledby` pointing to the dialog title.
- Set `aria-describedby` pointing to the dialog description when present.
- `Escape` key must close the dialog (except alert dialogs where a decision is required).
- Focus must move to the first focusable element inside the dialog on open.
- Focus must return to the trigger element on close.
- Background content must be inert while the dialog is open (`inert` attribute or `aria-hidden="true"`).
