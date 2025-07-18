import strawberry
from typing import List, Optional
from app.schemas.cajas import CajaType
from app.db import SessionLocal
from app.crud.cajas import get_caja, get_cajas

@strawberry.type
class CajaQueries:
    @strawberry.field
    def cajas(self, skip: int = 0, limit: int = 100) -> List[CajaType]:
        db = SessionLocal()
        result = get_cajas(db, skip=skip, limit=limit)
        db.close()
        return [
            CajaType(
                id_caja=c.id_caja,
                nombre=c.nombre,
                saldo_inicial=float(c.saldo_inicial) if c.saldo_inicial is not None else None,
                activo=c.activo
            ) for c in result
        ]

    @strawberry.field
    def caja(self, id_caja: int) -> Optional[CajaType]:
        db = SessionLocal()
        c = get_caja(db, id_caja)
        db.close()
        if not c:
            return None
        return CajaType(
            id_caja=c.id_caja,
            nombre=c.nombre,
            saldo_inicial=float(c.saldo_inicial) if c.saldo_inicial is not None else None,
            activo=c.activo
        )
