import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.produccion_items import ProduccionItemType
from app.db import SessionLocal
from app.crud.produccion_items import get_produccion_item, get_produccion_items

@strawberry.type
class ProduccionItemQueries:
    @strawberry.field
    def produccion_items(self, skip: int = 0, limit: int = 100) -> List[ProduccionItemType]:
        db = SessionLocal()
        result = get_produccion_items(db, skip=skip, limit=limit)
        db.close()
        return [
            ProduccionItemType(
                id_produccion_item=c.id_produccion_item,
                id_produccion=c.id_produccion,
                id_item=c.id_item,
                cantidad=float(cast(Decimal, c.cantidad))
            ) for c in result
        ]

    @strawberry.field
    def produccion_item(self, id_produccion_item: int) -> Optional[ProduccionItemType]:
        db = SessionLocal()
        c = get_produccion_item(db, id_produccion_item)
        db.close()
        if not c:
            return None
        return ProduccionItemType(
            id_produccion_item=c.id_produccion_item,
            id_produccion=c.id_produccion,
            id_item=c.id_item,
            cantidad=float(cast(Decimal, c.cantidad))
        )
