import strawberry
from typing import List, Optional
from app.schemas.cobros_retenciones import CobroRetencionType
from app.db import SessionLocal
from app.crud.cobros_retenciones import get_cobro_retencion, get_cobros_retenciones

@strawberry.type
class CobroRetencionQueries:
    @strawberry.field
    def cobros_retenciones(self, skip: int = 0, limit: int = 100) -> List[CobroRetencionType]:
        db = SessionLocal()
        result = get_cobros_retenciones(db, skip=skip, limit=limit)
        db.close()
        return [
            CobroRetencionType(
                id_cobro_retencion=c.id_cobro_retencion,
                id_cobro=c.id_cobro,
                tipo_retencion=c.tipo_retencion,
                importe=float(c.importe)
            ) for c in result
        ]

    @strawberry.field
    def cobro_retencion(self, id_cobro_retencion: int) -> Optional[CobroRetencionType]:
        db = SessionLocal()
        c = get_cobro_retencion(db, id_cobro_retencion)
        db.close()
        if not c:
            return None
        return CobroRetencionType(
            id_cobro_retencion=c.id_cobro_retencion,
            id_cobro=c.id_cobro,
            tipo_retencion=c.tipo_retencion,
            importe=float(c.importe)
        )
