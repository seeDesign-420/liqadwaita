# Liqadwaita Liquid Glass Window Expansion

## What This Is
This project aims to port the "Unified Window Layout" from the GNOME-macOS-Tahoe theme specifically into the core apps of the Liqadwaita GTK theme (Terminal, Image Viewer, Text Editor). We will replace Liqadwaita's default window presentation with a floating canvas encased in a contiguous frosted glass window surface, alongside implementing Mac-style window controls globally.

## Core Value
Achieve a contiguous, refractive Liquid Glass aesthetic for specific core GTK apps and global window controls without breaking the structural scaffolding of the Libadwaita underlying logic.

## Requirements

### Validated
- ✓ Libadwaita extension base functioning via `AdwStyleManager` and CSS providers.
- ✓ `scrolledwindow` and core widget baseline overrides are already in the source branch.
- ✓ Testing environment `adwaita-1-demo` is functioning via local build pipeline.

### Active
- [ ] Incorporate Mac-style window control CSS from GNOME-macOS-Tahoe into Liqadwaita globally.
- [ ] Identify and isolate the app-specific node classes for GNOME Console (Terminal), Loupe (Image Viewer), and Text Editor.
- [ ] Apply the unified window layout (transparent headerbar, refractive frosted window blur) to these targeted applications.
- [ ] Support correct floating canvas background colors inside the transparent window container.

### Out of Scope
- [ ] Porting of layout to applications beyond Terminal, Image Viewer, and Text Editor — Focus restricted to core targets to ensure stability.
- [ ] Complete replacement of Libadwaita structural components (e.g., completely rewriting `adw-wrap-layout`) — Structural CSS only, logic remains untouched.

## Context
- The codebase is a modified branch of Libadwaita relying on SCSS compilation (`ninja -C build`), utilizing the `AdwStyleManager` for its overrides.
- The user has already extracted the necessary design tokens for the unified window layout (e.g. `inset 0 1px 0 rgba(255, 255, 255, 0.15)`) and Mac-style window controls from the GNOME-macOS-Tahoe theme.
- Current GTK CSS parser errors exist from earlier experiments (e.g., `:not()` selectors) which might need addressing when compiling the SCSS during testing.

## Constraints
- **Framework Constraint**: Must abide by standard GTK/Libadwaita CSS conventions and DOM graph structure (e.g. standard widget classnames and hierarchy).
- **Design Constraint**: Visuals must mirror the 'Liquid Glass' extraction from MacTahoe precisely (including translucency and specific box-shadow refractive lighting).

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Restrict Glass layout to 3 specific core apps | Ensures we don't break complex, idiosyncratic layouts of unrelated core GNOME apps system-wide. | — Pending |
| Apply Mac Window controls globally | Creates a baseline unified aesthetic immediately visible even on apps not explicitly using the new glass canvas. | — Pending |

---
*Last updated: 2026-04-18 after initialization*

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state
