# Navigation

Navigation systems help users understand where they are, where they can go, and how to get there. RingCentral products use a combination of top navigation tabs, a left sidebar, and in-page navigation components.

---

## Navigation hierarchy

RingCentral products use a **three-tier navigation model**:

```
Tier 1: Top navigation tabs       ← Global product sections
Tier 2: Left sidebar              ← Section sub-pages
Tier 3: In-page anchors / TOC     ← Page-level navigation
```

---

## Top navigation tabs

Full-width gradient tabs that appear below the header. They represent the highest-level sections of a product.

**Specs:**

| Property | Value |
|----------|-------|
| Background | `--ac-gradient` |
| Height | `48px` |
| Font | Inter Tight, 14px, weight 600 |
| Active link | White, underlined |
| Inactive link | `rgba(255,255,255,0.75)` |
| Hover | White |
| Tab padding | `0 16px` |

**Rules:**

- 5–7 tabs maximum. More than that requires a different navigation pattern.
- The active tab is underlined with a semi-transparent white rule.
- Tabs are sticky (`navigation.tabs.sticky`) so they remain visible on scroll.

---

## Left sidebar

The sidebar provides in-section navigation. It sits at a fixed 240px width with a warm-to-cool gradient background.

**Sidebar gradient:**

```css
background: linear-gradient(180deg,
  #FFF4EF 0%,
  #F9F0F9 55%,
  #EFF3FA 100%
);
```

**Sidebar navigation item states:**

| State | Treatment |
|-------|-----------|
| Default | Text `#1A1A2E`, no background |
| Hover | `--ac-peach` background |
| Active | `--ac-orange-raw` text, bold weight, left accent border |
| Expanded group | Bold heading, children indented 12px |

**Sidebar width override:**

The plugin fixes the sidebar at exactly 240px so it aligns with the gradient background boundary:

```css
.md-sidebar--primary { width: 240px !important; }
```

---

## In-page table of contents

The right-side TOC automatically generates from `H2` and `H3` headings on each page. It appears in the right gutter on screens wider than 1220px.

**Rules:**

- Pages longer than 3 sections should always have in-page headers.
- Don't use more than two levels in the TOC (H2 + H3 maximum).
- TOC entries should match heading text exactly.

---

## Breadcrumbs

See [Breadcrumbs](breadcrumbs.md) for the standalone breadcrumb component.

The Material theme's `navigation.path` feature auto-generates breadcrumbs from the site navigation hierarchy. Enable it in `mkdocs.yml`:

```yaml
theme:
  features:
    - navigation.path
```

---

## Mobile navigation

On screens below 960px, the sidebar collapses into a hamburger menu. The top tabs collapse into a single dropdown menu.

**Mobile navigation rules:**

- All navigation items must be reachable via the hamburger menu.
- The active section should be visible/highlighted in the collapsed state.
- Touch targets must be at least 44×44px.

---

## Navigation accessibility

- The primary navigation landmark uses `<nav aria-label="Primary">`.
- The sidebar uses `<nav aria-label="Site navigation">`.
- Active pages carry `aria-current="page"`.
- Skip navigation links must be present: `<a href="#main" class="skip-link">Skip to main content</a>`.
- Keyboard navigation: `Tab` moves through links, `Enter` activates, `Escape` closes expanded menus.

```html
<!-- Skip link — visually hidden until focused -->
<a class="skip-link" href="#main-content">Skip to main content</a>

<nav aria-label="Primary navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/docs">Documentation</a></li>
    <li><a href="/support">Support</a></li>
  </ul>
</nav>
```

---

## Navigation dos and don'ts

**Do:**

- Use nouns for navigation labels (sections), verbs for actions (buttons).
- Keep labels short — 1–3 words.
- Mirror the navigation in the page title so users always know where they are.
- Provide breadcrumbs on pages deeper than 2 levels.

**Don't:**

- Use navigation tabs for in-page filtering — that's the [Tabs component](tabs.md).
- Create navigation items that lead to empty or placeholder pages.
- Duplicate items across navigation tiers.
- Hide important pages more than 3 clicks deep.
