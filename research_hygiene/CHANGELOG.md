# Changelog - Research Hygiene Manifesto

All notable changes to the Research Hygiene Manifesto will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- A general checker for Rulings II and III, which are currently enforced by tests and review rather than by a tool
- Worked examples in languages other than Python
- A decision tree for choosing which rulings a project has earned

## [1.0] - 2026-09-16

### Added

- Initial manifesto with nine rulings across the core, standard, and excellence tiers
- Core rulings: declare the status of every claim; a refusal is not a negative result; report the bound when you reach it; translation preserves or lowers authority
- Standard rulings: one claims ledger with generated surfaces; controls independent of what they test; terminology declared with its known leaks
- Excellence rulings: differential testing against an independent implementation; a delivery ledger that admits partial delivery
- Reference implementation table mapping rulings to checks in `claim_governance`, with the gaps stated
- Vale styles porting the prose rulings, and a root `.vale.ini` so that `vale **/*.md` runs as CONTRIBUTING describes

### Notes

- Every example is drawn from a defect caught in review rather than invented
