# Production-Ready Application

**Invocation**: `/production-ready-application`
**Category**: Development
**Stage**: 3.4.iv — Production-Ready Application

## Purpose
Completes the full feature set to production readiness: all requirements implemented, hardened, observable, documented, and verified. Removes all provisional elements, completes edge cases, implements operational tooling, and achieves the quality bar for production deployment.

## When to Use
- "production ready"
- "production readiness"
- "feature complete"
- "release candidate"
- "hardening"

## Inputs
- MVP Build (from `/mvp-build`)
- All Design stage outputs
- Requirements specification (from `/requirements-specification`)
- Validation & Verification results (from `/validation`, `/verification`)

## Outputs
- Production-ready application with:
  - **Complete feature set**: All in-scope requirements implemented and tested
  - **No provisional code**: All TODOs resolved or documented as known limitations
  - **Production data**: Migration from seed to production data strategy
  - **Observability**: Full logging, metrics, tracing, alerting, dashboards
  - **Operational tooling**: Backup, restore, migration, scaling, feature flags
  - **Security hardening**: Penetration test findings addressed, secrets rotated, compliance evidence
  - **Performance validation**: Load test results meeting SLAs
  - **Documentation**: Runbooks, API docs, architecture docs, onboarding
  - **Rollback capability**: Verified rollback procedures
  - **Compliance evidence**: ISO/IEC, OWASP, regulatory artefacts

## Standards Alignment
- **ISO/IEC 25010** — All characteristics at production levels
- **ISO/IEC/IEEE 12207** — Transition to operations
- **ISO/IEC 27001** — Operational security
- **IEEE 829 / ISO/IEC/IEEE 29119** — Test completion
- **OWASP ASVS Level 2/3** — Verification

## Example Invocation
```
/production-ready-application
```

## Related Skills
- `/mvp-build` — Prerequisite
- `/continuous-integration` — Pipeline must be green
- `/validation` — Prerequisite (requirements met)
- `/verification` — Prerequisite (implementation correct)
- `/testing-and-quality-assurance` — Prerequisite (quality gates)
- `/alpha-testing` — Prerequisite (user acceptance)
- `/performance-checks` — Prerequisite (SLAs met)
- `/compliance-to-standards` — Prerequisite (evidence complete)
- `/containerisation` — Follows; packages for deployment
- `/deployment-infrastructure-and-configuration` — Follows; deploys