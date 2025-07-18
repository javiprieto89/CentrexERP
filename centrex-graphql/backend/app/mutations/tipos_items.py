import strawberry
from typing import Optional
from app.schemas.tipos_items import TipoItemType, TipoItemInput
from app.db import SessionLocal
from app.crud.tipos_items import create_tipo_item, update_tipo_item, delete_tipo_item

@strawberry.type
class TipoItemMutations:
    @strawberry.mutation
    def create_tipo_item(self, data: TipoItemInput) -> TipoItemType:
        db = SessionLocal()
        new_obj = create_tipo_item(db, data.__dict__)
        db.close()
        return TipoItemType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tipo_item(self, id_tipoItem: int, data: TipoItemInput) -> Optional[TipoItemType]:
        db = SessionLocal()
        updated = update_tipo_item(db, id_tipoItem, data.__dict__)
        db.close()
        if not updated:
            return None
        return TipoItemType(**updated.__dict__)

    @strawberry.mutation
    def delete_tipo_item(self, id_tipoItem: int) -> bool:
        db = SessionLocal()
        result = delete_tipo_item(db, id_tipoItem)
        db.close()
        return result