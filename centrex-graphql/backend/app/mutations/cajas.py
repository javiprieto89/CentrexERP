import strawberry
from typing import Optional
from app.schemas.cajas import CajaType, CajaInput
from app.db import SessionLocal
from app.crud.cajas import create_caja, update_caja, delete_caja

@strawberry.type
class CajaMutations:
    @strawberry.mutation
    def create_caja(self, data: CajaInput) -> CajaType:
        db = SessionLocal()
        new_caja = create_caja(db, data.__dict__)
        db.close()
        return CajaType(**new_caja.__dict__)

    @strawberry.mutation
    def update_caja(self, id_caja: int, data: CajaInput) -> Optional[CajaType]:
        db = SessionLocal()
        updated = update_caja(db, id_caja, data.__dict__)
        db.close()
        if not updated:
            return None
        return CajaType(**updated.__dict__)

    @strawberry.mutation
    def delete_caja(self, id_caja: int) -> bool:
        db = SessionLocal()
        result = delete_caja(db, id_caja)
        db.close()
        return result
