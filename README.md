# LLM Engineering Practice

Hands-on practice with LLM engineering concepts — prompting, tokenization, memory, agents, and more.

## Prerequisites

- **Python 3.11+**
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (recommended) or pip
- A **Google API key** (Gemini) stored in a `.env` file

## Setup

### 1. Clone & enter the repo

```bash
git clone <your-repo-url>
cd llm_engineering_practice
```

### 2. Create a `.env` file

```bash
cp .env.example .env
# Then edit .env and add your API key:
#   GOOGLE_API_KEY=your-key-here
```

### 3. Install dependencies

**With uv (recommended):**

```bash
uv sync
```

**With pip:**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running

Edit `main.py` to uncomment the module you want to run, then:

```bash
# With uv
uv run python main.py

# With pip (after activating the venv)
python main.py
```

Or use the helper script:

```bash
./run.sh
```

## Project Structure

```
├── main.py                  # Entry point — uncomment a module to run it
├── gradio_app.py            # Gradio web UI experiment
├── scraper.py               # Shared web scraping utilities
├── pyproject.toml           # Project metadata & dependencies
├── week1/                   # Week 1 exercises
│   ├── w1d4_tokenizing.py       # Tokenization with tiktoken
│   ├── w1d4_memory.py           # Conversation memory with Gemini
│   ├── w1d4_brochure_generator.py  # Website brochure generator
│   ├── w2d1.py                  # Advanced prompting techniques
│   └── litellm_example.py       # LiteLLM unified API example
├── week2/                   # Week 2 exercises (coming soon)
└── .env                     # Your API keys (not committed)
```

## Adding New Modules

1. Create a new `.py` file in the appropriate `weekN/` folder.
2. Define a `run()` function as the entry point.
3. Add `from weekN.your_module import run` to `main.py`.
