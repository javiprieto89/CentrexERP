import strawberry
from typing import Optional
from app.schemas.cuentas_bancarias import CuentaBancariaType, CuentaBancariaInput
from app.db import SessionLocal
from app.crud.cuentas_bancarias import create_cuenta_bancaria, update_cuenta_bancaria, delete_cuenta_bancaria

@strawberry.type
class CuentaBancariaMutations:
    @strawberry.mutation
    def create_cuenta_bancaria(self, data: CuentaBancariaInput) -> CuentaBancariaType:
        db = SessionLocal()
        new_obj = create_cuenta_bancaria(db, data.__dict__)
        db.close()
        return CuentaBancariaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_cuenta_bancaria(self, id_cuenta: int, data: CuentaBancariaInput) -> Optional[CuentaBancariaType]:
        db = SessionLocal()
        updated = update_cuenta_bancaria(db, id_cuenta, data.__dict__)
        db.close()
        if not updated:
            return None
        return CuentaBancariaType(**updated.__dict__)

    @strawberry.mutation
    def delete_cuenta_bancaria(self, id_cuenta: int) -> bool:
        db = SessionLocal()
        result = delete_cuenta_bancaria(db, id_cuenta)
        db.close()
        return result
