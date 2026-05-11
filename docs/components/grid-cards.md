# Grid cards

MkDocs Material's built-in `grid cards` component is extended by three theme variants that bring RingCentral brand personality to documentation navigation grids. Each variant is applied by adding a single modifier class alongside the standard `grid cards` class — no custom HTML, no extra markup.

---

## Variants

=== "Bar (`rc-bar`)"

    Left orange accent bar with a warm shadow on hover. The lightest touch of the three — suited to any page where the card grid sits alongside body text.

    ```html
    <div class="grid cards rc-bar" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA.

        [:octicons-arrow-right-24: Browse library](index.md)

    </div>
    ```

    <div class="grid cards rc-bar" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns for enterprise deployments.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA support.

        [:octicons-arrow-right-24: Browse library](index.md)

    -   :material-palette-outline: **Design tokens**

        ---

        Color, spacing, radius, and motion values as CSS custom properties synced to Figma.

        [:octicons-arrow-right-24: View tokens](../foundations/colors.md)

    -   :material-layers-outline: **Foundations**

        ---

        Typography scale, grid system, elevation, and motion principles.

        [:octicons-arrow-right-24: Explore](../foundations/index.md)

    </div>

=== "Navy (`rc-navy`)"

    Dark navy surface with orange text accents. Matches the tone of the homepage hero and AI sections — use it for high-emphasis navigation grids that are the primary content of a page.

    ```html
    <div class="grid cards rc-navy" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA.

        [:octicons-arrow-right-24: Browse library](index.md)

    </div>
    ```

    <div class="grid cards rc-navy" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns for enterprise deployments.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA support.

        [:octicons-arrow-right-24: Browse library](index.md)

    -   :material-palette-outline: **Design tokens**

        ---

        Color, spacing, radius, and motion values as CSS custom properties synced to Figma.

        [:octicons-arrow-right-24: View tokens](../foundations/colors.md)

    -   :material-layers-outline: **Foundations**

        ---

        Typography scale, grid system, elevation, and motion principles.

        [:octicons-arrow-right-24: Explore](../foundations/index.md)

    </div>

=== "Gradient (`rc-gradient`)"

    White surface framed by an orange-to-lavender gradient border drawn from the RingCentral brand palette. Uses `background-clip: padding-box / border-box` — no wrapper element required.

    ```html
    <div class="grid cards rc-gradient" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA.

        [:octicons-arrow-right-24: Browse library](index.md)

    </div>
    ```

    <div class="grid cards rc-gradient" markdown>

    -   :material-shield-lock-outline: **Authentication**

        ---

        OAuth 2.0 flows, token lifecycle, and SSO integration patterns for enterprise deployments.

        [:octicons-arrow-right-24: Read the guide](../getting-started.md)

    -   :material-puzzle-outline: **Components**

        ---

        Buttons, inputs, dialogs — production-ready with dark mode and WCAG AA support.

        [:octicons-arrow-right-24: Browse library](index.md)

    -   :material-palette-outline: **Design tokens**

        ---

        Color, spacing, radius, and motion values as CSS custom properties synced to Figma.

        [:octicons-arrow-right-24: View tokens](../foundations/colors.md)

    -   :material-layers-outline: **Foundations**

        ---

        Typography scale, grid system, elevation, and motion principles.

        [:octicons-arrow-right-24: Explore](../foundations/index.md)

    </div>

---

## Specs

| Property | Base | `rc-bar` | `rc-navy` | `rc-gradient` |
|----------|------|----------|-----------|---------------|
| Background | `--md-code-bg-color` | `--md-default-bg-color` | `#1B2A4A` | `--md-default-bg-color` |
| Border at rest | `1px solid` lightest fg | `1px` lightest + `3px left` orange | `1px solid rgba(255,136,0,.22)` | `1.5px transparent` + gradient |
| Border radius | `10px` | `0 10px 10px 0` | `10px` | `10px` |
| Hover affordance | Orange ring fade-in | Warm orange `box-shadow` | Orange ring fade-in | Soft orange `box-shadow` |
| Title color | Inherited | Inherited | `#F1F5F9` | Inherited |
| Description color | Inherited | Inherited | `#8B9BB8` | Inherited |
| Link color | `--md-primary-fg-color` | `--md-primary-fg-color` | `#FFAA40` | `--md-primary-fg-color` |
| Counter badge | Muted monospace | Muted monospace | `rgba(255,255,255,.22)` | Muted monospace |

---

## Auto-numbered counters

All three variants inherit the base `grid cards` behaviour: a CSS counter (`decimal-leading-zero`) is rendered at top-right of each card automatically — `01`, `02`, `03` — with no markup required. The `::before` pseudo-element is positioned `absolute; top: 1rem; right: 1rem` and colour-adjusted per variant.

To suppress the counter on a specific grid, add a `no-counter` class and a scoped rule:

```css
.md-typeset .grid.cards.no-counter > ul > li::before { display: none; }
```

---

## When to use

**`rc-bar`** is the everyday choice. It introduces brand colour without imposing a strong surface, so it works alongside body text, inside tabbed content, and on dense reference pages.

**`rc-navy`** is for high-emphasis, standalone navigation pages — a product landing, a section overview, or a getting-started hub. Avoid placing it on a page that already has a dark hero or heavily coloured header, and don't mix it with body text in the same content flow.

**`rc-gradient`** is the signature option for design-system pages. The orange-to-lavender gradient signals brand identity without colouring the card interior, keeping content readable across all contexts and in both light and dark mode.

---

## Accessibility

!!! warning "Colour contrast in `rc-navy`"
    The muted `#8B9BB8` description text on `#1B2A4A` passes WCAG AA at 4.6:1 but does not reach AAA (7:1). If description text carries critical navigational information, prefer `rc-bar` or `rc-gradient` instead.

!!! note "Link colour on white"
    RingCentral orange (`#FF8800`) on white achieves a 3.1:1 ratio — passing AA for large text (18px+ or 14px bold) only. The `→` icon suffix and underline-on-hover ensure a non-colour affordance is always present, satisfying [WCAG 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html).
