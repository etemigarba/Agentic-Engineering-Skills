# Risk Analysis & Threat Modelling

**Invocation**: `/risk-analysis-and-threat-modelling`
**Category**: Analysis
**Stage**: 1.6 — Risk Analysis and Threat Modelling

## Purpose
Delivers a comprehensive, quantified threat model with STRIDE decomposition, DREAD risk rating, abuse/misuse cases, Data Protection Impact Assessment (DPIA), and third-party supply-chain risk assessment. Feeds Design-stage security architecture, test design, penetration testing scope, and compliance evidence. Every residual risk must be formally accepted by a named owner.

## When to Use
- "risk analysis"
- "threat modelling"
- "threat model"
- "STRIDE"
- "DREAD"
- "DPIA"
- "data protection impact assessment"
- "supply chain risk"
- "security architecture"

## Inputs
- All documents in `project_documents/analysis/` (problem statement, requirements, blueprint, etc.)
- Architecture decisions (if available)
- Data inventory and classification
- Regulatory scoping

## Outputs
- `project_documents/analysis/risk_analysis_and_threat_modelling.md` — Complete threat model with:
  - Data-flow decomposition with trust boundaries (context + decomposed levels)
  - STRIDE per element and boundary crossing (with CWE, OWASP mappings)
  - Quantified risk rating (DREAD + likelihood/impact matrix, CVSS reconciliation)
  - Abuse/misuse cases (external actor, compromised credential, insider, supply chain)
  - Data Protection Impact Assessment (if personal data processed)
  - Third-party supply-chain risk assessment (SBOM, hallucinated dependencies, typosquatting)
  - Theoretical models applied (DREAD, ALE, NRV, availability, residual risk, defect escalation)
  - Traceability matrix (threat ↔ requirement ↔ design ↔ test ↔ evidence)
  - Analysis-gate exit checklist (quantified criteria)

## Standards Alignment
- **ISO/IEC 27001/27005** — Risk management
- **ISO/IEC 25010** — Security characteristics
- **OWASP Top 10** — Threat categories
- **OWASP ASVS** — Verification requirements
- **OWASP Threat Modelling** — Methodology
- **NIST SP 800-30/161** — Risk assessment
- **MITRE CWE/ATT&CK** — Weakness and adversary taxonomy
- **IEEE 1016** — Design security description

## Key Requirements
- Minimum 7 governing equations with variable definitions
- Every threat traced to requirement, design element, test case, evidence
- Non-applicability of STRIDE categories explicitly justified
- Risk-to-data-subject vs risk-to-organisation separated
- Every risk has named owner, treatment decision, residual position

## Example Invocation
```
/risk-analysis-and-threat-modelling
```

## Related Skills
- `/statement-of-the-problem` — Prerequisite (solution boundary)
- `/requirements-specification` — Prerequisite (security NFRs)
- `/design-principles` — Follows; security principles
- `/backend-apis-dal-database` — Consumes threat model for API security
- `/security-checks` — Verifies mitigations implemented
- `/compliance-to-standards` — Consumes for compliance evidence