# Repository Guidelines

## Project Structure & Module Organization
- `overflow/`: Python package and DSL for the compiler.
  - `overflow/cli.py`: CLI entrypoint (`overflow`).
  - `overflow/compiler/compile.py`: compilation pipeline stages.
  - `overflow/DSL/`: DSL primitives, types, and rules.
- `main.py`: example workspace script compiled to Workshop.
- `config.yaml`: language config (`language: en|ko`).
- `pyproject.toml`: package metadata and script entry.
- `requirements.txt`: dev/runtime tools (e.g., `pyright`, `PyYAML`).
- `README.md`, `SPEC.md`, `TODO.md`: docs and roadmap.

## Build, Test, and Development Commands
- Install deps: `pip install -r requirements.txt`
- Local install (provides `overflow` CLI): `pip install .`
- Initialize config (select language): `./init.sh`
- Compile example: `overflow main.py -o output.ow`
- Type check (fast feedback): `pyright main.py`

## Coding Style & Naming Conventions
- Python 3.11; use type hints throughout (pyright-friendly).
- Follow PEP 8: 4-space indents, snake_case for functions/vars, PascalCase for classes.
- Keep modules small and focused; group DSL utilities under `overflow/DSL/`.
- Docstrings: first line succinctly describes rules; keep user-facing names stable.

## Testing Guidelines
- Current status: no formal unit test suite committed.
- Minimum check before PR: `pyright` passes and `overflow main.py` produces a valid `.ow`.
- If adding tests, place them under `tests/` with `test_*.py` names and prefer `pytest` (update requirements accordingly).

## Commit & Pull Request Guidelines
- Commits: imperative, present tense, concise subject (e.g., "Fix CLI overwrite prompt").
- Group related changes; keep diffs minimal and scoped.
- PRs must include: clear description, rationale, before/after behavior, and usage examples/commands. Link related issues.
- For CLI/DSL changes, include a small code snippet in `main.py` (or a new example) showing usage.

## Security & Configuration Tips
- Do not commit secrets. The only config is `config.yaml` (language); safe to commit.
- Keep external tooling optional; the compiler must run offline once installed.
