import strawberry
from typing import List, Optional
from app.schemas.asocItems import AsocItemType
from app.db import SessionLocal
from app.crud.asocItems import get_asocitem, get_asocitems

@strawberry.type
class AsocItemQueries:
    @strawberry.field
    def asocitems(self, skip: int = 0, limit: int = 100) -> List[AsocItemType]:
        db = SessionLocal()
        result = get_asocitems(db, skip=skip, limit=limit)
        db.close()
        return [
            AsocItemType(
                id_asocItem=a.id_asocItem,
                id_item_padre=a.id_item_padre,
                id_item_hijo=a.id_item_hijo,
                cantidad=a.cantidad
            ) for a in result
        ]

    @strawberry.field
    def asocitem(self, id_asocItem: int) -> Optional[AsocItemType]:
        db = SessionLocal()
        a = get_asocitem(db, id_asocItem)
        db.close()
        if not a:
            return None
        return AsocItemType(
            id_asocItem=a.id_asocItem,
            id_item_padre=a.id_item_padre,
            id_item_hijo=a.id_item_hijo,
            cantidad=a.cantidad
        )
