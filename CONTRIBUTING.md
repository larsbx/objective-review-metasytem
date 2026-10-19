# Contributing

This repository is intentionally a simple collection of independent skills.

## Change an existing skill

Edit its `skills/<domain>/SKILL.md` directly. Keep the skill self-contained and actionable:

- Preserve YAML frontmatter with only `name` and `description`.
- Make the description specific enough to select the skill from a user request.
- Write body instructions in imperative form.
- Keep requirements distinct from recommendations and examples.
- State evidence limits, assumptions, and exceptions where they affect conclusions.
- Avoid runtime dependencies, generated registries, routing applications, and duplicated metadata.

## Add a skill

Create `skills/<domain>/SKILL.md`. Use lowercase letters, digits, and hyphens for the directory and skill name. Add the skill to the table in [README.md](./README.md).

Add a new skill only when it has a distinct task boundary. Extend an existing skill when the new guidance would trigger for the same requests.

## Review checklist

- The directory contains a `SKILL.md` file.
- Frontmatter parses as YAML and contains non-empty `name` and `description` values.
- The frontmatter name is unique and uses lowercase hyphen-case.
- The body tells an agent what to do, what to verify, and how to report limitations.
- Internal links resolve.
- No instruction depends on the removed advisor or generated agent data.

## License

Contributions are dedicated under [CC0 1.0 Universal](./LICENSE).
