# Compliance to Standards

**Invocation**: `/compliance-to-standards`
**Category**: Testing & QA
**Stage**: 5.6 — Compliance to Standards

## Purpose
Produces the compliance evidence pack demonstrating adherence to ISO/IEC, IEEE, OWASP, and regulatory standards. Maps requirements, design, implementation, testing, and verification artefacts to specific standard clauses. Generates audit-ready documentation.

## When to Use
- "compliance"
- "ISO 27001 compliance"
- "OWASP compliance"
- "audit evidence"
- "regulatory compliance"
- "standards mapping"
- "evidence pack"

## Inputs
- All Analysis, Design, Development, Validation & Verification outputs
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)
- Validation report (from `/validation`)
- Verification report (from `/verification`)
- Testing reports (from `/testing-and-quality-assurance`, `/alpha-testing`, `/performance-checks`)
- Security checks (from `/security-checks`)

## Outputs
- `project_documents/testing/compliance_to_standards.md` — Compliance evidence pack with:
  - Standards applicability matrix (which clauses apply, why)
  - Evidence mapping (clause → artefact → location → status)
  - Gap analysis (unmet clauses, compensating controls, remediation plan)
  - Audit trail (who, when, what, how for each evidence item)
  - Control implementation statements (ISO/IEC 27001 Annex A, OWASP ASVS)
  - Residual risk register (accepted risks with owner approval)
  - Certification readiness assessment (internal audit results)
  - Continuous compliance monitoring plan

## Standards Alignment
- **ISO/IEC 27001/27002** — ISMS compliance (primary)
- **ISO/IEC 25010** — Quality model compliance
- **ISO/IEC/IEEE 12207** — Lifecycle process compliance
- **ISO/IEC/IEEE 29148** — Requirements process compliance
- **IEEE 1016** — Design process compliance
- **IEEE 829 / ISO/IEC/IEEE 29119** — Testing process compliance
- **OWASP Top 10** — Vulnerability mitigation evidence
- **OWASP ASVS** — Verification level evidence
- **OWASP API Security Top 10** — API security evidence

## Example Invocation
```
/compliance-to-standards
```

## Related Skills
- `/risk-analysis-and-threat-modelling` — Prerequisite (risk treatment)
- `/validation` — Prerequisite
- `/verification` — Prerequisite
- `/security-checks` — Prerequisite
- `/performance-checks` — Prerequisite
- `/testing-and-quality-assurance` — Prerequisite
- `/production-ready-application` — Prerequisite
- `/development-exit-review` — Consumes compliance gate
- `/deployment-infrastructure-and-configuration` — Operational compliance