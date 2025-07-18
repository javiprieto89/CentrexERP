import strawberry
from datetime import datetime

@strawberry.type
class ComprobanteType:
    id_comprobante: int
    id_cliente: int
    fecha: datetime
    tipo_comprobante: str
    numero: str
    total: float
    estado: str | None
    observaciones: str | None

@strawberry.input
class ComprobanteInput:
    id_cliente: int
    fecha: datetime
    tipo_comprobante: str
    numero: str
    total: float
    estado: str | None = None
    observaciones: str | None = None
