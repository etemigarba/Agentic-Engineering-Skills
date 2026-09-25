# Validation

**Invocation**: `/validation`
**Category**: Validation & Verification
**Stage**: 4.1 — Validation

## Purpose
Answers "Are we building the right thing?" Validates that the implemented system satisfies the stakeholder needs and requirements as documented in the Requirements Specification. Includes stakeholder reviews, acceptance testing, usability validation, and requirements traceability verification.

## When to Use
- "validation"
- "acceptance testing"
- "stakeholder validation"
- "requirements validation"
- "user acceptance"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Production-ready application (from `/production-ready-application`)
- Alpha testing results (from `/alpha-testing`)
- Stakeholder availability

## Outputs
- `project_documents/validation/validation_report.md` — Validation report with:
  - Requirements satisfaction matrix (requirement → test → result)
  - Stakeholder acceptance records (sign-offs per requirement group)
  - Usability validation results (task success rates, SUS scores, feedback)
  - Business process validation (end-to-end scenarios with real users)
  - Regulatory/compliance validation (evidence mapped to obligations)
  - Gap analysis (unmet requirements, deviations, waivers)
  - Validation summary and release recommendation

## Standards Alignment
- **ISO/IEC/IEEE 29148** — Validation process
- **ISO/IEC 25010** — Quality in use (validation perspective)
- **IEEE 829 / ISO/IEC/IEEE 29119** — Acceptance testing
- **ISO/IEC 27001** — Control validation

## Example Invocation
```
/validation
```

## Related Skills
- `/requirements-specification` — Prerequisite (what to validate)
- `/production-ready-application` — Prerequisite (what to validate against)
- `/alpha-testing` — Prerequisite (user feedback)
- `/verification` — Complementary (builds right vs builds right thing)
- `/compliance-to-standards` — Provides compliance evidence