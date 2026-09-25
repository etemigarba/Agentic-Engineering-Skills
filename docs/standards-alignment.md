# Standards Alignment

This document maps each skill to the ISO/IEC, IEEE, and OWASP standards it implements or verifies.

## Standards Overview

| Standard | Title | Scope |
|----------|-------|-------|
| **ISO/IEC 25010** | Systems and software Quality Requirements and Evaluation (SQuaRE) | Product quality characteristics |
| **ISO/IEC 27001** | Information security management systems | ISMS requirements |
| **ISO/IEC 27002** | Information security controls | Control implementation guidance |
| **ISO/IEC/IEEE 12207** | Systems and software engineering — Life cycle processes | Life cycle processes |
| **ISO/IEC/IEEE 29148** | Systems and software engineering — Life cycle processes — Requirements engineering | Requirements engineering |
| **IEEE 1016** | Software design descriptions | Design documentation |
| **IEEE 829** | Software test documentation | Test documentation |
| **ISO/IEC/IEEE 29119** | Software testing | Testing processes |
| **OWASP Top 10** | Top 10 Web Application Security Risks | Vulnerability awareness |
| **OWASP ASVS** | Application Security Verification Standard | Security verification |
| **OWASP API Security Top 10** | API Security Risks | API security |

---

## Skill → Standards Mapping

### Analysis Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | ISO/IEC/IEEE 29148 | IEEE 1016 | OWASP |
|-------|---------------|---------------|-------------------|-------------------|-----------|-------|
| Statement of the Problem | ✅ | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS |
| Concept Note & Idea Validation | ✅ | | ✅ | ✅ | | |
| Feasibility Study | ✅ | | ✅ | | | |
| Proposal & Technical Blueprint | ✅ | ✅ | ✅ | | ✅ | |
| Requirements Specification | ✅ | ✅ | ✅ | ✅ | | ASVS |
| Risk Analysis & Threat Modelling | ✅ | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS, Threat Modelling |

### Design Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | ISO/IEC/IEEE 29148 | IEEE 1016 | OWASP |
|-------|---------------|---------------|-------------------|-------------------|-----------|-------|
| Design Principles | ✅ | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS |
| Presentation Layer (UI/UX) | ✅ | | ✅ | ✅ | ✅ | ASVS |
| Logic, Algorithms, Workflows | ✅ | | ✅ | | ✅ | ASVS |
| Backend APIs, DAL & Database | ✅ | ✅ | ✅ | | ✅ | API Top 10, ASVS |
| Cross-Cutting Architecture | ✅ | ✅ | ✅ | | ✅ | ASVS |
| Design Documentation & Review | ✅ | | ✅ | ✅ | ✅ | |
| Phase-Gate Design Exit Review | ✅ | ✅ | ✅ | ✅ | ✅ | |

### Development Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | IEEE 829/29119 | OWASP |
|-------|---------------|---------------|-------------------|----------------|-------|
| Project Creation & Structure | ✅ | | ✅ | | ASVS |
| Coding, Integration & Debugging | ✅ | ✅ | ✅ | | Top 10, ASVS |
| Proof of Concept | ✅ | ✅ | ✅ | | ASVS |
| Prototype | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS |
| MVP Build | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS, API Top 10 |
| Production-Ready Application | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS, API Top 10 |
| Continuous Integration | ✅ | | ✅ | | ASVS, SLSA |
| Development Exit Review | ✅ | ✅ | ✅ | ✅ | ASVS |
| Debug | ✅ | ✅ | ✅ | | |

### Validation & Verification Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | ISO/IEC/IEEE 29148 | IEEE 1016 | IEEE 829/29119 | OWASP |
|-------|---------------|---------------|-------------------|-------------------|-----------|----------------|-------|
| Validation | ✅ | ✅ | ✅ | ✅ | | ✅ | ASVS |
| Verification | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ASVS |

### Testing & QA Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | IEEE 829/29119 | OWASP |
|-------|---------------|---------------|-------------------|----------------|-------|
| Testing & QA | ✅ | ✅ | ✅ | ✅ | ASVS |
| Alpha Testing | ✅ | | ✅ | ✅ | |
| Performance Checks | ✅ | | ✅ | ✅ | |
| Compliance to Standards | ✅ | ✅ | ✅ | ✅ | Top 10, ASVS, API Top 10 |

### Deployment Skills

| Skill | ISO/IEC 25010 | ISO/IEC 27001 | ISO/IEC/IEEE 12207 | OWASP | SLSA |
|-------|---------------|---------------|-------------------|-------|------|
| Building from Source | ✅ | | ✅ | ASVS | ✅ |
| Containerisation | ✅ | ✅ | ✅ | ASVS | ✅ |
| Pushing to Source Repository | ✅ | | ✅ | | ✅ |
| Deployment Infrastructure & Config | ✅ | ✅ | ✅ | ASVS | |

---

## Quality Characteristics Coverage (ISO/IEC 25010)

| Characteristic | Primary Skills |
|----------------|----------------|
| **Functional Suitability** | Requirements Spec, MVP Build, Production-Ready, Validation |
| **Performance Efficiency** | Logic/Algorithms, Performance Checks, MVP Build |
| **Compatibility** | Backend APIs, Containerisation, Deployment Infra |
| **Usability** | Presentation Layer, Alpha Testing, Validation |
| **Reliability** | Prototype, MVP Build, Production-Ready, Debug, Verification |
| **Security** | Risk Analysis, All Dev Skills, Security Checks, Compliance |
| **Maintainability** | Design Principles, Coding Standards, Design Docs, Verification |
| **Portability** | Containerisation, Deployment Infra, Project Structure |

---

## OWASP Coverage

| OWASP Standard | Skills Implementing |
|----------------|---------------------|
| **Top 10** | Risk Analysis, All Development Skills, Security Checks, Compliance |
| **ASVS Level 1** | All Development Skills, Validation, Verification, Testing & QA |
| **ASVS Level 2** | MVP Build, Production-Ready, Security Checks, Verification |
| **ASVS Level 3** | Production-Ready, Compliance to Standards |
| **API Security Top 10** | Backend APIs, MVP Build, Production-Ready, Containerisation |
| **Threat Modelling** | Risk Analysis & Threat Modelling |

---

## Compliance Evidence Generation

The `/compliance-to-standards` skill generates an evidence pack mapping every applicable clause to project artefacts:

```
Clause → Artefact → Location → Status → Auditor Notes
```

This enables:
- Internal audit readiness
- External certification (ISO 27001)
- Customer security questionnaires
- Regulatory submissions