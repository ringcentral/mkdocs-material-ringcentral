# Tables

Tables display structured data in rows and columns. Use them when users need to compare values, scan for specific records, or understand relationships between multiple attributes.

---

## Basic table

```markdown
| Connector | Status | Last sync | Records |
|-----------|--------|-----------|---------|
| Salesforce | ✅ Active | 2 min ago | 1,234 |
| HubSpot | ✅ Active | 5 min ago | 892 |
| Clio | ⚠️ Warning | 2 hrs ago | 456 |
| Bullhorn | ❌ Error | — | — |
```

Renders as:

| Connector | Status | Last sync | Records |
|-----------|--------|-----------|---------|
| Salesforce | ✅ Active | 2 min ago | 1,234 |
| HubSpot | ✅ Active | 5 min ago | 892 |
| Clio | ⚠️ Warning | 2 hrs ago | 456 |
| Bullhorn | ❌ Error | — | — |

---

## Column alignment

Use alignment markers in the separator row:

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Default text | Centered | Numbers |
| More text | Centered | 1,234 |
```

| Left | Center | Right |
|:-----|:------:|------:|
| Default text | Centered | Numbers |
| More text | Centered | 1,234 |

**Rule:** Right-align numeric columns so decimal points and digits align vertically.

---

## Table design specifications

| Property | Value |
|----------|-------|
| Header background | `#F6F8FA` |
| Header font | 12px, weight 600, uppercase, `#5A6070` |
| Row height (default) | 48px |
| Row height (compact) | 36px |
| Row height (spacious) | 60px |
| Cell padding | `12px 16px` |
| Row hover | `--ac-peach` background |
| Selected row | `--ac-peach` background + left border `--ac-orange-raw` |
| Border | `1px solid #DDD0D8` (horizontal only) |
| Striped rows (optional) | Alternate `#FAFAFA` |

---

## Table variants

### Default (bordered rows)

Standard table with horizontal dividers between rows.

### Striped

Alternating row shading for very wide tables where horizontal scanning is difficult:

```html
<table class="rc-table rc-table--striped">…</table>
```

### Compact

Reduced row height for dense data displays (log viewers, admin panels):

```html
<table class="rc-table rc-table--compact">…</table>
```

### Sortable columns

Clickable column headers with sort-direction indicators. See [Data Table pattern](../patterns/data-tables.md) for the full sortable table pattern including keyboard behavior.

---

## Usage guidelines

**Do:**

- Use a table when users need to compare values across rows.
- Right-align numeric data and left-align text data.
- Include a clear column header for every column — never leave a header blank except for checkbox/action columns.
- Allow columns to be sorted when sort order is meaningful.
- Show "—" for empty/null values rather than leaving cells blank.

**Don't:**

- Use a table to lay out non-tabular content — use grid or flex layout instead.
- Create tables with more than 8–10 columns without providing horizontal scroll or column customization.
- Use tables on mobile without testing — consider a card-based layout for small screens.
- Mix table rows that have very different content shapes — consider separate tables.

---

## Responsive behavior

Tables wider than their container should scroll horizontally, not collapse columns or truncate data:

```css
.rc-table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
```

On narrow screens (< 768px), consider switching to a card-based layout if the table's primary purpose is browsing rather than comparison.

---

## Empty table state

When a table has no rows, show an [empty state](../patterns/empty-states.md) within the table container — not an empty grid:

```html
<table class="rc-table">
  <thead>
    <tr><th>Connector</th><th>Status</th></tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2" class="rc-table__empty">
        <div class="rc-empty-state">
          No connectors yet. <a href="/connectors/add">Add your first connector</a>.
        </div>
      </td>
    </tr>
  </tbody>
</table>
```

---

## Accessibility

- Always use `<th>` for header cells with `scope="col"` or `scope="row"`.
- Provide a `<caption>` or `aria-label` on the `<table>` element to describe its purpose.
- For sortable columns, use `aria-sort="ascending"`, `aria-sort="descending"`, or `aria-sort="none"`.
- Ensure row-level actions (edit, delete) have unique accessible labels — "Edit Salesforce" not just "Edit".

```html
<table aria-label="Connected integrations">
  <thead>
    <tr>
      <th scope="col" aria-sort="ascending">Connector</th>
      <th scope="col">Status</th>
      <th scope="col">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Salesforce</td>
      <td>Active</td>
      <td>
        <button aria-label="Edit Salesforce connector">Edit</button>
      </td>
    </tr>
  </tbody>
</table>
```
