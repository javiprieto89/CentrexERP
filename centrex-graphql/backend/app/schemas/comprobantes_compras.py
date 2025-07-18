import strawberry
from datetime import datetime

@strawberry.type
class ComprobanteCompraType:
    id_comprobante_compra: int
    id_proveedor: int
    fecha: datetime
    tipo_comprobante: str
    numero: str
    total: float
    estado: str | None
    observaciones: str | None

@strawberry.input
class ComprobanteCompraInput:
    id_proveedor: int
    fecha: datetime
    tipo_comprobante: str
    numero: str
    total: float
    estado: str | None = None
    observaciones: str | None = None
