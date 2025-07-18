import strawberry
from typing import Optional

@strawberry.type
class SysModoMiPymeType:
    id_modoMiPyme: int
    nombre: str
    descripcion: Optional[str]

@strawberry.input
class SysModoMiPymeInput:
    nombre: str
    descripcion: Optional[str] = None