# Debug

**Invocation**: `/debug`
**Category**: Development
**Stage**: 3.7 — Debugging

## Purpose
Provides a systematic, hypothesis-driven debugging workflow for production and development issues. Covers reproduction, isolation, root-cause analysis, fix verification, and regression prevention. Integrates with observability stack and coding standards.

## When to Use
- "debug"
- "debugging"
- "troubleshooting"
- "root cause analysis"
- "incident response"
- "bug investigation"

## Inputs
- Coding standards (from `/coding-integration-and-debugging-standard`)
- Cross-cutting architecture (from `/cross-cutting-architecture`) — observability
- Incident reports, error logs, user reports
- Production/application access

## Outputs
- Debugging session record with:
  - Problem statement (symptoms, impact, severity)
  - Reproduction steps (minimal, reliable)
  - Hypothesis list (prioritised by likelihood and impact)
  - Investigation log (queries, traces, logs examined, experiments)
  - Root cause identification (with evidence)
  - Fix implementation (minimal, targeted, tested)
  - Verification (reproduction fails, regression tests pass)
  - Prevention (test added, monitor/alert added, process change)
  - Post-mortem (if production incident)

## Standards Alignment
- **ISO/IEC 25010** — Reliability, maintainability
- **ISO/IEC/IEEE 12207** — Maintenance process
- **ISO/IEC 27001** — Incident management
- **IEEE 1044** — Defect classification

## Example Invocation
```
/debug
```

## Related Skills
- `/coding-integration-and-debugging-standard` — Prerequisite (procedures)
- `/cross-cutting-architecture` — Prerequisite (observability)
- `/verification` — Validates fix correctness
- `/continuous-integration` — Runs regression tests