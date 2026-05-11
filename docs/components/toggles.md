# Toggle

Toggles represent an immediate binary on/off state. Unlike checkboxes — which represent a selection in a form — toggles trigger an instant action when switched.

---

## When to use

Use a toggle when:

- The change takes effect **immediately** (no submit button needed).
- The setting is binary — there's a clear on/off state.
- The visual metaphor of a physical switch aids comprehension.

Use a checkbox instead when:

- The change applies only when the user submits a form.
- The option is part of a multi-select group.

---

## Anatomy

```
Label              Toggle
─────────────────────────────────
Enable call logging   [●────] ON
Auto-record calls     [────○] OFF
```

Labels appear to the **left** of the toggle in settings panels. In dense forms, they may appear above.

---

## Variants

### Default (right label)

```html
<label class="rc-toggle">
  <input type="checkbox" role="switch" aria-checked="true" />
  <span class="rc-toggle__track" aria-hidden="true">
    <span class="rc-toggle__thumb"></span>
  </span>
  <span class="rc-toggle__label">Enable call logging</span>
</label>
```

### With description

For settings that benefit from a short explanatory sentence:

```html
<div class="rc-toggle-row">
  <div class="rc-toggle-row__content">
    <span class="rc-toggle-row__label">Auto-record calls</span>
    <span class="rc-toggle-row__desc">Automatically start recording on every inbound and outbound call.</span>
  </div>
  <label class="rc-toggle">
    <input type="checkbox" role="switch" aria-checked="false" />
    <span class="rc-toggle__track" aria-hidden="true">
      <span class="rc-toggle__thumb"></span>
    </span>
    <span class="sr-only">Auto-record calls</span>
  </label>
</div>
```

---

## Sizes

| Size | Track | Thumb | Usage |
|------|-------|-------|-------|
| Default | 40×22px | 18px | Standard settings |
| Small | 32×18px | 14px | Dense lists, table rows |

---

## States

| State | Track | Thumb |
|-------|-------|-------|
| Off | `#DDD0D8` | White |
| On | `--ac-orange-raw` | White |
| Hover (off) | `#C5BCC2` | White |
| Hover (on) | `#CC6200` | White |
| Focus | Orange focus ring on the input |
| Disabled (off) | `#EEE8EC` | `#F9F6F8` |
| Disabled (on) | `rgba(255,122,0,0.4)` | White |

---

## Animation

The thumb slides from one side to the other. Respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: no-preference) {
  .rc-toggle__thumb {
    transition: transform 150ms cubic-bezier(0.4, 0, 0.2, 1);
  }
  .rc-toggle__track {
    transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1);
  }
}
```

---

## Accessibility

- Use `role="switch"` on the `<input>` element to declare the toggle semantics.
- `aria-checked` must reflect the current state and update on change.
- The visible label must be associated with the input — either as a wrapping `<label>` or via `aria-labelledby`.
- Announce state changes to screen readers via `aria-live` or rely on the `role="switch"` announcement built into assistive technologies.
- Touch target must be at least 44×44px even if the visual toggle is smaller.

```javascript
toggle.addEventListener('change', () => {
  toggle.setAttribute('aria-checked', toggle.checked.toString());
});
```
