import strawberry
from typing import List, Optional
from app.schemas.pedidos_items import PedidoItemType
from app.db import SessionLocal
from app.crud.pedidos_items import get_pedido_item, get_pedidos_items

@strawberry.type
class PedidoItemQueries:
    @strawberry.field
    def pedidos_items(self, skip: int = 0, limit: int = 100) -> List[PedidoItemType]:
        db = SessionLocal()
        result = get_pedidos_items(db, skip=skip, limit=limit)
        db.close()
        return [
            PedidoItemType(
                id_pedido_item=c.id_pedido_item,
                id_pedido=c.id_pedido,
                id_item=c.id_item,
                cantidad=float(c.cantidad),
                precio_unitario=float(c.precio_unitario),
                subtotal=float(c.subtotal)
            ) for c in result
        ]

    @strawberry.field
    def pedido_item(self, id_pedido_item: int) -> Optional[PedidoItemType]:
        db = SessionLocal()
        c = get_pedido_item(db, id_pedido_item)
        db.close()
        if not c:
            return None
        return PedidoItemType(
            id_pedido_item=c.id_pedido_item,
            id_pedido=c.id_pedido,
            id_item=c.id_item,
            cantidad=float(c.cantidad),
            precio_unitario=float(c.precio_unitario),
            subtotal=float(c.subtotal)
        )
