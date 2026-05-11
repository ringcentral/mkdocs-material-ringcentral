# Pagination

Pagination splits a large dataset into pages, allowing users to navigate between them. Use it for tables and lists when loading all records at once would degrade performance or overwhelm the user.

---

## Variants

### Numbered pagination

Standard pagination with page numbers and previous/next controls.

```html
<nav class="rc-pagination" aria-label="Results pages">
  <button class="rc-pagination__prev" aria-label="Previous page" disabled>
    ‹ Previous
  </button>

  <button class="rc-pagination__page" aria-label="Page 1" aria-current="false">1</button>
  <button class="rc-pagination__page" aria-label="Page 2" aria-current="false">2</button>
  <button class="rc-pagination__page rc-pagination__page--active" aria-label="Page 3, current" aria-current="page">3</button>
  <button class="rc-pagination__page" aria-label="Page 4" aria-current="false">4</button>
  <span class="rc-pagination__ellipsis" aria-hidden="true">…</span>
  <button class="rc-pagination__page" aria-label="Page 12" aria-current="false">12</button>

  <button class="rc-pagination__next" aria-label="Next page">
    Next ›
  </button>
</nav>
```

### Simple (previous / next only)

For infinite or very large datasets where numbered pages aren't helpful:

```html
<nav class="rc-pagination rc-pagination--simple" aria-label="Results pages">
  <button class="rc-pagination__prev" aria-label="Previous page">
    ← Previous
  </button>
  <span class="rc-pagination__info">Page 3 of 12</span>
  <button class="rc-pagination__next" aria-label="Next page">
    Next →
  </button>
</nav>
```

### With page size selector

```html
<div class="rc-pagination-bar">
  <div class="rc-pagination-bar__info">
    Showing 41–60 of 234 results
  </div>

  <nav class="rc-pagination" aria-label="Results pages">
    <!-- page buttons -->
  </nav>

  <div class="rc-pagination-bar__size">
    <label for="page-size">Rows per page</label>
    <select id="page-size" class="rc-select rc-select--sm">
      <option>20</option>
      <option selected>40</option>
      <option>100</option>
    </select>
  </div>
</div>
```

---

## Specs

| Property | Value |
|----------|-------|
| Button size | 36×36px |
| Page button border radius | 4px |
| Active button background | `--ac-orange-raw` |
| Active button text | White |
| Hover background | `--ac-peach` |
| Font | 14px, weight 600 |
| Gap between buttons | 4px |
| Ellipsis color | `#9EA8B8` |

---

## How many page links to show

| Total pages | Visible pages |
|-------------|---------------|
| 1–7 | All pages |
| 8–99 | Current ±2, first, last, ellipsis |
| 100+ | Current ±1, first, last, ellipsis |

Always show at minimum: first page, last page, current page, and one page on each side of current.

---

## Usage guidelines

- Position pagination **below** the list or table it controls.
- Keep the total record count visible near the pagination: "Showing 41–60 of 234 results".
- Persist the current page in the URL so users can share links to specific pages.
- Scroll to the top of the list when the page changes.
- Disable (not hide) previous/next when at the first/last page.

---

## Accessibility

- Wrap in `<nav aria-label="Results pages">`.
- `aria-current="page"` on the active page button.
- Disabled prev/next buttons should be `disabled` (not just visually styled).
- Each page button needs a unique `aria-label`: "Page 3" not just "3".
