import strawberry

@strawberry.type
class PaisType:
    id_pais: int
    nombre: str
    codigo: str | None

@strawberry.input
class PaisInput:
    nombre: str
    codigo: str | None = None
