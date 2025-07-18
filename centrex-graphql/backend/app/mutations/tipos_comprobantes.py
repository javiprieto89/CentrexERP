import strawberry
from typing import Optional
from app.schemas.tipos_comprobantes import TiposComprobantesType, TiposComprobantesInput
from app.db import SessionLocal
from app.crud.tipos_comprobantes import create_tipo_comprobante, update_tipo_comprobante, delete_tipo_comprobante

@strawberry.type
class TiposComprobantesMutations:
    @strawberry.mutation
    def create_tipos_comprobante(self, data: TiposComprobantesInput) -> TiposComprobantesType:
        db = SessionLocal()
        new_obj = create_tipo_comprobante(db, data.__dict__)
        db.close()
        return TiposComprobantesType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tipos_comprobante(self, id_tipoComprobante: int, data: TiposComprobantesInput) -> Optional[TiposComprobantesType]:
        db = SessionLocal()
        updated = update_tipo_comprobante(db, id_tipoComprobante, data.__dict__)
        db.close()
        if not updated:
            return None
        return TiposComprobantesType(**updated.__dict__)

    @strawberry.mutation
    def delete_tipos_comprobante(self, id_tipoComprobante: int) -> bool:
        db = SessionLocal()
        result = delete_tipo_comprobante(db, id_tipoComprobante)
        db.close()
        return result
