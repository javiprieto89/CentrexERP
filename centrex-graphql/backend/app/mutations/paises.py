import strawberry
from typing import Optional
from app.schemas.paises import PaisType, PaisInput
from app.db import SessionLocal
from app.crud.paises import create_pais, update_pais, delete_pais

@strawberry.type
class PaisMutations:
    @strawberry.mutation
    def create_pais(self, data: PaisInput) -> PaisType:
        db = SessionLocal()
        new_obj = create_pais(db, data.__dict__)
        db.close()
        return PaisType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pais(self, id_pais: int, data: PaisInput) -> Optional[PaisType]:
        db = SessionLocal()
        updated = update_pais(db, id_pais, data.__dict__)
        db.close()
        if not updated:
            return None
        return PaisType(**updated.__dict__)

    @strawberry.mutation
    def delete_pais(self, id_pais: int) -> bool:
        db = SessionLocal()
        result = delete_pais(db, id_pais)
        db.close()
        return result
