# Tabs

Tabs organize content into parallel views within the same context. Use tabs when users need to switch between related content sections without losing their place.

---

## Variants

### Content tabs (MkDocs)

Content tabs are the primary tab pattern in documentation. They switch between parallel representations of the same subject (code in different languages, steps for different platforms, etc.).

=== "macOS"
    ```bash
    brew install mkdocs
    pip install mkdocs-material-ringcentral
    ```

=== "Windows"
    ```powershell
    pip install mkdocs mkdocs-material mkdocs-material-ringcentral
    ```

=== "Linux"
    ```bash
    pip install mkdocs mkdocs-material mkdocs-material-ringcentral
    ```

```markdown
=== "macOS"
    ```bash
    brew install mkdocs
    ```

=== "Windows"
    ```powershell
    pip install mkdocs
    ```

=== "Linux"
    ```bash
    pip install mkdocs
    ```
```

!!! note "Linked tabs"
    Enable `content.tabs.link` in `mkdocs.yml` so tab selections persist across the site — selecting "Windows" in one tab group switches all tab groups to "Windows".

    ```yaml
    theme:
      features:
        - content.tabs.link
    ```

---

### UI tabs (product interface)

For in-product tab bars that switch between views within a page or panel.

```html
<div class="rc-tabs" role="tablist" aria-label="Connector settings">
  <button
    class="rc-tab rc-tab--active"
    role="tab"
    aria-selected="true"
    aria-controls="panel-general"
    id="tab-general"
  >
    General
  </button>
  <button
    class="rc-tab"
    role="tab"
    aria-selected="false"
    aria-controls="panel-advanced"
    id="tab-advanced"
    tabindex="-1"
  >
    Advanced
  </button>
  <button
    class="rc-tab"
    role="tab"
    aria-selected="false"
    aria-controls="panel-logs"
    id="tab-logs"
    tabindex="-1"
  >
    Logs
  </button>
</div>

<div id="panel-general" role="tabpanel" aria-labelledby="tab-general">
  <!-- General settings content -->
</div>
<div id="panel-advanced" role="tabpanel" aria-labelledby="tab-advanced" hidden>
  <!-- Advanced settings content -->
</div>
```

---

## Sizes

| Variant | Height | Font | Usage |
|---------|--------|------|-------|
| Default | 40px | 14px, weight 600 | Standard page-level tabs |
| Compact | 32px | 13px, weight 600 | Panel tabs, dense UIs |

---

## Tab states

| State | Visual |
|-------|--------|
| Default | Text `#5A6070` |
| Hover | Text `#1A1A2E`, `--ac-peach` background |
| Active | Text `--ac-orange-raw`, 2px bottom border `--ac-orange-raw` |
| Focus | Focus ring |
| Disabled | 40% opacity, `cursor: not-allowed` |

---

## Usage guidelines

**Do:**

- Use tabs for genuinely parallel content — every tab should be at the same conceptual level.
- Keep tab labels short: 1–2 words.
- Show the default/recommended tab first.
- Preserve tab state on navigation within the same session.

**Don't:**

- Use tabs to replace navigation — if tabs feel like navigation, use [Navigation](navigation.md) instead.
- Have more than 5–6 tabs — use a dropdown or sidebar for more options.
- Use tabs for sequential steps — use a stepper or wizard instead.
- Change the URL for each tab unless tabs represent genuinely different pages.

---

## Keyboard interaction

Tabs must follow the ARIA tablist keyboard pattern:

| Key | Action |
|-----|--------|
| `Tab` | Move focus into/out of the tab list |
| `←` / `→` | Move focus between tabs (and auto-activate) |
| `Home` | Focus first tab |
| `End` | Focus last tab |
| `Enter` / `Space` | Activate focused tab (if not auto-activating) |

```javascript
tabList.addEventListener('keydown', (e) => {
  const tabs = [...tabList.querySelectorAll('[role="tab"]')];
  const current = tabs.indexOf(document.activeElement);

  if (e.key === 'ArrowRight') {
    tabs[(current + 1) % tabs.length].focus();
  } else if (e.key === 'ArrowLeft') {
    tabs[(current - 1 + tabs.length) % tabs.length].focus();
  } else if (e.key === 'Home') {
    tabs[0].focus();
  } else if (e.key === 'End') {
    tabs[tabs.length - 1].focus();
  }
});
```
