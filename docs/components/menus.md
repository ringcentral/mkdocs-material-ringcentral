# Menus

Menus present a list of actions or options in a floating panel. They appear in response to a trigger — a button, a right-click, or an overflow icon.

---

## Variants

### Dropdown menu

Triggered by a button. Presents a list of actions related to the trigger element.

```html
<div class="rc-menu-container">
  <button
    class="md-button"
    aria-haspopup="true"
    aria-expanded="false"
    aria-controls="actions-menu"
    id="actions-trigger"
  >
    Actions ▾
  </button>

  <ul
    id="actions-menu"
    role="menu"
    aria-labelledby="actions-trigger"
    hidden
  >
    <li role="menuitem"><a href="#">Edit settings</a></li>
    <li role="menuitem"><a href="#">Duplicate</a></li>
    <li role="separator" aria-hidden="true"></li>
    <li role="menuitem" class="rc-menu__item--danger">
      <a href="#">Delete connector</a>
    </li>
  </ul>
</div>
```

### Context menu (right-click)

Same markup as dropdown menu but positioned at the cursor location.

### Overflow menu ("⋮" menu)

Common in table rows and card actions — a small icon button that reveals row-specific actions:

```html
<button
  class="rc-icon-button"
  aria-label="More actions for Salesforce connector"
  aria-haspopup="true"
  aria-expanded="false"
>
  :material-dots-vertical:
</button>
```

!!! tip "Accessible overflow menu labels"
    The `aria-label` on overflow buttons must identify the item they control — "More actions for Salesforce" not just "More actions". Without this, every overflow button in a table sounds identical to screen reader users.

---

## Menu item types

| Type | Usage |
|------|-------|
| **Action item** | Triggers an operation (edit, delete, copy) |
| **Navigation item** | Navigates to a different page or section |
| **Toggle item** | Toggles a boolean setting (show/hide column) |
| **Submenu trigger** | Opens a nested menu |
| **Section header** | Labels a group (non-interactive) |
| **Separator** | Visual divider between groups |

---

## Menu anatomy

```
┌──────────────────────────┐
│ Section header (optional)│  ← Not a menu item — aria-hidden
│──────────────────────────│
│ :icon: Edit settings     │  ← menuitem
│ :icon: Duplicate         │  ← menuitem
│──────────────────────────│  ← separator
│ :icon: Delete connector  │  ← menuitem (danger)
└──────────────────────────┘
```

---

## Specs

| Property | Value |
|----------|-------|
| Min width | 160px |
| Max width | 320px |
| Item height | 40px |
| Item padding | `10px 16px` |
| Font | 14px, weight 400 |
| Background | `#FFFFFF` |
| Shadow | `shadow-lg` |
| Border radius | `8px` |
| Separator height | `1px` |
| Separator color | `#DDD0D8` |
| Hover background | `--ac-peach` |
| Danger item text | `#D32F2F` |
| Section header font | 11px, weight 600, uppercase, `#9EA8B8` |

---

## Placement

Menus open below their trigger and align to the left edge by default. They flip when the dropdown would overflow the viewport:

| Default | Flips to |
|---------|----------|
| Below + left-aligned | Above when too close to bottom |
| Left-aligned | Right-aligned when too close to right edge |

---

## Keyboard interaction

| Key | Action |
|-----|--------|
| `Enter` / `Space` | Open menu / activate focused item |
| `↑` / `↓` | Navigate items |
| `Home` | Focus first item |
| `End` | Focus last item |
| `Escape` | Close menu, return focus to trigger |
| `Tab` | Close menu, move focus to next element |

---

## Accessibility

- Trigger button: `aria-haspopup="true"`, `aria-expanded` reflects open/close state, `aria-controls` points to the menu.
- Menu container: `role="menu"`, `aria-labelledby` points to the trigger.
- Menu items: `role="menuitem"` (or `menuitemcheckbox` / `menuitemradio`).
- Separators: `role="separator"`.
- Section headers: `aria-hidden="true"` (they label sections visually but are not interactive).
- On open, focus moves to the first item.
- On close, focus returns to the trigger.
