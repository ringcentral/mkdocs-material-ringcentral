# Checkbox & Radio

Checkboxes and radio buttons are the primary controls for selecting from a small, visible set of options.

---

## Checkbox

Checkboxes allow **multiple selections** from a list. Each checkbox is independent.

```html
<fieldset class="rc-fieldset">
  <legend>Notification preferences</legend>

  <label class="rc-checkbox">
    <input type="checkbox" name="notifications" value="calls" checked />
    <span class="rc-checkbox__box" aria-hidden="true"></span>
    Call activity
  </label>

  <label class="rc-checkbox">
    <input type="checkbox" name="notifications" value="sms" />
    <span class="rc-checkbox__box" aria-hidden="true"></span>
    SMS messages
  </label>

  <label class="rc-checkbox">
    <input type="checkbox" name="notifications" value="voicemail" />
    <span class="rc-checkbox__box" aria-hidden="true"></span>
    Voicemails
  </label>
</fieldset>
```

### Indeterminate state

Use the indeterminate state for a "select all" checkbox when some but not all children are selected:

```javascript
const selectAll = document.getElementById('select-all');
selectAll.indeterminate = true; // Sets the mixed state
selectAll.checked = false;       // Base state is unchecked
```

---

## Radio buttons

Radio buttons allow **exactly one selection** from a mutually exclusive list. All options in a group must share the same `name`.

```html
<fieldset class="rc-fieldset">
  <legend>Sync frequency</legend>

  <label class="rc-radio">
    <input type="radio" name="sync" value="realtime" checked />
    <span class="rc-radio__dot" aria-hidden="true"></span>
    Real-time
  </label>

  <label class="rc-radio">
    <input type="radio" name="sync" value="hourly" />
    <span class="rc-radio__dot" aria-hidden="true"></span>
    Every hour
  </label>

  <label class="rc-radio">
    <input type="radio" name="sync" value="daily" />
    <span class="rc-radio__dot" aria-hidden="true"></span>
    Daily
  </label>
</fieldset>
```

---

## Choosing between checkbox and radio

| Use case | Checkbox | Radio |
|----------|----------|-------|
| Multiple options can be selected | ✅ | ❌ |
| Exactly one option must be selected | ❌ | ✅ |
| Binary on/off setting | ✅ | Consider [Toggle](toggles.md) |
| < 5 options | Both | ✅ |
| > 7 options | ✅ | Use [Select](selects.md) |

---

## Specs

| Property | Checkbox | Radio |
|----------|----------|-------|
| Control size | 18×18px | 18×18px |
| Border | `1.5px solid #9EA8B8` | `1.5px solid #9EA8B8` |
| Border radius | 3px | 50% (circle) |
| Checked color | `--ac-orange-raw` | `--ac-orange-raw` |
| Label gap | 8px | 8px |
| Touch target | 40×40px | 40×40px |

---

## States

| State | Visual |
|-------|--------|
| Unchecked | Empty box/circle, gray border |
| Checked | Orange fill, white check/dot |
| Indeterminate (checkbox) | Orange fill, white dash |
| Hover | Darker border, orange tint background |
| Focus | 2px orange focus ring |
| Disabled | 40% opacity, `cursor: not-allowed` |
| Error | Red border, error message below group |

---

## Accessibility

- Always wrap checkbox and radio groups in `<fieldset>` with a `<legend>`.
- Each control must have an associated `<label>`.
- Use native `<input type="checkbox">` and `<input type="radio">` — don't re-implement these with `div`s.
- For custom-styled controls, use the real input as the source of truth and style the visual box/circle as a sibling element.
- Error messages for a group go beneath the `<fieldset>`, referenced by `aria-describedby` on the fieldset.

```html
<fieldset class="rc-fieldset rc-fieldset--error" aria-describedby="notify-error">
  <legend>At least one notification method required</legend>
  <label class="rc-checkbox">
    <input type="checkbox" name="notify" value="email" />
    Email
  </label>
  <span id="notify-error" class="rc-field__error" role="alert">
    Select at least one notification method.
  </span>
</fieldset>
```
