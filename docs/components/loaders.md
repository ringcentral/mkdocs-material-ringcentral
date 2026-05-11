# Loaders

Loaders manage perceived performance. The right loader for a situation makes waiting feel shorter and keeps users informed that the system is working.

---

## Spinner

A rotating circle for short, in-place loading states (button actions, inline data refresh).

```html
<!-- Standalone spinner -->
<div class="rc-spinner" role="status" aria-label="Loading…">
  <span class="sr-only">Loading…</span>
</div>

<!-- Spinner inside a button -->
<button class="md-button md-button--primary" disabled aria-busy="true">
  <span class="rc-spinner rc-spinner--sm" aria-hidden="true"></span>
  Saving…
</button>
```

**Sizes:**

| Size | Diameter | Stroke | Usage |
|------|----------|--------|-------|
| `sm` | 16px | 2px | Inside buttons, inline |
| **Default** | 24px | 2.5px | **Cards, panels** |
| `lg` | 40px | 3px | Page-level loading |
| `xl` | 64px | 4px | Full-screen loading |

**Color:** Defaults to `--ac-orange-raw`. On dark backgrounds, uses white.

```css
@keyframes spin {
  to { transform: rotate(360deg); }
}

.rc-spinner {
  width: 24px;
  height: 24px;
  border: 2.5px solid rgba(255,122,0,0.2);
  border-top-color: var(--ac-orange-raw);
  border-radius: 50%;
  animation: spin 0.75s linear infinite;
}
```

---

## Skeleton screen

Skeleton loaders replace content before it loads, preserving layout and reducing perceived wait time. Use skeletons instead of spinners when loading a list, table, or complex card layout.

### Text skeleton

```html
<div class="rc-skeleton">
  <div class="rc-skeleton__line rc-skeleton__line--title"></div>
  <div class="rc-skeleton__line"></div>
  <div class="rc-skeleton__line"></div>
  <div class="rc-skeleton__line rc-skeleton__line--short"></div>
</div>
```

### Card skeleton

```html
<div class="rc-skeleton-card">
  <div class="rc-skeleton rc-skeleton--avatar"></div>
  <div class="rc-skeleton__content">
    <div class="rc-skeleton__line rc-skeleton__line--title"></div>
    <div class="rc-skeleton__line"></div>
  </div>
</div>
```

**Skeleton animation:**

```css
@keyframes skeleton-pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

.rc-skeleton__line,
.rc-skeleton--avatar {
  background: linear-gradient(90deg, #EEE8EC 25%, #F9F3F7 50%, #EEE8EC 75%);
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s ease-in-out infinite;
  border-radius: 4px;
}

@keyframes skeleton-shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### Skeleton specs

| Element | Width | Height |
|---------|-------|--------|
| Title line | 60% | 16px |
| Body line | 100% | 12px |
| Short line | 40% | 12px |
| Avatar/circle | Same as avatar size | Same as avatar size |
| Card | Full card width | 80px |
| Space between lines | 8px | — |

---

## Page-level loading

For full-page transitions or initial app load:

```html
<div class="rc-page-loader" role="status" aria-label="Loading page…">
  <div class="rc-spinner rc-spinner--lg"></div>
  <p class="rc-page-loader__message">Loading connectors…</p>
</div>
```

---

## Choosing the right loader

| Situation | Loader |
|-----------|--------|
| Button action (async) | Spinner inside button |
| Small data fetch (card, widget) | Spinner centered in container |
| List or table loading | Skeleton rows |
| Card grid loading | Skeleton cards |
| Full page loading | Spinner + message |
| File upload | [Linear progress bar](progress.md) |
| Multi-step operation | [Step progress](progress.md) |

---

## Accessibility

- All loaders must have `role="status"` or `aria-live="polite"` so assistive technologies announce the loading state.
- Include a visually hidden text description: `<span class="sr-only">Loading…</span>`.
- When loading completes, announce the result: `aria-live` region with the new content or a status message.
- Skeleton screens should have `role="status"` and `aria-busy="true"` on the container.
- Respect `prefers-reduced-motion` — use a static skeleton (no shimmer) or simple opacity pulse instead of the sliding shimmer.
