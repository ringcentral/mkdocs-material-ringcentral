# Cards

Cards are contained surfaces that group related content and actions around a single subject. They create visual separation between discrete items in a list or grid.

---

## Variants

### Basic card

A simple container with padding and a subtle shadow. Use for non-interactive groupings.

```html
<div class="rc-card">
  <h3>Card title</h3>
  <p>Supporting description text goes here. Keep it concise.</p>
</div>
```

### Card with media

An image or illustration header above the content body.

```html
<div class="rc-card rc-card--media">
  <div class="rc-card__media">
    <img src="cover.png" alt="Feature illustration" />
  </div>
  <div class="rc-card__body">
    <h3>Feature name</h3>
    <p>Description of the feature.</p>
  </div>
</div>
```

### Card with actions

Cards can include action buttons in a footer region.

```html
<div class="rc-card">
  <div class="rc-card__body">
    <h3>Salesforce integration</h3>
    <p>Sync call logs and contacts with your Salesforce CRM automatically.</p>
  </div>
  <div class="rc-card__actions">
    <button class="md-button md-button--primary">Connect</button>
    <button class="md-button">Learn more</button>
  </div>
</div>
```

### Clickable / linked card

The entire card surface acts as a link. Use for navigation-first cards (product listings, doc categories).

```html
<a class="rc-card rc-card--link" href="/docs/salesforce">
  <h3>Salesforce</h3>
  <p>Setup and configuration guide.</p>
  <span class="rc-card__arrow" aria-hidden="true">→</span>
</a>
```

### Stat card

Displays a single metric with a label and optional trend indicator.

```html
<div class="rc-card rc-card--stat">
  <span class="rc-stat__label">Active connectors</span>
  <span class="rc-stat__value">24</span>
  <span class="rc-stat__trend rc-stat__trend--up">+3 this week</span>
</div>
```

---

## Sizes

| Property | Value |
|----------|-------|
| Border radius | `8px` |
| Padding | `24px` |
| Shadow (rest) | `shadow-sm` |
| Shadow (hover) | `shadow-md` |
| Background | `#FFFFFF` |
| Border | `1px solid rgba(221,208,216,0.5)` |
| Gap between children | `16px` |

---

## States

| State | Treatment |
|-------|-----------|
| Default | `shadow-sm`, standard border |
| Hover (clickable card) | `shadow-md`, slight `translateY(-2px)` |
| Active | `shadow-xs`, `translateY(0)` |
| Focus (clickable card) | Focus ring on the `<a>` or container |
| Selected | `1.5px solid --ac-orange-raw` border, `--ac-peach` background tint |
| Loading | Replaced by [skeleton loader](loaders.md) |

---

## Layout guidelines

Cards in a grid should have equal heights. Use CSS Grid with `align-items: stretch`:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  align-items: stretch;
}
```

---

## Usage guidelines

**Do:**

- Group cards of the same type together.
- Keep card content scannable — lead with the most important information.
- Use consistent card heights within a grid by standardizing content structure.
- Provide an accessible name for linked cards.

**Don't:**

- Nest cards inside cards.
- Mix interactive and non-interactive cards in the same group.
- Use a card for a single piece of text — a list item or inline text is more appropriate.
- Overload cards with too much information — if a card needs scrolling, redesign.

---

## Accessibility

- Linked cards must use `<a href="...">` so they are keyboard focusable.
- Cards with only icon links need `aria-label` on the card or the link.
- Action buttons inside a non-linked card are individually focusable and do not need special treatment.
- Group multiple clickable cards in a `<ul>/<li>` structure for screen reader navigation.

```html
<ul class="card-grid" role="list">
  <li>
    <a class="rc-card rc-card--link" href="/crm/salesforce">
      Salesforce connector
    </a>
  </li>
  <li>
    <a class="rc-card rc-card--link" href="/crm/hubspot">
      HubSpot connector
    </a>
  </li>
</ul>
```
