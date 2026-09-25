# Validation & Verification Skills

## Overview

The Validation & Verification stage (2 skills) provides independent assurance: Validation answers "Are we building the right thing?" (stakeholder needs), Verification answers "Are we building it right?" (design conformance).

## Skills

### 4.1 Validation (`/validation`)

**Purpose**: Validate that the implemented system satisfies stakeholder needs and requirements.

**Key Outputs**:
- Requirements satisfaction matrix (requirement → test → result)
- Stakeholder acceptance records (sign-offs per requirement group)
- Usability validation results (task success rates, SUS scores, feedback)
- Business process validation (end-to-end scenarios with real users)
- Regulatory/compliance validation (evidence mapped to obligations)
- Gap analysis (unmet requirements, deviations, waivers)
- Validation summary and release recommendation

**Standards**: ISO/IEC/IEEE 29148, 25010, IEEE 829/29119, ISO/IEC 27001

---

### 4.2 Verification (`/verification`)

**Purpose**: Verify that the implementation conforms to design specifications, coding standards, and quality requirements.

**Key Outputs**:
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

**Standards**: ISO/IEC/IEEE 12207, 29148, IEEE 1016, 829/29119, OWASP ASVS, 25010

---

## Stage Flow

```
Development Exit Review → Validation (right thing?) + Verification (right way?)
  → Testing & QA Stage
```

## Relationship

| Aspect | Validation | Verification |
|--------|------------|--------------|
| Question | "Right thing?" | "Right way?" |
| Focus | Stakeholder needs | Design specifications |
| Methods | Acceptance testing, usability, stakeholder review | Inspection, static analysis, test coverage, conformance |
| Standards | ISO/IEC/IEEE 29148 | IEEE 1016, ISO/IEC/IEEE 29148 |
| Output | Validation report | Verification report |

## Exit Criteria

- Validation: All requirements have stakeholder acceptance; usability targets met; regulatory obligations satisfied
- Verification: 100% design elements implemented and verified; static analysis clean; coverage thresholds met; architecture conformance confirmed; security verification complete

Both reports required for Testing & QA stage entry.