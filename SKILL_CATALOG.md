# Agentic Engineering Skills Catalog

Generated on: The current date is: 01/10/2026 
Enter the new date: (dd-mm-yy)
Total Skills: 33 across 6 categories

---

## Analysis

### `/concept-note-and-idea-validation`
**Stage**: 1.2 — Concept Note and Idea Validation
**Purpose**: Validates product concepts against feasibility, market fit, strategic alignment, and stakeholder value. Produces a structured concept note that either greenlights progression to feasibility study or identifies fatal flaws early.

### `/feasibility-study`
**Stage**: 1.3 — Feasibility Study
**Purpose**: Assesses technical, economic, legal, operational, and scheduling feasibility of the proposed solution. Produces a quantified feasibility report with risk-adjusted NPV, sensitivity analysis, and go/no-go recommendation for funding.

### `/proposal-and-technical-blueprint`
**Stage**: 1.4 — Proposal and Technical Blueprint
**Purpose**: Creates a funded proposal with architecture blueprint, cost model, risk assessment, and implementation roadmap. The artefact that secures executive funding and authorises the Design stage.

### `/requirements-specification`
**Stage**: 1.5 — Requirements Specification
**Purpose**: Produces an IEEE 29148-compliant requirements specification with full traceability, acceptance criteria, and quantified non-functional requirements. The authoritative source for all downstream design, development, and verification activities.

### `/risk-analysis-and-threat-modelling`
**Stage**: 1.6 — Risk Analysis and Threat Modelling
**Purpose**: Delivers a comprehensive, quantified threat model with STRIDE decomposition, DREAD risk rating, abuse/misuse cases, Data Protection Impact Assessment (DPIA), and third-party supply-chain risk assessment. Feeds Design-stage security architecture, test design, penetration testing scope, and compliance evidence. Every residual risk must be formally accepted by a named owner.

### `/statement-of-the-problem`
**Stage**: 1.1 — Statement of the Problem
**Purpose**: Produces the opening analysis artefact — the Statement of the Problem — with quantified gap analysis, root-cause investigation (Five Whys, Ishikawa, Pareto), current-state baseline, impact quantification (financial, operational, reputational, regulatory), and explicit solution boundary. This artefact must survive an analysis exit review before design funding is released.

---

## Design

### `/backend-apis-dal-database`
**Stage**: 2.4 — Backend APIs, Data Access Layer, and Database
**Purpose**: Designs the backend contract surface: API specifications (REST/gRPC/graph), data access layer patterns, database schema, migration strategy, and data integrity rules. Technology-agnostic with explicit contract definitions, versioning strategy, and security controls.

### `/cross-cutting-architecture`
**Stage**: 2.5 — Cross-Cutting Architecture
**Purpose**: Defines the cross-cutting concerns that span all layers: observability (logging, metrics, tracing), configuration management, error handling, transaction management, security enforcement, caching, and feature flags. Provides technology-agnostic patterns and enforcement mechanisms.

### `/design-documentation-and-review`
**Stage**: 2.6 — Design Documentation and Review
**Purpose**: Produces the complete design documentation package: Architecture Decision Records (ADRs), detailed design specifications, review checklists, and traceability matrices. Ensures every requirement traces to at least one design element and every design decision is recorded with rationale.

### `/design-principles`
**Stage**: 2.1 — Design Principles and Constraints
**Purpose**: Authors the authoritative reference chapter for design governance: Separation of Concerns, SOLID, DRY/KISS/YAGNI, Coupling/Cohesion (measured), and Cloud-Native Tenets. Each principle includes formal apparatus (equations, metrics, thresholds), techniques, tool categories, failure catalogue, and standard mappings. Includes Six-Protocol prompt boxes for each principle family and quantified Design exit gate criteria.

### `/logic-algorithms-workflows-data-structures`
**Stage**: 2.3 — Logic, Algorithms, Workflows, and Data Structures
**Purpose**: Designs the computational core: algorithm selection with complexity analysis, workflow orchestration patterns, and data structure design. Produces technology-agnostic specifications with formal complexity bounds, invariants, and traceability to functional requirements.

### `/phase-gate-design-exit-review`
**Stage**: 2.7 — Phase-Gate Design Exit Review
**Purpose**: Executes the quantified exit gate for the Design stage. Validates that all design artefacts are complete, traceable, reviewed, and meet the numerical thresholds defined in the Design Principles. Produces a go/no-go decision for the Development stage with a formal sign-off record.

### `/presentation-layer-ui-ux-wireframes`
**Stage**: 2.2 — Presentation Layer: UI/UX Wireframes
**Purpose**: Produces comprehensive wireframes, interaction flows, component specifications, and accessibility requirements for the presentation layer. Defines screen layouts, navigation patterns, state transitions, component library, design tokens, and usability criteria — all technology-agnostic.

---

## Development

### `/coding-integration-and-debugging-standard`
**Stage**: 3.3 — Coding, Integration, and Debugging Standard
**Purpose**: Defines and enforces coding standards, integration patterns, and debugging workflows. Covers naming conventions, code organisation, error handling, logging, testing patterns, code review checklists, and systematic debugging procedures — all aligned to the project's technology choices and Design stage decisions.

### `/continuous-integration`
**Stage**: 3.5 — Continuous Integration
**Purpose**: Establishes and maintains the CI/CD pipeline with quality gates, automated testing, security scanning, and deployment preparation. Ensures every change is validated against the full quality bar before merge and provides fast feedback to developers.

### `/debug`
**Stage**: 3.7 — Debugging
**Purpose**: Provides a systematic, hypothesis-driven debugging workflow for production and development issues. Covers reproduction, isolation, root-cause analysis, fix verification, and regression prevention. Integrates with observability stack and coding standards.

### `/development-exit-review`
**Stage**: 3.6 — Development Exit Review
**Purpose**: Executes the quantified exit gate for the Development stage. Validates that all code is complete, tested, reviewed, secure, performant, and documented. Produces a go/no-go decision for the Deployment stage with a formal sign-off record.

### `/mvp-build`
**Stage**: 3.4.iii — MVP Build
**Purpose**: Builds the Minimum Viable Product: a genuinely working vertical slice of the product with functional interface, real domain logic, real backend contracts, and real durable persistence (provisional data acceptable). The golden path transaction must execute end-to-end, persist, survive restart, and be retrievable.

### `/production-ready-application`
**Stage**: 3.4.iv — Production-Ready Application
**Purpose**: Completes the full feature set to production readiness: all requirements implemented, hardened, observable, documented, and verified. Removes all provisional elements, completes edge cases, implements operational tooling, and achieves the quality bar for production deployment.

### `/project-creation-and-structure`
**Stage**: 3.2 — Project Creation and Structure
**Purpose**: Scaffolds the repository with standardised directory layout, tooling configuration, coding conventions, CI/CD pipeline skeleton, and development environment setup. Establishes the foundation for consistent, reproducible development across the team.

### `/proof-of-concept`
**Stage**: 3.4.i — Proof of Concept (UI Wireframes)
**Purpose**: Builds a rapid feasibility validation focusing on the presentation layer wired to real contracts with provisional data. Validates that the UI/UX design is implementable, the API contracts are sound, and the core user journeys are achievable — before committing to full backend implementation.

### `/prototype`
**Stage**: 3.4.ii — Prototype
**Purpose**: Delivers a functional vertical slice with real persistence, real contracts, and seeded data. Implements the core domain logic, data access, and at least one complete user journey end-to-end. The exit test: a transaction executes through interface → logic → backend, persists, survives restart, and is retrievable.

---

## Validation & Verification

### `/validation`
**Stage**: 4.1 — Validation
**Purpose**: Answers "Are we building the right thing?" Validates that the implemented system satisfies the stakeholder needs and requirements as documented in the Requirements Specification. Includes stakeholder reviews, acceptance testing, usability validation, and requirements traceability verification.

### `/verification`
**Stage**: 4.2 — Verification
**Purpose**: Answers "Are we building it right?" Verifies that the implementation conforms to the design specifications, coding standards, and quality requirements. Includes code inspection, static analysis, test coverage verification, architecture conformance, and security verification.

---

## Testing & QA

### `/alpha-testing`
**Stage**: 5.1 — Alpha Testing
**Purpose**: Conducts internal acceptance testing with real users in a controlled environment. Captures usability feedback, functional gaps, performance observations, and user satisfaction data before beta or production release.

### `/compliance-to-standards`
**Stage**: 5.6 — Compliance to Standards
**Purpose**: Produces the compliance evidence pack demonstrating adherence to ISO/IEC, IEEE, OWASP, and regulatory standards. Maps requirements, design, implementation, testing, and verification artefacts to specific standard clauses. Generates audit-ready documentation.

### `/performance-checks`
**Stage**: 5.4 — Performance Checks
**Purpose**: Executes systematic performance testing: load, stress, soak, spike, and scalability testing. Measures latency, throughput, resource utilisation, and degradation patterns against defined SLAs. Identifies bottlenecks and provides optimisation evidence.

### `/security-checks`
**Stage**: 5.5 — Security Checks
**Purpose**: Executes comprehensive security verification aligned to OWASP ASVS, Top 10, and API Security Top 10. Includes SAST, SCA, secrets scanning, dependency analysis, configuration review, and penetration testing coordination. Produces audit-ready security evidence.

### `/testing-and-quality-assurance`
**Stage**: 5.0 — Testing and Quality Assurance
**Purpose**: Defines and executes the comprehensive test strategy: test pyramid, test data management, quality gates, defect lifecycle, and release criteria. Ensures testing is systematic, measurable, and aligned to risk.

---

## Deployment

### `/building-app-from-source-code`
**Stage**: 6.1 — Building the Application from Source Code
**Purpose**: Produces reproducible, verified build artefacts from source code. Implements build pipeline with dependency resolution, compilation, packaging, artefact signing, SBOM generation, and provenance attestation. Ensures build integrity and supply-chain security.

### `/containerisation`
**Stage**: 6.2 — Containerisation (Preparing for Staging)
**Purpose**: Creates production-hardened container images using multi-stage builds, distroless/minimal base images, security hardening, and compliance scanning. Implements image signing, vulnerability management, and registry promotion workflows.

### `/deployment-infrastructure-and-configuration`
**Stage**: 6.4 — Deployment Infrastructure and Configuration
**Purpose**: Provisions and configures the deployment infrastructure using Infrastructure as Code (IaC). Implements environment promotion (dev → staging → prod), secrets management, service discovery, load balancing, TLS termination, observability integration, and rollback automation.

### `/pushing-app-to-source-repo`
**Stage**: 6.3 — Pushing the Application to the Source Repository
**Purpose**: Manages the Git workflow for releasing code: conventional commits, semantic versioning, signed commits/tags, release notes generation, branch protection, and PR automation. Ensures traceability from commit to deployment.

---

**Total Skills: 33**