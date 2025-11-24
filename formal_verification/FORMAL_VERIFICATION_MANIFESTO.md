---
id: "formal-verification"
title: "The Formal Verification Manifesto"
version: "2.1"
status: "current"
focus: "Mathematical correctness proofs for critical systems"
primary_users: ["safety-engineers", "security-researchers", "aerospace-developers", "kernel-developers"]
learning_curve: "very-high"
roi_timeline: "long-term"
adoption_scope: "specialized"
principles_count: 4
tier_structure:
  core: 4
  standard: 0
  excellence: 0
applicability:
  project_types: ["safety-critical", "security-critical", "high-assurance"]
  languages: ["coq", "isabelle", "lean", "agda", "f-star", "dafny", "tla-plus", "spark-ada"]
  contexts: ["avionics", "medical-devices", "automotive", "cryptography", "authentication", "consensus-protocols"]
related_manifestos:
  complements: ["security-hardening", "vibe-coding"]
  prerequisites: ["strong-type-systems", "discrete-mathematics"]
  enables: ["provable-security", "bug-free-critical-components"]
tools:
  categories: ["proof-assistants", "theorem-provers", "smt-solvers", "model-checkers"]
  count: 20+
measurement:
  proof_coverage:
    critical_functions_verified:
      target: "100%"
      measurement: "proof-assistant-reports"
    lines_of_spec_per_loc:
      target: "0.1-0.5 for Dafny, 3-10 for Coq"
      measurement: "manual-count"
  proof_checking:
    proof_check_time:
      target: "≤5 minutes in CI"
      acceptable: "≤15 minutes"
      measurement: "ci-cd-logs"
  defects:
    critical_bugs_in_verified_code:
      target: "0"
      measurement: "bug-tracker"
---
# The Formal Verification Manifesto

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
