# Grid & Layout

RingCentral products use a responsive 12-column grid with defined breakpoints. The grid ensures consistent alignment across screens and scales gracefully from mobile to widescreen.

---

## Breakpoints

| Name | Token | Min width | Typical device |
|------|-------|-----------|----------------|
| `xs` | — | 0px | Small phones |
| `sm` | `--breakpoint-sm` | 480px | Large phones |
| `md` | `--breakpoint-md` | 768px | Tablets |
| `lg` | `--breakpoint-lg` | 1024px | Laptops |
| `xl` | `--breakpoint-xl` | 1280px | Desktops |
| `2xl` | `--breakpoint-2xl` | 1536px | Wide screens |

---

## 12-column grid

| Breakpoint | Columns | Gutter | Margin |
|------------|---------|--------|--------|
| xs (< 480px) | 4 | 16px | 16px |
| sm (≥ 480px) | 4 | 16px | 24px |
| md (≥ 768px) | 8 | 24px | 32px |
| lg (≥ 1024px) | 12 | 24px | 48px |
| xl (≥ 1280px) | 12 | 32px | 64px |

---

## Content column widths

| Layout type | Max width | Usage |
|-------------|-----------|-------|
| Reading column | 720px | Long-form content, documentation |
| Form column | 480px | Single-column forms |
| Wide content | 960px | Tables, dashboards |
| Full bleed | 100% | Hero images, banners, data-heavy pages |

---

## Page anatomy

A typical product page is composed of these nested layout regions:

```
┌─────────────────────────────────────────┐
│  Header (full bleed, gradient)          │
├─────────────────────────────────────────┤
│  Nav tabs (full bleed, gradient)        │
├──────────────┬──────────────────────────┤
│  Sidebar     │  Content column          │
│  240px       │  max-width: 960px        │
│              │                          │
│  Navigation  │  Page title              │
│  tree        │  ─────────               │
│              │  Body content            │
│              │                          │
│              │  ─────────               │
│              │  Related links           │
├──────────────┴──────────────────────────┤
│  Footer (full bleed)                    │
└─────────────────────────────────────────┘
```

---

## CSS Grid patterns

### Two-column card grid

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem; /* 24px */
}
```

### Sidebar + content layout

```css
.page-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 0;
}

@media (max-width: 768px) {
  .page-layout {
    grid-template-columns: 1fr; /* Stack on mobile */
  }
}
```

### Centered reading column

```css
.reading-column {
  max-width: 720px;
  margin-inline: auto;
  padding-inline: 1.5rem;
}
```

---

## MkDocs Material layout

The plugin sets the sidebar to a fixed 240px width. This overrides Material's default `12.1rem` sidebar so it aligns precisely with the gradient background:

```css
.md-sidebar--primary {
  width: 240px !important;
}
```

The main content area fills the remaining horizontal space with a standard Material content container. The `md-grid` class provides the responsive page-level grid.

---

## Responsive design guidance

- **Mobile first.** Define base styles for the smallest breakpoint, then add complexity as screens grow.
- **Don't hide mobile content on desktop.** If content is important enough for mobile, it's important for desktop too — re-layout, don't remove.
- **Test at 320px.** The smallest iPhone SE viewport. If the layout doesn't break here, it won't break anywhere.
- **Avoid fixed widths on content.** Let content containers flex to available space; reserve fixed widths for chrome elements like the sidebar.
