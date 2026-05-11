# Chips

Chips are compact, interactive elements that represent attributes, filters, or selections. They're most common in filter bars and multi-select inputs.

---

## Variants

### Filter chip

Used in filter bars to toggle a category on or off.

```html
<div class="rc-chip-group" role="group" aria-label="Filter by status">
  <button class="rc-chip rc-chip--filter rc-chip--selected" aria-pressed="true">
    Active
  </button>
  <button class="rc-chip rc-chip--filter" aria-pressed="false">
    Inactive
  </button>
  <button class="rc-chip rc-chip--filter" aria-pressed="false">
    Pending
  </button>
</div>
```

### Input chip (tag)

Represents a selected value in a multi-select input. Has a remove button.

```html
<span class="rc-chip rc-chip--input">
  Salesforce
  <button class="rc-chip__remove" aria-label="Remove Salesforce filter">
    <span aria-hidden="true">✕</span>
  </button>
</span>
```

### Suggestion chip

Non-interactive chips used as contextual labels or tags:

```html
<span class="rc-chip rc-chip--label">CRM</span>
<span class="rc-chip rc-chip--label">Beta</span>
```

---

## Sizes

| Size | Height | Font | Usage |
|------|--------|------|-------|
| Default | 32px | 13px, weight 600 | Standard filter bars, input tags |
| Small | 24px | 11px, weight 600 | Dense lists, badge-like labels |

---

## Specs

| Property | Value |
|----------|-------|
| Border radius | `16px` (pill) |
| Padding | `0 12px` |
| Default border | `1px solid #DDD0D8` |
| Default background | `#FFFFFF` |
| Selected background | `--ac-peach` |
| Selected border | `1.5px solid --ac-orange-raw` |
| Selected text | `--ac-orange-raw` |
| Font | Inter Tight, 13px, weight 600 |
| Gap between chips | `8px` |

---

## Accessibility

- Filter chips must use `aria-pressed` to communicate their selected state.
- Input chip remove buttons need an `aria-label` that identifies what's being removed.
- Chip groups should have a `role="group"` with an `aria-label` describing the filter category.
