import strawberry
from typing import Optional
from app.schemas.items_impuestos import ItemImpuestoType, ItemImpuestoInput
from app.db import SessionLocal
from app.crud.items_impuestos import create_item_impuesto, update_item_impuesto, delete_item_impuesto

@strawberry.type
class ItemImpuestoMutations:
    @strawberry.mutation
    def create_item_impuesto(self, data: ItemImpuestoInput) -> ItemImpuestoType:
        db = SessionLocal()
        new_obj = create_item_impuesto(db, data.__dict__)
        db.close()
        return ItemImpuestoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_item_impuesto(self, id_item_impuesto: int, data: ItemImpuestoInput) -> Optional[ItemImpuestoType]:
        db = SessionLocal()
        updated = update_item_impuesto(db, id_item_impuesto, data.__dict__)
        db.close()
        if not updated:
            return None
        return ItemImpuestoType(**updated.__dict__)

    @strawberry.mutation
    def delete_item_impuesto(self, id_item_impuesto: int) -> bool:
        db = SessionLocal()
        result = delete_item_impuesto(db, id_item_impuesto)
        db.close()
        return result
