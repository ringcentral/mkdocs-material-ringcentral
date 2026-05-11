# Accessibility

RingCentral products target **WCAG 2.1 AA** compliance. Accessibility is a design and engineering requirement — not an afterthought. This page outlines the requirements, testing process, and implementation patterns used across the design system.

---

## Compliance target

| Standard | Level | Status |
|----------|-------|--------|
| WCAG 2.1 | AA | Required for all new product surfaces |
| WCAG 2.1 | AAA | Targeted where feasible (especially contrast) |
| Section 508 | — | Required for US government customers |
| EN 301 549 | — | Required for EU public sector customers |

---

## The four principles (POUR)

### Perceivable

Information must be presentable to users in ways they can perceive.

- All images have `alt` text.
- Videos have captions.
- Color is not the only means of conveying information.
- Text has sufficient contrast with its background (4.5:1 for normal text).
- Text can be resized to 200% without loss of content or functionality.

### Operable

All functionality is available from the keyboard.

- Every interactive element is reachable by `Tab`.
- Focus order matches the visual reading order.
- Focus is never trapped (except in dialogs, where it's intentionally managed).
- No keyboard traps — `Escape` or `Tab` always provides a way out.
- No time limits that can't be extended, unless they're security-critical.

### Understandable

Information and UI operation must be understandable.

- Language is declared on the `<html>` element (`lang="en"`).
- Navigation is consistent across pages.
- Error messages identify and describe the issue and how to resolve it.
- Labels and instructions are clear and sufficient before input.

### Robust

Content must be interpreted reliably by assistive technologies.

- All HTML is valid and uses semantic elements.
- Custom widgets implement the correct ARIA patterns.
- Status messages are announced by screen readers via `aria-live`.

---

## Keyboard patterns

Every interactive component must be keyboard-operable. These are the standard patterns from the ARIA Authoring Practices Guide:

| Component | Keys |
|-----------|------|
| Button | `Tab` to focus, `Enter`/`Space` to activate |
| Link | `Tab` to focus, `Enter` to activate |
| Checkbox | `Tab` to focus, `Space` to toggle |
| Radio group | `Tab` into group, `←`/`→` to move between options |
| Select | `Tab` to focus, `↑`/`↓` to navigate options |
| Dialog | `Tab`/`Shift+Tab` within dialog, `Escape` to close |
| Dropdown/Menu | `Enter`/`Space` to open, `↑`/`↓` to navigate, `Escape` to close |
| Tabs | `Tab` into tab list, `←`/`→` to switch tabs |
| Accordion | `Tab` to focus trigger, `Enter`/`Space` to toggle |
| Tooltip | Shows on focus, hides on blur, dismisses on `Escape` |

---

## Focus management

### Focus ring

Never remove the default focus ring without providing an equally visible alternative:

```css
/* Correct — replaces default ring with brand-styled one */
:focus-visible {
  outline: 2px solid var(--ac-orange-raw);
  outline-offset: 2px;
  border-radius: 2px;
}

/* Wrong — removes the ring entirely */
:focus { outline: none; }
```

### Focus trapping

Dialogs and drawers must trap focus while open:

```javascript
function trapFocus(container) {
  const focusable = container.querySelectorAll(
    'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last  = focusable[focusable.length - 1];

  container.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault(); last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault(); first.focus();
    }
  });
}
```

### Skip links

Every page must have a skip-to-main-content link as the first focusable element:

```html
<a class="skip-link" href="#main-content">Skip to main content</a>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--ac-orange-raw);
  color: white;
  padding: 8px;
  z-index: 9999;
}

.skip-link:focus {
  top: 0;
}
```

---

## Color contrast requirements

| Text type | Minimum ratio | Our target |
|-----------|--------------|------------|
| Normal text (< 18pt) | 4.5:1 | 7:1+ |
| Large text (≥ 18pt) | 3:1 | 4.5:1+ |
| UI components and graphics | 3:1 | 4.5:1+ |
| Placeholder text | 4.5:1 | 4.5:1+ |
| Disabled (exempt) | None | — |

Use the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) or browser DevTools to verify.

---

## Screen reader testing

Test with at minimum:

| Platform | Screen reader | Browser |
|----------|--------------|---------|
| macOS | VoiceOver | Safari |
| Windows | NVDA | Chrome |
| Windows | JAWS | Edge |
| iOS | VoiceOver | Safari |
| Android | TalkBack | Chrome |

**Key scenarios to test:**

- Form completion with error recovery
- Dialog open/close with focus management
- Dynamic content updates (toasts, live regions)
- Table navigation
- Icon-only button labels
- Pagination and list navigation

---

## Testing tools

| Tool | Use case |
|------|----------|
| [axe DevTools](https://www.deque.com/axe/) | Automated WCAG scanning in browser |
| [Lighthouse](https://developers.google.com/web/tools/lighthouse) | Automated accessibility audit |
| [WAVE](https://wave.webaim.org/) | Visual accessibility reporting |
| [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Color contrast verification |
| Browser DevTools (Accessibility tree) | Inspect ARIA roles and names |

Automated tools catch ~30–40% of accessibility issues. Manual testing with keyboard and screen reader is required for full coverage.

---

## Reporting issues

Found an accessibility issue? File a GitHub issue with:

1. The page or component affected
2. The specific WCAG criterion it fails (e.g., 1.4.3 Contrast Minimum)
3. The assistive technology and browser where it was found
4. Steps to reproduce

Tag issues with `accessibility` and assign severity: `a11y-blocker` (prevents task completion), `a11y-major` (significant barrier), `a11y-minor` (inconvenience).
