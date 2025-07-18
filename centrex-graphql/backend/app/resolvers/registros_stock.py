import strawberry
from app.schemas.registros_stock import RegistroStockType
from app.crud.registros_stock import get_all_registros_stock
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def registros_stock(self, info) -> List[RegistroStockType]:
        db = next(get_db())
        return get_all_registros_stock(db)
