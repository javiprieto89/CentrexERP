import strawberry
from typing import Optional
from app.schemas.transferencias import TransferenciaType, TransferenciaInput
from app.db import SessionLocal
from app.crud.transferencias import create_transferencia, update_transferencia, delete_transferencia

@strawberry.type
class TransferenciaMutations:
    @strawberry.mutation
    def create_transferencia(self, data: TransferenciaInput) -> TransferenciaType:
        db = SessionLocal()
        new_obj = create_transferencia(db, data.__dict__)
        db.close()
        return TransferenciaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_transferencia(self, id_transferencia: int, data: TransferenciaInput) -> Optional[TransferenciaType]:
        db = SessionLocal()
        updated = update_transferencia(db, id_transferencia, data.__dict__)
        db.close()
        if not updated:
            return None
        return TransferenciaType(**updated.__dict__)

    @strawberry.mutation
    def delete_transferencia(self, id_transferencia: int) -> bool:
        db = SessionLocal()
        result = delete_transferencia(db, id_transferencia)
        db.close()
        return result