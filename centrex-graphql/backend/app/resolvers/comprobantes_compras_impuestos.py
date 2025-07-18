import strawberry
from typing import List, Optional
from app.schemas.comprobantes_compras_impuestos import ComprobanteCompraImpuestoType
from app.db import SessionLocal
from app.crud.comprobantes_compras_impuestos import get_comprobante_compra_impuesto, get_comprobantes_compras_impuestos

@strawberry.type
class ComprobanteCompraImpuestoQueries:
    @strawberry.field
    def comprobantes_compras_impuestos(self, skip: int = 0, limit: int = 100) -> List[ComprobanteCompraImpuestoType]:
        db = SessionLocal()
        result = get_comprobantes_compras_impuestos(db, skip=skip, limit=limit)
        db.close()
        return [
            ComprobanteCompraImpuestoType(
                id_impuesto=c.id_impuesto,
                id_comprobante_compra=c.id_comprobante_compra,
                tipo_impuesto=c.tipo_impuesto,
                importe=float(c.importe)
            ) for c in result
        ]

    @strawberry.field
    def comprobante_compra_impuesto(self, id_impuesto: int) -> Optional[ComprobanteCompraImpuestoType]:
        db = SessionLocal()
        c = get_comprobante_compra_impuesto(db, id_impuesto)
        db.close()
        if not c:
            return None
        return ComprobanteCompraImpuestoType(
            id_impuesto=c.id_impuesto,
            id_comprobante_compra=c.id_comprobante_compra,
            tipo_impuesto=c.tipo_impuesto,
            importe=float(c.importe)
        )
