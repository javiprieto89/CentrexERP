import strawberry
from app.schemas.tipos_comprobantes import TiposComprobantesType
from app.crud.tipos_comprobantes import get_all_tipos_comprobantes
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tipos_comprobantes(self, info) -> List[TiposComprobantesType]:
        db = next(get_db())
        return get_all_tipos_comprobantes(db)
