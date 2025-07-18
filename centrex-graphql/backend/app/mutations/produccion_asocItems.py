import strawberry
from typing import Optional
from app.schemas.produccion_asocItems import ProduccionAsocItemType, ProduccionAsocItemInput
from app.db import SessionLocal
from app.crud.produccion_asocItems import create_produccion_asoc_item, update_produccion_asoc_item, delete_produccion_asoc_item

@strawberry.type
class ProduccionAsocItemMutations:
    @strawberry.mutation
    def create_produccion_asoc_item(self, data: ProduccionAsocItemInput) -> ProduccionAsocItemType:
        db = SessionLocal()
        new_obj = create_produccion_asoc_item(db, data.__dict__)
        db.close()
        return ProduccionAsocItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_produccion_asoc_item(self, id_asoc: int, data: ProduccionAsocItemInput) -> Optional[ProduccionAsocItemType]:
        db = SessionLocal()
        updated = update_produccion_asoc_item(db, id_asoc, data.__dict__)
        db.close()
        if not updated:
            return None
        return ProduccionAsocItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_produccion_asoc_item(self, id_asoc: int) -> bool:
        db = SessionLocal()
        result = delete_produccion_asoc_item(db, id_asoc)
        db.close()
        return result
