import strawberry
from typing import Optional

@strawberry.type
class SeparadorDecimalType:
    id_separador: int
    descripcion: str
    simbolo: str

@strawberry.input
class SeparadorDecimalInput:
    descripcion: str
    simbolo: str