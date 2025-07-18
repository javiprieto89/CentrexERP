import strawberry

@strawberry.type
class CondicionCompraType:
    id_condicion: int
    descripcion: str

@strawberry.input
class CondicionCompraInput:
    descripcion: str
