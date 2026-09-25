# MVP Build

**Invocation**: `/mvp-build`
**Category**: Development
**Stage**: 3.4.iii — MVP Build

## Purpose
Builds the Minimum Viable Product: a genuinely working vertical slice of the product with functional interface, real domain logic, real backend contracts, and real durable persistence (provisional data acceptable). The golden path transaction must execute end-to-end, persist, survive restart, and be retrievable.

## When to Use
- "MVP"
- "minimum viable product"
- "MVP build"
- "product slice"
- "golden path"

## Inputs
- Prototype (from `/prototype`)
- All Design stage outputs
- Requirements specification (from `/requirements-specification`)
- Coding standards (from `/coding-integration-and-debugging-standard`)

## Outputs
- Production-grade MVP with:
  - **Interface**: Functional screens/endpoints for core journeys, all states (loading, empty, success, error, validation)
  - **Logic**: Real workflows, algorithms, data structures implementing core business rules
  - **Backend**: Real service contracts, durable persistence, versioned migrations
  - **Data**: Provisional/seeded data through real persistence layer
  - **Security**: AuthN/authZ, input validation, parameterised access, secure secrets, password hashing, structured errors, security logging, abuse protection
  - **Performance**: Indexed access paths, paginated lists, no N+1, documented assumptions
  - **Tests**: Unit (domain), integration (contracts/persistence), E2E (golden path)
  - **Documentation**: Setup, config, migration, seeding, run, test, known limitations
  - **Exit Test Evidence**: Golden path execution + restart + retrieve verification

## Standards Alignment
- **ISO/IEC 25010** — All quality characteristics
- **ISO/IEC/IEEE 12207** — Implementation
- **ISO/IEC 27001** — Security controls
- **IEEE 829 / ISO/IEC/IEEE 29119** — Testing
- **OWASP Top 10 / ASVS / API Security Top 10** — Application security

## Key Principle
> **Real persistence, real contracts, provisional data.** Minimum viable = scope, never quality.

## Exit Test
At least one complete end-to-end transaction (the "golden path") executes successfully through interface, logic, and backend, persists, survives restart, and is retrievable.

## Example Invocation
```
/mvp-build
```

## Related Skills
- `/prototype` — Prerequisite
- `/production-ready-application` — Follows; completes full feature set
- `/continuous-integration` — Validates MVP
- `/development-exit-review` — Validates stage completion