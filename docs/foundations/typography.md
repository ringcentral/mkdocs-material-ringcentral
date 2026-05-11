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

<div style="margin: 1.5rem 0 2.5rem; border-left: 3px solid #FF8800; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 1.25rem;">

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 3rem; font-weight: 800; line-height: 1.15; color: var(--md-default-fg-color);">Display</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">48px · weight 800 · line-height 1.15 · Hero headings</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 2.25rem; font-weight: 700; line-height: 1.2; color: var(--md-default-fg-color);">Heading 1</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">36px · weight 700 · line-height 1.2 · Page titles</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 1.75rem; font-weight: 700; line-height: 1.25; color: var(--md-default-fg-color);">Heading 2</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">28px · weight 700 · line-height 1.25 · Major sections</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 1.375rem; font-weight: 600; line-height: 1.3; color: var(--md-default-fg-color);">Heading 3</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">22px · weight 600 · line-height 1.3 · Sub-sections</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 1.125rem; font-weight: 600; line-height: 1.35; color: var(--md-default-fg-color);">Heading 4</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">18px · weight 600 · line-height 1.35 · Component groups</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 1rem; font-weight: 600; line-height: 1.4; color: var(--md-default-fg-color);">Heading 5</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">16px · weight 600 · line-height 1.4 · Minor headings, labels</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; font-weight: 600; line-height: 1.4; color: var(--md-default-fg-color);">Heading 6</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">14px · weight 600 · line-height 1.4 · Captions, small labels</div>
  </div>

  <div style="border-top: 1px solid var(--md-default-fg-color--lightest); padding-top: 1.25rem;">
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 1rem; font-weight: 400; line-height: 1.6; color: var(--md-default-fg-color);">Body large — The quick brown fox jumps over the lazy dog. This is what primary body copy looks like at 16px with a comfortable 1.6 line-height for long-form reading.</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">16px · weight 400 · line-height 1.6</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.875rem; font-weight: 400; line-height: 1.6; color: var(--md-default-fg-color);">Body — Interface copy and secondary descriptions sit at 14px. This weight and size is used for most text inside components and documentation pages.</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">14px · weight 400 · line-height 1.6</div>
  </div>

  <div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 400; line-height: 1.5; color: var(--md-default-fg-color);">Body small — Helper text, captions, and metadata. Use sparingly and never for primary content.</div>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.2rem;">12px · weight 400 · line-height 1.5</div>
  </div>

  <div>
    <span style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; line-height: 1.4; background: #FFF0DC; color: #CC6E00; border-radius: 4px; padding: 0.2rem 0.5rem; display: inline-block;">Label</span>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.4rem;">12px · weight 600 · line-height 1.4 · Form labels, badges, tags</div>
  </div>

  <div>
    <code style="font-family: 'Roboto Mono', monospace; font-size: 0.8125rem; font-weight: 400; line-height: 1.6;">const greeting = "Hello from RingCentral";</code>
    <div style="font-family: 'Inter Tight', sans-serif; font-size: 0.75rem; font-weight: 600; color: var(--md-default-fg-color--light); margin-top: 0.4rem;">Roboto Mono · 13px · weight 400 · line-height 1.6 · Inline code and code blocks</div>
  </div>

</div>

| Role | Size | Weight | Line height | Usage |
|------|------|--------|-------------|-------|
| **Display** | 48px / 3rem | 800 | 1.15 | Hero headings, splash screens |
| **H1** | 36px / 2.25rem | 700 | 1.2 | Page titles |
| **H2** | 28px / 1.75rem | 700 | 1.25 | Major section headings |
| **H3** | 22px / 1.375rem | 600 | 1.3 | Sub-section headings |
| **H4** | 18px / 1.125rem | 600 | 1.35 | Component group headings |
| **H5** | 16px / 1rem | 600 | 1.4 | Minor headings, labels |
| **H6** | 14px / 0.875rem | 600 | 1.4 | Captions, small section labels |
| **Body large** | 16px / 1rem | 400 | 1.6 | Primary body copy |
| **Body** | 14px / 0.875rem | 400 | 1.6 | Secondary body, interface copy |
| **Body small** | 12px / 0.75rem | 400 | 1.5 | Helper text, captions, metadata |
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

Never remove the content column constraint to make text span full width. For wide data (tables, code), horizontal scroll within a contained element is preferred over breaking the content width.

---

## Code typography

Code uses **Roboto Mono** at 13px / 0.8125rem. Code blocks get a light grey background and subtle border.

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
