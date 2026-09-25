# Concept Note & Idea Validation

**Invocation**: `/concept-note-and-idea-validation`
**Category**: Analysis
**Stage**: 1.2 — Concept Note and Idea Validation

## Purpose
Validates product concepts against feasibility, market fit, strategic alignment, and stakeholder value. Produces a structured concept note that either greenlights progression to feasibility study or identifies fatal flaws early.

## When to Use
- "concept note"
- "idea validation"
- "concept validation"
- "product concept review"
- Early-stage product ideation

## Inputs
- Raw concept/idea description
- Stakeholder objectives
- Market context (if available)

## Outputs
- `project_documents/analysis/concept_note_and_idea_validation.md` — Validation report with:
  - Concept summary and value hypothesis
  - Feasibility indicators (technical, market, financial, organisational)
  - Stakeholder alignment assessment
  - Go/No-Go recommendation with rationale
  - Next steps or pivot suggestions

## Standards Alignment
- **ISO/IEC/IEEE 29148** — Requirements engineering (concept phase)
- **ISO/IEC 25010** — Product quality (suitability, viability)
- **ISO/IEC 27001** — Early security posture assessment

## Example Invocation
```
/concept-note-and-idea-validation
```

## Related Skills
- `/statement-of-the-problem` — Follows if concept is validated
- `/feasibility-study` — Follows for deeper analysis
- `/proposal-and-technical-blueprint` — Follows for funded proposal