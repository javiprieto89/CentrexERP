import strawberry
from typing import Optional

@strawberry.type
class SysEstadoChequeType:
    id_estadoCheque: int
    nombre: str
    descripcion: Optional[str]

@strawberry.input
class SysEstadoChequeInput:
    nombre: str
    descripcion: Optional[str] = None