import strawberry
from typing import Optional
from app.schemas.pagos import PagoType, PagoInput
from app.db import SessionLocal
from app.crud.pagos import create_pago, update_pago, delete_pago

@strawberry.type
class PagoMutations:
    @strawberry.mutation
    def create_pago(self, data: PagoInput) -> PagoType:
        db = SessionLocal()
        new_obj = create_pago(db, data.__dict__)
        db.close()
        return PagoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pago(self, id_pago: int, data: PagoInput) -> Optional[PagoType]:
        db = SessionLocal()
        updated = update_pago(db, id_pago, data.__dict__)
        db.close()
        if not updated:
            return None
        return PagoType(**updated.__dict__)

    @strawberry.mutation
    def delete_pago(self, id_pago: int) -> bool:
        db = SessionLocal()
        result = delete_pago(db, id_pago)
        db.close()
        return result
