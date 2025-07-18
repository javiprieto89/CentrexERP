import strawberry
from typing import Optional

@strawberry.type
class TipoDocumentoType:
    id_tipoDocumento: int
    nombreDocumento: str
    nombreAbreviado: str
    id_claseFiscal: int
    activo: bool

@strawberry.input
class TipoDocumentoInput:
    nombreDocumento: str
    nombreAbreviado: str
    id_claseFiscal: int
    activo: bool = True