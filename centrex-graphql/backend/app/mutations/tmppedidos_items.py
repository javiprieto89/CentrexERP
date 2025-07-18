import strawberry
from typing import Optional
from app.schemas.tmppedidos_items import TmpPedidoItemType, TmpPedidoItemInput
from app.db import SessionLocal
from app.crud.tmppedidos_items import create_tmppedido_item, update_tmppedido_item, delete_tmppedido_item

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
        result = delete_tmppedido_item(db, id_tmpPedidoItem)
        db.close()
        return result