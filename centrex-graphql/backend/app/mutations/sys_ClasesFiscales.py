import strawberry
from typing import Optional
from app.schemas.sys_ClasesFiscales import SysClaseFiscalType, SysClaseFiscalInput
from app.db import SessionLocal
from app.crud.sys_ClasesFiscales import (
    create_sysClasesFiscales,
    update_sysClasesFiscales,
    delete_sysClasesFiscales,
    get_sysClasesFiscales_by_id,
)

@strawberry.type
class SysClaseFiscalMutations:
    @strawberry.mutation
    def create_sys_clase_fiscal(self, data: SysClaseFiscalInput) -> SysClaseFiscalType:
        db = SessionLocal()
        new_obj = create_sysClasesFiscales(db, data.__dict__)
        db.close()
        return SysClaseFiscalType(**new_obj.__dict__)

    @strawberry.mutation
    def update_sys_clase_fiscal(self, id_claseFiscal: int, data: SysClaseFiscalInput) -> Optional[SysClaseFiscalType]:
        db = SessionLocal()
        updated = update_sysClasesFiscales(db, id_claseFiscal, data.__dict__)
        db.close()
        if not updated:
            return None
        return SysClaseFiscalType(**updated.__dict__)

    @strawberry.mutation
    def delete_sys_clase_fiscal(self, id_claseFiscal: int) -> bool:
        db = SessionLocal()
        obj = get_sysClasesFiscales_by_id(db, id_claseFiscal)
        if not obj:
            db.close()
            return False
        delete_sysClasesFiscales(db, obj)
        db.close()
        return True