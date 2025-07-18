import strawberry
from typing import Optional
from app.schemas.pedidos import PedidoType, PedidoInput
from app.db import SessionLocal
from app.crud.pedidos import create_pedido, update_pedido, delete_pedido

@strawberry.type
class PedidoMutations:
    @strawberry.mutation
    def create_pedido(self, data: PedidoInput) -> PedidoType:
        db = SessionLocal()
        new_obj = create_pedido(db, data.__dict__)
        db.close()
        return PedidoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pedido(self, id_pedido: int, data: PedidoInput) -> Optional[PedidoType]:
        db = SessionLocal()
        updated = update_pedido(db, id_pedido, data.__dict__)
        db.close()
        if not updated:
            return None
        return PedidoType(**updated.__dict__)

    @strawberry.mutation
    def delete_pedido(self, id_pedido: int) -> bool:
        db = SessionLocal()
        result = delete_pedido(db, id_pedido)
        db.close()
        return result
