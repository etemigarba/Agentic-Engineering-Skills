# Prototype

**Invocation**: `/prototype`
**Category**: Development
**Stage**: 3.4.ii — Prototype

## Purpose
Delivers a functional vertical slice with real persistence, real contracts, and seeded data. Implements the core domain logic, data access, and at least one complete user journey end-to-end. The exit test: a transaction executes through interface → logic → backend, persists, survives restart, and is retrievable.

## When to Use
- "prototype"
- "vertical slice"
- "end-to-end prototype"
- "functional prototype"
- "working prototype"

## Inputs
- Proof of Concept (from `/proof-of-concept`)
- Logic/algorithms/data structures (from `/logic-algorithms-workflows-data-structures`)
- Backend APIs/DAL/Database (from `/backend-apis-dal-database`)
- Cross-cutting architecture (from `/cross-cutting-architecture`)

## Outputs
- Working prototype with:
  - Real, durable persistence (configured database)
  - Schema migrations (version-controlled, repeatable)
  - Domain logic implementation (workflows, algorithms, data structures)
  - Data access layer (repositories, query objects)
  - API implementation (contracts from Design)
  - UI wired to real endpoints (core journey)
  - Seed scripts (idempotent, realistic test data)
  - Basic authN/authZ enforced server-side
  - Security controls (input validation, parameterised queries, error handling)
  - Performance basics (indexes, pagination, no N+1)
  - Exit test evidence (transaction → restart → retrieve)

## Standards Alignment
- **ISO/IEC 25010** — Functional suitability, reliability, performance efficiency, security
- **ISO/IEC/IEEE 12207** — Implementation
- **ISO/IEC 27001** — Security controls in prototype
- **OWASP Top 10 / ASVS** — Prototype-level security
- **IEEE 829** — Test documentation

## Key Principle
> Real persistence, real contracts, provisional data.

## Exit Test
At least one complete end-to-end transaction executes successfully through interface, logic, and backend layers, and its result is durably recorded — it survives a restart of the system and can be retrieved afterwards.

## Example Invocation
```
/prototype
```

## Related Skills
- `/proof-of-concept` — Prerequisite
- `/mvp-build` — Follows; expands scope
- `/production-ready-application` — Follows; completes features
- `/continuous-integration` — Validates prototype