import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.cuentas_bancarias import CuentaBancariaType
from app.db import SessionLocal
from app.crud.cuentas_bancarias import get_cuenta_bancaria, get_cuentas_bancarias

@strawberry.type
class CuentaBancariaQueries:
    @strawberry.field
    def cuentas_bancarias(self, skip: int = 0, limit: int = 100) -> List[CuentaBancariaType]:
        db = SessionLocal()
        result = get_cuentas_bancarias(db, skip=skip, limit=limit)
        db.close()
        return [
            CuentaBancariaType(
                id_cuenta=c.id_cuenta,
                banco=c.banco,
                sucursal=c.sucursal,
                numero=c.numero,
                titular=c.titular,
                cbu=c.cbu,
                saldo=float(cast(Decimal, c.saldo))
            ) for c in result
        ]

    @strawberry.field
    def cuenta_bancaria(self, id_cuenta: int) -> Optional[CuentaBancariaType]:
        db = SessionLocal()
        c = get_cuenta_bancaria(db, id_cuenta)
        db.close()
        if not c:
            return None
        return CuentaBancariaType(
            id_cuenta=c.id_cuenta,
            banco=c.banco,
            sucursal=c.sucursal,
            numero=c.numero,
            titular=c.titular,
            cbu=c.cbu,
            saldo=float(cast(Decimal, c.saldo))
        )
