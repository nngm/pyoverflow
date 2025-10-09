# OverFlow

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/license/MIT)
[![Stars](https://img.shields.io/github/stars/nngm/pyoverflow?style=social)](https://github.com/nngm/pyoverflow/stargazers)

This is a `Python` to `overwatch workshop script` compiler.

You can write your workshop code in `main.py` and compile.

```sh
conda create -n overwatch "python<3.12"
conda activate overwatch
./init
```
Write your Python code in main.py

```sh
pip install .
overflow main.py
```

`Final` means it will be inlined in the workshop script.
The first line of docstrings in each function will be the rule name.
