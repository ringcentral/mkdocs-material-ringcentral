# Error States

Errors are inevitable. How the product responds to them determines whether users recover successfully or abandon their task in frustration. Good error handling is specific, actionable, and honest.

---

## Error categories

| Category | Cause | User expectation |
|----------|-------|-----------------|
| **Validation error** | User input doesn't meet requirements | Immediate feedback, stay on page |
| **Network error** | Request failed due to connectivity | Retry option, temporary message |
| **Authentication error** | Token expired, session ended | Re-auth prompt, no data loss |
| **Permission error** | User lacks access to a resource | Explanation, alternative action |
| **Server error** | Something failed on the backend | Acknowledgment, retry, support link |
| **Not found (404)** | Resource doesn't exist | Navigate back, search |
| **Rate limit** | Too many requests | Wait time, upgrade prompt |

---

## Validation errors

See [Forms](../components/forms.md) for full field-level validation guidance.

**Key rules:**

- Show errors inline next to the field that caused them.
- Never show errors before the user has touched the field.
- Tell users exactly what to fix — not just that something is wrong.
- For multi-error forms, show a summary at the top linking to each error.

**Good vs. bad:**

| Bad | Good |
|-----|------|
| "Invalid input" | "Enter a 10-digit phone number, like 555-867-5309" |
| "Error in form" | "Fix 2 errors to continue: email address and phone number" |
| "Required" | "Enter your email address" |

---

## Network errors

Network errors are temporary — emphasize that and offer a retry.

```html
<div class="rc-error-state" role="alert">
  <span class="rc-error-state__icon" aria-hidden="true">:material-wifi-off:</span>
  <h2 class="rc-error-state__title">Couldn't reach the server</h2>
  <p class="rc-error-state__body">
    Check your internet connection and try again.
  </p>
  <button class="md-button md-button--primary" onclick="retry()">
    Try again
  </button>
</div>
```

---

## Authentication errors

When a session or token expires, preserve the user's work and prompt re-authentication.

```html
<div class="rc-banner rc-banner--warning" role="alert">
  <strong>Your session has expired.</strong>
  <a href="/auth/login?return_to=/settings/connectors">Sign in again</a>
  to continue — your changes are saved.
</div>
```

**Rules:**

- Never silently lose user input on session expiry.
- Redirect back to the interrupted page after re-authentication.
- If the user was mid-form, restore their draft.

---

## Permission errors

When users request a resource they're not authorized to see:

```html
<div class="rc-error-state">
  <span class="rc-error-state__icon" aria-hidden="true">:material-lock:</span>
  <h2>You don't have access to this connector</h2>
  <p>This connector was created by your organization admin.
     Contact <a href="mailto:admin@example.com">your admin</a> to request access.</p>
</div>
```

**Don't:** Show a 404 when the resource exists but the user can't see it — this leaks information.
**Do:** Clearly explain why they can't see it and who can grant access.

---

## Server errors (5xx)

Be honest, but don't alarm users unnecessarily. Temporary errors happen.

```html
<div class="rc-error-state">
  <span class="rc-error-state__icon" aria-hidden="true">:material-alert-circle:</span>
  <h2>Something went wrong on our end</h2>
  <p>
    We've been notified. Try again in a moment, or
    <a href="/support">contact support</a> if this keeps happening.
  </p>
  <div class="rc-error-state__actions">
    <button class="md-button md-button--primary">Try again</button>
    <a class="md-button" href="/support">Get help</a>
  </div>
</div>
```

**Never:** Say "unexpected error occurred" — every error is unexpected from the server's perspective. Say what failed.

---

## 404 — Page not found

```html
<div class="rc-error-state rc-error-state--404">
  <h1>404 — Page not found</h1>
  <p>The page you're looking for doesn't exist or has been moved.</p>
  <div class="rc-error-state__actions">
    <a class="md-button md-button--primary" href="/">Go home</a>
    <a class="md-button" href="/search">Search docs</a>
  </div>
</div>
```

---

## Error tone

| Tone to avoid | Tone to use |
|---------------|-------------|
| Blaming the user ("you entered an invalid value") | Neutral ("This field needs a valid email address") |
| Technical jargon ("HTTP 503 Service Unavailable") | Plain language ("Our service is temporarily unavailable") |
| Apologetic overload ("We're so sorry for the inconvenience!") | Direct ("Something went wrong — try again") |
| Vague ("An error occurred") | Specific ("Couldn't save your changes — check your connection") |

---

## Error logging

Every error shown to users should be logged with:

- Error type and code
- User ID and session
- Page and action that triggered it
- Timestamp

This lets the team track error frequency and prioritize fixes.
