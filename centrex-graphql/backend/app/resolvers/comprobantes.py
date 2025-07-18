import strawberry
from typing import List, Optional
from app.schemas.comprobantes import ComprobanteType
from app.db import SessionLocal
from app.crud.comprobantes import get_comprobante, get_comprobantes

@strawberry.type
class ComprobanteQueries:
    @strawberry.field
    def comprobantes(self, skip: int = 0, limit: int = 100) -> List[ComprobanteType]:
        db = SessionLocal()
        result = get_comprobantes(db, skip=skip, limit=limit)
        db.close()
        return [
            ComprobanteType(
                id_comprobante=c.id_comprobante,
                id_cliente=c.id_cliente,
                fecha=c.fecha,
                tipo_comprobante=c.tipo_comprobante,
                numero=c.numero,
                total=float(c.total),
                estado=c.estado,
                observaciones=c.observaciones
            ) for c in result
        ]

    @strawberry.field
    def comprobante(self, id_comprobante: int) -> Optional[ComprobanteType]:
        db = SessionLocal()
        c = get_comprobante(db, id_comprobante)
        db.close()
        if not c:
            return None
        return ComprobanteType(
            id_comprobante=c.id_comprobante,
            id_cliente=c.id_cliente,
            fecha=c.fecha,
            tipo_comprobante=c.tipo_comprobante,
            numero=c.numero,
            total=float(c.total),
            estado=c.estado,
            observaciones=c.observaciones
        )
