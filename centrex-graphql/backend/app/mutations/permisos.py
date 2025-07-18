import strawberry
from typing import Optional
from app.schemas.permisos import PermisoType, PermisoInput
from app.db import SessionLocal
from app.crud.permisos import create_permiso, update_permiso, delete_permiso

@strawberry.type
class PermisoMutations:
    @strawberry.mutation
    def create_permiso(self, data: PermisoInput) -> PermisoType:
        db = SessionLocal()
        new_obj = create_permiso(db, data.__dict__)
        db.close()
        return PermisoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_permiso(self, id_permiso: int, data: PermisoInput) -> Optional[PermisoType]:
        db = SessionLocal()
        updated = update_permiso(db, id_permiso, data.__dict__)
        db.close()
        if not updated:
            return None
        return PermisoType(**updated.__dict__)

    @strawberry.mutation
    def delete_permiso(self, id_permiso: int) -> bool:
        db = SessionLocal()
        result = delete_permiso(db, id_permiso)
        db.close()
        return result
