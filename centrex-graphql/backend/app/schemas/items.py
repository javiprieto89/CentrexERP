import strawberry

@strawberry.type
class ItemType:
    id_item: int
    descripcion: str
    precio: float
    codigo: str | None
    stock: float | None

@strawberry.input
class ItemInput:
    descripcion: str
    precio: float
    codigo: str | None = None
    stock: float | None = 0
