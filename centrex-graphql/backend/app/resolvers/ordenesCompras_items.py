import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.ordenesCompras_items import OrdenCompraItemType
from app.db import SessionLocal
from app.crud.ordenesCompras_items import get_orden_compra_item, get_ordenes_compras_items

@strawberry.type
class OrdenCompraItemQueries:
    @strawberry.field
    def ordenes_compras_items(self, skip: int = 0, limit: int = 100) -> List[OrdenCompraItemType]:
        db = SessionLocal()
        result = get_ordenes_compras_items(db, skip=skip, limit=limit)
        db.close()
        return [
            OrdenCompraItemType(
                id_orden_item=c.id_orden_item,
                id_orden=c.id_orden,
                id_item=c.id_item,
                cantidad=float(cast(Decimal, c.cantidad)),
                precio_unitario=float(cast(Decimal, c.precio_unitario)),
                subtotal=float(cast(Decimal, c.subtotal))
            ) for c in result
        ]

    @strawberry.field
    def orden_compra_item(self, id_orden_item: int) -> Optional[OrdenCompraItemType]:
        db = SessionLocal()
        c = get_orden_compra_item(db, id_orden_item)
        db.close()
        if not c:
            return None
        return OrdenCompraItemType(
            id_orden_item=c.id_orden_item,
            id_orden=c.id_orden,
            id_item=c.id_item,
            cantidad=float(cast(Decimal, c.cantidad)),
            precio_unitario=float(cast(Decimal, c.precio_unitario)),
            subtotal=float(cast(Decimal, c.subtotal))
        )
