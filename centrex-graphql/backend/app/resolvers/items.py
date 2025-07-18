import strawberry
from typing import List, Optional
from app.schemas.items import ItemType
from app.db import SessionLocal
from app.crud.items import get_item, get_items

@strawberry.type
class ItemQueries:
    @strawberry.field
    def items(self, skip: int = 0, limit: int = 100) -> List[ItemType]:
        db = SessionLocal()
        result = get_items(db, skip=skip, limit=limit)
        db.close()
        return [
            ItemType(
                id_item=c.id_item,
                descripcion=c.descripcion,
                precio=float(c.precio),
                codigo=c.codigo,
                stock=float(c.stock) if c.stock is not None else 0.0
            ) for c in result
        ]

    @strawberry.field
    def item(self, id_item: int) -> Optional[ItemType]:
        db = SessionLocal()
        c = get_item(db, id_item)
        db.close()
        if not c:
            return None
        return ItemType(
            id_item=c.id_item,
            descripcion=c.descripcion,
            precio=float(c.precio),
            codigo=c.codigo,
            stock=float(c.stock) if c.stock is not None else 0.0
        )
