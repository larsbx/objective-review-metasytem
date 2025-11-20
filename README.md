Human note: These are for coding agents mostly.

# Code Review Manifestos

A curated collection of software engineering manifestos covering formal verification, coding practices, data analytics, and security hardening. These documents establish foundational principles for building reliable, maintainable, secure, and high-quality software systems.

## Overview

This repository organizes manifestos by domain, each containing comprehensive principles and practical guidance for software engineering excellence.

## Manifestos

### 🔬 [Formal Verification](./formal_verification/)

**[Formal Verification Manifesto](./formal_verification/FORMAL_VERIFICATION_MANIFESTO.md)** (v1.1)

16 foundational principles for formal methods and verified software development.

**Key Principles:**
- Specification as Foundation
- Types as Propositions (Curry-Howard)
- Totality & Termination
- Refinement Types
- Separation Logic
- Proof Automation
- Verified Compilation
- Incremental Formalization

**Best For:**
- Safety-critical systems (avionics, medical, automotive)
- Security-critical components (cryptography, authentication)
- High-assurance software requiring mathematical correctness proofs

**Tools Covered:** Coq, Isabelle, Lean, Agda, F*, Dafny, TLA+, SPARK Ada

---

### ✨ [Vibe Coding](./vibe_coding/)

**[Vibe Coding Manifesto](./vibe_coding/VIBE_CODING_MANIFESTO.md)** (v2.0) | [Changelog](./vibe_coding/CHANGELOG.md)

15 foundational principles for human-centric code that optimizes for readability, maintainability, and joy.

**Key Principles:**
- Aesthetic Legibility
- Intentional Naming
- Literate Programming
- Obviousness Over Cleverness
- Immutability Default
- Type as Documentation
- Error as Value
- Joyful Craft

**Principle Hierarchy:**
- **Core** (Universal): Legibility, Naming, Documentation, Obviousness, Cohesion
- **Intermediate** (Language-Dependent): Density, Immutability, Verbosity
- **Advanced** (Requires Strong Types): Type Systems, Composition, Error Handling

**Best For:**
- Long-lived production systems (10+ year horizon)
- Teams valuing correctness and maintainability
- Complex business logic domains
- Libraries and frameworks

**Languages Covered:** Python, TypeScript, Rust, Go, Haskell, Java

---

### 📊 [Data & Analytics](./data_analytics/)

**[Data & Analytics Manifesto](./data_analytics/DATA_ANALYTICS_MANIFESTO.md)** (v2.0) | [Changelog](./data_analytics/CHANGELOG.md)

18 foundational principles for building reliable, scalable data platforms and analytics systems.

**Key Principles:**
- Data as Product
- Single Source of Truth
- Immutability & Temporal Integrity
- Schema as Contract
- Data Quality by Design
- Lineage & Provenance
- Idempotency & Determinism
- Metrics as Code
- Data Observability
- Privacy & Compliance by Design
- Explicit Data Contracts
- Comprehensive Testing
- Cost-Aware Engineering

**Best For:**
- Data warehouses and analytics platforms
- Data pipelines (batch and streaming)
- Business intelligence systems
- Machine learning platforms
- Data mesh architectures

**Tools Covered:** dbt, Airflow, Snowflake, BigQuery, Spark, Kafka, Great Expectations, Amundsen

---

### 🔒 [Security Hardening](./security_hardening/)

**[Security Hardening Manifesto](./security_hardening/SECURITY_HARDENING_MANIFESTO.md)** (v2.0) | [Changelog](./security_hardening/CHANGELOG.md)

18 foundational principles for building secure, resilient systems.

**Key Principles:**
- Defense in Depth
- Least Privilege
- Fail Secure
- Complete Mediation
- Zero Trust
- Cryptographic Agility
- Secure Development Lifecycle
- Audit Everything
- Secrets Management
- Vulnerability Management
- Immutable Infrastructure
- Threat Modeling
- Supply Chain Security
- Security Monitoring & Incident Response

**Best For:**
- Security-critical applications (fintech, healthcare, government)
- Cloud-native and microservices architectures
- Organizations building security programs
- Compliance-driven environments (PCI-DSS, HIPAA, GDPR)
- DevSecOps transformation

**Standards Covered:** OWASP Top 10, NIST CSF, CIS Controls, ISO 27001, PCI-DSS

---

## Comparison Matrix

| Aspect | Formal Verification | Vibe Coding | Data & Analytics | Security Hardening |
|--------|-------------------|-------------|------------------|-------------------|
| **Primary Goal** | Mathematical correctness | Human readability | Data reliability | System security & resilience |
| **Verification** | Formal proofs | Code review + tests | Data quality tests | Pen testing, audits, scanning |
| **Automation** | Theorem provers, SMT | Linters, formatters | Observability, monitoring | SAST, DAST, SCA, SIEM |
| **Learning Curve** | Very High | Medium | Medium-High | Medium |
| **Industry Adoption** | Specialized (safety-critical) | Universal | Data-intensive orgs | Universal (required) |
| **ROI Timeline** | Long-term | Immediate | Medium-term | Immediate (avoid breach) |
| **Criticality** | Safety-critical systems | All systems | Data-driven systems | All systems |

## Common Themes

Despite different domains, these manifestos share core philosophy:

1. **Quality by Design**: Build correctness/quality into the system, don't bolt it on later
2. **Incremental Adoption**: Progressive enhancement from basic to advanced techniques
3. **Explicit Over Implicit**: Make invariants, contracts, and expectations explicit
4. **Tooling Matters**: Leverage automation for enforcement and verification
5. **Cost-Benefit Awareness**: Apply techniques proportional to criticality
6. **Documentation as Code**: Maintain documentation alongside implementation

## Usage Guidance

### For Individual Engineers

**Start with:** Vibe Coding Manifesto (Core Principles)
- Immediately applicable to daily work
- Language-agnostic fundamentals
- Low barrier to entry

**Expand to:** Data & Analytics (if working with data) or Formal Verification (if in critical systems)

### For Teams

**Phase 1 - Foundations** (Months 1-3):
- Adopt Vibe Coding core principles (formatting, naming, documentation)
- Establish code review culture
- Set up linting and formatting automation

**Phase 2 - Quality Gates** (Months 4-6):
- Add comprehensive testing (Vibe Coding testing philosophy)
- Implement data quality checks (if applicable)
- Establish SLAs and monitoring

**Phase 3 - Advanced Techniques** (Months 7-12):
- Type-driven design (Vibe Coding advanced principles)
- Formal contracts and contracts testing (Data manifesto)
- Consider formal verification for critical components

### For Organizations

**Assess Criticality:**
- **Safety-critical**: Formal Verification + Security Hardening (avionics, medical devices)
- **Security-critical**: Security Hardening + Vibe Coding (fintech, healthcare, government)
- **Data-intensive**: Data & Analytics + Security Hardening (analytics platforms, ML systems)
- **General software**: Vibe Coding + Security Hardening (all applications)

**Federated Adoption:**
- Platform teams: All four manifestos (infrastructure criticality)
- Product teams: Vibe Coding + Security Hardening + domain-specific (Data or Verification)
- Data teams: Data & Analytics + Security Hardening + Vibe Coding
- Security teams: Security Hardening as foundation, expand to domain-specific needs

## Implementation Checklists

Each manifesto includes detailed implementation guidance:

- **Formal Verification**: Learning paths (30-day quickstart, 3-month deep dive), decision tree for tool selection, cost-benefit analysis
- **Vibe Coding**: Incremental adoption strategy (3 phases), language-specific guidance, metrics & measurement
- **Data & Analytics**: Implementation checklist per principle, maturity model (6 levels), tool ecosystem map
- **Security Hardening**: Implementation checklists (18 principles), security maturity model (6 levels), tool ecosystem map (100+ tools), compliance mapping (OWASP, NIST, CIS, ISO 27001), learning paths (30-day to 3-month), modern architecture guidance

## Contributing

These manifestos are living documents. Contributions welcome:

- **Feedback**: Open issues with suggestions or questions
- **Improvements**: Submit pull requests for clarifications or examples
- **Case Studies**: Share adoption stories and lessons learned
- **Translations**: Help make these accessible to global community

## License

All manifestos in this collection: **CC0 - Public Domain**

Use freely for education, research, and industry.

## Source

Manifestos gathered from:
- **larsbx/tui-story** repository

## Version Information

| Manifesto | Version | Last Updated |
|-----------|---------|--------------|
| Formal Verification | 1.1 | 2024 |
| Vibe Coding | 2.0 | 2025-11-20 |
| Data & Analytics | 2.0 | 2025-11-20 |
| Security Hardening | 2.0 | 2025-11-20 |

---

**Repository maintained as part of code review best practices initiative.**

For questions or discussions, please open an issue.
