import strawberry
from typing import List, Optional
from app.schemas.empresa import EmpresaType
from app.db import SessionLocal
from app.crud.empresa import get_empresa, get_empresas

@strawberry.type
class EmpresaQueries:
    @strawberry.field
    def empresas(self, skip: int = 0, limit: int = 100) -> List[EmpresaType]:
        db = SessionLocal()
        result = get_empresas(db, skip=skip, limit=limit)
        db.close()
        return [
            EmpresaType(
                id_empresa=c.id_empresa,
                razon_social=c.razon_social,
                cuit=c.cuit,
                direccion=c.direccion,
                telefono=c.telefono,
                email=c.email
            ) for c in result
        ]

    @strawberry.field
    def empresa(self, id_empresa: int) -> Optional[EmpresaType]:
        db = SessionLocal()
        c = get_empresa(db, id_empresa)
        db.close()
        if not c:
            return None
        return EmpresaType(
            id_empresa=c.id_empresa,
            razon_social=c.razon_social,
            cuit=c.cuit,
            direccion=c.direccion,
            telefono=c.telefono,
            email=c.email
        )
