#!/bin/bash
# install-skills.sh - Install Agentic Engineering Skills globally or per-project
# Usage: ./install-skills.sh [--global|--project] [--target-dir PATH]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SOURCE="$REPO_ROOT/skills"

# Default values
INSTALL_MODE="global"
TARGET_DIR=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --global)
            INSTALL_MODE="global"
            shift
            ;;
        --project)
            INSTALL_MODE="project"
            shift
            ;;
        --target-dir)
            TARGET_DIR="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [--global|--project] [--target-dir PATH]"
            echo "  --global      Install globally (default)"
            echo "  --project     Install to current project (.claude/skills/)"
            echo "  --target-dir  Custom target directory"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Determine target directory
if [[ -n "$TARGET_DIR" ]]; then
    INSTALL_TARGET="$TARGET_DIR"
elif [[ "$INSTALL_MODE" == "global" ]]; then
    # Detect runtime and set appropriate global path
    if command -v claude &> /dev/null; then
        INSTALL_TARGET="$HOME/.claude/skills/agentic-engineering-skills"
    elif command -v opencode &> /dev/null; then
        INSTALL_TARGET="$HOME/.config/opencode/skills/agentic-engineering-skills"
    elif command -v antigravity &> /dev/null; then
        INSTALL_TARGET="$HOME/.antigravity/skills/agentic-engineering-skills"
    elif command -v codex &> /dev/null; then
        INSTALL_TARGET="$HOME/.codex/skills/agentic-engineering-skills"
    else
        # Default to Claude Code
        INSTALL_TARGET="$HOME/.claude/skills/agentic-engineering-skills"
    fi
else
    # Project-level install
    INSTALL_TARGET="$(pwd)/.claude/skills/agentic-engineering-skills"
fi

echo "Installing Agentic Engineering Skills..."
echo "Mode: $INSTALL_MODE"
echo "Target: $INSTALL_TARGET"
echo "Source: $SKILLS_SOURCE"

# Create target directory
mkdir -p "$INSTALL_TARGET"

# Copy skills directory structure
echo "Copying skills..."
rsync -av --progress "$SKILLS_SOURCE/" "$INSTALL_TARGET/skills/"

# Verify installation
SKILL_COUNT=$(find "$INSTALL_TARGET/skills" -name "*.skill" -type f | wc -l)
echo ""
echo "Installation complete!"
echo "Skills installed: $SKILL_COUNT"
echo ""
echo "To verify, run:"
echo "  ls \"$INSTALL_TARGET/skills/analysis/\""
echo ""
echo "To use skills in Claude Code:"
echo "  /statement-of-the-problem"
echo "  /mvp-build"
echo "  /security-checks"
echo ""
echo "Skills auto-discover on phrases like:"
echo "  \"statement of the problem\""
echo "  \"build MVP\""
echo "  \"security audit\""