import strawberry
from app.schemas.tmpcobros_retenciones import TmpCobroRetencionType
from app.crud.tmpcobros_retenciones import get_all_tmpcobros_retenciones
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpcobros_retenciones(self, info) -> List[TmpCobroRetencionType]:
        db = next(get_db())
        return get_all_tmpcobros_retenciones(db)