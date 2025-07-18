import strawberry
from typing import Optional

@strawberry.type
class TmpTransferenciaType:
    id_tmpTransferencia: int
    id_tmpOperacionStockOrigen: int
    id_tmpOperacionStockDestino: int
    fecha: str
    observaciones: Optional[str]

@strawberry.input
class TmpTransferenciaInput:
    id_tmpOperacionStockOrigen: int
    id_tmpOperacionStockDestino: int
    fecha: str
    observaciones: Optional[str] = None