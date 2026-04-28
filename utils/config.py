import os
from pathlib import Path


def load_system_prompt() -> str:
    """Load system prompt from prompt.txt safely."""
    try:
        root_dir = Path(__file__).resolve().parent.parent
        prompt_path = root_dir / "prompt.txt"

        if not prompt_path.exists():
            print(f"[WARNING] prompt.txt not found at: {prompt_path}")
            return "You are a helpful campus assistant."

        prompt_text = prompt_path.read_text(encoding="utf-8").strip()

        if not prompt_text:
            print("[WARNING] prompt.txt is empty.")
            return "You are a helpful campus assistant."

        return prompt_text

    except Exception as e:
        print(f"[ERROR] Failed to load prompt: {e}")
        return "You are a helpful campus assistant."


# ✅ IMPORTANT: always define this (never let import fail)
SYSTEM_PROMPT = load_system_prompt()