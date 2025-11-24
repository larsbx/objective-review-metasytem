# 5 Rulings

This document compiles the rulings from various manifestos within this project, categorizing them into OBLIGATORY, ENCOURAGED, OPTIONAL, DISCOURAGED, and PROHIBITED actions.

---

## The Quantified Ethics Manifesto

### OBLIGATORY
- **Encryption at Rest and in Transit**: Protects data confidentiality. (Score: `+10`)
- **Access Control (Least Privilege)**: Prevents unauthorized actions. (Score: `+10`)
- **Input Validation & Output Encoding**: Prevents injection attacks. (Score: `+5`)
- **Critical Vulnerability (CVE) Remediation**: Patching known, critical exploits within a strict SLA (e.g., 24 hours). (Score: `+10`)
- **Accessibility (WCAG 2.1 AA)**: Ensures the product is usable by people with disabilities. (Score: `+8`)
- **Privacy Compliance (GDPR/CCPA)**: Protects user data rights. (Score: `+13`)
- **Sustainable Pace**: Rejecting crunch culture and burnout. (Score: `+8` for protecting, `-12` for violating)
- **Bias Audits**: Ensuring models do not discriminate against protected groups. (Score: `+14`)
- **Explainability & Human Oversight**: For any life-altering decision (hiring, loans, legal), the AI's reasoning must be understandable and subject to human review. (Score: `+10`)

### ENCOURAGED
- **Immutable Infrastructure**: Replace servers, don't patch them. (Score: `+7`)
- **Comprehensive CI/CD Automation**: Removes human error from deployments. (Score: `+7`)
- **Disaster Recovery Drills**: Ensure backups are working and the system is recoverable. (Score: `+7`)
- **Infrastructure as Code (IaC)**: Version-controlled, auditable infrastructure. (Score: `+5`)
- **Domain-Driven Design (DDD)**: Aligning code with the business domain to improve clarity. (Score: `+5`)
- **Architecture Decision Records (ADRs)**: Documenting the "why" behind major decisions. (Score: `+6`)
- **Explicit API Contracts**: Using standards like OpenAPI to ensure clarity. (Score: `+8`)

### OPTIONAL
- No specific practices listed.

### DISCOURAGED
- **Manual Deployments**: Creates "snowflake" servers and configuration drift. (Score: `-7`)
- **In-place Server Patching**: Leads to un-reproducible environments. (Score: `-4`)
- **No Monitoring**: Deploying without observability is deploying blind. (Score: `-5`)
- **"God Objects"**: Large, complex classes/modules that are difficult to understand and maintain. (Score: `-10`)
- **Premature Microservices**: Introducing distributed complexity before it's needed. (Score: `-7`)
- **"Clever" Code**: Code that is hard to read and understand, optimized for novelty over clarity. (Score: `-7`)

### PROHIBITED
- **Hardcoded Secrets**: Committing credentials to version control. (Score: `-15`)
- **Ignoring Critical CVEs**: Knowingly shipping vulnerable code. (Score: `-15`)
- **Deceptive "Dark Patterns"**: UI designed to trick users. (Score: `-18`)
- **Storing Plaintext Passwords**: Gross negligence. (Score: `-15`)
- **Addictive or Manipulative Mechanics**: Algorithms designed to exploit psychological vulnerabilities (e.g., infinite scroll, FOMO notifications). (Score: `-12`)
- **Selling User Data without Explicit Consent**: A fundamental violation of trust. (Score: `-12`)
- **Mandatory, Uncompensated Crunch Time**: Exploitative and harmful. (Score: `-12`)
- **"Black Box" Authoritarianism**: Using an unexplainable model to make consequential decisions without a path for human appeal. (Score: `-27`)
- **Training on known-biased data** without clear mitigation strategies. (Score: `-10`)

---