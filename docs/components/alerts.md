# Alerts

Alerts communicate contextual information, feedback, or status directly within the content flow. Unlike banners (which are page-level), alerts are scoped to a specific section or form.

---

## Variants

Alerts follow MkDocs Material's admonition system — the same styling applies to documentation and product UI alike.

### Info

General information that is useful but not urgent. Blue/sky tones.

!!! info "Rate limit notice"
    Your API key allows 1,000 requests per minute. You're currently using 420 (42%).

```markdown
!!! info "Rate limit notice"
    Your API key allows 1,000 requests per minute. You're currently using 420 (42%).
```

### Success

Confirmation that an action completed successfully. Green tones.

!!! success "Integration connected"
    Salesforce is now syncing. Call logs will appear within the next 5 minutes.

```markdown
!!! success "Integration connected"
    Salesforce is now syncing. Call logs will appear within the next 5 minutes.
```

### Warning

Something needs attention but hasn't failed. Amber/orange tones.

!!! warning "Trial ending soon"
    Your free trial expires in 3 days. Upgrade to keep your data and connected integrations.

```markdown
!!! warning "Trial ending soon"
    Your free trial expires in 3 days. Upgrade to keep your data and connected integrations.
```

### Danger / Error

Something has failed or requires immediate action. Red tones.

!!! danger "Sync paused — authentication expired"
    Your Salesforce token has expired. Re-authenticate to resume call logging.

```markdown
!!! danger "Sync paused — authentication expired"
    Your Salesforce token has expired. Re-authenticate to resume call logging.
```

### Tip

Helpful hints or pro tips for users who want to learn more. Teal/green tones.

!!! tip "Use keyboard shortcuts"
    Press `K` anywhere in the app to open the command palette.

```markdown
!!! tip "Use keyboard shortcuts"
    Press `K` anywhere in the app to open the command palette.
```

### Note

Neutral callouts for important but non-urgent supplementary information.

!!! note "Admin-only setting"
    This configuration applies to all users in your organization. Only admins can change it.

```markdown
!!! note "Admin-only setting"
    This configuration applies to all users in your organization. Only admins can change it.
```

---

## Collapsible alerts

Add `???` instead of `!!!` to make an alert collapsible. Use `???+` to start expanded.

??? warning "Legacy API deprecation details"
    The `/v1/calls` endpoint will be removed on **January 1, 2027**. Migrate to `/v2/calls` before that date. See the [migration guide](#) for details.

```markdown
??? warning "Legacy API deprecation details"
    The `/v1/calls` endpoint will be removed on **January 1, 2027**...
```

---

## Inline vs. block alerts

| Type | When to use |
|------|-------------|
| **Block alert** (full width) | Page-level notices, form-level errors, section-level status |
| **Inline alert** (beside an element) | Field-level validation feedback (use [error text on inputs](inputs.md) instead) |

---

## Alert anatomy

Each alert has three parts:

1. **Icon** — reinforces the semantic type (info, success, warning, error)
2. **Title** — short, specific, often the outcome ("Authentication expired", not "Error")
3. **Body** — explain what happened and what to do next

**Write alert copy like this:**

| Part | Bad | Good |
|------|-----|------|
| Title | "Error" | "Sync paused — token expired" |
| Body | "An error occurred." | "Your Salesforce token has expired. Re-authenticate to resume call logging." |

---

## Usage guidelines

**Do:**

- Be specific about what happened and why.
- Provide a clear next action when one exists.
- Use the correct semantic type — errors look like warnings when you use the wrong color.
- Place alerts as close as possible to the content they relate to.

**Don't:**

- Use alerts for general informational content — a well-written heading and body is better.
- Stack multiple alerts of the same type — consolidate them.
- Use red (danger/error) for non-critical information — it creates unnecessary anxiety.

---

## Accessibility

Alerts should be announced by screen readers when they appear dynamically:

```html
<div role="alert" aria-live="polite">
  <!-- Success or info messages -->
</div>

<div role="alert" aria-live="assertive">
  <!-- Errors that require immediate attention -->
</div>
```

- `aria-live="polite"` — waits for the user to finish their current task before announcing
- `aria-live="assertive"` — interrupts immediately — use for errors only
