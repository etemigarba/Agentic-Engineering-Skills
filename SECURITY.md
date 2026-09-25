# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in any of the skills or tooling, please report it responsibly.

### How to Report

**Do not** open a public issue for security vulnerabilities.

Instead, email us at **security@your-org.com** with:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested mitigation

We will acknowledge receipt within 48 hours and provide a timeline for resolution.

### What to Expect

1. **Acknowledgment** within 48 hours
2. **Initial assessment** within 5 business days
3. **Fix timeline** communicated within 10 business days
4. **Coordinated disclosure** after fix is available

## Skill Security Considerations

These skills are designed with security-first principles:

- **No secrets in skills**: Skills never contain or generate credentials, keys, or tokens
- **Input validation**: All skills enforce validation at trust boundaries
- **Output encoding**: Skills prevent injection through proper encoding
- **Secure defaults**: Configuration follows secure-by-default patterns
- **Standards alignment**: OWASP Top 10, ASVS, ISO/IEC 27001 mapped throughout

### Using Skills Securely

1. **Review before use**: Understand what each skill does before invoking
2. **Validate outputs**: Check generated code/artefacts before committing
3. **Environment isolation**: Run in appropriate environments (dev/staging/prod)
4. **Secrets management**: Use your platform's secret management, never hardcode
5. **Dependency scanning**: Skills may reference tool categories — verify your tool choices

## Vulnerability Disclosure Timeline

| Severity | Target Fix Time |
|----------|-----------------|
| Critical | 7 days          |
| High     | 14 days         |
| Medium   | 30 days         |
| Low      | 90 days         |

## Security-Related Skills

- `/risk-analysis-and-threat-modelling` — STRIDE/DREAD threat modelling
- `/security-checks` — OWASP-aligned security verification
- `/compliance-to-standards` — ISO/IEC 27001, OWASP compliance evidence
- `/validation` / `/verification` — Security requirements traceability
- All Development & Deployment skills — Built-in security controls

## Contact

Security Team: security@your-org.com
PGP Key: [Available on request]