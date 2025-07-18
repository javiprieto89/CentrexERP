import strawberry
from datetime import datetime

@strawberry.type
class CobroType:
    id_cobro: int
    id_cliente: int
    fecha: datetime
    monto_total: float
    forma_pago: str
    observaciones: str | None

@strawberry.input
class CobroInput:
    id_cliente: int
    fecha: datetime
    monto_total: float
    forma_pago: str
    observaciones: str | None = None
