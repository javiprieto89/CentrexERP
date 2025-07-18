import strawberry

@strawberry.type
class ComprobanteCompraItemType:
    id_item: int
    id_comprobante_compra: int
    descripcion: str
    cantidad: float
    precio_unitario: float
    subtotal: float

@strawberry.input
class ComprobanteCompraItemInput:
    id_comprobante_compra: int
    descripcion: str
    cantidad: float
    precio_unitario: float
    subtotal: float
