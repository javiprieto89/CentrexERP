import strawberry
from typing import Optional
from app.schemas.usuarios_perfiles import UsuarioPerfilType, UsuarioPerfilInput
from app.db import SessionLocal
from app.crud.usuarios_perfiles import create_usuario_perfil, update_usuario_perfil, delete_usuario_perfil

@strawberry.type
class UsuarioPerfilMutations:
    @strawberry.mutation
    def create_usuario_perfil(self, data: UsuarioPerfilInput) -> UsuarioPerfilType:
        db = SessionLocal()
        new_obj = create_usuario_perfil(db, data.__dict__)
        db.close()
        return UsuarioPerfilType(**new_obj.__dict__)

    @strawberry.mutation
    def update_usuario_perfil(self, id_usuarioPerfil: int, data: UsuarioPerfilInput) -> Optional[UsuarioPerfilType]:
        db = SessionLocal()
        updated = update_usuario_perfil(db, id_usuarioPerfil, data.__dict__)
        db.close()
        if not updated:
            return None
        return UsuarioPerfilType(**updated.__dict__)

    @strawberry.mutation
    def delete_usuario_perfil(self, id_usuarioPerfil: int) -> bool:
        db = SessionLocal()
        result = delete_usuario_perfil(db, id_usuarioPerfil)
        db.close()
        return result