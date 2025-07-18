import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.comprobantes_compras import ComprobanteCompraType
from app.db import SessionLocal
from app.crud.comprobantes_compras import get_comprobante_compra, get_comprobantes_compras

@strawberry.type
class ComprobanteCompraQueries:
    @strawberry.field
    def comprobantes_compras(self, skip: int = 0, limit: int = 100) -> List[ComprobanteCompraType]:
        db = SessionLocal()
        result = get_comprobantes_compras(db, skip=skip, limit=limit)
        db.close()
        return [
            ComprobanteCompraType(
                id_comprobante_compra=c.id_comprobante_compra,
                id_proveedor=c.id_proveedor,
                fecha=c.fecha,
                tipo_comprobante=c.tipo_comprobante,
                numero=c.numero,
                total=float(cast(Decimal, c.total)),
                estado=c.estado,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def comprobante_compra(self, id_comprobante_compra: int) -> Optional[ComprobanteCompraType]:
        db = SessionLocal()
        c = get_comprobante_compra(db, id_comprobante_compra)
        db.close()
        if not c:
            return None
        return ComprobanteCompraType(
            id_comprobante_compra=c.id_comprobante_compra,
            id_proveedor=c.id_proveedor,
            fecha=c.fecha,
            tipo_comprobante=c.tipo_comprobante,
            numero=c.numero,
            total=float(cast(Decimal, c.total)),
            estado=c.estado,
            observaciones=c.observaciones
        )
