import strawberry
from datetime import datetime

@strawberry.type
class AjusteStockType:
    id_ajuste_stock: int
    fecha: datetime
    id_usuario: int
    motivo: str | None
    id_item: int
    cantidad: float
    comentario: str | None
    activo: bool

@strawberry.input
class AjusteStockInput:
    fecha: datetime
    id_usuario: int
    motivo: str | None = None
    id_item: int
    cantidad: float
    comentario: str | None = None
    activo: bool = True
