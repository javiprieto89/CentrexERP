import strawberry
from typing import Optional
from app.schemas.ordenesCompras_items import OrdenCompraItemType, OrdenCompraItemInput
from app.db import SessionLocal
from app.crud.ordenesCompras_items import create_orden_compra_item, update_orden_compra_item, delete_orden_compra_item

@strawberry.type
class OrdenCompraItemMutations:
    @strawberry.mutation
    def create_orden_compra_item(self, data: OrdenCompraItemInput) -> OrdenCompraItemType:
        db = SessionLocal()
        new_obj = create_orden_compra_item(db, data.__dict__)
        db.close()
        return OrdenCompraItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_orden_compra_item(self, id_orden_item: int, data: OrdenCompraItemInput) -> Optional[OrdenCompraItemType]:
        db = SessionLocal()
        updated = update_orden_compra_item(db, id_orden_item, data.__dict__)
        db.close()
        if not updated:
            return None
        return OrdenCompraItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_orden_compra_item(self, id_orden_item: int) -> bool:
        db = SessionLocal()
        result = delete_orden_compra_item(db, id_orden_item)
        db.close()
        return result
