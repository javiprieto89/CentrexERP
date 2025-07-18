import strawberry
from typing import Optional
from app.schemas.comprobantes_compras import ComprobanteCompraType, ComprobanteCompraInput
from app.db import SessionLocal
from app.crud.comprobantes_compras import create_comprobante_compra, update_comprobante_compra, delete_comprobante_compra

@strawberry.type
class ComprobanteCompraMutations:
    @strawberry.mutation
    def create_comprobante_compra(self, data: ComprobanteCompraInput) -> ComprobanteCompraType:
        db = SessionLocal()
        new_obj = create_comprobante_compra(db, data.__dict__)
        db.close()
        return ComprobanteCompraType(**new_obj.__dict__)

    @strawberry.mutation
    def update_comprobante_compra(self, id_comprobante_compra: int, data: ComprobanteCompraInput) -> Optional[ComprobanteCompraType]:
        db = SessionLocal()
        updated = update_comprobante_compra(db, id_comprobante_compra, data.__dict__)
        db.close()
        if not updated:
            return None
        return ComprobanteCompraType(**updated.__dict__)

    @strawberry.mutation
    def delete_comprobante_compra(self, id_comprobante_compra: int) -> bool:
        db = SessionLocal()
        result = delete_comprobante_compra(db, id_comprobante_compra)
        db.close()
        return result
