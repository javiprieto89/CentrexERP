import strawberry
from typing import Optional
from app.schemas.empresa import EmpresaType, EmpresaInput
from app.db import SessionLocal
from app.crud.empresa import create_empresa, update_empresa, delete_empresa

@strawberry.type
class EmpresaMutations:
    @strawberry.mutation
    def create_empresa(self, data: EmpresaInput) -> EmpresaType:
        db = SessionLocal()
        new_obj = create_empresa(db, data.__dict__)
        db.close()
        return EmpresaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_empresa(self, id_empresa: int, data: EmpresaInput) -> Optional[EmpresaType]:
        db = SessionLocal()
        updated = update_empresa(db, id_empresa, data.__dict__)
        db.close()
        if not updated:
            return None
        return EmpresaType(**updated.__dict__)

    @strawberry.mutation
    def delete_empresa(self, id_empresa: int) -> bool:
        db = SessionLocal()
        result = delete_empresa(db, id_empresa)
        db.close()
        return result
