# Ethical Framework Mapping: Software Development Domains

**Classification**: Public
**License**: CC0 - Public Domain
**Last Updated**: 2025-11-22

---

## Overview

This mapping translates the ethical axioms of the framework into concrete practices across the five primary domains of modern software development.

## 1. The Domain of Security & Reliability Engineering

**Primary Objective**: System Integrity (Hifz al-Din) & Resource Efficiency (Hifz al-Mal)

This domain is the most rigid because it protects the fundamental "truth" of the system.

### Critical Required (Fard):
* **Encryption at Rest/Transit**: You must protect data. Leaving it exposed violates the trust (Amanah) of the user.
* **Access Control (RBAC)**: Preventing unauthorized mutation of state.
* **Input Validation**: "Sanitizing" inputs to prevent injection attacks (corruption of truth).

### Prohibited (Haram):
* **Hardcoded Secrets**: Committing API keys to code repositories.
* **Dark Patterns**: UI designs specifically created to deceive users (e.g., hidden unsubscribe buttons).
* **Ignoring CVEs**: Knowingly shipping code with critical vulnerabilities.

---

## 2. The Domain of DevOps & Infrastructure (SRE)

**Primary Objective**: System Longevity (Hifz al-Nasl)

This domain focuses on the "lineage" of the code—ensuring it survives and evolves across generations of developers.

### Strongly Recommended (Mandub):
* **Immutable Infrastructure**: Servers that are replaced rather than patched. This ensures consistency (a form of integrity).
* **Comprehensive CI/CD**: Automating the "ritual" of deployment to remove human error.
* **Disaster Recovery Drills**: Practicing for failure to ensure the system's survival.

### Anti-Pattern (Makruh):
* **Manual Deployments**: "Clicking around" in the console. It creates "snowflake" servers that cannot be reproduced (breaking the lineage).
* **Configuration Drift**: Allowing environments (Dev, Staging, Prod) to slowly diverge.

---

## 3. The Domain of Product Management & UX

**Primary Objective**: Human Sustainability (Hifz al-Nafs)

This domain governs how the system impacts the human life—both the user's and the developer's.

### Critical Required (Fard):
* **Accessibility (a11y)**: Ensuring the system can be used by people with disabilities. Excluding them causes harm.
* **Privacy Compliance (GDPR/CCPA)**: Protecting the user's "digital self."

### Discretionary (Mubah):
* **Feature Toggles**: Releasing a feature to 10% of users.
* **A/B Testing**: Testing blue vs. green buttons. (Provided neither is deceptive).

### Prohibited (Haram):
* **Addictive Mechanics**: Algorithms designed specifically to trigger dopamine loops at the expense of user mental health (violating Hifz al-Nafs).

---

## 4. The Domain of Software Architecture

**Primary Objective**: Knowledge Capital (Hifz al-Aql) & Resource Efficiency

Architecture protects the "Intellect" of the system—how well it can be understood and reasoned about.

### Strongly Recommended (Mandub):
* **Domain-Driven Design (DDD)**: Aligning the code with the real-world business language. This preserves "meaning."
* **Documentation (ADRs)**: Writing down why a decision was made. Without this, the "intellect" of the team dies when a senior engineer leaves.

### Anti-Pattern (Makruh):
* **Premature Microservices**: Splitting a system before it's necessary adds cognitive load (harming Intellect) without benefit.
* **God Objects**: Classes that do too much, making them impossible to reason about.

---

## 5. The Domain of Data Science & AI

**Primary Objective**: System Integrity (Truth) & Human Sustainability

### Critical Required (Fard):
* **Bias Audits**: Ensuring the model doesn't discriminate against specific groups (Violates Justice/Adl).
* **Explainability**: Users must know why a decision was made (Hifz al-Aql).

### Prohibited (Haram):
* **Black Box Sentencing**: Using AI for life-altering decisions (hiring, loans, bail) without human oversight or explainability.

---

## Summary Table: The Developer's Field Guide

| Domain | If the action is... | It is mapped to... | Because it preserves... |
|---|---|---|---|
| Security | Fixing a CVE | Critical (Fard) | System Integrity (The system must be safe) |
| Testing | Writing Unit Tests | Recommended (Mandub) | System Longevity (Protecting future changes) |
| Frontend | Accessibility Fix | Critical (Fard) | Human Sustainability (Protecting vulnerable users) |
| Frontend | Pixel Pushing | Discretionary (Mubah) | Resource Efficiency (Aesthetic choice) |
| Backend | Refactoring | Recommended (Mandub) | Knowledge Capital (Making code readable) |
| Data | Selling User Data | Prohibited (Haram) | Human Sustainability (Violation of privacy) |
| Process | Crunch / Burnout | Prohibited (Haram) | Human Sustainability (Harming the team) |

---

## Ethical Categorization System

### Fard (Critical Required)
Actions that are mandatory because they preserve fundamental integrity—of the system, of trust, or of human welfare. Violating these causes direct harm.

### Mandub (Strongly Recommended)
Practices that significantly improve quality, sustainability, or maintainability. Not mandatory, but their absence creates technical debt and long-term risk.

### Mubah (Discretionary)
Neutral practices where the choice depends on context. Neither required nor discouraged—use judgment based on specific needs.

### Makruh (Anti-Pattern)
Practices that are discouraged because they introduce fragility, technical debt, or cognitive overhead. Not outright forbidden, but should be avoided unless justified.

### Haram (Prohibited)
Actions that cause direct harm to users, systems, or teams. These violate the fundamental ethical principles and must never be done.

---

## Five Objectives (Maqasid)

1. **Hifz al-Din (System Integrity)**: Protecting the fundamental "truth" and correctness of the system
2. **Hifz al-Mal (Resource Efficiency)**: Using computational and human resources wisely
3. **Hifz al-Nasl (System Longevity)**: Ensuring code survives and evolves across generations
4. **Hifz al-Nafs (Human Sustainability)**: Protecting the wellbeing of users and developers
5. **Hifz al-Aql (Knowledge Capital)**: Preserving and enhancing collective understanding

---

**Navigation**: [Ethical Engineering Manifesto](./ETHICAL_ENGINEERING_MANIFESTO.md) | [Main README](../README.md)
