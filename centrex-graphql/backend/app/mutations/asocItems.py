import strawberry
from typing import Optional
from app.schemas.asocItems import AsocItemType, AsocItemInput
from app.db import SessionLocal
from app.crud.asocItems import create_asocitem, update_asocitem, delete_asocitem

@strawberry.type
class AsocItemMutations:
    @strawberry.mutation
    def create_asocitem(self, data: AsocItemInput) -> AsocItemType:
        db = SessionLocal()
        new_asocitem = create_asocitem(db, data.__dict__)
        db.close()
        return AsocItemType(**new_asocitem.__dict__)

    @strawberry.mutation
    def update_asocitem(self, id_asocItem: int, data: AsocItemInput) -> Optional[AsocItemType]:
        db = SessionLocal()
        updated = update_asocitem(db, id_asocItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return AsocItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_asocitem(self, id_asocItem: int) -> bool:
        db = SessionLocal()
        result = delete_asocitem(db, id_asocItem)
        db.close()
        return result
