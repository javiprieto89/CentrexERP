import strawberry
from typing import List, Optional
from app.schemas.impuestos import ImpuestoType
from app.db import SessionLocal
from app.crud.impuestos import get_impuesto, get_impuestos

@strawberry.type
class ImpuestoQueries:
    @strawberry.field
    def impuestos(self, skip: int = 0, limit: int = 100) -> List[ImpuestoType]:
        db = SessionLocal()
        result = get_impuestos(db, skip=skip, limit=limit)
        db.close()
        return [
            ImpuestoType(
                id_impuesto=c.id_impuesto,
                nombre=c.nombre,
                descripcion=c.descripcion,
                porcentaje=float(c.porcentaje)
            ) for c in result
        ]

    @strawberry.field
    def impuesto(self, id_impuesto: int) -> Optional[ImpuestoType]:
        db = SessionLocal()
        c = get_impuesto(db, id_impuesto)
        db.close()
        if not c:
            return None
        return ImpuestoType(
            id_impuesto=c.id_impuesto,
            nombre=c.nombre,
            descripcion=c.descripcion,
            porcentaje=float(c.porcentaje)
        )
