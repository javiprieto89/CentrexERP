import strawberry
from typing import List, Optional
from app.schemas.cc_proveedores import CCProveedorType
from app.db import SessionLocal
from app.crud.cc_proveedores import get_cc_proveedor, get_cc_proveedores

@strawberry.type
class CCProveedorQueries:
    @strawberry.field
    def cc_proveedores(self, skip: int = 0, limit: int = 100) -> List[CCProveedorType]:
        db = SessionLocal()
        result = get_cc_proveedores(db, skip=skip, limit=limit)
        db.close()
        return [
            CCProveedorType(
                id_cc_proveedor=c.id_cc_proveedor,
                id_proveedor=c.id_proveedor,
                fecha=c.fecha,
                tipo=c.tipo,
                id_comprobante=c.id_comprobante,
                detalle=c.detalle,
                debe=float(c.debe) if c.debe is not None else None,
                haber=float(c.haber) if c.haber is not None else None,
                saldo=float(c.saldo) if c.saldo is not None else None
            ) for c in result
        ]

    @strawberry.field
    def cc_proveedor(self, id_cc_proveedor: int) -> Optional[CCProveedorType]:
        db = SessionLocal()
        c = get_cc_proveedor(db, id_cc_proveedor)
        db.close()
        if not c:
            return None
        return CCProveedorType(
            id_cc_proveedor=c.id_cc_proveedor,
            id_proveedor=c.id_proveedor,
            fecha=c.fecha,
            tipo=c.tipo,
            id_comprobante=c.id_comprobante,
            detalle=c.detalle,
            debe=float(c.debe) if c.debe is not None else None,
            haber=float(c.haber) if c.haber is not None else None,
            saldo=float(c.saldo) if c.saldo is not None else None
        )
