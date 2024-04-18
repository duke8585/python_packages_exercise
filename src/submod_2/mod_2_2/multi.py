# NOTE importing from non-empty __init__.py

from src.submod_1 import bar, bla

print(bla, bar)

try:
    from src.submod_1 import bor, blo
    print(bor, blo)
except ImportError:
    print("Failed to import bor, blo")
    # NOTE this is because the submodule (src/submod_1/__init__.py) does not import them

try:
    from submod_1 import bar, bla
    print(bla, bar)
except ImportError:
    print("Failed to import bar, bla from this module")
    # NOTE likely because submod_1 is a submodule to src and cannot be addressed directly

