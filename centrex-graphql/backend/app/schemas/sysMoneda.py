import strawberry
from typing import Optional

@strawberry.type
class SysMonedaType:
    id_moneda: int
    nombre: str
    simbolo: str
    activo: bool

@strawberry.input
class SysMonedaInput:
    nombre: str
    simbolo: str
    activo: bool = True