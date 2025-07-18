import strawberry
from typing import Optional
from app.schemas.sysMoneda import SysMonedaType, SysMonedaInput
from app.db import SessionLocal
from app.crud.sysMoneda import (
    create_sysMoneda,
    update_sysMoneda,
    delete_sysMoneda,
    get_sysMoneda_by_id,
)

@strawberry.type
class SysMonedaMutations:
    @strawberry.mutation
    def create_sysMoneda(self, data: SysMonedaInput) -> SysMonedaType:
        db = SessionLocal()
        new_obj = create_sysMoneda(db, data.__dict__)
        db.close()
        return SysMonedaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_sysMoneda(self, id_moneda: int, data: SysMonedaInput) -> Optional[SysMonedaType]:
        db = SessionLocal()
        updated = update_sysMoneda(db, id_moneda, data.__dict__)
        db.close()
        if not updated:
            return None
        return SysMonedaType(**updated.__dict__)

    @strawberry.mutation
    def delete_sysMoneda(self, id_moneda: int) -> bool:
        db = SessionLocal()
        obj = get_sysMoneda_by_id(db, id_moneda)
        if not obj:
            db.close()
            return False
        delete_sysMoneda(db, obj)
        db.close()
        return True