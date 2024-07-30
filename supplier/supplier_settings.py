import os
from typing import Any


def get_from_env(var_name: Any, default: Any = None, kt: Any = str):
    if var_name in os.environ:
        val = os.environ.get(var_name)
    elif var_name in globals():
        val = globals()[var_name]
    else:
        val = default
    if isinstance(val, kt):
        return val
    return None
