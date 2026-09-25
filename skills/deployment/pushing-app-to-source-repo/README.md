# Pushing Application to Source Repository

**Invocation**: `/pushing-app-to-source-repo`
**Category**: Deployment
**Stage**: 6.3 — Pushing the Application to the Source Repository

## Purpose
Manages the Git workflow for releasing code: conventional commits, semantic versioning, signed commits/tags, release notes generation, branch protection, and PR automation. Ensures traceability from commit to deployment.

## When to Use
- "git workflow"
- "conventional commits"
- "semantic versioning"
- "signed commits"
- "release automation"
- "branch protection"
- "PR automation"

## Inputs
- Development exit review approval (from `/development-exit-review`)
- Project structure (from `/project-creation-and-structure`)
- CI/CD pipeline (from `/continuous-integration`)

## Outputs
- Git workflow with:
  - Conventional commits enforcement (commitlint, husky)
  - Semantic versioning (auto-changelog, release-please)
  - Signed commits and tags (GPG, SSH, sigstore)
  - Branch protection rules (required reviews, status checks, linear history)
  - PR templates (conventional, security, breaking changes)
  - Automated release notes (from commits, PRs, issues)
  - Release tags and GitHub/GitLab releases
  - Changelog generation (Keep a Changelog format)
  - Dependabot/Renovate configuration
  - CODEOWNERS for review routing

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Configuration management
- **Conventional Commits** — Commit message format
- **SemVer** — Versioning scheme
- **SLSA** — Provenance and integrity
- **Git best practices** — Branching, merging, signing

## Example Invocation
```
/pushing-app-to-source-repo
```

## Related Skills
- `/development-exit-review` — Prerequisite
- `/project-creation-and-structure` — Prerequisite
- `/continuous-integration` — Pipeline integration
- `/building-app-from-source-code` — Consumes tags for build
- `/containerisation` — Consumes tags for image tags