import strawberry
from typing import List, Optional
from app.schemas.ordenes_compras import OrdenCompraType
from app.db import SessionLocal
from app.crud.ordenes_compras import get_orden_compra, get_ordenes_compras

@strawberry.type
class OrdenCompraQueries:
    @strawberry.field
    def ordenes_compras(self, skip: int = 0, limit: int = 100) -> List[OrdenCompraType]:
        db = SessionLocal()
        result = get_ordenes_compras(db, skip=skip, limit=limit)
        db.close()
        return [
            OrdenCompraType(
                id_orden=c.id_orden,
                id_proveedor=c.id_proveedor,
                fecha=c.fecha,
                estado=c.estado,
                total=float(c.total) if c.total is not None else None,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def orden_compra(self, id_orden: int) -> Optional[OrdenCompraType]:
        db = SessionLocal()
        c = get_orden_compra(db, id_orden)
        db.close()
        if not c:
            return None
        return OrdenCompraType(
            id_orden=c.id_orden,
            id_proveedor=c.id_proveedor,
            fecha=c.fecha,
            estado=c.estado,
            total=float(c.total) if c.total is not None else None,
            observaciones=c.observaciones
        )
