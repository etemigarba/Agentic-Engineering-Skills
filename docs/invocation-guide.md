# Invocation Guide

## How Skills Are Invoked

Skills can be invoked in two ways:

### 1. Explicit Invocation (Slash Command)

Use the skill's invocation name directly:

```bash
/statement-of-the-problem
/security-checks
/mvp-build
```

This is the most reliable method and works across all supported runtimes (Claude Code, OpenCode, Antigravity, Codex).

### 2. Auto-Discovery (Natural Language)

Skills register trigger phrases. When you use these phrases in a task description, the skill loads automatically:

| Phrase | Skill |
|--------|-------|
| "statement of the problem" | `/statement-of-the-problem` |
| "problem statement" | `/statement-of-the-problem` |
| "concept note" | `/concept-note-and-idea-validation` |
| "idea validation" | `/concept-note-and-idea-validation` |
| "feasibility study" | `/feasibility-study` |
| "technical blueprint" | `/proposal-and-technical-blueprint` |
| "requirements specification" | `/requirements-specification` |
| "threat model" | `/risk-analysis-and-threat-modelling` |
| "risk analysis" | `/risk-analysis-and-threat-modelling` |
| "design principles" | `/design-principles` |
| "wireframes" | `/presentation-layer-ui-ux-wireframes` |
| "UI design" | `/presentation-layer-ui-ux-wireframes` |
| "algorithm design" | `/logic-algorithms-workflows-data-structures` |
| "API design" | `/backend-apis-dal-database` |
| "cross-cutting" | `/cross-cutting-architecture` |
| "design review" | `/design-documentation-and-review` |
| "design gate" | `/phase-gate-design-exit-review` |
| "project setup" | `/project-creation-and-structure` |
| "coding standards" | `/coding-integration-and-debugging-standard` |
| "proof of concept" | `/proof-of-concept` |
| "prototype" | `/prototype` |
| "MVP" | `/mvp-build` |
| "production ready" | `/production-ready-application` |
| "CI/CD" | `/continuous-integration` |
| "development gate" | `/development-exit-review` |
| "debug" | `/debug` |
| "validation" | `/validation` |
| "verification" | `/verification` |
| "test strategy" | `/testing-and-quality-assurance` |
| "alpha testing" | `/alpha-testing` |
| "performance test" | `/performance-checks` |
| "compliance" | `/compliance-to-standards` |
| "build from source" | `/building-app-from-source-code` |
| "containerize" | `/containerisation` |
| "git workflow" | `/pushing-app-to-source-repo` |
| "deployment infrastructure" | `/deployment-infrastructure-and-configuration` |

## Invocation Patterns

### Single Skill

```bash
/statement-of-the-problem
```

### Sequential Skills (Pipeline)

```bash
/statement-of-the-problem
/concept-note-and-idea-validation
/feasibility-study
/proposal-and-technical-blueprint
/requirements-specification
/risk-analysis-and-threat-modelling
```

### Stage-Based Invocation

Invoke all skills in a stage:

```bash
# Analysis stage (6 skills)
/statement-of-the-problem
/concept-note-and-idea-validation
/feasibility-study
/proposal-and-technical-blueprint
/requirements-specification
/risk-analysis-and-threat-modelling
```

## Skill Context & Inputs

Most skills expect a `project_documents/` directory in the project root. Create it before running:

```bash
mkdir -p project_documents/{analysis,design,development,validation,testing,deployment}
```

Skills read from and write to this directory. The Analysis skills create the foundation that Design skills consume, which Development skills implement, and so on.

## Runtime Compatibility

| Runtime | Slash Command | Auto-Discovery | Notes |
|---------|---------------|----------------|-------|
| **Claude Code** | ✅ Full | ✅ Full | Native skill support |
| **OpenCode** | ✅ Full | ✅ Full | Compatible skill format |
| **Antigravity** | ✅ Full | ✅ Full | Compatible skill format |
| **Codex** | ✅ Full | ✅ Full | Compatible skill format |

## Troubleshooting

### Skill Not Loading

1. Check installation: `ls ~/.claude/skills/agentic-engineering-skills/skills/analysis/`
2. Verify skill name matches exactly (kebab-case)
3. Check runtime skill directory configuration

### Auto-Discovery Not Working

1. Use explicit invocation instead
2. Check trigger phrases match exactly
3. Ensure skill description in SKILL.md includes trigger phrases

### Permission Errors

```bash
chmod +x scripts/install-skills.sh
chmod +x scripts/validate-skills.py
chmod +x scripts/generate-catalog.py
```

## Best Practices

1. **Use explicit invocation** for critical skills (security, gates)
2. **Run stage-by-stage** — Analysis → Design → Development → Validation → Testing → Deployment
3. **Verify outputs** — Check `project_documents/` after each skill
4. **Commit artefacts** — Skills produce version-controllable markdown
5. **Run gates** — Exit reviews (`/phase-gate-design-exit-review`, `/development-exit-review`) enforce quality