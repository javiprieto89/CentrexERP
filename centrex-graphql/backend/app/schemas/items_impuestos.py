import strawberry

@strawberry.type
class ItemImpuestoType:
    id_item_impuesto: int
    id_item: int
    id_impuesto: int
    porcentaje: float

@strawberry.input
class ItemImpuestoInput:
    id_item: int
    id_impuesto: int
    porcentaje: float
