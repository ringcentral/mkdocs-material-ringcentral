# Changelog

Full release history for the RingCentral Design System and `mkdocs-material-ringcentral` plugin.

Versioning follows [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

- **MAJOR** — breaking changes to the plugin API, token names, or component behavior
- **MINOR** — new components, tokens, or features (backward compatible)
- **PATCH** — bug fixes and non-breaking corrections

---

## 2.1.0 — May 2026

### New

- **Drawer component** — Right and left panel overlay with backdrop, focus trap, and accessibility spec.
- **Motion tokens** — Full duration and easing token set (`--duration-*`, CSS easing variables).
- **Step progress** — Multi-step progress indicator for wizard flows.
- **Notification patterns** — Toast specification with stacking, timing, and ARIA guidance.

### Changed

- Dark mode surface colors updated for improved contrast across `navy-mid` tones.
- Skeleton animation now uses shimmer (`background-position`) instead of opacity pulse for smoother perceived performance.
- Button loading state now shows a spinner with "Saving…" label instead of disabling silently.

### Fixed

- Focus ring not visible on icon-only buttons in Firefox 123.
- `--ac-sidebar-width` token not applied consistently in nested layouts.
- Tooltip z-index was incorrectly set to 500 (below drawer). Now `var(--z-tooltip): 600`.
- Inter Tight weight 800 not loading on slow connections due to missing `display=swap`.

---

## 2.0.0 — January 2026

### Breaking changes

- **Color token rename:** All color tokens now use `--ac-*` prefix (previously `--rc-*`). Update all `var(--rc-coral)` references to `var(--ac-coral)`.
- **Sidebar width:** Default sidebar width changed from 220px to 240px. Custom overrides referencing `12.1rem` need updating.
- **Hero canvas:** The `ringcentral.js` canvas attachment now targets `.md-hero__inner` (previously `.md-hero`). Custom hero templates need adjustment.

### New

- Full 2026 brand refresh — coral/orange/lavender/sky gradient palette.
- Inter Tight typography (replaces Inter).
- New gradient sidebar background.
- `extra.js` GitHub Pages redirect utility.
- Full dark mode support with navy-family surface tokens.
- RingCentral Labs footer template with social links and copyright.

### Removed

- Legacy `--rc-*` CSS custom properties (replaced by `--ac-*`).
- Blue primary color from previous brand palette.
- Old `ringcentral-legacy.css` compatibility shim.

---

## 1.4.2 — October 2025

### Fixed

- 14 color contrast failures identified in accessibility audit:
  - Secondary text on `--ac-peach` background (ratio was 3.8:1, now 5.2:1)
  - Placeholder text contrast increased from 3.1:1 to 4.8:1
  - Chip selected state text adjusted for AA compliance
- Focus ring missing on `.md-tabs__link` elements.
- Skip link not visible on focus in Safari.
- Announcement banner link color was not readable at AA contrast.

---

## 1.4.0 — August 2025

### New

- **Chips component** — Filter, input, and label variants with specification.
- **Banners component** — Page-level announcement, status, and error banners.
- **Form patterns** — Single-page form, wizard, inline editing, and settings panel patterns.
- Badge dot variant for presence indicators.

### Changed

- Card hover shadow increased from `shadow-xs` to `shadow-md` for more tactile feel.
- Progress bar height increased from 4px to 6px for improved visibility.

---

## 1.3.0 — June 2025

### New

- **Accordion component** — Collapsible sections with animation spec.
- **Data table pattern** — Toolbar, sorting, selection, and bulk actions.
- **Loading states pattern** — 500ms rule, optimistic updates, and minimum display time.

---

## 1.2.0 — April 2025

### New

- **Elevation system** — Shadow scale, z-index tokens, interaction state elevation changes.
- **Motion foundation** — Duration and easing tokens, reduced motion guidance.
- Dark mode surface elevation (lighter surfaces for higher z-levels).

---

## 1.1.0 — February 2025

### New

- **Avatar component** — Photo, initials, icon, group variants with presence indicators.
- **Toast notification** — Success, info, warning, and error variants.
- Grid & layout foundation page.
- Spacing scale documentation.

---

## 1.0.0 — December 2024

Initial release of `mkdocs-material-ringcentral`.

### Features

- MkDocs Material plugin that injects RingCentral brand CSS, JS, logo, and template.
- Coral/orange gradient header and navigation tabs.
- Inter Tight + Roboto Mono typography.
- Custom sidebar gradient background.
- RingCentral Labs footer.
- Announcement banner block override.
- Hero canvas radial animation.

---

## Deprecation policy

Components and tokens are deprecated with a minimum of **one minor version** before removal. Deprecated items are marked in the documentation with a warning admonition and a removal target version.

!!! warning "Deprecated: `--rc-coral`"
    Renamed to `--ac-coral` in version 2.0. Will be removed in version 3.0.
