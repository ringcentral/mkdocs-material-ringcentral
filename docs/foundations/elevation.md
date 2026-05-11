# Elevation

Elevation describes the perceived height of a surface above the page background. In RingCentral products, elevation is expressed through shadows and z-index layering — it communicates hierarchy and focus.

---

## Shadow scale

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.5rem; margin: 1.5rem 0 2.5rem;">

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: none; border: 1px solid var(--md-default-fg-color--lightest);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-none · 0</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Flat surfaces — cards at rest</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 1px 2px rgba(27,42,74,0.08);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-xs · 1</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Inputs, chips, badges</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 2px 8px rgba(27,42,74,0.10);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-sm · 2</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Cards, panels at rest</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 4px 16px rgba(27,42,74,0.12);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-md · 3</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Cards on hover, focused inputs</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 8px 24px rgba(27,42,74,0.14);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-lg · 4</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Dropdowns, floating menus</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 16px 40px rgba(27,42,74,0.18);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-xl · 5</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Dialogs, modals</p>
  </div>

  <div style="background: var(--md-default-bg-color); border-radius: 10px; padding: 1.25rem 1.5rem; box-shadow: 0 24px 64px rgba(27,42,74,0.22);">
    <p style="font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--md-default-fg-color--light); margin: 0 0 0.4rem;">shadow-2xl · 6</p>
    <p style="font-size: 0.8rem; color: var(--md-default-fg-color--light); margin: 0; line-height: 1.5;">Drawers, fullscreen overlays</p>
  </div>

</div>

| Level | Token | Box-shadow value | Usage |
|-------|-------|-----------------|-------|
| 0 | `shadow-none` | `none` | Flat surfaces — cards in their default state |
| 1 | `shadow-xs` | `0 1px 2px rgba(27,42,74,0.08)` | Subtle lift — form inputs, chips, badges |
| 2 | `shadow-sm` | `0 2px 8px rgba(27,42,74,0.10)` | Cards, panels at rest |
| 3 | `shadow-md` | `0 4px 16px rgba(27,42,74,0.12)` | Cards on hover, focused inputs |
| 4 | `shadow-lg` | `0 8px 24px rgba(27,42,74,0.14)` | Dropdowns, floating menus |
| 5 | `shadow-xl` | `0 16px 40px rgba(27,42,74,0.18)` | Dialogs, modals |
| 6 | `shadow-2xl` | `0 24px 64px rgba(27,42,74,0.22)` | Drawers, fullscreen overlays |

The shadow color is derived from `--ac-navy` (`#1B2A4A`) at varying opacities to maintain a cool, professional shadow tone.

---

## Focus rings

Focus rings communicate keyboard position. The RingCentral focus ring uses a solid `2px` orange outline with `2px` offset so it clears the element's own border without blending into it.

<div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; margin: 1.5rem 0 2rem;">

  <button style="padding: 0.5rem 1.25rem; border-radius: 6px; border: none; background: #FF8800; color: white; font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; font-weight: 600; outline: 2px solid #FF8800; outline-offset: 2px; cursor: default;">Primary button</button>

  <button style="padding: 0.5rem 1.25rem; border-radius: 6px; border: 1.5px solid #CBD5E0; background: transparent; color: var(--md-default-fg-color); font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; font-weight: 600; outline: 2px solid #FF8800; outline-offset: 2px; cursor: default;">Secondary button</button>

  <input type="text" value="Text input" readonly style="padding: 0.4rem 0.75rem; border-radius: 6px; border: 1.5px solid #CBD5E0; background: var(--md-default-bg-color); color: var(--md-default-fg-color); font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; outline: 2px solid #FF8800; outline-offset: 2px; cursor: default;" />

  <a href="#" onclick="return false;" style="padding: 0.4rem 0.5rem; border-radius: 4px; color: #FF8800; font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; outline: 2px solid #FF8800; outline-offset: 2px; text-decoration: none;">Text link</a>

</div>

```css
:focus-visible {
  outline: 2px solid var(--ac-orange-raw); /* #FF8800 */
  outline-offset: 2px;
  z-index: var(--z-tooltip); /* Never clipped by other layers */
}
```

Never remove `:focus-visible` outlines — they are critical for keyboard accessibility.

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
