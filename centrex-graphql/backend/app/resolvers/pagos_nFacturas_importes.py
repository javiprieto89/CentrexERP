# app/resolvers/pagos_nFacturas_importes.py
import strawberry
from typing import List, Optional, cast
from decimal import Decimal
from app.schemas.pagos_nFacturas_importes import PagoNFacturaImporteType
from app.db import SessionLocal
from app.crud.pagos_nFacturas_importes import get_pago_nfactura_importe, get_pagos_nfacturas_importes

@strawberry.type
class PagoNFacturaImporteQueries:
    @strawberry.field
    def pagos_nfacturas_importes(self, skip: int = 0, limit: int = 100) -> List[PagoNFacturaImporteType]:
        db = SessionLocal()
        result = get_pagos_nfacturas_importes(db, skip=skip, limit=limit)
        db.close()
        return [
            PagoNFacturaImporteType(
                id_pago_factura=c.id_pago_factura,
                id_pago=c.id_pago,
                id_factura=c.id_factura,
                importe=float(cast(Decimal, c.importe))
            ) for c in result
        ]

    @strawberry.field
    def pago_nfactura_importe(self, id_pago_factura: int) -> Optional[PagoNFacturaImporteType]:
        db = SessionLocal()
        c = get_pago_nfactura_importe(db, id_pago_factura)
        db.close()
        if not c:
            return None
        return PagoNFacturaImporteType(
            id_pago_factura=c.id_pago_factura,
            id_pago=c.id_pago,
            id_factura=c.id_factura,
            importe=float(cast(Decimal, c.importe))
        )
