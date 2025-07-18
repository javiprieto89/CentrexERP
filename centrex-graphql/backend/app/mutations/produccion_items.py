import strawberry
from typing import Optional
from app.schemas.produccion_items import ProduccionItemType, ProduccionItemInput
from app.db import SessionLocal
from app.crud.produccion_items import create_produccion_item, update_produccion_item, delete_produccion_item

@strawberry.type
class ProduccionItemMutations:
    @strawberry.mutation
    def create_produccion_item(self, data: ProduccionItemInput) -> ProduccionItemType:
        db = SessionLocal()
        new_obj = create_produccion_item(db, data.__dict__)
        db.close()
        return ProduccionItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_produccion_item(self, id_produccion_item: int, data: ProduccionItemInput) -> Optional[ProduccionItemType]:
        db = SessionLocal()
        updated = update_produccion_item(db, id_produccion_item, data.__dict__)
        db.close()
        if not updated:
            return None
        return ProduccionItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_produccion_item(self, id_produccion_item: int) -> bool:
        db = SessionLocal()
        result = delete_produccion_item(db, id_produccion_item)
        db.close()
        return result
