import argparse
import sys
import json
import subprocess
from pathlib import Path
from typing import Optional
import yaml
from .compiler import compile


def _read_lang_config(config_path: Path) -> str:
    if config_path.exists():
        with config_path.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            return config.get("language", "en")
    return "en"


def _decide_output_path(src_path: Path, output_arg: Optional[str]) -> Path:
    if output_arg:
        return Path(output_arg).resolve()
    return src_path.with_suffix(".ow")


def _run_pyright(src_path: Path) -> dict | None:
    """
    Run pyright with JSON output. Return parsed dict or None if pyright is not available.
    """
    try:
        print(f"[overflow] Running pyright type check on {src_path}...")
        proc = subprocess.run(
            ["pyright", "--outputjson", str(src_path)],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        print(
            "[overflow] note: pyright not found; skipping type check.", file=sys.stderr
        )
        return None
    except Exception as e:
        print(f"[overflow] warning: failed to run pyright: {e}", file=sys.stderr)
        return None

    out = proc.stdout.strip()
    if not out:
        print("[overflow] warning: pyright produced no output.", file=sys.stderr)
        return None

    try:
        return json.loads(out)
    except json.JSONDecodeError:
        print(
            "[overflow] warning: could not parse pyright JSON output.", file=sys.stderr
        )
        return None


def _summarize_pyright(result: dict) -> tuple[int, int]:
    """
    Return (errors, warnings) and pretty-print a short summary of diagnostics.
    """
    errors = 0
    warnings = 0

    summary = result.get("summary") or {}
    errors = int(summary.get("errorCount", 0))
    warnings = int(summary.get("warningCount", 0))

    return errors, warnings


def _print_pyright_warnings(result: dict, max_items: int = 10) -> None:
    """
    Print up to 'max_items' warning diagnostics (file:line:col message).
    """
    diags = []
    for file_res in result.get("generalDiagnostics", []):
        if file_res.get("severity") == "warning":
            file = file_res.get("file", "<unknown>")
            msg = file_res.get("message", "").replace("\n", " ")
            range_ = file_res.get("range") or {}
            start = range_.get("start") or {}
            line = int(start.get("line", 0)) + 1
            col = int(start.get("character", 0)) + 1
            diags.append(f"{file}:{line}:{col} {msg}")

    if not diags:
        return

    print(
        f"[overflow] pyright warnings ({min(len(diags), max_items)}/{len(diags)} shown):",
        file=sys.stderr,
    )
    for item in diags[:max_items]:
        print(f"  - {item}", file=sys.stderr)
    if len(diags) > max_items:
        print(
            f"  ... {len(diags) - max_items} more warnings not shown", file=sys.stderr
        )


def main():
    parser = argparse.ArgumentParser(
        prog="overflow", description="OverFlow: Python → Overwatch Workshop compiler"
    )
    parser.add_argument("src", help="Source file (e.g., main.py)")
    parser.add_argument(
        "-l", "--lang", choices=["en", "ko"], help="Workshop script language"
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        default=None,
        help="Output path (e.g., output.ow)",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite existing output without asking",
    )
    parser.add_argument(
        "--skip-typecheck",
        action="store_true",
        help="Skip running pyright type check before compilation",
    )
    parser.add_argument(
        "--ignore-warnings",
        action="store_true",
        help="Do not print pyright warnings (errors still block compilation)",
    )

    args = parser.parse_args()

    src_path = Path(args.src).resolve()
    project_root = src_path.parent
    config_path = project_root / "config.yaml"

    if not src_path.exists():
        print(f"[overflow] error: source not found: {src_path}", file=sys.stderr)
        return 1
    if not src_path.is_file():
        print(f"[overflow] error: not a file: {src_path}", file=sys.stderr)
        return 1
    if src_path.suffix.lower() != ".py":
        print(
            f"[overflow] warning: source does not have .py extension: {src_path}",
            file=sys.stderr,
        )

    lang = args.lang or _read_lang_config(config_path)
    print(f"[overflow] Language set to: {lang}")

    if not args.skip_typecheck and not args.ignore_warnings and not args.force:
        result = _run_pyright(src_path)
        if result is not None:
            errors, warnings = _summarize_pyright(result)

            print(
                f"[overflow] pyright summary: {errors} error(s), {warnings} warning(s)."
            )

            if warnings and not args.ignore_warnings:
                _print_pyright_warnings(result)

            if errors:
                shown = 0
                print("[overflow] pyright errors (blocking):", file=sys.stderr)
                for g in result.get("generalDiagnostics", []):
                    if g.get("severity") == "error":
                        file = g.get("file", "<unknown>")
                        msg = g.get("message", "").replace("\n", " ")
                        range_ = g.get("range") or {}
                        start = range_.get("start") or {}
                        line = int(start.get("line", 0)) + 1
                        col = int(start.get("character", 0)) + 1
                        print(f"  - {file}:{line}:{col} {msg}", file=sys.stderr)
                        shown += 1
                        if shown >= 10:
                            break
                print(
                    "[overflow] warning: type check failed; aborting compilation.",
                    file=sys.stderr,
                )
                return 11
        else:
            pass

    try:
        src_code = src_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[overflow] error: failed to read source: {e}", file=sys.stderr)
        return 1

    try:
        ow_text = compile.compile(src_code, lang=lang)
    except Exception as e:
        print(f"[overflow] error: compilation failed: {e}", file=sys.stderr)
        return 2

    out_path = _decide_output_path(src_path, args.output)

    if out_path.exists() and not args.force:
        ans = (
            input(
                f"[overflow] warning: '{out_path}' already exists. Overwrite? (Y/n): "
            )
            .strip()
            .lower()
        )
        if ans not in ("y", "yes", ""):
            print("[overflow] cancelled by user.")
            return 0

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(ow_text, encoding="utf-8", newline="\n")
    except Exception as e:
        print(f"[overflow] error: failed to write output: {e}", file=sys.stderr)
        return 3

    print(f"[overflow] Wrote: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
