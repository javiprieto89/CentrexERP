import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.cambios import CambioType
from app.db import SessionLocal
from app.crud.cambios import get_cambio, get_cambios

@strawberry.type
class CambioQueries:
    @strawberry.field
    def cambios(self, skip: int = 0, limit: int = 100) -> List[CambioType]:
        db = SessionLocal()
        result = get_cambios(db, skip=skip, limit=limit)
        db.close()
        return [
            CambioType(
                id_cambio=c.id_cambio,
                fecha=c.fecha,
                id_moneda_origen=c.id_moneda_origen,
                id_moneda_destino=c.id_moneda_destino,
                valor=float(cast(Decimal, c.valor))
            ) for c in result
        ]

    @strawberry.field
    def cambio(self, id_cambio: int) -> Optional[CambioType]:
        db = SessionLocal()
        c = get_cambio(db, id_cambio)
        db.close()
        if not c:
            return None
        return CambioType(
            id_cambio=c.id_cambio,
            fecha=c.fecha,
            id_moneda_origen=c.id_moneda_origen,
            id_moneda_destino=c.id_moneda_destino,
            valor=float(cast(Decimal, c.valor))
        )
