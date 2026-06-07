# AI Agent Ollama SQLite

A small experimental repo for exploring AI agents, local LLMs, RAG-style tooling, and automation workflows.

This project combines:
- `langchain` agent creation
- `ollama` local LLM access via `langchain-ollama`
- `gradio` chat UI for easy local interaction
- `langgraph` SQLite checkpointing for agent history persistence
- `TavilySearch` for web search tool integration

## What this repo does

The repository runs a Gradio-based AI chat interface backed by a local Ollama model (`qwen3.5:4b`).
It creates a LangChain agent with:
- a date tool (`get_date()`)
- a web search tool (`TavilySearch`)
- a SQLite checkpointer for saving session history to `agent_history.db`

This is a starting point for experiments in:
- local LLM usage
- multi-tool agent workflows
- retrieval-augmented generation and automation
- simple web UI prototyping

## Requirements

Install the Python dependencies from `requirements.txt`.

```bash
python -m pip install -r requirements.txt
```

## Running the project

```bash
python main.py
```

Then open the local Gradio URL printed in the terminal.

## Notes

- The repo uses `.env` loading via `python-dotenv`, so you can add local configuration in a `.env` file if needed.
- `agent_history.db` is created automatically and stores agent checkpoints.
- The current Ollama model is configured in `main.py` as `qwen3.5:4b`.

## Ideas for experimentation

- swap the Ollama model or test a different local LLM backend
- add more tools for file access, knowledge retrieval, summaries, or automation tasks
- integrate a proper RAG index or vector store
- extend the Gradio UI with additional controls or state

## Project structure

- `main.py` — entry point for the AI agent and Gradio app
- `requirements.txt` — Python dependencies
- `.env` — optional environment config (not committed)
- `agent_history.db` — local SQLite checkpoint store
