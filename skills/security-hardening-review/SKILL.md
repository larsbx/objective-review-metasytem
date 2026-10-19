---
name: security-hardening-review
description: Review and harden software, infrastructure, cloud systems, and delivery pipelines using least privilege, defense in depth, secure defaults, vulnerability management, secrets protection, monitoring, and incident readiness.
---
# Security Hardening Review

Establish the assets, actors, trust boundaries, threat model, deployment context, and existing controls before recommending changes. Prioritize exploitable paths and high-impact failures, distinguish verified vulnerabilities from hardening opportunities, and pair every remediation with a validation method. Do not claim compliance from a checklist alone.

**Version**: 2.1
**Last Updated**: 2025-11-23

> Security is not a feature to be traded off; it is the foundation. We assume breach, shift left, and enforce defense in depth.

---

## The 5 Rulings

### OBLIGATORY (Core Principles)
**Mandatory practices. Non-negotiable for a secure system.**

-   **Assume Breach**: Design assuming the perimeter is already compromised.
-   **Enforce Least Privilege**: Default deny. Grant minimum necessary access.
-   **Input Validation**: Whitelist allowed inputs. Never trust user data.
-   **Secrets Management**: Never commit secrets to code. Use a secrets manager.
-   **Patch Management**: Remediate Critical CVEs within 24 hours.
-   **Secure by Default**: Products must be secure out-of-the-box (no default passwords).

### ENCOURAGED (Pillars of Implementation)
**Best practices for robust security posture.**

-   **Shift Security Left**: Integrate security into design and code reviews.
-   **Immutable Infrastructure**: Replace servers rather than patching them.
-   **Defense in Depth**: Layered controls (Network + App + Data).
-   **Zero Trust Architecture**: Authenticate every request, regardless of origin.
-   **Automated Scanning**: SAST, DAST, and SCA in CI/CD pipelines.
-   **Incident Response**: Automated playbooks and regular drills.

### OPTIONAL (Advanced/Contextual)
**Practices for high-security or specific environments.**

-   **Cryptographic Agility**: Abstracting crypto to allow easy algorithm rotation.
-   **Microsegmentation**: Granular network policies between services.
-   **Chaos Engineering**: Intentionally injecting failure to test resilience.

### DISCOURAGED (Anti-Patterns)
**Practices that weaken security.**

-   **Manual Configuration**: Leads to drift and errors. Use IaC.
-   **Long-Lived Secrets**: Rotate keys frequently (e.g., 90 days).
-   **"Security through Obscurity"**: Hiding logic is not securing it.
-   **Fail Open**: Systems must fail closed (deny access) when errors occur.

### PROHIBITED (Forbidden)
**Dangerous practices that create immediate vulnerability.**

-   **Hardcoded Secrets**: Committing credentials to git.
-   **Plaintext Passwords**: Storing passwords without hashing/salting.
-   **SQL Injection**: Using string concatenation for queries.
-   **Ignoring Critical CVEs**: Knowingly shipping vulnerable code.
-   **Default Credentials**: Shipping with `admin/admin`.

---

## Measurement Framework
-   **Critical Vuln SLA**: ≤24 hours.
-   **Mean Time To Detect (MTTD)**: ≤15 minutes.
-   **Dependency Vulnerabilities**: 0 Critical/High.

