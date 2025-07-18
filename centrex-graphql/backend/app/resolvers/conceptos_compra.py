import strawberry
from typing import List, Optional
from app.schemas.conceptos_compra import ConceptoCompraType
from app.db import SessionLocal
from app.crud.conceptos_compra import get_concepto_compra, get_conceptos_compra

@strawberry.type
class ConceptoCompraQueries:
    @strawberry.field
    def conceptos_compra(self, skip: int = 0, limit: int = 100) -> List[ConceptoCompraType]:
        db = SessionLocal()
        result = get_conceptos_compra(db, skip=skip, limit=limit)
        db.close()
        return [
            ConceptoCompraType(
                id_concepto=c.id_concepto,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def concepto_compra(self, id_concepto: int) -> Optional[ConceptoCompraType]:
        db = SessionLocal()
        c = get_concepto_compra(db, id_concepto)
        db.close()
        if not c:
            return None
        return ConceptoCompraType(
            id_concepto=c.id_concepto,
            descripcion=c.descripcion
        )
