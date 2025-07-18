import strawberry
from typing import Optional

@strawberry.type
class RegistroStockType:
    id_registro: int
    id_ingreso: int
    fecha: str
    fecha_ingreso: str
    factura: str
    archivofc: str
    id_proveedor: int
    id_item: int
    cantidad: int
    costo: float
    precio_lista: float
    factor: float
    cantidad_anterior: int
    costo_anterior: float
    precio_lista_anterior: float
    factor_anterior: float
    nota: Optional[str]
    activo: bool

@strawberry.input
class RegistroStockInput:
    id_ingreso: int
    fecha: str
    fecha_ingreso: str
    factura: str
    archivofc: str
    id_proveedor: int
    id_item: int
    cantidad: int
    costo: float
    precio_lista: float
    factor: float
    cantidad_anterior: int
    costo_anterior: float
    precio_lista_anterior: float
    factor_anterior: float
    nota: Optional[str] = None
    activo: bool = True