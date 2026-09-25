# Verification

**Invocation**: `/verification`
**Category**: Validation & Verification
**Stage**: 4.2 — Verification

## Purpose
Answers "Are we building it right?" Verifies that the implementation conforms to the design specifications, coding standards, and quality requirements. Includes code inspection, static analysis, test coverage verification, architecture conformance, and security verification.

## When to Use
- "verification"
- "code inspection"
- "static analysis"
- "architecture conformance"
- "design verification"
- "implementation verification"

## Inputs
- All Design stage outputs (2.1 through 2.6)
- Coding standards (from `/coding-integration-and-debugging-standard`)
- Production-ready application (from `/production-ready-application`)
- CI/CD pipeline results (from `/continuous-integration`)

## Outputs
- `project_documents/verification/verification_report.md` — Verification report with:
  - Design conformance matrix (design element → implementation → status)
  - Code inspection findings (peer review, checklist compliance)
  - Static analysis results (SAST, complexity, duplication, dependencies)
  - Test coverage verification (statement, branch, path, mutation)
  - Architecture conformance (layering, dependencies, patterns)
  - Security verification (OWASP ASVS mapping, penetration test)
  - Performance verification (benchmarks vs budgets)
  - Non-functional requirement verification (ISO/IEC 25010 metrics)
  - Traceability verification (requirement → design → code → test)
  - Verification summary and release recommendation

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Verification process
- **ISO/IEC/IEEE 29148** — Verification requirements
- **IEEE 1016** — Design conformance
- **IEEE 829 / ISO/IEC/IEEE 29119** — Verification testing
- **OWASP ASVS** — Security verification (primary)
- **ISO/IEC 25010** — Quality characteristic verification

## Example Invocation
```
/verification
```

## Related Skills
- `/design-documentation-and-review` — Prerequisite (what to verify)
- `/coding-integration-and-debugging-standard` — Prerequisite (standards)
- `/production-ready-application` — Prerequisite (what to verify)
- `/continuous-integration` — Provides automated verification data
- `/validation` — Complementary (right thing vs thing right)
- `/security-checks` — Provides security verification data
- `/performance-checks` — Provides performance verification data
- `/compliance-to-standards` — Consumes verification evidence