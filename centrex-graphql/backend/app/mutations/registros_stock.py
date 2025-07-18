import strawberry
from typing import Optional
from app.schemas.registros_stock import RegistroStockType, RegistroStockInput
from app.db import SessionLocal
from app.crud.registros_stock import (
    create_registro_stock,
    update_registro_stock,
    delete_registro_stock,
    get_registros_stock_by_id,
)

@strawberry.type
class RegistroStockMutations:
    @strawberry.mutation
    def create_registro_stock(self, data: RegistroStockInput) -> RegistroStockType:
        db = SessionLocal()
        new_obj = create_registro_stock(db, data.__dict__)
        db.close()
        return RegistroStockType(**new_obj.__dict__)

    @strawberry.mutation
    def update_registro_stock(self, id_registro: int, data: RegistroStockInput) -> Optional[RegistroStockType]:
        db = SessionLocal()
        updated = update_registro_stock(db, id_registro, data.__dict__)
        db.close()
        if not updated:
            return None
        return RegistroStockType(**updated.__dict__)

    @strawberry.mutation
    def delete_registro_stock(self, id_registro: int) -> bool:
        db = SessionLocal()
        obj = get_registros_stock_by_id(db, id_registro)
        if not obj:
            db.close()
            return False
        delete_registro_stock(db, obj)
        db.close()
        return True