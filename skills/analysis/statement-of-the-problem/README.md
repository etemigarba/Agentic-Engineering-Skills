# Statement of the Problem

**Invocation**: `/statement-of-the-problem`
**Category**: Analysis
**Stage**: 1.1 — Statement of the Problem

## Purpose
Produces the opening analysis artefact — the Statement of the Problem — with quantified gap analysis, root-cause investigation (Five Whys, Ishikawa, Pareto), current-state baseline, impact quantification (financial, operational, reputational, regulatory), and explicit solution boundary. This artefact must survive an analysis exit review before design funding is released.

## When to Use
- "statement of the problem"
- "problem statement"
- "root cause analysis"
- "gap analysis"
- "impact quantification"
- Starting a new project analysis phase

## Inputs
- `idea.md` in project root (sole authoritative input)
- Project context from `project_documents/` (if available)

## Outputs
- `project_documents/analysis/statement_of_the_problem.md` — Complete analysis document with:
  - Ideation (observation, problem statement, solution hypothesis, value proposition)
  - Problem framing (measured gap, stakeholders, consequence of inaction)
  - Root-cause investigation (Five Whys, Ishikawa, Pareto, addressable causes)
  - Current-state baseline (cycle times, error rates, effort, volume, SIPOC)
  - Impact quantification (financial, operational, reputational, regulatory, consolidated)
  - Solution boundary (in-scope, out-of-scope with defence, interfaces, assumptions)

## Standards Alignment
- **ISO/IEC/IEEE 29148** — Requirements specification
- **ISO/IEC/IEEE 12207** — Lifecycle processes
- **ISO/IEC 25010** — Product quality characteristics
- **ISO/IEC 27001** — Information security management
- **IEEE 1016** — Design description boundaries
- **OWASP Top 10 / ASVS** — Security posture

## Key Requirements
- Minimum 5 tables, 2 visualisations
- Minimum 5 governing equations with variable definitions
- All figures traceable to `idea.md` or marked `[ASSUMPTION]` with sensitivity range
- Technology-agnostic (no vendor, language, framework names)
- 1,800–2,500 words body text

## Example Invocation
```
/statement-of-the-problem
```

## Related Skills
- `/concept-note-and-idea-validation` — Precedes; validates the concept before problem framing
- `/feasibility-study` — Follows; assesses feasibility of the framed problem
- `/risk-analysis-and-threat-modelling` — Consumes solution boundary for threat modelling