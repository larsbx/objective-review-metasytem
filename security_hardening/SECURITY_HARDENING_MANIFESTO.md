---
id: "security-hardening"
title: "The Security Hardening Manifesto"
version: "2.1"
status: "current"
focus: "System security & resilience through layered, proactive defense"
primary_users: ["all-developers", "security-engineers", "devsecops-teams", "architects"]
learning_curve: "medium"
roi_timeline: "immediate"
adoption_scope: "universal-required"
principles_count: 6
tier_structure:
  core: 6
  standard: 0
  excellence: 0
applicability:
  project_types: ["all"]
  languages: ["all"]
  contexts: ["fintech", "healthcare", "government", "cloud-native", "compliance-driven"]
related_manifestos:
  complements: ["all"]
  prerequisites: []
  enables: ["zero-trust", "compliance", "incident-response"]
tools:
  categories: ["sast", "dast", "sca", "siem", "soar", "edr", "secrets-management", "cspm"]
  count: 100+
standards:
  - "OWASP Top 10"
  - "NIST Cybersecurity Framework"
  - "CIS Controls"
  - "ISO 27001"
  - "PCI-DSS"
  - "GDPR"
measurement:
  vulnerability_management:
    critical_vuln_sla:
      target: "≤24 hours to patch"
      measurement: "vulnerability-management-system"
    high_vuln_sla:
      target: "≤7 days to patch"
      measurement: "vulnerability-management-system"
  incident_response:
    mttd: # Mean Time To Detect
      target: "≤15 minutes"
      acceptable: "≤1 hour"
      measurement: "siem-metrics"
    mttr: # Mean Time To Respond
      target: "≤1 hour"
      acceptable: "≤4 hours"
      measurement: "incident-response-records"
  scanning:
    sast_scan_frequency:
      target: "every-commit"
      measurement: "ci-cd-logs"
    dependency_vulnerabilities:
      target: "0 critical, 0 high"
      measurement: "snyk-dependabot-renovate"
  secrets_management:
    hardcoded_secrets:
      target: "0"
      measurement: "trufflehog-gitleaks"
---
# The Security Hardening Manifesto

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
