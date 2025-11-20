Human note: These are for coding agents mostly.

# Code Review Manifestos

**A reference index of software engineering manifestos for reliable, maintainable, high-quality systems**

---

## Table of Contents

- [Quick Selection Guide](#quick-selection-guide)
- [Manifesto Index](#manifesto-index)
  - [🔬 Formal Verification](#-formal-verification)
  - [✨ Vibe Coding](#-vibe-coding)
  - [📊 Data & Analytics](#-data--analytics)
  - [🎨 User Experience](#-user-experience)
- [Comparison Matrix](#comparison-matrix)
- [Selection by Role](#selection-by-role)
- [Selection by Context](#selection-by-context)
- [Implementation Quick Reference](#implementation-quick-reference)
- [Common Themes](#common-themes)
- [Adoption Timeline](#adoption-timeline)
- [Version Information](#version-information)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Selection Guide

**Choose manifestos based on your primary concern:**

| If your priority is... | Start with | Also consider |
|------------------------|-----------|---------------|
| **Code correctness & safety** | 🔬 Formal Verification | ✨ Vibe Coding |
| **Code readability & maintainability** | ✨ Vibe Coding | 🎨 UX (if frontend) |
| **Data reliability & quality** | 📊 Data & Analytics | ✨ Vibe Coding |
| **User satisfaction & usability** | 🎨 User Experience | ✨ Vibe Coding |
| **General software quality** | ✨ Vibe Coding | Context-dependent |

---

## Manifesto Index

### 🔬 Formal Verification

**[Formal Verification Manifesto](./formal_verification/FORMAL_VERIFICATION_MANIFESTO.md)** • v1.1 • 16 principles

#### At a Glance
- **Goal**: Mathematical correctness proofs
- **Primary Users**: Safety engineers, security researchers
- **Learning Curve**: Very High
- **ROI**: Long-term
- **Adoption**: Specialized (safety/security-critical)

#### Key Principles
- Specification as Foundation
- Types as Propositions (Curry-Howard)
- Totality & Termination
- Refinement Types
- Separation Logic
- Proof Automation
- Verified Compilation
- Incremental Formalization

#### Best Fit
- ✅ Safety-critical systems (avionics, medical, automotive)
- ✅ Security-critical components (cryptography, authentication)
- ✅ High-assurance software requiring mathematical proofs

#### Tools & Ecosystem
Coq • Isabelle • Lean • Agda • F* • Dafny • TLA+ • SPARK Ada

#### Implementation Guide
- 30-day quickstart path
- 3-month deep dive
- Tool selection decision tree
- Cost-benefit analysis framework

---

### ✨ Vibe Coding

**[Vibe Coding Manifesto](./vibe_coding/VIBE_CODING_MANIFESTO.md)** • v2.0 • [Changelog](./vibe_coding/CHANGELOG.md) • 15 principles

#### At a Glance
- **Goal**: Human readability & maintainability
- **Primary Users**: All developers
- **Learning Curve**: Medium
- **ROI**: Immediate
- **Adoption**: Universal

#### Key Principles (by tier)

**Core** (Universal - Start Here):
- Aesthetic Legibility
- Intentional Naming
- Literate Programming
- Obviousness Over Cleverness
- Locality & Cohesion

**Intermediate** (Language-Dependent):
- Semantic Density
- Immutability Default
- Contextual Verbosity
- Joyful Craft

**Advanced** (Requires Strong Types):
- Type as Documentation
- Composition Over Configuration
- Error as Value
- Constraint Propagation

#### Best Fit
- ✅ Long-lived production systems (10+ year horizon)
- ✅ Teams valuing correctness & maintainability
- ✅ Complex business logic domains
- ✅ Libraries and frameworks

#### Languages Covered
Python • TypeScript • Rust • Go • Haskell • Java

#### Implementation Guide
- 3-phase incremental adoption (weeks 1-2, months 1-2, months 3-6)
- Language-specific guidance
- Metrics & measurement framework
- Code review checklists

---

### 📊 Data & Analytics

**[Data & Analytics Manifesto](./data_analytics/DATA_ANALYTICS_MANIFESTO.md)** • v2.0 • [Changelog](./data_analytics/CHANGELOG.md) • 18 principles

#### At a Glance
- **Goal**: Data reliability & scalability
- **Primary Users**: Data engineers, analysts
- **Learning Curve**: Medium-High
- **ROI**: Medium-term
- **Adoption**: Data-intensive organizations

#### Key Principles
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

#### Best Fit
- ✅ Data warehouses & analytics platforms
- ✅ Data pipelines (batch and streaming)
- ✅ Business intelligence systems
- ✅ Machine learning platforms
- ✅ Data mesh architectures

#### Tools & Ecosystem
dbt • Airflow • Snowflake • BigQuery • Spark • Kafka • Great Expectations • Amundsen

#### Implementation Guide
- Per-principle implementation checklist
- 6-level maturity model
- Tool ecosystem map
- Cost optimization framework

---

### 🎨 User Experience

**[UX Manifesto](./user_experience/UX_MANIFESTO.md)** • v2.0 • [Changelog](./user_experience/CHANGELOG.md) • 17 principles

#### At a Glance
- **Goal**: User success & satisfaction
- **Primary Users**: Designers, PMs, frontend developers
- **Learning Curve**: Medium
- **ROI**: Immediate-Medium
- **Adoption**: Universal (product-focused)

#### Key Principles (by tier)

**Core** (Non-negotiable):
- User Primacy
- Clarity Over Cleverness
- Progressive Disclosure
- Consistency & Coherence
- Accessibility as Foundation

**Standard** (Production-required):
- Immediate Feedback
- Forgiveness & Reversibility
- Recognition Over Recall
- Efficiency & Flow
- Appropriate Defaults
- Contextual Relevance
- Error Prevention
- Privacy & Ethical Design
- Navigation & Findability

**Excellence** (Differentiation):
- Aesthetic Integrity
- Performance as Feature
- Continuous Validation

#### Best Fit
- ✅ Web & mobile applications
- ✅ Voice interfaces & conversational UI
- ✅ AR/VR & spatial computing
- ✅ IoT devices & embedded systems
- ✅ Design systems & component libraries
- ✅ Multimodal interfaces

#### Standards & Coverage
Nielsen Heuristics • WCAG 2.1 AA • Core Web Vitals • Privacy-by-Design

#### Implementation Guide
- Core/Standard/Excellence implementation hierarchy
- Role-based ownership matrix
- Measurement framework with KPIs
- Conflict resolution framework

---

## Comparison Matrix

| Aspect | 🔬 Formal Verification | ✨ Vibe Coding | 📊 Data & Analytics | 🎨 User Experience |
|--------|----------------------|---------------|--------------------|--------------------|
| **Focus** | Mathematical correctness | Human readability | Data reliability | User success |
| **Verification Method** | Formal proofs | Code review + tests | Data quality tests | Usability testing + analytics |
| **Automation Tools** | Theorem provers, SMT solvers | Linters, formatters | Observability, monitoring | A11y tools, analytics, A/B |
| **Learning Curve** | ⚠️ Very High | ✓ Medium | ⚠️ Medium-High | ✓ Medium |
| **Adoption Scope** | Specialized | ✓ Universal | Data-intensive | ✓ Universal |
| **ROI Timeline** | Long-term (years) | ✓ Immediate | Medium (months) | ✓ Immediate-Medium |
| **Team Size Impact** | High (specialist knowledge) | Low (general practice) | Medium (platform teams) | Low-Medium (designers) |

---

## Selection by Role

### Developers (Backend/Fullstack)
1. **Start**: ✨ Vibe Coding (Core principles)
2. **Add**: 📊 Data & Analytics (if data-heavy) OR 🎨 UX (if user-facing)
3. **Consider**: 🔬 Formal Verification (for critical components)

### Frontend Developers
1. **Start**: 🎨 User Experience + ✨ Vibe Coding
2. **Priority**: Accessibility (VIII), Performance (XIV), Consistency (IV)

### Data Engineers / Analysts
1. **Start**: 📊 Data & Analytics
2. **Add**: ✨ Vibe Coding (pipeline code quality)
3. **Focus**: Data Quality, Lineage, Observability

### Designers / Product Managers
1. **Start**: 🎨 User Experience
2. **Priority**: User Primacy (I), Accessibility (VIII), Continuous Validation (XV)
3. **Consider**: ✨ Vibe Coding (understand engineering constraints)

### Platform / Infrastructure Engineers
1. **Start**: ✨ Vibe Coding
2. **Add**: 📊 Data & Analytics (observability) + 🔬 Formal Verification (critical paths)
3. **Priority**: All manifestos relevant due to infrastructure criticality

### Security Engineers
1. **Start**: 🔬 Formal Verification
2. **Add**: ✨ Vibe Coding + 🎨 UX (Privacy & Ethics principle)
3. **Focus**: Cryptography verification, secure-by-design

---

## Selection by Context

### Project Type

| Project Type | Primary | Secondary | Notes |
|--------------|---------|-----------|-------|
| **Web Application** | 🎨 UX | ✨ Vibe Coding | Add 📊 if data-heavy |
| **Mobile App** | 🎨 UX | ✨ Vibe Coding | Performance & accessibility critical |
| **API / Backend Service** | ✨ Vibe Coding | 📊 Data (if stateful) | Consider 🔬 for auth/payments |
| **Data Pipeline** | 📊 Data & Analytics | ✨ Vibe Coding | Quality & observability paramount |
| **ML Platform** | 📊 Data & Analytics | ✨ Vibe Coding | Reproducibility & lineage critical |
| **IoT / Embedded** | 🎨 UX | 🔬 Formal Verification | Safety + usability constraints |
| **Financial System** | 🔬 Formal Verification | 📊 Data + ✨ Vibe | Correctness & auditability |
| **Medical Device** | 🔬 Formal Verification | 🎨 UX | Safety + human factors |
| **Design System** | 🎨 UX | ✨ Vibe Coding | Consistency & documentation |
| **CLI Tool** | ✨ Vibe Coding | 🎨 UX | Clarity & error messages |

### Organizational Maturity

| Stage | Focus | Manifestos | Rationale |
|-------|-------|-----------|-----------|
| **Startup (MVP)** | Speed + UX | 🎨 UX + ✨ Vibe (Core only) | User validation priority |
| **Growth (Scaling)** | Quality + Reliability | ✨ Vibe + 📊 Data | Technical debt prevention |
| **Enterprise (Mature)** | All dimensions | All manifestos | Domain-specific application |
| **Legacy Modernization** | Code quality first | ✨ Vibe Coding | Refactoring foundation |

### Risk Profile

| Risk Level | Manifestos | Priority Principles |
|------------|-----------|---------------------|
| **Critical** (life/finance) | 🔬 Formal Verification + 📊 Data | Correctness proofs, auditability |
| **High** (security/PII) | 🔬 Formal + 🎨 UX (Privacy) | Cryptography, privacy-by-design |
| **Medium** (business-critical) | 📊 Data + ✨ Vibe | Quality, observability, maintainability |
| **Standard** (typical SaaS) | 🎨 UX + ✨ Vibe | User satisfaction, code quality |

---

## Implementation Quick Reference

### Timeline by Manifesto

| Manifesto | Phase 1 | Phase 2 | Phase 3 |
|-----------|---------|---------|---------|
| **🔬 Formal Verification** | 30-day intro (1 component) | 3-month deep dive (module) | 6-12 month (subsystem) |
| **✨ Vibe Coding** | Weeks 1-2 (formatting, naming) | Months 1-2 (immutability, cohesion) | Months 3-6 (types, composition) |
| **📊 Data & Analytics** | Month 1 (observability, SLOs) | Months 2-4 (quality, contracts) | Months 5-12 (lineage, mesh) |
| **🎨 User Experience** | Week 1 (Core: accessibility, clarity) | Months 1-3 (Standard principles) | Ongoing (Excellence: performance, validation) |

### Resources Required

| Manifesto | Team Training | Tool Investment | External Expertise |
|-----------|---------------|-----------------|-------------------|
| 🔬 Formal | ⚠️ High (specialist courses) | Medium (proof assistants) | Often required |
| ✨ Vibe | ✓ Low (internal workshops) | Low (linters, formatters) | Rarely needed |
| 📊 Data | Medium (platform training) | ⚠️ High (platform tools) | Sometimes needed |
| 🎨 UX | Medium (UX research methods) | Medium (testing tools) | Recommended |

### Success Metrics

| Manifesto | Leading Indicators | Lagging Indicators |
|-----------|-------------------|-------------------|
| 🔬 Formal | % code formally verified | Bug density in critical paths |
| ✨ Vibe | Code review approval time | Time to onboard new devs |
| 📊 Data | Data quality test coverage | Data incident frequency |
| 🎨 UX | Usability test pass rate | User satisfaction (NPS/CSAT) |

---

## Common Themes

Cross-cutting philosophy across all manifestos:

| Theme | Application |
|-------|-------------|
| **Quality by Design** | Build in correctness/quality from start, not retrofit |
| **Incremental Adoption** | Progressive enhancement from basic → advanced |
| **Explicit Over Implicit** | Make invariants, contracts, expectations explicit |
| **Automation Matters** | Leverage tooling for enforcement & verification |
| **Cost-Benefit Awareness** | Apply techniques proportional to criticality |
| **Documentation as Code** | Maintain docs alongside implementation |

---

## Adoption Timeline

### Individual Engineer (Self-Directed)

**Week 1**: Read ✨ Vibe Coding (Core principles) + apply to next PR
**Week 2-4**: Add domain manifesto (🔬/📊/🎨 based on context)
**Month 2-3**: Implement intermediate/standard principles
**Month 4-6**: Explore advanced principles, share with team

### Team (Coordinated)

**Month 1-3 (Foundations)**:
- ✨ Vibe Coding: Formatting, naming, documentation standards
- 🎨 UX: Core principles (if user-facing)
- Establish code review culture
- Set up linting & formatting automation

**Month 4-6 (Quality Gates)**:
- ✨ Vibe Coding: Testing philosophy, immutability
- 📊 Data: Quality checks, observability (if applicable)
- 🎨 UX: Standard principles, A11y testing
- Establish SLAs and monitoring

**Month 7-12 (Advanced Techniques)**:
- ✨ Vibe Coding: Type-driven design, advanced patterns
- 📊 Data: Contracts, lineage, cost optimization
- 🎨 UX: Excellence principles, continuous validation
- 🔬 Formal: Consider for critical components

### Organization (Federated)

**Quarter 1**: Pilot team adoption + tooling setup
**Quarter 2**: Expand to similar teams + refine playbooks
**Quarter 3-4**: Org-wide rollout with domain customization
**Ongoing**: Maturity assessment, continuous improvement

---

## Version Information

| Manifesto | Current Version | Last Updated | Status |
|-----------|----------------|--------------|--------|
| 🔬 Formal Verification | v1.1 | 2024 | Stable |
| ✨ Vibe Coding | v2.0 | 2025-11-20 | Current |
| 📊 Data & Analytics | v2.0 | 2025-11-20 | Current |
| 🎨 User Experience | v2.0 | 2025-11-20 | Current |

**Changelog Access**: Each v2.0+ manifesto includes detailed changelog in respective directory.

---

## Contributing

These are living documents. Contributions welcome:

- **Feedback**: [Open issues](../../issues) with suggestions or questions
- **Improvements**: Submit pull requests for clarifications or examples
- **Case Studies**: Share adoption stories and lessons learned
- **Translations**: Help make accessible to global community

**Contribution Guidelines**: See individual manifesto directories for domain-specific guidance.

---

## License

**CC0 - Public Domain**

All manifestos freely available for education, research, and industry use.

---

## Source & Maintenance

**Origin**: Manifestos gathered from larsbx/tui-story repository
**Maintained**: As part of code review best practices initiative
**Questions**: [Open an issue](../../issues) for discussion

---

**Navigation**: [Top ↑](#code-review-manifestos) | [Quick Selection ↑](#quick-selection-guide) | [Comparison ↑](#comparison-matrix)
