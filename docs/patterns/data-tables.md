# Data Tables

Data tables display large, structured datasets that users need to scan, compare, filter, and act on. They're more complex than [basic tables](../components/tables.md) — they include sorting, filtering, pagination, selection, and inline actions.

---

## Anatomy

```
┌─────────────────────────────────────────────────────────────────┐
│  [Filter bar]                    [Search]     [+ Add]  [⋮ More] │  ← Toolbar
│─────────────────────────────────────────────────────────────────│
│  ☐  │ Name ↑  │ Status    │ Last sync   │ Records │ Actions     │  ← Header row
│─────────────────────────────────────────────────────────────────│
│  ☐  │ Salesforce │ ✅ Active │ 2 min ago  │ 1,234   │ ✏️ 🗑️       │
│  ☐  │ HubSpot    │ ✅ Active │ 5 min ago  │ 892     │ ✏️ 🗑️       │
│  ☐  │ Clio       │ ⚠️ Warning │ 2 hrs ago  │ 456     │ ✏️ 🗑️       │
│─────────────────────────────────────────────────────────────────│
│  Showing 1–3 of 12 results          [← Prev]  1 2 3  [Next →]  │  ← Footer
└─────────────────────────────────────────────────────────────────┘
```

---

## Toolbar

The table toolbar appears above the table and contains:

- **Filter chips** or filter dropdown (left)
- **Search input** (right)
- **Primary action** button — "Add connector" (far right)
- **Bulk actions** (appear when rows are selected)

```html
<div class="rc-table-toolbar">
  <div class="rc-table-toolbar__left">
    <!-- Selected state: bulk actions -->
    <div class="rc-table-toolbar__bulk" hidden>
      <span class="rc-table-toolbar__selection-count">3 selected</span>
      <button class="md-button">Export</button>
      <button class="md-button md-button--danger">Delete</button>
    </div>

    <!-- Default state: filters -->
    <div class="rc-table-toolbar__filters">
      <div class="rc-chip-group" role="group" aria-label="Filter by status">
        <button class="rc-chip rc-chip--filter rc-chip--selected" aria-pressed="true">All</button>
        <button class="rc-chip rc-chip--filter" aria-pressed="false">Active</button>
        <button class="rc-chip rc-chip--filter" aria-pressed="false">Error</button>
      </div>
    </div>
  </div>

  <div class="rc-table-toolbar__right">
    <div class="rc-search-bar rc-search-bar--sm">
      <input type="search" placeholder="Search connectors…" />
    </div>
    <button class="md-button md-button--primary">+ Add connector</button>
  </div>
</div>
```

---

## Sorting

Click column headers to sort. The active sort column shows a direction arrow.

```html
<th scope="col" aria-sort="ascending">
  <button class="rc-table__sort">
    Name
    <span class="rc-table__sort-icon" aria-hidden="true">↑</span>
  </button>
</th>
<th scope="col" aria-sort="none">
  <button class="rc-table__sort">
    Status
    <span class="rc-table__sort-icon" aria-hidden="true">↕</span>
  </button>
</th>
```

**Rules:**

- Only one column sorted at a time (unless multi-sort is explicitly designed).
- Default sort should reflect the most useful order for the use case (often recency or name).
- Sort state persists on the current page only, unless saved in URL params.

---

## Row selection

Row checkboxes for bulk operations. The header checkbox selects all visible rows.

```html
<th scope="col">
  <input
    type="checkbox"
    id="select-all"
    aria-label="Select all rows"
  />
</th>

<td>
  <input
    type="checkbox"
    aria-label="Select Salesforce row"
    aria-rowindex="1"
  />
</td>
```

When rows are selected, the toolbar transitions to bulk-action mode showing the count and available bulk operations.

---

## Inline row actions

Use an overflow menu ("⋮") for row-level actions to keep the table clean:

```html
<td class="rc-table__actions">
  <button
    class="rc-icon-button"
    aria-label="More actions for Salesforce"
    aria-haspopup="true"
  >
    :material-dots-vertical:
  </button>
</td>
```

For 1–2 very common actions, you can show them inline with icon buttons (always with `aria-label`):

```html
<td class="rc-table__actions">
  <button class="rc-icon-button" aria-label="Edit Salesforce">:material-pencil:</button>
  <button class="rc-icon-button rc-icon-button--danger" aria-label="Delete Salesforce">:material-delete:</button>
</td>
```

---

## Empty and loading states

See [Empty States](empty-states.md) and [Loading States](loading-states.md) for how to handle these within a table context.

**Quick reference:**

- Loading: Show 5 skeleton rows.
- Empty (no data): Centered empty state inside `<tbody>` spanning all columns.
- No search results: No-results empty state with clear-search action.

---

## Column configuration

For tables with many columns, let users show/hide columns:

```html
<button class="md-button" aria-haspopup="true" aria-expanded="false" id="column-toggle">
  :material-view-column: Columns
</button>
```

The resulting dropdown shows a checklist of available columns.

---

## Responsive behavior

On screens < 768px, data tables with more than 4 columns should:

1. **Collapse to card view** — each row becomes a card showing key fields.
2. **Horizontally scroll** — simpler, but acceptable for admin/power-user tables.

Never truncate data in cells without a tooltip showing the full value.

---

## Performance

- Virtualize long tables (> 500 rows) — render only visible rows.
- Use server-side pagination for datasets > 1,000 rows.
- Debounce column-filter inputs.
- Cache page results in memory during a session to avoid refetches on page-back.
