import strawberry
from datetime import datetime

@strawberry.type
class CCProveedorType:
    id_cc_proveedor: int
    id_proveedor: int
    fecha: datetime
    tipo: int
    id_comprobante: int | None
    detalle: int | None
    debe: float | None
    haber: float | None
    saldo: float | None

@strawberry.input
class CCProveedorInput:
    id_proveedor: int
    fecha: datetime
    tipo: int
    id_comprobante: int | None = None
    detalle: int | None = None
    debe: float | None = None
    haber: float | None = None
    saldo: float | None = None
