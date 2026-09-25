# Analysis Skills

## Overview

The Analysis stage (6 skills) transforms a raw idea into a funded, well-understood problem with quantified impact, validated feasibility, and explicit solution boundaries. Each skill produces a markdown artefact in `project_documents/analysis/`.

## Skills

### 1.1 Statement of the Problem (`/statement-of-the-problem`)

**Purpose**: Produce the opening analysis artefact with quantified gap, root-cause (Five Whys, Ishikawa, Pareto), baseline, impact quantification, and solution boundary.

**Key Outputs**:
- Measured gap table (current vs required)
- Five Whys chain to systemic cause
- Ishikawa diagram (6 categories)
- Pareto ranking with cumulative %
- Impact quantification (financial, operational, reputational, regulatory)
- Consolidated impact table with confidence bands
- Explicit in-scope/out-of-scope lists

**Standards**: ISO/IEC/IEEE 29148, 12207, 25010, 27001, IEEE 1016, OWASP Top 10/ASVS

---

### 1.2 Concept Note & Idea Validation (`/concept-note-and-idea-validation`)

**Purpose**: Validate product concepts against feasibility, market fit, strategic alignment, and stakeholder value.

**Key Outputs**:
- Concept summary and value hypothesis
- Feasibility indicators (technical, market, financial, organisational)
- Stakeholder alignment assessment
- Go/No-Go recommendation with rationale

**Standards**: ISO/IEC/IEEE 29148, 25010, 27001

---

### 1.3 Feasibility Study (`/feasibility-study`)

**Purpose**: Assess technical, economic, legal, operational, and scheduling feasibility with quantified models.

**Key Outputs**:
- Technical feasibility (architecture, integration, scalability)
- Economic feasibility (NPV, IRR, payback, sensitivity analysis)
- Legal/regulatory feasibility
- Operational feasibility (org change, skills, culture)
- Schedule feasibility (critical path, risk buffers)
- Risk-adjusted go/no-go recommendation

**Standards**: ISO/IEC/IEEE 12207, 25010, 27001

---

### 1.4 Proposal & Technical Blueprint (`/proposal-and-technical-blueprint`)

**Purpose**: Create funded proposal with architecture blueprint, cost model, risk assessment, and implementation roadmap.

**Key Outputs**:
- Executive summary and investment thesis
- Technical architecture blueprint (logical, physical, deployment)
- Detailed cost model (CapEx, OpEx, TCO, phased)
- Risk register with mitigation investments
- Implementation roadmap (phases, milestones, dependencies)
- Governance model and success metrics

**Standards**: ISO/IEC/IEEE 12207, 25010, 27001, IEEE 1016

---

### 1.5 Requirements Specification (`/requirements-specification`)

**Purpose**: Produce IEEE 29148-compliant requirements with full traceability and quantified non-functional requirements.

**Key Outputs**:
- Functional requirements (use cases, user stories, business rules)
- Non-functional requirements (ISO/IEC 25010 quantified)
- Interface requirements (APIs, UI, data, hardware)
- Data requirements (entities, privacy, retention)
- Acceptance criteria per requirement (testable)
- Traceability matrix (requirement ↔ source ↔ design ↔ test)
- Prioritisation (MoSCoW, value/complexity)

**Standards**: ISO/IEC/IEEE 29148 (primary), 25010, 27001, IEEE 1016, OWASP ASVS

---

### 1.6 Risk Analysis & Threat Modelling (`/risk-analysis-and-threat-modelling`)

**Purpose**: Comprehensive threat model with STRIDE/DREAD, abuse cases, DPIA, supply-chain risk, and quantified risk register.

**Key Outputs**:
- Data-flow decomposition with trust boundaries (context + decomposed)
- STRIDE per element and boundary (CWE, OWASP mappings)
- Quantified risk rating (DREAD + likelihood/impact, CVSS)
- Abuse/misuse cases (4 adversary profiles)
- Data Protection Impact Assessment (if applicable)
- Third-party supply-chain risk (SBOM, hallucinated deps, typosquatting)
- 7+ governing equations (DREAD, ALE, NRV, availability, residual risk)
- Traceability matrix (threat ↔ requirement ↔ design ↔ test ↔ evidence)
- Analysis-gate exit checklist (quantified)

**Standards**: ISO/IEC 27001/27005, 25010, OWASP Top 10/ASVS/Threat Modelling, NIST SP 800-30/161, MITRE CWE/ATT&CK, IEEE 1016

---

## Stage Flow

```
Idea → Statement of Problem → Concept Validation → Feasibility Study
  → Proposal & Blueprint → Requirements Spec → Risk Analysis & Threat Model
  → Design Stage Gate
```

## Exit Criteria

All 6 analysis artefacts complete, traceable, reviewed, and approved. Risk register has all residual risks owned and accepted. Requirements specification passes IEEE 29148 checklist.