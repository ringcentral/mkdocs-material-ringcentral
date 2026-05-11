# Foundations

The foundations are the atoms of the design system — the raw decisions about color, type, space, and motion that flow into every component and layout. Consistent use of these tokens is what makes the RingCentral design language feel coherent across products and platforms.

---

<div class="grid cards" markdown>

-   :material-palette: **Colors**

    ---

    Brand palette, semantic roles, accessible combinations, and dark-mode mappings.

    [:octicons-arrow-right-24: Color system](colors.md)

-   :material-format-font: **Typography**

    ---

    Type scale, font families, weight usage, and line-height guidelines.

    [:octicons-arrow-right-24: Typography](typography.md)

-   :material-ruler: **Spacing**

    ---

    The 4px base grid, spacing scale, and rules for applying space consistently.

    [:octicons-arrow-right-24: Spacing](spacing.md)

-   :material-grid: **Grid & Layout**

    ---

    Responsive column grids, breakpoints, containers, and layout templates.

    [:octicons-arrow-right-24: Grid & Layout](grid.md)

-   :material-shape: **Icons**

    ---

    Icon library, sizing guidelines, usage rules, and accessibility requirements.

    [:octicons-arrow-right-24: Icons](icons.md)

-   :material-motion-play: **Motion**

    ---

    Duration tokens, easing curves, and animation guidelines.

    [:octicons-arrow-right-24: Motion](motion.md)

-   :material-layers: **Elevation**

    ---

    Shadow tokens, z-index scale, and surface hierarchy.

    [:octicons-arrow-right-24: Elevation](elevation.md)

</div>

---

## Using design tokens

All foundations are expressed as CSS custom properties (design tokens). Use tokens instead of raw values so your UI automatically inherits any future brand updates.

```css
/* Do this */
color: var(--ac-coral);
font-family: var(--md-text-font);

/* Not this */
color: #FF7A35;
font-family: "Inter Tight", sans-serif;
```

Tokens are injected by the `material-ringcentral` plugin and available globally in any stylesheet loaded after `ringcentral.css`.
