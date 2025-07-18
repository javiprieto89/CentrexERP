import strawberry
from typing import List, Optional
from app.schemas.paises import PaisType
from app.db import SessionLocal
from app.crud.paises import get_pais, get_paises

@strawberry.type
class PaisQueries:
    @strawberry.field
    def paises(self, skip: int = 0, limit: int = 100) -> List[PaisType]:
        db = SessionLocal()
        result = get_paises(db, skip=skip, limit=limit)
        db.close()
        return [
            PaisType(
                id_pais=c.id_pais,
                nombre=c.nombre,
                codigo=c.codigo
            ) for c in result
        ]

    @strawberry.field
    def pais(self, id_pais: int) -> Optional[PaisType]:
        db = SessionLocal()
        c = get_pais(db, id_pais)
        db.close()
        if not c:
            return None
        return PaisType(
            id_pais=c.id_pais,
            nombre=c.nombre,
            codigo=c.codigo
        )
