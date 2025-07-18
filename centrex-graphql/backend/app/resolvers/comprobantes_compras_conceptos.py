import strawberry
from typing import List, Optional
from app.schemas.comprobantes_compras_conceptos import ComprobanteCompraConceptoType
from app.db import SessionLocal
from app.crud.comprobantes_compras_conceptos import get_comprobante_compra_concepto, get_comprobantes_compras_conceptos

@strawberry.type
class ComprobanteCompraConceptoQueries:
    @strawberry.field
    def comprobantes_compras_conceptos(self, skip: int = 0, limit: int = 100) -> List[ComprobanteCompraConceptoType]:
        db = SessionLocal()
        result = get_comprobantes_compras_conceptos(db, skip=skip, limit=limit)
        db.close()
        return [
            ComprobanteCompraConceptoType(
                id_concepto=c.id_concepto,
                id_comprobante_compra=c.id_comprobante_compra,
                descripcion=c.descripcion,
                importe=float(c.importe)
            ) for c in result
        ]

    @strawberry.field
    def comprobante_compra_concepto(self, id_concepto: int) -> Optional[ComprobanteCompraConceptoType]:
        db = SessionLocal()
        c = get_comprobante_compra_concepto(db, id_concepto)
        db.close()
        if not c:
            return None
        return ComprobanteCompraConceptoType(
            id_concepto=c.id_concepto,
            id_comprobante_compra=c.id_comprobante_compra,
            descripcion=c.descripcion,
            importe=float(c.importe)
        )
