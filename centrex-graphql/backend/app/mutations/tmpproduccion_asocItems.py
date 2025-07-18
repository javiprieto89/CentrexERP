import strawberry
from typing import Optional
from app.schemas.tmpproduccion_asocItems import TmpProduccionAsocItemType, TmpProduccionAsocItemInput
from app.db import SessionLocal
from app.crud.tmpproduccion_asocItems import create_tmpproduccion_asocItem, update_tmpproduccion_asocItem, delete_tmpproduccion_asocItem

@strawberry.type
class TmpProduccionAsocItemMutations:
    @strawberry.mutation
    def create_tmp_produccion_asocitem(self, data: TmpProduccionAsocItemInput) -> TmpProduccionAsocItemType:
        db = SessionLocal()
        new_obj = create_tmpproduccion_asocItem(db, data.__dict__)
        db.close()
        return TmpProduccionAsocItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_produccion_asocitem(self, id_tmpProduccionAsocItem: int, data: TmpProduccionAsocItemInput) -> Optional[TmpProduccionAsocItemType]:
        db = SessionLocal()
        updated = update_tmpproduccion_asocItem(db, id_tmpProduccionAsocItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpProduccionAsocItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_produccion_asocitem(self, id_tmpProduccionAsocItem: int) -> bool:
        db = SessionLocal()
        result = delete_tmpproduccion_asocItem(db, id_tmpProduccionAsocItem)
        db.close()
        return result