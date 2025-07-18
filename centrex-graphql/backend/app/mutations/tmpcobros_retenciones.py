import strawberry
from typing import Optional
from app.schemas.tmpcobros_retenciones import TmpCobroRetencionType, TmpCobroRetencionInput
from app.db import SessionLocal
from app.crud.tmpcobros_retenciones import (
    create_tmpcobro_retencion,
    update_tmpcobro_retencion,
    delete_tmpcobro_retencion,
    get_tmpcobro_retencion_by_id,
)

@strawberry.type
class TmpCobroRetencionMutations:
    @strawberry.mutation
    def create_tmp_cobro_retencion(self, data: TmpCobroRetencionInput) -> TmpCobroRetencionType:
        db = SessionLocal()
        new_obj = create_tmpcobro_retencion(db, data.__dict__)
        db.close()
        return TmpCobroRetencionType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_cobro_retencion(self, id_tmpCobroRetencion: int, data: TmpCobroRetencionInput) -> Optional[TmpCobroRetencionType]:
        db = SessionLocal()
        updated = update_tmpcobro_retencion(db, id_tmpCobroRetencion, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpCobroRetencionType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_cobro_retencion(self, id_tmpCobroRetencion: int) -> bool:
        db = SessionLocal()
        obj = get_tmpcobro_retencion_by_id(db, id_tmpCobroRetencion)
        if not obj:
            db.close()
            return False
        delete_tmpcobro_retencion(db, obj)
        db.close()
        return True