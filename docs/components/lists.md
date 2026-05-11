# Lists

Lists display a vertical sequence of related items. They're one of the most common UI patterns in product interfaces — contact lists, activity feeds, settings items, and option menus are all lists.

---

## Variants

### Simple list

```html
<ul class="rc-list">
  <li class="rc-list__item">Item one</li>
  <li class="rc-list__item">Item two</li>
  <li class="rc-list__item">Item three</li>
</ul>
```

### List with metadata

```html
<ul class="rc-list">
  <li class="rc-list__item">
    <div class="rc-list__primary">Jane Smith</div>
    <div class="rc-list__secondary">jane.smith@example.com · +1 555 0100</div>
  </li>
  <li class="rc-list__item">
    <div class="rc-list__primary">John Doe</div>
    <div class="rc-list__secondary">john.doe@example.com · +1 555 0200</div>
  </li>
</ul>
```

### List with avatar

```html
<ul class="rc-list">
  <li class="rc-list__item">
    <img class="rc-avatar" src="jane.jpg" alt="" width="40" height="40" />
    <div class="rc-list__content">
      <div class="rc-list__primary">Jane Smith</div>
      <div class="rc-list__secondary">Account Manager</div>
    </div>
    <span class="rc-badge rc-badge--success">Active</span>
  </li>
</ul>
```

### Selectable list

```html
<ul class="rc-list rc-list--selectable" role="listbox" aria-label="Select a connector">
  <li
    class="rc-list__item rc-list__item--selected"
    role="option"
    aria-selected="true"
  >
    <span class="rc-list__check" aria-hidden="true">✓</span>
    Salesforce
  </li>
  <li class="rc-list__item" role="option" aria-selected="false">
    HubSpot
  </li>
</ul>
```

### Action list

Each item has an action (link or button) that takes up the entire item as a click target.

```html
<ul class="rc-list rc-list--action">
  <li>
    <a class="rc-list__item" href="/settings/general">
      <span class="rc-list__icon" aria-hidden="true">:material-cog:</span>
      <span class="rc-list__primary">General settings</span>
      <span class="rc-list__arrow" aria-hidden="true">›</span>
    </a>
  </li>
</ul>
```

---

## Specs

| Property | Value |
|----------|-------|
| Item min height | 48px |
| Item padding | `12px 16px` |
| Divider | `1px solid rgba(221,208,216,0.5)` |
| Hover background | `--ac-peach` |
| Selected background | `--ac-peach` + left border `--ac-orange-raw` |
| Primary text | 14px, weight 400, `#1A1A2E` |
| Secondary text | 12px, weight 400, `#5A6070` |
| Avatar gap | 12px |

---

## Usage guidelines

- Use `<ul>` for unordered items and `<ol>` for ordered/ranked items.
- Add a `role="listbox"` and `aria-selected` for selectable lists.
- Group long lists with section headers (`<li role="presentation">` or a heading above the group).
- Limit visible items to 8–10 before adding scroll or pagination.
- Items with actions (links, buttons) should have generous touch targets (min 44px).
