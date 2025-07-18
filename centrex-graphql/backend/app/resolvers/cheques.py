import strawberry
from typing import List, Optional
from app.schemas.cheques import ChequeType
from app.db import SessionLocal
from app.crud.cheques import get_cheque, get_cheques

@strawberry.type
class ChequeQueries:
    @strawberry.field
    def cheques(self, skip: int = 0, limit: int = 100) -> List[ChequeType]:
        db = SessionLocal()
        result = get_cheques(db, skip=skip, limit=limit)
        db.close()
        return [
            ChequeType(
                id_cheque=c.id_cheque,
                numero=c.numero,
                banco=c.banco,
                emisor=c.emisor,
                fecha_emision=c.fecha_emision,
                fecha_vencimiento=c.fecha_vencimiento,
                monto=float(c.monto),
                estado=c.estado,
                depositado=c.depositado,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def cheque(self, id_cheque: int) -> Optional[ChequeType]:
        db = SessionLocal()
        c = get_cheque(db, id_cheque)
        db.close()
        if not c:
            return None
        return ChequeType(
            id_cheque=c.id_cheque,
            numero=c.numero,
            banco=c.banco,
            emisor=c.emisor,
            fecha_emision=c.fecha_emision,
            fecha_vencimiento=c.fecha_vencimiento,
            monto=float(c.monto),
            estado=c.estado,
            depositado=c.depositado,
            observaciones=c.observaciones
        )
