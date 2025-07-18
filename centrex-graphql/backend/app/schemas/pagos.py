import strawberry
from datetime import datetime

@strawberry.type
class PagoType:
    id_pago: int
    id_proveedor: int
    fecha: datetime
    total: float
    estado: str | None
    observaciones: str | None

@strawberry.input
class PagoInput:
    id_proveedor: int
    fecha: datetime
    total: float
    estado: str | None = None
    observaciones: str | None = None
