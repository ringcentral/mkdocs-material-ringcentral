# Admonitions

Admonitions are call-out blocks that interrupt the reading flow to draw attention to notes, warnings, tips, and related content. They require the `admonition` and `pymdownx.details` extensions.

---

## Basic types

The type keyword controls the icon and colour. All standard Material types are supported.

=== "note"

    ```markdown
    !!! note "Optional custom title"
        Body text. Omit the quoted title to use the type name as the heading.
    ```

    !!! note "Optional custom title"
        Body text. Omit the quoted title to use the type name as the heading.

=== "tip"

    ```markdown
    !!! tip
        A suggestion that improves quality or saves time but is not required.
    ```

    !!! tip
        A suggestion that improves quality or saves time but is not required.

=== "warning"

    ```markdown
    !!! warning
        Something that could cause data loss, a security issue, or unexpected
        behaviour if overlooked.
    ```

    !!! warning
        Something that could cause data loss, a security issue, or unexpected
        behaviour if overlooked.

=== "danger"

    ```markdown
    !!! danger
        A destructive or irreversible action. Use sparingly — overuse dilutes impact.
    ```

    !!! danger
        A destructive or irreversible action. Use sparingly — overuse dilutes impact.

=== "success"

    ```markdown
    !!! success "You're connected"
        The call log appeared in your CRM. Everything is working correctly.
    ```

    !!! success "You're connected"
        The call log appeared in your CRM. Everything is working correctly.

=== "info"

    ```markdown
    !!! info
        Background context that supplements the main content without blocking it.
    ```

    !!! info
        Background context that supplements the main content without blocking it.

---

## Collapsible admonitions

Replace `!!!` with `???` to make the block closed by default. Use `???+` to start it open.

```markdown
??? note "Why does this happen?"
    Collapsed by default. Click to expand.

???+ tip "Pro tip — expand to read"
    Open by default. Click to collapse.
```

??? note "Why does this happen?"
    Collapsed by default. Click to expand.

???+ tip "Pro tip — expand to read"
    Open by default. Click to collapse.

---

## Admonitions with code

Body content inside admonitions is full Markdown — code blocks, lists, and links all work.

```markdown
!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level access in both RingCentral and your CRM.

    Run this command to verify your role:

    ```bash
    ringcentral roles get --user me
    ```

    If you see `403 Forbidden`, contact your account administrator.
```

!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level access in both RingCentral and your CRM.

    Run this command to verify your role:

    ```bash
    ringcentral roles get --user me
    ```

    If you see `403 Forbidden`, contact your account administrator.

---

## When to use each type

| Type | Use when |
|------|----------|
| `note` | Supplementary context that some readers need, others can skip |
| `tip` | Optional improvement or shortcut |
| `info` | Background explanation that supports the main flow |
| `success` | Confirmation that a step worked correctly |
| `warning` | Prerequisite, side-effect, or recoverable risk |
| `danger` | Irreversible action, data loss, or security exposure |
| `example` | Concrete illustration of a concept |
| `question` | FAQ entry or expected reader question |
| `quote` | External reference or block quotation |
| `abstract` / `summary` | Overview or TL;DR of a long section |

---

## Titling guidelines

A title is optional. When you include one, it appears in the coloured header bar.

| Pattern | Example |
|---------|---------|
| Sentence case, no period | `"SSO users"` |
| Action phrase | `"Admin permissions required"` |
| Question | `"Why does this error appear?"` |
| Confirmation | `"You're connected"` |

Avoid restating the type in the title. `!!! warning "Warning"` is redundant — omit the title instead and let the icon speak.
