import strawberry
from app.schemas.tmpOC_items import TmpOCItemType
from app.crud.tmpOC_items import get_all_tmpOC_items
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpOC_items(self, info) -> List[TmpOCItemType]:
        db = next(get_db())
        return get_all_tmpOC_items(db)