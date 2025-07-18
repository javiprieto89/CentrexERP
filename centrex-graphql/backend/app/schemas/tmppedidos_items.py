import strawberry
from typing import Optional

@strawberry.type
class TmpPedidoItemType:
    id_tmpPedidoItem: int
    id_tmpPedido: int
    id_item: int
    cantidad: float
    precioUnitario: float
    subtotal: float

@strawberry.input
class TmpPedidoItemInput:
    id_tmpPedido: int
    id_item: int
    cantidad: float
    precioUnitario: float
    subtotal: float