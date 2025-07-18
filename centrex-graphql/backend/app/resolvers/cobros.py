import strawberry
from typing import List, Optional
from app.schemas.cobros import CobroType
from app.db import SessionLocal
from app.crud.cobros import get_cobro, get_cobros

@strawberry.type
class CobroQueries:
    @strawberry.field
    def cobros(self, skip: int = 0, limit: int = 100) -> List[CobroType]:
        db = SessionLocal()
        result = get_cobros(db, skip=skip, limit=limit)
        db.close()
        return [
            CobroType(
                id_cobro=c.id_cobro,
                id_cliente=c.id_cliente,
                fecha=c.fecha,
                monto_total=float(c.monto_total),
                forma_pago=c.forma_pago,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def cobro(self, id_cobro: int) -> Optional[CobroType]:
        db = SessionLocal()
        c = get_cobro(db, id_cobro)
        db.close()
        if not c:
            return None
        return CobroType(
            id_cobro=c.id_cobro,
            id_cliente=c.id_cliente,
            fecha=c.fecha,
            monto_total=float(c.monto_total),
            forma_pago=c.forma_pago,
            observaciones=c.observaciones
        )
