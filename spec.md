# Adwaita Liquid — spec.md

## 1. Overview

Adwaita Liquid is a fork of libadwaita that redefines the GNOME UI layer with a new visual language inspired by:

- macOS Tahoe (layout, spacing, hierarchy)
- Liquid Glass aesthetic (depth, translucency, softness)
- Pill-based geometry system (no sharp rectangles)

The goal is to:
- Replace GNOME’s rigid HIG styling with a fluid, modern, tactile UI system
- Maintain libadwaita strengths (adaptive layouts, GTK4 compatibility)
- Eliminate inconsistencies found in third-party themes

---

## 2. Core Philosophy

### 2.1 Shape Language (GLOBAL RULE)

No rectangles. Anywhere.

All UI elements must be:
- Circles
- Pill shapes (capsules)
- Soft organic surfaces

Applies to:
Buttons, inputs, cards, windows, menus, toolbars, popovers, sliders, scrollbars

---

### 2.2 Visual Identity — Liquid Glass

- Translucent backgrounds
- Frosted blur layers
- Soft highlights and gradients
- Subtle reflections

---

### 2.3 Interaction Model

- Smooth transitions
- Hover = light bloom
- Active = soft press
- Focus = glow (no outlines)

---

## 3. Design System Layers

### 3.1 Base Layer

Override libadwaita defaults:
- Stylesheets
- Spacing inconsistencies
- Widget visuals

---

### 3.2 Component Layer

Buttons:
- Pill-shaped
- Glass styling

Toolbars:
- Floating glass bars

Inputs:
- Rounded with inner glow

Lists:
- Floating rows with spacing

---

### 3.3 Layout System

- More whitespace
- Hierarchy via spacing
- macOS Tahoe-inspired structure

---

## 4. Theme Integration Strategy

Merge:

Theme 1:
- Strong buttons, windows

Theme 2:
- Better layout, terminal UI

Shell:
- Rebuild completely

---

## 5. GNOME Shell

Out of scope for reuse — rebuild required:
- Top bar
- Overview
- Dock
- Notifications

---

## 6. Technical Architecture

- Fork libadwaita
- Replace stylesheet pipeline
- Keep GTK compatibility

---

## 7. Known Issues

- Inconsistent spacing
- Rigid HIG rules
- Flat visuals

---

## 8. Goals

Short-term:
- Remove rectangles
- Merge themes

Mid-term:
- Full Liquid Glass system

Long-term:
- Independent design system

---

## 9. Non-Goals

- GNOME HIG compliance
- GTK3 support
- Traditional theming

---

## 10. Future

- Animations
- Blur optimization
- Dynamic colors
