# Accessibility Manifesto: 15 Foundational Principles

**Version**: 1.1
**Last Updated**: 2025-11-20
**Classification**: Public
**License**: CC0 - Public Domain
**Conformance**: WCAG 2.1 Level AA

**Related**: This manifesto expands [UX Manifesto Principle VIII (Accessibility as Foundation)](../user_experience/UX_MANIFESTO.md#viii-accessibility-as-foundation) with implementation-focused guidance for WCAG compliance and inclusive design.

---

## Table of Contents

**Core Principles** (WCAG A - Legal Minimum)
- [I. Universal Design](#i-universal-design)
- [II. Perceivability](#ii-perceivability)
- [III. Operability](#iii-operability)
- [VII. Keyboard Accessibility](#vii-keyboard-accessibility)

**Standard Principles** (WCAG AA - Industry Baseline)
- [IV. Understandability](#iv-understandability)
- [V. Robustness](#v-robustness)
- [VI. Semantic Structure](#vi-semantic-structure)
- [VIII. Screen Reader Compatibility](#viii-screen-reader-compatibility)
- [IX. Sufficient Time](#ix-sufficient-time)
- [X. Seizure Prevention](#x-seizure-prevention)
- [XI. Navigational Clarity](#xi-navigational-clarity)
- [XII. Input Assistance](#xii-input-assistance)

**Excellence Principles** (WCAG AAA + Inclusive Design)
- [XIII. Adaptive Technology Support](#xiii-adaptive-technology-support)
- [XIV. Multimodal Interaction](#xiv-multimodal-interaction)
- [XV. Testing & Validation](#xv-testing--validation)

**Meta-Sections**
- [Implementation Tiers](#implementation-tiers)
- [Measurement Framework](#measurement-framework)
- [Corollaries](#corollaries)
- [WCAG 2.1 Quick Reference](#wcag-21-quick-reference)
- [Tool Ecosystem](#tool-ecosystem)
- [Changelog](#changelog)

---

## I. Universal Design
**Interfaces shall be usable by all people, to the greatest extent possible, without adaptation.**

Design for the widest spectrum of human ability from inception. Accessibility is not special accommodation; it is fundamental design quality. Benefits extend beyond disability to all users in diverse contexts.

- Curb cuts benefit wheelchairs, strollers, luggage, bicycles
- Captions benefit deaf users, language learners, noisy environments, silent contexts
- Keyboard navigation benefits motor impairments, power users, broken trackpads

**Implementation Tier**: Core (WCAG A)
**Related**: [UX Manifesto: User Primacy (I)](../user_experience/UX_MANIFESTO.md#i-user-primacy)

---

## II. Perceivability
**Information and interface components must be presentable in ways all users can perceive.**

Content available through multiple sensory modalities. Visual information has textual alternatives. Auditory content has visual equivalents. No information conveyed through single sensory channel exclusively.

- Images: `alt` text describing content and function
- Video: captions (deaf) + audio description (blind)
- Color: never sole indicator of meaning; supplement with text, pattern, shape
- Contrast ratio: ≥4.5:1 for text, ≥3:1 for UI components

**Implementation Tier**: Core (WCAG A)
**WCAG Guideline**: 1.1, 1.2, 1.3, 1.4

---

## III. Operability
**Interface components and navigation must be operable through diverse input methods.**

Functionality available via keyboard, mouse, touch, voice, switch control, eye tracking. Time limits adjustable. Motion not required. Seizure-inducing content avoided.

- Complete keyboard navigation: `Tab`, `Shift+Tab`, `Enter`, `Space`, `Esc`, arrows
- Focus indicators: visible, high-contrast (≥3:1), minimum 2px
- No keyboard traps: escape mechanism always available
- Touch targets: ≥44×44px, adequate spacing

**Implementation Tier**: Core (WCAG A)
**WCAG Guideline**: 2.1, 2.2, 2.3, 2.4, 2.5

---

## IV. Understandability
**Information and interface operation must be comprehensible to all users.**

Clear language. Predictable behavior. Consistent patterns. Error identification with suggestions. Help available contextually.

- Reading level: appropriate to audience; plain language preferred
- Labels: descriptive, unambiguous (`"Submit payment"` > `"OK"`)
- Instructions: provided before control, not after
- Error messages: specific problem + remediation path

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 3.1, 3.2, 3.3

---

## V. Robustness
**Content must be interpretable by diverse user agents, including assistive technologies.**

Semantic HTML. Valid markup. Compatibility with screen readers, magnifiers, alternative input devices. Graceful degradation. Progressive enhancement.

- Semantic elements: `<button>`, `<nav>`, `<main>`, `<article>` not `<div>` with `role`
- ARIA: supplement, not replace, semantic HTML
- Standards compliance: valid HTML5, CSS3, WCAG 2.1 AA minimum
- Feature detection: functionality without JavaScript where possible

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 4.1

---

## VI. Semantic Structure
**Document structure shall be meaningful and programmatically determinable.**

Logical heading hierarchy. Landmark regions. List markup for lists. Table markup for tabular data. Relationships explicit.

- Headings: `<h1>` → `<h2>` → `<h3>`, no skipped levels
- Landmarks: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
- Lists: `<ul>`, `<ol>`, `<dl>` with proper nesting
- Tables: `<th scope="col|row">`, `<caption>`, headers associated with data cells

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 1.3 (Info and Relationships)

---

## VII. Keyboard Accessibility
**All functionality accessible via keyboard alone; no mouse required.**

Tab order logical. Focus visible. Shortcuts available but not mandatory. Modal dialogs trap focus appropriately. Custom widgets implement expected keyboard patterns.

- Tab order: DOM order or explicit `tabindex` (0, -1 only; never positive integers)
- Focus management: moved programmatically for SPA navigation, modal dialogs
- Keyboard shortcuts: documented, customizable, don't conflict with AT
- Custom widgets: ARIA authoring practices keyboard patterns

**Implementation Tier**: Core (WCAG A)
**WCAG Guideline**: 2.1 (Keyboard Accessible)

---

## VIII. Screen Reader Compatibility
**Content and functionality fully accessible to screen reader users.**

Alternative text meaningful. Form labels explicit. Dynamic updates announced. Hidden content truly hidden. Status messages communicated.

- Images: `alt` describes information, not "image of"
- Icons: text alternative or `aria-label`
- Form inputs: `<label for="id">` or `aria-labelledby`
- Live regions: `aria-live="polite|assertive"`, `role="status|alert"`
- Hidden content: `display:none` or `visibility:hidden` or `aria-hidden="true"`

**Implementation Tier**: Standard (WCAG AA)
**Screen Readers**: NVDA, JAWS, VoiceOver (macOS/iOS), TalkBack (Android), Narrator (Windows)

---

## IX. Sufficient Time
**Users shall have adequate time to read and interact with content.**

No arbitrary time limits. Timing adjustable or disable-able. Real-time exceptions clearly justified. Warning before expiration with extension option.

- Timeouts: 20× default, or disable, or warn + extend
- Auto-advancing content: pause, stop, hide controls available
- Session expiration: 20-hour default or warning 20 seconds before + easy extension
- Exceptions: real-time events (auctions), security requirements (documented)

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 2.2 (Enough Time)

---

## X. Seizure Prevention
**Content shall not contain elements known to cause seizures or physical reactions.**

No flashing content >3 times per second. Moving content pauseable. Animation respects `prefers-reduced-motion`. Parallax effects minimal or optional.

- Flash threshold: ≤3 flashes/second, or small safe area
- Animation: `@media (prefers-reduced-motion: reduce)` removes non-essential motion
- Autoplay: disabled or user-controlled
- Vestibular considerations: minimize parallax, large-scale motion

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 2.3 (Seizures and Physical Reactions)

---

## XI. Navigational Clarity
**Users shall orient themselves, find content, and determine location within interface.**

Skip links. Multiple navigation methods. Current location indicated. Breadcrumbs where appropriate. Search available for large sites.

- Skip link: first focusable element, jumps to main content
- Multiple paths: navigation menu, sitemap, search, related links
- Current page: indicated in navigation (`aria-current="page"`)
- Headings + landmarks: facilitate screen reader navigation
- Focus management: preserve or move logically on navigation

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 2.4 (Navigable)

---

## XII. Input Assistance
**Users shall receive help identifying and correcting errors.**

Error identification automatic. Suggestions provided. Labels and instructions clear. Required fields indicated. Format examples shown.

- Validation: inline, real-time where appropriate
- Error messages: `role="alert"` or `aria-live="assertive"`
- Suggestions: "Email format invalid. Example: user@domain.com"
- Required fields: `required` attribute + visual indicator + text label includes "(required)"
- Format: shown before input, e.g., "Date (MM/DD/YYYY)"

**Implementation Tier**: Standard (WCAG AA)
**WCAG Guideline**: 3.3 (Input Assistance)

---

## XIII. Adaptive Technology Support
**Interfaces shall respect user preferences and assistive technology configurations.**

System preferences honored. Font size scalable. High contrast modes supported. Dark mode available. User stylesheets not blocked.

- Text resize: 200% without loss of functionality or content
- High contrast: Windows High Contrast Mode support
- Dark mode: `@media (prefers-color-scheme: dark)`
- User zoom: not disabled (`maximum-scale`, `user-scalable=no` forbidden)
- Custom stylesheets: `!important` rules not overridden without cause

**Implementation Tier**: Excellence (WCAG AAA)
**User Preferences**: `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme`, system font size

---

## XIV. Multimodal Interaction
**Functionality shall be available through multiple interaction modalities.**

Gesture alternatives. Voice control support. Switch access compatible. Single-pointer operation. Motion actuation optional.

- Multi-touch gestures: single-pointer alternative available
- Drag-and-drop: keyboard alternative provided
- Hover: not required; touch equivalent exists
- Motion: shake, tilt optional; on-screen alternative
- Voice control: unambiguous labels, visible text matches accessible name

**Implementation Tier**: Excellence (WCAG AAA)
**WCAG Guideline**: 2.5 (Input Modalities)

---

## XV. Testing & Validation
**Accessibility verified through automated tools, manual inspection, and user testing.**

WCAG 2.1 AA minimum compliance. Automated tests in CI/CD. Manual testing with keyboard, screen reader. Testing with disabled users.

- Automated: axe, WAVE, Lighthouse in pipeline
- Keyboard: complete navigation without mouse
- Screen reader: NVDA, JAWS, VoiceOver testing
- User testing: include disabled users across disability types
- Audit frequency: every release + quarterly comprehensive audit

**Implementation Tier**: Excellence
**Success Metric**: 100% automated test pass rate, ≥90% task completion by screen reader users

See [Tool Ecosystem](#tool-ecosystem) for comprehensive testing tool list.

---

## Implementation Tiers

### Core (WCAG A - Legal Minimum)
**Principles**: I, II, III, VII
**Timeline**: Week 1 (new projects) | Month 1 (existing projects)
**Focus**: Legal compliance floor, severe usability barriers

**Checklist**:
- [ ] Text alternatives for images (`alt` attributes)
- [ ] Captions for video/audio content
- [ ] Complete keyboard navigation (no mouse required)
- [ ] Visible focus indicators
- [ ] No keyboard traps
- [ ] Semantic HTML structure
- [ ] Form labels explicit (`<label for>`)

### Standard (WCAG AA - Industry Baseline)
**Principles**: IV, V, VI, VIII, IX, X, XI, XII
**Timeline**: Months 1-3 (new projects) | Months 2-6 (existing projects)
**Focus**: Industry standard, recommended baseline

**Checklist**:
- [ ] Color contrast ≥4.5:1 (text), ≥3:1 (UI components)
- [ ] Touch targets ≥44×44px
- [ ] Logical heading hierarchy (`<h1>` → `<h2>` → `<h3>`)
- [ ] ARIA landmarks and live regions
- [ ] Screen reader testing (NVDA, VoiceOver)
- [ ] Error identification and suggestions
- [ ] No content flashing >3 times/second
- [ ] Session timeout warnings

### Excellence (WCAG AAA + Inclusive Design)
**Principles**: XIII, XIV, XV
**Timeline**: Months 3-6+ (ongoing)
**Focus**: Aspirational, maximum accessibility, competitive advantage

**Checklist**:
- [ ] Respect user preferences (`prefers-reduced-motion`, `prefers-color-scheme`)
- [ ] Text resize to 200% without content loss
- [ ] High contrast mode support
- [ ] Multimodal interaction alternatives
- [ ] User testing with disabled users (≥20% of total usability testing)
- [ ] Quarterly comprehensive accessibility audits
- [ ] WCAG AAA compliance where feasible

---

## Measurement Framework

### WCAG Conformance Levels

| Level | Description | Status | Business Impact |
|-------|-------------|--------|-----------------|
| **A** | Legal minimum; severe barriers | 0 violations required | Avoid lawsuits, ADA compliance |
| **AA** | Industry baseline | Target standard | Market access, procurement eligibility |
| **AAA** | Aspirational maximum | Apply where feasible | Competitive differentiation, broader reach |

### Key Metrics

**Automated Testing** (CI/CD Integration):
- Automated test pass rate: **100%** (axe, WAVE, Lighthouse)
- Zero critical/serious violations in production
- Scan frequency: Every commit (automated), every release (manual review)

**Manual Testing**:
- Keyboard navigation completeness: **100%** of functionality
- Screen reader task completion rate: **≥90%** (equivalent to sighted users)
- Manual audit frequency: Every release + **quarterly** comprehensive audit

**User Testing**:
- Testing with disabled users: **≥20%** of total usability testing
- Disability type coverage: Visual, auditory, motor, cognitive
- Task success rate: **≥90%** for primary workflows

**Performance Metrics**:
- Time-on-task (screen reader): ≤1.5× sighted user baseline
- Error rate: **<5%** on common tasks
- User satisfaction (disabled users): SUS score **≥80**

**Compliance Tracking**:
- WCAG violations by severity (critical/serious/moderate/minor): Trend toward 0
- Accessibility debt: Track and prioritize remediation
- Legal/regulatory compliance: ADA, Section 508, EAA, AODA

### Success Indicators by Principle

| Principle | Metric | Target |
|-----------|--------|--------|
| II. Perceivability | Color contrast ratio | ≥4.5:1 (text), ≥3:1 (UI) |
| III. Operability | Touch target size | ≥44×44px |
| VI. Semantic Structure | Valid HTML | 0 errors (W3C validator) |
| VII. Keyboard | Focus indicator contrast | ≥3:1 |
| VIII. Screen Reader | Task completion rate | ≥90% |
| IX. Sufficient Time | User-reported timeout issues | 0 critical |
| XI. Navigation | Users reporting "lost" | <2% |
| XIII. Adaptive Tech | Text resize to 200% | No content loss |
| XV. Testing | Automated scan frequency | Every commit |

---

## Corollaries

### Metaprinciple: Accessibility Cannot Be Retrofitted
Accessible design from inception costs ~10% development time. Remediation costs 10× more. Lawsuits cost 100× more.

**Business Case**:
- **Proactive**: 10% additional development time, integrated workflow
- **Reactive**: 100% additional development time (refactor existing code)
- **Legal**: $50k-$500k+ settlement, ongoing monitoring, reputational damage

### Legal Compliance Baseline, Not Ceiling
WCAG AA is minimum. Aim for AAA where feasible. Local regulations (ADA, Section 508, EAA, AODA) establish floor.

**Jurisdictional Requirements**:
- **US**: ADA (all public accommodations), Section 508 (federal procurement)
- **EU**: European Accessibility Act (2025 enforcement)
- **Canada**: AODA (Ontario), Accessible Canada Act
- **International**: EN 301 549, WCAG 2.1 AA global baseline

### Nothing About Us Without Us
Disabled users participate in design, testing, and evaluation. Lived experience informs decisions.

**Implementation**:
- User research: ≥20% participants with disabilities
- Accessibility team: Include disabled employees/consultants
- Testing: Real assistive technology users, not just automated tools
- Feedback: Dedicated channel for accessibility concerns

### Temporary & Situational Disability
Broken arm, bright sunlight, noisy environment—accessibility benefits extend beyond permanent disability.

**Examples**:
- Captions: Deaf users, noisy gym, silent library, language learners
- Voice control: Motor impairment, hands busy cooking, driving
- High contrast: Low vision, bright sunlight, aging displays
- Keyboard navigation: Motor impairment, broken trackpad, power users

### Semantic Before Stylistic
Correct HTML element > ARIA role > styled `<div>`. Use ARIA to enhance, not replace, semantics.

**Hierarchy**:
1. **Best**: `<button>Click me</button>`
2. **Acceptable**: `<div role="button" tabindex="0" onKeyPress={...}>Click me</div>`
3. **Never**: `<div onClick={...}>Click me</div>`

### Progressive Enhancement
Core functionality without JavaScript. Enhanced experience with modern features. No user left behind.

**Pattern**:
1. HTML: Semantic structure, functional without JS
2. CSS: Visual enhancement, graceful degradation
3. JavaScript: Interaction enhancement, feature detection

### Documentation & Training
Accessibility requirements documented. Developers trained. Design system includes accessible patterns.

**Resources**:
- Onboarding: Accessibility 101 training for all developers
- Design system: Accessible components with usage guidelines
- Code review: Accessibility checklist integrated
- Champions: Accessibility advocates in each team

### Performance is Accessibility
Slow interfaces disproportionately impact users on older devices, limited bandwidth, cognitive disabilities.

**Intersection**:
- Core Web Vitals: LCP <2.5s, FID <100ms, CLS <0.1
- Network resilience: Offline functionality, progressive loading
- Device support: Test on low-end devices (3+ years old)
- Cognitive load: Fast feedback reduces working memory burden

---

## WCAG 2.1 Quick Reference

### Four Principles (POUR)

**P**erceivable: Information available to senses
**O**perable: Usable via multiple inputs
**U**nderstandable: Clear and predictable
**R**obust: Compatible with assistive tech

### Conformance Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| **A** | Minimum accessibility | Legal compliance floor |
| **AA** | Recommended accessibility | Industry standard, procurement |
| **AAA** | Enhanced accessibility | Specialized content, aspirational |

### Guidelines Summary

**1. Perceivable**
- 1.1 Text Alternatives
- 1.2 Time-based Media (captions, audio description)
- 1.3 Adaptable (structure, relationships)
- 1.4 Distinguishable (color, contrast, resize)

**2. Operable**
- 2.1 Keyboard Accessible
- 2.2 Enough Time
- 2.3 Seizures and Physical Reactions
- 2.4 Navigable
- 2.5 Input Modalities

**3. Understandable**
- 3.1 Readable
- 3.2 Predictable
- 3.3 Input Assistance

**4. Robust**
- 4.1 Compatible (parsing, name/role/value)

---

## Tool Ecosystem

### Automated Testing Tools

**Browser Extensions**:
- **axe DevTools** (Deque): Industry-leading automated scanner
- **WAVE** (WebAIM): Visual feedback, color contrast
- **Accessibility Insights** (Microsoft): Guided assessments, tab stops
- **ANDI** (SSA): Accessible Name & Description Inspector
- **HTML_CodeSniffer**: WCAG 2.1 validation

**Command Line / CI/CD**:
- **axe-core** (JavaScript): Programmatic testing, CI/CD integration
- **Pa11y**: Automated testing, configurable standards
- **Lighthouse** (Chrome): Performance + accessibility scoring
- **eslint-plugin-jsx-a11y**: React accessibility linting
- **axe-playwright / axe-puppeteer**: Browser automation testing

**Color & Contrast**:
- **Colour Contrast Analyser** (Paciello Group): WCAG contrast checking
- **Stark** (Figma/Sketch plugin): Design tool integration
- **WebAIM Contrast Checker**: Online tool
- **Colorblindly**: Color blindness simulation

### Manual Testing Tools

**Screen Readers**:
- **NVDA** (Windows): Free, most popular for testing
- **JAWS** (Windows): Industry standard, enterprise usage
- **VoiceOver** (macOS/iOS): Built-in, Apple ecosystem
- **TalkBack** (Android): Built-in, Android ecosystem
- **Narrator** (Windows): Built-in, Windows ecosystem

**Browser Testing**:
- **Keyboard-only testing**: Unplug mouse, test all functionality
- **Browser zoom**: Test at 200% zoom (WCAG 1.4.4)
- **Text spacing**: Increase line height, letter/word spacing (WCAG 1.4.12)
- **Windows High Contrast Mode**: Force colors mode

**Assistive Technology**:
- **Dragon NaturallySpeaking**: Voice control testing
- **Switch Control** (iOS/Android): Single-switch navigation
- **Eye tracking**: Tobii, eye gaze systems

### Design & Development Tools

**Design Systems**:
- **Material Design** (Google): Accessible components, guidelines
- **Fluent UI** (Microsoft): WCAG-compliant React components
- **Adobe Spectrum**: Accessible design system
- **GOV.UK Design System**: Public sector accessibility

**Development Frameworks**:
- **Reach UI** (React): Accessible component primitives
- **Radix UI** (React): Unstyled accessible components
- **Headless UI** (React/Vue): Tailwind-compatible accessible components
- **Angular Material**: Accessible Angular components

**Documentation**:
- **WAI-ARIA Authoring Practices**: Official W3C patterns
- **A11y Project**: Community-driven checklist, resources
- **WebAIM**: Training, articles, testing tools
- **Deque University**: Comprehensive accessibility training

### Audit & Compliance

**Professional Services**:
- **Deque**: Consulting, audits, training
- **Level Access**: Enterprise accessibility platform
- **TPGi (Paciello Group)**: Audits, VPAT creation
- **WebAIM**: Non-profit, training, audits

**VPAT (Voluntary Product Accessibility Template)**:
- Section 508 compliance documentation
- Required for US federal procurement
- Templates: ITI VPAT 2.4 (WCAG 2.1 aligned)

---

## Changelog

### Version 1.1 (2025-11-20)

**Added**:
- Table of Contents with anchor links
- Implementation Tiers (Core/Standard/Excellence)
- Comprehensive Measurement Framework section
- Tool Ecosystem section (automated, manual, design/dev tools)
- Cross-reference to UX Manifesto
- Principle-specific WCAG guideline mappings
- Success metrics and targets
- Jurisdictional legal requirements
- Changelog section

**Enhanced**:
- Principle XV (Testing & Validation): Expanded tool recommendations
  - Automated: axe-core, Pa11y, Lighthouse, eslint-plugin-jsx-a11y
  - Screen readers: NVDA, JAWS, VoiceOver, TalkBack, Narrator
  - Color tools: Colour Contrast Analyser, Stark, Colorblindly
  - CI/CD: axe-playwright, axe-puppeteer integration
- Measurement Framework: Specific targets and KPIs
- Corollaries: Added "Performance is Accessibility"
- Each principle: Added implementation tier and WCAG mapping

**Improved**:
- Document structure: Clearer hierarchy, navigation
- Actionable checklists: Per-tier implementation guidance
- Business case: Cost analysis (10% → 10× → 100×)
- Legal context: ADA, Section 508, EAA, AODA

### Version 1.0 (2025-11-20)

**Initial Release**:
- 15 foundational accessibility principles
- POUR framework alignment (WCAG 2.1)
- Corollaries section
- WCAG quick reference
- Basic testing & validation guidance

---

## Contributing

This manifesto is public domain (CC0). Contributions welcome:

1. **Feedback**: Open issues for suggestions, questions, or corrections
2. **Improvements**: Submit pull requests for clarifications, examples, or tools
3. **Case Studies**: Share adoption stories and lessons learned
4. **Translations**: Help make accessible to global community

**Contribution Guidelines**:
- Follow existing structure and tone
- Provide concrete examples and metrics
- Cite WCAG 2.1 success criteria where applicable
- Test recommendations with real assistive technology

---

## References & Further Reading

**Standards**:
- **WCAG 2.1**: [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) (W3C)
- **ARIA**: [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) (W3C)
- **Section 508**: [US Federal Accessibility Standards](https://www.section508.gov/)
- **EN 301 549**: European accessibility standard

**Organizations**:
- **WebAIM**: Web Accessibility in Mind (training, articles, tools)
- **Deque University**: Comprehensive accessibility training
- **A11y Project**: Community-driven accessibility resources
- **The Paciello Group (TPGi)**: Accessibility research and consulting

**Books**:
- *Inclusive Design Patterns* by Heydon Pickering
- *Accessibility for Everyone* by Laura Kalbag
- *A Web for Everyone* by Sarah Horton & Whitney Quesenbery

**Legal Resources**:
- ADA settlements database (Seyfarth Shaw)
- WebAIM Million: Annual accessibility analysis

---

**End of Manifesto**

*"Accessibility is not a feature. It's a fundamental human right, a legal requirement, and—when done well—better design for everyone."*
