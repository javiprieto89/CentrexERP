import strawberry
from typing import Optional
from app.schemas.cobros_retenciones import CobroRetencionType, CobroRetencionInput
from app.db import SessionLocal
from app.crud.cobros_retenciones import create_cobro_retencion, update_cobro_retencion, delete_cobro_retencion

@strawberry.type
class CobroRetencionMutations:
    @strawberry.mutation
    def create_cobro_retencion(self, data: CobroRetencionInput) -> CobroRetencionType:
        db = SessionLocal()
        new_cobro_retencion = create_cobro_retencion(db, data.__dict__)
        db.close()
        return CobroRetencionType(**new_cobro_retencion.__dict__)

    @strawberry.mutation
    def update_cobro_retencion(self, id_cobro_retencion: int, data: CobroRetencionInput) -> Optional[CobroRetencionType]:
        db = SessionLocal()
        updated = update_cobro_retencion(db, id_cobro_retencion, data.__dict__)
        db.close()
        if not updated:
            return None
        return CobroRetencionType(**updated.__dict__)

    @strawberry.mutation
    def delete_cobro_retencion(self, id_cobro_retencion: int) -> bool:
        db = SessionLocal()
        result = delete_cobro_retencion(db, id_cobro_retencion)
        db.close()
        return result
