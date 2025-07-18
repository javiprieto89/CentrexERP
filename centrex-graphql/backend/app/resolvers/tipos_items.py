import strawberry
from app.schemas.tipos_items import TipoItemType
from app.crud.tipos_items import get_all_tipos_items
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tipos_items(self, info) -> List[TipoItemType]:
        db = next(get_db())
        return get_all_tipos_items(db)