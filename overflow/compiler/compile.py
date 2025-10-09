import argparse
import os

def parse(src_code: str) -> str:
    return src_code

def desugar(src_ast: str) -> str:
    return src_ast

def first_inlining(IR: str) -> str:
    return IR

def propagate_constant(IR: str) -> str:
    return IR

def lower_data_structure(IR: str) -> str:
    return IR

def build_code(IR: str) -> str:
    return IR

def optimize(tar_code: str) -> str:
    return tar_code

def compile(src_code: str, lang: str = "en") -> str:
    src_ast = parse(src_code)
    IR = desugar(src_ast)
    IR = first_inlining(IR)
    IR = propagate_constant(IR)
    IR = lower_data_structure(IR)
    tar_code = build_code(IR)
    tar_code = optimize(tar_code)
    return tar_code

def main(src_path: str, tar_path: str, lang: str = "en"):
    with open(src_path, "r") as f:
        src_code = f.read()
    tar_code = compile(src_code, lang=lang)
    with open(tar_path, "w") as f:
        f.write(tar_code)
