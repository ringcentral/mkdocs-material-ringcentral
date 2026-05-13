# Homepage Hero Recipes

Full-bleed hero sections for the homepage. All variants use the `.ac-hero` base class inside a `.ac-home` wrapper.

---

## Required setup

Homepage heroes must live inside the `.ac-home` wrapper with the navigation and TOC hidden:

```markdown
---
hide:
  - navigation
  - toc
---

<div class="ac-home">

  <!-- hero goes here -->

</div>
```

---

## A — Cinematic Centered

Dark gradient background with a warm orange radial glow behind the content. The most versatile option — works for any product or context.

```html
<div class="ac-hero ac-hero--cinematic">
  <p class="ac-hero__eyebrow">RingCentral Labs</p>
  <h1 class="ac-hero__title">Build what's next<br>for RingEX.</h1>
  <p class="ac-hero__sub">
    The official design language for RingCentral products — tokens,
    components, and patterns all in one place.
  </p>
  <div class="ac-hero__cta">
    <a href="/getting-started/" class="ac-hero-btn ac-hero-btn--solid">Get started</a>
    <a href="/components/" class="ac-hero-btn ac-hero-btn--outline">Browse components</a>
  </div>
</div>
```

<div class="ac-hero ac-hero--cinematic" style="border-radius:12px; width:100%; margin-left:0;">
  <p class="ac-hero__eyebrow">RingCentral Labs</p>
  <h1 class="ac-hero__title" style="font-size:2rem;">Build what's next<br>for RingEX.</h1>
  <p class="ac-hero__sub">The official design language for RingCentral products — tokens, components, and patterns all in one place.</p>
  <div class="ac-hero__cta">
    <a href="#" class="ac-hero-btn ac-hero-btn--solid">Get started</a>
    <a href="#" class="ac-hero-btn ac-hero-btn--outline">Browse components</a>
  </div>
</div>

---

## B — Navy / Gradient Split

Two-column layout: copy on a dark navy left panel, a gradient colour field on the right. Place an illustration, icon, or widget in `.ac-hero__visual`.

```html
<div class="ac-hero ac-hero--split">

  <div class="ac-hero__left">
    <p class="ac-hero__eyebrow">Design System</p>
    <h1 class="ac-hero__title">One language.<br>Every surface.</h1>
    <p class="ac-hero__sub">
      Tokens, components, and patterns for RingCentral builders.
    </p>
    <div class="ac-hero__cta">
      <a href="/getting-started/" class="ac-hero-btn ac-hero-btn--solid">Explore →</a>
    </div>
  </div>

  <div class="ac-hero__right">
    <div class="ac-hero__visual">
      <!-- Place an SVG illustration or icon here -->
      ⬡
    </div>
  </div>

</div>
```

<div class="ac-hero ac-hero--split" style="border-radius:12px; width:100%; margin-left:0; min-height:280px;">
  <div class="ac-hero__left">
    <p class="ac-hero__eyebrow">Design System</p>
    <h1 class="ac-hero__title" style="font-size:1.8rem;">One language.<br>Every surface.</h1>
    <p class="ac-hero__sub">Tokens, components, and patterns for RingCentral builders.</p>
    <div class="ac-hero__cta">
      <a href="#" class="ac-hero-btn ac-hero-btn--solid">Explore →</a>
    </div>
  </div>
  <div class="ac-hero__right">
    <div class="ac-hero__visual">⬡</div>
  </div>
</div>

---

## C — Orange Diagonal Slash

White left panel with dark copy, right side cut diagonally with an orange-to-navy gradient. High contrast, directional energy.

```html
<div class="ac-hero ac-hero--slash">
  <div class="ac-hero__copy">
    <p class="ac-hero__eyebrow">v1.0 · Now available</p>
    <h1 class="ac-hero__title">Design tokens,<br>built for scale.</h1>
    <p class="ac-hero__sub">Drop into any MkDocs Material site in minutes.</p>
    <div class="ac-hero__cta">
      <a href="/getting-started/" class="ac-hero-btn ac-hero-btn--navy">Read the docs</a>
    </div>
  </div>
</div>
```

<div class="ac-hero ac-hero--slash" style="border-radius:12px; width:100%; margin-left:0; min-height:260px;">
  <div class="ac-hero__copy">
    <p class="ac-hero__eyebrow">v1.0 · Now available</p>
    <h1 class="ac-hero__title" style="font-size:1.8rem;">Design tokens,<br>built for scale.</h1>
    <p class="ac-hero__sub">Drop into any MkDocs Material site in minutes.</p>
    <div class="ac-hero__cta">
      <a href="#" class="ac-hero-btn ac-hero-btn--navy">Read the docs</a>
    </div>
  </div>
</div>

---

## D — Dark Stats Banner

Very dark background with an orange-to-lavender top rule. Good when you have real numbers worth surfacing — installs, components, API endpoints.

```html
<div class="ac-hero ac-hero--stats">
  <div>
    <p class="ac-hero__eyebrow">RingCentral Design System</p>
    <h1 class="ac-hero__title">Ship consistent UI, fast.</h1>
  </div>
  <div class="ac-hero__stats">
    <div>
      <div class="ac-hero__stat-num">48</div>
      <div class="ac-hero__stat-label">Components</div>
    </div>
    <div>
      <div class="ac-hero__stat-num">12</div>
      <div class="ac-hero__stat-label">Patterns</div>
    </div>
    <div>
      <div class="ac-hero__stat-num">3</div>
      <div class="ac-hero__stat-label">Theme variants</div>
    </div>
    <div>
      <div class="ac-hero__stat-num">100%</div>
      <div class="ac-hero__stat-label">Token-driven</div>
    </div>
  </div>
</div>
```

<div class="ac-hero ac-hero--stats" style="border-radius:12px; width:100%; margin-left:0; min-height:220px;">
  <div>
    <p class="ac-hero__eyebrow">RingCentral Design System</p>
    <h1 class="ac-hero__title" style="font-size:1.8rem;">Ship consistent UI, fast.</h1>
  </div>
  <div class="ac-hero__stats">
    <div><div class="ac-hero__stat-num">48</div><div class="ac-hero__stat-label">Components</div></div>
    <div><div class="ac-hero__stat-num">12</div><div class="ac-hero__stat-label">Patterns</div></div>
    <div><div class="ac-hero__stat-num">3</div><div class="ac-hero__stat-label">Theme variants</div></div>
    <div><div class="ac-hero__stat-num">100%</div><div class="ac-hero__stat-label">Token-driven</div></div>
  </div>
</div>

---

## E — Full-Bleed Gradient Mesh

Orange-to-lavender-to-navy gradient across the full width. Copy sits at the bottom-left for contrast. Use short, punchy headlines — the colour does the heavy lifting.

```html
<div class="ac-hero ac-hero--mesh">
  <span class="ac-hero__pill">New · 2026 Brand</span>
  <h1 class="ac-hero__title">
    Everything your team needs<br>to build on-brand.
  </h1>
  <p class="ac-hero__sub">
    Colors, typography, motion, and components — all in one place.
  </p>
</div>
```

<div class="ac-hero ac-hero--mesh" style="border-radius:12px; width:100%; margin-left:0; min-height:280px;">
  <span class="ac-hero__pill">New · 2026 Brand</span>
  <h1 class="ac-hero__title" style="font-size:1.9rem;">Everything your team needs<br>to build on-brand.</h1>
  <p class="ac-hero__sub">Colors, typography, motion, and components — all in one place.</p>
</div>

---

## CTA buttons

All heroes share the same button classes. Mix and match:

| Class | Style |
|-------|-------|
| `ac-hero-btn--solid` | Orange fill, white text |
| `ac-hero-btn--outline` | Transparent with white border — for dark backgrounds |
| `ac-hero-btn--navy` | Navy fill, white text — for light backgrounds |

```html
<div class="ac-hero__cta">
  <a href="/getting-started/" class="ac-hero-btn ac-hero-btn--solid">Primary</a>
  <a href="/docs/"            class="ac-hero-btn ac-hero-btn--outline">Secondary</a>
</div>
```
