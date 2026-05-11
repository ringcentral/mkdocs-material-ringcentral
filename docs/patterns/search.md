# Search

Search helps users find content quickly within a page, a section, or across the entire product. Different search contexts require different levels of complexity.

---

## Search types

| Type | Scope | Example |
|------|-------|---------|
| **Global search** | Entire product | Command palette, site-wide search |
| **List/table filter** | Current page dataset | Searching within a connector list |
| **Combobox** | Predefined options | Selecting a CRM from a dropdown with search |
| **Full-text** | Document content | MkDocs built-in site search |

---

## Global search (command palette)

A keyboard-triggered overlay that searches across all content. Triggered with `Cmd+K` / `Ctrl+K`.

```html
<div class="rc-command-palette" role="dialog" aria-label="Search" aria-modal="true">
  <div class="rc-command-palette__input-wrap">
    <span class="rc-command-palette__icon" aria-hidden="true">:material-magnify:</span>
    <input
      type="search"
      class="rc-command-palette__input"
      placeholder="Search docs, connectors, settings…"
      autocomplete="off"
      aria-autocomplete="list"
      aria-controls="search-results"
      aria-activedescendant=""
      role="combobox"
      aria-expanded="false"
    />
    <kbd class="rc-kbd">Esc</kbd>
  </div>

  <ul id="search-results" role="listbox" aria-label="Search results">
    <li role="option" aria-selected="true">
      <span class="rc-search-result__icon" aria-hidden="true">:material-file:</span>
      <span class="rc-search-result__title">Salesforce connector</span>
      <span class="rc-search-result__meta">Connectors</span>
    </li>
  </ul>
</div>
```

---

## List filter (inline search)

A search input above a list or table that filters the visible items:

```html
<div class="rc-search-bar">
  <label for="filter-connectors" class="sr-only">Filter connectors</label>
  <div class="rc-search-bar__input-wrap">
    <span class="rc-search-bar__icon" aria-hidden="true">:material-magnify:</span>
    <input
      type="search"
      id="filter-connectors"
      class="rc-search-bar__input"
      placeholder="Filter connectors…"
      aria-controls="connector-list"
    />
    <button
      class="rc-search-bar__clear"
      aria-label="Clear search"
      hidden
    >✕</button>
  </div>
</div>

<p class="rc-search-results-count" aria-live="polite">
  Showing 3 of 12 connectors
</p>
```

---

## Search results states

### Searching (in-progress)

Show a spinner inside the search input while results load:

```html
<div class="rc-search-bar rc-search-bar--loading">
  <input type="search" … />
  <div class="rc-spinner rc-spinner--sm" aria-hidden="true"></div>
</div>
```

### Results found

Display results in a structured list. Highlight the matching term:

```html
<li>
  <mark>Sales</mark>force — CRM Connector
</li>
```

### No results

Show a helpful message with suggestions:

```html
<div class="rc-empty-state" role="status" aria-live="polite">
  <p><strong>No results for "salesforc"</strong></p>
  <p>Check your spelling, or <button onclick="clearSearch()">clear the search</button> to see all connectors.</p>
</div>
```

---

## MkDocs site search

The `material-ringcentral` plugin works alongside MkDocs Material's built-in search. Configure it in `mkdocs.yml`:

```yaml
plugins:
  - material-ringcentral
  - search:
      separator: '[\s\-\.]+'  # Split on spaces, hyphens, dots
```

Enable additional search features:

```yaml
theme:
  features:
    - search.highlight    # Highlights matched terms on the page
    - search.sharing      # Share search URLs
    - search.suggest      # Auto-complete suggestions
```

---

## Performance guidelines

- **Debounce** list filter inputs by 200–300ms to avoid unnecessary renders on every keystroke.
- **Minimum 2 characters** before triggering remote search to reduce API load.
- Cache recent results in memory to avoid redundant API calls within a session.
- Show a results count in real-time so users know filtering is working.

```javascript
let debounceTimer;
searchInput.addEventListener('input', () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    filterList(searchInput.value);
  }, 250);
});
```

---

## Accessibility

- Search inputs must have a visible label (or `aria-label`).
- Use `type="search"` for browser-native search semantics (adds a clear button in some browsers).
- Announce result count changes via `aria-live="polite"`.
- Clear button must be keyboard accessible and have `aria-label="Clear search"`.
- Command palette: full keyboard navigation, `Escape` closes, `↑`/`↓` navigates results, `Enter` activates.
