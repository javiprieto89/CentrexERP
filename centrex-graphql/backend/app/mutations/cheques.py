import strawberry
from typing import Optional
from app.schemas.cheques import ChequeType, ChequeInput
from app.db import SessionLocal
from app.crud.cheques import create_cheque, update_cheque, delete_cheque

@strawberry.type
class ChequeMutations:
    @strawberry.mutation
    def create_cheque(self, data: ChequeInput) -> ChequeType:
        db = SessionLocal()
        new_cheque = create_cheque(db, data.__dict__)
        db.close()
        return ChequeType(**new_cheque.__dict__)

    @strawberry.mutation
    def update_cheque(self, id_cheque: int, data: ChequeInput) -> Optional[ChequeType]:
        db = SessionLocal()
        updated = update_cheque(db, id_cheque, data.__dict__)
        db.close()
        if not updated:
            return None
        return ChequeType(**updated.__dict__)

    @strawberry.mutation
    def delete_cheque(self, id_cheque: int) -> bool:
        db = SessionLocal()
        result = delete_cheque(db, id_cheque)
        db.close()
        return result
