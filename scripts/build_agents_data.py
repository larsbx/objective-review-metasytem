#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Builds the machine-readable agent data in dist/agents/
from the YAML front matter in the manifesto Markdown files.
"""

import glob
import os
import shutil
from pathlib import Path
import yaml

# --- Configuration ---
SRC_ROOT = Path(__file__).parent.parent
MANIFESTO_DIRS = [
    "accessibility",
    "content_communication",
    "data_analytics",
    "ethics",
    "formal_verification",
    "security_hardening",
    "user_experience",
    "vibe_coding",
]
DIST_DIR = SRC_ROOT / "dist"
AGENTS_DIR = DIST_DIR / "agents"
MANUAL_AGENT_FILES = ["decision-trees.yaml", "semantic-relationships.yaml"]

# --- Helper Functions ---

def read_markdown_front_matter(filepath):
    """
    Parses YAML front matter from a Markdown file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # A simple way to extract front matter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    front_matter = yaml.safe_load(parts[1])
                    return front_matter
    except Exception as e:
        print(f"Error reading or parsing {filepath}: {e}")
    return None

# --- Main Build Logic ---

def build_manifesto_index():
    """
    Generates manifesto-index.yaml
    """
    index_data = {
        "metadata": {
            "schema_version": "1.1",
            "description": "Index of all manifestos with metadata for AI agent consumption."
        },
        "manifestos": {}
    }

    for manifest_dir in MANIFESTO_DIRS:
        md_files = glob.glob(str(SRC_ROOT / manifest_dir / "*_MANIFESTO.md"))
        if not md_files:
            continue

        # Assuming one manifesto markdown per directory
        filepath = Path(md_files[0])
        front_matter = read_markdown_front_matter(filepath)

        if front_matter and 'id' in front_matter:
            manifesto_id = front_matter['id']
            # Add file paths for context
            front_matter['file_path'] = str(filepath.relative_to(SRC_ROOT.parent)).replace(os.path.sep, '/')
            front_matter['changelog_path'] = str((filepath.parent / "CHANGELOG.md").relative_to(SRC_ROOT.parent)).replace(os.path.sep, '/')
            index_data["manifestos"][manifesto_id] = front_matter

    return index_data

def build_measurement_frameworks():
    """
    Generates measurement-frameworks.yaml
    """
    framework_data = {
        "metadata": {
            "schema_version": "1.1",
            "description": "Quantifiable metrics, KPIs, and success criteria for all manifestos."
        }
    }

    for manifest_dir in MANIFESTO_DIRS:
        md_files = glob.glob(str(SRC_ROOT / manifest_dir / "*_MANIFESTO.md"))
        if not md_files:
            continue

        filepath = Path(md_files[0])
        front_matter = read_markdown_front_matter(filepath)

        if front_matter and 'id' in front_matter and 'measurement' in front_matter:
            manifesto_id = front_matter['id']
            framework_data[manifesto_id] = front_matter['measurement']

    return framework_data

def main():
    """
    Main function to drive the build process.
    """
    print("Starting build process for .agents data...")

    # 1. Clean and recreate destination directory
    if AGENTS_DIR.exists():
        shutil.rmtree(AGENTS_DIR)
    AGENTS_DIR.mkdir(parents=True)
    print(f"Cleaned and created {AGENTS_DIR}")

    # 2. Build manifesto-index.yaml
    manifesto_index = build_manifesto_index()
    index_path = AGENTS_DIR / "manifesto-index.yaml"
    with open(index_path, 'w', encoding='utf-8') as f:
        yaml.dump(manifesto_index, f, default_flow_style=False, sort_keys=False)
    print(f"Generated {index_path}")

    # 3. Build measurement-frameworks.yaml
    measurement_frameworks = build_measurement_frameworks()
    measurement_path = AGENTS_DIR / "measurement-frameworks.yaml"
    with open(measurement_path, 'w', encoding='utf-8') as f:
        yaml.dump(measurement_frameworks, f, default_flow_style=False, sort_keys=False)
    print(f"Generated {measurement_path}")

    # 4. Copy manually maintained files
    manual_files_source_dir = SRC_ROOT / ".agents_manual"

    for filename in MANUAL_AGENT_FILES:
        source_path = manual_files_source_dir / filename
        dest_path = AGENTS_DIR / filename
        if source_path.exists():
            shutil.copy(source_path, dest_path)
            print(f"Copied manual file {filename}")
        else:
            print(f"Warning: Manual file {filename} not found at {source_path}")

    print("Build process complete.")

if __name__ == "__main__":
    main()
