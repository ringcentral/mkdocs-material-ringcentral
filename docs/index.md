# RingCentral Design System

**One design language. Every product. Every platform.**

The RingCentral Design System provides everything teams need to build consistent, accessible, and beautiful product experiences — from foundational tokens and brand guidelines to production-ready component patterns.

---

## What's inside

<div class="grid cards" markdown>

-   :material-palette-outline: **Foundations**

    ---

    Color tokens, typography scale, spacing system, grid, iconography, motion, and elevation — the raw building blocks behind every UI decision.

    [:octicons-arrow-right-24: Explore foundations](foundations/index.md)

-   :material-cube-outline: **Components**

    ---

    A comprehensive library of tested, accessible UI components — buttons, inputs, cards, dialogs, navigation, and much more.

    [:octicons-arrow-right-24: Browse components](components/index.md)

-   :material-puzzle-outline: **Patterns**

    ---

    Repeatable solutions for common product problems: empty states, error handling, search, data tables, and notification flows.

    [:octicons-arrow-right-24: See patterns](patterns/index.md)

-   :material-text-box-outline: **Content**

    ---

    Voice and tone guidelines, writing principles, and an official terminology reference to keep every word on-brand.

    [:octicons-arrow-right-24: Read content guidelines](content/index.md)

</div>

---

## Design principles

These four principles inform every design decision in the system.

### Clarity first
Every element earns its place. We remove visual noise that forces users to work harder — empty space, purposeful hierarchy, and focused interactions replace decoration.

### Purposeful warmth
RingCentral products connect people. Our palette, typography, and interactions carry the warmth of human communication without sacrificing professionalism.

### Accessible by default
Accessibility is a constraint, not a feature. We design and build for WCAG 2.1 AA from the start, not as an afterthought.

### Predictably consistent
Patterns, components, and language behave the same way across every context. Users shouldn't have to learn a new mental model on each screen.

---

## Quick start

=== "Designers"

    1. Download the [Figma component library](#) from the RingCentral shared design library.
    2. Apply the **RingCentral 2026** theme to your file.
    3. Use components from the library — avoid detaching unless absolutely necessary.
    4. Reference this site for usage guidelines and accessibility requirements.

=== "Engineers"

    Install the MkDocs theme plugin for your documentation:

    ```bash
    pip install mkdocs-material-ringcentral
    ```

    Then configure it in your `mkdocs.yml`:

    ```yaml
    plugins:
      - material-ringcentral
      - search
    ```

    That's it — the full RingCentral brand layer is injected automatically.

=== "Content writers"

    1. Read the [Voice & Tone](content/voice-tone.md) guide first.
    2. Check the [Writing Guidelines](content/writing-guidelines.md) before drafting.
    3. Look up product and feature names in the [Terminology](content/terminology.md) reference.
    4. When in doubt, choose clarity over cleverness.

---

## What's new

| Version | Date | Highlights |
|---------|------|------------|
| **2.1.0** | May 2026 | New Drawer component, updated motion tokens, dark-mode contrast fixes |
| **2.0.0** | Jan 2026 | Full 2026 brand refresh — coral/orange/lavender palette, Inter Tight |
| **1.4.2** | Oct 2025 | Accessibility audit: 14 contrast fixes, focus-ring improvements |
| **1.4.0** | Aug 2025 | Chips, Banners, and Form Patterns added |

[:octicons-arrow-right-24: Full changelog](resources/changelog.md)

---

!!! info "This site is the living specification"
    Component behavior, token values, and usage rules on these pages are authoritative. If there is a conflict between this site and a Figma file or a code implementation, this site wins. File a GitHub issue to propose changes.
