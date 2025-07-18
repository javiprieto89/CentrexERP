import strawberry

@strawberry.type
class ComprobanteCompraConceptoType:
    id_concepto: int
    id_comprobante_compra: int
    descripcion: str
    importe: float

@strawberry.input
class ComprobanteCompraConceptoInput:
    id_comprobante_compra: int
    descripcion: str
    importe: float
