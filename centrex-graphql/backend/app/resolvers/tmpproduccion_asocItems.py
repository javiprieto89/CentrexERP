import strawberry
from app.schemas.tmpproduccion_asocItems import TmpProduccionAsocItemType
from app.crud.tmpproduccion_asocItems import get_all_tmpproduccion_asocItems
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpproduccion_asocItems(self, info) -> List[TmpProduccionAsocItemType]:
        db = next(get_db())
        return get_all_tmpproduccion_asocItems(db)