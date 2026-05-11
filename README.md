# mkdocs-material-ringcentral

A self-contained MkDocs plugin that applies the RingCentral 2026 brand layer to [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) sites. Install the plugin, add two lines to `mkdocs.yml`, and your documentation site gets the full RingCentral visual identity — header gradient, sidebar styling, footer, homepage sections, and brand card variants — with no CSS or template files to maintain.

---

## What it does

The plugin injects everything at build time through MkDocs hooks:

- **Brand CSS** — Inter Tight typography, orange primary colour, sidebar gradient, dark mode, RC Labs footer, and the complete homepage section system
- **Brand JS** — animated logo ticker, footer behaviour, and GitHub Pages redirect
- **Jinja2 template** — overrides MkDocs Material's `main.html` to add the RC Labs announce banner and dynamic footer without requiring a `custom_dir`
- **Logo** — the RingCentral colour logo is bundled and set automatically

---

## Installation

```bash
pip install mkdocs-material-ringcentral
```

Requires Python ≥ 3.9, MkDocs ≥ 1.5, and MkDocs Material ≥ 9.0.

---

## Usage

Add the plugin to your `mkdocs.yml`:

```yaml
theme:
  name: material
  font:
    text: Inter Tight
    code: Roboto Mono
  palette:
    - scheme: default
      primary: custom   # required — the plugin sets #FF8800 via CSS variables
      accent: indigo

plugins:
  - material-ringcentral:
  - search:
```

That's it. Run `mkdocs serve` to preview.

---

## Configuration

The plugin accepts one optional key:

```yaml
plugins:
  - material-ringcentral:
      labs_project: app-connect   # optional — see footer section below
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `labs_project` | `string` | `""` | Canonical key of the active Labs project. Used to highlight "You are here" in the footer. |

### Resolving the active project

The plugin resolves the active project in this order:

1. **`labs_project` plugin config** — highest priority, explicit
2. **`extra.labs_project`** — set alongside other extra vars in `mkdocs.yml`
3. **`site_url` auto-detection** — matches the hostname against known Labs project URLs

If no project is resolved (e.g. local development), the footer renders all projects as links with no "You are here" highlight.

---

## Homepage sections

For full-bleed homepage layouts, wrap all sections in `.ac-home` and add front matter to hide the sidebar and TOC:

```markdown
---
hide:
  - navigation
  - toc
---

<div class="ac-home">

  <!-- Hero -->
  <div class="ac-v5-hero">
    <div class="ac-v5-hero__copy">
      <p class="ac-v5-hero__eyebrow">RingCentral Labs</p>
      <h1 class="ac-v5-hero__title">Your headline here.</h1>
      <p class="ac-v5-hero__sub">Supporting description text.</p>
      <div class="ac-v5-hero__cta">
        <a href="/getting-started/" class="ac-v5-btn ac-v5-btn--navy">Get started</a>
        <a href="/docs/" class="ac-v5-btn ac-v5-btn--glass">Documentation</a>
      </div>
    </div>
  </div>

  <!-- Feature cards -->
  <div class="ac-v5-features">
    <p class="ac-v5-features__title">What's included.</p>
    <div class="ac-v5-features__grid">
      <div class="ac-v5-fc">
        <p class="ac-v5-fc__title">Feature name</p>
        <hr class="ac-v5-fc__sep">
        <p class="ac-v5-fc__desc">Brief description.</p>
        <a href="/feature/" class="ac-v5-fc__link">Learn more →</a>
      </div>
    </div>
  </div>

</div>
```

See the [HTML Recipes](https://github.com/ringcentral/mkdocs-material-ringcentral#) for the full set of available sections.

---

## Grid card variants

The plugin extends MkDocs Material's built-in `grid cards` with three brand variants. Add a class alongside `grid cards`:

```markdown
<div class="grid cards rc-bar" markdown>

-   :material-shield-lock-outline: **Authentication**

    ---

    OAuth 2.0 flows and SSO integration patterns.

    [:octicons-arrow-right-24: Read the guide](auth.md)

</div>
```

| Class | Style | Best for |
|-------|-------|----------|
| *(none)* | Muted surface, orange hover ring | Neutral reference navigation |
| `rc-bar` | Left orange accent bar | Inline grids alongside body text |
| `rc-navy` | Dark navy surface, orange accents | High-emphasis landing pages |
| `rc-gradient` | Orange-to-lavender gradient border | Design system and brand documentation |

All variants include auto-numbered decimal counters (`01`, `02`, …) via CSS `counter()` — no markup required.

---

## RC Labs footer

The footer lists RingCentral Labs projects. The active project is highlighted with a "You are here" badge; all others render as links. The `labs_project` config key (or auto-detection from `site_url`) determines which project is active.

**Registered project keys:**

| Key | Project | URL |
|-----|---------|-----|
| `app-connect` | App Connect | appconnect.labs.ringcentral.com |
| `rc-embeddable` | RC Embeddable | github.com/ringcentral/ringcentral-embeddable |
| `call-me` | Call Me | github.com/ringcentral/call-me |
| `ringcentral-mcp` | RingCentral MCP | github.com/ringcentral/ringcentral-mcp |

---

## Bundled assets

All assets are copied to `<site_dir>/_rc/` at build time:

| File | Purpose |
|------|---------|
| `ringcentral.css` | Full brand stylesheet |
| `ringcentral.js` | Ticker animation and footer JS |
| `extra.js` | GitHub Pages → canonical URL redirect |
| `RingCentral_logo_color.png` | Site logo |

---

## Recommended `mkdocs.yml`

```yaml
site_name: Your Site Name
site_url: https://your-site.ringcentral.com

theme:
  name: material
  font:
    text: Inter Tight
    code: Roboto Mono
  features:
    - navigation.path
    - navigation.sections
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.top
    - search.highlight
    - content.tabs.link
    - content.code.copy
    - content.code.annotate
  palette:
    - scheme: default
      primary: custom
      accent: indigo
    - scheme: slate
      primary: black
      accent: indigo

plugins:
  - material-ringcentral:
  - search:
      separator: '[\s\-\.]+'

markdown_extensions:
  - attr_list
  - md_in_html
  - admonition
  - footnotes
  - tables
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.details
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - toc:
      permalink: true
```

---

## Announce banner

The announce banner (the strip above the navigation) is project-aware. App Connect gets the 2.0 beta message; other registered projects get a relevant banner; unregistered sites get no banner.

To add a custom banner, override `main.html` using `custom_dir: overrides` and redefine the `{% block announce %}` block. See the [MkDocs Material docs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-header/#announcement-bar) for details.

---

## License

MIT © 2023–2026 RingCentral, Inc.
