# Interior Page Hero Recipes

Lead-in banners for content pages — exciting without being overpowering. These sit within the normal content column, above body text, and use the `.ac-page-hero` base class.

Unlike homepage heroes they do **not** require `.ac-home` or any front matter changes. Drop them at the top of any markdown page using `md_in_html`.

---

## F — Left-Bar Accent

The quietest option. A gradient left bar gives the page a brand anchor without competing with the content that follows. Works on any page type.

```html
<div class="ac-page-hero ac-page-hero--bar" markdown>
  <div class="ac-page-hero__body">
    <p class="ac-page-hero__eyebrow">Foundations</p>
    <h1 class="ac-page-hero__title">Color System</h1>
    <p class="ac-page-hero__sub">
      Brand tokens, semantic roles, and dark mode guidance.
    </p>
  </div>
</div>
```

<div class="ac-page-hero ac-page-hero--bar">
  <div class="ac-page-hero__body">
    <p class="ac-page-hero__eyebrow">Foundations</p>
    <h1 class="ac-page-hero__title">Color System</h1>
    <p class="ac-page-hero__sub">Brand tokens, semantic roles, and dark mode guidance.</p>
  </div>
</div>

---

## G — Tinted Surface

A very light orange tint with a gradient underline rule. Warm and inviting without being loud. Good for conceptual or introductory pages.

```html
<div class="ac-page-hero ac-page-hero--tint">
  <p class="ac-page-hero__eyebrow">Components · Actions</p>
  <h1 class="ac-page-hero__title">Buttons</h1>
  <p class="ac-page-hero__sub">
    Hierarchy, variants, states, and when to use each button type.
  </p>
</div>
```

<div class="ac-page-hero ac-page-hero--tint">
  <p class="ac-page-hero__eyebrow">Components · Actions</p>
  <h1 class="ac-page-hero__title">Buttons</h1>
  <p class="ac-page-hero__sub">Hierarchy, variants, states, and when to use each button type.</p>
</div>

---

## H — Navy Strip with Badge

A dark navy banner with an orange left rule and an optional badge on the right. Use the badge for status signals: `Updated`, `Beta`, `New`, `Deprecated`.

```html
<div class="ac-page-hero ac-page-hero--navy">
  <div>
    <p class="ac-page-hero__eyebrow">Foundations</p>
    <h1 class="ac-page-hero__title">Typography</h1>
    <p class="ac-page-hero__sub">Inter Tight · 8 levels · Responsive scale</p>
  </div>
  <div class="ac-page-hero__actions">
    <span class="ac-page-hero__badge">Updated</span>
  </div>
</div>
```

<div class="ac-page-hero ac-page-hero--navy">
  <div>
    <p class="ac-page-hero__eyebrow">Foundations</p>
    <h1 class="ac-page-hero__title">Typography</h1>
    <p class="ac-page-hero__sub">Inter Tight · 8 levels · Responsive scale</p>
  </div>
  <div class="ac-page-hero__actions">
    <span class="ac-page-hero__badge">Updated</span>
  </div>
</div>

---

## I — Gradient Underline Rule

White surface with a strong orange-to-lavender gradient rule separating the title from the description. The most editorial of the interior options — the rule creates a clean visual break that flows naturally into body content.

```html
<div class="ac-page-hero ac-page-hero--rule">
  <div class="ac-page-hero__title-wrap">
    <p class="ac-page-hero__eyebrow">Patterns</p>
    <h1 class="ac-page-hero__title">Empty States</h1>
  </div>
  <div class="ac-page-hero__rule"></div>
  <p class="ac-page-hero__sub">
    Guidance for zero-data views and first-time user onboarding moments.
  </p>
</div>
```

<div class="ac-page-hero ac-page-hero--rule">
  <div class="ac-page-hero__title-wrap">
    <p class="ac-page-hero__eyebrow">Patterns</p>
    <h1 class="ac-page-hero__title">Empty States</h1>
  </div>
  <div class="ac-page-hero__rule"></div>
  <p class="ac-page-hero__sub">Guidance for zero-data views and first-time user onboarding moments.</p>
</div>

---

## J — Copy + Visual Split

Copy column on the left, a dark navy panel on the right that holds an emoji, icon, or illustration. The visual panel is hidden below 860px so mobile layout stays clean.

```html
<div class="ac-page-hero ac-page-hero--visual">
  <div class="ac-page-hero__body">
    <p class="ac-page-hero__eyebrow">Components · Overlay</p>
    <h1 class="ac-page-hero__title">Drawers</h1>
    <p class="ac-page-hero__sub">
      Side panels for detail, context, and forms — without leaving the page.
    </p>
  </div>
  <div class="ac-page-hero__vis">
    🗂
  </div>
</div>
```

<div class="ac-page-hero ac-page-hero--visual">
  <div class="ac-page-hero__body">
    <p class="ac-page-hero__eyebrow">Components · Overlay</p>
    <h1 class="ac-page-hero__title">Drawers</h1>
    <p class="ac-page-hero__sub">Side panels for detail, context, and forms — without leaving the page.</p>
  </div>
  <div class="ac-page-hero__vis">🗂</div>
</div>

---

## K — Breadcrumb-Flush Header

A soft lavender-tinted surface with the page's breadcrumb trail built in. Use on deeply nested pages where orientation context is genuinely useful — component reference pages, API docs, and similar.

```html
<div class="ac-page-hero ac-page-hero--breadcrumb">
  <p class="ac-page-hero__breadcrumb">
    Components ›
    <a href="/components/navigation/">Navigation</a> ›
    Tabs
  </p>
  <h1 class="ac-page-hero__title">Tabs</h1>
  <div class="ac-page-hero__meta">
    <span class="ac-page-hero__tag">Component</span>
    <span class="ac-page-hero__reading">5 min read</span>
  </div>
</div>
```

<div class="ac-page-hero ac-page-hero--breadcrumb">
  <p class="ac-page-hero__breadcrumb">
    Components ›
    <a href="#">Navigation</a> ›
    Tabs
  </p>
  <h1 class="ac-page-hero__title">Tabs</h1>
  <div class="ac-page-hero__meta">
    <span class="ac-page-hero__tag">Component</span>
    <span class="ac-page-hero__reading">5 min read</span>
  </div>
</div>

---

## Shared elements

Any interior hero can include these optional elements:

```html
<!-- Status badge (right side of --navy hero) -->
<span class="ac-page-hero__badge">Updated</span>

<!-- Taxonomy tag (used in --breadcrumb meta row) -->
<span class="ac-page-hero__tag">Component</span>

<!-- Reading time or similar metadata -->
<span class="ac-page-hero__reading">5 min read</span>
```
