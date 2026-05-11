# Avatars

Avatars represent users, contacts, or organizations. They provide visual identification in places where a name alone is insufficient — presence indicators, conversation threads, assigned tasks, and contact lists.

---

## Variants

### Photo avatar

When a profile photo is available:

```html
<img
  class="rc-avatar"
  src="photo.jpg"
  alt="Jane Smith"
  width="40"
  height="40"
/>
```

### Initials avatar

When no photo is available, show the user's initials on a colored background:

```html
<div class="rc-avatar rc-avatar--initials" aria-label="Jane Smith" style="--avatar-color: #FF7A35;">
  JS
</div>
```

### Icon avatar

For system entities, bots, or anonymous users:

```html
<div class="rc-avatar rc-avatar--icon" aria-label="System notification">
  <!-- :material-robot: -->
</div>
```

### Group avatar

Stacked avatars representing multiple users:

```html
<div class="rc-avatar-group" aria-label="Assigned to 3 people">
  <img class="rc-avatar" src="user1.jpg" alt="Jane Smith" />
  <img class="rc-avatar" src="user2.jpg" alt="John Doe" />
  <div class="rc-avatar rc-avatar--overflow" aria-hidden="true">+1</div>
</div>
```

---

## Sizes

| Size | Dimensions | Font | Usage |
|------|-----------|------|-------|
| `xs` | 20×20px | 9px | Inline in table cells, dense lists |
| `sm` | 24×24px | 10px | Compact UI, tags |
| `md` | 32×32px | 13px | List items, comments |
| **`lg`** | **40×40px** | **15px** | **Default — conversation headers** |
| `xl` | 56×56px | 20px | Profile pages, contact cards |
| `2xl` | 80×80px | 28px | User profile header |

---

## Presence indicators

Overlay a small colored dot to show user presence:

| Status | Color | Meaning |
|--------|-------|---------|
| Online | `#2E7D32` (green) | Active and available |
| Busy | `#D32F2F` (red) | On a call or do not disturb |
| Away | `#F57C00` (amber) | Idle or away |
| Offline | `#9EA8B8` (gray) | Not connected |

```html
<div class="rc-avatar-wrapper">
  <img class="rc-avatar" src="photo.jpg" alt="Jane Smith" />
  <span
    class="rc-avatar__presence rc-avatar__presence--online"
    aria-label="Online"
    role="img"
  ></span>
</div>
```

---

## Initial color assignment

Assign initials avatar colors consistently based on the user's name (not randomly per session) so the same user always appears with the same color. Use a hash function:

```javascript
const PALETTE = [
  '#FF7A35', // coral
  '#D4A5C9', // lavender
  '#A8C8E8', // sky
  '#FFB347', // orange
  '#2C3E6A', // navy-mid
  '#2E7D32', // green
];

function avatarColor(name) {
  let hash = 0;
  for (const ch of name) hash = (hash * 31 + ch.charCodeAt(0)) >>> 0;
  return PALETTE[hash % PALETTE.length];
}
```

---

## Accessibility

- All avatars must have an `alt` text or `aria-label` describing the person or entity they represent.
- Presence indicators must have an `aria-label` — they cannot rely on color alone.
- Group avatar overflow counts ("+2") must be included in the group's `aria-label`.
- Decorative avatars (where the name is already in adjacent text) can use `alt=""`.
