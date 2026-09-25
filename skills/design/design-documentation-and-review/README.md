# Design Documentation & Review

**Invocation**: `/design-documentation-and-review`
**Category**: Design
**Stage**: 2.6 — Design Documentation and Review

## Purpose
Produces the complete design documentation package: Architecture Decision Records (ADRs), detailed design specifications, review checklists, and traceability matrices. Ensures every requirement traces to at least one design element and every design decision is recorded with rationale.

## When to Use
- "design documentation"
- "ADR"
- "architecture decision record"
- "design review"
- "design specification"
- "traceability matrix"
- "design sign-off"

## Inputs
- All Design stage outputs (2.1 through 2.5)
- Requirements specification (from `/requirements-specification`)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)

## Outputs
- `project_documents/design/design_documentation_and_review.md` — Documentation package with:
  - ADR catalogue (decision, context, alternatives, consequences, status)
  - Detailed design specifications per component
  - Review checklists (security, performance, maintainability, testability)
  - Requirements-to-design traceability matrix
  - Design-to-test traceability matrix
  - Open issues and decisions log
  - Review sign-off records

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Design documentation
- **ISO/IEC/IEEE 29148** — Traceability
- **IEEE 1016** — Design description documentation
- **ISO/IEC 25010** — Quality characteristics verification

## Example Invocation
```
/design-documentation-and-review
```

## Related Skills
- `/design-principles` through `/cross-cutting-architecture` — Prerequisites
- `/phase-gate-design-exit-review` — Validates completeness
- `/validation` — Validates design meets requirements
- `/coding-integration-and-debugging-standard` — Guides implementation