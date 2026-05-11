# Tables

Tables in MkDocs Material render with zebra striping, hover highlighting, and horizontal scroll on overflow — all via the `tables` extension.

---

## Basic syntax

```markdown
| Column one | Column two | Column three |
|------------|------------|--------------|
| Row 1 A    | Row 1 B    | Row 1 C      |
| Row 2 A    | Row 2 B    | Row 2 C      |
```

| Column one | Column two | Column three |
|------------|------------|--------------|
| Row 1 A    | Row 1 B    | Row 1 C      |
| Row 2 A    | Row 2 B    | Row 2 C      |

The pipes at the start and end of each row are optional. The separator row (dashes) is required and must have at least one dash per column.

---

## Column alignment

Control alignment with colons in the separator row.

```markdown
| Left-aligned | Centre-aligned | Right-aligned |
|:-------------|:--------------:|--------------:|
| Default      | Centred        | 42            |
| Text         | Text           | 1,024         |
```

| Left-aligned | Centre-aligned | Right-aligned |
|:-------------|:--------------:|--------------:|
| Default      | Centred        | 42            |
| Text         | Text           | 1,024         |

Right-align numeric columns so digits line up on the decimal point. Centre-align short labels and icons. Left-align everything else.

---

## API parameter table

The standard pattern for documenting configuration options, manifest fields, and REST parameters.

```markdown
| Parameter | Type | Required | Default | Description |
|-----------|------|:--------:|---------|-------------|
| `name` | `string` | ✅ | — | Display name shown in the UI |
| `version` | `string` | ✅ | — | Semantic version, e.g. `1.0.0` |
| `enabled` | `boolean` | | `true` | Whether the connector is active |
| `syncInterval` | `number` | | `300` | Seconds between background syncs |
| `fields` | `object[]` | ✅ | — | CRM field mapping definitions |
```

| Parameter | Type | Required | Default | Description |
|-----------|------|:--------:|---------|-------------|
| `name` | `string` | ✅ | — | Display name shown in the UI |
| `version` | `string` | ✅ | — | Semantic version, e.g. `1.0.0` |
| `enabled` | `boolean` | | `true` | Whether the connector is active |
| `syncInterval` | `number` | | `300` | Seconds between background syncs |
| `fields` | `object[]` | ✅ | — | CRM field mapping definitions |

---

## Comparison table

For feature comparisons and do/don't guidance. Use ✓ / ✗ with restraint — one symbol per cell is readable; two or more creates noise.

```markdown
| Feature | Starter | Professional | Enterprise |
|---------|:-------:|:------------:|:----------:|
| Call logging | ✓ | ✓ | ✓ |
| Contact matching | ✓ | ✓ | ✓ |
| Screen pop | — | ✓ | ✓ |
| AI summaries | — | ✓ | ✓ |
| Custom field mapping | — | — | ✓ |
| Dedicated support SLA | — | — | ✓ |
```

| Feature | Starter | Professional | Enterprise |
|---------|:-------:|:------------:|:----------:|
| Call logging | ✓ | ✓ | ✓ |
| Contact matching | ✓ | ✓ | ✓ |
| Screen pop | — | ✓ | ✓ |
| AI summaries | — | ✓ | ✓ |
| Custom field mapping | — | — | ✓ |
| Dedicated support SLA | — | — | ✓ |

---

## Inline code and links in cells

Markdown inside cells is rendered normally — inline code, links, bold, and emphasis all work.

```markdown
| Class | Purpose |
|-------|---------|
| `.rc-bar` | [Orange left-bar variant](grid-cards.md) |
| `.rc-navy` | Dark navy surface |
| `.rc-gradient` | `background-clip` gradient border |
```

| Class | Purpose |
|-------|---------|
| `.rc-bar` | [Orange left-bar variant](grid-cards.md) |
| `.rc-navy` | Dark navy surface |
| `.rc-gradient` | `background-clip` gradient border |

---

## Wide tables

Tables wider than the content column automatically get a horizontal scrollbar — no extra markup needed. For very wide tables (8+ columns), consider splitting into two tables or using a collapsible `???` block for secondary columns.

---

## When not to use a table

Prefer prose or a list when:

- There are only two columns and fewer than four rows — a definition list or a bulleted list reads more naturally
- The "table" is really a single key/value pair per item — use a `dl` in HTML or a formatted list
- Content in cells is longer than two lines — tables become hard to scan; use sections with headings instead

A good table has short, parallel cell content and a header row that makes the relationship between columns self-explanatory.
