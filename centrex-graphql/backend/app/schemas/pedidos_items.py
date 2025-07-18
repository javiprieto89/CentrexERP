import strawberry

@strawberry.type
class PedidoItemType:
    id_pedido_item: int
    id_pedido: int
    id_item: int
    cantidad: float
    precio_unitario: float
    subtotal: float

@strawberry.input
class PedidoItemInput:
    id_pedido: int
    id_item: int
    cantidad: float
    precio_unitario: float
    subtotal: float
