import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.pagos import PagoType
from app.db import SessionLocal
from app.crud.pagos import get_pago, get_pagos

@strawberry.type
class PagoQueries:
    @strawberry.field
    def pagos(self, skip: int = 0, limit: int = 100) -> List[PagoType]:
        db = SessionLocal()
        result = get_pagos(db, skip=skip, limit=limit)
        db.close()
        return [
            PagoType(
                id_pago=c.id_pago,
                id_proveedor=c.id_proveedor,
                fecha=c.fecha,
                total=float(cast(Decimal, c.total)),
                estado=c.estado,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def pago(self, id_pago: int) -> Optional[PagoType]:
        db = SessionLocal()
        c = get_pago(db, id_pago)
        db.close()
        if not c:
            return None
        return PagoType(
            id_pago=c.id_pago,
            id_proveedor=c.id_proveedor,
            fecha=c.fecha,
            total=float(cast(Decimal, c.total)),
            estado=c.estado,
            observaciones=c.observaciones
        )
