import strawberry
from typing import Optional

@strawberry.type
class TipoItemType:
    id_tipoItem: int
    tipoItem: str
    nombreAbreviado: str
    esProducto: bool
    esServicio: bool

@strawberry.input
class TipoItemInput:
    tipoItem: str
    nombreAbreviado: str
    esProducto: bool = True
    esServicio: bool = False