# Banners

Banners communicate important page-level or system-level messages. Unlike alerts — which are scoped to a section — banners span the full page width and persist until dismissed or the condition resolves.

---

## Variants

### Announcement banner

For product announcements, new features, and non-urgent updates. Used in the template as the announcement strip above the navigation.

The plugin's `main.html` template includes a pre-built announcement banner:

```html+jinja
{% block announce %}
  <strong>App Connect 2.0 is here!</strong>
  New connectors, plugin API, and AI call summaries.
  <a href="/2.0/" class="upgrade-button">Learn what's new</a>
{% endblock %}
```

Override it in your own `overrides/main.html` to customize the message.

---

### System status banner

For ongoing system issues, maintenance windows, or service degradation:

```html
<div class="rc-banner rc-banner--warning" role="status">
  <span class="rc-banner__icon" aria-hidden="true">⚠️</span>
  <span class="rc-banner__message">
    <strong>Scheduled maintenance:</strong>
    Call log sync will be paused on Saturday, May 17 from 2–4 AM UTC.
  </span>
  <button class="rc-banner__dismiss" aria-label="Dismiss this notice">✕</button>
</div>
```

### Error banner

For service-level errors that affect all users:

```html
<div class="rc-banner rc-banner--error" role="alert">
  <span class="rc-banner__icon" aria-hidden="true">❌</span>
  <span class="rc-banner__message">
    <strong>CRM sync is currently unavailable.</strong>
    Our team is investigating. Check the <a href="/status">status page</a> for updates.
  </span>
</div>
```

---

## Banner placement

| Type | Placement |
|------|-----------|
| Announcement | Above the navigation header (via template `announce` block) |
| System status | Below the navigation header, above the page content |
| Error | Below the navigation header, above the page content |

---

## Specs

| Property | Value |
|----------|-------|
| Min height | 48px |
| Padding | `10px 24px` |
| Font | 14px, weight 400 |
| Announcement bg | `#2D1A0E` (dark brown) |
| Announcement text | `rgba(255,255,255,0.9)` |
| Warning bg | `#FFF8E1` |
| Warning border | `3px solid #F57C00` (left border) |
| Error bg | `#FFEBEE` |
| Error border | `3px solid #D32F2F` (left border) |
| Info bg | `--ac-pale-blue` |
| Info border | `3px solid --ac-sky` (left border) |

---

## Usage guidelines

- **One banner at a time.** If multiple system conditions exist, merge them into a single banner.
- **Be specific.** "Sync is paused — your Salesforce token expired" not "Service issue detected."
- **Include a next action** when the user can do something: re-authenticate, check the status page, upgrade.
- **Dismiss when appropriate.** Non-critical announcements should be dismissible. Persistent error banners should not be dismissible until the issue resolves.

---

## Accessibility

- Announcement banners: `role="status"`, `aria-live="polite"`.
- Error banners: `role="alert"`, `aria-live="assertive"`.
- Dismiss buttons must have `aria-label`.
- Ensure banner text contrasts with the banner background (WCAG AA).
