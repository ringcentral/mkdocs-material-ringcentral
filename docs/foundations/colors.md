# Colors

The RingCentral palette is built on warmth and clarity. Coral and orange anchor the brand; lavender, sky, and navy provide depth and calm. Every color has a semantic role — don't use them interchangeably.

---

## Brand palette

These are the raw brand colors expressed as CSS custom properties. Use them via the token names, not as hardcoded hex values.

| Token | Hex | Name | Usage |
|-------|-----|------|-------|
| `--ac-coral` | `#FF7A35` | Coral | Primary actions, highlights, CTAs |
| `--ac-orange` | `#FFB347` | Orange | Gradients, accents, hover states |
| `--ac-orange-raw` | `#FF7A00` | Pure Orange | Primary foreground, interactive focus |
| `--ac-lavender` | `#D4A5C9` | Lavender | Gradient terminus, soft accents |
| `--ac-sky` | `#A8C8E8` | Sky | Gradient endpoint, informational tones |
| `--ac-navy` | `#002755` | Navy | Dark surfaces, text on light backgrounds |
| `--ac-navy-mid` | `#2C3E6A` | Navy Mid | Secondary dark surface, sidebar backgrounds |

### Tints and surface colors

| Token | Hex | Name | Usage |
|-------|-----|------|-------|
| `--ac-peach` | `#FFF0E8` | Peach | Warm surface tint, hover backgrounds |
| `--ac-mauve` | `#F5EAF5` | Mauve | Cool surface tint, sidebar gradient |
| `--ac-pale-blue` | `#EAF0FA` | Pale Blue | Informational backgrounds, gradient terminus |

---

## Gradient

The signature RingCentral gradient flows from Coral through Orange to Lavender and Sky. It appears in the header, navigation tabs, and hero sections.

```css
--ac-gradient: linear-gradient(
  135deg,
  var(--ac-coral)   0%,
  var(--ac-orange)  45%,
  var(--ac-lavender) 75%,
  var(--ac-sky)     100%
);
```

**Usage rules:**

- The gradient is reserved for **chrome surfaces** only: header, tab bar, and hero sections.
- Never apply the gradient as a text color in body content.
- Never tile or repeat the gradient — it should always span the full width of its container.

---

## Semantic roles

Map colors to semantic intent, not arbitrary decoration.

| Role | Token | Notes |
|------|-------|-------|
| **Primary action** | `--ac-orange-raw` | Buttons, links, interactive focus |
| **Destructive / error** | `#D32F2F` | Not a brand token — use `var(--md-typeset-del-color)` from Material |
| **Warning** | `#F57C00` | Amber — accessible on white at all type sizes |
| **Success** | `#2E7D32` | Forest green — accessible on white |
| **Informational** | `--ac-sky` | Used with white or navy text only |
| **Surface: default** | `#FFFFFF` | Page backgrounds |
| **Surface: warm** | `--ac-peach` | Hover states, warm tint areas |
| **Surface: cool** | `--ac-mauve` | Sidebar gradient, filter panel backgrounds |
| **Text: primary** | `#1A1A2E` | Body text — near-black with a hint of navy |
| **Text: secondary** | `#5A6070` | Captions, helper text, secondary labels |
| **Text: disabled** | `#9EA8B8` | Disabled inputs, placeholder text |
| **Border** | `#DDD0D8` | Dividers, card outlines, input borders |

---

## MkDocs Material token overrides

The plugin sets the following Material theme tokens to match the RingCentral brand:

```css
--md-primary-fg-color:        var(--ac-orange-raw);
--md-primary-fg-color--light: rgba(255,122,0,0.12);
--md-primary-fg-color--dark:  #CC6200;
--md-primary-bg-color:        #fff;
--md-primary-bg-color--light: rgba(255,255,255,0.7);
```

---

## Dark mode

In dark mode (`.md-color-scheme--slate`), surfaces invert to navy-family colors. The gradient remains unchanged in the header — it reads well against both light and dark backgrounds.

| Light mode | Dark mode |
|------------|-----------|
| `#ffffff` surface | `#1A2235` surface |
| `#1A1A2E` body text | `#E8ECF2` body text |
| `#DDD0D8` border | `#3A4560` border |
| `--ac-peach` hover | Navy hover (`rgba(255,122,53,0.08)`) |

---

## Accessibility — minimum contrast ratios

All text-on-background combinations must meet **WCAG 2.1 AA**:

- **4.5:1** minimum for normal text (< 18pt / < 14pt bold)
- **3:1** minimum for large text (≥ 18pt / ≥ 14pt bold) and UI components

| Combination | Ratio | Pass |
|-------------|-------|------|
| `#1A1A2E` on `#FFFFFF` | 15.8:1 | ✅ AAA |
| `#FF7A00` on `#FFFFFF` | 3.1:1 | ✅ AA (large) |
| `#FFFFFF` on `--ac-coral` | 3.6:1 | ✅ AA (large) |
| `#FFFFFF` on `--ac-navy` | 14.8:1 | ✅ AAA |
| `#5A6070` on `#FFFFFF` | 5.7:1 | ✅ AA |

!!! warning "Coral on white for small text"
    `--ac-coral` (#FF7A35) achieves only 3.6:1 contrast on white. **Do not use it for body text or small labels.** Acceptable uses: large headings, icon fills, and gradient surfaces where white text sits on top.

---

## Usage examples

=== "CSS"
    ```css
    .button-primary {
      background: var(--ac-orange-raw);
      color: #fff;
    }

    .surface-warm {
      background: var(--ac-peach);
    }

    .text-secondary {
      color: #5A6070;
    }
    ```

=== "HTML"
    ```html
    <!-- Use via inline style only for one-off overrides -->
    <div style="background: var(--ac-mauve); padding: 1rem;">
      Mauve surface
    </div>
    ```
