import argparse
import os

def parse():
    pass

def desugar():
    pass

def first_inlining():
    pass

def propagate_constant():
    pass

def lower_data_structure():
    pass

def build_code():
    pass

def optimize():
    pass

def compile(src_code: str) -> str:
    src_ast = parse(src_code)
    IR = desugar(src_ast)
    IR = first_inlining(IR)
    IR = propagate_constant(IR)
    IR = lower_data_structure(IR)
    tar_code = build_code(IR)
    tar_code = optimize(tar_code)
    return tar_code

def main(src_path: str, tar_path: str):
    with open(src_path, "r") as f:
        src_code = f.read()
    tar_code = compile(src_code)
    with open(tar_path, "w") as f:
        f.write(tar_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src_path", help="Source file path (e.g., main.py)")
    parser.add_argument("-o", "--output", dest="tar_path",
                        help="Output file path (optional). If not given, use input name with .ow")

    args = parser.parse_args()

    if args.tar_path is None:
        base, _ = os.path.splitext(args.src_path)
        args.tar_path = base + ".ow"

    main(args.src_path, args.tar_path)
