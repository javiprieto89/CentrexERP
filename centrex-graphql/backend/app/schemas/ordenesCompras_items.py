import strawberry

@strawberry.type
class OrdenCompraItemType:
    id_orden_item: int
    id_orden: int
    id_item: int
    cantidad: float
    precio_unitario: float
    subtotal: float

@strawberry.input
class OrdenCompraItemInput:
    id_orden: int
    id_item: int
    cantidad: float
    precio_unitario: float
    subtotal: float
