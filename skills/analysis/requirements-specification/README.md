# Requirements Specification

**Invocation**: `/requirements-specification`
**Category**: Analysis
**Stage**: 1.5 — Requirements Specification

## Purpose
Produces an IEEE 29148-compliant requirements specification with full traceability, acceptance criteria, and quantified non-functional requirements. The authoritative source for all downstream design, development, and verification activities.

## When to Use
- "requirements specification"
- "requirements engineering"
- "functional requirements"
- "non-functional requirements"
- "acceptance criteria"
- "traceability matrix"

## Inputs
- Statement of the Problem (from `/statement-of-the-problem`)
- Proposal & Technical Blueprint (from `/proposal-and-technical-blueprint`)
- Stakeholder interviews and workshops
- Regulatory and compliance obligations

## Outputs
- `project_documents/analysis/requirements_specification.md` — Requirements spec with:
  - Functional requirements (use cases, user stories, business rules)
  - Non-functional requirements (ISO/IEC 25010 quantified: security, performance, reliability, maintainability, usability)
  - Interface requirements (APIs, UI, data, hardware)
  - Data requirements (entities, attributes, constraints, privacy)
  - Acceptance criteria per requirement (testable, measurable)
  - Traceability matrix (requirement ↔ source ↔ design ↔ test)
  - Prioritisation (MoSCoW, value/complexity)
  - Assumptions, dependencies, constraints register

## Standards Alignment
- **ISO/IEC/IEEE 29148** — Requirements engineering (primary)
- **ISO/IEC 25010** — Quality requirements model
- **ISO/IEC 27001** — Security requirements
- **IEEE 1016** — Design interface requirements
- **OWASP ASVS** — Security verification requirements

## Example Invocation
```
/requirements-specification
```

## Related Skills
- `/statement-of-the-problem` — Prerequisite
- `/proposal-and-technical-blueprint` — Prerequisite
- `/risk-analysis-and-threat-modelling` — Consumes security requirements
- `/design-principles` — Follows; design must satisfy requirements
- `/validation` — Validates requirements are met
- `/verification` — Verifies implementation meets requirements