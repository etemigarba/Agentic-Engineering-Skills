# Backend APIs, DAL & Database

**Invocation**: `/backend-apis-dal-database`
**Category**: Design
**Stage**: 2.4 — Backend APIs, Data Access Layer, and Database

## Purpose
Designs the backend contract surface: API specifications (REST/gRPC/graph), data access layer patterns, database schema, migration strategy, and data integrity rules. Technology-agnostic with explicit contract definitions, versioning strategy, and security controls.

## When to Use
- "API design"
- "database design"
- "data access layer"
- "DAL design"
- "schema design"
- "migration strategy"
- "backend contracts"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Design principles (from `/design-principles`)
- Logic/algorithms/data structures (from `/logic-algorithms-workflows-data-structures`)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)

## Outputs
- `project_documents/design/backend_apis_dal_database.md` — Backend specification with:
  - API contract catalogue (endpoints, methods, schemas, status codes, versioning)
  - Data Access Layer pattern (repository, unit of work, query objects)
  - Database schema (entities, relationships, constraints, indexes, partitioning)
  - Migration strategy (versioning, rollback, seeding, zero-downtime)
  - Transaction boundaries and isolation levels
  - Security controls (authN/authZ, rate limiting, input validation, encryption)
  - Observability hooks (tracing, metrics, logging)
  - Traceability to requirements and logic specs

## Standards Alignment
- **ISO/IEC 25010** — Functional suitability, security, reliability
- **ISO/IEC 27001** — Data protection, access control
- **IEEE 1016** — Interface and data design
- **OWASP API Security Top 10** — API security
- **OWASP ASVS** — Data access and storage verification

## Example Invocation
```
/backend-apis-dal-database
```

## Related Skills
- `/design-principles` — Prerequisite
- `/logic-algorithms-workflows-data-structures` — Prerequisite
- `/risk-analysis-and-threat-modelling` — Prerequisite (threat model)
- `/cross-cutting-architecture` — Coordinates on observability, config, errors
- `/coding-integration-and-debugging-standard` — Implements contracts
- `/containerisation` — Consumes for deployment contracts
- `/security-checks` — Verifies API security