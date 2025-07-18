import strawberry
from typing import Optional
from app.schemas.condiciones_compra import CondicionCompraType, CondicionCompraInput
from app.db import SessionLocal
from app.crud.condiciones_compra import create_condicion_compra, update_condicion_compra, delete_condicion_compra

@strawberry.type
class CondicionCompraMutations:
    @strawberry.mutation
    def create_condicion_compra(self, data: CondicionCompraInput) -> CondicionCompraType:
        db = SessionLocal()
        new_obj = create_condicion_compra(db, data.__dict__)
        db.close()
        return CondicionCompraType(**new_obj.__dict__)

    @strawberry.mutation
    def update_condicion_compra(self, id_condicion: int, data: CondicionCompraInput) -> Optional[CondicionCompraType]:
        db = SessionLocal()
        updated = update_condicion_compra(db, id_condicion, data.__dict__)
        db.close()
        if not updated:
            return None
        return CondicionCompraType(**updated.__dict__)

    @strawberry.mutation
    def delete_condicion_compra(self, id_condicion: int) -> bool:
        db = SessionLocal()
        result = delete_condicion_compra(db, id_condicion)
        db.close()
        return result
