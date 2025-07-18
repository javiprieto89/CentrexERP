import strawberry
from typing import Optional
from app.schemas.transacciones import TransaccionType, TransaccionInput
from app.db import SessionLocal
from app.crud.transacciones import create_transaccion, update_transaccion, delete_transaccion

@strawberry.type
class TransaccionMutations:
    @strawberry.mutation
    def create_transaccion(self, data: TransaccionInput) -> TransaccionType:
        db = SessionLocal()
        new_obj = create_transaccion(db, data.__dict__)
        db.close()
        return TransaccionType(**new_obj.__dict__)

    @strawberry.mutation
    def update_transaccion(self, id_transaccion: int, data: TransaccionInput) -> Optional[TransaccionType]:
        db = SessionLocal()
        updated = update_transaccion(db, id_transaccion, data.__dict__)
        db.close()
        if not updated:
            return None
        return TransaccionType(**updated.__dict__)

    @strawberry.mutation
    def delete_transaccion(self, id_transaccion: int) -> bool:
        db = SessionLocal()
        result = delete_transaccion(db, id_transaccion)
        db.close()
        return result