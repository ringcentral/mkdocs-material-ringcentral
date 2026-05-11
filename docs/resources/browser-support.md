# Browser Support

RingCentral products support modern evergreen browsers. We use progressive enhancement to ensure core functionality works broadly, while layering enhancements for capable environments.

---

## Supported browsers

| Browser | Minimum version | Notes |
|---------|----------------|-------|
| Chrome | Last 2 versions | Primary development and testing browser |
| Firefox | Last 2 versions | Fully supported |
| Safari | Last 2 versions (macOS + iOS) | Test on both mobile and desktop |
| Edge | Last 2 versions | Chromium-based — shares Chrome compatibility |
| Samsung Internet | Last 2 versions | Important for Android users |
| Chrome for Android | Last 2 versions | Primary mobile browser |
| Safari on iOS | Last 2 versions | Required for iOS users |

---

## Unsupported browsers

| Browser | Status | Notes |
|---------|--------|-------|
| Internet Explorer (all versions) | ❌ Not supported | IE reached end-of-life June 2022 |
| Chrome < 90 | ❌ Not supported | Missing CSS Grid support |
| Firefox < 85 | ❌ Not supported | |
| Opera Mini | ⚠️ Limited | Core content only, no interactive features |

---

## Progressive enhancement strategy

We build in layers:

1. **Core layer:** Semantic HTML — works in any browser, screen reader, or search crawler.
2. **Enhancement layer:** CSS layout, typography, and visual design.
3. **Interaction layer:** JavaScript interactions — keyboard navigation, animations, dynamic updates.

If JavaScript fails, the page should degrade gracefully to a usable static state.

---

## CSS feature support

| Feature | Status | Fallback |
|---------|--------|---------|
| CSS Grid | ✅ Required | Flex layout fallback for older mobile |
| CSS Custom Properties | ✅ Required | No IE support needed |
| `aspect-ratio` | ✅ | Padding hack for very old browsers |
| Container queries | 🟡 Used where available | Viewport-based media queries |
| `:has()` selector | 🟡 Used for enhancements | Fallback via JavaScript class toggle |
| `@layer` | 🟡 Used internally | Specificity management via class names |
| `inert` attribute | ✅ | `aria-hidden` + `tabindex="-1"` polyfill |
| Subgrid | 🟡 Enhancement | CSS Grid fallback |

---

## JavaScript requirements

RingCentral products require JavaScript for interactive features. Server-rendered content must be accessible without JavaScript where feasible (navigation, static content).

**Required browser APIs:**

| API | Usage |
|-----|-------|
| `fetch` | API calls |
| `IntersectionObserver` | Lazy loading, infinite scroll |
| `ResizeObserver` | Responsive component adaptations |
| `MutationObserver` | Dynamic DOM updates |
| `CSS.supports()` | Feature detection |
| `localStorage` | User preferences |
| `dialog` element | Native dialog (with polyfill fallback) |

---

## Mobile and touch

- Touch targets must be at minimum **44×44px** (Apple HIG and WCAG 2.5.5).
- No hover-only interactions on primary actions — all hover states must be reachable on touch via focus or tap.
- Test on real devices — iOS simulator and Android emulator don't perfectly represent real behavior.
- `font-size` on inputs must be **≥ 16px** on iOS to prevent auto-zoom on focus.

---

## Viewport and screen sizes

| Breakpoint | Width |
|------------|-------|
| Minimum supported | 320px (iPhone SE) |
| Tablet | 768px |
| Desktop | 1024px |
| Wide | 1280px |

Test at each major breakpoint and at 320px minimum. Document any intentional layout differences at each breakpoint.

---

## Testing environments

The CI pipeline runs automated accessibility and visual regression tests against:

- Chrome (latest stable) — Linux headless
- Firefox (latest stable) — Linux headless

Manual testing is required on:

- Safari + macOS (VoiceOver accessibility testing)
- Safari + iOS (touch behavior and viewport handling)
- Chrome + Android (touch behavior)
