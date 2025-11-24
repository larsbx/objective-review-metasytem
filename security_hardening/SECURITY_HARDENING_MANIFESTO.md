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
principles_count: 6 # Was 18, revised to 6 core principles
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

> Security is not a feature to be traded off; it is the foundation upon which reliable systems are built. This manifesto codifies the principles of modern, practical security engineering.

---

## The Six Core Principles

These six principles are the heart of the manifesto. They are memorable, actionable, and form the basis of a robust security posture. Everything else in this document is an elaboration of these ideas.

1.  **Assume Breach.**
    Your perimeter will be breached. Your internal network is not trusted. Design systems for resilience, not infallibility. This mindset leads directly to Zero Trust architectures, comprehensive monitoring, and robust incident response. The critical question is not *if* you will be compromised, but *when*, and how quickly you can detect and respond.

2.  **Shift Security Left.**
    Security cannot be bolted on after development. It must be an integral part of the entire lifecycle, from design to deployment. The cost of fixing a vulnerability skyrockets the later it is found. Threat model before you build, test as you code, and scan as you deploy.

3.  **Enforce Least Privilege.**
    Every user, service, and system should have the absolute minimum set of permissions required to perform its function, and nothing more. Default to deny. Grant access explicitly, temporarily, and with full auditability. Never trust, always verify.

4.  **Secure by Default.**
    Ship products that are secure out-of-the-box. Users must explicitly and consciously *weaken* security, never the other way around. This means no default passwords, TLS enabled, and strict permissions from the start.

5.  **Defense in Depth.**
    No single security control is perfect. A layered defense ensures that if one control fails, others are in place to stop an attack. Combine network controls, application security, data encryption, and endpoint protection.

6.  **Simplify and Automate.**
    Complexity is the enemy of security. Simple, auditable systems are more secure than complex, opaque ones. Automate security processes—testing, deployment gates, incident response—to eliminate human error and ensure consistency.

---

## The Four Pillars of Implementation

These four pillars provide the practical framework for implementing the Core Principles. Each section contains detailed guidance, patterns, and anti-patterns.

### Pillar I: Secure by Design
*(Implementing: "Shift Security Left")*

This pillar focuses on proactive security measures integrated into the development lifecycle.

1.  **The Secure Development Lifecycle (SDL)**: A holistic process for integrating security at every phase.
    -   **Requirements**: Define security requirements alongside functional ones.
    -   **Design**: Conduct **Threat Modeling** (using STRIDE, attack trees) to identify threats before writing code.
    -   **Implementation**: Follow secure coding guidelines.
    -   **Verification**: Automate security testing (SAST, DAST, SCA) in the CI/CD pipeline.
    -   **Release**: Require security sign-off and penetration testing for high-risk changes.
    -   **Response**: Have a plan for handling vulnerabilities discovered post-release.

2.  **Input Validation and Output Encoding**: Never trust data crossing a trust boundary.
    -   **Input Validation**: Whitelist allowed inputs. Use strict schemas (e.g., OpenAPI). Canonicalize data before validation.
    -   **Output Encoding**: Encode all data for its destination context (HTML, JS, URL) to prevent injection attacks (XSS, etc.).
    -   **SQL Injection**: Use parameterized queries or ORMs. Never use string concatenation.

3.  **Supply Chain Security**: Your dependencies are your vulnerabilities.
    -   **SBOM (Software Bill of Materials)**: Know what's in your software.
    -   **Pin Dependencies**: Use lockfiles to ensure reproducible builds.
    -   **Scan Continuously**: Automate vulnerability scanning for all dependencies.
    -   **Verify Provenance**: Use code signing and SLSA to ensure your dependencies haven't been tampered with.

---

### Pillar II: Secure by Default
*(Implementing: "Secure by Default" and "Simplify and Automate")*

This pillar focuses on building architectures and configurations that are inherently secure.

1.  **Immutable Infrastructure & Reproducible Builds**: Replace, don't repair.
    -   **Infrastructure as Code (IaC)**: Define all infrastructure in version-controlled files (e.g., Terraform).
    -   **Immutable Images**: Build container images that are never modified after deployment. No SSH for changes.
    -   **GitOps**: Use Git as the single source of truth for your desired state. Automated tools ensure the live environment matches the definition in Git.
    -   **Incident Response**: A compromised instance is terminated and replaced, not cleaned.

2.  **Secure Secrets Management**: Never commit secrets to code.
    -   **Centralized Store**: Use a dedicated secrets manager like HashiCorp Vault or a cloud provider's service (AWS Secrets Manager, etc.).
    -   **Rotation**: Automate the rotation of secrets (e.g., every 90 days).
    -   **Runtime Injection**: Inject secrets into the application environment at runtime, not build time.
    -   **Audit**: Log every access to a secret.

3.  **Cryptographic Agility**: Prepare for cryptographic primitives to be broken.
    -   **Abstract Crypto**: Don't hardcode algorithms.
    -   **Version Payloads**: Store encrypted data with a version and algorithm identifier (e.g., `{v:2, alg:"ChaCha20-Poly1305", ...}`).
    -   **Plan for Rotation**: Have a clear process for migrating to new algorithms without a full data re-encryption.

---

### Pillar III: Secure in Depth
*(Implementing: "Assume Breach" and "Defense in Depth")*

This pillar focuses on layered defenses and the assumption that attackers are already inside your network.

1.  **Zero Trust Architecture**: Trust nothing, verify everything.
    -   **Identity, not Network**: Access is based on strong identity verification (MFA), not network location. "Internal" is not "trusted."
    -   **mTLS**: Use mutual TLS to encrypt and authenticate all service-to-service communication.
    -   **Microsegmentation**: Use firewalls and network policies to strictly limit lateral movement between services.
    -   **Device Posture**: Verify that the connecting device is healthy (patched, encrypted, etc.) before granting access.

2.  **Least Privilege Access Control**: The foundation of Zero Trust.
    -   **RBAC/ABAC**: Implement Role-Based or Attribute-Based Access Control.
    -   **Just-in-Time (JIT) Access**: Grant temporary, auto-expiring access for privileged operations.
    -   **Separation of Duties**: Require multiple independent actors for critical operations (e.g., deployment requires approvals from both dev and ops).
    -   **Complete Mediation**: Re-validate permissions on every sensitive request; do not trust a session flag set at login.

3.  **Fail Securely**: Systems must fail in a way that denies access.
    -   If an authentication or authorization service fails, it must deny all requests, not "fail open."
    -   Use circuit breakers to prevent cascading failures while maintaining security boundaries.

---

### Pillar IV: Secure Operations
*(Implementing: "Assume Breach" and continuous improvement)*

This pillar covers the essential, ongoing processes required to maintain a strong security posture.

1.  **Vulnerability Management**: A continuous cycle of discovery and remediation.
    -   **Scan Everything**: Continuously scan dependencies, containers, infrastructure, and code.
    -   **Prioritize Risk**: Use a risk-based model (e.g., CVSS + EPSS) to prioritize what to fix first.
    -   **Enforce SLAs**: Define and enforce strict SLAs for patching (e.g., Critical: 24 hours, High: 7 days).
    -   **Virtual Patching**: Use WAF rules as a temporary compensating control when an immediate patch is not possible.

2.  **Security Monitoring & Incident Response**: You can't stop what you can't see.
    -   **Audit Everything**: Log all security-relevant events (auth attempts, permission changes, data access) to a central, tamper-evident SIEM.
    -   **Detect**: Use a combination of signature-based rules, anomaly detection, and threat intelligence to detect indicators of compromise.
    -   **Respond**: Have documented, playbook-driven incident response plans. Automate where possible with a SOAR.
    -   **Practice**: Conduct regular tabletop exercises and "game days" to test your response capabilities.
    -   **Learn**: Conduct blameless post-mortems after every incident to identify and fix the systemic root cause.

---

## Appendices & Resources

*(This section would contain the incredibly detailed content from the original document, now framed as reference material.)*

-   **Appendix A: Detailed Implementation Guides**: The full, unabridged text for all 18 original principles.
-   **Appendix B: Tool Ecosystem Map**: A comprehensive mapping of principles to open-source and commercial tools.
-   **Appendix C: Implementation Checklists**: Actionable checklists for all 18 original principles.
-   **Appendix D: Security Maturity Model**: A guide for assessing your organization's current state and planning for the future.
-   **Appendix E: Organizational Enablement**: Guidance on culture, training, and executive sponsorship.
-   **Appendix F: Learning Paths**: 30-day, 3-month, and 1-day learning plans.
-   **Appendix G: Modern Architecture Considerations**: Security for microservices, serverless, and cloud-native environments.
-   **Appendix H: Compliance Mapping**: Mapping principles to OWASP, NIST, CIS, ISO 27001, and other frameworks.
-   **Appendix I: Common Anti-Patterns**: A detailed look at common security failures.
-   **Appendix J: Trade-offs & Resolution Patterns**: Practical advice for resolving common security conflicts.
