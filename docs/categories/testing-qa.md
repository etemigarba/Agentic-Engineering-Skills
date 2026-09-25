# Testing & QA Skills

## Overview

The Testing & QA stage (4 skills) executes the test strategy, conducts user acceptance testing, validates performance, and produces compliance evidence. Each skill produces a markdown report in `project_documents/testing/`.

## Skills

### 5.0 Testing & Quality Assurance (`/testing-and-quality-assurance`)

**Purpose**: Define and execute comprehensive test strategy: test pyramid, test data management, quality gates, defect lifecycle, release criteria.

**Key Outputs**:
- Test pyramid definition (unit, integration, contract, E2E, performance, security)
- Test data strategy (generation, masking, privacy, environments)
- Quality gates per pipeline stage (entry/exit criteria, thresholds)
- Defect lifecycle (classification, prioritisation, SLA, root cause)
- Release criteria (coverage, critical defects, performance, security)
- Test environment strategy (provisioning, isolation, teardown)
- Automation strategy (what, when, how, maintenance)
- Metrics and reporting (dashboards, trends, retrospectives)

**Standards**: ISO/IEC/IEEE 29119, IEEE 829, ISO/IEC 25010, 27001, OWASP ASVS

---

### 5.1 Alpha Testing (`/alpha-testing`)

**Purpose**: Internal acceptance testing with real users in controlled environment. Captures usability, functional gaps, performance observations, satisfaction.

**Key Outputs**:
- Test participant demographics and selection rationale
- Test scenarios and scripts (core journeys, edge cases)
- Functional findings (defects, gaps, workarounds)
- Usability metrics (task success, time, errors, SUS/NASA-TLX)
- Performance observations (perceived latency, responsiveness)
- User feedback (qualitative, feature requests, pain points)
- Severity-classified defect list with reproduction steps
- Release readiness assessment (go/no-go for beta/production)
- Action items for remediation

**Standards**: ISO/IEC/IEEE 29119, 25010, IEEE 829

---

### 5.4 Performance Checks (`/performance-checks`)

**Purpose**: Systematic performance testing: load, stress, soak, spike, scalability. Measures latency, throughput, resource utilisation against SLAs.

**Key Outputs**:
- Test configurations (scenarios, data volumes, user profiles, duration)
- Load test results (latency percentiles, throughput, error rates vs load)
- Stress test results (breaking point, degradation mode, recovery)
- Soak test results (stability over time, memory leaks, resource drift)
- Spike test results (burst handling, queue behaviour, autoscaling)
- Scalability results (horizontal/vertical scaling efficiency)
- Resource utilisation (CPU, memory, disk, network, DB)
- Bottleneck analysis (profiling, tracing, query analysis)
- SLA compliance matrix (requirement → measured → pass/fail)
- Optimisation recommendations with effort/impact estimates

**Standards**: ISO/IEC 25010 (performance efficiency), 29119, IEEE 829

---

### 5.6 Compliance to Standards (`/compliance-to-standards`)

**Purpose**: Produce compliance evidence pack mapping artefacts to ISO/IEC, IEEE, OWASP, regulatory clauses. Audit-ready documentation.

**Key Outputs**:
- Standards applicability matrix (which clauses apply, why)
- Evidence mapping (clause → artefact → location → status)
- Gap analysis (unmet clauses, compensating controls, remediation)
- Audit trail (who, when, what, how for each evidence item)
- Control implementation statements (ISO 27001 Annex A, OWASP ASVS)
- Residual risk register (accepted risks with owner approval)
- Certification readiness assessment (internal audit results)
- Continuous compliance monitoring plan

**Standards**: ISO/IEC 27001/27002, 25010, 12207, 29148, IEEE 1016, 829/29119, OWASP Top 10/ASVS/API Top 10

---

## Stage Flow

```
Validation & Verification → Testing Strategy → Alpha Testing
  → Performance Checks → Compliance Evidence
  → Deployment Stage Gate
```

## Exit Criteria

- Test strategy executed and documented
- Alpha testing complete with go/no-go for production
- Performance SLAs met (all test types)
- Compliance evidence pack complete and audit-ready
- All critical/high defects resolved or waived with owner approval
- Release criteria satisfied per Testing & QA strategy

All four reports required for Deployment stage entry.