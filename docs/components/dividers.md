# Dividers

Dividers are thin lines that separate content regions. Use them sparingly — if you're reaching for a divider, consider whether whitespace alone would serve the same purpose.

---

## Variants

### Horizontal divider

Separates stacked content sections.

```html
<hr class="rc-divider" />
```

```css
.rc-divider {
  border: none;
  border-top: 1px solid #DDD0D8;
  margin: 1.5rem 0;
}
```

### Inset divider

A divider that doesn't span the full width — used between list items to avoid drawing lines under the avatar or icon:

```html
<li class="rc-list__item">
  <img class="rc-avatar" src="user.jpg" alt="Jane Smith" />
  <div class="rc-list__content">Jane Smith</div>
</li>
<li aria-hidden="true"><hr class="rc-divider rc-divider--inset" /></li>
```

### Vertical divider

Separates side-by-side content regions:

```html
<div class="rc-panel-split">
  <div class="rc-panel">Left panel</div>
  <div class="rc-divider rc-divider--vertical" role="separator" aria-orientation="vertical"></div>
  <div class="rc-panel">Right panel</div>
</div>
```

### Section divider with label

Used in dropdown menus and long settings lists to label groups:

```html
<li role="separator" class="rc-divider rc-divider--labeled" aria-label="Danger zone">
  Danger zone
</li>
```

---

## Specs

| Property | Value |
|----------|-------|
| Color | `#DDD0D8` |
| Thickness | `1px` |
| Margin (horizontal) | `1.5rem 0` (24px top and bottom) |
| Inset start | 52px (aligns with content after a 40px avatar + 12px gap) |

---

## When not to use a divider

- **Between every list item** — use row hover and padding instead.
- **At the top of a section** that already has a heading.
- **Around a single item** — adds visual weight without purpose.
- **Instead of whitespace** — if the sections are clearly distinct via size and hierarchy, a divider adds noise.

---

## Accessibility

- Decorative dividers: use `<hr>` with no additional ARIA (it carries `role="separator"` natively).
- Menu separators: `role="separator"` on a `<li>`.
- Vertical dividers that separate functional panels: add `aria-orientation="vertical"`.
- Label dividers in menus: `aria-label` on the separator element.
