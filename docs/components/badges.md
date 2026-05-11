# Badges

Badges are small visual labels attached to other elements. They communicate status, counts, or categorical classifications without taking up much space.

---

## Variants

### Status badges

Communicate the current state of an object.

| Badge | Color | Usage |
|-------|-------|-------|
| **Active** | Green (`#2E7D32`) | Service running, connection healthy |
| **Inactive** | Gray (`#9EA8B8`) | Disabled, not configured |
| **Pending** | Amber (`#F57C00`) | In progress, awaiting approval |
| **Error** | Red (`#D32F2F`) | Failed, authentication expired |
| **Beta** | Coral (`--ac-coral`) | Features in preview |
| **New** | Lavender (`--ac-lavender`) | Recently added |
| **Deprecated** | Gray | Scheduled for removal |

### Count badges

Numeric indicators attached to icons or navigation items:

```html
<!-- Notification bell with unread count -->
<button aria-label="Notifications (5 unread)">
  :material-bell:
  <span class="rc-badge rc-badge--count" aria-hidden="true">5</span>
</button>
```

For counts over 99, display `99+`.

### Label badges

Used in tables, cards, and lists to categorize items:

```html
<span class="rc-badge rc-badge--info">API v2</span>
<span class="rc-badge rc-badge--warning">Deprecated</span>
<span class="rc-badge rc-badge--success">Verified</span>
```

---

## Sizes

| Size | Height | Font | Usage |
|------|--------|------|-------|
| Default | 20px | 11px, weight 600 | Standard usage in most contexts |
| Large | 24px | 12px, weight 600 | Standalone use, prominent labels |
| Dot | 8px | — | Presence indicators, unread dots |

---

## Specs

| Property | Value |
|----------|-------|
| Border radius | `10px` (pill shape) |
| Padding | `2px 8px` |
| Font | Inter Tight, 11px, weight 600, uppercase |
| Letter spacing | `0.03em` |
| Min width | `20px` |

---

## Placement rules

- Badges on icons sit in the **top-right corner** of the icon, slightly overlapping.
- Status badges in tables align **left** within their cell.
- Count badges on navigation items appear **after** the label text.
- Standalone label badges in a list flow **inline** with text.

---

## Accessibility

- Count badges attached to interactive elements must be included in the element's `aria-label` — not just visually.
- Status badges should not rely on color alone — always pair with text or an icon.
- Decorative dot indicators must be `aria-hidden="true"`.

```html
<!-- Count on button — aria-label includes the count -->
<button aria-label="Messages, 3 unread">
  :material-message:
  <span class="rc-badge rc-badge--count" aria-hidden="true">3</span>
</button>

<!-- Status badge — icon + text, not just color -->
<span class="rc-badge rc-badge--success">
  <span aria-hidden="true">●</span> Active
</span>
```
