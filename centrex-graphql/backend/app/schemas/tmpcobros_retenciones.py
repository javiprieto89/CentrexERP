import strawberry
from typing import Optional

@strawberry.type
class TmpCobroRetencionType:
    id_tmpCobroRetencion: int
    id_tmpCobro: int
    id_retencion: int
    importe: float

@strawberry.input
class TmpCobroRetencionInput:
    id_tmpCobro: int
    id_retencion: int
    importe: float