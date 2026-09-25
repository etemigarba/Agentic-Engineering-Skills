# Project Creation & Structure

**Invocation**: `/project-creation-and-structure`
**Category**: Development
**Stage**: 3.2 — Project Creation and Structure

## Purpose
Scaffolds the repository with standardised directory layout, tooling configuration, coding conventions, CI/CD pipeline skeleton, and development environment setup. Establishes the foundation for consistent, reproducible development across the team.

## When to Use
- "project setup"
- "repository scaffold"
- "project structure"
- "monorepo setup"
- "development environment"
- "tooling configuration"

## Inputs
- Design documentation (from `/design-documentation-and-review`)
- Phase-gate approval (from `/phase-gate-design-exit-review`)
- Technology choices (from Design stage, kept technology-agnostic in skills)

## Outputs
- Initialised repository with:
  - Directory structure (src/, tests/, docs/, scripts/, configs/)
  - Build configuration (package.json, pyproject.toml, etc.)
  - Linting/formatting config (ESLint, Prettier, Ruff, etc.)
  - Type checking config (TypeScript, mypy, etc.)
  - Test configuration (Jest, Vitest, pytest, Playwright)
  - CI/CD pipeline skeleton (GitHub Actions, GitLab CI, etc.)
  - Pre-commit hooks (Husky, pre-commit)
  - Development container / environment config
  - CONTRIBUTING.md, CODEOWNERS, .gitignore
  - License and security policy

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Project initiation
- **ISO/IEC 25010** — Maintainability (structure, modularity)
- **OWASP ASVS** — Secure development environment

## Example Invocation
```
/project-creation-and-structure
```

## Related Skills
- `/phase-gate-design-exit-review` — Prerequisite (gate must pass)
- `/coding-integration-and-debugging-standard` — Follows; uses conventions
- `/continuous-integration` — Extends pipeline skeleton
- `/containerisation` — Uses build config