# Logic, Algorithms, Workflows & Data Structures

**Invocation**: `/logic-algorithms-workflows-data-structures`
**Category**: Design
**Stage**: 2.3 — Logic, Algorithms, Workflows, and Data Structures

## Purpose
Designs the computational core: algorithm selection with complexity analysis, workflow orchestration patterns, and data structure design. Produces technology-agnostic specifications with formal complexity bounds, invariants, and traceability to functional requirements.

## When to Use
- "algorithm design"
- "workflow design"
- "data structure design"
- "business logic design"
- "complexity analysis"
- "computational design"

## Inputs
- Requirements specification (from `/requirements-specification`)
- Design principles (from `/design-principles`)
- Presentation layer wireframes (from `/presentation-layer-ui-ux-wireframes`) — for data display needs
- Non-functional requirements (performance, scalability)

## Outputs
- `project_documents/design/logic_algorithms_workflows_data_structures.md` — Logic specification with:
  - Algorithm catalogue (name, purpose, time/space complexity, invariants, edge cases)
  - Workflow definitions (states, transitions, guards, compensation actions)
  - Data structure specifications (ADTs, invariants, operations, persistence mapping)
  - Concurrency and synchronisation strategy
  - Error handling and retry policies
  - Performance budgets per operation
  - Traceability to functional requirements

## Standards Alignment
- **ISO/IEC 25010** — Performance efficiency, reliability
- **ISO/IEC/IEEE 12207** — Detailed design
- **IEEE 1016** — Design description (algorithmic)
- **OWASP ASVS** — Algorithmic security (timing attacks, resource exhaustion)

## Example Invocation
```
/logic-algorithms-workflows-data-structures
```

## Related Skills
- `/design-principles` — Prerequisite
- `/presentation-layer-ui-ux-wireframes` — Coordinates
- `/backend-apis-dal-database` — Consumes data structures for persistence
- `/coding-integration-and-debugging-standard` — Implements algorithms
- `/performance-checks` — Validates complexity bounds