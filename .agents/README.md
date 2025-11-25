# Machine-Readable Manifesto Data

This directory contains structured, machine-readable extractions from the Objective Review Metasystem optimized for AI agents and automated tooling.

## Purpose

While the main manifestos are written for human comprehension with narrative context, philosophy, and examples, this directory provides:

- **Structured data formats** (YAML/JSON) for programmatic access
- **Decision trees** as executable rule systems
- **Quantifiable metrics** for automated validation
- **Tool mappings** for CI/CD integration
- **Checklists** as actionable task lists

## Target Consumers

- **AI Coding Agents**: Code review assistants, pair programming bots
- **CI/CD Systems**: Automated quality gates and enforcement
- **IDE Extensions**: Real-time principle suggestions
- **Project Management Tools**: Adoption tracking and checklist generation
- **Analysis Tools**: Compliance scoring and gap analysis

## Structure

```
.agents/
├── README.md                          # This file
├── manifesto-index.yaml               # All manifestos metadata
├── principles-registry.yaml           # All principles with metadata
├── decision-trees.yaml                # Selection and conflict resolution logic
├── measurement-frameworks.yaml        # Metrics, KPIs, targets
├── tool-mappings.yaml                 # Tools → principles → languages
├── semantic-relationships.yaml        # Cross-manifesto dependencies
├── implementation-checklists/         # Per-manifesto, per-tier checklists
│   ├── accessibility.yaml
│   ├── content-communication.yaml
│   ├── data-analytics.yaml
│   ├── formal-verification.yaml
│   ├── security-hardening.yaml
│   ├── user-experience.yaml
│   └── vibe-coding.yaml
└── code-examples/                     # Structured example repository
    ├── index.yaml                     # Example registry
    └── by-principle/                  # Examples organized by principle ID
```

## Usage Examples

### For AI Agents

```python
import yaml

# Load principle registry
with open('.agents/principles-registry.yaml') as f:
    principles = yaml.safe_load(f)

# Get all Core tier principles for code review
core_principles = [p for p in principles if p['tier'] == 'core']

# Check if code violates principle constraints
if function_length > principles['vibe-coding-i']['function_max_lines']:
    suggest_refactor()
```

### For CI/CD Pipelines

```yaml
# .github/workflows/code-review.yml
- name: Validate against manifestos
  run: |
    python scripts/validate_principles.py \
      --principles .agents/principles-registry.yaml \
      --metrics .agents/measurement-frameworks.yaml \
      --threshold 0.8
```

### For IDE Extensions

```javascript
// Load decision tree for principle selection
const decisionTree = require('.agents/decision-trees.yaml');

// Suggest manifesto based on file type
function suggestManifesto(fileType) {
  if (fileType === 'component') return decisionTree.ux;
  if (fileType === 'api') return decisionTree['vibe-coding'];
  // ...
}
```

## Relationship to Human Documentation

**These files are automatically extractable from the main manifestos** and should be kept in sync.

- **Source of Truth**: Main manifesto markdown files
- **Derived Data**: This directory (.agents/)
- **Update Process**: When manifestos change, regenerate these files

## Semantic Relationships Preserved

All cross-references, dependencies, and relationships between manifestos are captured in `semantic-relationships.yaml`:

- **Principle overlaps**: Where different manifestos address the same concept
- **Dependencies**: Which principles enable/require others
- **Conflicts**: How to resolve competing guidance
- **Adoption sequences**: Recommended implementation order

## Version Compatibility

Each file includes version metadata matching the source manifesto:

```yaml
metadata:
  schema_version: "1.0"
  manifesto_version: "2.0"
  generated: "2025-11-20"
  source: "../vibe_coding/VIBE_CODING_MANIFESTO.md"
```

## Contributing

These files are generated/maintained alongside the main manifestos. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on updating structured data when changing principles.

---

**Questions?** [Open an issue](../../issues) or see the [main README](../README.md)
