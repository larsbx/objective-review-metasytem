#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
An interactive command-line tool to provide tailored recommendations
on which code review manifestos to adopt using a TUI and LLM.
"""

import yaml
from pathlib import Path
import sys
import os
from dotenv import load_dotenv
import google.generativeai as genai

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, Input

# --- Configuration ---
SRC_ROOT = Path(__file__).parent.parent
AGENTS_DIR = SRC_ROOT / "dist" / "agents"
MODEL_NAME = "gemini-pro"
load_dotenv()

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

# --- TUI Application ---

class AdvisorApp(App):
    """A Textual app to provide code review manifesto advice."""

    CSS_PATH = "advisor.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(
            Static("Please enter your primary concern or area of focus for code review:", id="question"),
            Input(placeholder="e.g., 'Improving code security'", id="concern_input"),
            Button("Get Advice", id="get_advice"),
            Static(id="advice_display")
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when the 'Get Advice' button is pressed."""
        if event.button.id == "get_advice":
            concern_input = self.query_one("#concern_input", Input)
            concern = concern_input.value.strip()
            
            # Input Validation
            if not concern:
                self.query_one("#advice_display", Static).update("Please enter a concern.")
                return
            if len(concern) > 500:
                self.query_one("#advice_display", Static).update("Input too long. Please keep it under 500 characters.")
                return

            # Disable button to prevent double-submit
            event.button.disabled = True
            self.query_one("#advice_display", Static).update("Getting advice...")
            
            # TODO: In a real app, run this in a worker thread to avoid freezing UI
            try:
                advice = self.get_llm_advice(concern)
                self.query_one("#advice_display", Static).update(advice)
            finally:
                event.button.disabled = False

    def get_llm_advice(self, concern: str) -> str:
        """Gets advice from the LLM based on the user's concern."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "Error: GEMINI_API_KEY not found in .env file."

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(MODEL_NAME)

        # For now, just returning a placeholder
        # In the future, we will build a more sophisticated prompt
        prompt = f"Based on the concern '{concern}', which code review manifesto should I adopt?"
        
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"


def main():
    """Main function to run the advisor app."""
    # Load the decision data (or other agent data)
    # This might be used to provide context to the LLM in the future
    decision_tree = load_agent_data("decision-trees.yaml")
    
    app = AdvisorApp()
    app.run()

if __name__ == "__main__":
    main()