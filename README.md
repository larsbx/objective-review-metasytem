# Objective Review Metasystem

**A collection of software engineering manifestos for building high-quality, sustainable, and ethical systems.**

The Objective Review Metasystem aggregates and refines software engineering best practices into a set of actionable manifestos. It's designed for both human engineers seeking guidance and for AI agents that need structured, machine-readable data to assist in code review and system design.

---

## 🚀 Getting Started: The Manifesto Advisor

The easiest way to get started is to use the **Manifesto Advisor** tool. It will ask you a few questions about your project and recommend the most relevant manifestos and principles to focus on.

**1. Install Dependencies:**
```bash
# You need Python 3
pip install -r requirements.txt
```

**2. Run the Advisor:**
```bash
python3 scripts/advisor.py
```
This interactive tool is the best entry point for navigating the philosophies in this repository.

---

## The Core Idea: Human-Readable and Machine-Readable

This project has a unique structure:

1.  **Human-Readable Manifestos:** Each directory (e.g., `vibe_coding/`, `security_hardening/`) contains a manifesto written in Markdown for engineers, managers, and designers. They provide the philosophy, examples, and detailed guidance behind each set of principles.

2.  **Machine-Readable Agent Data:** The `dist/agents/` directory contains the same information structured as YAML files. This data is generated from the manifestos and is designed to be used by AI agents, CI/CD pipelines, and other automated tools.

The Markdown files are the **single source of truth**. They contain YAML front matter that our build script uses to generate the agent data.

---

## Project Structure

```
.
├── accessibility/            # Accessibility Manifesto
├── content_communication/    # Content & Communication Manifesto
├── data_analytics/           # Data & Analytics Manifesto
├── ethics/                   # The Quantified Ethics Manifesto
├── formal_verification/      # Formal Verification Manifesto
├── security_hardening/       # Security Hardening Manifesto
├── user_experience/          # User Experience Manifesto
└── vibe_coding/              # Vibe Coding Manifesto
│
├── dist/
│   └── agents/               # Generated machine-readable data (YAML files)
│
├── scripts/
│   ├── advisor.py            # Interactive tool to get recommendations
│   └── build_agents_data.py  # Script to generate the dist/agents/ data
│
├── integrations/
│   ├── vale/                 # Example Vale configuration for prose linting
│   └── github/               # Example GitHub Actions workflow
│
├── README.md                 # This file
└── ...
```

---

## The Manifestos

Each manifesto represents a coherent philosophy for a specific dimension of software quality.

| Icon | Manifesto | Focus |
| :--: | --------- | ----- |
| ⚖️  | **[The Quantified Ethics Manifesto](./ethics/ETHICS_MANIFESTO.md)** | A structured, weighted framework for making ethical trade-offs. |
| ✨  | **[The Vibe Coding Manifesto](./vibe_coding/VIBE_CODING_MANIFESTO.md)** | Code readability, maintainability, and the craft of software development. |
| 🔒  | **[The Security Hardening Manifesto](./security_hardening/SECURITY_HARDENING_MANIFESTO.md)** | Building secure and resilient systems using a proactive, layered approach. |
| ♿  | **[The Accessibility Manifesto](./accessibility/ACCESSIBILITY_MANIFESTO.md)** | Ensuring products are usable by everyone, based on WCAG principles. |
| 🎨  | **[The User Experience Manifesto](./user_experience/UX_MANIFESTO.md)** | Creating products that are effective, efficient, and enjoyable to use. |
| 📝  | **[The Content & Communication Manifesto](./content_communication/CONTENT_COMMUNICATION_MANIFESTO.md)** | Writing clear, accessible, and actionable content for all touchpoints. |
| 📊  | **[The Data & Analytics Manifesto](./data_analytics/DATA_ANALYTICS_MANIFESTO.md)** | Building reliable, scalable, and trustworthy data platforms. |
| 🔬  | **[The Formal Verification Manifesto](./formal_verification/FORMAL_VERIFICATION_MANIFESTO.md)** | Using mathematical proofs to guarantee the correctness of critical systems. |

---

## How It Works: The Automation Engine

This repository is more than just a collection of documents; it's a system.

1.  **Single Source of Truth**: Each Markdown manifesto contains YAML front matter with structured metadata (e.g., `id`, `focus`, `metrics`).
2.  **Build Process**: The `scripts/build_agents_data.py` script iterates through the manifestos, parses the front matter, and generates the structured YAML files in `dist/agents/`. This ensures the human and machine-readable versions never go out of sync.
3.  **Tooling**: The generated data in `dist/agents/` powers tools like the `scripts/advisor.py` and can be used to configure CI/CD checks, IDE extensions, and more. See the `integrations/` directory for examples.

To run the build process yourself:
```bash
python3 scripts/build_agents_data.py
```

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

When editing a manifesto, you are editing the source of truth. After changing a Markdown file, please run the build script to regenerate the agent data and include it in your commit.

## License

**[CC0 1.0 Universal (Public Domain)](./LICENSE)**

To maximize reuse and accessibility, all content in this repository is dedicated to the public domain. You can use, modify, and distribute it freely without attribution.