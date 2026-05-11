# Spacing

All spacing in RingCentral products is derived from a **4px base unit**. Every margin, padding, gap, and component dimension should be a multiple of 4.

---

## Spacing scale

| Token | Value | Pixels | Usage |
|-------|-------|--------|-------|
| `space-0` | 0 | 0px | Explicit zero |
| `space-1` | 0.25rem | 4px | Minimal gaps — icon-to-label, tight rows |
| `space-2` | 0.5rem | 8px | Compact spacing — chip padding, tag margins |
| `space-3` | 0.75rem | 12px | Default icon padding, small internal spacing |
| `space-4` | 1rem | 16px | Default component padding — buttons, inputs, cells |
| `space-5` | 1.25rem | 20px | Comfortable content padding |
| `space-6` | 1.5rem | 24px | Card padding, form field gaps |
| `space-8` | 2rem | 32px | Section gaps, modal padding |
| `space-10` | 2.5rem | 40px | Large section separators |
| `space-12` | 3rem | 48px | Page-level vertical rhythm |
| `space-16` | 4rem | 64px | Hero sections, feature headers |
| `space-20` | 5rem | 80px | Landing page sections |
| `space-24` | 6rem | 96px | Maximum page-level spacing |

---

## Base unit

The 4px base unit exists because:

- It divides evenly into common device pixel ratios (1×, 2×, 3×).
- It creates a rhythm that feels balanced without being too rigid.
- It aligns with Material Design and the majority of modern design systems, reducing friction when integrating third-party components.

**Never use values that aren't multiples of 4 for layout spacing.** Use `space-3` (12px) rather than reaching for 10px or 14px.

---

## Component-level spacing defaults

| Component | Internal padding | Gap between children |
|-----------|-----------------|----------------------|
| Button (default) | 8px 16px | — |
| Button (compact) | 4px 12px | — |
| Input field | 8px 12px | — |
| Card | 24px | 16px |
| Dialog | 24px | 16px (between sections) |
| Form group | 24px | 16px (between fields) |
| Table cell | 12px 16px | — |
| Sidebar item | 8px 12px | — |
| Page body | 0 24px | 32px (between sections) |

---

## Layout spacing

Use larger space values for layout decisions:

```css
/* Page section separator */
.section + .section { margin-top: 3rem; /* 48px */ }

/* Card grid gap */
.card-grid { gap: 1.5rem; /* 24px */ }

/* Hero section padding */
.hero { padding: 5rem 2rem; /* 80px 32px */ }
```

---

## Don'ts

- **Don't mix units.** Use `rem` for everything that should scale with font-size preferences. Avoid `px` for layout spacing (it doesn't scale with user preferences).
- **Don't use arbitrary values.** `margin: 7px` or `padding: 11px` are signals that something is off with the layout math — revisit the component structure.
- **Don't use spacing for alignment.** If you're adding padding to one side to visually "push" something, check whether a flex/grid layout would achieve the same result more robustly.

---

## CSS custom properties

While tokens for spacing are referenced by their semantic names in Figma, the CSS implementation maps to the Material `--md-spacing-*` scale. You can define your own spacing properties in `extra.css`:

```css
:root {
  --rc-space-1:  0.25rem;
  --rc-space-2:  0.5rem;
  --rc-space-3:  0.75rem;
  --rc-space-4:  1rem;
  --rc-space-6:  1.5rem;
  --rc-space-8:  2rem;
  --rc-space-12: 3rem;
}
```
