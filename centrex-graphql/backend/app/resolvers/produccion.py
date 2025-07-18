import strawberry
from typing import List, Optional
from app.schemas.produccion import ProduccionType
from app.db import SessionLocal
from app.crud.produccion import get_produccion, get_producciones

@strawberry.type
class ProduccionQueries:
    @strawberry.field
    def producciones(self, skip: int = 0, limit: int = 100) -> List[ProduccionType]:
        db = SessionLocal()
        result = get_producciones(db, skip=skip, limit=limit)
        db.close()
        return [
            ProduccionType(
                id_produccion=c.id_produccion,
                fecha=c.fecha,
                estado=c.estado,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def produccion(self, id_produccion: int) -> Optional[ProduccionType]:
        db = SessionLocal()
        c = get_produccion(db, id_produccion)
        db.close()
        if not c:
            return None
        return ProduccionType(
            id_produccion=c.id_produccion,
            fecha=c.fecha,
            estado=c.estado,
            observaciones=c.observaciones
        )
