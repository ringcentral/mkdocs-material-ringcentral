# Getting Started

Everything you need to set up the RingCentral design language in a new or existing project.

---

## Prerequisites

| Requirement | Minimum version |
|-------------|-----------------|
| Python | 3.8+ |
| MkDocs | 1.5+ |
| mkdocs-material | 9.0+ |

---

## Installation

### 1. Install the plugin

```bash
pip install mkdocs-material-ringcentral
```

For a pinned install in a project:

```bash
pip install "mkdocs-material-ringcentral>=1.0,<2.0"
```

Add it to your `requirements.txt`:

```text
mkdocs>=1.5
mkdocs-material>=9.0
mkdocs-material-ringcentral>=1.0
```

### 2. Configure mkdocs.yml

Add the plugin to your configuration. The plugin must come **before** `search` so assets are registered in the correct order.

```yaml
site_name: My Product Docs

theme:
  name: material
  font:
    text: Inter Tight
    code: Roboto Mono
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - content.code.copy

plugins:
  - material-ringcentral   # (1)!
  - search

markdown_extensions:
  - admonition
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

1. This is the only required change. The plugin injects all CSS, JS, the logo, and the custom footer automatically.

### 3. Build or serve

```bash
# Development server with live reload
mkdocs serve

# Production build
mkdocs build
```

---

## What the plugin injects

The `material-ringcentral` plugin automatically applies the following without any additional configuration:

| Asset | Description |
|-------|-------------|
| `_rc/ringcentral.css` | Full brand token and component stylesheet |
| `_rc/ringcentral.js` | Hero canvas animation + ticker interaction |
| `_rc/RingCentral_logo_color.png` | RingCentral wordmark logo |
| `main.html` override | Announcement banner + Labs footer |

These assets are bundled inside the Python package and copied to your site at build time. You do **not** need to commit them or reference them manually.

---

## Customization

### Overriding the announcement banner

The plugin template includes a default announcement banner. Override it in your own `custom_dir` template:

```html+jinja title="overrides/main.html"
{% extends "base.html" %}

{% block announce %}
  <strong>New:</strong> Your custom announcement here.
  <a href="/changelog/" class="upgrade-button">See what's new</a>
{% endblock %}
```

Configure `custom_dir` in `mkdocs.yml`:

```yaml
theme:
  name: material
  custom_dir: overrides
```

### Adding extra CSS

Place additional styles in `docs/extra.css` and reference it after the plugin:

```yaml
extra_css:
  - extra.css   # Loaded after ringcentral.css, so you can override tokens here
```

Override design tokens in your extra CSS:

```css
:root {
  /* Override the primary accent color for your sub-product */
  --md-primary-fg-color: #0066CC;
}
```

### Disabling the hero animation

If you don't want the animated canvas on your home page, add this to your `extra.css`:

```css
.md-hero canvas { display: none; }
```

---

## Recommended extensions

These markdown extensions work well with the RingCentral theme and are used throughout this documentation site:

```yaml
markdown_extensions:
  - attr_list          # Add CSS classes directly in Markdown
  - md_in_html         # Use Markdown inside HTML blocks
  - admonition         # Note/warning/tip callout blocks
  - footnotes
  - tables
  - pymdownx.details   # Collapsible sections
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

---

## Troubleshooting

??? question "Fonts aren't loading"
    The plugin loads Inter Tight and Roboto Mono from Google Fonts. If you're on a network that blocks external requests, self-host the fonts and add `@font-face` declarations to your `extra.css`.

??? question "The logo shows a broken image"
    The plugin sets the logo path to `_rc/RingCentral_logo_color.png`. If your site is deployed to a subpath (e.g. `/docs/`), set `site_url` in `mkdocs.yml` so MkDocs resolves the path correctly.

    ```yaml
    site_url: https://example.com/docs/
    ```

??? question "The hero canvas animation doesn't appear"
    The animation attaches to `.md-hero`, which only appears on pages that define a `hero` block in Material's template. It fires automatically on the home page if you use the `home.html` layout, or you can add `template: home.html` to the front matter of any page.

??? question "My custom `overrides/main.html` conflicts with the plugin"
    The plugin injects its `main.html` via the Jinja2 template loader chain. If you also have an `overrides/main.html`, yours takes precedence. Copy the announce and footer blocks from the [plugin source](https://github.com/ringcentral/mkdocs-material-ringcentral/blob/main/mkdocs_material_ringcentral/templates/main.html) into your override so you don't lose those features.

---

!!! tip "Start from this demo site"
    This documentation site is itself built with `mkdocs-material-ringcentral`. Clone the repo and run `mkdocs serve` from the project root.

    ```bash
    git clone https://github.com/ringcentral/mkdocs-material-ringcentral.git
    cd mkdocs-material-ringcentral
    pip install -r requirements.txt
    mkdocs serve
    ```
