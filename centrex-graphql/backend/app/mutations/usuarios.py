import strawberry
from typing import Optional
from app.schemas.usuarios import UsuarioType, UsuarioInput
from app.db import SessionLocal
from app.crud.usuarios import (
    create_usuario,
    update_usuario,
    delete_usuario,
    get_usuarios_by_id,
)
from app.auth import authenticate_user, create_access_token

@strawberry.type
class UsuarioMutations:
    @strawberry.mutation
    def create_usuario(self, data: UsuarioInput) -> UsuarioType:
        db = SessionLocal()
        new_obj = create_usuario(db, data)
        db.close()
        return UsuarioType(**new_obj.__dict__)

    @strawberry.mutation
    def update_usuario(self, id_usuario: int, data: UsuarioInput) -> Optional[UsuarioType]:
        db = SessionLocal()
        db_obj = get_usuarios_by_id(db, id_usuario)    # <--- Buscar el objeto primero
        if not db_obj:
            db.close()
            return None
        updated = update_usuario(db, db_obj, data)     # <--- Pasar el objeto y los updates
        db.close()
        return UsuarioType(**updated.__dict__)

    @strawberry.mutation
    def delete_usuario(self, id_usuario: int) -> bool:
        db = SessionLocal()
        db_obj = get_usuarios_by_id(db, id_usuario)    # <--- Buscar el objeto primero
        if not db_obj:
            db.close()
            return False
        delete_usuario(db, db_obj)                     # <--- Pasar el objeto
        db.close()
        return True

    @strawberry.mutation
    def login(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return an access token."""
        db = SessionLocal()
        user = authenticate_user(db, username, password)
        if not user:
            db.close()
            return None
        token = create_access_token({"sub": user.usuario})
        db.close()
        return token

