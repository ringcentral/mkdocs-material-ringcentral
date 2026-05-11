# Empty States

Empty states appear when there is no content to display. Done well, they explain *why* there's nothing there and *what the user can do* about it. Done poorly, they leave users confused and stuck.

---

## Types of empty states

### First-use empty state

The user has just arrived at a feature they haven't configured yet. This is an opportunity to guide them through setup.

**Elements:**
- Illustration or icon (large, 64–96px)
- Headline: what can they do here?
- Body: 1–2 sentences explaining the value
- Primary CTA: the first action to take
- Optional secondary link: docs, video tutorial

**Example:**

> :material-puzzle-outline:{ style="font-size: 3rem" }
>
> **No connectors yet**
>
> Connect RingCentral to your CRM to automatically log calls and sync contacts.
>
> [Add your first connector →]()

---

### No-results empty state

The user searched or filtered and got zero results. Helps them understand why and suggests next steps.

**Elements:**
- Icon (smaller — 48px, no heavy illustration)
- Headline: what the search returned
- Body: suggest adjusting the query or clearing filters
- CTA: clear filters / broaden search

**Example:**

> :material-magnify-close:{ style="font-size: 2rem" }
>
> **No connectors match "salesforc"**
>
> Check your spelling or [clear the search](#) to see all connectors.

---

### Cleared / deleted empty state

The user deleted or removed all items. Brief confirmation that the action succeeded.

**Example:**

> :material-check-circle:{ style="font-size: 2rem" }
>
> **All connectors removed**
>
> Your workspace is clean. [Add a connector](#) when you're ready.

---

### Error empty state

Data failed to load. Distinct from a no-results state — this is a system failure, not an expected outcome.

**Elements:**
- Error icon (not a cute illustration — this is a real problem)
- Headline: what failed
- Body: is it temporary? who to contact?
- CTA: retry

**Example:**

> :material-alert-circle:{ style="font-size: 2rem" }
>
> **Couldn't load your connectors**
>
> This is a temporary issue on our end. Try refreshing — if it persists, [contact support](#).
>
> [Try again →]()

---

## Copy guidelines

| Part | Guidance |
|------|----------|
| Headline | Specific state — "No connectors" not "No data" |
| Body | Max 2 sentences. Explain why and what to do. |
| CTA | Verb-first — "Add connector", "Clear filters", "Try again" |
| Tone | Helpful and direct — not cute or apologetic |

---

## Illustration usage

| State type | Illustration guidance |
|------------|----------------------|
| First use | Warm, brand-appropriate illustration or large icon |
| No results | Small icon, no illustration |
| Cleared | Small check icon, no illustration |
| Error | Warning/error icon, no illustration |

!!! warning "Keep illustrations tasteful"
    Illustrations are appropriate for first-use states where you want to convey warmth and motivate action. Don't use playful illustrations for error states — they undermine trust when something actually went wrong.

---

## Layout

```
┌──────────────────────────────────────┐
│                                      │
│           [Illustration]             │  ← 64–96px icon or image
│                                      │
│         Headline text                │  ← H3, centered
│                                      │
│    One or two sentences of body      │  ← Body text, centered, max 320px wide
│         copy go here.                │
│                                      │
│         [ Primary CTA ]              │  ← Button, centered
│      Secondary link (optional)       │
│                                      │
└──────────────────────────────────────┘
```

Center the empty state within the container it belongs to. For full-page empty states, center vertically in the main content area.

---

## Do's and don'ts

| Do | Don't |
|----|-------|
| Say what the user can do next | Show a blank space with no explanation |
| Use first-use states to explain value | Use the same empty state for every scenario |
| Make the CTA the most obvious next step | Use vague CTAs like "Get started" without context |
| Be brief (2–3 elements max) | Write paragraphs explaining every detail |
