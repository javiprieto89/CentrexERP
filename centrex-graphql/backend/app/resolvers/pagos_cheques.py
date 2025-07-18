import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.pagos_cheques import PagoChequeType
from app.db import SessionLocal
from app.crud.pagos_cheques import get_pago_cheque, get_pagos_cheques

@strawberry.type
class PagoChequeQueries:
    @strawberry.field
    def pagos_cheques(self, skip: int = 0, limit: int = 100) -> List[PagoChequeType]:
        db = SessionLocal()
        result = get_pagos_cheques(db, skip=skip, limit=limit)
        db.close()
        return [
            PagoChequeType(
                id_pago_cheque=c.id_pago_cheque,
                id_pago=c.id_pago,
                id_cheque=c.id_cheque,
                monto=float(cast(Decimal, c.monto)),
                fecha_aplicacion=c.fecha_aplicacion
            ) for c in result
        ]

    @strawberry.field
    def pago_cheque(self, id_pago_cheque: int) -> Optional[PagoChequeType]:
        db = SessionLocal()
        c = get_pago_cheque(db, id_pago_cheque)
        db.close()
        if not c:
            return None
        return PagoChequeType(
            id_pago_cheque=c.id_pago_cheque,
            id_pago=c.id_pago,
            id_cheque=c.id_cheque,
            monto=float(cast(Decimal, c.monto)),
            fecha_aplicacion=c.fecha_aplicacion
        )
