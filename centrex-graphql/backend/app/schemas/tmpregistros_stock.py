import strawberry
from typing import Optional

@strawberry.type
class TmpRegistroStockType:
    id_tmpRegistroStock: int
    id_tmpOperacionStock: int
    id_item: int
    cantidad: float

@strawberry.input
class TmpRegistroStockInput:
    id_tmpOperacionStock: int
    id_item: int
    cantidad: float