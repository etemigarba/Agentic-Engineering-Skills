# Contributing to Agentic Engineering Skills

Thank you for your interest in contributing! This project thrives on community input.

## Ways to Contribute

### 1. Add a New Skill
- Follow the [Skill Authoring Guide](docs/skill-authoring-guide.md)
- Use the Six-Protocol structure (Role, Context, Task, Pitfalls, Format, Clarifying Questions)
- Ensure technology-agnostic language
- Align to ISO/IEC, IEEE, OWASP standards
- Include security-first and performance-first controls

### 2. Improve an Existing Skill
- Fix bugs or unclear instructions
- Add missing edge cases
- Improve examples or templates
- Update standards references

### 3. Documentation
- Fix typos, clarify explanations
- Add usage examples
- Improve category guides

### 4. Tooling
- Enhance installation scripts
- Add validation rules
- Improve catalog generation

## Skill Submission Process

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/new-skill-name`
3. **Add** your skill in `skills/<category>/<skill-name>/`
   - `<skill-name>.skill` (binary skill file)
   - `README.md` (documentation)
4. **Run** validation: `./scripts/validate-skills.py`
5. **Update** catalog: `./scripts/generate-catalog.py`
6. **Commit** with conventional commits: `feat: add <skill-name> skill`
7. **Push** and open a Pull Request

## Skill Structure

```
skills/<category>/<skill-name>/
├── <skill-name>.skill      # Binary skill file (required)
└── README.md               # Documentation (required)
```

## Skill README.md Template

```markdown
# <Skill Name>

**Invocation**: `/<skill-name>`
**Category**: <Analysis|Design|Development|Validation & Verification|Testing & QA|Deployment>
**Stage**: <Stage number and name>

## Purpose
One paragraph describing what this skill achieves and for whom.

## When to Use
- Trigger phrase 1
- Trigger phrase 2
- File type or input that should invoke this skill

## Inputs
What the skill expects (files, context, parameters).

## Outputs
What the skill produces (files, artefacts, decisions).

## Standards Alignment
- ISO/IEC XXXXX: <relevance>
- IEEE XXXX: <relevance>
- OWASP <Top 10/ASVS>: <relevance>

## Example Invocation
```
/skill-name
```

## Related Skills
- `/related-skill-1` — <relationship>
- `/related-skill-2` — <relationship>
```

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.