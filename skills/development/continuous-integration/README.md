# Continuous Integration

**Invocation**: `/continuous-integration`
**Category**: Development
**Stage**: 3.5 — Continuous Integration

## Purpose
Establishes and maintains the CI/CD pipeline with quality gates, automated testing, security scanning, and deployment preparation. Ensures every change is validated against the full quality bar before merge and provides fast feedback to developers.

## When to Use
- "CI/CD"
- "continuous integration"
- "pipeline"
- "quality gates"
- "automated testing"
- "build pipeline"

## Inputs
- Project structure (from `/project-creation-and-structure`)
- Coding standards (from `/coding-integration-and-debugging-standard`)
- All test suites (unit, integration, E2E, performance, security)
- Containerisation config (from `/containerisation`)

## Outputs
- CI/CD pipeline with:
  - **Pre-commit hooks**: Lint, format, type-check, unit tests
  - **PR pipeline**: Full test suite, security scan (SAST, SCA, secrets), build, container scan
  - **Merge pipeline**: Integration tests, E2E tests, performance benchmarks, deployment to staging
  - **Quality gates**: Coverage thresholds, mutation testing, complexity limits, security findings
  - **Artifact management**: Versioned builds, SBOM, signed images, provenance
  - **Notification**: Slack/email/Teams on failure, deployment status
  - **Rollback automation**: Failed deployment detection and rollback
  - **Metrics**: Build time, test time, failure rate, MTTR

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Integration process
- **ISO/IEC 25010** — Reliability, maintainability
- **OWASP ASVS** — Pipeline security
- **SLSA** — Supply chain levels

## Example Invocation
```
/continuous-integration
```

## Related Skills
- `/project-creation-and-structure` — Prerequisite
- `/coding-integration-and-debugging-standard` — Prerequisite
- `/containerisation` — Consumes pipeline
- `/mvp-build` — Validates via pipeline
- `/production-ready-application` — Prerequisite for production pipeline
- `/pushing-app-to-source-repo` — Coordinates on git workflow