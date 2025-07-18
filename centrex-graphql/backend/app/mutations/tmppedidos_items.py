import strawberry
from typing import Optional
from app.schemas.tmppedidos_items import TmpPedidoItemType, TmpPedidoItemInput
from app.db import SessionLocal
from app.crud.tmppedidos_items import (
    create_tmppedido_item,
    update_tmppedido_item,
    delete_tmppedido_item,
    get_tmppedidos_items_by_id,
)

@strawberry.type
class TmpPedidoItemMutations:
    @strawberry.mutation
    def create_tmp_pedido_item(self, data: TmpPedidoItemInput) -> TmpPedidoItemType:
        db = SessionLocal()
        new_obj = create_tmppedido_item(db, data.__dict__)
        db.close()
        return TmpPedidoItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_pedido_item(self, id_tmpPedidoItem: int, data: TmpPedidoItemInput) -> Optional[TmpPedidoItemType]:
        db = SessionLocal()
        updated = update_tmppedido_item(db, id_tmpPedidoItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpPedidoItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_pedido_item(self, id_tmpPedidoItem: int) -> bool:
        db = SessionLocal()
        obj = get_tmppedidos_items_by_id(db, id_tmpPedidoItem)
        if not obj:
            db.close()
            return False
        delete_tmppedido_item(db, obj)
        db.close()
        return True