# Cross-Cutting Architecture

**Invocation**: `/cross-cutting-architecture`
**Category**: Design
**Stage**: 2.5 — Cross-Cutting Architecture

## Purpose
Defines the cross-cutting concerns that span all layers: observability (logging, metrics, tracing), configuration management, error handling, transaction management, security enforcement, caching, and feature flags. Provides technology-agnostic patterns and enforcement mechanisms.

## When to Use
- "cross-cutting concerns"
- "observability design"
- "configuration management"
- "error handling strategy"
- "transaction management"
- "feature flags"
- "caching strategy"
- "security enforcement"

## Inputs
- Design principles (from `/design-principles`)
- All other Design stage outputs (presentation, logic, backend)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)
- Non-functional requirements

## Outputs
- `project_documents/design/cross_cutting_architecture.md` — Cross-cutting specification with:
  - Observability framework (structured logging, metrics taxonomy, distributed tracing)
  - Configuration management (externalised config, secrets, feature flags, environments)
  - Error handling taxonomy (categories, codes, retry, circuit breaker, fallback)
  - Transaction management (boundaries, propagation, compensation, saga patterns)
  - Security enforcement (authN/authZ framework, policy engine, audit)
  - Caching strategy (levels, invalidation, consistency models)
  - Feature flag framework (lifecycle, targeting, rollout)
  - Enforcement mechanisms (linters, gates, runtime guards)

## Standards Alignment
- **ISO/IEC 25010** — Reliability, maintainability, security
- **ISO/IEC 27001** — Security controls across layers
- **OWASP ASVS** — Architecture verification
- **IEEE 1016** — Architectural design description

## Example Invocation
```
/cross-cutting-architecture
```

## Related Skills
- `/design-principles` — Prerequisite
- `/presentation-layer-ui-ux-wireframes` — Consumes error handling, config
- `/logic-algorithms-workflows-data-structures` — Consumes transactions, caching
- `/backend-apis-dal-database` — Consumes observability, security
- `/coding-integration-and-debugging-standard` — Implements patterns
- `/continuous-integration` — Enforces via gates