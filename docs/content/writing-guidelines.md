# Writing Guidelines

Practical rules for UI copy. Apply these every time you write a label, heading, error message, tooltip, or button.

---

## Capitalization

### Title case

Use title case for:

- Navigation items ("Developer Guide", "Getting Started")
- Dialog and page titles ("Connect Your CRM")
- Section headings in marketing contexts

### Sentence case

Use sentence case for:

- Body copy and descriptions
- Form labels ("Full name", "Email address")
- Helper text and error messages
- Alert and banner text
- Tooltip content
- Button labels when they're instructional ("Learn more", "View all connectors")

### ALL CAPS

Never use all-caps in product copy, except in CSS for small badge/chip labels where it's a deliberate typographic treatment.

---

## Punctuation

### End punctuation

| Context | Rule |
|---------|------|
| Complete sentences (body, descriptions, helper text) | Period at end |
| Fragments used as labels, headings, button text | No period |
| Error messages (complete sentence) | Period at end |
| Tooltips (complete sentence) | Period at end |
| Tooltips (fragment or instruction) | No period |

**Examples:**

- Label: `Full name` — no period
- Helper: `Include country code for international numbers.` — period
- Button: `Save changes` — no period
- Error: `Enter a valid email address.` — period

### Oxford comma

Always use the Oxford comma in lists of three or more items.

- ✅ "Calls, SMS, and voicemails are logged."
- ❌ "Calls, SMS and voicemails are logged."

### Ellipsis (…)

Use the ellipsis character (`…` / `&hellip;`) not three periods (`...`). Use sparingly — for truncated text and "in progress" labels only.

- ✅ "Loading connectors…"
- ❌ "Loading connectors..."
- ❌ "View your settings..." (use "View settings" or link text instead)

### Ampersand (&)

Avoid in body text. Acceptable in space-constrained UI labels when both words are closely paired: "Terms & Conditions", "Calls & SMS".

---

## Button labels

Buttons describe the action they perform. The label should tell users exactly what will happen when they click.

**Format:** `[Verb] [object]`

| Good | Bad |
|------|-----|
| "Save changes" | "Submit" |
| "Delete connector" | "Delete" (ambiguous) |
| "Add your first connector" | "Get started" |
| "Send invitation" | "OK" |
| "Reconnect Salesforce" | "Fix it" |

**Pair labels:** When two buttons appear together, the pair should make their difference obvious without reading both labels. "Cancel" and "Delete connector" is better than "No" and "Yes."

---

## Error messages

| Principle | Guidance |
|-----------|----------|
| Say what happened | "We couldn't save your changes" not "An error occurred" |
| Say why (if known) | "…because your session expired" |
| Say what to do | "Sign in again to continue" |
| Keep it calm | Don't use exclamation marks or dramatic language |
| Avoid blame | "That email address isn't valid" not "You entered an invalid email" |

---

## Headings

- Use sentence case (capitalize first word and proper nouns only).
- Keep headings to 5–8 words maximum.
- One `H1` per page — the page title.
- Never use a heading just for visual styling — use it to help users navigate.
- Headings should work as navigation items: "Setting up your first connector" tells users what the section contains.

---

## Placeholder text

Placeholders are hints, not labels. They must:

- Show an example of the expected format: `+1 (555) 000-0000`
- Not repeat the label: if the label is "Email address", the placeholder should be `name@example.com` not "Email address"
- Disappear when the user types — never put instructions here that the user needs to reference while typing

---

## Numbers

| Rule | Example |
|------|---------|
| Spell out 1–9, use digits for 10+ | "three connectors", "12 records" |
| Always use digits for measurements and stats | "4px", "2 hours", "99+" |
| Use commas as thousands separator | "1,234 contacts" |
| Use decimals for precision where needed | "2.5 GB" |
| Don't start a sentence with a digit | Rewrite to put the number mid-sentence |

---

## Dates and times

| Format | Use |
|--------|-----|
| Relative (< 24h) | "2 minutes ago", "Today at 3:45 PM" |
| Absolute (> 24h) | "May 11, 2026" or "May 11" (same year) |
| Short date | "05/11/26" only in table cells where space is constrained |
| Time | 12-hour format with AM/PM: "3:45 PM" |

---

## Links

- Link text should describe the destination: "Read the migration guide" not "Click here".
- Avoid "Learn more" as standalone link text — include the subject: "Learn more about call logging".
- External links should open in a new tab with a visual indicator and `aria-label` noting this.

```html
<a href="https://docs.ringcentral.com" target="_blank" aria-label="RingCentral Docs (opens in new tab)">
  RingCentral Docs ↗
</a>
```
