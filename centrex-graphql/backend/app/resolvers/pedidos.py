import strawberry
from typing import List, Optional
from app.schemas.pedidos import PedidoType
from app.db import SessionLocal
from app.crud.pedidos import get_pedido, get_pedidos

@strawberry.type
class PedidoQueries:
    @strawberry.field
    def pedidos(self, skip: int = 0, limit: int = 100) -> List[PedidoType]:
        db = SessionLocal()
        result = get_pedidos(db, skip=skip, limit=limit)
        db.close()
        return [
            PedidoType(
                id_pedido=c.id_pedido,
                id_cliente=c.id_cliente,
                fecha=c.fecha,
                estado=c.estado,
                total=float(c.total) if c.total is not None else None,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def pedido(self, id_pedido: int) -> Optional[PedidoType]:
        db = SessionLocal()
        c = get_pedido(db, id_pedido)
        db.close()
        if not c:
            return None
        return PedidoType(
            id_pedido=c.id_pedido,
            id_cliente=c.id_cliente,
            fecha=c.fecha,
            estado=c.estado,
            total=float(c.total) if c.total is not None else None,
            observaciones=c.observaciones
        )
