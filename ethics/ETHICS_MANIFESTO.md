---
id: "ethics"
title: "The Quantified Ethics Manifesto"
version: "2.1"
status: "current"
focus: "A structured, quantified framework for making ethical engineering decisions"
primary_users: ["all-developers", "engineering-managers", "product-managers", "ai-agents"]
learning_curve: "low"
roi_timeline: "immediate"
adoption_scope: "universal"
principles_count: 5
tier_structure:
  core: 5
  standard: 0
  excellence: 0
applicability:
  project_types: ["all"]
  languages: ["all"]
  contexts: ["all"]
related_manifestos:
  complements: ["all"]
  prerequisites: []
  enables: ["decision-making", "trade-off-analysis", "ethical-guardrails"]
tools:
  categories: ["ci-cd-bots", "adr-templates", "feature-flag-rules"]
  count: 5+
measurement:
  system_integrity:
    cve_closure_time: "<7 days"
    security_incidents: "0 critical"
    uptime: "≥99.9%"
  human_sustainability:
    team_burnout_rate: "<5% annually"
    overtime_hours: "<5 hr/week avg"
    user_trust_score: "≥8"
  knowledge_capital:
    documentation_coverage: "≥80%"
    onboarding_time: "<2 weeks"
  system_longevity:
    test_coverage: "≥85%"
    mean_time_to_recover: "<1 hour"
  resource_efficiency:
    cost_per_transaction: "trend down"
    cycle_time: "trend down"
---
# The Quantified Ethics Manifesto: A Structured Decision Framework

**Version**: 2.1
**Last Updated**: 2025-11-23

> This manifesto provides a structured, quantified framework for making ethical engineering decisions. It prioritizes long-term system health and human well-being over short-term efficiency gains.

---

## The Core Principle

**Long-term sustainability must not be sacrificed for short-term efficiency.**

The framework is built on five objectives, ordered by importance:
1.  **System Integrity** (Weight: 5x): Security, Correctness, Reliability.
2.  **Human Sustainability** (Weight: 4x): User Safety, Wellbeing, Privacy.
3.  **Knowledge Capital** (Weight: 3x): Documentation, Understandability.
4.  **System Longevity** (Weight: 2x): Maintainability, Testability.
5.  **Resource Efficiency** (Weight: 1x): Speed, Cost.

---

## The 5 Rulings

This section categorizes engineering practices based on their ethical impact and alignment with the five objectives.

### OBLIGATORY (Required)
**Mandatory practices. Omitting them causes direct harm and violates core objectives.**

-   **Encryption at Rest and in Transit**: Protects data confidentiality. (Score: `+10`)
-   **Access Control (Least Privilege)**: Prevents unauthorized actions. (Score: `+10`)
-   **Input Validation & Output Encoding**: Prevents injection attacks. (Score: `+5`)
-   **Critical Vulnerability (CVE) Remediation**: Patching known, critical exploits within a strict SLA (e.g., 24 hours). (Score: `+10`)
-   **Accessibility (WCAG 2.1 AA)**: Ensures the product is usable by people with disabilities. (Score: `+8`)
-   **Privacy Compliance (GDPR/CCPA)**: Protects user data rights. (Score: `+13`)
-   **Sustainable Pace**: Rejecting crunch culture and burnout. (Score: `+8`)
-   **Bias Audits**: Ensuring models do not discriminate against protected groups. (Score: `+14`)
-   **Explainability & Human Oversight**: For any life-altering decision, the AI's reasoning must be understandable and subject to review. (Score: `+10`)

### ENCOURAGED (Recommended)
**Best practices that should be the default. Omitting them creates risk and technical debt.**

-   **Immutable Infrastructure**: Replace servers, don't patch them. (Score: `+7`)
-   **Comprehensive CI/CD Automation**: Removes human error from deployments. (Score: `+7`)
-   **Disaster Recovery Drills**: Ensure backups are working and the system is recoverable. (Score: `+7`)
-   **Infrastructure as Code (IaC)**: Version-controlled, auditable infrastructure. (Score: `+5`)
-   **Domain-Driven Design (DDD)**: Aligning code with the business domain to improve clarity. (Score: `+5`)
-   **Architecture Decision Records (ADRs)**: Documenting the "why" behind major decisions. (Score: `+6`)
-   **Explicit API Contracts**: Using standards like OpenAPI to ensure clarity. (Score: `+8`)

### OPTIONAL (Discretionary)
**Context-dependent practices that are ethically neutral on their own.**

-   Specific technology choices (e.g., React vs. Vue).
-   Aesthetic choices not impacting accessibility.
-   Experimental features (behind flags).

### DISCOURAGED (Anti-Patterns)
**Practices that should be avoided unless there is strong justification.**

-   **Manual Deployments**: Creates "snowflake" servers and configuration drift. (Score: `-7`)
-   **In-place Server Patching**: Leads to un-reproducible environments. (Score: `-4`)
-   **No Monitoring**: Deploying without observability is deploying blind. (Score: `-5`)
-   **"God Objects"**: Large, complex classes/modules that are difficult to understand and maintain. (Score: `-10`)
-   **Premature Microservices**: Introducing distributed complexity before it's needed. (Score: `-7`)
-   **"Clever" Code**: Code that is hard to read and understand. (Score: `-7`)

### PROHIBITED (Forbidden)
**Practices that cause direct, unambiguous harm and must never be done.**

-   **Hardcoded Secrets**: Committing credentials to version control. (Score: `-15`)
-   **Ignoring Critical CVEs**: Knowingly shipping vulnerable code. (Score: `-15`)
-   **Deceptive "Dark Patterns"**: UI designed to trick users. (Score: `-18`)
-   **Storing Plaintext Passwords**: Gross negligence. (Score: `-15`)
-   **Addictive or Manipulative Mechanics**: Algorithms designed to exploit psychological vulnerabilities. (Score: `-12`)
-   **Selling User Data without Explicit Consent**: A fundamental violation of trust. (Score: `-12`)
-   **Mandatory, Uncompensated Crunch Time**: Exploitative and harmful. (Score: `-12`)
-   **"Black Box" Authoritarianism**: Using an unexplainable model to make consequential decisions without appeal. (Score: `-27`)
-   **Training on known-biased data** without clear mitigation strategies. (Score: `-10`)

---

## FAQ & Process

**The Decision Engine**: Every action is evaluated by `Σ (Impact × Weight)`.
-   **✅ Proceed**: Score ≥ +3
-   **⚠️ Proceed with Conditions**: -2 ≤ Score < +3 (Requires "payback plan")
-   **🛑 Reject**: Score < -2 (Requires Guardian approval to override, generally forbidden)

**Guardians**: High-risk decisions (Score < -2) must be approved by a designated Guardian (e.g., Security Lead for integrity risks).
