import strawberry
from typing import Optional
from app.schemas.sys_modoMiPyme import SysModoMiPymeType, SysModoMiPymeInput
from app.db import SessionLocal
from app.crud.sys_modoMiPyme import create_sysmodoMiPyme, update_sysmodoMiPyme, delete_sysmodoMiPyme

@strawberry.type
class SysModoMiPymeMutations:
    @strawberry.mutation
    def create_sys_modo_mipyme(self, data: SysModoMiPymeInput) -> SysModoMiPymeType:
        db = SessionLocal()
        new_obj = create_sysmodoMiPyme(db, data.__dict__)
        db.close()
        return SysModoMiPymeType(**new_obj.__dict__)

    @strawberry.mutation
    def update_sys_modo_mipyme(self, id_modoMiPyme: int, data: SysModoMiPymeInput) -> Optional[SysModoMiPymeType]:
        db = SessionLocal()
        updated = update_sysmodoMiPyme(db, id_modoMiPyme, data.__dict__)
        db.close()
        if not updated:
            return None
        return SysModoMiPymeType(**updated.__dict__)

    @strawberry.mutation
    def delete_sys_modo_mipyme(self, id_modoMiPyme: int) -> bool:
        db = SessionLocal()
        result = delete_sysmodoMiPyme(db, id_modoMiPyme)
        db.close()
        return result