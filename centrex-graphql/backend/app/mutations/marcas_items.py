import strawberry
from typing import Optional
from app.schemas.marcas_items import MarcaItemType, MarcaItemInput
from app.db import SessionLocal
from app.crud.marcas_items import create_marca_item, update_marca_item, delete_marca_item

@strawberry.type
class MarcaItemMutations:
    @strawberry.mutation
    def create_marca_item(self, data: MarcaItemInput) -> MarcaItemType:
        db = SessionLocal()
        new_obj = create_marca_item(db, data.__dict__)
        db.close()
        return MarcaItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_marca_item(self, id_marca: int, data: MarcaItemInput) -> Optional[MarcaItemType]:
        db = SessionLocal()
        updated = update_marca_item(db, id_marca, data.__dict__)
        db.close()
        if not updated:
            return None
        return MarcaItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_marca_item(self, id_marca: int) -> bool:
        db = SessionLocal()
        result = delete_marca_item(db, id_marca)
        db.close()
        return result
