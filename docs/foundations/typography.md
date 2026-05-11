# Typography

RingCentral uses **Inter Tight** for all UI text and **Roboto Mono** for code and technical content. The type scale is built on a modular ratio to create clear visual hierarchy without overcomplicating decisions.

---

## Font families

| Token | Family | Weights | Usage |
|-------|--------|---------|-------|
| `--md-text-font` | Inter Tight | 400, 600, 700, 800, 900 | All UI copy — labels, headings, body |
| `--md-code-font` | Roboto Mono | 400, 500 | Code blocks, terminal output, IDs, tokens |

Both fonts load from Google Fonts. The CSS import is handled automatically by the `material-ringcentral` plugin.

```css
@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;600;700;800;900&family=Roboto+Mono:wght@400;500&display=swap');
```

---

## Type scale

| Role | Size | Weight | Line height | Usage |
|------|------|--------|-------------|-------|
| **Display** | 48px / 3rem | 800 | 1.15 | Hero headings, splash screens |
| **H1** | 36px / 2.25rem | 700 | 1.2 | Page titles |
| **H2** | 28px / 1.75rem | 700 | 1.25 | Major section headings |
| **H3** | 22px / 1.375rem | 600 | 1.3 | Sub-section headings |
| **H4** | 18px / 1.125rem | 600 | 1.35 | Component group headings |
| **H5** | 16px / 1rem | 600 | 1.4 | Minor headings, labels |
| **H6** | 14px / 0.875rem | 600 | 1.4 | Captions, small section labels |
| **Body Large** | 16px / 1rem | 400 | 1.6 | Primary body copy |
| **Body** | 14px / 0.875rem | 400 | 1.6 | Secondary body, interface copy |
| **Body Small** | 12px / 0.75rem | 400 | 1.5 | Helper text, captions, metadata |
| **Label** | 12px / 0.75rem | 600 | 1.4 | Form labels, tags, badge text |
| **Code** | 13px / 0.8125rem | 400 | 1.6 | Inline code, code blocks |

---

## Headings

Use semantic heading levels (`h1`–`h6`) in document order. Never skip levels for visual effect — use the type scale tokens instead.

```markdown
# Page Title (H1)
## Major Section (H2)
### Sub-section (H3)
#### Component Group (H4)
```

!!! warning "One H1 per page"
    Each page should have exactly one `H1` — the page title. Screen readers and search engines use `H1` as the document root.

---

## Font weights

| Weight | Usage |
|--------|-------|
| **400 Regular** | Body copy, helper text, placeholder text |
| **600 SemiBold** | Labels, navigation items, secondary headings |
| **700 Bold** | Headings H2–H4, button labels, CTAs |
| **800 ExtraBold** | H1, display headings |
| **900 Black** | Hero text only — use sparingly |

---

## Line length

Optimal reading line length is **60–80 characters** (roughly 30–40em). The content column in MkDocs Material is constrained to this range by default.

- **Never** remove the content column constraint to make text span full width.
- For wide data (tables, code), horizontal scroll within a contained element is preferred over breaking the content width.

---

## Code typography

Code uses **Roboto Mono** at 13px / 0.8125rem. Code blocks get a light grey background (`#F6F8FA`) and subtle border.

Inline code: `this is inline code`

Block code:

```python
def greet(name: str) -> str:
    """Return a RingCentral-branded greeting."""
    return f"Hello from RingCentral, {name}!"
```

---

## Localization notes

**CJK scripts** (Chinese, Japanese, Korean) fall back to the system UI font stack when Inter Tight doesn't have the required glyphs. Ensure adequate line-height (at least 1.8) for CJK body text.

**RTL languages** (Arabic, Hebrew) require `dir="rtl"` on the `html` element. The MkDocs Material theme has RTL support built in; verify all custom CSS uses logical properties (`margin-inline-start`, not `margin-left`).

---

## CSS reference

```css
/* Headings */
h1 { font-size: 2.25rem;  font-weight: 800; line-height: 1.2; }
h2 { font-size: 1.75rem;  font-weight: 700; line-height: 1.25; }
h3 { font-size: 1.375rem; font-weight: 600; line-height: 1.3; }
h4 { font-size: 1.125rem; font-weight: 600; line-height: 1.35; }
h5 { font-size: 1rem;     font-weight: 600; line-height: 1.4; }
h6 { font-size: 0.875rem; font-weight: 600; line-height: 1.4; }

/* Body */
body      { font-size: 0.875rem; font-weight: 400; line-height: 1.6; }
.text-sm  { font-size: 0.75rem;  line-height: 1.5; }
.label    { font-size: 0.75rem;  font-weight: 600; line-height: 1.4; }

/* Code */
code, pre { font-family: var(--md-code-font); font-size: 0.8125rem; }
```
