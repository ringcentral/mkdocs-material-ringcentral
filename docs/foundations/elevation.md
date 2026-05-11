# Elevation

Elevation describes the perceived height of a surface above the page background. In RingCentral products, elevation is expressed through shadows and z-index layering — it communicates hierarchy and focus.

---

## Shadow scale

| Level | Token | Box-shadow value | Usage |
|-------|-------|-----------------|-------|
| 0 | `shadow-none` | `none` | Flat surfaces — cards in their default state |
| 1 | `shadow-xs` | `0 1px 2px rgba(27,42,74,0.08)` | Subtle lift — form inputs, chips, badges |
| 2 | `shadow-sm` | `0 2px 8px rgba(27,42,74,0.10)` | Cards, panels at rest |
| 3 | `shadow-md` | `0 4px 16px rgba(27,42,74,0.12)` | Cards on hover, focused inputs |
| 4 | `shadow-lg` | `0 8px 24px rgba(27,42,74,0.14)` | Dropdowns, floating menus |
| 5 | `shadow-xl` | `0 16px 40px rgba(27,42,74,0.18)` | Dialogs, modals |
| 6 | `shadow-2xl` | `0 24px 64px rgba(27,42,74,0.22)` | Drawers, fullscreen overlays |

The shadow color is derived from `--ac-navy` (`#002755`) at varying opacities to maintain a cool, professional shadow tone.

---

## Z-index scale

Z-index values should never be arbitrary. Use the scale below:

| Layer | Value | Usage |
|-------|-------|-------|
| `z-below` | -1 | Background elements, pseudo-element underlays |
| `z-base` | 0 | Default page content |
| `z-raised` | 1 | Slightly raised content (sticky table headers) |
| `z-dropdown` | 100 | Dropdown menus, autocomplete suggestions |
| `z-sticky` | 200 | Sticky headers and sidebars |
| `z-overlay` | 300 | Modal backdrops |
| `z-modal` | 400 | Modal dialogs, drawers |
| `z-toast` | 500 | Toast notifications (must appear above modals) |
| `z-tooltip` | 600 | Tooltips (must appear above everything) |

```css
:root {
  --z-below:    -1;
  --z-base:      0;
  --z-raised:    1;
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-overlay:  300;
  --z-modal:    400;
  --z-toast:    500;
  --z-tooltip:  600;
}
```

---

## Elevation and focus

Focus rings are a special use of elevation — they need to appear on top of everything else. The focus ring in RingCentral products uses:

```css
:focus-visible {
  outline: 2px solid var(--ac-orange-raw);
  outline-offset: 2px;
  z-index: var(--z-tooltip); /* Ensure it's never clipped */
}
```

Never remove `:focus-visible` outlines — they are critical for keyboard accessibility.

---

## Interaction states and elevation changes

Elements change elevation in response to user interaction to provide physical metaphor feedback:

| Component | Rest | Hover | Active | Focus |
|-----------|------|-------|--------|-------|
| Card | `shadow-sm` | `shadow-md` | `shadow-xs` | `shadow-md` + focus ring |
| Button (primary) | `shadow-xs` | `shadow-sm` | `shadow-none` | `shadow-xs` + focus ring |
| Input | `shadow-xs` | `shadow-xs` | — | `shadow-sm` + focus ring |
| Dropdown | — | — | `shadow-lg` (when open) | — |
| Dialog | `shadow-xl` | — | — | — |

---

## CSS reference

```css
:root {
  --shadow-none: none;
  --shadow-xs:   0 1px 2px  rgba(27,42,74,0.08);
  --shadow-sm:   0 2px 8px  rgba(27,42,74,0.10);
  --shadow-md:   0 4px 16px rgba(27,42,74,0.12);
  --shadow-lg:   0 8px 24px rgba(27,42,74,0.14);
  --shadow-xl:   0 16px 40px rgba(27,42,74,0.18);
  --shadow-2xl:  0 24px 64px rgba(27,42,74,0.22);
}
```

---

## Dark mode

In dark mode, shadows become less perceptible on dark surfaces. Elevation is instead communicated through surface lightness — higher elevation surfaces use a lighter value of the base dark color.

| Elevation | Light mode | Dark mode surface |
|-----------|------------|-------------------|
| Base | `#FFFFFF` | `#1A2235` |
| Raised | + shadow | `#212E47` (lighter) |
| Floating | + shadow | `#293856` (lighter still) |
| Overlay | + shadow | `#323F60` |

!!! tip "Test elevation in dark mode"
    Shadows that look great in light mode can disappear completely in dark mode. Always test elevation hierarchy in both color schemes before shipping.
