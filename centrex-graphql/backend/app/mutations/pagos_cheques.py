import strawberry
from typing import Optional
from app.schemas.pagos_cheques import PagoChequeType, PagoChequeInput
from app.db import SessionLocal
from app.crud.pagos_cheques import create_pago_cheque, update_pago_cheque, delete_pago_cheque

@strawberry.type
class PagoChequeMutations:
    @strawberry.mutation
    def create_pago_cheque(self, data: PagoChequeInput) -> PagoChequeType:
        db = SessionLocal()
        new_obj = create_pago_cheque(db, data.__dict__)
        db.close()
        return PagoChequeType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pago_cheque(self, id_pago_cheque: int, data: PagoChequeInput) -> Optional[PagoChequeType]:
        db = SessionLocal()
        updated = update_pago_cheque(db, id_pago_cheque, data.__dict__)
        db.close()
        if not updated:
            return None
        return PagoChequeType(**updated.__dict__)

    @strawberry.mutation
    def delete_pago_cheque(self, id_pago_cheque: int) -> bool:
        db = SessionLocal()
        result = delete_pago_cheque(db, id_pago_cheque)
        db.close()
        return result
