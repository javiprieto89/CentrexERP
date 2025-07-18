# app/resolvers/cc_clientes.py
import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.cc_clientes import CCClienteType
from app.db import SessionLocal
from app.crud.cc_clientes import get_cc_cliente, get_cc_clientes

@strawberry.type
class CCClienteQueries:
    @strawberry.field
    def cc_clientes(self, skip: int = 0, limit: int = 100) -> List[CCClienteType]:
        db = SessionLocal()
        result = get_cc_clientes(db, skip=skip, limit=limit)
        db.close()
        return [
            CCClienteType(
                id_cc_cliente=c.id_cc_cliente,
                id_cliente=c.id_cliente,
                fecha=c.fecha,
                tipo=c.tipo,
                id_comprobante=c.id_comprobante,
                detalle=c.detalle,
                debe=float(cast(Decimal, c.debe)) if c.debe is not None else None,
                haber=float(cast(Decimal, c.haber)) if c.haber is not None else None,
                saldo=float(cast(Decimal, c.saldo)) if c.saldo is not None else None
            ) for c in result
        ]

    @strawberry.field
    def cc_cliente(self, id_cc_cliente: int) -> Optional[CCClienteType]:
        db = SessionLocal()
        c = get_cc_cliente(db, id_cc_cliente)
        db.close()
        if not c:
            return None
        return CCClienteType(
            id_cc_cliente=c.id_cc_cliente,
            id_cliente=c.id_cliente,
            fecha=c.fecha,
            tipo=c.tipo,
            id_comprobante=c.id_comprobante,
            detalle=c.detalle,
            debe=float(cast(Decimal, c.debe)) if c.debe is not None else None,
            haber=float(cast(Decimal, c.haber)) if c.haber is not None else None,
            saldo=float(cast(Decimal, c.saldo)) if c.saldo is not None else None
        )
