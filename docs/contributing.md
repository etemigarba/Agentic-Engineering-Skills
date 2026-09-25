# Contributing to Documentation

## Documentation Structure

```
docs/
├── index.md                      # This file
├── getting-started.md            # Installation & first steps
├── skill-reference.md            # Complete skill catalog
├── invocation-guide.md           # How to invoke skills
├── standards-alignment.md        # Standards mapping
├── contributing.md               # This file
└── categories/                   # Per-category guides
    ├── analysis.md
    ├── design.md
    ├── development.md
    ├── validation-verification.md
    ├── testing-qa.md
    └── deployment.md
```

## Writing Guidelines

### Style
- Use clear, concise language
- Prefer active voice
- Use British English spelling (consistent with skills)
- Keep sentences relatively short

### Formatting
- Use ATX headings (`#`, `##`, `###`)
- Use tables for structured data
- Use code blocks for commands and examples
- Use relative links for internal references

### Skill Documentation
Each skill's `README.md` must include:
1. **Purpose** — What the skill achieves
2. **When to Use** — Trigger phrases and scenarios
3. **Inputs** — What the skill expects
4. **Outputs** — What the skill produces
5. **Standards Alignment** — Specific standards with relevance
6. **Example Invocation** — Exact slash command
7. **Related Skills** — Dependencies and consumers

## Updating Documentation

### When Adding a Skill
1. Add skill to appropriate category in `skill-reference.md`
2. Create category guide entry in `categories/<category>.md`
3. Update invocation guide with trigger phrases
4. Update standards alignment matrix
5. Run `./scripts/generate-catalog.py`

### When Modifying a Skill
1. Update skill's `README.md`
2. Update `skill-reference.md` if invocation/purpose changed
3. Update category guide if scope changed
4. Run validation: `./scripts/validate-skills.py`

## Review Process

Documentation changes follow the same PR process as code:
1. Fork and create feature branch
2. Make changes
3. Run validation scripts
4. Submit PR with description of changes
5. Address review feedback

## Tools

- Markdown linting: Consider adding `markdownlint` to CI
- Link checking: `.markdown-link-check.json` configured
- Spell check: Consider `cspell` for technical terms