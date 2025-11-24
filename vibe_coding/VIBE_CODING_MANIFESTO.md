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
principles_count: 15 # As revised
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

---

## Philosophy & Scope

This manifesto provides principles for writing human-maintained production code in long-lived systems where **readability, maintainability, and correctness** are the primary goals.

It is guided by a single metaprinciple:

> **Code is for humans first, machines second.**

Compilers optimize for machines; we must optimize for human cognition. This manifesto is about the craft of creating code that is not just correct, but also clear, elegant, and a joy to work with.

### Applicability

-   **✓ Best Fit**: Long-lived systems (5+ years), teams valuing craft, complex business domains, libraries and frameworks.
-   **~ Conditional Fit**: Medium-sized projects, growing teams, greenfield projects. Adopt Core Principles first.
-   **✗ Poor Fit**: Throwaway prototypes, one-off scripts, machine-generated code, performance-critical code *before* profiling.

---

## Core Principles (Universal — Start Here)

These principles are the foundation of Vibe Coding. They transcend language and paradigm and should be adopted by all teams.

### 1. Collaborative Aesthetics
**Team consensus outweighs individual preference. Automate style to minimize conflict.**

Aesthetic debates are a drain on energy. The goal is a consistent, pleasant "vibe" that the whole team shares, not a single person's ideal.

**Guidelines**:
- **Hierarchy of Authority**:
    1.  **Language Idioms**: Follow community conventions (e.g., PEP 8 for Python).
    2.  **Auto-formatter**: Use Prettier, Black, rustfmt, etc. Its decisions are final.
    3.  **Team Style Guide**: Document choices not covered by the formatter.
    4.  **Individual Preference**: Permitted only for non-enforceable style (e.g., variable names not covered by linter).
- **Code Review Focus**: Review for logic, architecture, and tests. Do not comment on formatting that the auto-formatter handles.
- **Time-box Debates**: If a style issue isn't resolved by the hierarchy above, discuss for a maximum of 15 minutes, make a decision, document it, and move on.

---

### 2. Aesthetic Legibility
**Code should read like prose. Its visual structure must mirror its logical structure.**

Code is read far more often than it is written. A beautiful, clean aesthetic reduces cognitive friction and allows the reader to grasp the logic intuitively.

**Guidelines**:
-   **Rhythm & Spacing**: Use whitespace to group related concepts. Create a consistent visual rhythm.
-   **Alignment**: Align parallel constructs vertically to reveal patterns.
-   **Line Length**: Keep lines under 80-100 characters to fit comfortably on one screen.
-   **Nesting Depth**: Limit indentation to a maximum of 3-4 levels. Deeply nested code is a sign it needs refactoring.

```python
# Anti-pattern: cramped, irregular, hard to scan
def calc(x,y,z):
  if x>0:return x*y+z
  elif x<0:return abs(x)*y-z
  else:return z

# Vibe: spacious, symmetric, rhythmic
def calculate(x, y, z):
    if x > 0:  return (x * y) + z
    if x < 0:  return (abs(x) * y) - z

    return z
```
**Tooling**: Prettier, Black, rustfmt, gofmt.

---

### 3. Intentional Naming
**Names must reveal purpose unambiguously. Their length should be proportional to their scope.**

Good names are the bedrock of self-documenting code. Avoid generic, vague, or misleading names.

**Guidelines**:
-   **Clarity over Brevity**: `user_has_permission` is better than `permission`.
-   **Scope-to-Length Ratio**:
    -   *1-5 lines*: single letters are fine (`i`, `j`, `k`).
    -   *5-20 lines*: short names are acceptable (`idx`, `usr`).
    -   *20+ lines / public API*: fully descriptive names are required (`currentUser`, `authenticatedUserAccount`).
-   **Be Specific**:
    -   **Booleans**: `isActive`, `hasPermission`, `canWrite`.
    -   **Functions**: Use verbs for actions (`sendEmail`), nouns for queries (`userName`).
    -   **Avoid**: `data`, `info`, `manager`, `handler`, `temp`, `obj`.

```rust
// Anti-pattern: vague, stuttering
fn process_data(data: Data) -> ProcessedData { }

// Vibe: precise, meaningful
fn normalize_measurements(raw: Vec<Measurement>) -> Statistics { }
```

---

### 4. Obviousness Over Cleverness
**Prefer straightforward, boring code over clever, novel code.**

Clever code is a liability. It’s hard to read, hard to debug, and hard to maintain. Write code that is easy for a junior developer to understand.

**Guidelines**:
-   If you feel proud of how clever your code is, you should probably rewrite it.
-   Fancy language features must justify their complexity budget.
-   "Code golf" is a sport, not a professional engineering practice.

```python
# Anti-pattern: clever, but requires a moment of thought
unique_items = reduce(lambda acc, item: acc if item in acc else acc + [item], my_list, [])

# Vibe: obvious, uses well-known idioms
unique_items = list(dict.fromkeys(my_list))

# Vibe++: explicit is even better
unique_items = []
seen = set()
for item in my_list:
    if item not in seen:
        unique_items.append(item)
        seen.add(item)
```
**When to be "clever"**: Only when performance profiling has proven it necessary, and the code is heavily documented.

---

### 5. Literate Programming
**Code must explain itself. Comments explain *why*, not *what*.**

The best documentation is code so clear it doesn't need any. When comments are necessary, they should provide context that the code cannot.

**Guidelines for Comments**:
-   **Explain Rationale**: Why was this approach chosen? What alternatives were considered?
-   **Explain Constraints**: `// Workaround for Bug #1234; remove when upstream is fixed.`
-   **Explain Domain Knowledge**: `// Per CAP theorem, we are prioritizing Availability here.`
-   **Use TODOs**: `// TODO(@username): Migrate to v2 API by 2025-Q2.`

```python
# Anti-pattern: redundant, explains the "what"
# Increment the counter
counter += 1

# Vibe: explains the "why"
# We track retry attempts to implement exponential backoff.
retry_attempts += 1
```

---

### 6. Cohesion and Locality
**Keep related code together. Group by feature, not by technical layer.**

Code that changes together should live together. This minimizes context switching and makes the codebase easier to navigate.

**Guidelines**:
-   **Feature Folders > Layer Folders**: A `users` folder containing `api.ts`, `domain.ts`, and `storage.ts` is more cohesive than a `controllers` folder containing `user.controller.ts`, `order.controller.ts`, etc.
-   **Minimize File Sprawl**: A developer working on a feature should ideally only need to open files in one or two directories.
-   **Dependencies Flow Inward**: The core domain logic should have no knowledge of infrastructure like databases or HTTP requests.

```
// Anti-pattern: Technical Layers (Low Cohesion)
src/
  controllers/
    user.controller.ts
  services/
    user.service.ts
  models/
    user.model.ts

// Vibe: Feature Cohesion
src/
  users/
    user.domain.ts      // Types, business logic
    user.api.ts         // HTTP interface
    user.storage.ts     // Persistence logic
  orders/
    ...
```

---

## Standard Principles (Context-Dependent)

These principles offer significant benefits but may depend on language features or team preference. Adopt them after mastering the core principles.

### 7. Immutability by Default
**Transform data rather than mutating it. Isolate side effects.**

Mutable state is a primary source of bugs. Prefer pure functions that take data and return new data, without changing the original.

**Guidelines**:
-   Use `const` or `final` by default. Only use mutable variables when necessary.
-   Prefer data structures that produce new versions upon modification (e.g., `map`, `filter`).
-   Structure your application with a "functional core, imperative shell," where side effects (like database writes) are pushed to the edges of the system.

```javascript
// Anti-pattern: mutation and hidden side effects
function add_item_to_cart(cart, item) {
  cart.items.push(item); // Mutation
  cart.total += item.price; // Mutation
  saveCart(cart); // Hidden side effect
  return cart;
}

// Vibe: pure transformation, explicit side effects
const with_item = (cart, item) => ({
  ...cart,
  items: [...cart.items, item],
  total: cart.total + item.price,
});

// The side effect is handled separately
const new_cart = with_item(cart, item);
saveCart(new_cart); // Explicit side effect
```
**When to violate**: In measured, performance-critical hot paths (e.g., game loops, high-frequency data processing) where allocation is a bottleneck. Document this decision.

---

### 8. Semantic Density
**Express concepts with appropriate concision, but never at the cost of clarity.**

Good code has a high signal-to-noise ratio. Every character should contribute to meaning. This is not "code golf"; it is about finding the most potent expression of an idea that your team universally understands.

**Guidelines**:
-   Use method chaining and pipelines where they are idiomatic (`query.filter().sort().limit(10)`).
-   Use list comprehensions or `map`/`filter` chains instead of manual loops if they are clearer.
-   **Clarity > Density**: If a denser expression requires a comment to explain it, it is too dense. Always defer to **Principle 4 (Obviousness Over Cleverness)** in cases of conflict.

```python
# Context: Python team familiar with list comprehensions.
# Anti-pattern: noisy and verbose
active_user_emails = []
for user in users:
    if user.is_active:
        active_user_emails.append(user.email)

# Vibe: dense and semantic
active_user_emails = [
    user.email
    for user in users
    if user.is_active
]
```

---

### 9. Contextual Verbosity
**Be explicit at boundaries, be terse in local scopes.**

The amount of ceremony in your code should be proportional to its distance from the core logic.

**Guidelines**:
-   **Public APIs**: Maximum verbosity. Full docstrings, explicit types, and clear names.
-   **Internal Module Boundaries**: Clear names and type annotations are required.
-   **Private Functions**: Descriptive names are sufficient.
-   **Function-local scope**: Short, conventional names (`i`, `x`, `acc`) are fine.

---

### 10. Joyful Craft
**Treat code as an artistic medium. Find beauty in well-crafted software.**

Programming is a creative act. Take pride in your work. A well-crafted piece of code is a pleasure to read and maintain. This subjective sense of "joy" is often a powerful heuristic for quality.

**Heuristics for Joyful Code**:
-   Would you be proud to show this code to a junior developer as an example of good work?
-   Does the structure of the code elegantly reflect the structure of the problem?
-   Is deleting and simplifying code celebrated?
-   Would you enjoy maintaining this code in two years?

---

## Advanced Principles (Requires Strong Language Support)

These principles require advanced language features (like strong type systems) and team expertise but offer transformative gains in correctness and maintainability.

### 11. Type as Documentation
**Make illegal states unrepresentable. Use the type system to enforce invariants.**

A strong type system is your first line of defense against bugs. Instead of validating data everywhere, design types that make invalid data impossible to create.

**Guidelines**:
-   **Primitive Obsession is the Enemy**: Don't use `string` for everything. Create domain-specific types like `EmailAddress`, `UserId`, `PositiveNumber`.
-   **Parse, Don't Validate**: Validate input at the system boundary *once* and convert it into a rich domain type. The rest of your system can then trust the type.
-   Use `Option<T>` (or `Maybe<T>`) for values that can be absent.
-   Use `Result<T, E>` (or `Either<L, R>`) for operations that can fail.

```typescript
// Anti-pattern: "stringly-typed", requires runtime checks everywhere
function processUser(id: string, age: number): void {
  if (age < 18) {
    // ...
  }
}

// Vibe: Types encode constraints. The compiler is your assistant.
type UserId = Brand<string, 'UserId'>;
type Adult = User & { age: Min<18> };

function processAdultUser(id: UserId, user: Adult): void {
  // No age check needed. The type system guarantees the user is an adult.
}
```

---

### 12. Error as Value
**Treat errors as data, not as a special control flow path. Exceptions are for unrecoverable system failures.**

When an operation can fail in a predictable way (e.g., user not found, validation failed), this is not exceptional. The function's return type should explicitly state this possibility.

**Guidelines**:
-   **Return `Result<Success, Failure>`**: This forces the caller to consciously handle both the success and failure cases.
-   **Use Exceptions for Programmer Errors**: `panic!`, `assert`, null pointers, index out of bounds. These signal a bug in the code that must be fixed, not a predictable failure mode.

```rust
// Anti-pattern: Using exceptions for predictable control flow
fn find_user(id: &str) -> User {
    let user = db.find(id);
    if user.is_none() {
        throw NotFoundException("User not found"); // Control flow
    }
    user.unwrap()
}

// Vibe: The return type documents the possible failure.
fn find_user(id: &str) -> Result<User, DatabaseError> {
    db.find(id) // Returns a Result directly
}

// The caller handles the outcome explicitly.
match find_user("123") {
    Ok(user) => println!("Found user: {}", user.name),
    Err(e)  => println!("Failed to find user: {:?}", e),
}
```

---

### 13. Composition Over Configuration
**Build large systems from small, focused functions. Prefer composing functions over creating classes with boolean flags.**

Write small, pure functions that do one thing well. Then, combine them like LEGO blocks to build complex behavior. This is more flexible and testable than a monolithic object configured with flags.

**Guidelines**:
-   Follow the Unix philosophy: "Write programs that do one thing and do it well."
-   Use function composition (`f(g(x))`) or pipelines (`x |> g |> f`).
-   This approach makes it easy to create new behaviors by assembling existing pieces, rather than modifying a large, complex object.

```javascript
// Anti-pattern: monolithic, configurable object
function processUser(user, options = { validate: true, persist: true, notify: true }) {
  if (options.validate) { /* ... */ }
  if (options.persist) { /* ... */ }
  if (options.notify) { /* ... */ }
}

// Vibe: a pipeline of small, composable functions
const processUser = flow(
  validate,
  persist,
  notify
);

// It's easy to create a new, slightly different workflow.
const processWithoutNotification = flow(validate, persist);
```

---

### 14. Constraint Propagation
**Push correctness guarantees as early as possible: from runtime to compile-time, from tests to the type system.**

The earlier a bug is caught, the cheaper it is to fix. Your goal is to make bugs manifest as compiler errors, not production incidents.

**The Hierarchy of Guarantees (Best to Worst)**:
1.  **✅ Type System (Compile-time)**: Encoded in the types. `fn head(arr: NonEmptyArray<T>)`. The bug is impossible.
2.  **✅ Runtime Assertions (Fail-fast)**: `assert(arr.length > 0)`. The bug causes a crash during development.
3.  **🟡 Property-Based Tests**: `property("head([x, ...xs]) == x")`. The bug is found by the test suite.
4.  **🟡 Unit Tests**: `test("head([1,2,3]) == 1")`. The bug is found for a specific example.
5.  **🔴 Documentation**: `// The array must not be empty.`. The bug is found by a human (hopefully).
6.  **💀 Convention/Hope**: The bug is found by your users.

---

## Specialized Principles

### 15. Visual Symbolism
**Use operators and symbols where they have a universally understood, mathematical meaning. Use with extreme caution.**

In some domains (e.g., mathematics, physics, academic papers), specialized operators can aid clarity. For most business application code, this is an anti-pattern.

**Guidelines**:
-   **Default to ASCII**: Prefer `|>` `>>` `&&` over `▷` `≫` `∧`.
-   **When to Use Unicode**: Only in highly specialized domains where the symbols are more familiar to the domain experts than their spelled-out names.
-   **Team & Tooling Buy-in**: Never adopt without universal team agreement and IDE/tooling support that makes typing and reading them trivial.
-   **Accessibility**: Be aware that screen readers may not handle these symbols well.

---
## Practical Application Guides

### Testing Philosophy
**Tests validate properties, not just examples. Test code is production code and deserves the same level of craft.**

-   **Property-Based > Example-Based**: Instead of `assert(add(2, 3) == 5)`, test the property `add(a, b) == add(b, a)` for any `a` and `b`.
-   **Test Names Describe Behavior**: `test_rejects_invalid_email_format`.
-   **Arrange-Act-Assert**: Structure your tests clearly.
-   **Apply Vibe Principles to Tests**: Your tests should be as readable and maintainable as your main codebase.

### Performance Philosophy
**Make it readable, then make it right, then make it fast—*if you must*. Measure before you optimize.**

1.  **Choose the Right Algorithm**: `O(n log n)` vs `O(n²) ` is the most important optimization.
2.  **Profile Your Code**: Use profiling tools to find the *actual* bottlenecks. Do not guess.
3.  **Optimize the Hot Path**: Apply targeted optimizations only where the profiler shows a problem.
4.  **Document the Trade-off**: If an optimization makes the code less readable, add a `// PERF:` comment explaining why it was necessary, with a link to the profiling data.

### Incremental Adoption Strategy
1.  **Phase 1 (Weeks 1-2): High-Impact, Low-Friction**
    -   Set up an auto-formatter (`Aesthetic Legibility`).
    -   Focus on better naming in new code (`Intentional Naming`).
    -   Improve comments in files you touch (`Literate Programming`).
2.  **Phase 2 (Months 1-2): Structural Improvements**
    -   Write new functions to be immutable (`Immutability by Default`).
    -   Organize new features by cohesion (`Cohesion and Locality`).
3.  **Phase 3 (Months 3-6): Architectural Shifts**
    -   Gradually introduce richer types (`Type as Documentation`).
    -   Incrementally migrate functions to return `Result` types (`Error as Value`).

---

## FAQ

**Q: What if my language doesn't support these principles?**
A: Focus on the language-agnostic Core Principles. Every language supports better naming, clearer structure, and good comments.

**Q: How do I convince my team to adopt this?**
A: Start small. Apply the principles to a single new module. Demonstrate the benefits in a code review. Show, don't just tell.

**Q: What if principles conflict?**
A: `Obviousness > Density`. `Clarity > all`. When in doubt, choose the option that will be easiest for a new team member to understand.

**Q: How do I handle legacy code?**
A: Don't rewrite it all at once. Apply the "boy scout rule": leave the code cleaner than you found it. Add tests, then refactor opportunistically.

**Q: What about performance?**
A: Measure first. Optimize only proven hot paths. Document trade-offs. See Performance Philosophy.
