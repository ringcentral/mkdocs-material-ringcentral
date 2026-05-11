# Grid cards (Markdown)

The `grid cards` pattern is the primary navigation component for documentation index pages. It requires only Markdown list syntax inside a single `<div>` attribute — no HTML structure, no class nesting.

---

## Basic syntax

Every grid card is a list item (`-`) with three parts: an icon + bold title on the first line, a `---` separator, and body content.

```markdown
<div class="grid cards" markdown>

-   :material-icon-name: **Card title**

    ---

    Card description text. One to three sentences. Can include
    inline `code`, *emphasis*, or links.

    [:octicons-arrow-right-24: Link label](target.md)

-   :material-icon-name: **Card title**

    ---

    Another card's description.

    [:octicons-arrow-right-24: Link label](target.md)

</div>
```

The `markdown` attribute on the `<div>` tells MkDocs Material to process the contents as Markdown. Without it, the list renders as raw HTML.

!!! tip "Indentation matters"
    Body content inside each list item must be indented by **four spaces**. The `---` separator and all subsequent lines — including the link — must match that indent level. Misaligned content will break the card structure.

---

## RingCentral brand variants

Add a single class to the `<div>` alongside `grid cards` to apply a brand style. The rendered example appears below each code block.

### Bar (`rc-bar`)

Left orange accent bar. Suited to pages where the grid sits alongside body text.

```markdown
<div class="grid cards rc-bar" markdown>

-   :material-shield-lock-outline: **Authentication**

    ---

    OAuth 2.0 flows, token lifecycle, and SSO integration patterns.

    [:octicons-arrow-right-24: Read the guide](../getting-started.md)

-   :material-api: **REST API**

    ---

    Endpoint reference, authentication headers, and rate limits.

    [:octicons-arrow-right-24: API reference](../resources/index.md)

-   :material-webhook: **Webhooks**

    ---

    Event subscriptions, payload schemas, and delivery guarantees.

    [:octicons-arrow-right-24: Webhook guide](../resources/index.md)

-   :material-code-braces: **SDKs**

    ---

    Official client libraries for JavaScript, Python, Java, and C#.

    [:octicons-arrow-right-24: Choose an SDK](../getting-started.md)

</div>
```

<div class="grid cards rc-bar" markdown>

-   :material-shield-lock-outline: **Authentication**

    ---

    OAuth 2.0 flows, token lifecycle, and SSO integration patterns.

    [:octicons-arrow-right-24: Read the guide](../getting-started.md)

-   :material-api: **REST API**

    ---

    Endpoint reference, authentication headers, and rate limits.

    [:octicons-arrow-right-24: API reference](../resources/index.md)

-   :material-webhook: **Webhooks**

    ---

    Event subscriptions, payload schemas, and delivery guarantees.

    [:octicons-arrow-right-24: Webhook guide](../resources/index.md)

-   :material-code-braces: **SDKs**

    ---

    Official client libraries for JavaScript, Python, Java, and C#.

    [:octicons-arrow-right-24: Choose an SDK](../getting-started.md)

</div>

---

### Navy (`rc-navy`)

Dark navy surface with orange accents. Best for high-emphasis landing pages.

```markdown
<div class="grid cards rc-navy" markdown>

-   :material-phone-log: **Call logging**

    ---

    Every call logged automatically — inbound, outbound, missed.
    No manual entry, ever.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-account-search: **Contact matching**

    ---

    Caller ID resolution against your CRM in under 200 ms.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-monitor-account: **Screen pop**

    ---

    The right record surfaces before you say hello.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-robot-outline: **AI summaries**

    ---

    Post-call notes drafted from the transcript, ready to save.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

</div>
```

<div class="grid cards rc-navy" markdown>

-   :material-phone-log: **Call logging**

    ---

    Every call logged automatically — inbound, outbound, missed.
    No manual entry, ever.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-account-search: **Contact matching**

    ---

    Caller ID resolution against your CRM in under 200 ms.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-monitor-account: **Screen pop**

    ---

    The right record surfaces before you say hello.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

-   :material-robot-outline: **AI summaries**

    ---

    Post-call notes drafted from the transcript, ready to save.

    [:octicons-arrow-right-24: Learn more](../getting-started.md)

</div>

---

### Gradient (`rc-gradient`)

Orange-to-lavender gradient border. Signature style for design-system and brand documentation.

```markdown
<div class="grid cards rc-gradient" markdown>

-   :material-palette-outline: **Colors**

    ---

    Brand tokens, semantic roles, and WCAG contrast ratios.

    [:octicons-arrow-right-24: View palette](../foundations/colors.md)

-   :material-format-font: **Typography**

    ---

    Inter Tight type scale, weights, and line-length guidelines.

    [:octicons-arrow-right-24: View type scale](../foundations/typography.md)

-   :material-grid: **Spacing**

    ---

    4px base grid, component defaults, and CSS custom properties.

    [:octicons-arrow-right-24: View spacing](../foundations/spacing.md)

-   :material-motion-play-outline: **Motion**

    ---

    Duration tokens, easing curves, and reduced-motion guidance.

    [:octicons-arrow-right-24: View motion](../foundations/motion.md)

</div>
```

<div class="grid cards rc-gradient" markdown>

-   :material-palette-outline: **Colors**

    ---

    Brand tokens, semantic roles, and WCAG contrast ratios.

    [:octicons-arrow-right-24: View palette](../foundations/colors.md)

-   :material-format-font: **Typography**

    ---

    Inter Tight type scale, weights, and line-length guidelines.

    [:octicons-arrow-right-24: View type scale](../foundations/typography.md)

-   :material-grid: **Spacing**

    ---

    4px base grid, component defaults, and CSS custom properties.

    [:octicons-arrow-right-24: View spacing](../foundations/spacing.md)

-   :material-motion-play-outline: **Motion**

    ---

    Duration tokens, easing curves, and reduced-motion guidance.

    [:octicons-arrow-right-24: View motion](../foundations/motion.md)

</div>

---

## Card count and column layout

The grid fills columns automatically using `repeat(auto-fill, minmax(10rem, 1fr))`. The practical column counts by card count are:

| Cards | Columns (desktop) | Notes |
|-------|-------------------|-------|
| 2 | 2 | Natural 50/50 split |
| 3 | 3 | Fills the row evenly |
| 4 | 4 or 2×2 | Depends on viewport width |
| 5–6 | Wraps to multiple rows | Avoid odd counts — the last row looks unbalanced |
| 8 | 4×2 | Clean grid, the maximum recommended |

For a deliberate 2-column grid at any count, override the column width:

```html
<div class="grid cards" style="grid-template-columns: repeat(2, minmax(0,1fr));" markdown>
```

---

## Cards without links

The `[:octicons-arrow-right-24: Label](url)` link line is optional. Omit it for informational cards that don't need a call to action:

```markdown
<div class="grid cards" markdown>

-   :material-check-circle-outline: **WCAG AA**

    ---

    All interactive elements meet 4.5:1 contrast on default and slate themes.

-   :material-check-circle-outline: **Keyboard navigation**

    ---

    Tab order follows reading order. All interactive elements are reachable
    without a mouse.

</div>
```

---

## Choosing a variant

| Variant | Class | When to use |
|---------|-------|-------------|
| Default | *(none)* | Neutral navigation inside reference pages |
| Bar | `rc-bar` | Any page where the grid sits within body content |
| Navy | `rc-navy` | Standalone landing pages, getting-started hubs |
| Gradient | `rc-gradient` | Design system, brand, and component documentation |

See the [Grid cards component page](../components/grid-cards.md) for the full spec including colour values, hover states, and dark-mode behaviour.
