---
id: "research-hygiene"
title: "The Research Hygiene Manifesto"
version: "1.0"
status: "current"
focus: "What a result is entitled to claim, and what happens when evidence runs out"
primary_users: ["research-engineers", "ml-practitioners", "benchmark-maintainers", "technical-writers"]
learning_curve: "low"
roi_timeline: "immediate"
adoption_scope: "broad"
principles_count: 9
tier_structure:
  core: 4
  standard: 3
  excellence: 2
applicability:
  project_types: ["research", "evaluation-harnesses", "benchmarks", "scientific-software", "proof-adjacent"]
  languages: ["python", "rust", "julia", "r", "lean", "tla-plus", "mojo"]
  contexts: ["experiments", "model-evaluation", "literature-backed-claims", "multi-repository-programmes"]
related_manifestos:
  complements: ["formal-verification", "data-analytics", "content-communication"]
  prerequisites: []
  enables: ["reproducible-research", "auditable-claims"]
tools:
  categories: ["claim-ledgers", "prose-linters", "differential-testing", "model-checkers"]
  count: 6+
measurement:
  claim_status:
    claims_with_declared_status:
      target: "100%"
      measurement: "claim-ledger-audit"
    surfaces_in_agreement:
      target: "100%"
      measurement: "ci-consistency-check"
  refusal_handling:
    bounded_failures_reported_as_absence:
      target: "0"
      measurement: "code-review"
  translation:
    authority_raised_across_a_boundary:
      target: "0"
      measurement: "vocabulary-map-tests"
---
# The Research Hygiene Manifesto

**Version**: 1.0
**Last Updated**: 2026-09-16

> A passing test tells you what your code did. It does not tell you what you are entitled to say about the world. Most research mistakes are not bugs; they are sentences.

---

## Why this manifesto exists

Every failure named here is one where the code ran correctly and the tests passed, while the claim attached to the result was wrong. Ordinary code review does not catch these, because there is nothing wrong with the code. Type checkers do not catch them. A green pipeline actively hides them, because green is read as a claim.

The examples in this manifesto are real. Each comes from a specific defect caught in review, not from a hypothetical.

---

## The 5 Rulings

### OBLIGATORY (Non-negotiable)

**Required of any result offered as evidence.**

- **Declare the status of every claim**: proved, imported, scaffolded, or open. A claim with no status is an open claim.
- **Distinguish a refusal from a negative result**: "could not evaluate" and "evaluated, found nothing" must not share a representation.
- **Report a bound when you reach it**: a search that stopped at a limit says so, in its return value, not only in a log.
- **Preserve or lower authority in translation**: evidence crossing a system boundary may become weaker, never stronger.

### ENCOURAGED (Production quality)

- **Keep a machine-checkable claims ledger**: one source of truth, with every surface generated from it or checked against it.
- **Build controls independent of what they test**: a control derived from its subject cannot fail.
- **Declare terminology with its known leaks**: a borrowed word carries assumptions; name them.

### OPTIONAL (Advanced)

- **Differential-test against an independent implementation**: agreement between two implementations written from the same specification is real evidence.
- **Keep a delivery ledger that admits partial delivery**: "done" and "done except" are different states.

### DISCOURAGED (Anti-patterns)

- **Unqualified "verified"**: verified by what, on what domain, under what assumptions.
- **Status duplicated across documents with nothing keeping it in step**: the stale copy is the one the next reader follows.
- **Prose that asserts an equivalence the code does not check**: "is isomorphic to", "is equivalent to", "corresponds exactly".

### PROHIBITED (Forbidden)

- **Reporting a bounded failure as absence**: "we did not find one" presented as "there is none".
- **A control that cannot fail**: a negative control whose outcome is fixed by its construction.
- **Raising authority in translation**: an unexecuted step, or a failed one, becoming a pass.

---

## Core rulings

### I. Declare the status of every claim

Every assertion carries one of four statuses, and the status travels with the assertion.

- **Proved**: established here, by a checkable artifact.
- **Imported**: established elsewhere, under hypotheses you must name.
- **Scaffolded**: the structure exists, the content does not.
- **Open**: not established.

An unlabelled claim is open. This is the rule that makes the rest enforceable, because a reviewer can ask "which is it?" about any sentence.

```python
# Anti-pattern: the reader cannot tell what kind of thing this is
RESULTS = {
    "density_converges": True,
    "fibres_are_trivial": True,
}

# ✓ Status travels with the claim, and the imported one names its source
RESULTS = {
    "density_converges": Claim(PROVED, evidence="tests/test_density.py::test_limit"),
    "fibres_are_trivial": Claim(
        IMPORTED,
        source="Graczyk-Swiatek 1998; Smirnov 2000",
        hypotheses=["exceptional set is null, not empty"],
    ),
}
```

**Why**: status drift is silent. A claim written as scaffolded in January reads as proved in June, because nothing in the sentence records which it was.

**When to violate**: never for published claims. Exploratory scratch files are exempt until they are cited.

### II. A refusal is not a negative result

When a computation declines to answer, its answer must be distinguishable from "answered, and the answer is empty".

This is the most dangerous failure in the manifesto, because the two collapse into the same value under the most natural implementation: an empty list.

```python
# Anti-pattern: the cap and the clean result are the same value
def find_obstructions(graph, limit=10_000):
    if graph.size > limit:
        return []          # caller reads this as "no obstructions"
    return search(graph)

# ✓ A refusal is its own state, and cannot be read as a verdict
def find_obstructions(graph, limit=10_000):
    if graph.size > limit:
        return Refused(reason=f"graph exceeds {limit} vertices")
    return Found(search(graph))
```

**Why**: an empty result is a positive verdict about a complete search. Returning it for an incomplete one converts a resource limit into a scientific claim.

**When to violate**: never. If the type system makes a separate state expensive, that cost is the price of the distinction.

### III. Report the bound when you reach it

A bounded search reports the bound in its result, not only in a log line nobody reads.

State the bound, state that it was reached, and state that the outcome is therefore unknown on the remainder. Counting how many inputs were refused is usually worth reporting too; a sweep that quietly skipped half its cases looks identical to one that covered them.

```text
Anti-pattern: "checked 29 types, all clean"
✓            "checked 29 types, all clean; 35 more exceeded the bound and were
              refused, not passed"
```

**Why**: the reader's next question is always "and the rest?". If the answer is not in the result, the reader supplies an optimistic one.

### IV. Translation preserves or lowers authority

When evidence crosses a boundary between systems, the receiving system may weaken it or keep it, never strengthen it.

Build the map explicitly and test it. The interesting cases are the ones where the source system has no equivalent of the target's strongest state.

| Source receipt                         | Honest translation                      | Never              |
| -------------------------------------- | --------------------------------------- | ------------------ |
| Step not executed                      | Pending                                 | Passed             |
| Test ran and failed                    | Pending, or refuted                     | Passed, or ignored |
| Ran in a dirty environment             | Bounded, valid on that environment only | Verified generally |
| Ran clean, with a command and a digest | Verified                                | Proved             |

```python
# Anti-pattern: an unexecuted step becomes a pass because the field was absent
status = receipt.get("status", "PASS")

# ✓ Absence is pending, and the rule is asserted, not assumed
status = TRANSLATION[receipt["status"]]
assert authority(status) <= authority(receipt["status"])
```

**Why**: translation layers are where authority quietly inflates, because each side's vocabulary looks reasonable in isolation.

---

## Standard rulings

### V. Keep one claims ledger, and generate the surfaces

Status appears in many places: a README badge, a specification, a docstring, a dashboard. Keep one machine-readable ledger and derive or check the rest against it.

**Why**: duplicated status does not stay in step. In practice the stale copy is the one a newcomer finds, because it is usually the friendlier document.

**Concretely**: a documentation change that corrects a claim is not finished until every surface stating that claim is corrected. Grep for the phrase before opening the change.

### VI. Build controls independent of what they test

A negative control must be able to fail. If its construction guarantees the outcome, it measures nothing and is worse than no control, because it reads as evidence.

```python
# Anti-pattern: the separators are built from the points being separated,
# so every point lands in its own cell and the "control" always passes
separators = [(points[i], points[i + 1]) for i in range(len(points) - 1)]
assert all_points_separated(points, separators)   # cannot fail

# ✓ The separators come from an independent source, so the assertion has content
separators = declared_prefix(source="period-3 orbit", tag=RATIONAL_RAY_LANDING)
report = extract(points, separators)              # may find obstructions, and does
```

**The test to apply**: ask what result would refute this. If no input produces a different answer, it is not a control.

**Why**: a tautological control is the most expensive kind of wrong, because it is cited as the reason to stop looking.

### VII. Declare terminology with its known leaks

When you borrow a word from another field, or coin one, declare it where it is defined:

- **Genealogy**: where the word comes from and what it means there.
- **Bridge claim**: whether the correspondence is theorem-backed, conditional, definition-only, or analogy-only.
- **Known leaks**: what the source meaning carries that yours does not.
- **Use discipline**: where the word may appear, and what it may never be used to assert.

**Why**: borrowed words import their connotations for free. A reader who knows the source field will assume the source guarantees unless you say otherwise.

---

## Excellence rulings

### VIII. Differential-test against an independent implementation

Write the thing twice, from the specification rather than from the first implementation, and compare on a large input space.

This catches what tests written alongside the code cannot, because a test written by the author encodes the author's misunderstanding as readily as the code does. It is most valuable where one implementation cannot be run locally, since the other becomes the oracle.

**Discipline that makes it real**: the second implementation must not be a transliteration of the first. If it is, agreement proves only that you copied accurately. Use a different algorithm where one exists.

### IX. Keep a delivery ledger that admits partial delivery

Track what shipped against what was specified, with a column for what is still owed. A row marked "done" is a row nobody reads again.

A ranked plan without a delivery column tends to lose exactly the items that are small enough to be deprioritised and small enough that nobody notices they are missing.

**The sharper reason**: a delivery ledger can catch a plan that was wrong, not merely unfinished. An item's own definition can turn out to be unachievable as written, and a column that only tracks whether code shipped will record it as done and bury that.

---

## Reference implementation

`claim_governance` in [`larsbx/finite-math-kernels`](https://github.com/larsbx/finite-math-kernels) enforces a working subset of these rulings in continuous integration across two research repositories.

| Ruling                             | Check                                                                               |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| I. Declare status                  | Every governed claim carries a status class; unknown values fail                    |
| I, V. One ledger                   | Status surfaces are compared against the ledger and must agree                      |
| VII. Declare terminology           | Declarations must carry all of genealogy, bridge claim, known leaks, use discipline |
| DISCOURAGED. Asserted equivalence  | Risky bridge phrases fail unless the file carries a declaration                     |
| DISCOURAGED. Unqualified promotion | An item the ledger records as open may not be described as proved                   |

It is not a complete implementation of this manifesto. Rulings II, III, IV, VI, VIII and IX are enforced there by tests and review rather than by a linter, and a general tool for them would be a useful contribution.

---

## Vale rules

[CONTRIBUTING](../CONTRIBUTING.md) tells contributors to run `vale **/*.md`. Vale reads its configuration from the working directory, and the repository's only configuration lived under `integrations/vale/`, so that instruction did nothing from the repository root.

A root `.vale.ini` now makes it runnable. It reuses the existing styles tree at `integrations/vale/styles` rather than creating a second one, and loads no external packages, so it runs offline without `vale sync`. The richer example configuration in `integrations/vale/.vale.ini`, which pulls in the Microsoft and Google packages, is untouched and stays opt-in.

`integrations/vale/styles/ResearchHygiene/` ports the prose rulings:

- `AssertedEquivalence.yml` flags equivalence language that needs a declaration.
- `UnqualifiedVerification.yml` flags "verified" and "proved" without a qualifier.
- `BoundedAbsence.yml` flags absence claims phrased from a failed search.
- `HedgeAsEvidence.yml` flags "should be", "presumably" and similar standing in for a result.

Run `vale **/*.md`. The rules are warnings, not errors: they mark sentences that need a decision, and plenty of flagged sentences are fine once a declaration is present.

---

## Implementation guide

1. **Start with Ruling I.** Pick your four status names and label every claim in one document. This takes an afternoon and immediately exposes the claims nobody can classify.
2. **Then Ruling II.** Grep for functions that return an empty collection on a limit, cap, or timeout. Each is a place where a resource limit can be read as a result.
3. **Then Ruling V.** Put the statuses in one file and add a check that the prose agrees with it.
4. **Add Ruling VI when you next write a control.** Ask what would refute it before writing the assertion.
5. **The rest as the project earns them.** Rulings VIII and IX pay off on long-lived, multi-repository work and are overkill for a single experiment.

---

## When to violate this manifesto

- **Exploratory work**: scratch analysis is exempt until it is cited. The moment a number leaves your notebook, it is a claim.
- **Ruling VIII**: a second implementation is not worth it for code you can check directly, or where the specification is the implementation.
- **Ruling IX**: a project with one deliverable does not need a ledger.

Rulings I through IV do not have exemptions. They are cheap, and each one exists because its absence converts a limitation into an assertion.

---

## Related manifestos

- [Formal Verification Manifesto](../formal_verification/FORMAL_VERIFICATION_MANIFESTO.md): what to do when you can prove it. This manifesto covers what you may say when you cannot, which is the usual case.
- [Data & Analytics Manifesto](../data_analytics/): evidence handling and measurement.
- [Content & Communication Manifesto](../content_communication/CONTENT_COMMUNICATION_MANIFESTO.md): precision and clarity in how a claim is written, once you are entitled to write it.
