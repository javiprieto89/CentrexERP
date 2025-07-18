import strawberry

@strawberry.type
class CobroNFacturaImporteType:
    id_cobro_nfactura_importe: int
    id_cobro: int
    id_factura: int
    importe: float

@strawberry.input
class CobroNFacturaImporteInput:
    id_cobro: int
    id_factura: int
    importe: float
