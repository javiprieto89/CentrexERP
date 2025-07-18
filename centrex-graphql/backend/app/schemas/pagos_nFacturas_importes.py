import strawberry

@strawberry.type
class PagoNFacturaImporteType:
    id_pago_factura: int
    id_pago: int
    id_factura: int
    importe: float

@strawberry.input
class PagoNFacturaImporteInput:
    id_pago: int
    id_factura: int
    importe: float
