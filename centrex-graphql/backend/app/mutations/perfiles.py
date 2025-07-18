import strawberry
from typing import Optional
from app.schemas.perfiles import PerfilType, PerfilInput
from app.db import SessionLocal
from app.crud.perfiles import create_perfil, update_perfil, delete_perfil

@strawberry.type
class PerfilMutations:
    @strawberry.mutation
    def create_perfil(self, data: PerfilInput) -> PerfilType:
        db = SessionLocal()
        new_obj = create_perfil(db, data.__dict__)
        db.close()
        return PerfilType(**new_obj.__dict__)

    @strawberry.mutation
    def update_perfil(self, id_perfil: int, data: PerfilInput) -> Optional[PerfilType]:
        db = SessionLocal()
        updated = update_perfil(db, id_perfil, data.__dict__)
        db.close()
        if not updated:
            return None
        return PerfilType(**updated.__dict__)

    @strawberry.mutation
    def delete_perfil(self, id_perfil: int) -> bool:
        db = SessionLocal()
        result = delete_perfil(db, id_perfil)
        db.close()
        return result
