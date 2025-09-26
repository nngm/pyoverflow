# SingleFlow-overwatch

This is a `Python` to `overwatch workshop script` compiler.

You can write your workshop code in `main.py` and compile.

```sh
conda create -n overwatch "python<3.12"
conda activate overwatch
./init
```
Write your Python code in main.py

```sh
./compile
```

`Final` means it will be inlined in the workshop script.
The first line of docstrings in each function will be the rule name.