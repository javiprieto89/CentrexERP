import strawberry
from typing import Optional

@strawberry.type
class TmpProduccionAsocItemType:
    id_tmpProduccionAsocItem: int
    id_tmpProduccion: int
    id_item: int
    cantidad: float

@strawberry.input
class TmpProduccionAsocItemInput:
    id_tmpProduccion: int
    id_item: int
    cantidad: float