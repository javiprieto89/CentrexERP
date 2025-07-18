import strawberry
from app.schemas.tmpregistros_stock import TmpRegistroStockType
from app.crud.tmpregistros_stock import get_all_tmpregistros_stock
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpregistros_stock(self, info) -> List[TmpRegistroStockType]:
        db = next(get_db())
        return get_all_tmpregistros_stock(db)