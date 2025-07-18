import strawberry
from typing import Optional
from app.schemas.conceptos_compra import ConceptoCompraType, ConceptoCompraInput
from app.db import SessionLocal
from app.crud.conceptos_compra import create_concepto_compra, update_concepto_compra, delete_concepto_compra

@strawberry.type
class ConceptoCompraMutations:
    @strawberry.mutation
    def create_concepto_compra(self, data: ConceptoCompraInput) -> ConceptoCompraType:
        db = SessionLocal()
        new_obj = create_concepto_compra(db, data.__dict__)
        db.close()
        return ConceptoCompraType(**new_obj.__dict__)

    @strawberry.mutation
    def update_concepto_compra(self, id_concepto: int, data: ConceptoCompraInput) -> Optional[ConceptoCompraType]:
        db = SessionLocal()
        updated = update_concepto_compra(db, id_concepto, data.__dict__)
        db.close()
        if not updated:
            return None
        return ConceptoCompraType(**updated.__dict__)

    @strawberry.mutation
    def delete_concepto_compra(self, id_concepto: int) -> bool:
        db = SessionLocal()
        result = delete_concepto_compra(db, id_concepto)
        db.close()
        return result
