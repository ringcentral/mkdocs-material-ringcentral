# Motion

Motion in RingCentral products is purposeful and restrained. Animation communicates state changes, guides attention, and provides feedback — it never performs for its own sake.

---

## Principles

**Responsive, not decorative.** Every animation responds to a user action or communicates a system state. Idle animations (looping, unprompted) appear only in hero/marketing contexts.

**Fast and precise.** UI interactions use short durations (100–250ms). Long animations feel sluggish and break flow.

**Respect user preferences.** All motion respects the `prefers-reduced-motion` media query. Transitions reduce to instantaneous or simple opacity fades for users who have enabled reduced motion.

---

## Duration tokens

| Token | Value | Usage |
|-------|-------|-------|
| `duration-instant` | 0ms | Reduced-motion fallback, truly instantaneous state changes |
| `duration-fast` | 100ms | Micro-interactions: checkbox checks, toggle flips, button press |
| `duration-base` | 150ms | Default: hover states, focus rings, small state changes |
| `duration-moderate` | 200ms | Dropdown open/close, tooltip appear/disappear |
| `duration-slow` | 300ms | Dialog open/close, drawer slide, page transitions |
| `duration-deliberate` | 500ms | Onboarding reveals, skeleton-to-content |

---

## Easing tokens

| Token | Value | Usage |
|-------|-------|-------|
| `ease-standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | General state changes, entering and leaving |
| `ease-decelerate` | `cubic-bezier(0, 0, 0.2, 1)` | Elements entering the screen (drop in, slide in) |
| `ease-accelerate` | `cubic-bezier(0.4, 0, 1, 1)` | Elements leaving the screen (slide out, fade out) |
| `ease-sharp` | `cubic-bezier(0.4, 0, 0.6, 1)` | Elements that persist but change state (expand/collapse) |
| `ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful moments — FAB bounce, success animation |

---

## CSS reference

```css
:root {
  /* Durations */
  --duration-fast:       100ms;
  --duration-base:       150ms;
  --duration-moderate:   200ms;
  --duration-slow:       300ms;
  --duration-deliberate: 500ms;

  /* Easings */
  --ease-standard:    cubic-bezier(0.4, 0, 0.2, 1);
  --ease-decelerate:  cubic-bezier(0, 0, 0.2, 1);
  --ease-accelerate:  cubic-bezier(0.4, 0, 1, 1);
  --ease-sharp:       cubic-bezier(0.4, 0, 0.6, 1);
  --ease-spring:      cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## Common animation patterns

### Hover state

```css
.button {
  transition: background-color var(--duration-base) var(--ease-standard),
              box-shadow var(--duration-base) var(--ease-standard);
}
```

### Dropdown open/close

```css
.dropdown {
  transform-origin: top center;
  transition: transform var(--duration-moderate) var(--ease-decelerate),
              opacity  var(--duration-moderate) var(--ease-decelerate);
}

.dropdown[hidden] {
  transform: scaleY(0.9) translateY(-4px);
  opacity: 0;
}
```

### Dialog enter/exit

```css
.dialog-backdrop {
  transition: opacity var(--duration-slow) var(--ease-standard);
}

.dialog {
  transition: transform var(--duration-slow) var(--ease-decelerate),
              opacity   var(--duration-slow) var(--ease-decelerate);
}

.dialog[closing] {
  transition: transform var(--duration-moderate) var(--ease-accelerate),
              opacity   var(--duration-moderate) var(--ease-accelerate);
  transform: translateY(8px) scale(0.98);
  opacity: 0;
}
```

### Skeleton to content

```css
@keyframes skeleton-pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

.skeleton {
  animation: skeleton-pulse var(--duration-deliberate) var(--ease-standard) infinite;
}
```

---

## Reduced motion

**This is non-negotiable.** Wrap all non-trivial animations in a `prefers-reduced-motion` check:

```css
@media (prefers-reduced-motion: no-preference) {
  .animated-element {
    transition: transform 300ms var(--ease-decelerate);
  }
}

/* Fallback — still show state change, just without animation */
.animated-element {
  transition: opacity 150ms linear;
}
```

The hero canvas animation in `ringcentral.js` respects `prefers-reduced-motion` and stops emitting new lines when the preference is set.

---

## The hero canvas animation

The site header includes an animated radial canvas — lines radiate outward from a central origin, spaced at minimum 22.5° angles to prevent clumping. Key behaviors:

| Property | Value |
|----------|-------|
| Emission interval | 380ms |
| Max concurrent attempts | 60 |
| Minimum angle separation | 22.5° |
| Lines per emission | 1 |
| Respects `prefers-reduced-motion` | Yes — stops on `reduce` |
| Pauses on click/tap | Yes — resumes on second click |

The animation is cosmetic and has no functional impact. It can be disabled entirely:

```css
.md-hero canvas { display: none; }
```
