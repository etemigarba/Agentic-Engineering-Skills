# Proof of Concept

**Invocation**: `/proof-of-concept`
**Category**: Development
**Stage**: 3.4.i — Proof of Concept (UI Wireframes)

## Purpose
Builds a rapid feasibility validation focusing on the presentation layer wired to real contracts with provisional data. Validates that the UI/UX design is implementable, the API contracts are sound, and the core user journeys are achievable — before committing to full backend implementation.

## When to Use
- "proof of concept"
- "PoC"
- "feasibility validation"
- "UI validation"
- "contract validation"
- "rapid prototype"

## Inputs
- Presentation layer wireframes (from `/presentation-layer-ui-ux-wireframes`)
- Backend API contracts (from `/backend-apis-dal-database`)
- Coding standards (from `/coding-integration-and-debugging-standard`)

## Outputs
- Working proof-of-concept with:
  - Functional UI screens for core user journeys (wired to mock/real contracts)
  - Real API contract definitions (OpenAPI/GraphQL schema)
  - Provisional data loaded through real persistence layer
  - Basic authentication and authorisation stubs
  - Key interaction flows demonstrated
  - Technical feasibility report (risks, unknowns, decisions needed)
  - Go/No-Go for Prototype stage

## Standards Alignment
- **ISO/IEC 25010** — Functional suitability, usability
- **ISO/IEC/IEEE 12207** — Prototyping process
- **OWASP ASVS** — Early security validation

## Key Principle
> Real contracts, provisional data, functional UI — not static mockups.

## Example Invocation
```
/proof-of-concept
```

## Related Skills
- `/presentation-layer-ui-ux-wireframes` — Prerequisite
- `/backend-apis-dal-database` — Prerequisite
- `/coding-integration-and-debugging-standard` — Prerequisite
- `/prototype` — Follows; builds on PoC
- `/mvp-build` — Follows; full implementation