import strawberry
from typing import List, Optional
from app.schemas.items_impuestos import ItemImpuestoType
from app.db import SessionLocal
from app.crud.items_impuestos import get_item_impuesto, get_items_impuestos

@strawberry.type
class ItemImpuestoQueries:
    @strawberry.field
    def items_impuestos(self, skip: int = 0, limit: int = 100) -> List[ItemImpuestoType]:
        db = SessionLocal()
        result = get_items_impuestos(db, skip=skip, limit=limit)
        db.close()
        return [
            ItemImpuestoType(
                id_item_impuesto=c.id_item_impuesto,
                id_item=c.id_item,
                id_impuesto=c.id_impuesto,
                porcentaje=float(c.porcentaje)
            ) for c in result
        ]

    @strawberry.field
    def item_impuesto(self, id_item_impuesto: int) -> Optional[ItemImpuestoType]:
        db = SessionLocal()
        c = get_item_impuesto(db, id_item_impuesto)
        db.close()
        if not c:
            return None
        return ItemImpuestoType(
            id_item_impuesto=c.id_item_impuesto,
            id_item=c.id_item,
            id_impuesto=c.id_impuesto,
            porcentaje=float(c.porcentaje)
        )
