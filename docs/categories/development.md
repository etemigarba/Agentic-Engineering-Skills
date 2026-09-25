# Development Skills

## Overview

The Development stage (9 skills) implements the design into working software through progressive refinement: scaffold → standards → PoC → Prototype → MVP → Production-Ready → CI/CD → Exit Review. Debugging is available throughout.

## Skills

### 3.2 Project Creation & Structure (`/project-creation-and-structure`)

**Purpose**: Scaffold repository with standardised layout, tooling, conventions, CI/CD skeleton, and dev environment.

**Key Outputs**:
- Directory structure (src/, tests/, docs/, scripts/, configs/)
- Build configuration (package.json, pyproject.toml, etc.)
- Lint/format/type-check config
- Test configuration (unit, integration, E2E)
- CI/CD pipeline skeleton
- Pre-commit hooks
- Dev container / environment config
- CONTRIBUTING.md, CODEOWNERS, .gitignore

**Standards**: ISO/IEC/IEEE 12207, 25010, OWASP ASVS

---

### 3.3 Coding, Integration & Debugging Standard (`/coding-integration-and-debugging-standard`)

**Purpose**: Define and enforce coding standards, integration patterns, debugging workflows, code review checklists.

**Key Outputs**:
- Coding conventions (naming, formatting, organisation, patterns)
- Integration patterns (API client, event-driven, message queues)
- Error handling taxonomy (categories, wrapping, context, user messages)
- Logging standards (structured, levels, correlation IDs, PII handling)
- Debugging procedures (hypothesis-driven, reproducible, tooling)
- Code review checklist (security, performance, correctness, style)
- Refactoring guidelines
- Tooling enforcement (linters, formatters, type checkers, SAST)

**Standards**: ISO/IEC 25010, 12207, OWASP Top 10/ASVS

---

### 3.4.i Proof of Concept (`/proof-of-concept`)

**Purpose**: Rapid feasibility validation — UI wired to real contracts with provisional data.

**Key Outputs**:
- Functional UI screens for core journeys (wired to mock/real contracts)
- Real API contract definitions (OpenAPI/GraphQL)
- Provisional data through real persistence
- Basic authN/authZ stubs
- Key interaction flows demonstrated
- Technical feasibility report
- Go/No-Go for Prototype

**Principle**: Real contracts, provisional data, functional UI — not static mockups.

**Standards**: ISO/IEC 25010, 12207, OWASP ASVS

---

### 3.4.ii Prototype (`/prototype`)

**Purpose**: Functional vertical slice with real persistence, real contracts, seeded data. Exit test: transaction survives restart.

**Key Outputs**:
- Real, durable persistence (configured database)
- Schema migrations (version-controlled, repeatable)
- Domain logic implementation (workflows, algorithms, data structures)
- Data access layer (repositories, query objects)
- API implementation (contracts from Design)
- UI wired to real endpoints (core journey)
- Seed scripts (idempotent, realistic test data)
- Basic authN/authZ enforced server-side
- Security controls (validation, parameterised queries, error handling)
- Performance basics (indexes, pagination, no N+1)
- **Exit test evidence** (transaction → restart → retrieve)

**Principle**: Real persistence, real contracts, provisional data.

**Standards**: ISO/IEC 25010, 12207, 27001, OWASP Top 10/ASVS, IEEE 829

---

### 3.4.iii MVP Build (`/mvp-build`)

**Purpose**: Minimum Viable Product — working vertical slice with all core journeys, security, performance, tests, documentation.

**Key Outputs**:
- **Interface**: Functional screens, all states (loading, empty, success, error, validation)
- **Logic**: Real workflows, algorithms, data structures for core rules
- **Backend**: Real service contracts, durable persistence, versioned migrations
- **Data**: Provisional/seeded data through real persistence
- **Security**: AuthN/authZ, validation, parameterised access, secrets, password hashing, structured errors, security logging, abuse protection
- **Performance**: Indexed paths, paginated lists, no N+1, documented assumptions
- **Tests**: Unit (domain), Integration (contracts/persistence), E2E (golden path)
- **Documentation**: Setup, config, migration, seeding, run, test, limitations
- **Exit Test**: Golden path execution + restart + retrieve verification

**Principle**: Minimum viable = scope, never quality.

**Standards**: ISO/IEC 25010, 12207, 27001, IEEE 829/29119, OWASP Top 10/ASVS/API Top 10

---

### 3.4.iv Production-Ready Application (`/production-ready-application`)

**Purpose**: Full feature completion, hardening, observability, documentation, operational tooling.

**Key Outputs**:
- Complete feature set (all in-scope requirements)
- No provisional code (TODOs resolved or documented)
- Production data strategy (migration from seed)
- Full observability (logging, metrics, tracing, alerting, dashboards)
- Operational tooling (backup, restore, migration, scaling, feature flags)
- Security hardening (pentest findings, secrets rotated, compliance evidence)
- Performance validation (load test results meeting SLAs)
- Documentation (runbooks, API docs, architecture, onboarding)
- Rollback capability (verified procedures)
- Compliance evidence (ISO/IEC, OWASP, regulatory)

**Standards**: ISO/IEC 25010, 12207, 27001, IEEE 829/29119, OWASP ASVS Level 2/3

---

### 3.5 Continuous Integration (`/continuous-integration`)

**Purpose**: CI/CD pipeline with quality gates, automated testing, security scanning, deployment prep.

**Key Outputs**:
- Pre-commit hooks (lint, format, type-check, unit tests)
- PR pipeline (full test suite, SAST, SCA, secrets, build, container scan)
- Merge pipeline (integration, E2E, performance benchmarks, staging deploy)
- Quality gates (coverage, mutation testing, complexity, security)
- Artefact management (versioned builds, SBOM, signed images, provenance)
- Notifications and rollback automation
- Metrics (build time, test time, failure rate, MTTR)

**Standards**: ISO/IEC/IEEE 12207, 25010, OWASP ASVS, SLSA

---

### 3.6 Development Exit Review (`/development-exit-review`)

**Purpose**: Quantified exit gate validating completeness, testing, security, performance, documentation.

**Key Outputs**:
- Feature completeness (per requirements)
- Test coverage (unit ≥80%, integration ≥70%, E2E critical paths)
- Security gate (SAST/SCA/secrets clean, pentest passed)
- Performance gate (SLAs met, benchmarks recorded)
- Code quality gate (complexity, duplication, standards)
- Documentation completeness (API docs, runbooks, architecture)
- Operational readiness (observability, rollback, scaling)
- Go/No-Go with Technical Lead, Security, Operations sign-off

**Standards**: ISO/IEC/IEEE 12207, 25010, 27001, IEEE 829, OWASP ASVS

---

### 3.7 Debug (`/debug`)

**Purpose**: Systematic, hypothesis-driven debugging workflow for production and development issues.

**Key Outputs**:
- Problem statement (symptoms, impact, severity)
- Reproduction steps (minimal, reliable)
- Hypothesis list (prioritised)
- Investigation log (queries, traces, experiments)
- Root cause identification (with evidence)
- Fix implementation (minimal, targeted, tested)
- Verification (reproduction fails, regression tests pass)
- Prevention (test added, monitor/alert added, process change)
- Post-mortem (if production incident)

**Standards**: ISO/IEC 25010, 12207, 27001, IEEE 1044

---

## Stage Flow

```
Design Exit Review → Project Structure → Coding Standards
  → Proof of Concept → Prototype → MVP Build → Production-Ready
  → Continuous Integration → Development Exit Review
  → Deployment Stage Gate
(Debug available throughout)
```

## Exit Criteria

- All features implemented per requirements (traceability verified)
- Test coverage thresholds met
- Security gate passed (no critical/high findings)
- Performance SLAs met
- Code quality thresholds met
- Documentation complete
- Operational readiness verified
- Technical Lead, Security, Operations sign-off