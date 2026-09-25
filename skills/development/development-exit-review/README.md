# Development Exit Review

**Invocation**: `/development-exit-review`
**Category**: Development
**Stage**: 3.6 — Development Exit Review

## Purpose
Executes the quantified exit gate for the Development stage. Validates that all code is complete, tested, reviewed, secure, performant, and documented. Produces a go/no-go decision for the Deployment stage with a formal sign-off record.

## When to Use
- "development exit review"
- "development gate"
- "code complete"
- "stage gate"

## Inputs
- All Development stage outputs (3.2 through 3.5)
- MVP or Production-Ready Application (from `/mvp-build` or `/production-ready-application`)
- CI/CD pipeline results (from `/continuous-integration`)
- Testing & QA results (from `/testing-and-quality-assurance`)

## Outputs
- `project_documents/development/development_exit_review.md` — Exit review record with:
  - Completeness checklist (all features implemented per requirements)
  - Test coverage verification (unit ≥80%, integration ≥70%, E2E critical paths)
  - Security gate (SAST/SCA/Secrets clean, penetration test passed)
  - Performance gate (SLAs met, benchmarks recorded)
  - Code quality gate (complexity, duplication, standards adherence)
  - Documentation completeness (API docs, runbooks, architecture)
  - Operational readiness (observability, rollback, scaling verified)
  - Review evidence (reviewers, findings, resolutions)
  - Go/No-Go decision with rationale
  - Sign-off by Technical Lead, Security, Operations
  - Conditions for Deployment stage entry

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Stage gate process
- **ISO/IEC 25010** — Quality thresholds
- **ISO/IEC 27001** — Security verification
- **IEEE 829** — Test completion criteria
- **OWASP ASVS** — Verification completion

## Example Invocation
```
/development-exit-review
```

## Related Skills
- `/continuous-integration` — Prerequisite (pipeline green)
- `/testing-and-quality-assurance` — Prerequisite
- `/security-checks` — Prerequisite
- `/performance-checks` — Prerequisite
- `/compliance-to-standards` — Prerequisite
- `/containerisation` — Follows if gate passes
- `/deployment-infrastructure-and-configuration` — Follows