import strawberry

@strawberry.type
class ImpuestoType:
    id_impuesto: int
    nombre: str
    descripcion: str | None
    porcentaje: float

@strawberry.input
class ImpuestoInput:
    nombre: str
    descripcion: str | None = None
    porcentaje: float
