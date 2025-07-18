import strawberry
from typing import List, Optional
from app.schemas.permisos_perfiles import PermisoPerfilType
from app.db import SessionLocal
from app.crud.permisos_perfiles import get_permiso_perfil, get_permisos_perfiles

@strawberry.type
class PermisoPerfilQueries:
    @strawberry.field
    def permisos_perfiles(self, skip: int = 0, limit: int = 100) -> List[PermisoPerfilType]:
        db = SessionLocal()
        result = get_permisos_perfiles(db, skip=skip, limit=limit)
        db.close()
        return [
            PermisoPerfilType(
                id_permiso_perfil=c.id_permiso_perfil,
                id_perfil=c.id_perfil,
                id_permiso=c.id_permiso
            ) for c in result
        ]

    @strawberry.field
    def permiso_perfil(self, id_permiso_perfil: int) -> Optional[PermisoPerfilType]:
        db = SessionLocal()
        c = get_permiso_perfil(db, id_permiso_perfil)
        db.close()
        if not c:
            return None
        return PermisoPerfilType(
            id_permiso_perfil=c.id_permiso_perfil,
            id_perfil=c.id_perfil,
            id_permiso=c.id_permiso
        )
