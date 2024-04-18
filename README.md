# python import exercise

## structure of this repo

```python

$ tree .

.
├── Makefile
├── misc
└── src
    ├── __init__.py       # 🟢 (1) this one inits the src as package
    ├── submod_1
    │   ├── __init__.py   # 🟢 (2) this one inits the submod_1 as package, needed for importing inits
    │   ├── mod_1_1
    │   │   └── bla.py
    │   └── mod_1_2
    │       └── bar.py
    └── submod_2
        ├── __init__.py   # 🟢 (3) this one inits the submod_2 as package, entirely optional
        ├── mod_2_1
        │   └── multi.py
        └── mod_2_2
            └── flat.py

```

### prerequisites

if using vs-code, the `PYTHONPATH` env var needs to be set to the root of the repo, this is done via the `.vscode/settings.json` if using this repo.

### tests

the **first** one `make empty_inits` merely uses empty inits placed at the beginning of the package `src/` in our case. it only needs `(1)` to function. python will interpret folders and py files as parts of the import address.

the **second** one `make importing_inits` makes use of the submodule init file `(2)`, which only imports some symbols from its modules `mod_1_1` and `mod_1_2`.
other imports will fail, as not imported in the `submod_1` init file. also, importing directly from `submod_1` will not work because it is nested in `src`, thus its address is `src.submod_1`

the `(3)` init file is entirely optional and could be used in a way it is used in the other submodule in the preceding example.

## resources

* https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
* https://stackoverflow.com/questions/53653083/how-to-correctly-set-pythonpath-for-visual-studio-code