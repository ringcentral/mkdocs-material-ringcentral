# HTML Recipes

Copy-paste HTML templates that work directly with the `material-ringcentral` theme. Every class in these recipes is defined in `ringcentral.css` — no extra stylesheets needed.

---

## How to use these recipes

All recipes are raw HTML blocks that go inside a Markdown file. MkDocs Material renders HTML alongside Markdown, so you can mix them freely.

**Required front matter for homepage-style pages** (removes sidebar, TOC, and padding):

```yaml
---
hide:
  - navigation
  - toc
---
```

**The `.ac-home` wrapper** is required for any page that uses full-bleed sections. It signals to the CSS that the page should have its padding and background stripped so sections can extend edge-to-edge.

```html
<div class="ac-home">
  <!-- All full-bleed sections go here -->
</div>
```

**Full-bleed technique:** Sections inside `.ac-home` break out of MkDocs Material's content container using:

```css
width: 100vw;
margin-left: calc(50% - 50vw);
```

This pulls each section's left edge to the viewport edge and spans the full browser width, regardless of the content column width.

---

## Available recipes

<div class="grid cards" markdown>

-   :material-home-outline: **[Homepage](homepage.md)**

    ---

    Full homepage build: gradient hero with call widget, value pillars, animated logo ticker, feature card grid, dark AI section, and developer tile.

-   :material-card-outline: **[Cards](cards.md)**

    ---

    All card patterns: feature cards (`ac-v5-fc`), general purpose cards (`rc-card`), CRM partner cards, and stat cards.

-   :material-file-document-outline: **[Content Pages](content-pages.md)**

    ---

    Standard content page layouts: section intros, step-by-step guides, API reference tables, and two-column layouts.

</div>
