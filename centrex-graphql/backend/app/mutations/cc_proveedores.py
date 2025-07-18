import strawberry
from typing import Optional
from app.schemas.cc_proveedores import CCProveedorType, CCProveedorInput
from app.db import SessionLocal
from app.crud.cc_proveedores import create_cc_proveedor, update_cc_proveedor, delete_cc_proveedor

@strawberry.type
class CCProveedorMutations:
    @strawberry.mutation
    def create_cc_proveedor(self, data: CCProveedorInput) -> CCProveedorType:
        db = SessionLocal()
        new_cc_proveedor = create_cc_proveedor(db, data.__dict__)
        db.close()
        return CCProveedorType(**new_cc_proveedor.__dict__)

    @strawberry.mutation
    def update_cc_proveedor(self, id_cc_proveedor: int, data: CCProveedorInput) -> Optional[CCProveedorType]:
        db = SessionLocal()
        updated = update_cc_proveedor(db, id_cc_proveedor, data.__dict__)
        db.close()
        if not updated:
            return None
        return CCProveedorType(**updated.__dict__)

    @strawberry.mutation
    def delete_cc_proveedor(self, id_cc_proveedor: int) -> bool:
        db = SessionLocal()
        result = delete_cc_proveedor(db, id_cc_proveedor)
        db.close()
        return result
