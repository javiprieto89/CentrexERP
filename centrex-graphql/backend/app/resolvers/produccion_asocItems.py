import strawberry
from typing import List, Optional
from app.schemas.produccion_asocItems import ProduccionAsocItemType
from app.db import SessionLocal
from app.crud.produccion_asocItems import get_produccion_asoc_item, get_produccion_asoc_items

@strawberry.type
class ProduccionAsocItemQueries:
    @strawberry.field
    def produccion_asoc_items(self, skip: int = 0, limit: int = 100) -> List[ProduccionAsocItemType]:
        db = SessionLocal()
        result = get_produccion_asoc_items(db, skip=skip, limit=limit)
        db.close()
        return [
            ProduccionAsocItemType(
                id_asoc=c.id_asoc,
                id_produccion=c.id_produccion,
                id_item=c.id_item,
                cantidad=float(c.cantidad)
            ) for c in result
        ]

    @strawberry.field
    def produccion_asoc_item(self, id_asoc: int) -> Optional[ProduccionAsocItemType]:
        db = SessionLocal()
        c = get_produccion_asoc_item(db, id_asoc)
        db.close()
        if not c:
            return None
        return ProduccionAsocItemType(
            id_asoc=c.id_asoc,
            id_produccion=c.id_produccion,
            id_item=c.id_item,
            cantidad=float(c.cantidad)
        )
