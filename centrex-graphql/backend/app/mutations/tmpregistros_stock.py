import strawberry
from typing import Optional
from app.schemas.tmpregistros_stock import TmpRegistroStockType, TmpRegistroStockInput
from app.db import SessionLocal
from app.crud.tmpregistros_stock import create_tmpregistro_stock, update_tmpregistro_stock, delete_tmpregistro_stock

@strawberry.type
class TmpRegistroStockMutations:
    @strawberry.mutation
    def create_tmp_registro_stock(self, data: TmpRegistroStockInput) -> TmpRegistroStockType:
        db = SessionLocal()
        new_obj = create_tmpregistro_stock(db, data.__dict__)
        db.close()
        return TmpRegistroStockType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_registro_stock(self, id_tmpRegistroStock: int, data: TmpRegistroStockInput) -> Optional[TmpRegistroStockType]:
        db = SessionLocal()
        updated = update_tmpregistro_stock(db, id_tmpRegistroStock, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpRegistroStockType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_registro_stock(self, id_tmpRegistroStock: int) -> bool:
        db = SessionLocal()
        result = delete_tmpregistro_stock(db, id_tmpRegistroStock)
        db.close()
        return result