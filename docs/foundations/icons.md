# Icons

RingCentral products use the **Material Symbols** icon library as the primary icon set, supplemented by **Font Awesome** brand icons for social and third-party service logos. Icons are available inline via MkDocs Material's emoji extension.

---

## Icon library

The design system uses two icon sources:

| Source | Prefix | Best for |
|--------|--------|----------|
| Material Symbols (via Twemoji) | `:material-` | All product UI icons |
| Font Awesome (Brands) | `:fontawesome-brands-` | Social media, external services |
| Font Awesome (Regular/Solid) | `:fontawesome-regular-`, `:fontawesome-solid-` | Supplementary glyphs |
| Octicons | `:octicons-` | GitHub-flavored interface icons |

---

## Sizing

Icons should always be sized relative to their typographic context.

| Context | Size | Usage |
|---------|------|-------|
| Inline with body text | 16px / 1rem | Icons within sentences or labels |
| Button icon | 20px / 1.25rem | Icon-only buttons, icon+label buttons |
| Navigation item | 20px / 1.25rem | Sidebar and tab bar icons |
| Card decoration | 24px / 1.5rem | Feature icons in cards |
| Section illustration | 48px / 3rem | Empty state icons, section headers |
| Hero illustration | 64px–96px | Large decorative icons |

!!! tip "Optical sizing"
    Some icons look too heavy or too light at certain sizes. If an icon feels off at a prescribed size, move up or down one step in the scale (4px increments) before breaking from the system.

---

## Usage in Markdown

Use emoji shortcodes for icons in documentation content:

```markdown
:material-check-circle: Feature complete
:material-alert-circle: Needs attention
:material-information: More information available
:material-lock: Authentication required
```

Renders as:

- :material-check-circle: Feature complete
- :material-alert-circle: Needs attention
- :material-information: More information available
- :material-lock: Authentication required

---

## Common UI icons

### Navigation & wayfinding

| Icon | Code | Usage |
|------|------|-------|
| :material-home: | `:material-home:` | Home / dashboard |
| :material-arrow-left: | `:material-arrow-left:` | Back |
| :material-arrow-right: | `:material-arrow-right:` | Forward / proceed |
| :material-chevron-down: | `:material-chevron-down:` | Expand / dropdown indicator |
| :material-menu: | `:material-menu:` | Hamburger menu |
| :material-close: | `:material-close:` | Dismiss / close |
| :material-dots-vertical: | `:material-dots-vertical:` | More options (vertical) |
| :material-dots-horizontal: | `:material-dots-horizontal:` | More options (horizontal) |

### Actions

| Icon | Code | Usage |
|------|------|-------|
| :material-plus: | `:material-plus:` | Add / create |
| :material-pencil: | `:material-pencil:` | Edit |
| :material-delete: | `:material-delete:` | Delete |
| :material-content-copy: | `:material-content-copy:` | Copy |
| :material-download: | `:material-download:` | Download |
| :material-upload: | `:material-upload:` | Upload |
| :material-share: | `:material-share:` | Share |
| :material-filter: | `:material-filter:` | Filter |
| :material-magnify: | `:material-magnify:` | Search |
| :material-refresh: | `:material-refresh:` | Refresh / reload |

### Status & feedback

| Icon | Code | Usage |
|------|------|-------|
| :material-check-circle: | `:material-check-circle:` | Success |
| :material-alert-circle: | `:material-alert-circle:` | Error |
| :material-alert: | `:material-alert:` | Warning |
| :material-information: | `:material-information:` | Info |
| :material-clock-outline: | `:material-clock-outline:` | Pending / in progress |
| :material-lock: | `:material-lock:` | Locked / authenticated |
| :material-lock-open: | `:material-lock-open:` | Unlocked |

### Communication

| Icon | Code | Usage |
|------|------|-------|
| :material-phone: | `:material-phone:` | Phone call |
| :material-video: | `:material-video:` | Video call |
| :material-message: | `:material-message:` | Message / chat |
| :material-email: | `:material-email:` | Email |
| :material-bell: | `:material-bell:` | Notifications |
| :material-account: | `:material-account:` | User / contact |
| :material-account-group: | `:material-account-group:` | Team / group |

---

## Accessibility

Icons used without visible text labels **must** have an accessible name:

```html
<!-- Icon with visible label — no extra aria needed -->
<button>
  <span class="icon"><!-- svg --></span>
  Delete
</button>

<!-- Icon-only button — requires aria-label -->
<button aria-label="Delete item">
  <span class="icon"><!-- svg --></span>
</button>

<!-- Decorative icon — hide from screen readers -->
<span aria-hidden="true"><!-- svg --></span>
```

!!! warning "Never use icons alone for status"
    Always pair status icons (success, error, warning) with text or a tooltip. Color-blind users and screen reader users both depend on this.

---

## Don'ts

- **Don't use icons from multiple libraries on the same screen** for the same conceptual role — pick one source per product.
- **Don't scale icons to non-standard sizes** — stay on the sizing scale.
- **Don't use decorative icons in dense data tables** — they add visual noise without helping comprehension.
- **Don't invent new icons** — request additions to the library if a needed icon is absent.
