# 5 Rulings

This document compiles the rulings from all manifestos within this project, categorizing them into OBLIGATORY, ENCOURAGED, OPTIONAL, DISCOURAGED, and PROHIBITED actions.

---

## ⚖️ Ethics (The Quantified Ethics Manifesto)

### OBLIGATORY
- **Encryption at Rest and in Transit**: Score `+10`.
- **Access Control (Least Privilege)**: Score `+10`.
- **Input Validation**: Score `+5`.
- **Critical CVE Remediation (<24h)**: Score `+10`.
- **Accessibility (WCAG 2.1 AA)**: Score `+8`.
- **Privacy Compliance**: Score `+13`.
- **Sustainable Pace**: Score `+8`.
- **Bias Audits**: Score `+14`.
- **Explainability**: Score `+10`.

### ENCOURAGED
- **Immutable Infrastructure**: Score `+7`.
- **Comprehensive CI/CD Automation**: Score `+7`.
- **Disaster Recovery Drills**: Score `+7`.
- **Infrastructure as Code (IaC)**: Score `+5`.
- **Domain-Driven Design (DDD)**: Score `+5`.
- **Architecture Decision Records (ADRs)**: Score `+6`.
- **Explicit API Contracts**: Score `+8`.

### OPTIONAL
- Specific technology choices.
- Aesthetic choices not impacting accessibility.
- Experimental features (behind flags).

### DISCOURAGED
- **Manual Deployments**: Score `-7`.
- **In-place Server Patching**: Score `-4`.
- **No Monitoring**: Score `-5`.
- **"God Objects"**: Score `-10`.
- **Premature Microservices**: Score `-7`.
- **"Clever" Code**: Score `-7`.

### PROHIBITED
- **Hardcoded Secrets**: Score `-15`.
- **Ignoring Critical CVEs**: Score `-15`.
- **Dark Patterns**: Score `-18`.
- **Plaintext Passwords**: Score `-15`.
- **Addictive Mechanics**: Score `-12`.
- **Selling Data w/o Consent**: Score `-12`.
- **Crunch Culture**: Score `-12`.
- **Black Box Authoritarianism**: Score `-27`.
- **Training on known-biased data**: Score `-10`.

---

## 🔒 Security Hardening

### OBLIGATORY
- **Assume Breach**: Design for compromise.
- **Enforce Least Privilege**: Default deny.
- **Input Validation**: Whitelist only.
- **Secrets Management**: Use vault, no code commits.
- **Patch Management**: Remediate Critical CVEs within 24 hours.
- **Secure by Default**: No default passwords.

### ENCOURAGED
- **Shift Security Left**: Integrate security into design and code reviews.
- **Immutable Infrastructure**: Replace servers rather than patching them.
- **Defense in Depth**: Layered controls (Network + App + Data).
- **Zero Trust Architecture**: Authenticate every request.
- **Automated Scanning**: SAST, DAST, and SCA in CI/CD.
- **Incident Response**: Automated playbooks and regular drills.

### OPTIONAL
- **Cryptographic Agility**: Abstracting crypto to allow easy rotation.
- **Microsegmentation**: Granular network policies.
- **Chaos Engineering**: Intentionally injecting failure.

### DISCOURAGED
- **Manual Configuration**: Leads to drift and errors.
- **Long-Lived Secrets**: Rotate keys frequently.
- **"Security through Obscurity"**: Hiding logic is not securing it.
- **Fail Open**: Systems must fail closed.

### PROHIBITED
- **Hardcoded Secrets**
- **Plaintext Passwords**
- **SQL Injection** (String concatenation)
- **Ignoring Critical CVEs**
- **Default Credentials**

---

## 💻 Vibe Coding

### OBLIGATORY
- **Collaborative Aesthetics**: Use auto-formatters.
- **Aesthetic Legibility**: Reads like prose.
- **Intentional Naming**: Clear, descriptive names.
- **Obviousness Over Cleverness**
- **Literate Programming**: Explain *why*.
- **Cohesion and Locality**: Group by feature, not by layer.

### ENCOURAGED
- **Immutability by Default**: Transform data, don't mutate.
- **Semantic Density**: High signal-to-noise ratio.
- **Contextual Verbosity**: Explicit at boundaries, terse locally.
- **Joyful Craft**: Refactor for beauty.

### OPTIONAL
- **Type as Documentation**: Make illegal states unrepresentable.
- **Error as Value**: Return `Result<T,E>`.
- **Composition Over Configuration**
- **Visual Symbolism**: Use mathematical symbols if appropriate.

### DISCOURAGED
- **Clever Code**: One-liners that require decoding.
- **Primitive Obsession**: Using `string` for everything.
- **Mutation**: Modifying data in place.
- **Comments explaining "What"**
- **Layered Architecture**: Spreading a feature across many folders.

### PROHIBITED
- **Code Golf**
- **Inconsistent Style**
- **Misleading Names**
- **God Functions**

---

## ♿ Accessibility

### OBLIGATORY
- **Text Alternatives**: Alt text for images.
- **Captions & Transcripts**
- **Keyboard Accessible**: No mouse required.
- **No Keyboard Traps**
- **Error Identification**
- **Semantic HTML**

### ENCOURAGED
- **Color Contrast**: Minimum 4.5:1 (AA).
- **Visible Focus**: Clear focus indicators.
- **Resize Text**: Up to 200% without loss.
- **Consistent Navigation**
- **Descriptive Headings & Labels**

### OPTIONAL
- **Sign Language**
- **Extended Audio Description**
- **Target Size (Enhanced)**: ≥ 44x44px (AAA).
- **No Interruptions**

### DISCOURAGED
- **"Click Here" Links**
- **Positive `tabindex`**
- **Removing Focus Outlines**
- **Autoplay Media**
- **Arbitrary Time Limits**

### PROHIBITED
- **Flashing Content (>3Hz)**
- **Keyboard Traps**
- **Color-Only Information**
- **Inaccessible CAPTCHAs**

---

## 🎨 User Experience

### OBLIGATORY
- **User Primacy**: User goals > system convenience.
- **Accessibility**: Non-negotiable.
- **Privacy & Ethical Design**
- **Clarity and Recognition**
- **Consistency**

### ENCOURAGED
- **Immediate Feedback**: Response within 100ms.
- **Error Prevention**: Constraints and smart defaults.
- **Forgiveness**: Undo and autosave.
- **Progressive Disclosure**
- **Efficiency**: Shortcuts and bulk operations.
- **Findability**

### OPTIONAL
- **Aesthetic Integrity**
- **Performance as Feature**: LCP < 2.5s.
- **Contextual Relevance**
- **Continuous Validation**

### DISCOURAGED
- **"Organizational" Logic**: Exposing internal structures.
- **Dead Ends**: Unhelpful error messages.
- **Mystery Meat Navigation**
- **Slow Response**: >100ms lag.

### PROHIBITED
- **Dark Patterns**
- **Non-Consensual Data Collection**
- **Inaccessible Core Flows**
- **Hostile Design**

---

## 📝 Content & Communication

### OBLIGATORY
- **Clarity as Prime Directive**
- **Design for Reader's Goal**
- **Ensure Accessibility**
- **Treat Content as Product** (Git, Ownership)
- **Empathetic Tone**

### ENCOURAGED
- **Semantic Hierarchy**
- **Progressive Disclosure**
- **Scannability**
- **Searchability**
- **Visual Communication**
- **Code as Communication**
- **Style Guides**

### OPTIONAL
- **Diátaxis Framework**
- **Specific Diagramming Tools**
- **Brand Voice Nuance**

### DISCOURAGED
- **Passive Voice**
- **Jargon & Acronyms**
- **"Click Here"**
- **Inconsistent Terminology**
- **Wall of Text**

### PROHIBITED
- **Deceptive Patterns**
- **Blaming the User**
- **Broken Links**
- **Untested Code Examples**

---

## 📊 Data & Analytics

### OBLIGATORY
- **Treat Data as a Product**
- **Single Source of Truth**
- **Quality by Design**
- **Immutability**
- **Declarative Logic**

### ENCOURAGED
- **Separation of Concerns**
- **Schema as Contract**
- **Lineage & Provenance**
- **Idempotency**
- **Metrics as Code**
- **Data Observability**

### OPTIONAL
- **Data Mesh**
- **Streaming Architecture**
- **Feature Stores**

### DISCOURAGED
- **Dashboard-Driven Development**
- **Copy-Paste Logic**
- **Schema-less Hell**
- **Manual Quality Checks**
- **Non-Deterministic Logic**

### PROHIBITED
- **Destructive Updates** (Overwrite history)
- **Undocumented Tables**
- **Silencing Alerts**
- **Direct Prod Access**

---

## 🔬 Formal Verification

### OBLIGATORY
- **Specify First**: Before coding.
- **Rigorous Testing**
- **Strict Null-Checking**
- **Code Review**

### ENCOURAGED
- **Make Invalid States Unrepresentable**
- **Automate Proofs** (SMT solvers)
- **Design by Contract (DbC)**
- **Static Analysis**

### OPTIONAL
- **Interactive Theorem Proving**
- **Verified Compilation**
- **Verified Cryptography**

### DISCOURAGED
- **Primitive Obsession**
- **"Code First, Spec Later"**
- **Manual Proofs**
- **Over-Verification**

### PROHIBITED
- **Unverified Critical Code** (in safety-critical systems)
- **Ignoring Counterexamples**
- **Runtime Validation Only** (when static is possible)
