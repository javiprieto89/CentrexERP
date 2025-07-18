import strawberry
from datetime import datetime

@strawberry.type
class ProduccionType:
    id_produccion: int
    fecha: datetime
    estado: str | None
    observaciones: str | None

@strawberry.input
class ProduccionInput:
    fecha: datetime
    estado: str | None = None
    observaciones: str | None = None
