import strawberry
from typing import Optional
from app.schemas.separador_decimal import SeparadorDecimalType, SeparadorDecimalInput
from app.db import SessionLocal
from app.crud.separador_decimal import (
    create_separador_decimal,
    update_separador_decimal,
    delete_separador_decimal,
    get_separador_decimal_by_id,
)

@strawberry.type
class SeparadorDecimalMutations:
    @strawberry.mutation
    def create_separador_decimal(self, data: SeparadorDecimalInput) -> SeparadorDecimalType:
        db = SessionLocal()
        new_obj = create_separador_decimal(db, data.__dict__)
        db.close()
        return SeparadorDecimalType(**new_obj.__dict__)

    @strawberry.mutation
    def update_separador_decimal(self, id_separador: int, data: SeparadorDecimalInput) -> Optional[SeparadorDecimalType]:
        db = SessionLocal()
        updated = update_separador_decimal(db, id_separador, data.__dict__)
        db.close()
        if not updated:
            return None
        return SeparadorDecimalType(**updated.__dict__)

    @strawberry.mutation
    def delete_separador_decimal(self, id_separador: int) -> bool:
        db = SessionLocal()
        obj = get_separador_decimal_by_id(db, id_separador)
        if not obj:
            db.close()
            return False
        delete_separador_decimal(db, obj)
        db.close()
        return True