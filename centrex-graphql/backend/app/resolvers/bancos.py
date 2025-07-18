import strawberry
from typing import List, Optional
from app.schemas.bancos import BancoType
from app.db import SessionLocal
from app.crud.bancos import get_banco, get_bancos

@strawberry.type
class BancoQueries:
    @strawberry.field
    def bancos(self, skip: int = 0, limit: int = 100) -> List[BancoType]:
        db = SessionLocal()
        result = get_bancos(db, skip=skip, limit=limit)
        db.close()
        return [
            BancoType(
                id_banco=b.id_banco,
                nombre=b.nombre,
                activo=b.activo
            ) for b in result
        ]

    @strawberry.field
    def banco(self, id_banco: int) -> Optional[BancoType]:
        db = SessionLocal()
        b = get_banco(db, id_banco)
        db.close()
        if not b:
            return None
        return BancoType(
            id_banco=b.id_banco,
            nombre=b.nombre,
            activo=b.activo
        )
