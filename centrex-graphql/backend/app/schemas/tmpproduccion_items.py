import strawberry
from typing import Optional

@strawberry.type
class TmpProduccionItemType:
    id_tmpProduccionItem: int
    id_tmpProduccion: int
    id_item: int
    cantidad: float

@strawberry.input
class TmpProduccionItemInput:
    id_tmpProduccion: int
    id_item: int
    cantidad: float