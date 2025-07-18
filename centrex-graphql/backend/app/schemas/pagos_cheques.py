import strawberry
from datetime import datetime

@strawberry.type
class PagoChequeType:
    id_pago_cheque: int
    id_pago: int
    id_cheque: int
    monto: float
    fecha_aplicacion: datetime | None

@strawberry.input
class PagoChequeInput:
    id_pago: int
    id_cheque: int
    monto: float
    fecha_aplicacion: datetime | None = None
