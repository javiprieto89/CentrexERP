import strawberry
from datetime import datetime

@strawberry.type
class OrdenCompraType:
    id_orden: int
    id_proveedor: int
    fecha: datetime
    estado: str | None
    total: float | None
    observaciones: str | None

@strawberry.input
class OrdenCompraInput:
    id_proveedor: int
    fecha: datetime
    estado: str | None = None
    total: float | None = None
    observaciones: str | None = None
