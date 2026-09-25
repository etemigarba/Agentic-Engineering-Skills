# Testing & Quality Assurance

**Invocation**: `/testing-and-quality-assurance`
**Category**: Testing & QA
**Stage**: 5.0 — Testing and Quality Assurance

## Purpose
Defines and executes the comprehensive test strategy: test pyramid, test data management, quality gates, defect lifecycle, and release criteria. Ensures testing is systematic, measurable, and aligned to risk.

## When to Use
- "test strategy"
- "quality assurance"
- "test planning"
- "test pyramid"
- "quality gates"
- "defect management"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)
- All Development stage outputs

## Outputs
- `project_documents/testing/testing_and_quality_assurance.md` — Test strategy with:
  - Test pyramid definition (unit, integration, contract, E2E, performance, security)
  - Test data strategy (generation, masking, privacy, environments)
  - Quality gates per pipeline stage (entry/exit criteria, thresholds)
  - Defect lifecycle (classification, prioritisation, SLA, root cause)
  - Release criteria (coverage, critical defects, performance, security)
  - Test environment strategy (provisioning, isolation, teardown)
  - Automation strategy (what, when, how, maintenance)
  - Metrics and reporting (dashboards, trends, retrospectives)

## Standards Alignment
- **ISO/IEC/IEEE 29119** — Software testing (primary)
- **IEEE 829** — Test documentation
- **ISO/IEC 25010** — Quality characteristics testing
- **ISO/IEC 27001** — Security testing
- **OWASP ASVS** — Security test requirements

## Example Invocation
```
/testing-and-quality-assurance
```

## Related Skills
- `/risk-analysis-and-threat-modelling` — Prerequisite (risk-based testing)
- `/alpha-testing` — Follows; user acceptance
- `/performance-checks` — Follows; non-functional
- `/security-checks` — Follows; security testing
- `/compliance-to-standards` — Consumes test evidence
- `/validation` — Consumes test results
- `/verification` — Consumes test results