# Grid cards (Markdown)

The `grid cards` pattern is the primary navigation component for documentation index pages. Add a single modifier class alongside `grid cards` to apply a RingCentral brand style.

---

## Syntax

```markdown
<div class="grid cards rc-bar" markdown>

-   :material-icon-name: **Card title**

    ---

    Card description. One to three sentences.

    [:octicons-arrow-right-24: Link label](target.md)

</div>
```

!!! tip "Indentation"
    Body content inside each list item must be indented by **four spaces**. The `---` separator and link line must match that indent level.

---

## Accepted class names

| Class | Style |
|-------|-------|
| *(none)* | Muted surface, orange hover-ring fade-in |
| `rc-bar` | White surface, left orange accent bar, warm shadow on hover |
| `rc-navy` | Dark navy surface, orange text accents, lifted on dark hover |
| `rc-gradient` | White surface, orange-to-lavender gradient border |

---

## Examples

### Default

<div class="grid cards" markdown>

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

### `rc-bar`

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

### `rc-navy`

<div class="grid cards rc-navy" markdown>

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

### `rc-gradient`

<div class="grid cards rc-gradient" markdown>

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

## When to use each variant

| Variant | Best for |
|---------|----------|
| Default | Neutral reference navigation inside content pages |
| `rc-bar` | Grids that sit alongside body text |
| `rc-navy` | Standalone landing pages and getting-started hubs |
| `rc-gradient` | Design system, brand, and component documentation |

See the [Grid cards component page](../components/grid-cards.md) for the full spec including colour values, hover states, dark-mode behaviour, and the auto-numbered counter system.
