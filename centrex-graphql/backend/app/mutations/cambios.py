import strawberry
from typing import Optional
from app.schemas.cambios import CambioType, CambioInput
from app.db import SessionLocal
from app.crud.cambios import create_cambio, update_cambio, delete_cambio

@strawberry.type
class CambioMutations:
    @strawberry.mutation
    def create_cambio(self, data: CambioInput) -> CambioType:
        db = SessionLocal()
        new_cambio = create_cambio(db, data.__dict__)
        db.close()
        return CambioType(**new_cambio.__dict__)

    @strawberry.mutation
    def update_cambio(self, id_cambio: int, data: CambioInput) -> Optional[CambioType]:
        db = SessionLocal()
        updated = update_cambio(db, id_cambio, data.__dict__)
        db.close()
        if not updated:
            return None
        return CambioType(**updated.__dict__)

    @strawberry.mutation
    def delete_cambio(self, id_cambio: int) -> bool:
        db = SessionLocal()
        result = delete_cambio(db, id_cambio)
        db.close()
        return result
