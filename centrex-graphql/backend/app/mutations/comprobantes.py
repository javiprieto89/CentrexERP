import strawberry
from typing import Optional
from app.schemas.comprobantes import ComprobanteType, ComprobanteInput
from app.db import SessionLocal
from app.crud.comprobantes import create_comprobante, update_comprobante, delete_comprobante

@strawberry.type
class ComprobanteMutations:
    @strawberry.mutation
    def create_comprobante(self, data: ComprobanteInput) -> ComprobanteType:
        db = SessionLocal()
        new_obj = create_comprobante(db, data.__dict__)
        db.close()
        return ComprobanteType(**new_obj.__dict__)

    @strawberry.mutation
    def update_comprobante(self, id_comprobante: int, data: ComprobanteInput) -> Optional[ComprobanteType]:
        db = SessionLocal()
        updated = update_comprobante(db, id_comprobante, data.__dict__)
        db.close()
        if not updated:
            return None
        return ComprobanteType(**updated.__dict__)

    @strawberry.mutation
    def delete_comprobante(self, id_comprobante: int) -> bool:
        db = SessionLocal()
        result = delete_comprobante(db, id_comprobante)
        db.close()
        return result
