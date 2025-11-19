# require.py
import importlib
import sys

def require(module_name):
    """
    Charge un module Python comme Lua require.
    Renvoie le module entier.
    """
    if module_name in sys.modules:
        return sys.modules[module_name]
    return importlib.import_module(module_name)
