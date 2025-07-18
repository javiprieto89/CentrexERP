import strawberry
from typing import List, Optional
from app.schemas.marcas_items import MarcaItemType
from app.db import SessionLocal
from app.crud.marcas_items import get_marca_item, get_marcas_items

@strawberry.type
class MarcaItemQueries:
    @strawberry.field
    def marcas_items(self, skip: int = 0, limit: int = 100) -> List[MarcaItemType]:
        db = SessionLocal()
        result = get_marcas_items(db, skip=skip, limit=limit)
        db.close()
        return [
            MarcaItemType(
                id_marca=c.id_marca,
                nombre=c.nombre,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def marca_item(self, id_marca: int) -> Optional[MarcaItemType]:
        db = SessionLocal()
        c = get_marca_item(db, id_marca)
        db.close()
        if not c:
            return None
        return MarcaItemType(
            id_marca=c.id_marca,
            nombre=c.nombre,
            descripcion=c.descripcion
        )
