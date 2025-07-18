import strawberry
from typing import List, Optional
from app.schemas.permisos import PermisoType
from app.db import SessionLocal
from app.crud.permisos import get_permiso, get_permisos

@strawberry.type
class PermisoQueries:
    @strawberry.field
    def permisos(self, skip: int = 0, limit: int = 100) -> List[PermisoType]:
        db = SessionLocal()
        result = get_permisos(db, skip=skip, limit=limit)
        db.close()
        return [
            PermisoType(
                id_permiso=c.id_permiso,
                nombre=c.nombre,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def permiso(self, id_permiso: int) -> Optional[PermisoType]:
        db = SessionLocal()
        c = get_permiso(db, id_permiso)
        db.close()
        if not c:
            return None
        return PermisoType(
            id_permiso=c.id_permiso,
            nombre=c.nombre,
            descripcion=c.descripcion
        )
