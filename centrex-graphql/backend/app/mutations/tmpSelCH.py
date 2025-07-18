import strawberry
from typing import Optional
from app.schemas.tmpSelCH import TmpSelCHType, TmpSelCHInput
from app.db import SessionLocal
from app.crud.tmpSelCH import (
    create_tmpSelCH,
    update_tmpSelCH,
    delete_tmpSelCH,
    get_tmpSelCH_by_id,
)

@strawberry.type
class TmpSelCHMutations:
    @strawberry.mutation
    def create_tmp_selch(self, data: TmpSelCHInput) -> TmpSelCHType:
        db = SessionLocal()
        new_obj = create_tmpSelCH(db, data.__dict__)
        db.close()
        return TmpSelCHType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_selch(self, id_tmpSelCH: int, data: TmpSelCHInput) -> Optional[TmpSelCHType]:
        db = SessionLocal()
        updated = update_tmpSelCH(db, id_tmpSelCH, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpSelCHType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_selch(self, id_tmpSelCH: int) -> bool:
        db = SessionLocal()
        obj = get_tmpSelCH_by_id(db, id_tmpSelCH)
        if not obj:
            db.close()
            return False
        delete_tmpSelCH(db, obj)
        db.close()
        return True