# Tabs

Tabbed content lets you present multiple versions of the same information — code in different languages, platform-specific steps, or variant comparisons — without repeating page structure. Requires `pymdownx.tabbed` with `alternate_style: true`.

---

## Basic syntax

```markdown
=== "Tab one"
    Content for tab one. Must be indented by four spaces.

=== "Tab two"
    Content for tab two.

=== "Tab three"
    Content for tab three.
```

=== "Tab one"
    Content for tab one. Must be indented by four spaces.

=== "Tab two"
    Content for tab two.

=== "Tab three"
    Content for tab three.

---

## Code variant tabs

The most common use case — the same task in multiple languages or environments.

````markdown
=== "npm"

    ```bash
    npm install @ringcentral/sdk
    ```

=== "yarn"

    ```bash
    yarn add @ringcentral/sdk
    ```

=== "pnpm"

    ```bash
    pnpm add @ringcentral/sdk
    ```
````

=== "npm"

    ```bash
    npm install @ringcentral/sdk
    ```

=== "yarn"

    ```bash
    yarn add @ringcentral/sdk
    ```

=== "pnpm"

    ```bash
    pnpm add @ringcentral/sdk
    ```

---

## Tabs with rich content

Each tab panel is full Markdown — headings, admonitions, lists, and code all render normally.

```markdown
=== "Salesforce"

    ### Prerequisites

    - Salesforce admin role
    - OAuth connected app with `api` and `refresh_token` scopes

    !!! tip
        Enable "Allow OAuth Username-Password Flows" only in sandbox.
        Production orgs should use the authorization code flow.

    ```bash
    sf org login web --alias my-sandbox
    ```

=== "HubSpot"

    ### Prerequisites

    - HubSpot account with CRM access
    - Private app with `crm.objects.contacts.read` scope

    !!! note
        HubSpot private apps replace legacy API keys. If you have an existing
        key-based integration, migrate before the deprecation date.
```

=== "Salesforce"

    ### Prerequisites

    - Salesforce admin role
    - OAuth connected app with `api` and `refresh_token` scopes

    !!! tip
        Enable "Allow OAuth Username-Password Flows" only in sandbox.
        Production orgs should use the authorization code flow.

    ```bash
    sf org login web --alias my-sandbox
    ```

=== "HubSpot"

    ### Prerequisites

    - HubSpot account with CRM access
    - Private app with `crm.objects.contacts.read` scope

    !!! note
        HubSpot private apps replace legacy API keys. If you have an existing
        key-based integration, migrate before the deprecation date.

---

## Linked tabs (`content.tabs.link`)

With `content.tabs.link` enabled in `mkdocs.yml`, tab selections sync across all tab groups on the same page that share the same label. A reader who picks "Python" in one code block will see "Python" selected in every subsequent code block on that page.

This is enabled in the theme by default. No extra markup needed — just use consistent tab labels across your tab groups.

---

## When to use tabs

| Use case | Tabs | Admonition (`???+`) | Separate pages |
|----------|------|---------------------|----------------|
| Same task, different languages | ✓ | — | — |
| Same task, different platforms | ✓ | — | — |
| Optional deep-dive | — | ✓ | — |
| Substantially different content | — | — | ✓ |
| 2+ steps that differ by audience | ✓ | — | — |

Avoid tabs when the content in each tab is longer than one screenful — readers lose context when they can't see the tab label while reading.
