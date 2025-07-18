import strawberry
from typing import List, Optional
from app.schemas.perfiles import PerfilType
from app.db import SessionLocal
from app.crud.perfiles import get_perfil, get_perfiles

@strawberry.type
class PerfilQueries:
    @strawberry.field
    def perfiles(self, skip: int = 0, limit: int = 100) -> List[PerfilType]:
        db = SessionLocal()
        result = get_perfiles(db, skip=skip, limit=limit)
        db.close()
        return [
            PerfilType(
                id_perfil=c.id_perfil,
                nombre=c.nombre,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def perfil(self, id_perfil: int) -> Optional[PerfilType]:
        db = SessionLocal()
        c = get_perfil(db, id_perfil)
        db.close()
        if not c:
            return None
        return PerfilType(
            id_perfil=c.id_perfil,
            nombre=c.nombre,
            descripcion=c.descripcion
        )
