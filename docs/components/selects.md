# Select

Select components let users choose one or more options from a predefined list. Use selects when the list of options is fixed and the user knows what they're looking for.

---

## Variants

### Single select (native)

For short lists (< 7 options), the native `<select>` is perfectly acceptable — it's accessible, keyboard-operable, and works on all platforms.

```html
<div class="rc-field">
  <label for="region">Region</label>
  <select id="region" class="rc-select">
    <option value="">Select a region…</option>
    <option value="na1">North America</option>
    <option value="eu1">Europe</option>
    <option value="ap1">Asia Pacific</option>
  </select>
</div>
```

### Custom single select

For more than 7 options, or when you need search/filter capability, use a custom select:

```html
<div class="rc-field">
  <label for="crm">CRM platform</label>
  <div class="rc-select-custom" role="combobox" aria-expanded="false" aria-haspopup="listbox">
    <input
      type="text"
      id="crm"
      placeholder="Search or select…"
      autocomplete="off"
      role="combobox"
      aria-autocomplete="list"
      aria-controls="crm-listbox"
    />
    <span class="rc-select__arrow" aria-hidden="true">▾</span>
  </div>
  <ul id="crm-listbox" role="listbox" aria-label="CRM platforms" hidden>
    <li role="option" aria-selected="false">Salesforce</li>
    <li role="option" aria-selected="false">HubSpot</li>
    <li role="option" aria-selected="false">Clio</li>
  </ul>
</div>
```

### Multi-select

For choosing multiple options. Renders as a dropdown with checkboxes and a pill-style display of selected items.

```html
<div class="rc-field">
  <label id="features-label">Enabled features</label>
  <div class="rc-multiselect" aria-labelledby="features-label">
    <!-- Selected pills display -->
    <div class="rc-multiselect__pills">
      <span class="rc-chip">Call logging <button aria-label="Remove call logging">✕</button></span>
      <span class="rc-chip">SMS logging <button aria-label="Remove SMS logging">✕</button></span>
    </div>
    <!-- Dropdown trigger -->
    <button class="rc-multiselect__trigger" aria-expanded="false" aria-haspopup="listbox">
      Add feature…
    </button>
  </div>
</div>
```

---

## When to use which variant

| Situation | Component |
|-----------|-----------|
| < 7 options, no search | Native `<select>` |
| 7–20 options, search helpful | Custom select with filter |
| > 20 options | Custom select with search (required) |
| Multiple values | Multi-select |
| Free-form + suggestions | Combobox / autocomplete input |

---

## Sizes

Same as [Text Input](inputs.md) — Large (48px), Default (40px), Small (32px).

---

## States

Same state model as text inputs: default, hover, focus, disabled, error.

---

## Accessibility

- Native `<select>` is the most accessible option — prefer it when it meets the design requirements.
- Custom selects must implement the ARIA `combobox` or `listbox` pattern fully.
- The dropdown list must be keyboard-navigable with `↑`/`↓` and closeable with `Escape`.
- Selected options in multi-select must have `aria-selected="true"`.
- Each `<option>` must have a visible, unique label.

```
Keyboard pattern for custom select:
- Click / Enter → Opens dropdown
- ↑ / ↓         → Navigate options
- Enter          → Select focused option
- Escape         → Close without selecting
- Type           → Filter options (if search enabled)
```
