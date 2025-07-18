import strawberry

@strawberry.type
class ComprobanteCompraImpuestoType:
    id_impuesto: int
    id_comprobante_compra: int
    tipo_impuesto: int
    importe: float

@strawberry.input
class ComprobanteCompraImpuestoInput:
    id_comprobante_compra: int
    tipo_impuesto: int
    importe: float
