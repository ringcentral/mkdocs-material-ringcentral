# Progress

Progress indicators communicate how much of a task is complete and whether the system is working. Use them whenever an operation takes more than ~500ms.

---

## Linear progress bar

For operations with a known completion percentage.

```html
<!-- Determinate -->
<div class="rc-progress" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100" aria-label="Uploading contacts: 65%">
  <div class="rc-progress__fill" style="width: 65%"></div>
</div>

<!-- With label -->
<div class="rc-progress-labeled">
  <div class="rc-progress-labeled__header">
    <span>Importing 1,234 contacts</span>
    <span>65%</span>
  </div>
  <div class="rc-progress" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100">
    <div class="rc-progress__fill" style="width: 65%"></div>
  </div>
</div>
```

**Specs:**

| Property | Value |
|----------|-------|
| Height | 6px |
| Border radius | 3px |
| Track color | `#DDD0D8` |
| Fill color | `--ac-orange-raw` |
| Fill animation | Transition width with `ease-standard` |

---

## Indeterminate progress bar

For operations with unknown duration. The fill animates back and forth continuously.

```html
<div class="rc-progress rc-progress--indeterminate" role="progressbar" aria-label="Loading…" aria-valuetext="Loading">
  <div class="rc-progress__fill"></div>
</div>
```

```css
@keyframes indeterminate {
  0%   { transform: translateX(-100%) scaleX(0.4); }
  50%  { transform: translateX(50%)  scaleX(0.6); }
  100% { transform: translateX(200%) scaleX(0.4); }
}

.rc-progress--indeterminate .rc-progress__fill {
  width: 100%;
  animation: indeterminate 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
```

---

## Circular progress (spinner)

See [Loaders](loaders.md) for the spinner component used in buttons and page-level loading states.

---

## Step progress

For multi-step flows where the user can see their position in a sequence.

```html
<ol class="rc-steps" aria-label="Setup progress">
  <li class="rc-step rc-step--complete" aria-current="false">
    <span class="rc-step__icon" aria-hidden="true">✓</span>
    <span class="rc-step__label">Connect CRM</span>
  </li>
  <li class="rc-step rc-step--active" aria-current="step">
    <span class="rc-step__icon" aria-hidden="true">2</span>
    <span class="rc-step__label">Configure fields</span>
  </li>
  <li class="rc-step" aria-current="false">
    <span class="rc-step__icon" aria-hidden="true">3</span>
    <span class="rc-step__label">Test connection</span>
  </li>
</ol>
```

**Step states:**

| State | Icon | Color |
|-------|------|-------|
| Complete | ✓ checkmark | `#2E7D32` green |
| Active | Step number | `--ac-orange-raw`, bold label |
| Upcoming | Step number | `#9EA8B8` gray |
| Error | ✕ mark | `#D32F2F` red |

---

## Usage guidelines

- Show a progress indicator for any operation that takes more than **500ms**.
- Use **determinate** progress when you know the percentage; **indeterminate** when you don't.
- Include a text label alongside the progress bar when space allows — "Importing contacts… 65%".
- For very fast operations (< 300ms), skip the progress indicator to avoid flicker.
- On completion, briefly show a success state before removing the progress element.

---

## Accessibility

- `role="progressbar"` is required for assistive technology to identify the element.
- Set `aria-valuenow`, `aria-valuemin`, and `aria-valuemax` for determinate progress.
- Set `aria-label` or `aria-labelledby` to describe what's progressing.
- For indeterminate progress, set `aria-valuetext="Loading"` or `aria-busy="true"` on the loading region.
- Respect `prefers-reduced-motion` — use a simple static fill or pulse instead of animation.
