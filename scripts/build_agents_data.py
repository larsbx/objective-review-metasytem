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
# MANIFESTO_DIRS removed in favor of dynamic discovery
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

def find_manifesto_file(manifest_dir_path):
    """
    Finds the manifesto file in the given directory.
    Priority:
    1. Ends with _MANIFESTO.md
    2. Any .md file with valid front matter
    """
    if not manifest_dir_path.exists():
        return None
        
    md_files = glob.glob(str(manifest_dir_path / "*.md"))
    if not md_files:
        return None

    # First pass: Look for _MANIFESTO.md
    for md_file in md_files:
        if md_file.endswith("_MANIFESTO.md"):
            return Path(md_file)

    # Second pass: Look for any file with valid front matter
    for md_file in md_files:
        filepath = Path(md_file)
        if read_markdown_front_matter(filepath):
            return filepath

    return None

def discover_manifesto_dirs():
    """
    Dynamically discovers directories containing manifestos.
    Returns a list of Path objects.
    """
    manifesto_dirs = []
    # Look for any directory in SRC_ROOT that contains a *_MANIFESTO.md file
    # This is a heuristic to find manifesto directories
    for item in SRC_ROOT.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['dist', 'scripts', 'integrations']:
            # Check if it contains a manifesto file
            if find_manifesto_file(item):
                manifesto_dirs.append(item)
    return sorted(manifesto_dirs)



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

    manifesto_dirs = discover_manifesto_dirs()
    for manifest_dir_path in manifesto_dirs:
        filepath = find_manifesto_file(manifest_dir_path)

        if not filepath:
            print(f"Warning: No valid manifesto file found in {manifest_dir_path}")
            continue

        front_matter = read_markdown_front_matter(filepath)

        if front_matter and 'id' in front_matter:
            manifesto_id = front_matter['id']
            # Add file paths for context
            front_matter['file_path'] = str(filepath.relative_to(SRC_ROOT.parent)).replace(os.path.sep, '/')
            front_matter['changelog_path'] = str((filepath.parent / "CHANGELOG.md").relative_to(SRC_ROOT.parent)).replace(os.path.sep, '/')
            index_data["manifestos"][manifesto_id] = front_matter
        else:
             print(f"Warning: No valid front matter found in {filepath}")

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

    manifesto_dirs = discover_manifesto_dirs()
    for manifest_dir_path in manifesto_dirs:
        filepath = find_manifesto_file(manifest_dir_path)

        if not filepath:
            continue

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