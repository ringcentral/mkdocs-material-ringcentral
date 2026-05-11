# Buttons

Buttons trigger actions. They are the primary mechanism users use to submit forms, confirm decisions, open dialogs, and navigate within a flow. Every button communicates an action label, a visual priority, and — when needed — a destructive or disabled state.

---

## Variants

### Primary

The primary button is the **single most important action** on a screen. There should be no more than one primary button in a view at a time.

```html
<button class="md-button md-button--primary">Get started</button>
```

**Specs:** Background `--ac-orange-raw`, text white, `border-radius: 4px`, padding `8px 16px`, font-weight 700.

---

### Secondary

Secondary buttons are for important-but-not-primary actions. They sit alongside primary buttons or appear alone when no strong hierarchy is needed.

```html
<button class="md-button">Learn more</button>
```

**Specs:** Background transparent, border `1.5px solid --ac-orange-raw`, text `--ac-orange-raw`, same padding and radius as primary.

---

### Tertiary / Ghost

Tertiary buttons are the lowest visual priority. Use for supplementary actions that don't compete with primary or secondary options.

```html
<button class="md-button md-button--ghost">Cancel</button>
```

**Specs:** No background, no border, text `--ac-orange-raw`. Appears as a styled link-like button.

---

### Destructive

For irreversible actions: delete, remove, revoke. Always pair a destructive button with a confirmation dialog unless the action can be undone.

```html
<button class="md-button md-button--danger">Delete account</button>
```

**Specs:** Background `#D32F2F`, text white. On hover: `#B71C1C`.

---

### Icon + Label

Pair an icon with a label when the icon meaningfully reinforces the action. Do not use icons purely for decoration.

```html
<button class="md-button md-button--primary">
  <span class="icon"><!-- :material-plus: --></span>
  Add connector
</button>
```

---

### Icon-only

Icon-only buttons must have an `aria-label`. Reserve them for toolbars and areas where space is extremely constrained.

```html
<button class="md-button md-button--icon" aria-label="Delete">
  <!-- :material-delete: -->
</button>
```

---

## Sizes

| Size | Height | Padding | Font size | Usage |
|------|--------|---------|-----------|-------|
| Large | 48px | `12px 24px` | 16px | Hero CTAs, prominent actions |
| **Default** | 40px | `8px 16px` | 14px | **Standard usage** |
| Small | 32px | `6px 12px` | 12px | Dense UIs, toolbars, inline actions |
| Compact | 24px | `4px 8px` | 12px | Table row actions, chips |

---

## States

| State | Visual treatment |
|-------|-----------------|
| Default | Base styles per variant |
| Hover | Darken background 8%, or lighten border |
| Active | Darken 16%, remove shadow |
| Focus | 2px orange focus ring, outline-offset 2px |
| Disabled | 40% opacity, `cursor: not-allowed` |
| Loading | Replace label with spinner, disable interaction |

---

## Usage guidelines

**Do:**

- Use one primary button per view.
- Make button labels verb-first: "Save changes", "Delete account", "Add connector".
- Keep labels short — 1–3 words for most actions.
- Show a loading state on async buttons instead of immediately disabling them.

**Don't:**

- Use "Click here" or "Submit" — be specific about what happens.
- Stack multiple primary buttons.
- Disable a button without explaining why (use a tooltip on the disabled state).
- Use a button where a link is more appropriate (navigation should use `<a>`, not `<button>`).

---

## Accessibility

- All buttons must have an accessible name — either the text content or an `aria-label`.
- Buttons must be focusable with `Tab` and activatable with `Enter` and `Space`.
- Do not disable buttons without providing a reason — prefer disabling with an explanatory tooltip over hiding the button entirely.
- Loading buttons must communicate state to screen readers: `aria-busy="true"` and updated `aria-label`.

```html
<!-- Loading state example -->
<button
  class="md-button md-button--primary"
  aria-busy="true"
  aria-label="Saving changes…"
  disabled
>
  <span class="spinner" aria-hidden="true"></span>
  Saving…
</button>
```

---

## CSS reference

```css
.md-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-family: var(--md-text-font);
  font-size: 0.875rem;
  font-weight: 700;
  line-height: 1.4;
  cursor: pointer;
  transition: background-color var(--duration-base) var(--ease-standard),
              box-shadow      var(--duration-base) var(--ease-standard);
}

.md-button--primary {
  background: var(--ac-orange-raw);
  color: #fff;
  border: none;
  box-shadow: var(--shadow-xs);
}

.md-button--primary:hover {
  background: #CC6200;
  box-shadow: var(--shadow-sm);
}

.md-button--primary:active {
  background: #A85000;
  box-shadow: none;
}

.md-button:focus-visible {
  outline: 2px solid var(--ac-orange-raw);
  outline-offset: 2px;
}

.md-button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
```
