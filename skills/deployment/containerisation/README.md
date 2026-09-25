# Containerisation

**Invocation**: `/containerisation`
**Category**: Deployment
**Stage**: 6.2 — Containerisation (Preparing for Staging)

## Purpose
Creates production-hardened container images using multi-stage builds, distroless/minimal base images, security hardening, and compliance scanning. Implements image signing, vulnerability management, and registry promotion workflows.

## When to Use
- "containerisation"
- "Dockerfile"
- "container image"
- "multi-stage build"
- "distroless"
- "container security"
- "image scanning"

## Inputs
- Build artefacts (from `/building-app-from-source-code`)
- Application runtime requirements
- Security baseline (from `/risk-analysis-and-threat-modelling`)
- Deployment infrastructure (from `/deployment-infrastructure-and-configuration`)

## Outputs
- Container images with:
  - Multi-stage Dockerfile (build → test → runtime stages)
  - Minimal base images (distroless, scratch, alpine, wolfi)
  - Non-root user, read-only filesystem, dropped capabilities
  - Health checks, graceful shutdown, signal handling
  - Resource limits and requests defined
  - Security scanning (Trivy, Grype, Syft) in pipeline
  - Image signing (cosign, sigstore)
  - SBOM embedded/attached
  - Registry promotion (dev → staging → prod with gates)
  - Base image update automation (Dependabot, Renovate)

## Standards Alignment
- **ISO/IEC 27001** — Deployment security
- **NIST SP 800-190** — Container security
- **CIS Docker Benchmark** — Hardening
- **SLSA** — Build integrity
- **OWASP ASVS** — Deployment verification

## Example Invocation
```
/containerisation
```

## Related Skills
- `/building-app-from-source-code` — Prerequisite (artefacts)
- `/continuous-integration` — Pipeline integration
- `/pushing-app-to-source-repo` — Registry auth
- `/deployment-infrastructure-and-configuration` — Consumes images
- `/containerisation` — Security checks in pipeline