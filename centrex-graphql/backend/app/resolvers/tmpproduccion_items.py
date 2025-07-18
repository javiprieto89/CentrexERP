import strawberry
from app.schemas.tmpproduccion_items import TmpProduccionItemType
from app.crud.tmpproduccion_items import get_all_tmpproduccion_items
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpproduccion_items(self, info) -> List[TmpProduccionItemType]:
        db = next(get_db())
        return get_all_tmpproduccion_items(db)