import strawberry
from typing import Optional

@strawberry.type
class TransaccionType:
    id_transaccion: int
    fecha: str
    tipo: str
    importe: float
    descripcion: Optional[str]

@strawberry.input
class TransaccionInput:
    fecha: str
    tipo: str
    importe: float
    descripcion: Optional[str] = None