import strawberry
from datetime import datetime

@strawberry.type
class ChequeType:
    id_cheque: int
    numero: str
    banco: str
    emisor: str
    fecha_emision: datetime
    fecha_vencimiento: datetime
    monto: float
    estado: str
    depositado: bool
    observaciones: str | None

@strawberry.input
class ChequeInput:
    numero: str
    banco: str
    emisor: str
    fecha_emision: datetime
    fecha_vencimiento: datetime
    monto: float
    estado: str
    depositado: bool = False
    observaciones: str | None = None
