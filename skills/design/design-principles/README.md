# Design Principles

**Invocation**: `/design-principles`
**Category**: Design
**Stage**: 2.1 — Design Principles and Constraints

## Purpose
Authors the authoritative reference chapter for design governance: Separation of Concerns, SOLID, DRY/KISS/YAGNI, Coupling/Cohesion (measured), and Cloud-Native Tenets. Each principle includes formal apparatus (equations, metrics, thresholds), techniques, tool categories, failure catalogue, and standard mappings. Includes Six-Protocol prompt boxes for each principle family and quantified Design exit gate criteria.

## When to Use
- "design principles"
- "design governance"
- "SOLID principles"
- "coupling cohesion"
- "separation of concerns"
- "design standards"
- "architecture principles"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)
- Running case study from `project_documents/`

## Outputs
- `project_documents/design/design_principles_and_constraints.md` — Reference chapter with:
  - Economic justification (defect cost escalation, maintenance share)
  - Five principle families (each: definition, rationale, formal apparatus, techniques, tools, quantified threshold, failure catalogue, standard mapping)
  - Constraints register (principles vs binding constraints with approvers)
  - Five Six-Protocol prompt boxes (one per family)
  - Quantified Design exit gate criteria table
  - Consolidated references

## Standards Alignment
- **ISO/IEC 25010** — Product quality (maintainability, reliability, security)
- **ISO/IEC/IEEE 12207** — Design process
- **ISO/IEC/IEEE 29148** — Requirements-to-design traceability
- **IEEE 1016** — Design description
- **ISO/IEC 27001/27002** — Security by design
- **OWASP Top 10 / ASVS** — Secure design principles

## Key Requirements
- Technology-agnostic (no vendor, language, framework names)
- Every quantitative claim sourced; unsourced claims omitted
- Metrics with measurement methods and tolerance bands
- British orthography, academic/technical register
- Roman numeral enumeration, full-stop terminated entries

## Example Invocation
```
/design-principles
```

## Related Skills
- `/requirements-specification` — Prerequisite
- `/risk-analysis-and-threat-modelling` — Prerequisite
- All subsequent Design skills — Consume these principles
- `/design-documentation-and-review` — Documents adherence
- `/phase-gate-design-exit-review` — Validates against exit criteria