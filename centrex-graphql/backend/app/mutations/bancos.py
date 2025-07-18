import strawberry
from typing import Optional
from app.schemas.bancos import BancoType, BancoInput
from app.db import SessionLocal
from app.crud.bancos import create_banco, update_banco, delete_banco

@strawberry.type
class BancoMutations:
    @strawberry.mutation
    def create_banco(self, data: BancoInput) -> BancoType:
        db = SessionLocal()
        new_banco = create_banco(db, data.__dict__)
        db.close()
        return BancoType(**new_banco.__dict__)

    @strawberry.mutation
    def update_banco(self, id_banco: int, data: BancoInput) -> Optional[BancoType]:
        db = SessionLocal()
        updated = update_banco(db, id_banco, data.__dict__)
        db.close()
        if not updated:
            return None
        return BancoType(**updated.__dict__)

    @strawberry.mutation
    def delete_banco(self, id_banco: int) -> bool:
        db = SessionLocal()
        result = delete_banco(db, id_banco)
        db.close()
        return result
