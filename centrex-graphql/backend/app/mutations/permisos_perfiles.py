import strawberry
from typing import Optional
from app.schemas.permisos_perfiles import PermisoPerfilType, PermisoPerfilInput
from app.db import SessionLocal
from app.crud.permisos_perfiles import create_permiso_perfil, update_permiso_perfil, delete_permiso_perfil

@strawberry.type
class PermisoPerfilMutations:
    @strawberry.mutation
    def create_permiso_perfil(self, data: PermisoPerfilInput) -> PermisoPerfilType:
        db = SessionLocal()
        new_obj = create_permiso_perfil(db, data.__dict__)
        db.close()
        return PermisoPerfilType(**new_obj.__dict__)

    @strawberry.mutation
    def update_permiso_perfil(self, id_permiso_perfil: int, data: PermisoPerfilInput) -> Optional[PermisoPerfilType]:
        db = SessionLocal()
        updated = update_permiso_perfil(db, id_permiso_perfil, data.__dict__)
        db.close()
        if not updated:
            return None
        return PermisoPerfilType(**updated.__dict__)

    @strawberry.mutation
    def delete_permiso_perfil(self, id_permiso_perfil: int) -> bool:
        db = SessionLocal()
        result = delete_permiso_perfil(db, id_permiso_perfil)
        db.close()
        return result
