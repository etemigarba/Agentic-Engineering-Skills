# Deployment Skills

## Overview

The Deployment stage (4 skills) takes production-ready code through reproducible builds, containerisation, git release workflow, and infrastructure provisioning to running production systems.

## Skills

### 6.1 Building from Source (`/building-app-from-source-code`)

**Purpose**: Reproducible, verified build artefacts with dependency resolution, compilation, packaging, signing, SBOM generation, and provenance attestation.

**Key Outputs**:
- Reproducible build process (hermetic, deterministic, cached)
- Dependency resolution (lockfiles, verified checksums, provenance)
- Compilation and packaging (optimised, stripped, versioned)
- Artefact signing (cosign, sigstore, keyless signing)
- SBOM generation (SPDX, CycloneDX, Syft)
- Provenance attestation (SLSA Level 3 target)
- Vulnerability scanning (artefact, dependencies, base images)
- Build attestation (GitHub Actions, GitLab CI, etc.)
- Artefact promotion (dev → staging → prod gates)

**Standards**: ISO/IEC/IEEE 12207, SLSA, SPDX/CycloneDX, Sigstore/cosign, OWASP ASVS

---

### 6.2 Containerisation (`/containerisation`)

**Purpose**: Production-hardened container images using multi-stage builds, distroless bases, security hardening, compliance scanning.

**Key Outputs**:
- Multi-stage Dockerfile (build → test → runtime)
- Minimal base images (distroless, scratch, alpine, wolfi)
- Non-root user, read-only filesystem, dropped capabilities
- Health checks, graceful shutdown, signal handling
- Resource limits and requests defined
- Security scanning (Trivy, Grype, Syft) in pipeline
- Image signing (cosign, sigstore)
- SBOM embedded/attached
- Registry promotion (dev → staging → prod with gates)
- Base image update automation (Dependabot, Renovate)

**Standards**: ISO/IEC 27001, NIST SP 800-190, CIS Docker Benchmark, SLSA, OWASP ASVS

---

### 6.3 Pushing to Source Repository (`/pushing-app-to-source-repo`)

**Purpose**: Git workflow for releasing: conventional commits, semantic versioning, signed commits/tags, release notes, branch protection, PR automation.

**Key Outputs**:
- Conventional commits enforcement (commitlint, husky)
- Semantic versioning (auto-changelog, release-please)
- Signed commits and tags (GPG, SSH, sigstore)
- Branch protection rules (required reviews, status checks, linear history)
- PR templates (conventional, security, breaking changes)
- Automated release notes (from commits, PRs, issues)
- Release tags and GitHub/GitLab releases
- Changelog generation (Keep a Changelog format)
- Dependabot/Renovate configuration
- CODEOWNERS for review routing

**Standards**: ISO/IEC/IEEE 12207, Conventional Commits, SemVer, SLSA, Git best practices

---

### 6.4 Deployment Infrastructure & Configuration (`/deployment-infrastructure-and-configuration`)

**Purpose**: IaC for environment promotion, secrets management, service discovery, load balancing, TLS, observability, GitOps, rollback, DR.

**Key Outputs**:
- IaC (Terraform, OpenTofu, Pulumi, CloudFormation) for all environments
- Environment promotion pipeline (dev → staging → prod with gates)
- Secrets management (Vault, Sealed Secrets, External Secrets, cloud KMS)
- Service discovery and load balancing (Ingress, Gateway API, service mesh)
- TLS everywhere (cert-manager, mTLS, certificate rotation)
- Observability stack (Prometheus, Grafana, Loki, Tempo, alerting)
- GitOps deployment (ArgoCD, Flux) with drift detection
- Rollback automation (failed deployment detection, one-click rollback)
- Disaster recovery (backup, restore, RTO/RPO tested)
- Cost monitoring and optimisation

**Standards**: ISO/IEC 27001, 25010, NIST SP 800-53, CIS Benchmarks, SLSA

---

## Stage Flow

```
Testing & QA Exit → Build from Source → Containerise
  → Push to Source Repo (triggers) → Deploy Infrastructure
  → Running Production Systems
```

## Exit Criteria

- Reproducible builds with SLSA Level 3 provenance
- Container images hardened, scanned, signed, promoted
- Git workflow enforced (signed commits, semantic versioning, protected branches)
- Infrastructure provisioned via IaC with GitOps
- All environments (dev, staging, prod) deployed and healthy
- Observability stack operational
- Rollback tested and documented
- Disaster recovery tested (RTO/RPO met)
- Cost monitoring active

All four skills must complete successfully for production release.