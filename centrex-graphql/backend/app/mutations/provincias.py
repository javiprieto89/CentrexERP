import strawberry
from typing import Optional
from app.schemas.provincias import ProvinciaType, ProvinciaInput
from app.db import SessionLocal
from app.crud.provincias import create_provincia, update_provincia, delete_provincia

@strawberry.type
class ProvinciaMutations:
    @strawberry.mutation
    def create_provincia(self, data: ProvinciaInput) -> ProvinciaType:
        db = SessionLocal()
        new_obj = create_provincia(db, data.__dict__)
        db.close()
        return ProvinciaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_provincia(self, id_provincia: int, data: ProvinciaInput) -> Optional[ProvinciaType]:
        db = SessionLocal()
        updated = update_provincia(db, id_provincia, data.__dict__)
        db.close()
        if not updated:
            return None
        return ProvinciaType(**updated.__dict__)

    @strawberry.mutation
    def delete_provincia(self, id_provincia: int) -> bool:
        db = SessionLocal()
        result = delete_provincia(db, id_provincia)
        db.close()
        return result
