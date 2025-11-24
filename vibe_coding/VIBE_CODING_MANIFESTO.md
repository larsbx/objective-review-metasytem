---
id: "vibe-coding"
title: "The Vibe Coding Manifesto"
version: "2.1"
status: "current"
focus: "Human readability & maintainability"
primary_users: ["all-developers"]
learning_curve: "medium"
roi_timeline: "immediate"
adoption_scope: "universal"
principles_count: 15
tier_structure:
  core: 6
  standard: 4
  advanced: 4
  specialized: 1
applicability:
  project_types: ["all"]
  languages: ["python", "typescript", "rust", "go", "haskell", "java"]
  contexts: ["long-lived-systems", "complex-business-logic", "libraries", "frameworks"]
related_manifestos:
  complements: ["accessibility", "content-communication", "formal-verification"]
  prerequisites: []
  enables: ["security-hardening", "data-analytics"]
tools:
  categories: ["linters", "formatters", "type-checkers"]
  count: 20+
measurement:
  cyclomatic_complexity:
    target: "≤10"
    acceptable: "≤15"
    alert_threshold: ">15"
  function_length:
    target: "≤25 lines"
    acceptable: "≤50 lines"
  nesting_depth:
    target: "≤3"
  test_coverage:
    target: "≥90%"
    acceptable: "≥80%"
---
# Vibe Coding Manifesto: 15 Foundational Principles

**Version**: 2.1
**Classification**: Public
**License**: CC0 - Public Domain

> **Code is for humans first, machines second.**
> We optimize for human cognition, readability, and the joy of craft.

---

## The 5 Rulings

### OBLIGATORY (Core Principles)
**Universal requirements for Vibe compliance.**

-   **Collaborative Aesthetics**: Automate formatting (Prettier/Black). No style bikeshedding.
-   **Aesthetic Legibility**: Code must read like prose. Consistent rhythm, alignment, and max nesting (3 levels).
-   **Intentional Naming**: Names must reveal purpose. Length proportional to scope. No `data` or `obj`.
-   **Obviousness Over Cleverness**: Boring code is better than clever code. Optimize for the junior dev.
-   **Literate Programming**: Comments explain *why*, not *what*.
-   **Cohesion and Locality**: Group by feature, not by layer. Keep related code together.

### ENCOURAGED (Standard Principles)
**Highly recommended for maintainability.**

-   **Immutability by Default**: Transform data, don't mutate. Use `const`/`final`.
-   **Semantic Density**: High signal-to-noise ratio. Use method chains and pipelines where clear.
-   **Contextual Verbosity**: Be explicit at boundaries (APIs), terse in local scope.
-   **Joyful Craft**: Take pride in the artifact. Refactor for beauty.

### OPTIONAL (Advanced/Specialized)
**Powerful techniques for experienced teams.**

-   **Type as Documentation**: Make illegal states unrepresentable (ADTs, Domain Types).
-   **Error as Value**: Return `Result<T,E>` instead of throwing exceptions.
-   **Composition Over Configuration**: Compose small functions rather than configuring god objects.
-   **Visual Symbolism**: Use mathematical symbols (Unicode) *only* if domain-appropriate and team-agreed.

### DISCOURAGED (Anti-Patterns)
**Practices that harm readability and "vibe".**

-   **Clever Code**: One-liners that require decoding.
-   **Primitive Obsession**: Using `string` for everything.
-   **Mutation**: Modifying data in place (except in hot paths).
-   **Comments explaining "What"**: `i++ // increment i`.
-   **Layered Architecture**: Spreading a single feature across 5 folders (Controllers, Services, Models...).

### PROHIBITED (Forbidden)
**Practices that destroy maintainability.**

-   **Code Golf**: Minimizing characters at the expense of clarity.
-   **Inconsistent Style**: Ignoring the auto-formatter or linter.
-   **Misleading Names**: `getUser()` that actually deletes a user.
-   **God Functions**: 500+ line functions doing everything.

---

## Practical Guides

### Testing
-   **Property-Based > Example-Based**: Test invariants.
-   **Readable Tests**: Tests are documentation.

### Performance
-   **Measure First**: Don't optimize without profiling.
-   **Document Trade-offs**: If you must write ugly code for speed, explain why with data.
