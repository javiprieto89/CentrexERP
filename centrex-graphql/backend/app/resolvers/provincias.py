import strawberry
from typing import List, Optional
from app.schemas.provincias import ProvinciaType
from app.db import SessionLocal
from app.crud.provincias import get_provincia, get_provincias

@strawberry.type
class ProvinciaQueries:
    @strawberry.field
    def provincias(self, skip: int = 0, limit: int = 100) -> List[ProvinciaType]:
        db = SessionLocal()
        result = get_provincias(db, skip=skip, limit=limit)
        db.close()
        return [
            ProvinciaType(
                id_provincia=c.id_provincia,
                nombre=c.nombre,
                id_pais=c.id_pais
            ) for c in result
        ]

    @strawberry.field
    def provincia(self, id_provincia: int) -> Optional[ProvinciaType]:
        db = SessionLocal()
        c = get_provincia(db, id_provincia)
        db.close()
        if not c:
            return None
        return ProvinciaType(
            id_provincia=c.id_provincia,
            nombre=c.nombre,
            id_pais=c.id_pais
        )
