---
name: formal-verification-review
description: Plan and review high-assurance software verification using precise specifications, type-driven design, model checking, SMT solving, proof assistants, and machine-checked evidence.
---
# Formal Verification Review

Identify the property, system boundary, threat or fault model, assumptions, and required assurance level. Select the weakest adequate formal method, preserve a trace from requirements to checked artifacts, and distinguish tests, static analysis, model checking, and proof. Never describe an unchecked specification or admitted theorem as verified.

**Version**: 2.1
**Last Updated**: 2025-11-23

> We write tests to check if our code is wrong. We write proofs to *prove* it is right. For safety-critical systems, correctness must be a guarantee, not a probability.

---

## The 5 Rulings

### OBLIGATORY (Standard Best Practices)
**Mandatory for any high-assurance system.**

-   **Specify First**: Define requirements with mathematical precision before coding.
-   **Rigorous Testing**: Unit, integration, and property-based testing as a baseline.
-   **Strict Null-Checking**: Eliminate null pointer exceptions by design.
-   **Code Review**: rigorous peer review for all critical paths.

### ENCOURAGED (Type-Driven & Automated)
**Recommended to eliminate entire classes of bugs.**

-   **Make Invalid States Unrepresentable**: Use the type system (ADTs, Enums) to prevent invalid data construction.
-   **Automate Proofs**: Use SMT solvers and model checkers (Dafny, TLA+) rather than manual proofs where possible.
-   **Design by Contract (DbC)**: Annotate code with preconditions, postconditions, and invariants.
-   **Static Analysis**: Use advanced linters and abstract interpretation tools.

### OPTIONAL (Full Functional Correctness)
**Discretionary usage for the most critical components (High ROI only).**

-   **Interactive Theorem Proving**: Using Coq/Lean/Isabelle for machine-checked proofs of complex algorithms.
-   **Verified Compilation**: Using formally verified compilers (e.g., CompCert).
-   **Verified Cryptography**: Proving resistance to side-channel attacks.

### DISCOURAGED (Anti-Patterns)
**Practices that undermine verification efforts.**

-   **Primitive Obsession**: Using `string` or `int` for complex domain concepts.
-   **"Code First, Spec Later"**: Writing the specification to match the implementation.
-   **Manual Proofs**: Relying on paper proofs without machine-checking.
-   **Over-Verification**: Attempting to verify non-critical UI or prototype code (Low ROI).

### PROHIBITED (Forbidden)
**Practices unacceptable in safety-critical contexts.**

-   **Unverified Critical Code**: Deploying life-critical logic without formal assurance.
-   **Ignoring Counterexamples**: Dismissing model checker failures as "unlikely".
-   **Runtime Validation Only**: Relying solely on runtime checks when compile-time guarantees are possible.

---

## The Path to Verification

1.  **Level 0**: Standard Best Practices (Testing, Review).
2.  **Level 1**: Type-Driven Development (Strong types, ADTs).
3.  **Level 2**: Lightweight Verification (Contracts, Model Checking).
4.  **Level 3**: Full Correctness (Theorem Proving).

**Strategy**: Verify the critical 1-5% (kernel, consensus, crypto). Test the rest.
