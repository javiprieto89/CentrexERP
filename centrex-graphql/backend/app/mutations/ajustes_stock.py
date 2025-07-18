import strawberry
from typing import Optional
from app.schemas.ajustes_stock import AjusteStockType, AjusteStockInput
from app.db import SessionLocal
from app.crud.ajustes_stock import create_ajuste_stock, update_ajuste_stock, delete_ajuste_stock, get_ajuste_stock

@strawberry.type
class AjusteStockMutations:
    @strawberry.mutation
    def create_ajuste_stock(self, data: AjusteStockInput) -> AjusteStockType:
        db = SessionLocal()
        new_ajuste = create_ajuste_stock(db, data.__dict__)
        db.close()
        return AjusteStockType(**new_ajuste.__dict__)

    @strawberry.mutation
    def update_ajuste_stock(self, id_ajuste_stock: int, data: AjusteStockInput) -> Optional[AjusteStockType]:
        db = SessionLocal()
        updated = update_ajuste_stock(db, id_ajuste_stock, data.__dict__)
        db.close()
        if not updated:
            return None
        return AjusteStockType(**updated.__dict__)

    @strawberry.mutation
    def delete_ajuste_stock(self, id_ajuste_stock: int) -> bool:
        db = SessionLocal()
        result = delete_ajuste_stock(db, id_ajuste_stock)
        db.close()
        return result

# Alias for backward compatibility
AjustesStockMutations = AjusteStockMutations
