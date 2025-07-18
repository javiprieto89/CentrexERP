import strawberry
from typing import Optional
from app.schemas.comprobantes_compras_impuestos import ComprobanteCompraImpuestoType, ComprobanteCompraImpuestoInput
from app.db import SessionLocal
from app.crud.comprobantes_compras_impuestos import create_comprobante_compra_impuesto, update_comprobante_compra_impuesto, delete_comprobante_compra_impuesto

@strawberry.type
class ComprobanteCompraImpuestoMutations:
    @strawberry.mutation
    def create_comprobante_compra_impuesto(self, data: ComprobanteCompraImpuestoInput) -> ComprobanteCompraImpuestoType:
        db = SessionLocal()
        new_obj = create_comprobante_compra_impuesto(db, data.__dict__)
        db.close()
        return ComprobanteCompraImpuestoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_comprobante_compra_impuesto(self, id_impuesto: int, data: ComprobanteCompraImpuestoInput) -> Optional[ComprobanteCompraImpuestoType]:
        db = SessionLocal()
        updated = update_comprobante_compra_impuesto(db, id_impuesto, data.__dict__)
        db.close()
        if not updated:
            return None
        return ComprobanteCompraImpuestoType(**updated.__dict__)

    @strawberry.mutation
    def delete_comprobante_compra_impuesto(self, id_impuesto: int) -> bool:
        db = SessionLocal()
        result = delete_comprobante_compra_impuesto(db, id_impuesto)
        db.close()
        return result
