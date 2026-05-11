# Admonitions

Admonitions are call-out blocks that interrupt reading flow to draw attention to notes, warnings, tips, and related content. They require the `admonition` and `pymdownx.details` extensions.

---

## Syntax

```markdown
!!! type "Optional custom title"
    Body text. Four-space indent required.
    Omit the quoted title to use the type name as the heading.
```

Use `???` instead of `!!!` for a collapsible block (closed by default). Use `???+` to start it open.

---

## All supported types

Every type has a distinct icon and colour. Aliases (e.g. `hint`, `caution`) render identically to their canonical type.

### note

The default. Blue-grey. Use for supplementary context that some readers need and others can skip.

!!! note
    Supplementary context that supports the main content without blocking it.

!!! note "Custom title"
    The same type with an explicit title in the header bar.

---

### abstract · summary · tldr

Teal. Use for overviews and TL;DR sections at the top of long pages.

!!! abstract
    A concise summary of what this page covers, written for readers who want the key points before committing to the full content.

---

### info · todo

Blue. Background context or in-progress notices.

!!! info
    Background information that helps readers understand the surrounding topic.

!!! todo
    This section is in progress. Check back after the next release.

---

### tip · hint · important

Green. Optional improvements, shortcuts, and things worth knowing.

!!! tip
    A suggestion that improves quality or saves time but is not required to proceed.

!!! hint
    Same visual treatment — use whichever reads most naturally for the context.

!!! important
    A non-blocking but notable point that readers should not overlook.

---

### success · check · done

Green (brighter). Confirmation that something worked.

!!! success "You're connected"
    The call log appeared in your CRM within 30 seconds. Everything is working correctly.

---

### question · help · faq

Green-teal. FAQ entries and expected reader questions.

!!! question "Why didn't my call log appear?"
    Call logs sync within 30 seconds of a call ending. If you don't see an entry after 60 seconds, check that your CRM connection is authorized in **Settings → Integrations**.

---

### warning · caution · attention

Amber-orange. Prerequisites, side-effects, and recoverable risks.

!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level access in both RingCentral and your CRM. Contact your admin if you see a `403 Forbidden` error.

!!! caution
    Changing the sync interval below 60 seconds may trigger CRM API rate limits.

---

### failure · fail · missing

Red. Something went wrong or a required item is absent.

!!! failure
    The connection attempt failed. Verify that your OAuth application has the `crm.objects.contacts.write` scope and try again.

---

### danger · error

Dark red. Destructive or irreversible actions.

!!! danger
    Deleting a connector removes all synced field mappings permanently. This action cannot be undone.

!!! error
    A `500 Internal Server Error` indicates a problem on the CRM's side. Check your CRM's status page before retrying.

---

### bug

Red. Known issues and defect documentation.

!!! bug
    Screen pop does not fire for calls transferred from a queue if the agent's browser tab is not in focus. This is a known issue tracked in [APPCN-1234](#).

---

### example

Purple. Concrete illustrations and code walkthroughs.

!!! example
    To log a call manually, POST to `/rccrm/v1/call-logs` with the following body:

    ```json
    {
      "direction": "outbound",
      "duration": 142,
      "contactId": "003Dn000002xyzABC"
    }
    ```

---

### quote · cite

Grey. External references and block quotations.

!!! quote "RingCentral Developer Portal"
    App Connect is a powerful integration platform that connects RingCentral with your CRM, so every call is automatically logged and every contact is matched in real time.

---

## Collapsible blocks

Replace `!!!` with `???` for closed-by-default, `???+` for open-by-default.

```markdown
??? note "Why does this happen?"
    Collapsed by default. Click the header to expand.

???+ tip "Best practice — expand to read"
    Open by default. Click the header to collapse.
```

??? note "Why does this happen?"
    Collapsed by default. Click the header to expand.

???+ tip "Best practice — expand to read"
    Open by default. Click the header to collapse.

---

## Rich content inside admonitions

Body content is full Markdown — code blocks, lists, tables, and nested admonitions all render correctly.

```markdown
!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level access in both systems.

    Steps to verify your role:

    1. Open **Settings → Account**.
    2. Check your assigned role.
    3. Contact your admin if the **Integrations** tab is not visible.

    ```bash
    ringcentral roles get --user me
    ```
```

!!! warning "Admin permissions required"
    Connecting a CRM requires admin-level access in both systems.

    Steps to verify your role:

    1. Open **Settings → Account**.
    2. Check your assigned role.
    3. Contact your admin if the **Integrations** tab is not visible.

    ```bash
    ringcentral roles get --user me
    ```

---

## When to use each type

| Type | Colour | Use when |
|------|--------|----------|
| `note` | Blue-grey | Supplementary context, optional reading |
| `abstract` | Teal | Page summaries, TL;DR sections |
| `info` | Blue | Background explanation, in-progress notices |
| `tip` | Green | Optional improvements, shortcuts |
| `success` | Bright green | Confirmation a step worked |
| `question` | Green-teal | FAQ entries, expected reader questions |
| `warning` | Amber | Prerequisites, side-effects, recoverable risks |
| `failure` | Red | Something went wrong, missing required item |
| `danger` | Dark red | Irreversible actions, data loss, security exposure |
| `bug` | Red | Known issues and defect documentation |
| `example` | Purple | Code walkthroughs, concrete illustrations |
| `quote` | Grey | External references, block quotations |

---

## Titling guidelines

| Pattern | Example |
|---------|---------|
| Sentence case, no period | `"SSO users"` |
| Action phrase | `"Admin permissions required"` |
| Question | `"Why does this error appear?"` |
| Confirmation | `"You're connected"` |

Avoid restating the type in the title. `!!! warning "Warning"` is redundant — omit the title and let the icon speak.
