import strawberry
from typing import Optional

@strawberry.type
class TmpSelCHType:
    id_tmpSelCH: int
    nroCheque: str
    id_banco: int
    fecha: str
    importe: float

@strawberry.input
class TmpSelCHInput:
    nroCheque: str
    id_banco: int
    fecha: str
    importe: float