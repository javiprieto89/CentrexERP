import strawberry
from datetime import datetime

@strawberry.type
class PedidoType:
    id_pedido: int
    id_cliente: int
    fecha: datetime
    estado: str | None
    total: float | None
    observaciones: str | None

@strawberry.input
class PedidoInput:
    id_cliente: int
    fecha: datetime
    estado: str | None = None
    total: float | None = None
    observaciones: str | None = None
