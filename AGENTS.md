# Repository Guidelines

## Project Structure & Module Organization
- `main.py` – author your Workshop DSL scenario; serves as the user entry.
- `src/` – library code.
  - `src/DSL/` – runtime DSL (events, rules, values, types). Keep side‑effect free; `actions.py` is a placeholder.
  - `src/compiler/` – compiler pipeline (`compile.py`) and CLI.
  - `src/overwatch.py` – convenience re‑exports for DSL symbols.
- Scripts: `init.sh` (set language), `compile.sh` (compile to `.ow`).
- Config: `config.yaml` with `language: en|ko`.
- Assets: `workshop.json` (reference of actions/rules).

## Build, Test, and Development Commands
- Python: use 3.11 (Python < 3.12 per README).
- Setup: `pip install -r requirements.txt` (needs `pyyaml`, `tree_sitter`, `tree_sitter_languages`).
- Init language: `./init.sh`.
- Compile: `./compile.sh` or `python src/compiler/compile.py main.py -o output.ow`.
- Quick run: `python main.py` to exercise DSL evaluation in Python.

## Coding Style & Naming Conventions
- Follow PEP 8, 4‑space indentation; add type hints.
- Names: `snake_case` for functions/vars, `PascalCase` for classes, `UPPER_SNAKE` for constants (e.g., `ALL_TEAMS`, `MELEE`).
- DSL modules (`src/DSL/*`) should avoid I/O and global side effects. Prefer pure helpers that operate on provided context.
- Docstrings: the first line of a function’s docstring becomes the Workshop rule name.

## Testing Guidelines
- Framework: pytest (planned). Place tests under `tests/` with files like `test_values.py`, `test_rules.py`.
- Run: `pytest -q`.
- Aim for unit tests around: condition evaluation (`compare`, `is_button_held`), array helpers (`filtered_array`, `count_of`), and compiler stages as they are implemented.

## Commit & Pull Request Guidelines
- Commits: imperative, concise subjects (≈50 chars). Examples: "Add workshop_setting", "Format code".
- PRs: include a summary, rationale, linked issues, reproduction/verification steps, and before/after snippets (e.g., sample `main.py` and generated `.ow`). Update README/docs when behavior changes. Keep diffs focused.

## Security & Configuration Tips
- `config.yaml` should not contain secrets; only `language` is expected.
- Keep DSL runtime deterministic; avoid filesystem/network access in `src/DSL/*`.
