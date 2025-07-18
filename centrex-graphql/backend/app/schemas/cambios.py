import strawberry
from datetime import datetime

@strawberry.type
class CambioType:
    id_cambio: int
    fecha: datetime
    id_moneda_origen: int
    id_moneda_destino: int
    valor: float

@strawberry.input
class CambioInput:
    fecha: datetime
    id_moneda_origen: int
    id_moneda_destino: int
    valor: float
