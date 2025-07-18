import strawberry
from typing import Optional
from app.schemas.cobros import CobroType, CobroInput
from app.db import SessionLocal
from app.crud.cobros import create_cobro, update_cobro, delete_cobro

@strawberry.type
class CobroMutations:
    @strawberry.mutation
    def create_cobro(self, data: CobroInput) -> CobroType:
        db = SessionLocal()
        new_cobro = create_cobro(db, data.__dict__)
        db.close()
        return CobroType(**new_cobro.__dict__)

    @strawberry.mutation
    def update_cobro(self, id_cobro: int, data: CobroInput) -> Optional[CobroType]:
        db = SessionLocal()
        updated = update_cobro(db, id_cobro, data.__dict__)
        db.close()
        if not updated:
            return None
        return CobroType(**updated.__dict__)

    @strawberry.mutation
    def delete_cobro(self, id_cobro: int) -> bool:
        db = SessionLocal()
        result = delete_cobro(db, id_cobro)
        db.close()
        return result
