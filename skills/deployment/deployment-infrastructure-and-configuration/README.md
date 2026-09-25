# Deployment Infrastructure & Configuration

**Invocation**: `/deployment-infrastructure-and-configuration`
**Category**: Deployment
**Stage**: 6.4 — Deployment Infrastructure and Configuration

## Purpose
Provisions and configures the deployment infrastructure using Infrastructure as Code (IaC). Implements environment promotion (dev → staging → prod), secrets management, service discovery, load balancing, TLS termination, observability integration, and rollback automation.

## When to Use
- "deployment infrastructure"
- "IaC"
- "Terraform"
- "Kubernetes"
- "environment promotion"
- "secrets management"
- "service mesh"
- "rollback automation"

## Inputs
- Container images (from `/containerisation`)
- Release artefacts (from `/building-app-from-source-code`)
- Git tags/releases (from `/pushing-app-to-source-repo`)
- Cross-cutting architecture (from `/cross-cutting-architecture`) — observability, config
- Risk analysis (from `/risk-analysis-and-threat-modelling`) — security requirements

## Outputs
- Deployment infrastructure with:
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

## Standards Alignment
- **ISO/IEC 27001** — Operational security
- **ISO/IEC 25010** — Reliability, availability
- **NIST SP 800-53** — System security
- **CIS Benchmarks** — Platform hardening
- **SLSA** — Deployment integrity

## Example Invocation
```
/deployment-infrastructure-and-configuration
```

## Related Skills
- `/containerisation` — Prerequisite (images)
- `/building-app-from-source-code` — Prerequisite (artefacts)
- `/pushing-app-to-source-repo` — Prerequisite (triggers)
- `/cross-cutting-architecture` — Prerequisite (observability, config patterns)
- `/continuous-integration` — Pipeline integration
- `/performance-checks` — Validates infrastructure performance
- `/compliance-to-standards` — Provides infrastructure compliance evidence