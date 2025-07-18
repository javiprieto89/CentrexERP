# stubs/strawberry/__init__.pyi
from dataclasses import dataclass as type
from typing import Any, TypeVar

_T = TypeVar('_T')


def field(resolver: Any = ...) -> Any: ...

class Schema:
    def __init__(self, query: Any, mutation: Any | None = ...) -> None: ...
