import strawberry
from typing import Optional
from app.schemas.tmpOC_items import TmpOCItemType, TmpOCItemInput
from app.db import SessionLocal
from app.crud.tmpOC_items import (
    create_tmpOC_item,
    update_tmpOC_item,
    delete_tmpOC_item,
    get_tmpOC_items_by_id,
)

@strawberry.type
class TmpOCItemMutations:
    @strawberry.mutation
    def create_tmp_oc_item(self, data: TmpOCItemInput) -> TmpOCItemType:
        db = SessionLocal()
        new_obj = create_tmpOC_item(db, data.__dict__)
        db.close()
        return TmpOCItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_oc_item(self, id_tmpOCItem: int, data: TmpOCItemInput) -> Optional[TmpOCItemType]:
        db = SessionLocal()
        updated = update_tmpOC_item(db, id_tmpOCItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpOCItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_oc_item(self, id_tmpOCItem: int) -> bool:
        db = SessionLocal()
        obj = get_tmpOC_items_by_id(db, id_tmpOCItem)
        if not obj:
            db.close()
            return False
        delete_tmpOC_item(db, obj)
        db.close()
        return True