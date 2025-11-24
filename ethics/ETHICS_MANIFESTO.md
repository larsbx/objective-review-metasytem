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

> This manifesto provides a structured, quantified framework for making ethical engineering decisions. It prioritizes long-term system health and human well-being over short-term efficiency gains, using a weighted system to provide clear, actionable guidance and prevent common anti-patterns like burnout and technical debt.

---

## The Core Principle

**Long-term sustainability must not be sacrificed for short-term efficiency.**

The framework is built on five objectives, ordered by importance. This hierarchy is enforced by a weighted scoring system, creating mathematical "firebreaks" that prevent lower-priority gains from justifying higher-priority harms.

---

## The Five Objectives (In Order of Priority)

### 1. System Integrity — Weight: 5x
**The system must be secure, correct, and reliable.**
This is the highest priority. It covers the system's truthfulness and its resilience against corruption and attack.
-   **Core Concerns**: Security, Correctness, Reliability, Data Integrity.

### 2. Human Sustainability — Weight: 4x
**The system must not harm the people who build or use it.**
This protects both developers and end-users from physical, mental, or social harm.
-   **Core Concerns**: User Safety, Developer Wellbeing, Accessibility, Privacy, Fairness.

### 3. Knowledge Capital — Weight: 3x
**The system must be understandable and maintainable.**
This covers the preservation and clarity of the knowledge required to operate and evolve the system.
-   **Core Concerns**: Documentation, Code Clarity, Specification, Explainability.

### 4. System Longevity — Weight: 2x
**The system must be built to last and evolve.**
This objective ensures the codebase can be passed on to future generations of developers.
-   **Core Concerns**: Maintainability, Testability, Disaster Recovery, Portability.

### 5. Resource Efficiency — Weight: 1x
**The system should use resources (time, money, compute) wisely.**
This is the **lowest priority**. Efficiency is important, but gains here can *never* justify harm to a higher-level objective.
-   **Core Concerns**: Development Speed, Cloud Costs, Performance.

---

## The Decision Engine

Every proposed action is evaluated by scoring its impact on each of the five objectives.

**`Total Score = Σ (Impact × Weight)`**

-   **Impact**: A score from -3 (strong negative impact) to +3 (strong positive impact).
-   **Weight**: The 5x-4x-3x-2x-1x multiplier for each objective.

The mathematical hierarchy ensures that a minor harm to a major objective (e.g., -1 to System Integrity = -5 points) will always outweigh a major gain to a minor one (e.g., +3 to Resource Efficiency = +3 points).

### Decision Thresholds

-   **✅ Proceed (Score ≥ +3)**: The decision is ethically sound.
-   **⚠️ Proceed with Conditions (-2 ≤ Score < +3)**: The decision involves acceptable trade-offs, but requires a documented "payback plan."
-   **🛑 Reject (Score < -2)**: The decision is harmful and must not be executed.

---

## The Scoring Process & Preventing Gaming

The framework's integrity depends on honest and consistent scoring. While the `Impact` score is inherently subjective, the following process is designed to add rigor, foster discussion, and prevent individuals from "gaming the system" to achieve a desired outcome.

### 1. The Scoring Rubric

Use these concrete examples to anchor your impact scores. A score should be justifiable based on this rubric.

| Score | System Integrity (5x) | Human Sustainability (4x) | Knowledge Capital (3x) | System Longevity (2x) | Resource Efficiency (1x) |
| :---: | ---------------------- | ------------------------- | ---------------------- | --------------------- | ------------------------ |
| **+3** | Fixes a critical CVE. | Ships a major accessibility feature. | Creates comprehensive, interactive documentation for a whole system. | Creates a fully automated CI/CD pipeline from scratch. | Reduces annual cloud bill by >20%. |
| **+2** | Adds encryption to a new feature. | Improves performance to eliminate user frustration. | Documents a complex, core component. | Adds 80% test coverage to a legacy module. | Ships a major feature two weeks early. |
| **+1** | Refactors code to be more secure. | Improves an error message. | Adds clarifying comments to a confusing function. | Fixes a flaky test. | Optimizes a single slow database query. |
| **0** | No impact. | No impact. | No impact. | No impact. | No impact. |
| **-1** | Introduces a low-severity security risk. | A confusing UI that causes minor user frustration. | A code change without corresponding documentation updates. | A temporary workaround without a cleanup ticket. | A feature that is slightly over-engineered. |
| **-2** | Skips security review for a feature. | A new feature is not accessible to screen readers. | A major architectural change is made without an ADR. | Test coverage drops significantly. | A choice that doubles server costs for a minor feature. |
| **-3** | Ships with a known critical vulnerability. | Introduces a dark pattern or requires mandatory crunch time. | "Black box" AI for a critical system is deployed without explainability. | A manual deployment that breaks production and has no rollback plan. | An approach that is 10x more expensive for no user benefit. |

### 2. The Review Process: Objective Guardians

No major decision should be scored in a vacuum. For any proposed action that scores a **-2 or -3 in any objective**, the decision must be reviewed and approved by a designated **Guardian** for that objective.

-   **System Integrity Guardian** (e.g., Principal Security Engineer, Staff Engineer): Reviews any decision that significantly harms security, correctness, or reliability.
-   **Human Sustainability Guardian** (e.g., UX Lead, Accessibility Specialist): Reviews decisions impacting user well-being (accessibility, privacy, ethics) or team health (burnout).
-   **Knowledge Capital Guardian** (e.g., Tech Lead, Documentation Lead): Reviews decisions that harm system understandability.
-   **System Longevity Guardian** (e.g., SRE Lead, Architect): Reviews decisions that create significant technical debt or risk to future development.

This "council of guardians" provides a human check-and-balance, ensuring that scores are not being manipulated and that high-priority harms are given the weight they deserve. The approval of the relevant Guardian must be documented in the ADR or ticket.

---

## Domain Mappings: A Catalog of Ethical Practices

This section provides a non-exhaustive catalog of common engineering practices, classified by their ethical standing within the framework. Use this as a starting point for applying the principles.

### Ethical Categories
-   **🔴 Required**: Mandatory practices. Omitting them causes direct harm and violates core objectives.
-   **🟡 Recommended**: Best practices that should be the default. Omitting them creates risk and technical debt.
-   **🟢 Discretionary**: Context-dependent practices that are ethically neutral on their own.
-   **🟠 Discouraged**: Anti-patterns that should be avoided unless there is strong justification.
-   **❌ Forbidden**: Practices that cause direct, unambiguous harm and must never be done.

---

### Domain 1: Security & Reliability
*(Primarily serves: System Integrity)*

-   **🔴 Required**:
    -   **Encryption at Rest and in Transit**: Protects data confidentiality. (Score: `+10`)
    -   **Access Control (Least Privilege)**: Prevents unauthorized actions. (Score: `+10`)
    -   **Input Validation & Output Encoding**: Prevents injection attacks. (Score: `+5`)
    -   **Critical Vulnerability (CVE) Remediation**: Patching known, critical exploits within a strict SLA (e.g., 24 hours). (Score: `+10`)
-   **❌ Forbidden**:
    -   **Hardcoded Secrets**: Committing credentials to version control. (Score: `-15`)
    -   **Ignoring Critical CVEs**: Knowingly shipping vulnerable code. (Score: `-15`)
    -   **Deceptive "Dark Patterns"**: UI designed to trick users. (Score: `-18`)
    -   **Storing Plaintext Passwords**: Gross negligence. (Score: `-15`)

### Domain 2: DevOps & Infrastructure
*(Primarily serves: System Longevity, System Integrity)*

-   **🟡 Recommended**:
    -   **Immutable Infrastructure**: Replace servers, don't patch them. (Score: `+7`)
    -   **Comprehensive CI/CD Automation**: Removes human error from deployments. (Score: `+7`)
    -   **Disaster Recovery Drills**: Ensure backups are working and the system is recoverable. (Score: `+7`)
    -   **Infrastructure as Code (IaC)**: Version-controlled, auditable infrastructure. (Score: `+5`)
-   **🟠 Discouraged**:
    -   **Manual Deployments**: Creates "snowflake" servers and configuration drift. (Score: `-7`)
    -   **In-place Server Patching**: Leads to un-reproducible environments. (Score: `-4`)
    -   **No Monitoring**: Deploying without observability is deploying blind. (Score: `-5`)

### Domain 3: Product, UX & HR
*(Primarily serves: Human Sustainability)*

-   **🔴 Required**:
    -   **Accessibility (WCAG 2.1 AA)**: Ensures the product is usable by people with disabilities. (Score: `+8`)
    -   **Privacy Compliance (GDPR/CCPA)**: Protects user data rights. (Score: `+13`)
    -   **Sustainable Pace**: Rejecting crunch culture and burnout. (Score: `+8` for protecting, `-12` for violating)
-   **❌ Forbidden**:
    -   **Addictive or Manipulative Mechanics**: Algorithms designed to exploit psychological vulnerabilities (e.g., infinite scroll, FOMO notifications). (Score: `-12`)
    -   **Selling User Data without Explicit Consent**: A fundamental violation of trust. (Score: `-12`)
    -   **Mandatory, Uncompensated Crunch Time**: Exploitative and harmful. (Score: `-12`)

### Domain 4: Software Architecture
*(Primarily serves: Knowledge Capital, System Longevity)*

-   **🟡 Recommended**:
    -   **Domain-Driven Design (DDD)**: Aligning code with the business domain to improve clarity. (Score: `+5`)
    -   **Architecture Decision Records (ADRs)**: Documenting the "why" behind major decisions. (Score: `+6`)
    -   **Explicit API Contracts**: Using standards like OpenAPI to ensure clarity. (Score: `+8`)
-   **🟠 Discouraged**:
    -   **"God Objects"**: Large, complex classes/modules that are difficult to understand and maintain. (Score: `-10`)
    -   **Premature Microservices**: Introducing distributed complexity before it's needed. (Score: `-7`)
    -   **"Clever" Code**: Code that is hard to read and understand, optimized for novelty over clarity. (Score: `-7`)

### Domain 5: Data Science & AI
*(Primarily serves: System Integrity, Human Sustainability)*

-   **🔴 Required**:
    -   **Bias Audits**: Ensuring models do not discriminate against protected groups. (Score: `+14`)
    -   **Explainability & Human Oversight**: For any life-altering decision (hiring, loans, legal), the AI's reasoning must be understandable and subject to human review. (Score: `+10`)
-   **❌ Forbidden**:
    -   **"Black Box" Authoritarianism**: Using an unexplainable model to make consequential decisions without a path for human appeal. (Score: `-27`)
    -   **Training on known-biased data** without clear mitigation strategies. (Score: `-10`)

---

## Integration and Further Reading

This framework is the ethical engine for decision-making. For detailed implementation of the practices listed above, refer to the other manifestos:
-   **For Security**: See the *Security Hardening Manifesto*.
-   **For Code Quality**: See the *Vibe Coding Manifesto*.
-   **For Product & UX**: See the *User Experience* and *Accessibility* Manifestos.
-   **For High-Assurance Systems**: See the *Formal Verification Manifesto*.

### Framework Origins
This framework is a technical adaptation of the principles found in the *Maqasid al-Shariah* (the objectives of Islamic higher purpose). The hierarchical structure and the five core objectives are directly mapped to modern software engineering concerns. We acknowledge this intellectual heritage as a robust and time-tested system of ethical reasoning.

---

## FAQ

**Q: What prevents a team from just "gaming" the scores to get the result they want?**

A: This is a critical question. The framework prevents this in three ways:
1.  **Detailed Scoring Rubric**: The scoring rubric provides concrete examples for each impact level, making it harder to justify an inaccurate score in good faith.
2.  **Written Justification**: Scores should be documented in an ADR, forcing the rationale to be explicit and open to challenge.
3.  **The Guardian Process**: The requirement for a designated "Guardian" to approve any significant negative impact on a high-priority objective creates a human check-and-balance. A security guardian is unlikely to approve a decision that scores a `-3` on System Integrity, regardless of the claimed efficiency benefits.

**Q: Isn't this too rigid for agile development?**

A: No. The framework is designed for agility. The `:proceed_with_conditions` outcome explicitly allows for incurring technical debt to meet urgent needs, as long as a concrete "payback plan" is documented and tracked. It prevents *unmanaged* debt and permanent harm, not temporary trade-offs.

**Q: Where do the weights (5x, 4x, etc.) come from?**

A: The weights are the core of the framework's philosophy. They assert an opinionated, hierarchical view of what matters: a secure and working system (Integrity) that doesn't harm people (Sustainability) is fundamentally more important than one that is merely cheap to run (Efficiency). The specific values are chosen to create "firebreaks" between the layers.
