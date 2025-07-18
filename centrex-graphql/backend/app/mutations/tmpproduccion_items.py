import strawberry
from typing import Optional
from app.schemas.tmpproduccion_items import TmpProduccionItemType, TmpProduccionItemInput
from app.db import SessionLocal
from app.crud.tmpproduccion_items import create_tmpproduccion_item, update_tmpproduccion_item, delete_tmpproduccion_item

@strawberry.type
class TmpProduccionItemMutations:
    @strawberry.mutation
    def create_tmp_produccion_item(self, data: TmpProduccionItemInput) -> TmpProduccionItemType:
        db = SessionLocal()
        new_obj = create_tmpproduccion_item(db, data.__dict__)
        db.close()
        return TmpProduccionItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_produccion_item(self, id_tmpProduccionItem: int, data: TmpProduccionItemInput) -> Optional[TmpProduccionItemType]:
        db = SessionLocal()
        updated = update_tmpproduccion_item(db, id_tmpProduccionItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpProduccionItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_produccion_item(self, id_tmpProduccionItem: int) -> bool:
        db = SessionLocal()
        result = delete_tmpproduccion_item(db, id_tmpProduccionItem)
        db.close()
        return result