from functools import _Wrapped
from typing import Any, Callable

def call_highest_priority(method_name) -> Callable[..., _Wrapped[..., Any, ..., Any]]:
    ...

def sympify_method_args(cls):
    ...

def sympify_return(*args) -> Callable[..., _SympifyWrapper]:
    ...

def _sympifyit(arg, retval=None) -> Callable[..., _SympifyWrapper]:
    ...

def __sympifyit(func, arg, retval=None) -> Callable[..., _SympifyWrapper]:
    ...

class _SympifyWrapper:
    def __init__(self, func, args) -> None:
        ...
    
    def make_wrapped(self, cls) -> _Wrapped[..., Any, ..., Any]:
        ...
    


