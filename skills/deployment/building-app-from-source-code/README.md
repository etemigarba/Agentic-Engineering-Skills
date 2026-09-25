# Building Application from Source Code

**Invocation**: `/building-app-from-source-code`
**Category**: Deployment
**Stage**: 6.1 — Building the Application from Source Code

## Purpose
Produces reproducible, verified build artefacts from source code. Implements build pipeline with dependency resolution, compilation, packaging, artefact signing, SBOM generation, and provenance attestation. Ensures build integrity and supply-chain security.

## When to Use
- "build from source"
- "reproducible build"
- "build pipeline"
- "artefact generation"
- "SBOM"
- "supply chain security"

## Inputs
- Development exit review approval (from `/development-exit-review`)
- CI/CD pipeline (from `/continuous-integration`)
- Containerisation config (from `/containerisation`)
- Source repository (from `/pushing-app-to-source-repo`)

## Outputs
- Build system with:
  - Reproducible build process (hermetic, deterministic, cached)
  - Dependency resolution (lockfiles, verified checksums, provenance)
  - Compilation and packaging (optimised, stripped, versioned)
  - Artefact signing (cosign, sigstore, keyless signing)
  - SBOM generation (SPDX, CycloneDX, Syft)
  - Provenance attestation (SLSA Level 3 target)
  - Vulnerability scanning (artefact, dependencies, base images)
  - Build attestation (GitHub Actions, GitLab CI, etc.)
  - Artefact promotion (dev → staging → prod gates)

## Standards Alignment
- **ISO/IEC/IEEE 12207** — Integration and build process
- **SLSA** — Supply chain Levels for Software Artifacts
- **SPDX / CycloneDX** — SBOM formats
- **Sigstore / cosign** — Signing and verification
- **OWASP ASVS** — Build security

## Example Invocation
```
/building-app-from-source-code
```

## Related Skills
- `/development-exit-review` — Prerequisite
- `/continuous-integration` — Prerequisite (pipeline)
- `/containerisation` — Coordinates (build → image)
- `/pushing-app-to-source-repo` — Prerequisite (source)
- `/deployment-infrastructure-and-configuration` — Consumes artefacts