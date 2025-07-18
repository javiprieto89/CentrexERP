import strawberry
from typing import Optional

@strawberry.type
class SysClaseComprobanteType:
    id_claseComprobante: int
    nombre: str
    descripcion: Optional[str]

@strawberry.input
class SysClaseComprobanteInput:
    nombre: str
    descripcion: Optional[str] = None