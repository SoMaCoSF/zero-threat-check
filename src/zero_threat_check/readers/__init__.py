"""Reader registry for capability modules."""
from typing import Callable, Dict

READERS: Dict[str, Callable] = {}

def register(name: str):
    def deco(fn):
        READERS[name] = fn
        return fn
    return deco
