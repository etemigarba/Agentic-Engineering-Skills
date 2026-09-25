# Phase-Gate Design Exit Review

**Invocation**: `/phase-gate-design-exit-review`
**Category**: Design
**Stage**: 2.7 — Phase-Gate Design Exit Review

## Purpose
Executes the quantified exit gate for the Design stage. Validates that all design artefacts are complete, traceable, reviewed, and meet the numerical thresholds defined in the Design Principles. Produces a go/no-go decision for the Development stage with a formal sign-off record.

## When to Use
- "design exit review"
- "design gate"
- "phase gate"
- "design sign-off"
- "stage gate review"

## Inputs
- All Design stage outputs (2.1 through 2.6)
- Requirements specification (from `/requirements-specification`)
- Design Principles exit criteria (from `/design-principles`)

## Outputs
- `project_documents/design/phase_gate_design_exit_review.md` — Exit review record with:
  - Completeness checklist (all design artefacts present)
  - Traceability verification (100% requirements → design, design → test)
  - Threshold compliance (coupling, cohesion, complexity, security, performance)
  - Review evidence (reviewers, findings, resolutions)
  - Risk acceptance register (residual risks with owners)
  - Go/No-Go decision with rationale
  - Sign-off by Design Authority and stakeholders
  - Conditions for Development stage entry

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Stage gate process
- **ISO/IEC/IEEE 29148** — Requirements satisfaction
- **ISO/IEC 25010** — Quality thresholds
- **IEEE 1016** — Design completeness
- **ISO/IEC 27001** — Security design verification

## Example Invocation
```
/phase-gate-design-exit-review
```

## Related Skills
- `/design-documentation-and-review` — Prerequisite
- `/design-principles` — Provides exit criteria thresholds
- All Design skills (2.1–2.5) — Validated by this gate
- `/project-creation-and-structure` — Follows if gate passes