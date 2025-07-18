import strawberry

@strawberry.type
class MarcaItemType:
    id_marca: int
    nombre: str
    descripcion: str | None

@strawberry.input
class MarcaItemInput:
    nombre: str
    descripcion: str | None = None
