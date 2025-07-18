# stubs/strawberry/__init__.pyi
from typing import Any, Callable, TypeVar

_T = TypeVar('_T')

def type(cls: _T = ...) -> Callable[[Any], _T]: ...

def field(resolver: Any = ...) -> Any: ...

class Schema:
    def __init__(self, query: Any, mutation: Any | None = ...) -> None: ...
