"""
LLM Engineering Practice - Main Entry Point
============================================

Run with: python main.py
    or:   uv run start  (after installing with uv)

Uncomment the module you want to run below.
"""

# ============================================
# PRACTICE MODULES - Uncomment one to run
# ============================================

# Week 1
# from week1.w1d4_tokenizing import run   # Tokenizing practice
# from week1.w1d4_memory import run       # Memory/conversation practice
# from week1.w1d4_brochure_generator import run  # Brochure generator
# from week1.w2d1 import run              # Advanced prompting

# Week 2
from week2.gradio_app import run          # Gradio chat app


def main():
    print("=" * 50)
    print("LLM Engineering Practice")
    print("=" * 50)
    run()


if __name__ == "__main__":
    main()
