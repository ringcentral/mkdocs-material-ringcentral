# Cards Recipe

Three card systems are available in the theme. Each has a distinct visual purpose and set of CSS classes. Mix and match within a page, but use only one card type per grid.

---

## System 1 — Feature cards (`ac-v5-fc`)

White cards with an orange top border. Used in the homepage features section and anywhere you need a clean, linked feature grid.

### Single feature card

```html
<div class="ac-v5-fc">
  <p class="ac-v5-fc__title">Call logging</p>
  <hr class="ac-v5-fc__sep">
  <p class="ac-v5-fc__desc">
    Every call logged automatically — inbound, outbound, missed.
    No manual entry, ever.
  </p>
  <a href="/users/logging/" class="ac-v5-fc__link">Learn about call logging →</a>
</div>
```

### Feature card grid (4-up)

The grid uses `grid-template-columns: repeat(4, minmax(0, 1fr))`. Wraps to 2-col at 960px and 1-col at 560px.

```html
<div class="ac-v5-features">
  <p class="ac-v5-features__title">Section heading goes here.</p>
  <div class="ac-v5-features__grid">

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature one</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description, one or two sentences max.</p>
      <a href="/feature-1/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature two</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description, one or two sentences max.</p>
      <a href="/feature-2/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature three</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description, one or two sentences max.</p>
      <a href="/feature-3/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature four</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description, one or two sentences max.</p>
      <a href="/feature-4/" class="ac-v5-fc__link">Learn more →</a>
    </div>

  </div>
</div>
```

**The `ac-v5-features` wrapper** applies the pastel gradient background and full-bleed width. If you want feature cards without the background section — for example, inline on a content page — drop the wrapper and use just the grid:

```html
<div class="ac-v5-features__grid" style="margin: 1.5rem 0;">
  <div class="ac-v5-fc">…</div>
  <div class="ac-v5-fc">…</div>
  <div class="ac-v5-fc">…</div>
</div>
```

---

## System 2 — General purpose cards (`rc-card`)

Floating white cards with a subtle gradient background and hover shadow. Used for documentation index pages, integration listings, and content navigation.

### Single card

```html
<div class="rc-card">
  <span class="rc-card__icon">🔌</span>
  <p class="rc-card__title">Salesforce connector</p>
  <p class="rc-card__desc">
    Set up call logging, contact matching, and screen pop
    for Salesforce CRM.
  </p>
  <a href="/crm/salesforce/" class="rc-card__link">View setup guide</a>
</div>
```

### Linked card (entire card is clickable)

Wrap the card in an `<a>` tag instead of using `.rc-card__link`:

```html
<a href="/crm/salesforce/" class="rc-card" style="display:block; text-decoration:none;">
  <span class="rc-card__icon">🔌</span>
  <p class="rc-card__title">Salesforce connector</p>
  <p class="rc-card__desc">Set up call logging and contact matching.</p>
</a>
```

### Card grid (auto-fill)

The `rc-cards` grid fills columns automatically with `minmax(220px, 1fr)`:

```html
<div class="rc-cards">

  <div class="rc-card">
    <span class="rc-card__icon">🏢</span>
    <p class="rc-card__title">Salesforce</p>
    <p class="rc-card__desc">Log calls and sync contacts with Salesforce CRM.</p>
    <a href="/crm/salesforce/" class="rc-card__link">Setup guide</a>
  </div>

  <div class="rc-card">
    <span class="rc-card__icon">🎯</span>
    <p class="rc-card__title">HubSpot</p>
    <p class="rc-card__desc">Connect to HubSpot Sales Hub for call logging.</p>
    <a href="/crm/hubspot/" class="rc-card__link">Setup guide</a>
  </div>

  <div class="rc-card">
    <span class="rc-card__icon">⚖️</span>
    <p class="rc-card__title">Clio</p>
    <p class="rc-card__desc">Legal CRM integration for law firms.</p>
    <a href="/crm/clio/" class="rc-card__link">Setup guide</a>
  </div>

  <div class="rc-card">
    <span class="rc-card__icon">📋</span>
    <p class="rc-card__title">NetSuite</p>
    <p class="rc-card__desc">Sync calls and contacts with Oracle NetSuite.</p>
    <a href="/crm/netsuite/" class="rc-card__link">Setup guide</a>
  </div>

</div>
```

**Dark mode:** `rc-card` has a dark mode override that switches to `#151B2B` background with a lighter orange top border automatically — no extra work needed.

### `rc-card` anatomy reference

| Element | Class | Purpose |
|---------|-------|---------|
| Wrapper | `.rc-card` | Card container with gradient background and hover shadow |
| Icon | `.rc-card__icon` | Emoji or icon, displays at 1.3rem in orange |
| Title | `.rc-card__title` | 0.9rem, bold, navy `#1B2A4A` |
| Description | `.rc-card__desc` | 0.8rem, muted gray `#5A6076` |
| Link | `.rc-card__link` | 0.8rem orange link with `→` arrow appended via CSS |

---

## System 3 — CRM partner cards (`crm-mkt__card`)

Full-card link tiles used on integration listing pages. The entire card is the link. A `--partner` modifier adds an orange top border for featured partners.

### Standard partner card

```html
<a href="/crm/salesforce/" class="crm-mkt__card">
  <div class="crm-mkt__card-top">
    <img src="img/crm-logo-salesforce.png" alt="Salesforce" class="crm-mkt__logo" />
  </div>
  <div class="crm-mkt__card-body">
    <p class="crm-mkt__card-name">Salesforce</p>
    <p class="crm-mkt__card-desc">
      Log every call and sync contacts with Salesforce Sales Cloud and Service Cloud.
    </p>
  </div>
  <div class="crm-mkt__card-foot">
    <span class="crm-mkt__cta">View integration →</span>
  </div>
</a>
```

### Featured / partner card (orange top border)

```html
<a href="/crm/salesforce/" class="crm-mkt__card crm-mkt__card--partner">
  <!-- same structure as above -->
</a>
```

### Partner card grid

```html
<div class="crm-mkt__grid">

  <a href="/crm/salesforce/" class="crm-mkt__card crm-mkt__card--partner">
    <div class="crm-mkt__card-top">
      <img src="img/logo-salesforce.png" alt="Salesforce" class="crm-mkt__logo" />
    </div>
    <div class="crm-mkt__card-body">
      <p class="crm-mkt__card-name">Salesforce</p>
      <p class="crm-mkt__card-desc">Sales Cloud, Service Cloud, and Field Service.</p>
    </div>
    <div class="crm-mkt__card-foot">
      <span class="crm-mkt__cta">View integration →</span>
    </div>
  </a>

  <a href="/crm/hubspot/" class="crm-mkt__card">
    <div class="crm-mkt__card-top">
      <img src="img/logo-hubspot.png" alt="HubSpot" class="crm-mkt__logo" />
    </div>
    <div class="crm-mkt__card-body">
      <p class="crm-mkt__card-name">HubSpot</p>
      <p class="crm-mkt__card-desc">HubSpot Sales Hub and Service Hub.</p>
    </div>
    <div class="crm-mkt__card-foot">
      <span class="crm-mkt__cta">View integration →</span>
    </div>
  </a>

  <!-- The grid uses auto-fill with minmax(260px, 1fr) -->

</div>
```

---

## System 4 — AI section cards (`ac-v5-ai-card`)

Dark frosted glass cards for use inside the navy AI section. Not meant to stand alone — always inside `.ac-v5-ai-section`.

```html
<div class="ac-v5-ai-section">
  <p class="ac-v5-ai-section__eyebrow">Section eyebrow</p>
  <p class="ac-v5-ai-section__title">Section headline goes here.</p>
  <p class="ac-v5-ai-section__desc">
    Supporting description of the section. One to three sentences.
  </p>

  <div class="ac-v5-ai-section__grid">

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Card label</p>
      <p class="ac-v5-ai-card__title">Card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Two or three sentences of supporting detail.
      </p>
    </div>

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Card label</p>
      <p class="ac-v5-ai-card__title">Card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Two or three sentences of supporting detail.
      </p>
    </div>

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Card label</p>
      <p class="ac-v5-ai-card__title">Card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Two or three sentences of supporting detail.
      </p>
    </div>

  </div>

  <a href="/feature/" class="ac-v5-ai-section__cta">
    Learn more →
  </a>
</div>
```

---

## Choosing the right card system

| System | Use when |
|--------|----------|
| `ac-v5-fc` | Feature listings on marketing/homepage sections |
| `rc-card` | Documentation index pages, integration catalogs |
| `crm-mkt__card` | Full-card navigation links, partner listings |
| `ac-v5-ai-card` | Inside dark navy sections only |

!!! tip "MkDocs Material card grid"
    MkDocs Material's built-in `grid cards` admonition works well for simple in-page navigation grids. See the [homepage](../index.md) source for an example using the `:material-icon:` emoji syntax. Use it for lightweight navigation; use the theme's card systems for full-bleed sections.
