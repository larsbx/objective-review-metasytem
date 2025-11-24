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

### PROHIBITED
- **Hardcoded Secrets**: Score `-15`.
- **Ignoring Critical CVEs**: Score `-15`.
- **Dark Patterns**: Score `-18`.
- **Plaintext Passwords**: Score `-15`.
- **Addictive Mechanics**: Score `-12`.
- **Selling Data w/o Consent**: Score `-12`.
- **Crunch Culture**: Score `-12`.
- **Black Box Authoritarianism**: Score `-27`.

---

## 🔒 Security Hardening

### OBLIGATORY
- **Assume Breach**: Design for compromise.
- **Enforce Least Privilege**: Default deny.
- **Input Validation**: Whitelist only.
- **Secrets Management**: Use vault, no code commits.
- **Secure by Default**: No default passwords.

### PROHIBITED
- **Hardcoded Secrets**
- **Plaintext Passwords**
- **SQL Injection** (String concatenation)
- **Ignoring Critical CVEs**

---

## 💻 Vibe Coding

### OBLIGATORY
- **Collaborative Aesthetics**: Use auto-formatters.
- **Aesthetic Legibility**: Reads like prose.
- **Intentional Naming**: Clear, descriptive names.
- **Obviousness Over Cleverness**
- **Literate Programming**: Explain *why*.

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
- **Semantic HTML**

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

### PROHIBITED
- **Unverified Critical Code** (in safety-critical systems)
- **Ignoring Counterexamples**
- **Runtime Validation Only** (when static is possible)
