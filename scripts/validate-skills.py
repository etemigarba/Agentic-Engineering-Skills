#!/usr/bin/env python3
"""
validate-skills.py - Validate Agentic Engineering Skills format and structure
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

EXPECTED_CATEGORIES = [
    "analysis",
    "design",
    "development",
    "validation-verification",
    "testing-qa",
    "deployment"
]

EXPECTED_SKILLS = {
    "analysis": [
        "statement-of-the-problem",
        "concept-note-and-idea-validation",
        "feasibility-study",
        "proposal-and-technical-blueprint",
        "requirements-specification",
        "risk-analysis-and-threat-modelling"
    ],
    "design": [
        "design-principles",
        "presentation-layer-ui-ux-wireframes",
        "logic-algorithms-workflows-data-structures",
        "backend-apis-dal-database",
        "cross-cutting-architecture",
        "design-documentation-and-review",
        "phase-gate-design-exit-review"
    ],
    "development": [
        "project-creation-and-structure",
        "coding-integration-and-debugging-standard",
        "proof-of-concept",
        "prototype",
        "mvp-build",
        "production-ready-application",
        "continuous-integration",
        "development-exit-review",
        "debug"
    ],
    "validation-verification": [
        "validation",
        "verification"
    ],
    "testing-qa": [
        "testing-and-quality-assurance",
        "alpha-testing",
        "performance-checks",
        "compliance-to-standards",
        "security-checks"
    ],
    "deployment": [
        "building-app-from-source-code",
        "containerisation",
        "pushing-app-to-source-repo",
        "deployment-infrastructure-and-configuration"
    ]
}

def validate_skill_file(skill_path: Path) -> List[str]:
    """Validate a single skill directory."""
    errors = []
    
    # Check for .skill binary file
    skill_files = list(skill_path.glob("*.skill"))
    if not skill_files:
        errors.append(f"Missing .skill binary file in {skill_path}")
    elif len(skill_files) > 1:
        errors.append(f"Multiple .skill files in {skill_path}: {skill_files}")
    
    # Check for README.md
    readme_path = skill_path / "README.md"
    if not readme_path.exists():
        errors.append(f"Missing README.md in {skill_path}")
    else:
        # Validate README structure
        content = readme_path.read_text(encoding='utf-8')
        required_sections = [
            "## Purpose",
            "## When to Use",
            "## Inputs",
            "## Outputs",
            "## Standards Alignment",
            "## Example Invocation",
            "## Related Skills"
        ]
        for section in required_sections:
            if section not in content:
                errors.append(f"README.md missing section '{section}' in {skill_path}")
    
    return errors

def validate_category(category: str) -> List[str]:
    """Validate all skills in a category."""
    errors = []
    category_path = SKILLS_DIR / category
    
    if not category_path.exists():
        errors.append(f"Category directory missing: {category}")
        return errors
    
    expected_skills = EXPECTED_SKILLS.get(category, [])
    found_skills = [d.name for d in category_path.iterdir() if d.is_dir()]
    
    # Check for missing skills
    for skill in expected_skills:
        if skill not in found_skills:
            errors.append(f"Missing skill: {category}/{skill}")
    
    # Check for unexpected skills
    for skill in found_skills:
        if skill not in expected_skills:
            errors.append(f"Unexpected skill in {category}: {skill}")
        else:
            # Validate skill structure
            skill_path = category_path / skill
            errors.extend(validate_skill_file(skill_path))
    
    return errors

def main():
    print("Validating Agentic Engineering Skills...")
    print(f"Repository: {REPO_ROOT}")
    print(f"Skills directory: {SKILLS_DIR}")
    print()
    
    all_errors = []
    
    # Check categories exist
    for category in EXPECTED_CATEGORIES:
        category_path = SKILLS_DIR / category
        if not category_path.exists():
            all_errors.append(f"Missing category directory: {category}")
    
    # Validate each category
    for category in EXPECTED_CATEGORIES:
        print(f"Validating {category}...")
        errors = validate_category(category)
        if errors:
            all_errors.extend(errors)
            for err in errors:
                print(f"  [FAIL] {err}")
        else:
            skill_count = len(EXPECTED_SKILLS.get(category, []))
            print(f"  [OK] {category}: {skill_count} skills valid")
    
    print()
    print("=" * 50)
    
    if all_errors:
        print(f"VALIDATION FAILED: {len(all_errors)} error(s)")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        total_skills = sum(len(s) for s in EXPECTED_SKILLS.values())
        print(f"VALIDATION PASSED: All {len(EXPECTED_CATEGORIES)} categories and {total_skills} skills valid")
        sys.exit(0)

if __name__ == "__main__":
    main()