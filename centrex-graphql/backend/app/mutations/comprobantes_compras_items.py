import strawberry
from typing import Optional
from app.schemas.comprobantes_compras_items import ComprobanteCompraItemType, ComprobanteCompraItemInput
from app.db import SessionLocal
from app.crud.comprobantes_compras_items import create_comprobante_compra_item, update_comprobante_compra_item, delete_comprobante_compra_item

@strawberry.type
class ComprobanteCompraItemMutations:
    @strawberry.mutation
    def create_comprobante_compra_item(self, data: ComprobanteCompraItemInput) -> ComprobanteCompraItemType:
        db = SessionLocal()
        new_obj = create_comprobante_compra_item(db, data.__dict__)
        db.close()
        return ComprobanteCompraItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_comprobante_compra_item(self, id_item: int, data: ComprobanteCompraItemInput) -> Optional[ComprobanteCompraItemType]:
        db = SessionLocal()
        updated = update_comprobante_compra_item(db, id_item, data.__dict__)
        db.close()
        if not updated:
            return None
        return ComprobanteCompraItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_comprobante_compra_item(self, id_item: int) -> bool:
        db = SessionLocal()
        result = delete_comprobante_compra_item(db, id_item)
        db.close()
        return result
