# Coding, Integration & Debugging Standard

**Invocation**: `/coding-integration-and-debugging-standard`
**Category**: Development
**Stage**: 3.3 — Coding, Integration, and Debugging Standard

## Purpose
Defines and enforces coding standards, integration patterns, and debugging workflows. Covers naming conventions, code organisation, error handling, logging, testing patterns, code review checklists, and systematic debugging procedures — all aligned to the project's technology choices and Design stage decisions.

## When to Use
- "coding standards"
- "code style"
- "integration patterns"
- "debugging workflow"
- "code review checklist"
- "error handling patterns"
- "logging standards"

## Inputs
- Project structure (from `/project-creation-and-structure`)
- All Design stage outputs (especially `/cross-cutting-architecture`)
- Team conventions and preferences

## Outputs
- `project_documents/development/coding_integration_debugging_standard.md` — Standards document with:
  - Coding conventions (naming, formatting, organisation, patterns)
  - Integration patterns (API client, event-driven, message queues, sync/async)
  - Error handling taxonomy (categories, wrapping, context, user-facing messages)
  - Logging standards (structured, levels, correlation IDs, PII handling)
  - Debugging procedures (hypothesis-driven, reproducible, tooling)
  - Code review checklist (security, performance, correctness, style)
  - Refactoring guidelines (when, how, verification)
  - Tooling enforcement (linters, formatters, type checkers, SAST)

## Standards Alignment
- **ISO/IEC 25010** — Maintainability, reliability, security
- **ISO/IEC/IEEE 12207** — Implementation process
- **OWASP ASVS** — Secure coding practices
- **OWASP Top 10** — Mitigation patterns

## Example Invocation
```
/coding-integration-and-debugging-standard
```

## Related Skills
- `/project-creation-and-structure` — Prerequisite
- `/cross-cutting-architecture` — Prerequisite (patterns defined there)
- `/proof-of-concept` — Applies standards early
- `/prototype` — Enforces standards
- `/mvp-build` — Full enforcement
- `/development-exit-review` — Validates adherence