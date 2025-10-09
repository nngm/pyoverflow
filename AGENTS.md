# Repository Guidelines

## Project Structure & Module Organization
- `main.py` – author your Workshop DSL scenario; serves as the entry point.
- `overflow/` – library code.
  - `overflow/DSL/` – runtime DSL (events, rules, values, types). Keep side‑effect free.
  - `overflow/compiler/` – core compiler pipeline (`compile.py`).
  - `overflow/cli.py` – installed CLI entry (`overflow`).
- `src/compiler/compile.py` – minimal standalone CLI wrapper for local runs.
- `config.yaml` – configuration (`language: en|ko`).
- `workshop.json` – reference of actions/rules.
- `tests/` – pytest tests (planned).

## Build, Test, and Development Commands
- Python: use 3.11 (Python < 3.12).
- Setup: `pip install -r requirements.txt` then `pip install .` for the CLI.
- Init language: `./init.sh` (writes `config.yaml`).
- Compile (installed): `overflow main.py -o output.ow`.
- Compile (MVP): `python src/compiler/compile.py main.py -o output.ow`.
- Quick run DSL in Python: `python main.py` (exercises evaluation only).
- Tests (planned): `pytest -q` from repo root.

## Coding Style & Naming Conventions
- PEP 8, 4‑space indentation; include type hints.
- Names: `snake_case` (functions/vars), `PascalCase` (classes), `UPPER_SNAKE` (constants e.g., `ALL_TEAMS`, `MELEE`).
- DSL modules under `overflow/DSL/*` must be deterministic and side‑effect free (no filesystem/network I/O). Prefer pure helpers operating on provided context.
- Docstrings: the first line of a function’s docstring becomes the Workshop rule name.

## Testing Guidelines
- Framework: `pytest` (planned). Place files under `tests/` (e.g., `test_values.py`, `test_rules.py`).
- Targets: condition evaluation (`compare`, `is_button_held`), array helpers (`filtered_array`, `count_of`), compiler stages as they land.
- Keep tests unit‑level and deterministic.

## Commit & Pull Request Guidelines
- Commits: imperative, concise subject (~50 chars). Examples: "Add workshop_setting", "Format code".
- PRs: include summary, rationale, linked issues, repro/verification steps, and before/after snippets (e.g., sample `main.py` and generated `.ow`). Keep diffs focused and update README/docs when behavior changes.

## Security & Configuration Tips
- `config.yaml` must not contain secrets; only `language` is expected.
- Keep the DSL runtime deterministic; avoid external I/O within `overflow/DSL/*`.
