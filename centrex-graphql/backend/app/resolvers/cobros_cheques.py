import strawberry
from typing import List, Optional
from app.schemas.cobros_cheques import CobroChequeType
from app.db import SessionLocal
from app.crud.cobros_cheques import get_cobro_cheque, get_cobros_cheques

@strawberry.type
class CobroChequeQueries:
    @strawberry.field
    def cobros_cheques(self, skip: int = 0, limit: int = 100) -> List[CobroChequeType]:
        db = SessionLocal()
        result = get_cobros_cheques(db, skip=skip, limit=limit)
        db.close()
        return [
            CobroChequeType(
                id_cobro_cheque=c.id_cobro_cheque,
                id_cobro=c.id_cobro,
                id_cheque=c.id_cheque,
                importe=float(c.importe)
            ) for c in result
        ]

    @strawberry.field
    def cobro_cheque(self, id_cobro_cheque: int) -> Optional[CobroChequeType]:
        db = SessionLocal()
        c = get_cobro_cheque(db, id_cobro_cheque)
        db.close()
        if not c:
            return None
        return CobroChequeType(
            id_cobro_cheque=c.id_cobro_cheque,
            id_cobro=c.id_cobro,
            id_cheque=c.id_cheque,
            importe=float(c.importe)
        )
