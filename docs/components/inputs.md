# Text Input

Text inputs allow users to enter free-form text. They are the most common interactive element in forms and should behave predictably and accessibly in all contexts.

---

## Variants

### Default

The standard single-line text input for short, free-form responses.

```html
<div class="rc-field">
  <label for="name">Full name</label>
  <input type="text" id="name" placeholder="Jane Smith" />
</div>
```

### With helper text

Use helper text to clarify format requirements or provide supplementary guidance. Helper text appears below the input at all times (not just on error).

```html
<div class="rc-field">
  <label for="phone">Phone number</label>
  <input type="tel" id="phone" placeholder="+1 (555) 000-0000" />
  <span class="rc-field__helper">Include country code for international numbers.</span>
</div>
```

### With prefix/suffix

For inputs with a known unit, currency symbol, or icon context.

```html
<div class="rc-field">
  <label for="price">Monthly price</label>
  <div class="rc-field__addons">
    <span class="rc-field__prefix">$</span>
    <input type="number" id="price" placeholder="0.00" />
    <span class="rc-field__suffix">USD</span>
  </div>
</div>
```

### Textarea

Multi-line free-form text. Use when the expected input is more than one sentence or when line breaks are meaningful.

```html
<div class="rc-field">
  <label for="notes">Notes</label>
  <textarea id="notes" rows="4" placeholder="Add any relevant context…"></textarea>
  <span class="rc-field__helper">Maximum 500 characters.</span>
</div>
```

---

## Sizes

| Size | Height | Font size | Usage |
|------|--------|-----------|-------|
| Large | 48px | 16px | Prominent search, hero forms |
| **Default** | 40px | 14px | **Standard usage** |
| Small | 32px | 12px | Dense tables, compact settings panels |

Textareas have no fixed height — use `rows` to set a sensible default and allow vertical resize.

---

## States

| State | Visual |
|-------|--------|
| Default | `1px solid #DDD0D8` border, white background |
| Hover | `1px solid #9EA8B8` border |
| Focus | `1.5px solid --ac-orange-raw` border, `shadow-sm` |
| Filled | Default border |
| Disabled | 50% opacity, `background: #F6F8FA`, no hover/focus |
| Read-only | `background: #F6F8FA`, no focus ring |
| Error | `1.5px solid #D32F2F` border, error message below |
| Success | `1.5px solid #2E7D32` border (optional, for validated fields) |

---

## Validation and error states

Error messages appear below the input field, replacing helper text when validation fails. They should be:

- Specific about what went wrong
- Instructive — tell the user how to fix it
- Associated with the input via `aria-describedby`

```html
<div class="rc-field rc-field--error">
  <label for="email">Email address</label>
  <input
    type="email"
    id="email"
    value="not-an-email"
    aria-describedby="email-error"
    aria-invalid="true"
  />
  <span class="rc-field__error" id="email-error">
    Enter a valid email address, like name@example.com.
  </span>
</div>
```

---

## Specs

| Property | Value |
|----------|-------|
| Border radius | 4px |
| Padding | `8px 12px` |
| Font | Inter Tight, 14px, weight 400 |
| Placeholder color | `#9EA8B8` |
| Background | `#FFFFFF` |
| Disabled background | `#F6F8FA` |
| Label size | 12px, weight 600 |
| Label margin-bottom | 4px |
| Helper text size | 12px, weight 400, color `#5A6070` |
| Error text size | 12px, weight 600, color `#D32F2F` |

---

## Accessibility

- Every input **must** have a visible `<label>` — do not rely on `placeholder` as a label.
- `placeholder` text disappears when the user types, so it cannot convey required format.
- Associate helper and error text with the input using `aria-describedby`.
- Use `aria-invalid="true"` on inputs with validation errors.
- Use appropriate `type` attributes (`email`, `tel`, `number`, `url`, `password`, `search`) to invoke the correct mobile keyboard and enable browser autofill.
- Group related inputs inside `<fieldset>` with a `<legend>`.

!!! warning "Never use placeholder as a label"
    Placeholder text fails WCAG 1.3.1 (Info and Relationships) when used as the only label. It disappears on focus, has insufficient contrast by definition, and is not reliably announced by all screen readers.
