# GEMINI.md: project context

This file provides instructional context about the `code_review_manifestos` directory for AI assistants.

## Directory overview

This directory contains a collection of software engineering manifestos focused on improving code review and overall system quality. It is a non-code project, primarily consisting of Markdown documents that define coherent philosophies and provide actionable guidance on various aspects of software development.

The project has a unique structure, designed for both human readers and AI agents:
- **Human-Readable Manifestos**: Each topic (e.g., `security_hardening/`) has a `..._MANIFESTO.md` file written for engineers.
- **Machine-Readable Agent Data**: The `dist/agents/` directory contains generated YAML files with structured data, intended for tooling and automation.

The Markdown files, which contain YAML front matter, serve as the single source of truth.

## Project structure
- `accessibility/`, `content_communication/`, etc.: Directories for each manifesto's human-readable Markdown file.
- `dist/agents/`: Contains machine-readable data (YAML) generated from the manifestos.
- `scripts/`: Contains Python scripts for building the agent data and providing interactive advice.
- `integrations/`: Contains example configurations for third-party tools like Vale and GitHub Actions.
- `.agents_manual/`: Stores manually maintained YAML files used by the build script.
- `README.md`: The main entry point to the project.

## Key files

- `README.md`: The main entry point to the project. It explains the project's dual human/machine philosophy and directs users to the `advisor.py` tool.
- `CONTRIBUTING.md`: Details how to contribute, including how to update the manifestos and run the build script.
- `STYLE_GUIDE.md`: Outlines the voice, tone, and formatting standards for all content.
- `*/<MANIFESTO_NAME>_MANIFESTO.md`: The core content. Each manifesto is a detailed document with YAML front matter containing its metadata and metrics.
- `scripts/build_agents_data.py`: A Python script that parses the front matter from all manifestos and generates the content for the `dist/agents/` directory.
- `scripts/advisor.py`: An interactive CLI tool that reads the agent data to provide tailored recommendations to users.
- `dist/agents/*.yaml`: Machine-readable data used by the advisor tool and other automations.

## Usage

The contents of this directory are intended to be used as a reference and a guide for software engineering teams. The primary use cases are:

- **Standardizing Code Review:** Adopting manifestos to create a shared set of principles.
- **Improving Engineering Culture:** Fostering a culture of quality and continuous improvement.
- **Onboarding New Engineers:** Using the documents as a resource for engineering standards.
- **Automated Tooling:** Leveraging the `dist/agents/` data to build bots, CI/CD checks, and IDE extensions.

To get started, a user should run the `scripts/advisor.py` tool for a guided experience.
