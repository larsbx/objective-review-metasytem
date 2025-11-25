# Changelog - Content & Communication Manifesto

All notable changes to the Content & Communication Manifesto will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2025-11-20

### Added - Major Expansion
- **Expanded scope**: From "Technical Documentation" to "Content & Communication" covering all content types
- **Tiered structure**: Organized 18 principles into Core/Standard/Excellence tiers
- **At a Glance section**: Quick reference matching other v2.0 manifestos
- **Three new principles**:
  - XVI. Content Governance & Strategy (workflows, ownership, lifecycle management)
  - XVII. Internationalization & Localization (global-ready content, cultural awareness)
  - XI. Voice & Tone Consistency (elevated from corollary to full principle)
- **Content type coverage**:
  - UI/UX content (microcopy, error messages, tooltips, labels)
  - Marketing content (landing pages, emails, product descriptions)
  - Support content (help centers, FAQs, chatbots)
  - Internal content (runbooks, incident reports, specifications)
- **Implementation guide**: Phased adoption (Week 1-2, Month 1-2, Month 3-6, Ongoing)
- **Measurement framework**:
  - Content quality scorecard (Findability, Comprehension, Correctness, Freshness, Accessibility, Efficiency)
  - Content maturity model (5 levels)
  - Success metrics by content type (documentation, UI, marketing, errors, onboarding)
- **Tool ecosystem map**: Comprehensive table with 50+ tools across 15 categories
- **Role-specific guidance**: 8 roles (Technical Writers, Developers, DevRel, UX Writers, PMs, Marketing, Support, Engineering Leaders)
- **Content type decision matrix**: When to use tutorials vs. how-tos vs. reference vs. explanation
- **Anti-patterns section**: Consolidated 18 common anti-patterns with fixes
- **Context-specific examples**: Technical docs, UI microcopy, marketing, error messages for each principle where applicable

### Changed - Restructuring
- **Principle I (Clarity)**: Added context-specific application (technical, UI, marketing)
- **Principle II (Semantic Hierarchy)**: Added UI application guidance
- **Principle III (Precision in Terminology)**: Expanded to cover UI consistency
- **Principle IV (Accessibility)**: Condensed with cross-reference to dedicated Accessibility Manifesto
- **Principle V (Empathy)**: Enhanced with error message framework, inclusive language examples
- **Principle VI (Audience-First)**: Added user journey examples, marketing application
- **Principle VII (Actionable Documentation)**: Integrated Diátaxis framework table
- **Principle VIII (Progressive Disclosure)**: Added UI application examples
- **Principle IX (Scannability)**: Added F-pattern optimization guidance
- **Principle X (Code as Communication)**: Added CI/CD testing example
- **Principle XII (Version Control)**: Added deprecation notice template
- **Principle XIII (Maintenance)**: Added automation workflow example
- **Principle XIV (Visual Communication)**: Added diagram-as-code examples, screenshot best practices
- **Principle XV (Searchability)**: Added internal linking strategy, URL structure guidance

### Enhanced - Quality Improvements
- **Examples**: All principles now have "Anti-pattern vs. ✓" examples
- **Measurement**: Each principle section references relevant metrics
- **Cross-references**: Links to related manifestos (Accessibility, UX)
- **Actionability**: Added checklists, templates, code samples throughout
- **Accessibility**: Enhanced WCAG guidance with quick checklists
- **Internationalization**: New comprehensive i18n/l10n guidance
- **Content governance**: CODEOWNERS examples, lifecycle workflows, review checklists

### Documentation
- Added CHANGELOG.md (this file)
- Created comprehensive README cross-references
- Version information section with standards alignment

---

## [1.0.0] - 2025-11-17 (Initial Draft)

### Added - Initial Release
- **15 foundational principles** for technical documentation:
  - I. Clarity as Prime Directive
  - II. Audience-First Architecture
  - III. Semantic Hierarchy
  - IV. Precision in Terminology
  - V. Actionable Documentation
  - VI. Progressive Disclosure
  - VII. Consistency Across Artifacts
  - VIII. Scannability & Skimming
  - IX. Code as Communication
  - X. Visual Communication
  - XI. Searchability & Discoverability
  - XII. Version Control & Change Management
  - XIII. Accessibility as Requirement
  - XIV. Maintenance & Decay Prevention
  - XV. Empathy & Respect

- **Diátaxis framework integration**: Tutorial, How-To, Reference, Explanation
- **Content quality metrics**: Findability, Comprehension, Correctness, Freshness
- **Writing tools**: Basic prose linting, grammar, readability tools
- **Anti-patterns**: Scattered throughout principles
- **Corollaries**: Metaprinciples and best practices

### Scope
- Focused primarily on **technical documentation** (API docs, guides, tutorials)
- Limited coverage of UI/marketing content
- No formal tiered structure
- Basic tool recommendations

---

## Version Comparison

| Aspect | v1.0 (Initial) | v2.0 (Current) | Change |
|--------|----------------|----------------|--------|
| **Scope** | Technical documentation | All content types | +4 content categories |
| **Principles** | 15 (flat) | 18 (tiered) | +3 principles, hierarchical |
| **Structure** | Linear | Core/Standard/Excellence | Tiered for adoption |
| **Implementation** | Basic | Phased (4 phases) | Detailed timeline |
| **Measurement** | Partial | Comprehensive | Maturity model + scorecard |
| **Tools** | Scattered list (~15) | Ecosystem map (50+) | Organized by category |
| **Roles** | None | 8 roles | Guidance per role |
| **Content Types** | 1 (docs) | 5 (docs, UI, marketing, support, internal) | Multi-touchpoint |
| **Examples** | Code-focused | All content types | Broader application |
| **Cross-references** | None | Accessibility, UX manifestos | Integrated ecosystem |

---

## Migration Guide: v1.0 → v2.0

### Breaking Changes
**None**. v2.0 is **fully backward compatible** with v1.0. All v1.0 principles retained and enhanced.

### New Capabilities
If you implemented v1.0, you can incrementally adopt v2.0:

1. **Week 1**: Review new tiered structure, identify your current maturity level
2. **Week 2**: Add new Principle XI (Voice & Tone) - create voice guide
3. **Month 1**: Implement Principle XVI (Content Governance) - assign ownership
4. **Month 2**: Assess Principle XVII (Internationalization) - needed if global product
5. **Month 3**: Expand scope beyond technical docs to UI/marketing if applicable

### Principle Renumbering
Several principles renumbered due to additions:

| v1.0 Principle | v2.0 Principle | Notes |
|----------------|----------------|-------|
| I. Clarity | I. Clarity | ✓ Same (enhanced) |
| II. Audience-First | VI. Audience-First | Moved to Standard tier |
| III. Semantic Hierarchy | II. Semantic Hierarchy | Promoted to Core tier |
| IV. Precision | III. Precision | Promoted to Core tier |
| V. Actionable Documentation | VII. Actionable Documentation | Enhanced with Diátaxis |
| VI. Progressive Disclosure | VIII. Progressive Disclosure | Enhanced |
| VII. Consistency | XI. Voice & Tone | Expanded and renamed |
| VIII. Scannability | IX. Scannability | ✓ Same (enhanced) |
| IX. Code as Communication | X. Code as Communication | ✓ Same (enhanced) |
| X. Visual Communication | XIV. Visual Communication | Enhanced |
| XI. Searchability | XV. Searchability | Enhanced |
| XII. Version Control | XII. Version Control | ✓ Same (enhanced) |
| XIII. Accessibility | IV. Accessibility | Promoted to Core tier |
| XIV. Maintenance | XIII. Maintenance | ✓ Same (enhanced) |
| XV. Empathy | V. Empathy | Promoted to Core tier |
| *(new)* | XVI. Content Governance | NEW principle |
| *(new)* | XVII. Internationalization | NEW principle |

---

## Upcoming (Planned for v2.1)

### Under Consideration
- [ ] **Principle XIX: AI-Assisted Content** - Using LLMs for drafting, editing, translation
- [ ] **Video content guidelines** - Expanded video/multimedia standards
- [ ] **Content operations playbook** - Detailed workflows, org structures, career ladders
- [ ] **Case studies section** - Real-world adoption stories
- [ ] **Interactive examples** - Embedded code playgrounds, interactive diagrams
- [ ] **Content design patterns library** - Reusable templates for common scenarios
- [ ] **API documentation best practices** - OpenAPI, GraphQL, gRPC specific guidance
- [ ] **Conversational UI guidance** - Chatbots, voice interfaces, AI assistants
- [ ] **Developer portal checklist** - Comprehensive checklist for dev portal quality

### Feedback Requested
We're seeking input on:
- Mobile-first content design (apps, progressive web apps)
- Content for developer tools (CLI, SDKs, libraries)
- Internal documentation (runbooks, incident reports, RFCs)
- AI-generated content quality standards

**Submit feedback**: [Open an issue](../../issues) with your use case.

---

## Standards & Compliance Updates

### v2.0
- **WCAG 2.1 AA**: Referenced with cross-link to Accessibility Manifesto
- **Plain Language Guidelines**: US federal standard for clear communication
- **Microsoft Style Guide**: Alignment with industry-standard style guide
- **Google Developer Documentation Style Guide**: Technical writing best practices
- **Diátaxis Framework**: Documentation structure methodology
- **ISO/IEC/IEEE 26514**: Software user documentation standard

### Future
- Considering: WCAG 2.2 (when widely adopted)
- Considering: EN 301 549 (European accessibility standard)
- Monitoring: ISO 82079 series (preparation of instructions for use)

---

## Contributors

### v2.0
- Comprehensive restructuring and expansion
- Integration with existing manifesto ecosystem
- Role-specific guidance development
- Tool ecosystem curation
- Measurement framework design

### v1.0
- Initial principle formulation
- Diátaxis framework integration
- Code examples and anti-patterns
- Foundational content quality metrics

---

## Related Manifestos

This manifesto complements:
- **[Accessibility Manifesto](../accessibility/)** v1.1 - Principle IV references comprehensive WCAG implementation
- **[UX Manifesto](../user_experience/)** v2.0 - Overlaps on UI content, microcopy, error messages
- **[Vibe Coding Manifesto](../vibe_coding/)** v2.0 - Code as Communication principle aligns with readable code
- **[Security Hardening Manifesto](../security_hardening/)** v2.0 - Error messages, security disclosures
- **[Data & Analytics Manifesto](../data_analytics/)** v2.0 - Data documentation, metrics definitions

**See**: [Objective Review Metasystem README](../../README.md) for full ecosystem.

---

**Last Updated**: 2025-11-20
**Maintained By**: Objective Review Metasystem Project
**License**: CC0 - Public Domain
