# Security Checks

**Invocation**: `/security-checks`
**Category**: Testing & QA
**Stage**: 5.5 — Security Checks

## Purpose
Executes comprehensive security verification aligned to OWASP ASVS, Top 10, and API Security Top 10. Includes SAST, SCA, secrets scanning, dependency analysis, configuration review, and penetration testing coordination. Produces audit-ready security evidence.

## When to Use
- "security audit"
- "security checks"
- "OWASP verification"
- "penetration testing"
- "SAST"
- "secrets scanning"
- "dependency scanning"

## Inputs
- Production-ready application (from `/production-ready-application`)
- Risk analysis & threat model (from `/risk-analysis-and-threat-modelling`)
- CI/CD pipeline (from `/continuous-integration`)
- Container images (from `/containerisation`)
- Infrastructure config (from `/deployment-infrastructure-and-configuration`)

## Outputs
- `project_documents/testing/security_checks_report.md` — Security report with:
  - SAST findings (code-level vulnerabilities, categorised by OWASP Top 10)
  - SCA findings (vulnerable dependencies, licence issues, provenance)
  - Secrets scan results (hardcoded credentials, API keys, tokens)
  - Configuration review (insecure defaults, excessive permissions)
  - Container image vulnerabilities (base image, installed packages)
  - Infrastructure security (IaC misconfigurations, network exposure)
  - Penetration test coordination (scope, findings, remediation)
  - OWASP ASVS mapping (verification level achieved per requirement)
  - Remediation tracker (finding → fix → verification → regression test)
  - Security gate decision (pass/fail with conditions)

## Standards Alignment
- **OWASP Top 10** — Vulnerability categories (primary)
- **OWASP ASVS** — Verification requirements (Level 1/2/3)
- **OWASP API Security Top 10** — API-specific checks
- **ISO/IEC 27001** — Control implementation verification
- **NIST SSDF** — Secure software development framework
- **SLSA** — Supply chain integrity

## Example Invocation
```
/security-checks
```

## Related Skills
- `/risk-analysis-and-threat-modelling` — Prerequisite (threat model)
- `/production-ready-application` — Prerequisite (what to test)
- `/containerisation` — Prerequisite (container security)
- `/continuous-integration` — Pipeline integration
- `/compliance-to-standards` — Consumes security evidence
- `/development-exit-review` — Consumes security gate
- `/validation` / `/verification` — Complementary verification