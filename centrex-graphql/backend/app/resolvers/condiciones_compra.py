import strawberry
from typing import List, Optional
from app.schemas.condiciones_compra import CondicionCompraType
from app.db import SessionLocal
from app.crud.condiciones_compra import get_condicion_compra, get_condiciones_compra

@strawberry.type
class CondicionCompraQueries:
    @strawberry.field
    def condiciones_compra(self, skip: int = 0, limit: int = 100) -> List[CondicionCompraType]:
        db = SessionLocal()
        result = get_condiciones_compra(db, skip=skip, limit=limit)
        db.close()
        return [
            CondicionCompraType(
                id_condicion=c.id_condicion,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def condicion_compra(self, id_condicion: int) -> Optional[CondicionCompraType]:
        db = SessionLocal()
        c = get_condicion_compra(db, id_condicion)
        db.close()
        if not c:
            return None
        return CondicionCompraType(
            id_condicion=c.id_condicion,
            descripcion=c.descripcion
        )
