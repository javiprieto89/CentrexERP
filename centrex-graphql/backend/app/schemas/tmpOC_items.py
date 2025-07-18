import strawberry
from typing import Optional

@strawberry.type
class TmpOCItemType:
    id_tmpOCItem: int
    id_tmpOC: int
    id_item: int
    cantidad: float
    precioUnitario: float
    subtotal: float

@strawberry.input
class TmpOCItemInput:
    id_tmpOC: int
    id_item: int
    cantidad: float
    precioUnitario: float
    subtotal: float