# Loading States

Loading states manage perceived performance. The goal is to make waiting feel shorter, keep users informed, and prevent the interface from appearing broken.

---

## The 500ms rule

- **< 100ms:** No loading indicator needed — feels instantaneous.
- **100–500ms:** No loading indicator needed if you can optimistically update the UI.
- **500ms–2s:** Show a spinner. Don't show a skeleton for very short loads — the transition is jarring.
- **> 2s:** Show a skeleton screen or a progress bar with a message.
- **> 10s:** Show a progress bar with a percentage and estimated time. Let the user cancel.

---

## Patterns by context

### Button loading

When a button triggers an async action, replace the label with a spinner and disable the button:

```html
<!-- Before submit -->
<button class="md-button md-button--primary" id="save-btn">
  Save changes
</button>

<!-- While saving -->
<button class="md-button md-button--primary" disabled aria-busy="true" id="save-btn">
  <span class="rc-spinner rc-spinner--sm" aria-hidden="true"></span>
  Saving…
</button>

<!-- On success — briefly show, then restore -->
<button class="md-button md-button--primary" id="save-btn">
  <span aria-hidden="true">✓</span>
  Saved
</button>
```

---

### Inline content loading

When refreshing a small section of the page (a stats widget, a list item):

```html
<div class="rc-widget" aria-busy="true" aria-label="Loading activity feed…">
  <div class="rc-spinner" role="status">
    <span class="sr-only">Loading…</span>
  </div>
</div>
```

---

### List / table loading

Replace the list with skeleton rows that mirror the expected content shape:

```html
<ul class="rc-list" aria-busy="true" aria-label="Loading connectors…">
  <!-- 3 skeleton rows -->
  <li class="rc-list__item rc-list__item--skeleton" aria-hidden="true">
    <div class="rc-skeleton rc-skeleton--avatar"></div>
    <div class="rc-skeleton__content">
      <div class="rc-skeleton__line rc-skeleton__line--title"></div>
      <div class="rc-skeleton__line rc-skeleton__line--short"></div>
    </div>
  </li>
  <li class="rc-list__item rc-list__item--skeleton" aria-hidden="true"><!-- repeat --></li>
  <li class="rc-list__item rc-list__item--skeleton" aria-hidden="true"><!-- repeat --></li>
</ul>
```

Show the same number of skeleton rows as the expected page size (or a reasonable default like 5–8).

---

### Page loading

For full-page transitions and initial app hydration:

```html
<div class="rc-page-load" role="status" aria-label="Loading…">
  <div class="rc-spinner rc-spinner--lg"></div>
  <p>Loading your connectors…</p>
</div>
```

---

### File upload / long operation

Use a determinate [progress bar](../components/progress.md) with text:

```html
<div class="rc-progress-card" role="status">
  <div class="rc-progress-card__header">
    <span>Importing contacts</span>
    <span>234 of 1,500</span>
  </div>
  <div class="rc-progress" role="progressbar"
       aria-valuenow="16"
       aria-valuemin="0"
       aria-valuemax="100"
       aria-label="Importing contacts: 16%">
    <div class="rc-progress__fill" style="width: 16%"></div>
  </div>
  <div class="rc-progress-card__footer">
    <span>About 45 seconds remaining</span>
    <button class="md-button rc-button--sm">Cancel</button>
  </div>
</div>
```

---

## Optimistic updates

For fast, reversible actions (toggling a setting, marking an item), update the UI immediately without waiting for the server response. Revert and show an error if the request fails.

```javascript
// Toggle connector on/off
async function toggleConnector(id, enabled) {
  // Update UI immediately
  updateConnectorUI(id, enabled);

  try {
    await api.patchConnector(id, { enabled });
  } catch (err) {
    // Revert and show error
    updateConnectorUI(id, !enabled);
    showErrorBanner('Couldn't update connector — try again.');
  }
}
```

Optimistic updates make the app feel snappier. Use them for:
- Toggle on/off
- Mark as read/unread
- Reorder items
- Like/star/favorite

Do **not** use optimistic updates for:
- Deletes (use a confirmation dialog + show a "Deleting…" state)
- Multi-step forms (wait for server confirmation)
- Payments or irreversible actions

---

## Avoiding loading state flicker

A loading spinner that flashes in and out faster than 200ms is worse than no spinner at all. Use a minimum display time:

```javascript
async function fetchWithMinDelay(fn, minMs = 300) {
  const [result] = await Promise.all([
    fn(),
    new Promise(r => setTimeout(r, minMs))
  ]);
  return result;
}
```
