# Forms

Forms are containers that group related inputs toward a shared goal. A well-designed form reduces friction and error rate by presenting fields clearly, validating helpfully, and making the path to completion obvious.

---

## Form anatomy

Every form contains some combination of:

1. **Form title** — optional, appears at the top of the form section
2. **Field groups** — related fields visually grouped (via `<fieldset>`)
3. **Individual fields** — label + input + helper/error text
4. **Form actions** — submit and cancel buttons

```html
<form class="rc-form" novalidate>
  <fieldset class="rc-fieldset">
    <legend class="rc-fieldset__legend">Account details</legend>

    <div class="rc-field">
      <label for="full-name">Full name <span aria-hidden="true">*</span></label>
      <input type="text" id="full-name" required autocomplete="name" />
    </div>

    <div class="rc-field">
      <label for="work-email">Work email <span aria-hidden="true">*</span></label>
      <input type="email" id="work-email" required autocomplete="email" />
      <span class="rc-field__helper">We'll send a verification link to this address.</span>
    </div>
  </fieldset>

  <div class="rc-form__actions">
    <button type="button" class="md-button">Cancel</button>
    <button type="submit" class="md-button md-button--primary">Create account</button>
  </div>
</form>
```

---

## Field layout

### Single column (default)

Single-column layouts are easier to complete and have lower error rates. Use single-column for most forms.

### Two-column

Use two-column layouts only for:
- Short, closely related pairs (first name / last name)
- Compact setting forms where screen real estate is limited
- Never for unrelated fields

```css
.rc-field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 640px) {
  .rc-field-row {
    grid-template-columns: 1fr; /* Stack on mobile */
  }
}
```

---

## Required fields

Mark required fields clearly. Two acceptable approaches:

1. **Mark required fields** with an asterisk (`*`) and include a legend: `* Required fields`
2. **Mark optional fields** with "(optional)" when most fields are required

Do not rely on color alone to indicate required status.

---

## Validation strategy

### When to validate

| Trigger | Use for |
|---------|---------|
| **On submit** | Simple short forms (< 4 fields) |
| **On blur** (field loses focus) | Medium-length forms — validates field after user leaves it |
| **On change** (real-time) | Format-constrained fields (phone, credit card) |
| **Hybrid** | Validate on blur, re-validate on change after first error |

### Error messaging

- Show errors adjacent to the field they belong to.
- Never show errors before the user has interacted with a field.
- Provide an error summary at the top of the form for long forms with multiple errors.

```html
<!-- Error summary for long forms -->
<div role="alert" class="rc-form__error-summary">
  <h2>Please fix 2 errors before continuing:</h2>
  <ul>
    <li><a href="#work-email">Work email — enter a valid email address</a></li>
    <li><a href="#phone">Phone number — enter a 10-digit number</a></li>
  </ul>
</div>
```

---

## Form sections

For longer forms, use visual section breaks with `<fieldset>` and `<legend>`:

| Section | When to use |
|---------|-------------|
| `<fieldset>` + `<legend>` | Grouping related fields under a header |
| Visual divider | Separating major sections in a long form |
| Progressive disclosure | Showing advanced options conditionally |

---

## Form actions

| Scenario | Button arrangement |
|----------|--------------------|
| Short inline form | Submit button only, right-aligned |
| Full-page form | Cancel + Submit, right-aligned |
| Wizard step | Back + Next/Continue, right-aligned; cancel left-aligned or tertiary |
| Destructive confirmation | Cancel (left) + Destructive action (right) |

**Button labels:** Be specific. "Save settings", "Create connector", "Send invitation" — not "Submit" or "OK".

---

## Autofill and autocomplete

Always set `autocomplete` attributes on inputs that correspond to user data. This improves form completion speed dramatically.

```html
<input type="text"  autocomplete="given-name"  />  <!-- First name -->
<input type="text"  autocomplete="family-name" />  <!-- Last name -->
<input type="email" autocomplete="email"        />  <!-- Email -->
<input type="tel"   autocomplete="tel"          />  <!-- Phone -->
<input type="text"  autocomplete="organization" />  <!-- Company -->
```

---

## Accessibility

- Wrap related fields in `<fieldset>` with a `<legend>`.
- Every `<input>` must have a `<label>` — never omit labels.
- Indicate required fields in both the label and with `required` attribute.
- Error messages must be associated with their input via `aria-describedby`.
- On submit with errors, move focus to the first error or the error summary.
- Use `aria-invalid="true"` on inputs with validation failures.
- Set `novalidate` on forms that use custom validation to prevent browser default pop-ups.
