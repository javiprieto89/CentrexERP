import strawberry

@strawberry.type
class ProduccionItemType:
    id_produccion_item: int
    id_produccion: int
    id_item: int
    cantidad: float

@strawberry.input
class ProduccionItemInput:
    id_produccion: int
    id_item: int
    cantidad: float
