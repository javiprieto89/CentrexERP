import strawberry
from typing import Optional

@strawberry.type
class TransferenciaType:
    id_transferencia: int
    id_cuentaOrigen: int
    id_cuentaDestino: int
    importe: float
    fecha: str
    observaciones: Optional[str]

@strawberry.input
class TransferenciaInput:
    id_cuentaOrigen: int
    id_cuentaDestino: int
    importe: float
    fecha: str
    observaciones: Optional[str] = None