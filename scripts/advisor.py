#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
An interactive command-line tool to provide tailored recommendations
on which code review manifestos to adopt.
"""

import yaml
from pathlib import Path
import argparse
import sys

# --- Configuration ---
SRC_ROOT = Path(__file__).parent.parent
AGENTS_DIR = SRC_ROOT / "dist" / "agents"

# --- Helper Functions ---

def load_agent_data(filename):
    """Loads a YAML file from the agents directory."""
    filepath = AGENTS_DIR / filename
    if not filepath.exists():
        print(f"Error: Required data file not found at {filepath}")
        print("Please run 'python scripts/build_agents_data.py' first.")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def print_recommendation(primary, secondary, rationale):
    """Prints a formatted recommendation."""
    print("\n--- Recommendation ---")
    print(f"✅ Primary Manifesto: {primary.replace('-', ' ').title()}")
    if secondary:
        print(f"➡️ Also Consider: {', '.join([s.replace('-', ' ').title() for s in secondary])}")
    print(f"\nRationale: {rationale}")
    print("----------------------\n")

def interactive_advisor(decision_tree):
    """Runs the interactive selection guide."""
    print("--- Manifesto Advisor ---")
    print("Please answer the following questions to get a recommendation.")

    # 1. Ask about priority
    priorities = [rule['condition']['value'] for rule in decision_tree['manifesto_selection']['rules']]
    print("\nWhat is your primary priority for this project?")
    for i, p in enumerate(priorities, 1):
        print(f"  {i}. {p.replace('-', ' ').title()}")

    try:
        choice = int(input(f"Enter number (1-{len(priorities)}): "))
        if 1 <= choice <= len(priorities):
            selected_priority = priorities[choice - 1]
            for rule in decision_tree['manifesto_selection']['rules']:
                if rule['condition']['value'] == selected_priority:
                    print_recommendation(rule['primary'], rule.get('secondary', []), rule['rationale'])
                    break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the advisor."""
    parser = argparse.ArgumentParser(description="A CLI tool to recommend code review manifestos.")
    parser.add_argument(
        '--priority',
        choices=['safety-critical-system', 'user-facing-product', 'data-intensive', 'general-software'],
        help='Select a project priority for a non-interactive recommendation.'
    )
    args = parser.parse_args()

    # Load the decision data
    decision_tree = load_agent_data("decision-trees.yaml")

    if args.priority:
        # Non-interactive mode
        for rule in decision_tree['manifesto_selection']['rules']:
            if rule['condition']['value'] == args.priority:
                print_recommendation(rule['primary'], rule.get('secondary', []), rule['rationale'])
                break
    else:
        # Interactive mode
        interactive_advisor(decision_tree)

if __name__ == "__main__":
    main()
