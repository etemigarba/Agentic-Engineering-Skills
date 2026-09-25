# Alpha Testing

**Invocation**: `/alpha-testing`
**Category**: Testing & QA
**Stage**: 5.1 — Alpha Testing

## Purpose
Conducts internal acceptance testing with real users in a controlled environment. Captures usability feedback, functional gaps, performance observations, and user satisfaction data before beta or production release.

## When to Use
- "alpha testing"
- "internal acceptance testing"
- "user acceptance testing"
- "usability testing"
- "internal beta"

## Inputs
- MVP or Production-Ready Application (from `/mvp-build` or `/production-ready-application`)
- Testing strategy (from `/testing-and-quality-assurance`)
- User personas and journey maps
- Internal test users (stakeholders, domain experts, team)

## Outputs
- `project_documents/testing/alpha_testing_report.md` — Alpha test report with:
  - Test participant demographics and selection rationale
  - Test scenarios and scripts (core journeys, edge cases)
  - Functional findings (defects, gaps, workarounds)
  - Usability metrics (task success, time, errors, SUS/NASA-TLX)
  - Performance observations (perceived latency, responsiveness)
  - User feedback (qualitative, feature requests, pain points)
  - Severity-classified defect list with reproduction steps
  - Release readiness assessment (go/no-go for beta/production)
  - Action items for remediation

## Standards Alignment
- **ISO/IEC/IEEE 29119** — Acceptance testing
- **ISO/IEC 25010** — Usability, quality in use
- **IEEE 829** — Test reporting

## Example Invocation
```
/alpha-testing
```

## Related Skills
- `/testing-and-quality-assurance` — Prerequisite
- `/mvp-build` — Prerequisite (what to test)
- `/production-ready-application` — Prerequisite (what to test)
- `/validation` — Consumes alpha results
- `/performance-checks` — Complements with measurements
- `/compliance-to-standards` — Consumes evidence