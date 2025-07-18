import strawberry
from typing import Optional
from app.schemas.cc_clientes import CCClienteType, CCClienteInput
from app.db import SessionLocal
from app.crud.cc_clientes import create_cc_cliente, update_cc_cliente, delete_cc_cliente

@strawberry.type
class CCClienteMutations:
    @strawberry.mutation
    def create_cc_cliente(self, data: CCClienteInput) -> CCClienteType:
        db = SessionLocal()
        new_cc_cliente = create_cc_cliente(db, data.__dict__)
        db.close()
        return CCClienteType(**new_cc_cliente.__dict__)

    @strawberry.mutation
    def update_cc_cliente(self, id_cc_cliente: int, data: CCClienteInput) -> Optional[CCClienteType]:
        db = SessionLocal()
        updated = update_cc_cliente(db, id_cc_cliente, data.__dict__)
        db.close()
        if not updated:
            return None
        return CCClienteType(**updated.__dict__)

    @strawberry.mutation
    def delete_cc_cliente(self, id_cc_cliente: int) -> bool:
        db = SessionLocal()
        result = delete_cc_cliente(db, id_cc_cliente)
        db.close()
        return result
