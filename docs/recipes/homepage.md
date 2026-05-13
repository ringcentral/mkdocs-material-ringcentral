# Homepage Recipe

A complete homepage built from the App Connect theme's full-bleed HTML sections. Copy the scaffolding below into your `docs/index.md` and swap in your content.

---

## Required front matter

Every homepage must suppress the sidebar and TOC and wrap everything in `.ac-home`:

```markdown
---
hide:
  - navigation
  - toc
---

<div class="ac-home">
  <!-- sections go here -->
</div>
```

---

## Section 1 — Hero

The gradient hero spans full viewport width. The left side holds eyebrow text, an H1 title, a sub-heading, and CTA buttons. The right side holds any floating widget (shown here as the active-call card from App Connect).

```html
<div class="ac-v5-hero">

  <!-- ── Left: copy ── -->
  <div class="ac-v5-hero__copy">
    <p class="ac-v5-hero__eyebrow">RingCentral Labs</p>

    <h1 class="ac-v5-hero__title">
      Your headline.<br>Second line here.
    </h1>

    <p class="ac-v5-hero__sub">
      One or two sentences describing what this product does and who it's for.
      Keep it under 30 words — the hero is for impact, not detail.
    </p>

    <div class="ac-v5-hero__cta">
      <a href="/getting-started/" class="ac-v5-btn ac-v5-btn--navy">
        Primary action
      </a>
      <a href="/docs/" class="ac-v5-btn ac-v5-btn--glass">
        Secondary action
      </a>
    </div>
  </div>

  <!-- ── Right: widget ── -->
  <div class="ac-v5-widget">
    <div class="ac-v5-widget__active-hd">
      <span class="ac-v5-widget__active-dot"></span>
      <span class="ac-v5-widget__active-label">Active call</span>
      <span class="ac-v5-widget__rec">
        <span class="ac-v5-widget__rec-dot"></span>REC
      </span>
      <span class="ac-v5-widget__duration">4:17</span>
    </div>

    <div class="ac-v5-widget__caller">
      <p class="ac-v5-widget__caller-name">Sarah Johnson</p>
      <p class="ac-v5-widget__caller-meta">Acme Corp · Account Executive</p>
    </div>

    <div class="ac-v5-widget__transcript">
      <p class="ac-v5-widget__transcript-label">Live transcript</p>
      <div class="ac-v5-widget__transcript-exchange">
        <p class="ac-v5-widget__transcript-line ac-v5-widget__transcript-line--them">
          <span class="ac-v5-widget__transcript-who">Sarah</span>
          "The renewal's due end of Q2 — we'd love to revisit pricing."
        </p>
        <p class="ac-v5-widget__transcript-line ac-v5-widget__transcript-line--you">
          <span class="ac-v5-widget__transcript-who">You</span>
          "Absolutely. I'll put together a proposal by Friday."
          <span class="ac-v5-widget__transcript-cursor"></span>
        </p>
      </div>
    </div>

    <div class="ac-v5-widget__crm">
      <span class="ac-v5-widget__crm-pulse"></span>
      Logging to your CRM in real time
    </div>

    <div class="ac-v5-widget__end">End call</div>
  </div>

</div>
```

### Hero without a widget

If you don't need the call widget, omit the right column. The copy will expand to fill the full hero width:

```html
<div class="ac-v5-hero">
  <div class="ac-v5-hero__copy">
    <p class="ac-v5-hero__eyebrow">RingCentral Design System</p>
    <h1 class="ac-v5-hero__title">
      One design language.<br>Every product.
    </h1>
    <p class="ac-v5-hero__sub">
      Tokens, components, and patterns for building consistent,
      accessible RingCentral product experiences.
    </p>
    <div class="ac-v5-hero__cta">
      <a href="/foundations/" class="ac-v5-btn ac-v5-btn--navy">
        Explore foundations
      </a>
      <a href="/getting-started/" class="ac-v5-btn ac-v5-btn--glass">
        Get started
      </a>
    </div>
  </div>
</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-hero" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden;">
  <div class="ac-v5-hero__copy" style="padding: 2rem;">
    <p class="ac-v5-hero__eyebrow">RingCentral Design System</p>
    <h1 class="ac-v5-hero__title">
      One design language.<br>Every product.
    </h1>
    <p class="ac-v5-hero__sub">
      Tokens, components, and patterns for building consistent,
      accessible RingCentral product experiences.
    </p>
    <div class="ac-v5-hero__cta">
      <a href="#" class="ac-v5-btn ac-v5-btn--navy">
        Explore foundations
      </a>
      <a href="#" class="ac-v5-btn ac-v5-btn--glass">
        Get started
      </a>
    </div>
  </div>
</div>

### Button variants

Two button styles are available for use inside `.ac-v5-hero__cta`:

```html
<!-- Dark navy — for the primary CTA -->
<a href="#" class="ac-v5-btn ac-v5-btn--navy">Primary action</a>

<!-- Frosted glass — for the secondary CTA -->
<a href="#" class="ac-v5-btn ac-v5-btn--glass">Secondary action</a>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div style="display:flex; gap:1rem; flex-wrap:wrap; padding:1.5rem 2rem; background:linear-gradient(135deg,#1b2a4a 0%,#0e1f3a 100%); border-radius:12px;">
  <a href="#" class="ac-v5-btn ac-v5-btn--navy">Primary action</a>
  <a href="#" class="ac-v5-btn ac-v5-btn--glass">Secondary action</a>
</div>

---

## Section 2 — Value pillars

Three equal columns on a warm pastel gradient. Used to state the three core value propositions of the product just below the hero.

```html
<div class="ac-v5-pillars">

  <div class="ac-v5-pillar">
    <p class="ac-v5-pillar__num">01 — First value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences describing the first pillar. Keep it
      scannable — this is a teaser, not a full description.
    </p>
  </div>

  <div class="ac-v5-pillar ac-v5-pillar--mid">
    <p class="ac-v5-pillar__num">02 — Second value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences for the second pillar. The
      <code>--mid</code> modifier adds the left and right borders.
    </p>
  </div>

  <div class="ac-v5-pillar">
    <p class="ac-v5-pillar__num">03 — Third value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences for the third pillar.
    </p>
  </div>

</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-pillars" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden;">
  <div class="ac-v5-pillar" style="padding: 2rem;">
    <p class="ac-v5-pillar__num">01 — First value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences describing the first pillar. Keep it
      scannable — this is a teaser, not a full description.
    </p>
  </div>
  <div class="ac-v5-pillar ac-v5-pillar--mid" style="padding: 2rem;">
    <p class="ac-v5-pillar__num">02 — Second value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences for the second pillar. The
      <code>--mid</code> modifier adds the left and right borders.
    </p>
  </div>
  <div class="ac-v5-pillar" style="padding: 2rem;">
    <p class="ac-v5-pillar__num">03 — Third value</p>
    <p class="ac-v5-pillar__text">
      One or two sentences for the third pillar.
    </p>
  </div>
</div>

!!! note "Middle pillar modifier"
    The middle pillar always gets `ac-v5-pillar--mid` to draw the left and right separator borders. On mobile (< 960px) these borders switch to top/bottom automatically.

---

## Section 3 — Animated logo ticker

An infinitely scrolling row of partner or integration logos. The track must contain **two identical sets** of logos to create a seamless loop.

```html
<div class="ac-v5-ticker-wrap">
  <p class="ac-v5-ticker-label">15+ supported integrations and growing</p>
  <div class="ac-v5-ticker-overflow">
    <div class="ac-v5-ticker-track">

      <!-- ── First set (visible) ── -->
      <div class="ac-v5-ticker-pill">
        <a href="/integrations/salesforce/">
          <img src="img/logo-salesforce.png" alt="Salesforce" />
        </a>
      </div>
      <div class="ac-v5-ticker-pill">
        <a href="/integrations/hubspot/">
          <img src="img/logo-hubspot.png" alt="HubSpot" />
        </a>
      </div>
      <div class="ac-v5-ticker-pill">
        <a href="/integrations/clio/">
          <img src="img/logo-clio.png" alt="Clio" />
        </a>
      </div>
      <!-- Add more logos here -->

      <!-- ── Second set (duplicate — required for seamless loop) ── -->
      <div class="ac-v5-ticker-pill" aria-hidden="true">
        <a href="/integrations/salesforce/" tabindex="-1">
          <img src="img/logo-salesforce.png" alt="" />
        </a>
      </div>
      <div class="ac-v5-ticker-pill" aria-hidden="true">
        <a href="/integrations/hubspot/" tabindex="-1">
          <img src="img/logo-hubspot.png" alt="" />
        </a>
      </div>
      <div class="ac-v5-ticker-pill" aria-hidden="true">
        <a href="/integrations/clio/" tabindex="-1">
          <img src="img/logo-clio.png" alt="" />
        </a>
      </div>

    </div>
  </div>
</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-ticker-wrap" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden;">
  <p class="ac-v5-ticker-label">15+ supported integrations and growing</p>
  <div class="ac-v5-ticker-overflow">
    <div class="ac-v5-ticker-track">
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">Salesforce</div>
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">HubSpot</div>
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">Clio</div>
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">Zendesk</div>
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">ServiceNow</div>
      <div class="ac-v5-ticker-pill" style="padding:0.4rem 1rem;">Microsoft Teams</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">Salesforce</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">HubSpot</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">Clio</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">Zendesk</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">ServiceNow</div>
      <div class="ac-v5-ticker-pill" aria-hidden="true" style="padding:0.4rem 1rem;">Microsoft Teams</div>
    </div>
  </div>
</div>

**How the loop works:** The CSS animation translates the track by `-50%` over 36 seconds. Since the track contains two identical sets, when the first set scrolls off the left edge the second set has taken its exact position — creating a seamless infinite scroll. `aria-hidden="true"` and `tabindex="-1"` on the duplicate set prevent screen readers and keyboard users from encountering duplicate links.

**Adjusting speed:** Override the animation duration in your `extra.css`:

```css
.ac-v5-ticker-track { animation-duration: 24s; } /* faster */
.ac-v5-ticker-track { animation-duration: 60s; } /* slower */
```

---

## Section 4 — Feature card grid

White cards with an orange top border, arranged in an auto-fill grid. Use for listing product features, capabilities, or content categories.

```html
<div class="ac-v5-features">
  <p class="ac-v5-features__title">
    A complete communications stack, built into your CRM.
  </p>

  <div class="ac-v5-features__grid">

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature name</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        One or two sentences describing what this feature does
        and why it matters. Keep it under 25 words.
      </p>
      <a href="/feature/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Second feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the second feature.
      </p>
      <a href="/feature-2/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Third feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the third feature.
      </p>
      <a href="/feature-3/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Fourth feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the fourth feature.
      </p>
      <a href="/feature-4/" class="ac-v5-fc__link">Learn more →</a>
    </div>

    <!-- Add as many .ac-v5-fc blocks as needed.
         Grid is auto-fill with minmax(0, 1fr) in 4 columns desktop,
         2 columns tablet, 1 column mobile. -->

  </div>
</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-features" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden;">
  <p class="ac-v5-features__title" style="padding: 2rem 2rem 0;">
    A complete communications stack, built into your CRM.
  </p>
  <div class="ac-v5-features__grid" style="padding: 1rem 2rem 2rem;">
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature name</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        One or two sentences describing what this feature does
        and why it matters. Keep it under 25 words.
      </p>
      <a href="#" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Second feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the second feature.
      </p>
      <a href="#" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Third feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the third feature.
      </p>
      <a href="#" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Fourth feature</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">
        Brief description of the fourth feature.
      </p>
      <a href="#" class="ac-v5-fc__link">Learn more →</a>
    </div>
  </div>
</div>

---

## Section 5 — AI / dark navy section

A dark `#1B2A4A` section with an eyebrow label, large title, description, and a 3-column card grid. Use for high-impact enterprise messaging.

```html
<div class="ac-v5-ai-section">

  <p class="ac-v5-ai-section__eyebrow">AI in the enterprise</p>

  <p class="ac-v5-ai-section__title">
    The data layer your AI initiatives are waiting for.
  </p>

  <p class="ac-v5-ai-section__desc">
    Two or three sentences expanding on the title. Describe the
    capability in concrete terms — what it captures, how it works,
    what teams can do with it.
  </p>

  <div class="ac-v5-ai-section__grid">

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Card label</p>
      <p class="ac-v5-ai-card__title">Card headline goes here.</p>
      <p class="ac-v5-ai-card__desc">
        Two or three sentences of supporting detail. Keep each
        card focused on one idea.
      </p>
    </div>

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Second card</p>
      <p class="ac-v5-ai-card__title">Second card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Supporting detail for the second card.
      </p>
    </div>

    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Third card</p>
      <p class="ac-v5-ai-card__title">Third card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Supporting detail for the third card.
      </p>
    </div>

  </div>

  <a href="/ai/" class="ac-v5-ai-section__cta">
    Learn about AI capabilities →
  </a>

</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-ai-section" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden; padding: 2rem;">
  <p class="ac-v5-ai-section__eyebrow">AI in the enterprise</p>
  <p class="ac-v5-ai-section__title">
    The data layer your AI initiatives are waiting for.
  </p>
  <p class="ac-v5-ai-section__desc">
    Two or three sentences expanding on the title. Describe the
    capability in concrete terms — what it captures, how it works,
    what teams can do with it.
  </p>
  <div class="ac-v5-ai-section__grid">
    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Card label</p>
      <p class="ac-v5-ai-card__title">Card headline goes here.</p>
      <p class="ac-v5-ai-card__desc">
        Two or three sentences of supporting detail. Keep each
        card focused on one idea.
      </p>
    </div>
    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Second card</p>
      <p class="ac-v5-ai-card__title">Second card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Supporting detail for the second card.
      </p>
    </div>
    <div class="ac-v5-ai-card">
      <p class="ac-v5-ai-card__label">Third card</p>
      <p class="ac-v5-ai-card__title">Third card headline.</p>
      <p class="ac-v5-ai-card__desc">
        Supporting detail for the third card.
      </p>
    </div>
  </div>
  <a href="#" class="ac-v5-ai-section__cta">
    Learn about AI capabilities →
  </a>
</div>

---

## Section 6 — Developer tile

A three-column gradient section. The left column is a brand statement; the right two columns are "path" cards leading developers to different documentation tracks.

```html
<div class="ac-v5-devtile">

  <!-- ── Col 1: Brand statement ── -->
  <div class="ac-v5-devtile__brand">
    <p class="ac-v5-devtile__eyebrow">Open source · Developer framework</p>
    <p class="ac-v5-devtile__title">
      Connect to any platform in a fraction of the time.
    </p>
    <a href="/developers/" class="ac-v5-devtile__more">
      Read the developer guide →
    </a>
  </div>

  <!-- ── Col 2: Path A (orange accent) ── -->
  <div class="ac-v5-devpath">
    <p class="ac-v5-devpath__num">Path 01</p>
    <p class="ac-v5-devpath__name">Connectors</p>
    <p class="ac-v5-devpath__desc">
      Map call data into your platform's contacts and activity records.
      Build once, log everything automatically.
    </p>
    <a href="/developers/connectors/" class="ac-v5-devpath__cta">
      Build a connector →
    </a>
  </div>

  <!-- ── Col 3: Path B (purple accent) ── -->
  <div class="ac-v5-devpath ac-v5-devpath--plugins">
    <p class="ac-v5-devpath__num">Path 02</p>
    <p class="ac-v5-devpath__name">Plugins</p>
    <p class="ac-v5-devpath__desc">
      Intercept call payloads before the platform — enrich, redact,
      route, or transform data on the way through.
    </p>
    <a href="/developers/plugins/" class="ac-v5-devpath__cta">
      Build a plugin →
    </a>
  </div>

</div>
```

<hr>
<p style="font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#aaa; margin:1.5rem 0 0.5rem;">Preview</p>

<div class="ac-v5-devtile" style="width:100%; margin-left:0; border-radius:12px; overflow:hidden;">
  <div class="ac-v5-devtile__brand" style="padding: 2rem;">
    <p class="ac-v5-devtile__eyebrow">Open source · Developer framework</p>
    <p class="ac-v5-devtile__title">
      Connect to any platform in a fraction of the time.
    </p>
    <a href="#" class="ac-v5-devtile__more">
      Read the developer guide →
    </a>
  </div>
  <div class="ac-v5-devpath" style="padding: 2rem;">
    <p class="ac-v5-devpath__num">Path 01</p>
    <p class="ac-v5-devpath__name">Connectors</p>
    <p class="ac-v5-devpath__desc">
      Map call data into your platform's contacts and activity records.
      Build once, log everything automatically.
    </p>
    <a href="#" class="ac-v5-devpath__cta">
      Build a connector →
    </a>
  </div>
  <div class="ac-v5-devpath ac-v5-devpath--plugins" style="padding: 2rem;">
    <p class="ac-v5-devpath__num">Path 02</p>
    <p class="ac-v5-devpath__name">Plugins</p>
    <p class="ac-v5-devpath__desc">
      Intercept call payloads before the platform — enrich, redact,
      route, or transform data on the way through.
    </p>
    <a href="#" class="ac-v5-devpath__cta">
      Build a plugin →
    </a>
  </div>
</div>

**Path variants:**

| Class | Top border | CTA color |
|-------|------------|-----------|
| `.ac-v5-devpath` | Orange (`--ac-orange-raw`) | Orange |
| `.ac-v5-devpath--plugins` | Purple (`#6D28D9`) | Purple |

---

## Complete homepage template

Putting it all together — a drop-in starting point for any homepage:

```markdown
---
hide:
  - navigation
  - toc
---

<div class="ac-home">

<div class="ac-v5-hero">
  <div class="ac-v5-hero__copy">
    <p class="ac-v5-hero__eyebrow">Your product tagline</p>
    <h1 class="ac-v5-hero__title">Headline line one.<br>Line two here.</h1>
    <p class="ac-v5-hero__sub">One or two sentences about what this does and who it's for.</p>
    <div class="ac-v5-hero__cta">
      <a href="/getting-started/" class="ac-v5-btn ac-v5-btn--navy">Get started</a>
      <a href="/docs/" class="ac-v5-btn ac-v5-btn--glass">Read the docs</a>
    </div>
  </div>
</div>

<div class="ac-v5-pillars">
  <div class="ac-v5-pillar">
    <p class="ac-v5-pillar__num">01 — Value one</p>
    <p class="ac-v5-pillar__text">Brief description of the first value proposition.</p>
  </div>
  <div class="ac-v5-pillar ac-v5-pillar--mid">
    <p class="ac-v5-pillar__num">02 — Value two</p>
    <p class="ac-v5-pillar__text">Brief description of the second value proposition.</p>
  </div>
  <div class="ac-v5-pillar">
    <p class="ac-v5-pillar__num">03 — Value three</p>
    <p class="ac-v5-pillar__text">Brief description of the third value proposition.</p>
  </div>
</div>

<div class="ac-v5-features">
  <p class="ac-v5-features__title">What's inside.</p>
  <div class="ac-v5-features__grid">
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature one</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description.</p>
      <a href="/feature-1/" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature two</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description.</p>
      <a href="/feature-2/" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature three</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description.</p>
      <a href="/feature-3/" class="ac-v5-fc__link">Learn more →</a>
    </div>
    <div class="ac-v5-fc">
      <p class="ac-v5-fc__title">Feature four</p>
      <hr class="ac-v5-fc__sep">
      <p class="ac-v5-fc__desc">Brief description.</p>
      <a href="/feature-4/" class="ac-v5-fc__link">Learn more →</a>
    </div>
  </div>
</div>

</div><!-- /.ac-home -->
```
