import strawberry
from typing import Optional
from app.schemas.impuestos import ImpuestoType, ImpuestoInput
from app.db import SessionLocal
from app.crud.impuestos import create_impuesto, update_impuesto, delete_impuesto

@strawberry.type
class ImpuestoMutations:
    @strawberry.mutation
    def create_impuesto(self, data: ImpuestoInput) -> ImpuestoType:
        db = SessionLocal()
        new_obj = create_impuesto(db, data.__dict__)
        db.close()
        return ImpuestoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_impuesto(self, id_impuesto: int, data: ImpuestoInput) -> Optional[ImpuestoType]:
        db = SessionLocal()
        updated = update_impuesto(db, id_impuesto, data.__dict__)
        db.close()
        if not updated:
            return None
        return ImpuestoType(**updated.__dict__)

    @strawberry.mutation
    def delete_impuesto(self, id_impuesto: int) -> bool:
        db = SessionLocal()
        result = delete_impuesto(db, id_impuesto)
        db.close()
        return result
