# Objective Review Skills

A collection of independent skills for reviewing software, research, data, product design, and engineering decisions.

Each directory under `skills/` is a complete skill. Its `SKILL.md` contains the discovery metadata and the instructions an agent follows. There is no advisor application, generated registry, shared runtime, or model-specific dependency.

## Skills

| Skill | Use it for |
| --- | --- |
| [accessibility-review](./skills/accessibility-review/SKILL.md) | Accessibility audits, inclusive implementation, and WCAG-oriented remediation |
| [content-communication-review](./skills/content-communication-review/SKILL.md) | Documentation, interface copy, error messages, and technical communication |
| [data-analytics-review](./skills/data-analytics-review/SKILL.md) | Reliable data platforms, pipelines, metrics, governance, and observability |
| [formal-verification-review](./skills/formal-verification-review/SKILL.md) | Specifications, proof plans, model checking, and machine-checked assurance |
| [quantified-ethics-review](./skills/quantified-ethics-review/SKILL.md) | Structured ethical analysis of engineering and product trade-offs |
| [research-hygiene-review](./skills/research-hygiene-review/SKILL.md) | Claim status, evidence boundaries, bounded searches, and reproducibility |
| [security-hardening-review](./skills/security-hardening-review/SKILL.md) | Threat-aware review, least privilege, defense in depth, and incident readiness |
| [user-experience-review](./skills/user-experience-review/SKILL.md) | Usability, ethical interaction, privacy, performance, and user success |
| [readable-code-review](./skills/readable-code-review/SKILL.md) | Readability, maintainability, explicit intent, and sustainable code structure |

## Structure

```text
skills/
  <domain>/
    SKILL.md
```

Skill names use lowercase letters and hyphens. Each `SKILL.md` begins with YAML frontmatter containing only `name` and `description`; the body contains the operational guidance.

## Use

Copy or install the skill directory in a skill-capable agent environment. Relevant skills may be selected automatically from their descriptions, or invoked explicitly by name where the environment supports that.

## License

[CC0 1.0 Universal](./LICENSE)
