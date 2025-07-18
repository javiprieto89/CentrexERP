import strawberry
from typing import Optional
from app.schemas.sysestados_cheques import SysEstadoChequeType, SysEstadoChequeInput
from app.db import SessionLocal
from app.crud.sysestados_cheques import (
    create_sysestado_cheque,
    update_sysestado_cheque,
    delete_sysestado_cheque,
    get_sysestados_cheques_by_id,
)

@strawberry.type
class SysEstadoChequeMutations:
    @strawberry.mutation
    def create_sys_estado_cheque(self, data: SysEstadoChequeInput) -> SysEstadoChequeType:
        db = SessionLocal()
        new_obj = create_sysestado_cheque(db, data.__dict__)
        db.close()
        return SysEstadoChequeType(**new_obj.__dict__)

    @strawberry.mutation
    def update_sys_estado_cheque(self, id_estadoCheque: int, data: SysEstadoChequeInput) -> Optional[SysEstadoChequeType]:
        db = SessionLocal()
        updated = update_sysestado_cheque(db, id_estadoCheque, data.__dict__)
        db.close()
        if not updated:
            return None
        return SysEstadoChequeType(**updated.__dict__)

    @strawberry.mutation
    def delete_sys_estado_cheque(self, id_estadoCheque: int) -> bool:
        db = SessionLocal()
        obj = get_sysestados_cheques_by_id(db, id_estadoCheque)
        if not obj:
            db.close()
            return False
        delete_sysestado_cheque(db, obj)
        db.close()
        return True