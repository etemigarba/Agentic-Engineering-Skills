# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial repository structure with 33 skills across 6 categories
- MIT License (c) 2026 Prof. Etemi Joshua Garba
- Installation and validation scripts
- Documentation framework
- Example project structure

## [1.0.0] - 2026-09-25

### Added
- **Analysis (6 skills)**: Statement of the Problem, Concept Note & Idea Validation, Feasibility Study, Proposal & Technical Blueprint, Requirements Specification, Risk Analysis & Threat Modelling
- **Design (7 skills)**: Design Principles, Presentation Layer UI/UX Wireframes, Logic Algorithms Workflows Data Structures, Backend APIs DAL Database, Cross-Cutting Architecture, Design Documentation & Review, Phase-Gate Design Exit Review
- **Development (9 skills)**: Project Creation & Structure, Coding Integration & Debugging Standard, Proof of Concept, Prototype, MVP Build, Production-Ready Application, Continuous Integration, Development Exit Review, Debug
- **Validation & Verification (2 skills)**: Validation, Verification
- **Testing & QA (4 skills)**: Testing & Quality Assurance, Alpha Testing, Performance Checks, Compliance to Standards
- **Deployment (4 skills)**: Building from Source, Containerisation, Pushing to Source Repository, Deployment Infrastructure & Configuration

### Standards Alignment
- ISO/IEC 25010 (Product Quality)
- ISO/IEC 27001/27002 (Information Security)
- ISO/IEC/IEEE 12207 (Lifecycle Processes)
- ISO/IEC/IEEE 29148 (Requirements Engineering)
- IEEE 1016 (Design Descriptions)
- IEEE 829 / ISO/IEC/IEEE 29119 (Testing)
- OWASP Top 10, ASVS, API Security Top 10

### Tooling
- `scripts/install-skills.sh` — Global and project-level installation
- `scripts/validate-skills.py` — Skill format validation
- `scripts/generate-catalog.py` — Auto-generate skill catalog

---

## Versioning Scheme

- **Major**: Breaking changes to skill interfaces or invocation patterns
- **Minor**: New skills, significant enhancements to existing skills
- **Patch**: Bug fixes, documentation updates, minor improvements