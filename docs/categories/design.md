# Design Skills

## Overview

The Design stage (7 skills) transforms analysed requirements into detailed, reviewable design specifications with quantified quality thresholds. Each skill produces a markdown artefact in `project_documents/design/`.

## Skills

### 2.1 Design Principles (`/design-principles`)

**Purpose**: Authoritative reference for design governance: SoC, SOLID, DRY/KISS/YAGNI, Coupling/Cohesion (measured), Cloud-Native Tenets. Each with formal apparatus, thresholds, failure catalogues, and standard mappings.

**Key Outputs**:
- Economic justification (defect cost escalation, maintenance share)
- 5 principle families × 8-part structure (definition, rationale, equations, techniques, tools, thresholds, failures, mappings)
- Constraints register (negotiable principles vs binding constraints)
- 5 Six-Protocol prompt boxes (one per family)
- Quantified Design exit gate criteria table

**Standards**: ISO/IEC 25010, 12207, 29148, IEEE 1016, 27001/27002, OWASP Top 10/ASVS

---

### 2.2 Presentation Layer — UI/UX Wireframes (`/presentation-layer-ui-ux-wireframes`)

**Purpose**: Comprehensive wireframes, interaction flows, component specs, design tokens, and accessibility requirements.

**Key Outputs**:
- Screen inventory and navigation map
- Wireframes for all user-facing screens
- Interaction flows and state transitions
- Component specifications (anatomy, states, variants, props)
- Design tokens (color, typography, spacing, elevation, motion)
- Accessibility requirements (WCAG 2.2 AA minimum)
- Responsive breakpoints and layout rules
- Usability criteria and test scenarios

**Standards**: ISO/IEC 25010 (usability), 29148, IEEE 1016, WCAG 2.2, OWASP ASVS

---

### 2.3 Logic, Algorithms, Workflows & Data Structures (`/logic-algorithms-workflows-data-structures`)

**Purpose**: Algorithm selection with complexity analysis, workflow orchestration, data structure design with formal bounds and invariants.

**Key Outputs**:
- Algorithm catalogue (complexity, invariants, edge cases)
- Workflow definitions (states, transitions, guards, compensation)
- Data structure specs (ADTs, invariants, operations, persistence mapping)
- Concurrency and synchronisation strategy
- Error handling and retry policies
- Performance budgets per operation

**Standards**: ISO/IEC 25010 (performance, reliability), 12207, IEEE 1016, OWASP ASVS

---

### 2.4 Backend APIs, DAL & Database (`/backend-apis-dal-database`)

**Purpose**: API contracts, data access layer patterns, database schema, migration strategy, security controls.

**Key Outputs**:
- API contract catalogue (endpoints, schemas, versioning)
- DAL pattern (repository, unit of work, query objects)
- Database schema (entities, relationships, constraints, indexes)
- Migration strategy (versioning, rollback, seeding, zero-downtime)
- Transaction boundaries and isolation levels
- Security controls (authN/authZ, rate limiting, encryption)
- Observability hooks

**Standards**: ISO/IEC 25010, 27001, IEEE 1016, OWASP API Top 10, ASVS

---

### 2.5 Cross-Cutting Architecture (`/cross-cutting-architecture`)

**Purpose**: Observability, configuration, error handling, transactions, security enforcement, caching, feature flags.

**Key Outputs**:
- Observability framework (logging, metrics, tracing)
- Configuration management (externalised, secrets, feature flags)
- Error handling taxonomy (categories, codes, retry, circuit breaker)
- Transaction management (boundaries, saga patterns)
- Security enforcement (authN/authZ framework, policy engine)
- Caching strategy (levels, invalidation, consistency)
- Feature flag framework (lifecycle, targeting, rollout)
- Enforcement mechanisms (linters, gates, runtime guards)

**Standards**: ISO/IEC 25010, 27001, OWASP ASVS, IEEE 1016

---

### 2.6 Design Documentation & Review (`/design-documentation-and-review`)

**Purpose**: Complete design documentation package: ADRs, detailed specs, review checklists, traceability matrices.

**Key Outputs**:
- ADR catalogue (decision, context, alternatives, consequences)
- Detailed design specifications per component
- Review checklists (security, performance, maintainability, testability)
- Requirements-to-design traceability matrix
- Design-to-test traceability matrix
- Open issues and decisions log
- Review sign-off records

**Standards**: ISO/IEC/IEEE 12207, 29148, IEEE 1016, 25010

---

### 2.7 Phase-Gate Design Exit Review (`/phase-gate-design-exit-review`)

**Purpose**: Quantified exit gate validating completeness, traceability, threshold compliance, and review evidence.

**Key Outputs**:
- Completeness checklist (all design artefacts)
- Traceability verification (100% req→design, design→test)
- Threshold compliance (coupling, cohesion, complexity, security, performance)
- Review evidence (reviewers, findings, resolutions)
- Risk acceptance register
- Go/No-Go decision with rationale
- Sign-off by Design Authority and stakeholders

**Standards**: ISO/IEC/IEEE 12207, 29148, 25010, IEEE 1016, 27001

---

## Stage Flow

```
Requirements → Design Principles → [Parallel: UI/UX, Logic, Backend, Cross-Cutting]
  → Design Documentation & Review → Design Exit Review
  → Development Stage Gate
```

## Exit Criteria

- All 7 design artefacts complete and reviewed
- 100% requirements traced to design elements
- 100% design elements traced to test cases
- All quantified thresholds met (coupling < X, cohesion > Y, complexity < Z)
- Security design verified against threat model
- Performance budgets allocated and documented
- ADRs recorded for all significant decisions
- Design Authority and stakeholder sign-off obtained