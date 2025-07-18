import strawberry
from app.schemas.separador_decimal import SeparadorDecimalType
from app.crud.separador_decimal import get_all_separador_decimal
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def separador_decimal(self, info) -> List[SeparadorDecimalType]:
        db = next(get_db())
        return get_all_separador_decimal(db)
