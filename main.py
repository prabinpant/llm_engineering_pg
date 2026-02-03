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

# Week 1 Day 4
# from src.w1d4_tokenizing import run  # Tokenizing practice
# from src.w1d4_memory import run  # Memory/conversation practice
# from src.w1d4_brochure_generator import run  # Brochure generator practice
from src.w2d1 import *

def main():
    print("=" * 50)
    print("LLM Engineering Practice")
    print("=" * 50)
    run()


if __name__ == "__main__":
    main()
