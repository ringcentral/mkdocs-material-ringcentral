# Recipes

Copy-paste patterns for building pages with the `material-ringcentral` theme. HTML recipes use raw markup and the theme's CSS classes. Markdown recipes use only standard MkDocs Material syntax — no HTML required.

---

## HTML recipes

Raw HTML blocks that go inside any `.md` file. Every class is defined in `ringcentral.css` — no extra stylesheets needed.

**Required front matter for homepage-style pages** (removes sidebar, TOC, and padding):

```yaml
---
hide:
  - navigation
  - toc
---
```

**The `.ac-home` wrapper** is required for any page that uses full-bleed sections:

```html
<div class="ac-home">
  <!-- full-bleed sections go here -->
</div>
```

<div class="grid cards" markdown>

-   :material-home-outline: **[Homepage](homepage.md)**

    ---

    Full homepage build: gradient hero with call widget, value pillars, animated logo ticker, feature card grid, dark AI section, and developer tile.

-   :material-card-outline: **[Cards](cards.md)**

    ---

    All card patterns: feature cards (`ac-v5-fc`), general purpose cards (`rc-card`), CRM partner cards, and AI section cards.

-   :material-file-document-outline: **[Content Pages](content-pages.md)**

    ---

    Standard content page layouts: section intros, step-by-step guides, API reference tables, and two-column do/don't blocks.

</div>

---

## Markdown recipes

Pure Markdown patterns — no HTML required. All syntax relies only on the extensions declared in `mkdocs.yml`.

<div class="grid cards" markdown>

-   :material-card-multiple-outline: **[Grid cards](../md-recipes/grid-cards.md)**

    ---

    Navigation grids with the three RingCentral brand variants — `rc-bar`, `rc-navy`, and `rc-gradient`. Rendered examples included.

-   :material-alert-box-outline: **[Admonitions](../md-recipes/admonitions.md)**

    ---

    All supported call-out types rendered with their colour and icon: note, tip, warning, danger, success, and more.

-   :material-tab: **[Tabs](../md-recipes/tabs.md)**

    ---

    Tabbed content for code variants, platform-specific steps, and side-by-side comparisons.

-   :material-table: **[Tables](../md-recipes/tables.md)**

    ---

    Reference tables, comparison matrices, and API parameter tables with alignment and width control.

</div>
