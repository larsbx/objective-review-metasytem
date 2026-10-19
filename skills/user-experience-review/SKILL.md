---
name: user-experience-review
description: Design and review user-facing products for task success, usability, accessibility, privacy, ethical interaction, consistency, feedback, performance, and measurable user satisfaction.
---
# User Experience Review

Identify the users, their goals, constraints, critical journeys, and success measures. Review observable behavior across normal, error, empty, loading, recovery, privacy, and accessibility states. Separate evidence from design judgment, prioritize failures by user impact, and provide testable acceptance criteria for proposed changes.

**Version**: 2.1
**Last Updated**: 2025-11-23
**Conformance**: WCAG 2.1 Level AA

> Good UX is not a luxury; it is a fundamental requirement. We measure quality by the user's ability to achieve their goals with minimum friction and maximum satisfaction.

---

## The 5 Rulings

### OBLIGATORY (Core Principles)
**Non-negotiable fundamentals. A failure here is a failure of the product.**

-   **User Primacy**: Design must serve user goals, not organizational convenience.
-   **Accessibility (WCAG 2.1 AA)**: Interfaces must be perceivable, operable, and understandable for all.
-   **Privacy & Ethical Design**: Minimal data collection, explicit consent, no dark patterns.
-   **Clarity and Recognition**: Minimize memory load. Show, don't tell.
-   **Consistency**: Similar elements must behave in similar ways.

### ENCOURAGED (Standard Principles)
**Required for a professional, competitive product.**

-   **Immediate Feedback**: Every action gets a response within 100ms.
-   **Error Prevention**: Design to make errors difficult to commit (constraints, smart defaults).
-   **Forgiveness**: Undo, non-destructive actions, and autosave.
-   **Progressive Disclosure**: Reveal complexity incrementally.
-   **Efficiency**: Optimize frequent tasks (keyboard shortcuts, bulk operations).
-   **Findability**: Clear navigation hierarchy and robust search.

### OPTIONAL (Excellence Principles)
**Differentiators for a best-in-class experience.**

-   **Aesthetic Integrity**: Visuals that reinforce structure and delight.
-   **Performance as Feature**: Optimizing for speed (LCP < 2.5s) as a form of respect.
-   **Contextual Relevance**: Interface adapts to user state (location, time, history).
-   **Continuous Validation**: Hypothesis-driven design tested with real users.

### DISCOURAGED (Anti-Patterns)
**Practices that degrade the experience.**

-   **"Organizational" Logic**: Exposing internal database structures to the user.
-   **Dead Ends**: Error messages that don't tell you how to fix the problem.
-   **Mystery Meat Navigation**: Icons without labels or unclear interactions.
-   **Slow Response**: Interfaces that freeze or lag >100ms without feedback.

### PROHIBITED (Forbidden)
**Unethical and harmful practices.**

-   **Dark Patterns**: Deceptive UI designed to trick users (e.g., hidden costs, roach motel cancellation).
-   **Non-Consensual Data Collection**: Tracking without permission.
-   **Inaccessible Core Flows**: Blocking disabled users from completing primary tasks.
-   **Hostile Design**: Punishing the user for system errors.

---

## Conflict Resolution Hierarchy
1.  **Accessibility & Ethics** (Non-negotiable).
2.  **User Primacy** (Data-driven user goals).
3.  **Clarity** (When in doubt, be obvious).

