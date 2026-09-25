# Presentation Layer (UI/UX Wireframes)

**Invocation**: `/presentation-layer-ui-ux-wireframes`
**Category**: Design
**Stage**: 2.2 — Presentation Layer: UI/UX Wireframes

## Purpose
Produces comprehensive wireframes, interaction flows, component specifications, and accessibility requirements for the presentation layer. Defines screen layouts, navigation patterns, state transitions, component library, design tokens, and usability criteria — all technology-agnostic.

## When to Use
- "UI wireframes"
- "UX wireframes"
- "user interface design"
- "wireframes"
- "screen design"
- "interaction flows"
- "component library"
- "design tokens"
- "accessibility requirements"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Design principles (from `/design-principles`)
- User research, personas, journey maps (if available)
- Brand guidelines (if available)

## Outputs
- `project_documents/design/presentation_layer_ui_ux_wireframes.md` — Wireframe specification with:
  - Screen inventory and navigation map
  - Wireframes (low/medium fidelity) for all user-facing screens
  - Interaction flows and state transitions
  - Component specifications (anatomy, states, variants, props)
  - Design tokens (color, typography, spacing, elevation, motion)
  - Accessibility requirements (WCAG 2.2 AA minimum)
  - Responsive breakpoints and layout rules
  - Usability criteria and test scenarios
  - Traceability to requirements

## Standards Alignment
- **ISO/IEC 25010** — Usability, accessibility
- **ISO/IEC/IEEE 29148** — UI requirements
- **IEEE 1016** — Interface design description
- **WCAG 2.2** — Accessibility (AA minimum)
- **OWASP ASVS** — Client-side security requirements

## Example Invocation
```
/presentation-layer-ui-ux-wireframes
```

## Related Skills
- `/design-principles` — Prerequisite
- `/logic-algorithms-workflows-data-structures` — Coordinates on data display needs
- `/backend-apis-dal-database` — Coordinates on API contracts for UI
- `/design-documentation-and-review` — Documents decisions
- `/phase-gate-design-exit-review` — Validates completeness