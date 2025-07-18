import strawberry
from typing import Optional

@strawberry.type
class SysClaseFiscalType:
    id_claseFiscal: int
    nombre: str
    descripcion: Optional[str]

@strawberry.input
class SysClaseFiscalInput:
    nombre: str
    descripcion: Optional[str] = None