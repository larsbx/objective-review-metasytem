Human note: These are for coding agents mostly.

# Code Review Manifestos

A curated collection of software engineering manifestos covering formal verification, coding practices, data analytics, and user experience design. These documents establish foundational principles for building reliable, maintainable, and high-quality software systems.

## Overview

This repository organizes manifestos by domain, each containing comprehensive principles and practical guidance for software engineering excellence. Four manifestos cover the critical dimensions of software development: correctness (Formal Verification), maintainability (Vibe Coding), data reliability (Data & Analytics), and user success (User Experience).

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

### 🎨 [User Experience](./user_experience/)

**[UX Manifesto](./user_experience/UX_MANIFESTO.md)** (v2.0) | [Changelog](./user_experience/CHANGELOG.md)

17 foundational principles for designing clear, accessible, and ethical user interfaces across all platforms.

**Key Principles:**
- User Primacy
- Clarity Over Cleverness
- Progressive Disclosure
- Consistency & Coherence
- Accessibility as Foundation
- Immediate Feedback
- Forgiveness & Reversibility
- Recognition Over Recall
- Efficiency & Flow
- Appropriate Defaults
- Contextual Relevance
- Error Prevention
- Privacy & Ethical Design
- Navigation & Findability
- Aesthetic Integrity
- Performance as Feature
- Continuous Validation

**Principle Hierarchy:**
- **Core** (Non-negotiable): User Primacy, Clarity, Progressive Disclosure, Consistency, Accessibility
- **Standard** (Production-required): Feedback, Forgiveness, Recognition, Efficiency, Defaults, Context, Error Prevention, Privacy, Navigation
- **Excellence** (Differentiation): Aesthetic Integrity, Performance, Continuous Validation

**Best For:**
- Web and mobile applications
- Voice interfaces and conversational UI
- AR/VR and spatial computing
- IoT devices and embedded systems
- Design systems and component libraries
- Multimodal interfaces

**Coverage:** Nielsen heuristics, WCAG 2.1 AA, Core Web Vitals, privacy-by-design, multimodal interactions

---

## Comparison Matrix

| Aspect | Formal Verification | Vibe Coding | Data & Analytics | User Experience |
|--------|-------------------|-------------|------------------|-----------------|
| **Primary Goal** | Mathematical correctness | Human readability | Data reliability | User success |
| **Verification** | Formal proofs | Code review + tests | Data quality tests | Usability testing + analytics |
| **Automation** | Theorem provers, SMT | Linters, formatters | Observability, monitoring | A11y tools, analytics, A/B testing |
| **Learning Curve** | Very High | Medium | Medium-High | Medium |
| **Industry Adoption** | Specialized (safety-critical) | Universal | Data-intensive orgs | Universal (product-focused) |
| **ROI Timeline** | Long-term | Immediate | Medium-term | Immediate-Medium |
| **Key Stakeholders** | Safety engineers, researchers | All developers | Data engineers, analysts | Designers, PMs, frontend devs |

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

**Expand to:**
- **UX Manifesto** (if building user-facing products)
- **Data & Analytics** (if working with data pipelines/platforms)
- **Formal Verification** (if in safety/security-critical systems)

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
- **Safety-critical**: Prioritize Formal Verification Manifesto
- **Data-intensive**: Prioritize Data & Analytics Manifesto
- **User-facing products**: Prioritize UX Manifesto + Vibe Coding
- **General software**: Prioritize Vibe Coding Manifesto

**Federated Adoption:**
- Platform teams: All manifestos (infrastructure criticality)
- Product/Frontend teams: UX Manifesto + Vibe Coding
- Data teams: Data & Analytics + Vibe Coding
- Safety-critical teams: Formal Verification + Vibe Coding

## Implementation Checklists

Each manifesto includes detailed implementation guidance:

- **Formal Verification**: Learning paths (30-day quickstart, 3-month deep dive), decision tree for tool selection, cost-benefit analysis
- **Vibe Coding**: Incremental adoption strategy (3 phases), language-specific guidance, metrics & measurement
- **Data & Analytics**: Implementation checklist per principle, maturity model (6 levels), tool ecosystem map
- **User Experience**: Implementation hierarchy (Core/Standard/Excellence), role-based ownership, measurement framework with specific KPIs

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
| User Experience | 2.0 | 2025-11-20 |

---

**Repository maintained as part of code review best practices initiative.**

For questions or discussions, please open an issue.
