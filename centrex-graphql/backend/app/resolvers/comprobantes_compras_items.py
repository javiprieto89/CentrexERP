import strawberry
from typing import List, Optional
from app.schemas.comprobantes_compras_items import ComprobanteCompraItemType
from app.db import SessionLocal
from app.crud.comprobantes_compras_items import get_comprobante_compra_item, get_comprobantes_compras_items

@strawberry.type
class ComprobanteCompraItemQueries:
    @strawberry.field
    def comprobantes_compras_items(self, skip: int = 0, limit: int = 100) -> List[ComprobanteCompraItemType]:
        db = SessionLocal()
        result = get_comprobantes_compras_items(db, skip=skip, limit=limit)
        db.close()
        return [
            ComprobanteCompraItemType(
                id_item=c.id_item,
                id_comprobante_compra=c.id_comprobante_compra,
                descripcion=c.descripcion,
                cantidad=float(c.cantidad),
                precio_unitario=float(c.precio_unitario),
                subtotal=float(c.subtotal)
            ) for c in result
        ]

    @strawberry.field
    def comprobante_compra_item(self, id_item: int) -> Optional[ComprobanteCompraItemType]:
        db = SessionLocal()
        c = get_comprobante_compra_item(db, id_item)
        db.close()
        if not c:
            return None
        return ComprobanteCompraItemType(
            id_item=c.id_item,
            id_comprobante_compra=c.id_comprobante_compra,
            descripcion=c.descripcion,
            cantidad=float(c.cantidad),
            precio_unitario=float(c.precio_unitario),
            subtotal=float(c.subtotal)
        )
