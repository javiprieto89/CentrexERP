import strawberry
from typing import Optional
from app.schemas.pedidos_items import PedidoItemType, PedidoItemInput
from app.db import SessionLocal
from app.crud.pedidos_items import create_pedido_item, update_pedido_item, delete_pedido_item

@strawberry.type
class PedidoItemMutations:
    @strawberry.mutation
    def create_pedido_item(self, data: PedidoItemInput) -> PedidoItemType:
        db = SessionLocal()
        new_obj = create_pedido_item(db, data.__dict__)
        db.close()
        return PedidoItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pedido_item(self, id_pedido_item: int, data: PedidoItemInput) -> Optional[PedidoItemType]:
        db = SessionLocal()
        updated = update_pedido_item(db, id_pedido_item, data.__dict__)
        db.close()
        if not updated:
            return None
        return PedidoItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_pedido_item(self, id_pedido_item: int) -> bool:
        db = SessionLocal()
        result = delete_pedido_item(db, id_pedido_item)
        db.close()
        return result
