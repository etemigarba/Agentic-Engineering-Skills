# Performance Checks

**Invocation**: `/performance-checks`
**Category**: Testing & QA
**Stage**: 5.4 — Performance Checks

## Purpose
Executes systematic performance testing: load, stress, soak, spike, and scalability testing. Measures latency, throughput, resource utilisation, and degradation patterns against defined SLAs. Identifies bottlenecks and provides optimisation evidence.

## When to Use
- "performance testing"
- "load testing"
- "stress testing"
- "soak testing"
- "scalability testing"
- "performance benchmarks"
- "SLA validation"

## Inputs
- Production-ready application (from `/production-ready-application`)
- Non-functional requirements (from `/requirements-specification`)
- Performance budgets (from `/logic-algorithms-workflows-data-structures`, `/backend-apis-dal-database`)
- Testing strategy (from `/testing-and-quality-assurance`)

## Outputs
- `project_documents/testing/performance_checks_report.md` — Performance report with:
  - Test configurations (scenarios, data volumes, user profiles, duration)
  - Load test results (latency percentiles, throughput, error rates vs load)
  - Stress test results (breaking point, degradation mode, recovery)
  - Soak test results (stability over time, memory leaks, resource drift)
  - Spike test results (burst handling, queue behaviour, autoscaling)
  - Scalability results (horizontal/vertical scaling efficiency)
  - Resource utilisation (CPU, memory, disk, network, DB)
  - Bottleneck analysis (profiling, tracing, database query analysis)
  - SLA compliance matrix (requirement → measured → pass/fail)
  - Optimisation recommendations with effort/impact estimates

## Standards Alignment
- **ISO/IEC 25010** — Performance efficiency (primary)
- **ISO/IEC/IEEE 29119** — Performance testing
- **IEEE 829** — Test reporting

## Example Invocation
```
/performance-checks
```

## Related Skills
- `/logic-algorithms-workflows-data-structures` — Prerequisite (complexity budgets)
- `/backend-apis-dal-database` — Prerequisite (indexing, query patterns)
- `/testing-and-quality-assurance` — Prerequisite
- `/production-ready-application` — Prerequisite
- `/development-exit-review` — Consumes performance gate
- `/containerisation` — Validates container resource limits
- `/deployment-infrastructure-and-configuration` — Validates autoscaling