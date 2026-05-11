# Form Patterns

Form patterns describe how to compose individual form components into complete, working forms. The goal is to minimize friction and maximize completion rates.

---

## Single-page form

For short forms (< 8 fields), a single-page layout is almost always the right choice.

**Best practices:**

- One column — don't try to save vertical space with two columns.
- Group related fields with `<fieldset>` and a `<legend>`.
- Place the primary action at the bottom, right-aligned.
- Validate on blur — don't wait until submit to show field-level errors.

```
┌───────────────────────────────────────┐
│  Form title (optional)                │
│                                       │
│  [Field group label]                  │
│  ┌─────────────────────────────────┐  │
│  │ Label                           │  │
│  │ [__________________________]    │  │
│  │ Helper text                     │  │
│  └─────────────────────────────────┘  │
│  ┌─────────────────────────────────┐  │
│  │ Label *                         │  │
│  │ [__________________________]    │  │
│  └─────────────────────────────────┘  │
│                                       │
│             [Cancel]  [Save changes]  │
└───────────────────────────────────────┘
```

---

## Multi-step wizard

For complex flows with 3+ distinct phases (onboarding, account setup, connector configuration).

**When to use:** The task has a clear sequence of steps that would be overwhelming in a single screen.

**Step indicator:**

Display step progress at the top using the [step progress component](../components/progress.md).

```
Step 1 of 3 ──●──○──○──
Connect your CRM
```

**Navigation rules:**

- "Continue" or "Next" advances to the next step.
- "Back" returns to the previous step without losing data.
- Users can navigate to any completed step via the step indicator.
- Completed steps are validated before proceeding.
- Show a summary page before the final irreversible action.

```
┌──────────────────────────────────────────────┐
│  ●──○──○  Step 1 of 3: Choose CRM           │
│──────────────────────────────────────────────│
│                                              │
│  Which CRM do you use?                       │
│                                              │
│  ○ Salesforce                                │
│  ○ HubSpot                                   │
│  ○ Clio                                      │
│                                              │
│──────────────────────────────────────────────│
│                      [Cancel]  [Continue →]  │
└──────────────────────────────────────────────┘
```

---

## Inline editing

For settings pages and tables where users edit individual values in place without navigating to a separate form.

**Trigger:** Click the value or a visible edit icon.

**Behavior:**
1. The static value is replaced with an input pre-populated with the current value.
2. Save and cancel buttons appear inline.
3. On save: optimistically update and confirm with a brief success state.
4. On cancel: revert to the original value.

```html
<!-- Static view -->
<div class="rc-inline-edit" data-value="My Salesforce">
  <span class="rc-inline-edit__value">My Salesforce</span>
  <button class="rc-icon-button" aria-label="Edit connector name">:material-pencil:</button>
</div>

<!-- Editing view -->
<div class="rc-inline-edit rc-inline-edit--active">
  <input type="text" value="My Salesforce" aria-label="Connector name" />
  <button class="rc-icon-button rc-icon-button--confirm" aria-label="Save">✓</button>
  <button class="rc-icon-button rc-icon-button--cancel" aria-label="Cancel">✕</button>
</div>
```

---

## Settings panels

Settings forms have distinct patterns:

- **Immediate save:** Toggles and selects save on change. No submit button needed.
- **Explicit save:** Text inputs save only when the user clicks "Save changes".
- **Mixed panels:** If a panel has both types, group them visually and be explicit about which fields auto-save.

```html
<!-- Auto-save toggle -->
<div class="rc-settings-row">
  <div>
    <strong>Enable call logging</strong>
    <p>Automatically log all inbound and outbound calls.</p>
  </div>
  <label class="rc-toggle">
    <input type="checkbox" role="switch" checked />
    <!-- auto-saves on change -->
  </label>
</div>

<!-- Explicit-save text field -->
<form>
  <div class="rc-field">
    <label for="webhook-url">Webhook URL</label>
    <input type="url" id="webhook-url" value="https://example.com/hook" />
  </div>
  <div class="rc-form__actions">
    <button type="submit" class="md-button md-button--primary">Save</button>
  </div>
</form>
```

---

## Destructive form actions

When a form action is irreversible (delete, reset, disconnect):

1. Use a danger-variant button.
2. Require explicit confirmation — either a dialog or typing the item name.
3. Place the destructive action visually separated from the main form actions (bottom of settings page, separated by a divider labeled "Danger zone").

```html
<section class="rc-danger-zone">
  <h2>Danger zone</h2>
  <div class="rc-danger-zone__item">
    <div>
      <strong>Delete this connector</strong>
      <p>Permanently removes all settings and stops call logging. Cannot be undone.</p>
    </div>
    <button class="md-button md-button--danger" data-confirm-delete>
      Delete connector
    </button>
  </div>
</section>
```

---

## Form submission feedback

After the user submits a form:

| Outcome | Feedback |
|---------|---------|
| Success (same page) | Brief success banner or inline confirmation, then revert to static view |
| Success (navigate away) | Navigate to the new page — the page content is the confirmation |
| Validation error | Inline field errors + summary at top, focus moves to first error |
| Server error | Error banner at top of form, fields remain editable |
| Network error | Error banner, "Try again" action, fields remain editable |

Never redirect on a server error — the user would lose their form data.
