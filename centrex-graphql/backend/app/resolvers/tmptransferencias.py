import strawberry
from app.schemas.tmptransferencias import TmpTransferenciaType
from app.crud.tmptransferencias import get_all_tmptransferencias
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmptransferencias(self, info) -> List[TmpTransferenciaType]:
        db = next(get_db())
        return get_all_tmptransferencias(db)