import argparse
import sys
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
