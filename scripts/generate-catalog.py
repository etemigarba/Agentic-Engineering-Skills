#!/usr/bin/env python3
"""
generate-catalog.py - Generate skill catalog from skill README files
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Any

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
OUTPUT_FILE = REPO_ROOT / "SKILL_CATALOG.md"

CATEGORY_ORDER = [
    "analysis",
    "design",
    "development",
    "validation-verification",
    "testing-qa",
    "deployment"
]

CATEGORY_DISPLAY = {
    "analysis": "Analysis",
    "design": "Design",
    "development": "Development",
    "validation-verification": "Validation & Verification",
    "testing-qa": "Testing & QA",
    "deployment": "Deployment"
}

def parse_readme(readme_path: Path) -> Dict[str, str]:
    """Extract key information from skill README."""
    content = readme_path.read_text(encoding='utf-8')
    
    info = {
        "purpose": "",
        "invocation": "",
        "category": "",
        "stage": ""
    }
    
    # Extract invocation from first line or header
    lines = content.split('\n')
    for line in lines[:10]:
        if line.startswith('**Invocation**:') or line.startswith('Invocation:'):
            info["invocation"] = line.split(':', 1)[1].strip().strip('`')
            break
    
    # Extract purpose
    purpose_match = re.search(r'## Purpose\s*\n(.*?)(?:\n##|\Z)', content, re.DOTALL)
    if purpose_match:
        info["purpose"] = purpose_match.group(1).strip().split('\n')[0]
    
    # Extract category and stage from header
    for line in lines[:20]:
        if '**Category**:' in line or 'Category:' in line:
            info["category"] = line.split(':', 1)[1].strip()
        if '**Stage**:' in line or 'Stage:' in line:
            info["stage"] = line.split(':', 1)[1].strip()
    
    return info

def generate_catalog() -> str:
    """Generate the skill catalog markdown."""
    lines = [
        "# Agentic Engineering Skills Catalog",
        "",
        f"Generated on: {os.popen('date').read().strip()}",
        f"Total Skills: 33 across 6 categories",
        "",
        "---",
        ""
    ]
    
    total_skills = 0
    
    for category in CATEGORY_ORDER:
        category_path = SKILLS_DIR / category
        if not category_path.exists():
            continue
        
        display_name = CATEGORY_DISPLAY.get(category, category.title())
        lines.append(f"## {display_name}")
        lines.append("")
        
        skill_dirs = sorted([d for d in category_path.iterdir() if d.is_dir()])
        
        for skill_dir in skill_dirs:
            readme_path = skill_dir / "README.md"
            if not readme_path.exists():
                continue
            
            info = parse_readme(readme_path)
            invocation = info.get("invocation", f"/{skill_dir.name}")
            purpose = info.get("purpose", "No description available")
            stage = info.get("stage", "")
            
            lines.append(f"### `{invocation}`")
            if stage:
                lines.append(f"**Stage**: {stage}")
            lines.append(f"**Purpose**: {purpose}")
            lines.append("")
        
        lines.append("---")
        lines.append("")
        total_skills += len(skill_dirs)
    
    lines.append(f"**Total Skills: {total_skills}**")
    
    return '\n'.join(lines)

def main():
    print("Generating skill catalog...")
    catalog = generate_catalog()
    OUTPUT_FILE.write_text(catalog, encoding='utf-8')
    print(f"Catalog written to: {OUTPUT_FILE}")
    print("Done!")

if __name__ == "__main__":
    main()