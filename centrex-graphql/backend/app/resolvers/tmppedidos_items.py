import strawberry
from app.schemas.tmppedidos_items import TmpPedidoItemType
from app.crud.tmppedidos_items import get_all_tmppedidos_items
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmppedidos_items(self, info) -> List[TmpPedidoItemType]:
        db = next(get_db())
        return get_all_tmppedidos_items(db)