# Tooltips

Tooltips reveal supplementary information when users hover or focus on an element. They provide brief, helpful context without cluttering the interface.

---

## When to use

Use a tooltip when:

- An icon button has no visible label and needs one.
- An interface term needs a brief clarification that would clutter the page if always visible.
- A truncated text label needs its full value exposed.

Do **not** use a tooltip when:

- The information is critical to completing the task — put it in helper text or a label instead.
- The content includes interactive elements (links, buttons) — use a [Popover](menus.md) instead.
- The information repeats the visible label — tooltips on buttons that already have text are noise.
- On mobile — tooltips are hover-triggered and inaccessible on touch devices.

---

## Variants

### Default tooltip

```html
<button
  class="rc-icon-button"
  aria-label="Copy to clipboard"
  data-tooltip="Copy to clipboard"
>
  :material-content-copy:
</button>
```

Tooltip text is the same as `aria-label` — the tooltip is purely visual reinforcement.

### Information tooltip

For clarifying interface terms or explaining a complex setting:

```html
<label>
  Webhook endpoint
  <button
    class="rc-tooltip-trigger"
    aria-describedby="webhook-tip"
    type="button"
  >
    :material-information-outline:
    <span class="sr-only">What is this?</span>
  </button>
</label>
<div id="webhook-tip" role="tooltip" hidden>
  The URL RingCentral will POST call event data to. Must be publicly accessible and respond with HTTP 200.
</div>
```

---

## Placement

Tooltips default to appearing **above** the trigger. They automatically flip to avoid viewport edges.

| Placement | Use when |
|-----------|----------|
| `top` (default) | General use |
| `bottom` | When the trigger is near the top of the viewport |
| `right` | For sidebar items or left-edge triggers |
| `left` | For right-edge triggers |

---

## Specs

| Property | Value |
|----------|-------|
| Max width | 240px |
| Padding | `6px 10px` |
| Background | `#1A1A2E` (near-black) |
| Text color | `#F5F5F5` |
| Font | 12px, weight 400 |
| Border radius | 4px |
| Arrow size | 6px |
| Delay before show | 400ms |
| Delay before hide | 100ms |
| Animation | Fade in 150ms |

---

## Accessibility

- Tooltips triggered by hover must **also** be triggered by keyboard focus.
- Use `role="tooltip"` on the tooltip container.
- Associate the tooltip with its trigger via `aria-describedby` (pointing to the tooltip's `id`).
- Do not put essential information in a tooltip — it's not accessible to touch device users.
- Tooltips must be **dismissible with `Escape`** when triggered by focus.

```javascript
trigger.addEventListener('mouseenter', showTooltip);
trigger.addEventListener('focus',      showTooltip);
trigger.addEventListener('mouseleave', hideTooltip);
trigger.addEventListener('blur',       hideTooltip);
trigger.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') hideTooltip();
});
```

---

## Tooltip vs. Popover

| | Tooltip | Popover |
|-|---------|---------|
| Trigger | Hover / focus | Click |
| Contains interactive elements | No | Yes |
| Dismissed by | Move away / blur / Escape | Click outside / Escape |
| Used for | Brief context | Actions, additional content |
