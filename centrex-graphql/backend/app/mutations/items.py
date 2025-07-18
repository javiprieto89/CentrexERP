import strawberry
from typing import Optional
from app.schemas.items import ItemType, ItemInput
from app.db import SessionLocal
from app.crud.items import create_item, update_item, delete_item

@strawberry.type
class ItemMutations:
    @strawberry.mutation
    def create_item(self, data: ItemInput) -> ItemType:
        db = SessionLocal()
        new_obj = create_item(db, data.__dict__)
        db.close()
        return ItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_item(self, id_item: int, data: ItemInput) -> Optional[ItemType]:
        db = SessionLocal()
        updated = update_item(db, id_item, data.__dict__)
        db.close()
        if not updated:
            return None
        return ItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_item(self, id_item: int) -> bool:
        db = SessionLocal()
        result = delete_item(db, id_item)
        db.close()
        return result
