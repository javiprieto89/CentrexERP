import strawberry
from typing import Optional
from app.schemas.proveedores import ProveedorType, ProveedorInput
from app.db import SessionLocal
from app.crud.proveedores import create_proveedor, update_proveedor, delete_proveedor

@strawberry.type
class ProveedorMutations:
    @strawberry.mutation
    def create_proveedor(self, data: ProveedorInput) -> ProveedorType:
        db = SessionLocal()
        new_obj = create_proveedor(db, data.__dict__)
        db.close()
        return ProveedorType(**new_obj.__dict__)

    @strawberry.mutation
    def update_proveedor(self, id_proveedor: int, data: ProveedorInput) -> Optional[ProveedorType]:
        db = SessionLocal()
        updated = update_proveedor(db, id_proveedor, data.__dict__)
        db.close()
        if not updated:
            return None
        return ProveedorType(**updated.__dict__)

    @strawberry.mutation
    def delete_proveedor(self, id_proveedor: int) -> bool:
        db = SessionLocal()
        result = delete_proveedor(db, id_proveedor)
        db.close()
        return result
