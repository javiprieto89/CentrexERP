import strawberry
from typing import List, Optional
from app.schemas.proveedores import ProveedorType
from app.db import SessionLocal
from app.crud.proveedores import get_proveedor, get_proveedores

@strawberry.type
class ProveedorQueries:
    @strawberry.field
    def proveedores(self, skip: int = 0, limit: int = 100) -> List[ProveedorType]:
        db = SessionLocal()
        result = get_proveedores(db, skip=skip, limit=limit)
        db.close()
        return [
            ProveedorType(
                id_proveedor=c.id_proveedor,
                nombre=c.nombre,
                direccion=c.direccion,
                telefono=c.telefono,
                email=c.email
            ) for c in result
        ]

    @strawberry.field
    def proveedor(self, id_proveedor: int) -> Optional[ProveedorType]:
        db = SessionLocal()
        c = get_proveedor(db, id_proveedor)
        db.close()
        if not c:
            return None
        return ProveedorType(
            id_proveedor=c.id_proveedor,
            nombre=c.nombre,
            direccion=c.direccion,
            telefono=c.telefono,
            email=c.email
        )
