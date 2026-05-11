# Drawers

Drawers are panel overlays that slide in from the edge of the screen. They provide a focused secondary workspace without fully navigating away from the current page.

---

## When to use

Use a drawer when:

- The user needs to **view or edit details** of a list item while keeping the list visible.
- The task requires **more space than a dialog** but doesn't warrant a new page.
- A **secondary workflow** needs to be accessible alongside the main view (filters, settings, help).

Do not use a drawer when:

- The task is simple and focused — use a [Dialog](dialogs.md) instead.
- The user needs to focus completely — use a full page.
- The content is very long with its own navigation — use a page.

---

## Variants

### Right panel (default)

Slides in from the right edge. Used for detail views, record editing, and extended settings.

```html
<aside
  class="rc-drawer rc-drawer--right"
  role="complementary"
  aria-label="Connector details"
  aria-hidden="false"
>
  <div class="rc-drawer__header">
    <h2 class="rc-drawer__title">Salesforce connector</h2>
    <button class="rc-drawer__close" aria-label="Close panel">✕</button>
  </div>

  <div class="rc-drawer__body">
    <!-- Drawer content -->
  </div>

  <div class="rc-drawer__footer">
    <button class="md-button" onclick="closeDrawer()">Cancel</button>
    <button class="md-button md-button--primary">Save changes</button>
  </div>
</aside>

<!-- Backdrop -->
<div class="rc-drawer__backdrop" aria-hidden="true"></div>
```

### Left panel

Slides in from the left. Used for navigation trees, filter panels, and exploratory browsing.

```html
<aside
  class="rc-drawer rc-drawer--left"
  role="navigation"
  aria-label="Filter panel"
>
  <!-- Filter content -->
</aside>
```

### Bottom sheet (mobile)

On screens below 768px, drawers automatically transform into bottom sheets that slide up from the bottom edge.

---

## Sizes

| Size | Width | Usage |
|------|-------|-------|
| Narrow | 320px | Simple details, short forms |
| **Default** | 480px | **Standard record editing, settings** |
| Wide | 640px | Complex forms, comparisons |
| Full | 100vw | Mobile-only, full-screen flows |

---

## Anatomy

```
┌─────────────────────────┐
│ Title              [✕] │  ← Header: fixed, sticky
│─────────────────────────│
│                         │
│  Scrollable body        │  ← Body: scrolls when content overflows
│                         │
│  ...                    │
│                         │
│─────────────────────────│
│  [Cancel]  [Save]       │  ← Footer: fixed at bottom
└─────────────────────────┘
```

---

## Backdrop

A semi-transparent `rgba(0,0,0,0.3)` backdrop covers the rest of the page. Clicking the backdrop closes the drawer (unless there are unsaved changes).

---

## Animation

| Direction | Enter | Exit |
|-----------|-------|------|
| Right | `translateX(100%) → translateX(0)`, 300ms `ease-decelerate` | `translateX(0) → translateX(100%)`, 200ms `ease-accelerate` |
| Left | `translateX(-100%) → translateX(0)` | `translateX(0) → translateX(-100%)` |
| Bottom | `translateY(100%) → translateY(0)` | `translateY(0) → translateY(100%)` |

---

## Accessibility

- The drawer container must have `role="complementary"` (for detail panels) or `role="dialog"` (for task panels) and `aria-label`.
- When open, the drawer must trap focus inside it.
- `Escape` must close the drawer (warn about unsaved changes first if needed).
- Background content must be made inert (`inert` attribute) when the drawer is open.
- Focus returns to the trigger element when the drawer closes.
- On mobile, the bottom sheet must be reachable by scroll in addition to swipe.

```javascript
// Mark background inert when drawer opens
document.getElementById('main-content').inert = true;

// Restore on close
document.getElementById('main-content').inert = false;
```
