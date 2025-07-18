import strawberry
from typing import Optional
from app.schemas.clientes import ClienteType, ClienteInput
from app.db import SessionLocal
from app.crud.clientes import create_cliente, update_cliente, delete_cliente, get_cliente

@strawberry.type
class ClienteMutations:
    @strawberry.mutation
    def create_cliente(self, data: ClienteInput) -> ClienteType:
        db = SessionLocal()
        new_cliente = create_cliente(db, data.__dict__)
        db.close()
        return ClienteType(**new_cliente.__dict__)

    @strawberry.mutation
    def update_cliente(self, id_cliente: int, data: ClienteInput) -> Optional[ClienteType]:
        db = SessionLocal()
        updated = update_cliente(db, id_cliente, data.__dict__)
        db.close()
        if not updated:
            return None
        return ClienteType(**updated.__dict__)

    @strawberry.mutation
    def delete_cliente(self, id_cliente: int) -> bool:
        db = SessionLocal()
        result = delete_cliente(db, id_cliente)
        db.close()
        return result
