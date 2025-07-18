import strawberry
from typing import Optional
from app.schemas.comprobantes_compras_conceptos import ComprobanteCompraConceptoType, ComprobanteCompraConceptoInput
from app.db import SessionLocal
from app.crud.comprobantes_compras_conceptos import create_comprobante_compra_concepto, update_comprobante_compra_concepto, delete_comprobante_compra_concepto

@strawberry.type
class ComprobanteCompraConceptoMutations:
    @strawberry.mutation
    def create_comprobante_compra_concepto(self, data: ComprobanteCompraConceptoInput) -> ComprobanteCompraConceptoType:
        db = SessionLocal()
        new_obj = create_comprobante_compra_concepto(db, data.__dict__)
        db.close()
        return ComprobanteCompraConceptoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_comprobante_compra_concepto(self, id_concepto: int, data: ComprobanteCompraConceptoInput) -> Optional[ComprobanteCompraConceptoType]:
        db = SessionLocal()
        updated = update_comprobante_compra_concepto(db, id_concepto, data.__dict__)
        db.close()
        if not updated:
            return None
        return ComprobanteCompraConceptoType(**updated.__dict__)

    @strawberry.mutation
    def delete_comprobante_compra_concepto(self, id_concepto: int) -> bool:
        db = SessionLocal()
        result = delete_comprobante_compra_concepto(db, id_concepto)
        db.close()
        return result
