# Accordion

Accordions show and hide sections of content. They help manage long pages by letting users focus on the sections they care about.

---

## When to use

Use an accordion when:

- A page has multiple sections where users typically only need **one or two at a time**.
- Content is **progressive** — basic users need the first section, advanced users explore later ones.
- Space is constrained and the sections are roughly equal in importance.

Do not use an accordion when:

- Users need to **compare content across sections** — collapsed content can't be compared.
- Sections are short — if all sections fit on screen without scrolling, there's no benefit.
- The content is a narrative or procedure that should be read in order.

---

## Collapsible sections in MkDocs

MkDocs Material provides collapsible `details` blocks via the `pymdownx.details` extension:

??? note "What is a connector?"
    A connector is a plugin that links RingCentral App Connect to a third-party CRM or platform. Connectors handle authentication, field mapping, and data sync between the two systems.

```markdown
??? note "What is a connector?"
    A connector is a plugin that links RingCentral App Connect to a third-party CRM...
```

Start expanded with `???+`:

???+ tip "Start expanded by default"
    Add a `+` after `???` to render the section open by default.

```markdown
???+ tip "Start expanded by default"
    Add a `+` after `???` to render the section open by default.
```

---

## HTML accordion

```html
<div class="rc-accordion">

  <div class="rc-accordion__item">
    <button
      class="rc-accordion__trigger"
      aria-expanded="true"
      aria-controls="panel-1"
      id="header-1"
    >
      General settings
      <span class="rc-accordion__icon" aria-hidden="true">▾</span>
    </button>
    <div
      id="panel-1"
      role="region"
      aria-labelledby="header-1"
    >
      <div class="rc-accordion__body">
        <!-- Content -->
      </div>
    </div>
  </div>

  <div class="rc-accordion__item">
    <button
      class="rc-accordion__trigger"
      aria-expanded="false"
      aria-controls="panel-2"
      id="header-2"
    >
      Advanced settings
      <span class="rc-accordion__icon" aria-hidden="true">›</span>
    </button>
    <div
      id="panel-2"
      role="region"
      aria-labelledby="header-2"
      hidden
    >
      <div class="rc-accordion__body">
        <!-- Content -->
      </div>
    </div>
  </div>

</div>
```

---

## Specs

| Property | Value |
|----------|-------|
| Trigger height | 52px |
| Trigger padding | `16px 20px` |
| Trigger font | 14px, weight 600 |
| Trigger hover background | `--ac-peach` |
| Active trigger border | `3px solid --ac-orange-raw` (left) |
| Body padding | `16px 20px 24px` |
| Divider | `1px solid #DDD0D8` |
| Expand/collapse animation | height 200ms `ease-sharp` |
| Icon rotation | `0° → 180°` when open, 200ms |

---

## Accessibility

- Trigger buttons must have `aria-expanded="true/false"`.
- `aria-controls` on the trigger points to the panel's `id`.
- Panel regions use `role="region"` and `aria-labelledby` pointing to the trigger's `id`.
- Use `hidden` attribute (not `display: none`) on closed panels so they're excluded from the accessibility tree.
- Keyboard: `Tab` to the trigger, `Enter`/`Space` to open/close. Arrow keys are not required for accordions (unlike tabs).
