# Proposal & Technical Blueprint

**Invocation**: `/proposal-and-technical-blueprint`
**Category**: Analysis
**Stage**: 1.4 — Proposal and Technical Blueprint

## Purpose
Creates a funded proposal with architecture blueprint, cost model, risk assessment, and implementation roadmap. The artefact that secures executive funding and authorises the Design stage.

## When to Use
- "proposal"
- "technical blueprint"
- "architecture blueprint"
- "funding proposal"
- "executive proposal"

## Inputs
- Feasibility study (from `/feasibility-study`)
- Statement of the Problem (from `/statement-of-the-problem`)
- Organisational strategy and budget cycles

## Outputs
- `project_documents/analysis/proposal_and_technical_blueprint.md` — Funded proposal with:
  - Executive summary and investment thesis
  - Technical architecture blueprint (logical, physical, deployment)
  - Detailed cost model (CapEx, OpEx, TCO, phased investment)
  - Risk register with mitigation investments
  - Implementation roadmap (phases, milestones, dependencies)
  - Governance model (roles, gates, reporting)
  - Success metrics and KPIs

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Project initiation and planning
- **ISO/IEC 25010** — Quality requirements allocation
- **ISO/IEC 27001** — Security investment justification
- **IEEE 1016** — Architecture description

## Example Invocation
```
/proposal-and-technical-blueprint
```

## Related Skills
- `/feasibility-study` — Prerequisite
- `/design-principles` — Follows; establishes design governance
- `/risk-analysis-and-threat-modelling` — Informs risk register
- All Design skills — Consumes the blueprint