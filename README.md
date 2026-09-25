# Agentic Engineering Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 33](https://img.shields.io/badge/Skills-33-blue.svg)](#skill-catalog)
[![Categories: 6](https://img.shields.io/badge/Categories-6-green.svg)](#categories)
[![Year: 2026](https://img.shields.io/badge/Year-2026-orange.svg)](#)
[![Standards: ISO/IEC, IEEE, OWASP](https://img.shields.io/badge/Standards-ISO%2FIEC%2C%20IEEE%2C%20OWASP-red.svg)](#standards-alignment)

> **33 production-grade, technology-agnostic skills for AI-native software engineering across 6 SDLC stages.** Security-first, performance-first, enterprise-ready. Auto-discoverable in Claude Code, OpenCode, Antigravity, and Codex.

---

## Overview

**Agentic Engineering Skills** is a curated collection of 33 reusable skills that enable professional agentic engineers to orchestrate the development of full-stack applications using technology-agnostic prompts based on global best practices. Each skill implements a Six-Protocol prompt structure (Role, Context, Task, Pitfalls, Format, Clarifying Questions) aligned to ISO/IEC, IEEE, and OWASP standards.

### Key Features

- **Technology-Agnostic**: No vendor, language, framework, or cloud platform lock-in
- **Standards-Aligned**: ISO/IEC 25010, 27001, 12207, 29148; IEEE 1016, 829; OWASP Top 10, ASVS
- **Security-First & Performance-First**: Built-in security and performance controls at every stage
- **Auto-Discovery**: Skills load automatically when relevant tasks appear
- **Explicit Invocation**: Use `/skill-name` (e.g., `/statement-of-the-problem`, `/security-checks`, `/mvp-build`)
- **Multi-Runtime**: Works with Claude Code, OpenCode, Antigravity, and Codex

---

## Quick Start

### Installation

```bash
# Global installation (available across all projects)
~/.claude/skills/agentic-engineering-skills/

# Or project-level installation
git clone https://github.com/your-org/agentic-engineering-skills.git
cp -r skills/* .claude/skills/
```

### Usage

Skills auto-discover based on task context, or invoke explicitly:

```bash
# Explicit invocation
/statement-of-the-problem
/security-checks
/mvp-build

# Auto-discovery triggers on phrases like:
"optimize prompt", "improve my prompt" → /etemi-prompt-enhancer
"statement of the problem" → /statement-of-the-problem
"security audit" → /security-checks
"build MVP" → /mvp-build
```

---

## Skill Catalog

### Analysis (6 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Statement of the Problem | `/statement-of-the-problem` | Produce the opening analysis artefact with quantified gap, root-cause (5 Whys, Ishikawa, Pareto), baseline, impact quantification, and solution boundary |
| Concept Note & Idea Validation | `/concept-note-and-idea-validation` | Validate product concepts against feasibility, market fit, and strategic alignment |
| Feasibility Study | `/feasibility-study` | Assess technical, economic, legal, operational, and scheduling feasibility |
| Proposal & Technical Blueprint | `/proposal-and-technical-blueprint` | Create funded proposal with architecture blueprint, cost model, and risk assessment |
| Requirements Specification | `/requirements-specification` | Produce IEEE 29148-compliant requirements with traceability and acceptance criteria |
| Risk Analysis & Threat Modelling | `/risk-analysis-and-threat-modelling` | STRIDE/DREAD threat model, DPIA, supply-chain risk, abuse cases, quantified risk register |

### Design (7 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Design Principles | `/design-principles` | Authoritative reference for SoC, SOLID, DRY/KISS/YAGNI, coupling/cohesion, cloud-native tenets with quantified thresholds |
| Presentation Layer (UI/UX) | `/presentation-layer-ui-ux-wireframes` | Wireframes, interaction flows, accessibility, component states, design tokens |
| Logic, Algorithms & Data Structures | `/logic-algorithms-workflows-data-structures` | Algorithm selection, complexity analysis, workflow modelling, data structure design |
| Backend APIs, DAL & Database | `/backend-apis-dal-database` | API contracts, data access layer, schema design, migration strategy |
| Cross-Cutting Architecture | `/cross-cutting-architecture` | Observability, security, configuration, error handling, transaction boundaries |
| Design Documentation & Review | `/design-documentation-and-review` | ADRs, design specs, review checklists, traceability to requirements |
| Phase-Gate Design Exit Review | `/phase-gate-design-exit-review` | Quantified exit criteria for design stage gate |

### Development (9 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Project Creation & Structure | `/project-creation-and-structure` | Scaffold repo, directory layout, tooling, conventions |
| Coding, Integration & Debugging Standard | `/coding-integration-and-debugging-standard` | Code style, integration patterns, debugging workflows |
| Proof of Concept | `/proof-of-concept` | Rapid feasibility validation with real contracts, provisional data |
| Prototype | `/prototype` | Functional vertical slice with real persistence, seeded data |
| MVP Build | `/mvp-build` | End-to-end working product slice: interface, logic, backend, real persistence |
| Production-Ready Application | `/production-ready-application` | Full feature completion, hardening, observability, documentation |
| Continuous Integration | `/continuous-integration` | Pipeline setup, quality gates, automated testing, deployment prep |
| Development Exit Review | `/development-exit-review` | Quantified exit criteria for development stage gate |
| Debug | `/debug` | Systematic debugging workflow with hypothesis tracking |

### Validation & Verification (2 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Validation | `/validation` | "Are we building the right thing?" — requirements traceability, stakeholder acceptance |
| Verification | `/verification` | "Are we building it right?" — code inspection, static analysis, test coverage |

### Testing & QA (4 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Testing & Quality Assurance | `/testing-and-quality-assurance` | Test strategy, pyramid, test data management, quality gates |
| Alpha Testing | `/alpha-testing` | Internal acceptance testing with real users, feedback loops |
| Performance Checks | `/performance-checks` | Load, stress, soak testing; latency, throughput, resource profiling |
| Compliance to Standards | `/compliance-to-standards` | ISO/IEC, IEEE, OWASP, regulatory compliance evidence packs |

### Deployment (4 skills)
| Skill | Invocation | Purpose |
|-------|------------|---------|
| Building from Source | `/building-app-from-source-code` | Reproducible builds, artifact generation, SBOM |
| Containerisation | `/containerisation` | Multi-stage Dockerfiles, security hardening, image signing |
| Pushing to Source Repository | `/pushing-app-to-source-repo` | Git workflow, conventional commits, signed commits, PR automation |
| Deployment Infrastructure & Config | `/deployment-infrastructure-and-configuration` | IaC, environment promotion, secrets, rollback, health checks |

---

## Standards Alignment

| Standard | Scope | Skills Applying |
|----------|-------|-----------------|
| **ISO/IEC 25010** | Product quality characteristics | All skills |
| **ISO/IEC 27001/27002** | Information security | Risk Analysis, Security Checks, all Design/Dev skills |
| **ISO/IEC/IEEE 12207** | Lifecycle processes | All stage skills |
| **ISO/IEC/IEEE 29148** | Requirements engineering | Requirements Spec, Validation |
| **IEEE 1016** | Design descriptions | Design Principles, all Design skills |
| **IEEE 829 / ISO/IEC/IEEE 29119** | Testing documentation | Testing & QA, Alpha Testing |
| **OWASP Top 10** | Application security | Security Checks, all Dev/Deployment skills |
| **OWASP ASVS** | Security verification | Security Checks, Verification |
| **OWASP API Security Top 10** | API security | Backend APIs, Containerisation |

---

## Repository Structure

```
agentic-engineering-skills/
├── .github/                 # CI/CD, issue/PR templates
├── docs/                    # Documentation site
│   ├── categories/          # Per-category guides
│   └── ...
├── skills/
│   ├── analysis/            # 6 skills
│   ├── design/              # 7 skills
│   ├── development/         # 9 skills
│   ├── validation-verification/  # 2 skills
│   ├── testing-qa/          # 4 skills
│   └── deployment/          # 4 skills
├── scripts/                 # Installation, validation, catalog tools
├── examples/
│   └── project_documents/   # Minimal demo project structure
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contribution guidelines
├── CODE_OF_CONDUCT.md       # Community standards
├── CHANGELOG.md             # Version history
├── SECURITY.md              # Security policy
└── package.json             # Node.js tooling
```

---

## Installation Scripts

```bash
# Install all skills globally
./scripts/install-skills.sh --global

# Install to current project
./scripts/install-skills.sh --project

# Validate all skill formats
./scripts/validate-skills.py

# Generate skill catalog
./scripts/generate-catalog.py
```

---

## Documentation

- [Getting Started](docs/getting-started.md)
- [Skill Reference](docs/skill-reference.md)
- [Invocation Guide](docs/invocation-guide.md)
- [Standards Mapping](docs/standards-alignment.md)
- [Category Guides](docs/categories/)
- [Contributing](CONTRIBUTING.md)

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new skills
- Improving existing skills
- Reporting issues
- Documentation updates

---

## License

MIT License © 2026 [Prof. Etemi Joshua Garba](LICENSE)

No explicit permission required for adoption, editing, or refactoring of the skills.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-org/agentic-engineering-skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/agentic-engineering-skills/discussions)
- **Security**: [SECURITY.md](SECURITY.md)

---

*Built for agentic engineers, by agentic engineers. 🤖🚀*