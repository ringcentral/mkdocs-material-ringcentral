# Content Pages Recipe

Standard content pages use MkDocs Material's document layout — sidebar, TOC, and content column — without any full-bleed overrides. These recipes show how to combine Markdown with the theme's HTML classes to create rich content pages.

---

## Standard content page

A regular documentation page needs no special front matter. The sidebar, breadcrumbs, and TOC appear automatically:

```markdown
# Page title

Introductory paragraph. Keep it to 2–3 sentences — this appears just below
the page title and sets context for everything that follows.

---

## First section

Content for the first section.

## Second section

Content for the second section.
```

---

## Section intro page (with `rc-cards`)

Index pages for major sections lead with a short intro paragraph then a card grid linking to child pages. This is the same pattern used on the [Components index](../components/index.md).

```markdown
# Components

Brief description of what this section contains and who it's for.

---

<div class="rc-cards">

  <div class="rc-card">
    <span class="rc-card__icon">🔘</span>
    <p class="rc-card__title">Buttons</p>
    <p class="rc-card__desc">
      Primary, secondary, tertiary, icon, and destructive action variants.
    </p>
    <a href="buttons/" class="rc-card__link">View component</a>
  </div>

  <div class="rc-card">
    <span class="rc-card__icon">✏️</span>
    <p class="rc-card__title">Inputs</p>
    <p class="rc-card__desc">
      Text fields, textareas, and field states.
    </p>
    <a href="inputs/" class="rc-card__link">View component</a>
  </div>

  <div class="rc-card">
    <span class="rc-card__icon">🃏</span>
    <p class="rc-card__title">Cards</p>
    <p class="rc-card__desc">
      Content containers with optional media and actions.
    </p>
    <a href="cards/" class="rc-card__link">View component</a>
  </div>

</div>
```

---

## Integration / CRM page intro (with hero-style header)

Product pages for individual integrations use a light header section with the partner logo and key stats, then drop into standard content.

```html
<div class="crm-mkt__hero">
  <div>
    <img src="../img/crm-logo-salesforce.png"
         alt="Salesforce"
         style="height:48px; margin-bottom:1rem; display:block;" />
    <h1 class="crm-mkt__hero-title">Salesforce integration</h1>
    <p class="crm-mkt__hero-sub">
      Log every call, sync contacts, and surface the right CRM record
      the moment a call arrives — all without leaving RingEX.
    </p>
    <div class="crm-mkt__hero-stats">
      <div class="crm-mkt__stat">
        <span class="crm-mkt__stat-num">100%</span>
        <span class="crm-mkt__stat-label">Calls logged</span>
      </div>
      <div class="crm-mkt__stat">
        <span class="crm-mkt__stat-num">0</span>
        <span class="crm-mkt__stat-label">Manual entries</span>
      </div>
      <div class="crm-mkt__stat">
        <span class="crm-mkt__stat-num">Real-time</span>
        <span class="crm-mkt__stat-label">CRM sync</span>
      </div>
    </div>
  </div>
</div>
```

The `.crm-mkt__hero` class applies a pastel gradient background and handles responsive layout. The `crm-mkt__stat` elements display in a horizontal row with a left-border separator between them.

---

## Component reference page structure

Component pages follow a consistent structure. Using the theme's admonition and tab systems:

````markdown
# Buttons

Brief description of what this component is and when to use it.

---

## Variants

=== "Primary"
    ```html
    <button class="md-button md-button--primary">Get started</button>
    ```

=== "Secondary"
    ```html
    <button class="md-button">Learn more</button>
    ```

=== "Destructive"
    ```html
    <button class="md-button md-button--danger">Delete</button>
    ```

---

## Specs

| Property | Value |
|----------|-------|
| Border radius | 4px |
| Default height | 40px |
| Font weight | 700 |

---

## Accessibility

!!! warning "Disabled buttons"
    Never disable a button without explaining why. Use a tooltip on
    the disabled state or provide inline guidance.

---

## Do's and don'ts

| Do | Don't |
|----|-------|
| "Save changes" | "Submit" |
| One primary button per view | Multiple primary buttons |
````

---

## API reference table

For documenting configuration options, manifest fields, or API parameters:

```markdown
## Configuration options

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `name` | `string` | ✅ | — | Display name shown in the App Connect UI |
| `version` | `string` | ✅ | — | Semantic version string, e.g. `1.0.0` |
| `enabled` | `boolean` | | `true` | Whether the connector is active |
| `syncInterval` | `number` | | `300` | Seconds between background syncs |
| `fields` | `object[]` | ✅ | — | CRM field mapping definitions |
```

For parameters with complex types, use a collapsible details block:

````markdown
??? example "`fields` object shape"
    Each entry in `fields` must include:

    | Key | Type | Description |
    |-----|------|-------------|
    | `crm` | `string` | The CRM field API name |
    | `ringcentral` | `string` | The RingCentral data source key |
    | `label` | `string` | Human-readable label in the UI |

    ```json
    {
      "fields": [
        {
          "crm": "Subject",
          "ringcentral": "callDirection",
          "label": "Call direction"
        }
      ]
    }
    ```
````

---

## Step-by-step setup guide

Numbered steps with code blocks and admonitions:

````markdown
## Getting started

### Step 1 — Install the extension

Install from the Chrome Web Store or Edge Add-ons:

```bash
# Or install the development build directly
git clone https://github.com/ringcentral/rc-unified-crm-extension
cd rc-unified-crm-extension
npm install && npm run build
```

### Step 2 — Authenticate

1. Click the RingCentral icon in your browser toolbar.
2. Select **Sign in with RingCentral**.
3. Complete the OAuth flow — you'll be redirected back automatically.

!!! tip "SSO users"
    If your organization uses SSO, select **Sign in with SSO** and enter
    your company email to be redirected to your identity provider.

### Step 3 — Connect your CRM

1. Go to **Settings → Integrations**.
2. Select your CRM from the list.
3. Click **Connect** and authorize App Connect.

!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level permissions in both
    RingCentral and your CRM. Contact your admin if you see
    a permissions error.

### Step 4 — Test the connection

Make a test call. Within 30 seconds, a call log should appear
in your CRM.

!!! success "You're connected!"
    If the log appears, everything is working. If not, see the
    [troubleshooting guide](../support.md).
````

---

## Two-column layout for specs

For side-by-side comparisons or a "do / don't" visual layout:

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">

  <div style="border: 2px solid #2E7D32; border-radius: 8px; padding: 1rem;">
    <p style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
              letter-spacing: 0.06em; color: #2E7D32; margin: 0 0 0.5rem;">✓ Do</p>
    <p style="margin: 0; font-size: 0.875rem;">
      Use one primary button per view. The primary button is the
      single most important action on the screen.
    </p>
  </div>

  <div style="border: 2px solid #D32F2F; border-radius: 8px; padding: 1rem;">
    <p style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
              letter-spacing: 0.06em; color: #D32F2F; margin: 0 0 0.5rem;">✗ Don't</p>
    <p style="margin: 0; font-size: 0.875rem;">
      Stack multiple primary buttons next to each other. This
      dilutes hierarchy and forces users to choose without guidance.
    </p>
  </div>

</div>
```

---

## Announcement banner override

To customize the announcement banner (the dark strip above the navigation), add an `overrides/main.html` to your project:

```html+jinja title="overrides/main.html"
{% extends "base.html" %}

{% block announce %}
  <strong>New in 2.1:</strong>
  Drawer component, motion tokens, and dark-mode improvements.
  <a href="/resources/changelog/" class="upgrade-button">See what's new</a>
{% endblock %}
```

Then point `mkdocs.yml` to the overrides directory:

```yaml
theme:
  name: material
  custom_dir: overrides
```

!!! note "Plugin vs. overrides precedence"
    If you provide your own `overrides/main.html`, it takes precedence over the plugin's template. Copy the footer block from the [plugin template](https://github.com/ringcentral/mkdocs-material-ringcentral/blob/main/mkdocs_material_ringcentral/templates/main.html) if you want to keep the RingCentral Labs footer alongside your custom banner.
