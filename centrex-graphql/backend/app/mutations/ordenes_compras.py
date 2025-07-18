import strawberry
from typing import Optional
from app.schemas.ordenes_compras import OrdenCompraType, OrdenCompraInput
from app.db import SessionLocal
from app.crud.ordenes_compras import create_orden_compra, update_orden_compra, delete_orden_compra

@strawberry.type
class OrdenCompraMutations:
    @strawberry.mutation
    def create_orden_compra(self, data: OrdenCompraInput) -> OrdenCompraType:
        db = SessionLocal()
        new_obj = create_orden_compra(db, data.__dict__)
        db.close()
        return OrdenCompraType(**new_obj.__dict__)

    @strawberry.mutation
    def update_orden_compra(self, id_orden: int, data: OrdenCompraInput) -> Optional[OrdenCompraType]:
        db = SessionLocal()
        updated = update_orden_compra(db, id_orden, data.__dict__)
        db.close()
        if not updated:
            return None
        return OrdenCompraType(**updated.__dict__)

    @strawberry.mutation
    def delete_orden_compra(self, id_orden: int) -> bool:
        db = SessionLocal()
        result = delete_orden_compra(db, id_orden)
        db.close()
        return result
