import strawberry

@strawberry.type
class ProduccionAsocItemType:
    id_asoc: int
    id_produccion: int
    id_item: int
    cantidad: float

@strawberry.input
class ProduccionAsocItemInput:
    id_produccion: int
    id_item: int
    cantidad: float
