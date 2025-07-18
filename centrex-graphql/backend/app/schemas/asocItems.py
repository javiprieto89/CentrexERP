import strawberry

@strawberry.type
class AsocItemType:
    id_asocItem: int
    id_item_padre: int
    id_item_hijo: int
    cantidad: int

@strawberry.input
class AsocItemInput:
    id_item_padre: int
    id_item_hijo: int
    cantidad: int
