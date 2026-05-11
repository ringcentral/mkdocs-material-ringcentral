# Breadcrumbs

Breadcrumbs show a user's current location within a hierarchical structure. They let users understand where they are and navigate up the hierarchy without using the back button.

---

## When to use

Use breadcrumbs when:

- The site has **3 or more levels** of hierarchy.
- Users are likely to navigate up (not just back) — for example, drilling into a record from a list.
- The page content belongs to a clear parent/child relationship.

Do not use breadcrumbs when:

- The site is flat (1–2 levels) — they add noise without value.
- The user arrived via a single linear flow (wizard, onboarding) — use step progress instead.

---

## Automatic breadcrumbs in MkDocs

Enable the `navigation.path` feature in `mkdocs.yml` to automatically generate breadcrumbs from the site navigation hierarchy:

```yaml
theme:
  features:
    - navigation.path
```

This renders breadcrumbs above the page title on every page deeper than the root.

---

## Manual breadcrumb markup

```html
<nav aria-label="Breadcrumb">
  <ol class="rc-breadcrumb">
    <li class="rc-breadcrumb__item">
      <a href="/">Home</a>
    </li>
    <li class="rc-breadcrumb__item">
      <a href="/developers">Developer Guide</a>
    </li>
    <li class="rc-breadcrumb__item">
      <a href="/developers/interfaces">Interfaces</a>
    </li>
    <li class="rc-breadcrumb__item rc-breadcrumb__item--current" aria-current="page">
      createCallLog
    </li>
  </ol>
</nav>
```

---

## Specs

| Property | Value |
|----------|-------|
| Separator | `/` or `›` (CSS `::after` pseudo-element) |
| Font size | 13px |
| Font weight | 400 |
| Link color | `#5A6070` |
| Link hover color | `--ac-orange-raw` |
| Current page | `#1A1A2E`, no underline, not a link |
| Separator color | `#9EA8B8` |
| Item spacing | `4px` on either side of separator |

---

## Truncation

For very deep hierarchies, truncate middle levels:

```html
<nav aria-label="Breadcrumb">
  <ol class="rc-breadcrumb">
    <li><a href="/">Home</a></li>
    <li>
      <button class="rc-breadcrumb__ellipsis" aria-label="Show full breadcrumb path">
        …
      </button>
    </li>
    <li><a href="/interfaces">Interfaces</a></li>
    <li aria-current="page">createCallLog</li>
  </ol>
</nav>
```

---

## Accessibility

- Wrap breadcrumbs in `<nav aria-label="Breadcrumb">`.
- Use an `<ol>` (ordered list) — the order is meaningful.
- The current page item should have `aria-current="page"` and **not** be a link.
- Never use the breadcrumb as the only means of understanding location — the page title should also be descriptive.
