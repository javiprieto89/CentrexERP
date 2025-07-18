import strawberry
from typing import Optional
from app.schemas.produccion import ProduccionType, ProduccionInput
from app.db import SessionLocal
from app.crud.produccion import create_produccion, update_produccion, delete_produccion

@strawberry.type
class ProduccionMutations:
    @strawberry.mutation
    def create_produccion(self, data: ProduccionInput) -> ProduccionType:
        db = SessionLocal()
        new_obj = create_produccion(db, data.__dict__)
        db.close()
        return ProduccionType(**new_obj.__dict__)

    @strawberry.mutation
    def update_produccion(self, id_produccion: int, data: ProduccionInput) -> Optional[ProduccionType]:
        db = SessionLocal()
        updated = update_produccion(db, id_produccion, data.__dict__)
        db.close()
        if not updated:
            return None
        return ProduccionType(**updated.__dict__)

    @strawberry.mutation
    def delete_produccion(self, id_produccion: int) -> bool:
        db = SessionLocal()
        result = delete_produccion(db, id_produccion)
        db.close()
        return result
