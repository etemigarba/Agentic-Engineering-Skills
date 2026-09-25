# Getting Started

## Prerequisites

- **Claude Code** (latest) — Primary runtime
- **OpenCode** (latest) — Alternative runtime
- **Antigravity** (latest) — Alternative runtime
- **Codex** (latest) — Alternative runtime
- **Git** ≥ 2.30
- **Node.js** ≥ 18.x (for tooling scripts)
- **Python** ≥ 3.10 (for validation scripts)

## Installation

### Option 1: Global Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-org/agentic-engineering-skills.git
cd agentic-engineering-skills

# Install globally for all projects
./scripts/install-skills.sh --global
```

This installs skills to `~/.claude/skills/agentic-engineering-skills/` (or equivalent for OpenCode/Antigravity/Codex).

### Option 2: Project-Level Installation

```bash
# In your project root
git clone https://github.com/your-org/agentic-engineering-skills.git .claude/skills/agentic-engineering-skills
# Or copy the skills directory
cp -r /path/to/agentic-engineering-skills/skills .claude/skills/
```

## Verification

```bash
# Validate all skill formats
./scripts/validate-skills.py

# Generate skill catalog
./scripts/generate-catalog.py

# List available skills
ls ~/.claude/skills/agentic-engineering-skills/skills/
```

## First Invocation

Skills auto-discover based on task context. Try explicit invocation:

```bash
# In a Claude Code session
/statement-of-the-problem

# Or trigger by phrase
"Create a statement of the problem for my project"
```

## Project Structure for Skills

Skills expect a `project_documents/` directory in your project root:

```
your-project/
├── .claude/
│   └── skills/
│       └── agentic-engineering-skills/
├── project_documents/
│   ├── analysis/
│   ├── design/
│   ├── development/
│   ├── validation/
│   ├── testing/
│   └── deployment/
├── src/
├── tests/
└── ...
```

Create it before running skills:

```bash
mkdir -p project_documents/{analysis,design,development,validation,testing,deployment}
```

## Skill Categories & Invocation

| Category | Skills | Example Invocations |
|----------|--------|---------------------|
| **Analysis** | 6 | `/statement-of-the-problem`, `/risk-analysis-and-threat-modelling` |
| **Design** | 7 | `/design-principles`, `/backend-apis-dal-database` |
| **Development** | 9 | `/mvp-build`, `/production-ready-application` |
| **Validation & Verification** | 2 | `/validation`, `/verification` |
| **Testing & QA** | 4 | `/testing-and-quality-assurance`, `/performance-checks` |
| **Deployment** | 4 | `/containerisation`, `/deployment-infrastructure-and-configuration` |

## Auto-Discovery Triggers

Skills also trigger on natural language:

| Phrase | Invokes |
|--------|---------|
| "statement of the problem" | `/statement-of-the-problem` |
| "security audit" | `/security-checks` |
| "build MVP" | `/mvp-build` |
| "threat model" | `/risk-analysis-and-threat-modelling` |
| "design principles" | `/design-principles` |
| "performance test" | `/performance-checks` |
| "compliance check" | `/compliance-to-standards` |

## Next Steps

1. Read the [Invocation Guide](invocation-guide.md)
2. Browse the [Skill Reference](skill-reference.md)
3. Check [Standards Alignment](standards-alignment.md)
4. Try a skill on a sample project (see `examples/`)

## Troubleshooting

**Skill not found?**
- Verify installation: `ls ~/.claude/skills/`
- Check skill name: `ls ~/.claude/skills/agentic-engineering-skills/skills/analysis/`

**Permission errors?**
- Ensure scripts are executable: `chmod +x scripts/*.sh`

**Validation fails?**
- Run `./scripts/validate-skills.py --verbose` for details