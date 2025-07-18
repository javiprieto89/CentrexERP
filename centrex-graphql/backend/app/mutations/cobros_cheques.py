import strawberry
from typing import Optional
from app.schemas.cobros_cheques import CobroChequeType, CobroChequeInput
from app.db import SessionLocal
from app.crud.cobros_cheques import create_cobro_cheque, update_cobro_cheque, delete_cobro_cheque

@strawberry.type
class CobroChequeMutations:
    @strawberry.mutation
    def create_cobro_cheque(self, data: CobroChequeInput) -> CobroChequeType:
        db = SessionLocal()
        new_cobro_cheque = create_cobro_cheque(db, data.__dict__)
        db.close()
        return CobroChequeType(**new_cobro_cheque.__dict__)

    @strawberry.mutation
    def update_cobro_cheque(self, id_cobro_cheque: int, data: CobroChequeInput) -> Optional[CobroChequeType]:
        db = SessionLocal()
        updated = update_cobro_cheque(db, id_cobro_cheque, data.__dict__)
        db.close()
        if not updated:
            return None
        return CobroChequeType(**updated.__dict__)

    @strawberry.mutation
    def delete_cobro_cheque(self, id_cobro_cheque: int) -> bool:
        db = SessionLocal()
        result = delete_cobro_cheque(db, id_cobro_cheque)
        db.close()
        return result
