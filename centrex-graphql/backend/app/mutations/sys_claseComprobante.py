import strawberry
from typing import Optional
from app.schemas.sys_claseComprobante import SysClaseComprobanteType, SysClaseComprobanteInput
from app.db import SessionLocal
from app.crud.sys_claseComprobante import (
    create_sysclaseComprobante,
    update_sysclaseComprobante,
    delete_sysclaseComprobante,
    get_sysclaseComprobante_by_id,
)

@strawberry.type
class SysClaseComprobanteMutations:
    @strawberry.mutation
    def create_sys_clase_comprobante(self, data: SysClaseComprobanteInput) -> SysClaseComprobanteType:
        db = SessionLocal()
        new_obj = create_sysclaseComprobante(db, data.__dict__)
        db.close()
        return SysClaseComprobanteType(**new_obj.__dict__)

    @strawberry.mutation
    def update_sys_clase_comprobante(self, id_claseComprobante: int, data: SysClaseComprobanteInput) -> Optional[SysClaseComprobanteType]:
        db = SessionLocal()
        updated = update_sysclaseComprobante(db, id_claseComprobante, data.__dict__)
        db.close()
        if not updated:
            return None
        return SysClaseComprobanteType(**updated.__dict__)

    @strawberry.mutation
    def delete_sys_clase_comprobante(self, id_claseComprobante: int) -> bool:
        db = SessionLocal()
        obj = get_sysclaseComprobante_by_id(db, id_claseComprobante)
        if not obj:
            db.close()
            return False
        delete_sysclaseComprobante(db, obj)
        db.close()
        return True